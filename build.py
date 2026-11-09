#!/usr/bin/env python3
"""Static site builder untuk situs belajar sertifikasi developer.

Input : content/certs.json + content/<cert>/*.md (frontmatter + markdown)
Output: out/  -> disajikan nginx sebagai /var/www/blog

Jalankan: python3 build.py
"""
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT = ROOT / "out"
ASSETS = ROOT / "assets"

SITE = {
    "name": "DevCert",
    "tagline": "Dari pemula sampai lulus sertifikasi",
    "base": "",
}

# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text: str):
    meta = {}
    body = text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        key = None
        for raw in fm.strip().splitlines():
            line = raw.rstrip()
            if not line.strip():
                continue
            if re.match(r"^\s+-\s+", line) and key:
                if not isinstance(meta.get(key), list):
                    continue          # item list yatim di bawah key non-list: lewati
                meta[key].append(line.split("-", 1)[1].strip().strip('"'))
                continue
            if ":" not in line:
                continue          # baris tanpa kolom diabaikan, bukan crash
            if ":" in line:
                k, v = line.split(":", 1)
                key = k.strip()
                v = v.strip().strip('"')
                meta[key] = v if v else []
    return meta, body.strip()

# ------------------------------------------------------------------- markdown
CODE_RE = re.compile(r"```([a-zA-Z0-9+#-]*)\n(.*?)```", re.S)
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")

def _inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = INLINE_CODE_RE.sub(r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", s)
    return s

def md_to_html(text: str) -> str:
    blocks, codes = [], []

    def stash(m):
        lang = (m.group(1) or "text").strip()
        code = html.escape(m.group(2).rstrip("\n"))
        idx = len(codes)
        codes.append(
            f'<div class="code" data-lang="{lang}"><div class="code-head"><span>{lang}</span>'
            f'<button class="copy" type="button">copy</button></div>'
            f'<pre><code>{code}</code></pre></div>'
        )
        return f"\x00CODE{idx}\x00"

    text = CODE_RE.sub(stash, text)
    lines = text.split("\n")
    out, i = [], 0

    def flush_para(buf):
        if buf:
            out.append("<p>" + _inline(" ".join(buf)) + "</p>")
            buf.clear()

    para = []
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s.startswith("\x00CODE"):
            flush_para(para)
            out.append(s)
            i += 1
            continue

        if not s:
            flush_para(para)
            i += 1
            continue

        # raw html passthrough (details/summary/div)
        if s.startswith("<"):
            flush_para(para)
            chunk = [line]
            depth = s.count("<details") - s.count("</details")
            while depth > 0 and i + 1 < len(lines):
                i += 1
                chunk.append(lines[i])
                depth += lines[i].count("<details") - lines[i].count("</details")
            out.append("\n".join(chunk))
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush_para(para)
            lvl = len(m.group(1))
            txt = _inline(m.group(2))
            anchor = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
            out.append(f'<h{lvl} id="{anchor}">{txt}</h{lvl}>')
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,})$", s):
            flush_para(para)
            out.append("<hr>")
            i += 1
            continue

        if s.startswith(">"):
            flush_para(para)
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + _inline(" ".join(quote)) + "</blockquote>")
            continue

        if re.match(r"^[-*]\s+", s):
            flush_para(para)
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{_inline(x)}</li>" for x in items) + "</ul>")
            continue

        if re.match(r"^\d+\.\s+", s):
            flush_para(para)
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{_inline(x)}</li>" for x in items) + "</ol>")
            continue

        if s.startswith("|") and s.endswith("|"):
            flush_para(para)
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            if len(rows) >= 2 and set("".join(rows[1])) <= set("-: "):
                head, body = rows[0], rows[2:]
                t = "<table><thead><tr>" + "".join(f"<th>{_inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                for r in body:
                    t += "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
                out.append(t + "</tbody></table>")
            else:
                out.append("<p>" + _inline(" ".join("|".join(r) for r in rows)) + "</p>")
            continue

        para.append(s)
        i += 1

    flush_para(para)
    html_out = "\n".join(out)
    for idx, code in enumerate(codes):
        html_out = html_out.replace(f"\x00CODE{idx}\x00", code)
    return html_out

# ------------------------------------------------------------------- template
PAGE = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f2f4f7">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script>try{{var t=localStorage.getItem('devcert-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.setAttribute('data-theme',t);}}catch(e){{document.documentElement.setAttribute('data-theme','light');}}</script>
<link rel="stylesheet" href="/assets/style.css?v={ver}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%232460e0'/><text x='50' y='68' font-size='54' font-family='monospace' fill='white' text-anchor='middle'>D</text></svg>">
</head>
<body data-cert="{cert_id}" data-topic="{topic_id}">
<a class="skip" href="#main">Lewati ke konten</a>
<header class="top">
  <a class="brand" href="/"><span class="mark">D</span> DevCert <span class="dot" title="siap dipakai"></span></a>
  <button id="searchBtn" class="search-open" type="button">
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.6-3.6"/></svg>
    <span>Cari topik…</span> <kbd>/</kbd>
  </button>
  <div class="progress-mini" title="Progres belajar">
    <svg viewBox="0 0 36 36" aria-hidden="true"><circle class="bg" cx="18" cy="18" r="15.5"/><circle id="ring" class="fg" cx="18" cy="18" r="15.5"/></svg>
    <span id="progressPct">0%</span>
  </div>
  <button id="themeBtn" class="icon-btn" type="button" aria-label="Ganti tema terang atau gelap" title="Ganti tema">
    <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>
    <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8Z"/></svg>
  </button>
</header>
<div class="shell{shelld}">
  <aside class="side">{sidebar}</aside>
  <main id="main">{content}</main>
</div>
<div id="searchWrap" class="search-wrap" hidden>
  <div class="search-box">
    <input id="searchInput" type="search" placeholder="Cari: JPA, servlet, JMS, batch…" autocomplete="off">
    <button id="searchClose" type="button">tutup</button>
  </div>
  <ul id="searchResults" class="search-results"></ul>
</div>
<footer class="foot">
  <span>DevCert — dibuat untuk belajar mandiri, dalam bahasa Indonesia.</span>
  <span>Progres disimpan di browser kamu (localStorage).</span>
  <span><a href="https://boyfsimbolon.netlify.app/devcert">Portofolio pembuatnya →</a></span>
</footer>
<script>window.__TOTAL_TOPICS__={total};</script>
<script src="/assets/app.js?v={ver}" defer></script>
</body>
</html>"""

def render_sidebar(certs, active_cert=None, active_topic=None):
    parts = ['<nav class="nav">']
    for c in certs:
        cls = "cert-link" + (" active" if c["id"] == active_cert else "")
        badge = f'<span class="chip">{c.get("badge","")}</span>' if c.get("badge") else ""
        if c.get("status") == "soon":
            parts.append(f'<a class="{cls} soon" href="/sertifikasi/{c["id"]}/">{html.escape(c["title"])}{badge}</a>')
            continue
        parts.append(f'<a class="{cls}" href="/sertifikasi/{c["id"]}/">{html.escape(c["title"])}{badge}</a>')
        if c["id"] == active_cert:
            for d in c["domains"]:
                parts.append('<div class="dom">')
                parts.append(f'<span class="dom-title">{html.escape(d["title"])}</span><ul>')
                for t in d["topics"]:
                    a = "topic-link" + (" active" if t["id"] == active_topic else "")
                    ok = f' data-topic="{c["id"]}/{t["id"]}"'
                    parts.append(
                        f'<li><a class="{a}" href="/sertifikasi/{c["id"]}/{d["slug"]}/{t["slug"]}/"{ok}>'
                        f'<span class="tick" aria-hidden="true"></span>{html.escape(t["title"])}</a></li>'
                    )
                parts.append("</ul></div>")
    parts.append("</nav>")
    return "".join(parts)

def domain_count(d):
    return len(d["topics"]) if d.get("topics") else len(d.get("syllabus", []))

def cert_count(c):
    return sum(domain_count(d) for d in c["domains"])

def total_topics(certs):
    return sum(cert_count(c) for c in certs)

def write_page(path: Path, title, desc, content, sidebar, cert_id="", topic_id="", no_side=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if no_side:
        sidebar = ""
        shelld = " no-side"
    else:
        shelld = ""
    path.write_text(PAGE.format(title=title, desc=html.escape(desc), content=content,
                                sidebar=sidebar, cert_id=cert_id, topic_id=topic_id,
                                shelld=shelld, total=TOTAL_TOPICS, ver=VERSION),
                    encoding="utf-8")

# ----------------------------------------------------------------------- pages
def load_certs():
    data = json.loads((CONTENT / "certs.json").read_text(encoding="utf-8"))
    return data["certs"] if isinstance(data, dict) else data

def build_topic_page(cert, domain, topic, prev_t, next_t):
    md = (CONTENT / cert["id"] / topic["file"]).read_text(encoding="utf-8")
    meta, body = parse_frontmatter(md)
    body_html = md_to_html(body)
    objectives = meta.get("objectives", [])
    obj_html = ""
    if isinstance(objectives, str):
        objectives = [objectives]
    if objectives:
        obj_html = ('<div class="objectives"><h2>Tujuan pembelajaran</h2><ul>'
                    + "".join(f"<li>{_inline(o)}</li>" for o in objectives) + "</ul></div>")

    badge = meta.get("badge", "lengkap")
    badge_html = f'<span class="badge b-{badge}" title="Kelayakan materi, bukan progres belajar">materi {badge}</span>'
    minutes = meta.get("minutes", "20")
    level = meta.get("level", "Dasar")

    nav = ['<nav class="pager">']
    nav.append(f'<a class="prev" href="{prev_t["url"]}"><span>← Sebelumnya</span><b>{html.escape(prev_t["title"])}</b></a>'
               if prev_t else '<span class="prev disabled"><span>← Sebelumnya</span><b>Awal materi</b></span>')
    nav.append(f'<a class="next" href="{next_t["url"]}"><span>Selanjutnya →</span><b>{html.escape(next_t["title"])}</b></a>'
               if next_t else '<span class="next disabled"><span>Selanjutnya →</span><b>Selesai</b></span>')
    nav.append("</nav>")

    content = f"""
<div class="crumbs"><a href="/">Beranda</a> / <a href="/sertifikasi/{cert['id']}/">{html.escape(cert['title'])}</a> / <span>{html.escape(domain['title'])}</span></div>
<article class="doc">
  <div class="doc-head">
    <div class="meta-row">{badge_html}<span class="meta">⏱ {minutes} menit</span><span class="meta">📊 {level}</span></div>
    <h1>{html.escape(topic["title"])}</h1>
    <p class="domain-tag">{html.escape(domain["title"])}</p>
  </div>
  {obj_html}
  <div class="prose">{body_html}</div>
  <div class="done-box">
    <button id="markDone" class="btn-done" type="button">Tandai sudah dipelajari</button>
    <span class="hint">Progres tersimpan di browser ini.</span>
  </div>
  {''.join(nav)}
</article>"""
    return content, meta

def build_cert_page(cert):
    total_min = sum(int(t.get("minutes", 20)) for d in cert["domains"] for t in d["topics"]) if cert.get("status") != "soon" else 0
    dom_html = []
    for n, d in enumerate(cert["domains"], 1):
        if d.get("topics"):
            topics = "".join(
                f'<li data-topic="{cert["id"]}/{t["id"]}"><a href="/sertifikasi/{cert["id"]}/{d["slug"]}/{t["slug"]}/">'
                f'<span class="tick" aria-hidden="true"></span><span class="t-title">{html.escape(t["title"])}</span>'
                f'<span class="t-min">{t.get("minutes",20)}m</span></a></li>'
                for t in d["topics"]
            )
        else:
            topics = "".join(
                f'<li class="plain"><span class="t-title">{html.escape(x)}</span>'
                f'<span class="t-min">segera</span></li>'
                for x in d.get("syllabus", [])
            )
        dom_html.append(f"""
<section class="dom-block" id="{d['slug']}">
  <header><span class="dn">{n:02d}</span><h2>{html.escape(d['title'])}</h2><span class="dprog" data-dom="{d['slug']}"></span><span class="dcount">{domain_count(d)} topik</span></header>
  <ul class="topic-list">{topics}</ul>
</section>""")

    facts = "".join(f'<div class="fact"><span>{html.escape(k)}</span><b>{html.escape(v)}</b></div>'
                    for k, v in cert.get("facts", {}).items())

    quiz_actions = ""
    if (QUIZ_DIR / f"{cert['id']}.json").exists():
        quiz_actions = ('<div class="cert-actions"><a class="btn primary" '
                        f'href="/sertifikasi/{cert["id"]}/ujian/">Mulai ujian latihan</a>'
                        '<span class="hint">Soal pilihan ganda, ada timer dan pembahasan.</span></div>')

    roadmap = ""
    if cert.get("roadmap"):
        steps = "".join(f"<li><b>{html.escape(s['week'])}</b><p>{html.escape(s['goal'])}</p></li>"
                        for s in cert["roadmap"])
        roadmap = f'<section class="roadmap"><h2>Rencana belajar</h2><ol class="weeks">{steps}</ol></section>'

    content = f"""
<div class="crumbs"><a href="/">Beranda</a> / <span>{html.escape(cert['title'])}</span></div>
<header class="cert-hero">
  <div class="cert-vendor">{html.escape(cert.get('vendor',''))} · {html.escape(cert.get('code',''))}</div>
  <h1>{html.escape(cert['title'])}</h1>
  <p class="lede">{html.escape(cert.get('desc',''))}</p>
  <div class="facts">{facts}</div>
  <div class="cert-progress"><div class="bar"><i id="certBar"></i></div><span id="certProgressText">0 dari {cert_count(cert)} topik</span></div>
  {quiz_actions}
  {('<div class="soon-note">Materi sertifikasi ini sedang disusun. Silabusnya sudah lengkap di bawah, jadi bisa dipakai sebagai checklist belajar.</div>' if cert.get("status") == "soon" else "")}
</header>
{roadmap}
<div class="domains">
  <h2 class="section-title">Silabus &amp; materi <span class="muted">({cert_count(cert)} topik{(' · ~' + str(total_min) + ' menit baca') if total_min else ''})</span></h2>
  {''.join(dom_html)}
</div>"""
    return content

QUIZ_DIR = CONTENT / "quiz"


def build_quiz_page(cert):
    data = json.loads((QUIZ_DIR / f"{cert['id']}.json").read_text(encoding="utf-8"))
    qs = data["questions"]
    per_dom = {}
    for q in qs:
        per_dom[q["d"]] = per_dom.get(q["d"], 0) + 1
    dom_titles = {d["slug"]: d["title"] for d in cert["domains"]}
    payload = json.dumps({"cert": cert["id"], "minutes": data.get("minutes", 60),
                          "pass": data.get("pass", 63),
                          "passLabel": data.get("passLabel", "nilai lulus"),
                          "domTitles": dom_titles,
                          "questions": qs}, ensure_ascii=False)
    rows = "".join(
        f'<div class="qmeta-row"><span>{html.escape(dom_titles.get(k, k))}</span><b>{v} soal</b></div>'
        for k, v in per_dom.items()
    )
    content = f"""
<div class="crumbs"><a href="/">Beranda</a> / <a href="/sertifikasi/{cert['id']}/">{html.escape(cert['title'])}</a> / <span>Ujian latihan</span></div>
<header class="cert-hero">
  <div class="cert-vendor">Simulasi ujian · {html.escape(cert.get('code',''))}</div>
  <h1>Ujian latihan: {html.escape(cert['title'])}</h1>
  <p class="lede">{len(qs)} soal pilihan ganda dari 14 domain, waktu {data.get('minutes',60)} menit, {data.get('passLabel','nilai lulus')} {data.get('pass',63)}%. Sama seperti ujian aslinya: tidak ada pembahasan sampai kamu submit.</p>
</header>

<div class="quiz" id="quiz">
  <section class="quiz-start" id="qStart">
    <div class="facts">
      <div class="fact"><span>Soal</span><b>{len(qs)}</b></div>
      <div class="fact"><span>Durasi</span><b>{data.get('minutes',60)} menit</b></div>
      <div class="fact"><span>{data.get('passLabel','Nilai lulus').capitalize()}</span><b>{data.get('pass',63)}%</b></div>
      <div class="fact"><span>Domain</span><b>{len(per_dom)}</b></div>
    </div>
    <div class="qmeta">{rows}</div>
    <button class="btn primary" id="startQuiz" type="button">Mulai ujian</button>
    <p class="hint">Jawaban bisa diubah sebelum submit. Waktu berjalan otomatis; saat habis, ujian dikumpulkan sendiri.</p>
  </section>

  <section class="quiz-run" id="qRun" hidden>
    <div class="qbar">
      <span class="qcount" id="qCount">Soal 1 / {len(qs)}</span>
      <span class="qtimer" id="qTimer">--:--</span>
      <button class="btn ghost small" id="qSubmit" type="button">Kumpulkan</button>
    </div>
    <div class="qbody">
      <p class="qdom" id="qDom"></p>
      <h2 class="qtext" id="qText"></h2>
      <div class="qopts" id="qOpts"></div>
    </div>
    <div class="qnav">
      <button class="btn ghost small" id="qPrev" type="button">← Sebelumnya</button>
      <button class="btn ghost small" id="qNext" type="button">Berikutnya →</button>
    </div>
    <div class="qgrid" id="qGrid"></div>
  </section>

  <section class="quiz-result" id="qResult" hidden></section>
</div>
<script id="quizData" type="application/json">{payload}</script>
<script src="/assets/quiz.js?v={VERSION}" defer></script>"""
    return content

def build_index(certs):
    cards = []
    for c in certs:
        n = cert_count(c)
        soon = c.get("status") == "soon"
        cards.append(f"""
<a class="card{' soon' if soon else ''}" href="/sertifikasi/{c['id']}/">
  <div class="card-top"><span class="card-code">{html.escape(c.get('code',''))}</span>{'<span class="chip soon-chip">segera</span>' if soon else ''}</div>
  <h3>{html.escape(c['title'])}</h3>
  <p>{html.escape(c.get('desc',''))}</p>
  <div class="card-foot"><span>{len(c['domains'])} domain · {n} topik</span><span>{html.escape(c.get('level',''))}</span></div>
</a>""")

    content = f"""
<section class="hero">
  <div class="hero-in">
    <span class="kicker">Belajar mandiri · bahasa Indonesia</span>
    <h1>Dari pemula sampai <em>lulus</em> sertifikasi dan tes kemampuan.</h1>
    <p class="lede">Materi disusun persis mengikuti topik yang diuji. Pilih jalur → pilih domain → pelajari per topik, dengan contoh, jebakan ujian, latihan, dan simulasi ujian.</p>
    <div class="hero-actions">
      <a class="btn primary" href="/sertifikasi/java-ee-7/">Mulai: Java EE 7</a>
      <a class="btn ghost" href="/cara-belajar/">Cara pakai situs ini</a>
    </div>
    <div class="hero-stats">
      <div><b>{len([c for c in certs if c.get('status')!='soon'])}</b><span>jalur siap</span></div>
      <div><b>{sum(cert_count(c) for c in certs if c.get("status") != "soon")}</b><span>topik siap</span></div>
      <div><b>100%</b><span>bahasa Indonesia</span></div>
    </div>
  </div>
</section>
<section class="certs">
  <h2 class="section-title">Pilih jalur sertifikasi</h2>
  <div class="cards">{''.join(cards)}</div>
</section>
<section class="how">
  <h2 class="section-title">Cara kerjanya</h2>
  <ol class="steps">
    <li><b>01</b><h3>Pilih sertifikasi</h3><p>Setiap sertifikasi dipetakan ke domain dan topik resmi yang diuji.</p></li>
    <li><b>02</b><h3>Belajar per topik</h3><p>Satu halaman = satu topik ujian: konsep, kode, jebakan, latihan.</p></li>
    <li><b>03</b><h3>Tandai selesai</h3><p>Progres tersimpan di browser, jadi kelihatan sisa materi yang belum disentuh.</p></li>
    <li><b>04</b><h3>Ulangi yang merah</h3><p>Kembali ke topik yang belum ditandai sebelum ujian.</p></li>
  </ol>
</section>"""
    return content

def build_howto(certs):
    content = """
<div class="crumbs"><a href="/">Beranda</a> / <span>Cara belajar</span></div>
<article class="doc">
  <h1>Cara memakai situs ini</h1>
  <div class="prose">
    <p>Situs ini bukan ringkasan semalam. Setiap halaman ditulis untuk satu topik ujian, dengan urutan yang sama seperti silabus resmi. Ikuti berurutan, jangan acak.</p>
    <h2>Urutan yang disarankan</h2>
    <ol>
      <li><b>Baca halaman sertifikasi dulu.</b> Pahami domain, bobot topik, dan rencana belajar per pekan.</li>
      <li><b>Kerjakan per domain, bukan per topik favorit.</b> Sertifikasi gagal biasanya karena satu domain terlewat, bukan karena kurang dalam.</li>
      <li><b>Setiap topik: baca → ketik ulang kodenya → jawab latihan tanpa lihat jawaban.</b> Mengetik ulang kode adalah cara tercepat menempelkan sintaks ke memori.</li>
      <li><b>Tandai selesai hanya kalau bisa menjelaskan topik itu ke orang lain.</b> Bukan karena halaman sudah dibaca.</li>
    </ol>
    <h2>Arti label pada tiap topik</h2>
    <ul>
      <li><b>lengkap</b> — materi penuh: konsep, kode, jebakan ujian, latihan.</li>
      <li><b>ringkas</b> — kerangka padat; cukup untuk mengingat, belum cukup untuk topik baru.</li>
      <li><b>segera</b> — silabus sudah dipetakan, materi menyusul.</li>
    </ul>
    <h2>Ritme yang realistis</h2>
    <p>Dua topik per hari, 45–60 menit per sesi, lima hari sepekan. Untuk Java EE 7 dengan 35 topik, itu sekitar empat pekan efektif — cocok dengan rencana belajar delapan pekan yang santai.</p>
    <blockquote>Aturan keras: jangan lanjut ke topik berikutnya sebelum bisa menuliskan contoh minimalnya tanpa membuka halaman.</blockquote>
    <h2>Keyboard</h2>
    <ul>
      <li><kbd>/</kbd> — buka pencarian</li>
      <li><kbd>←</kbd> <kbd>→</kbd> — topik sebelumnya / berikutnya</li>
      <li><kbd>Esc</kbd> — tutup pencarian</li>
    </ul>
  </div>
</article>"""
    return content

TOTAL_TOPICS = 39
VERSION = "1"


def main():
    global TOTAL_TOPICS, VERSION
    import hashlib
    h = hashlib.sha1()
    for f in ("style.css", "app.js"):
        h.update((ASSETS / f).read_bytes())
    VERSION = h.hexdigest()[:8]
    certs = load_certs()
    TOTAL_TOPICS = sum(cert_count(c) for c in certs if c.get("status") != "soon")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ASSETS, OUT / "assets")

    index = []
    # landing + static pages
    write_page(OUT / "index.html", "DevCert — Belajar sertifikasi & tes kemampuan",
               "Materi belajar mandiri untuk sertifikasi developer dalam bahasa Indonesia.",
               build_index(certs), "", no_side=True)
    write_page(OUT / "cara-belajar" / "index.html", "Cara belajar — DevCert",
               "Cara memakai situs belajar sertifikasi ini.", build_howto(certs), "", no_side=True)

    for cert in certs:
        cert_dir = OUT / "sertifikasi" / cert["id"]
        write_page(cert_dir / "index.html", f"{cert['title']} — DevCert",
                   cert.get("desc", ""), build_cert_page(cert),
                   render_sidebar(certs, cert["id"]), cert["id"])

        # flatten topics for prev/next
        flat = []
        for d in cert["domains"]:
            for t in d["topics"]:
                flat.append((d, t, f"/sertifikasi/{cert['id']}/{d['slug']}/{t['slug']}/"))

        qdir = cert_dir / "ujian"
        if not (QUIZ_DIR / f"{cert['id']}.json").exists():
            qdir = None
        else:
            qdir.mkdir(parents=True, exist_ok=True)
        if qdir:
          (qdir / "index.html").write_text(PAGE.format(
            title=f"Ujian latihan {cert['title']} — DevCert",
            desc=f"Simulasi ujian {cert['code']} dengan soal pilihan ganda dan pembahasan.",
            content=build_quiz_page(cert),
            sidebar="",
            cert_id=cert["id"], topic_id="", shelld=" no-side", total=TOTAL_TOPICS, ver=VERSION),
            encoding="utf-8")

        for i, (d, t, url) in enumerate(flat):
            prev_t = {"url": flat[i-1][2], "title": flat[i-1][1]["title"]} if i > 0 else None
            next_t = {"url": flat[i+1][2], "title": flat[i+1][1]["title"]} if i < len(flat)-1 else None
            body, meta = build_topic_page(cert, d, t, prev_t, next_t)
            page = OUT / "sertifikasi" / cert["id"] / d["slug"] / t["slug"] / "index.html"
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(PAGE.format(title=f"{t['title']} — {cert['title']}",
                                        desc=meta.get("summary", t["title"]),
                                        content=body,
                                        sidebar=render_sidebar(certs, cert["id"], t["id"]),
                                        cert_id=cert["id"], topic_id=t["id"], shelld="", total=TOTAL_TOPICS, ver=VERSION), encoding="utf-8")
            plain = re.sub(r"<[^>]+>", " ", md_to_html(parse_frontmatter(
                (CONTENT / cert["id"] / t["file"]).read_text(encoding="utf-8"))[1]))
            index.append({
                "c": cert["id"], "ct": cert["title"], "d": d["title"],
                "t": t["title"], "u": url,
                "x": re.sub(r"\s+", " ", plain)[:400],
            })

    (OUT / "search.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    qout = OUT / "quiz"
    qout.mkdir(parents=True, exist_ok=True)
    for f in QUIZ_DIR.glob("*.json"):
        shutil.copy2(f, qout / f.name)
    (OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print(f"built {len(index)} topic pages + landing + {len(certs)} cert pages -> {OUT}")

if __name__ == "__main__":
    main()
