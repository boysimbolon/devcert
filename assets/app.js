/* DevCert — progres, pencarian, navigasi */
(function () {
  "use strict";
  var KEY = "devcert.progress.v1";
  var body = document.body;
  var certId = body.dataset.cert || "";
  var topicId = body.dataset.topic || "";

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { return {}; }
  }
  function save(obj) {
    try { localStorage.setItem(KEY, JSON.stringify(obj)); } catch (e) {}
  }
  var progress = load();

  /* ---------- progress ring (global) ---------- */
  function updateGlobal() {
    var total = 0, done = 0;
    document.querySelectorAll("[data-topic]").forEach(function (el) {
      if (el.classList.contains("topic-link") || el.tagName === "LI") total += 1;
    });
    document.querySelectorAll(".topic-link[data-topic]").forEach(function (el) {
      if (progress[el.dataset.topic]) done += 1;
    });
    var totalAll = window.__TOTAL_TOPICS__ || null;
    var ring = document.getElementById("ring");
    var pctEl = document.getElementById("progressPct");
    if (!ring) return;
    var keys = Object.keys(progress).length;
    var denom = totalAll || 35;
    var pct = Math.min(100, Math.round((keys / denom) * 100));
    ring.style.strokeDashoffset = String(97.4 - (97.4 * pct) / 100);
    if (pctEl) pctEl.textContent = pct + "%";
  }

  /* ---------- sidebar + list ticks ---------- */
  function paintTicks() {
    document.querySelectorAll("[data-topic]").forEach(function (el) {
      var k = el.dataset.topic;
      if (progress[k]) el.classList.add("done"); else el.classList.remove("done");
    });
  }

  /* ---------- topic page: mark done ---------- */
  var btn = document.getElementById("markDone");
  if (btn && certId && topicId) {
    var key = certId + "/" + topicId;
    function reflect() {
      var on = !!progress[key];
      btn.classList.toggle("done", on);
      btn.textContent = on ? "✓ Sudah dipelajari — klik untuk batal" : "Tandai sudah dipelajari";
    }
    btn.addEventListener("click", function () {
      if (progress[key]) delete progress[key]; else progress[key] = 1;
      save(progress); reflect(); paintTicks(); updateGlobal(); updateCertBar();
    });
    reflect();
  }

  /* ---------- cert page: progress bar ---------- */
  function updateCertBar() {
    var bar = document.getElementById("certBar");
    if (!bar) return;
    var items = document.querySelectorAll(".topic-list li[data-topic]");
    if (!items.length) return;
    var done = 0;
    items.forEach(function (li) { if (progress[li.dataset.topic]) done += 1; });
    bar.style.width = Math.round((done / items.length) * 100) + "%";
    var txt = document.getElementById("certProgressText");
    if (txt) txt.textContent = done + " dari " + items.length + " topik";

    // progres per domain
    document.querySelectorAll(".dprog").forEach(function (el) {
      var block = el.closest(".dom-block");
      if (!block) return;
      var lis = block.querySelectorAll(".topic-list li[data-topic]");
      var d = 0;
      lis.forEach(function (li) { if (progress[li.dataset.topic]) d += 1; });
      if (d > 0) { el.textContent = d + "/" + lis.length; } else { el.classList.add("empty"); }
    });
  }

  paintTicks(); updateGlobal(); updateCertBar();

  /* ---------- copy buttons ---------- */
  document.querySelectorAll(".copy").forEach(function (b) {
    b.addEventListener("click", function () {
      var code = b.closest(".code").querySelector("code");
      var text = code ? code.innerText : "";
      var done = function () {
        b.textContent = "✓";
        setTimeout(function () { b.textContent = "copy"; }, 1200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, done);
      } else {
        var ta = document.createElement("textarea");
        ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); } catch (e) {}
        document.body.removeChild(ta); done();
      }
    });
  });

  /* ---------- search ---------- */
  var wrap = document.getElementById("searchWrap");
  var input = document.getElementById("searchInput");
  var results = document.getElementById("searchResults");
  var idx = null, loading = false;

  function openSearch() {
    if (!wrap) return;
    wrap.hidden = false;
    input.value = "";
    results.innerHTML = "";
    input.focus();
    if (!idx && !loading) {
      loading = true;
      fetch("/search.json").then(function (r) { return r.json(); }).then(function (d) {
        idx = d; loading = false;
        if (input.value) render(input.value);   // render ulang setelah index siap
      }).catch(function () { loading = false; });
    }
  }
  function closeSearch() { if (wrap) wrap.hidden = true; }

  var searchBtn = document.getElementById("searchBtn");
  if (searchBtn) searchBtn.addEventListener("click", openSearch);
  var searchClose = document.getElementById("searchClose");
  if (searchClose) searchClose.addEventListener("click", closeSearch);
  if (wrap) wrap.addEventListener("click", function (e) { if (e.target === wrap) closeSearch(); });

  function render(q) {
    if (!idx) return;
    var needle = q.toLowerCase().trim();
    var hits = idx.filter(function (it) {
      if (!needle) return false;
      return (it.t + " " + it.d + " " + it.ct + " " + it.x).toLowerCase().indexOf(needle) !== -1;
    }).slice(0, 12);

    if (!needle) { results.innerHTML = '<li class="empty">Ketik kata kunci: <b>JPA</b>, <b>servlet</b>, <b>JMS</b>, <b>Batch</b>…</li>'; return; }
    if (!hits.length) { results.innerHTML = '<li class="empty">Tidak ada hasil untuk “' + q + '”</li>'; return; }

    results.innerHTML = hits.map(function (it) {
      return '<li><a href="' + it.u + '"><div class="sc">' + it.ct + " · " + it.d +
        '</div><div class="st">' + it.t + '</div><div class="sd">' +
        it.x.slice(0, 110).replace(/</g, "&lt;") + '…</div></a></li>';
    }).join("");
  }

  if (input) input.addEventListener("input", function () { render(input.value); });

  document.addEventListener("keydown", function (e) {
    var tag = (e.target.tagName || "").toLowerCase();
    if (e.key === "/" && tag !== "input" && tag !== "textarea") { e.preventDefault(); openSearch(); }
    if (e.key === "Escape") closeSearch();
  });

  /* ---------- keyboard prev/next ---------- */
  document.addEventListener("keydown", function (e) {
    var tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea" || !wrap || !wrap.hidden) return;
    if (e.key === "ArrowLeft") {
      var p = document.querySelector(".pager a.prev"); if (p) location.href = p.href;
    }
    if (e.key === "ArrowRight") {
      var n = document.querySelector(".pager a.next"); if (n) location.href = n.href;
    }
  });

  /* ---------- keep active topic visible ---------- */
  var active = document.querySelector(".topic-link.active");
  if (active && active.scrollIntoView) {
    active.scrollIntoView({ block: "center" });
  }
})();
