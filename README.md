# DevCert — situs belajar sertifikasi

Generator situs statis untuk materi belajar sertifikasi IT dalam bahasa Indonesia, lengkap dengan bank soal dan simulasi ujian ber-timer.

Live: https://belajar.43.157.209.184.nip.io

## Isi

11 jalur, 392 halaman materi, 593 soal latihan:

| Jalur | Kode | Topik | Soal |
|---|---|---|---|
| Java EE 7 Application Developer | 1Z0-895 | 39 | 58 |
| TOEFL iBT (metode Longman, format 2026) | — | 30 | 50 |
| MySQL 8.0 Database Administrator | 1Z0-908 | 47 | 56 |
| MySQL 8.0 Database Developer | 1Z0-909 | 32 | 46 |
| MySQL Implementation Associate | 1Z0-922 | 22 | 41 |
| Oracle Database SQL | 1Z0-071 | 59 | 68 |
| Oracle 19c Performance Management & Tuning | 1Z0-084 | 46 | 62 |
| Oracle AI Database@AWS Architect Professional | 1Z0-1146 | 24 | 47 |
| Oracle Java SE 17 Developer | 1Z0-829 | 28 | 55 |
| Docker Certified Associate | DCA | 40 | 55 |
| Certified Kubernetes Application Developer | CKAD | 25 | 55 |

## Struktur

```
build.py                 generator statis (Python stdlib, tanpa dependensi)
assets/style.css         styling, termasuk mode ujian
assets/app.js            navigasi, progress per topik (localStorage), pencarian
assets/quiz.js           mesin ujian: timer, grid soal, penilaian per domain, pembahasan
content/certs.json       katalog jalur, domain, topik, roadmap
content/<cert>/*.md      materi per topik (frontmatter + markdown)
content/quiz/<cert>.json bank soal
out/                     hasil build (tidak di-commit)
```

Format frontmatter topik:

```yaml
---
title: Judul topik
minutes: 20
level: Dasar | Menengah | Lanjutan
badge: lengkap
summary: Satu paragraf ringkas.
objectives:
  - Tujuan pembelajaran pertama
  - Tujuan kedua
---
```

Setiap topik memakai bagian tetap: `## Kenapa topik ini diuji`, `## Konsep inti`, `## Jebakan`, `## Latihan` dengan blok `<details><summary>Jawaban</summary>`.

## Build

```bash
python3 build.py          # hasil ke out/
```

Deploy (nginx menyajikan hasil build):

```bash
rm -rf /var/www/blog && mkdir -p /var/www/blog && cp -a out/. /var/www/blog/
```

## Menambah jalur sertifikasi

1. Buat `content/<cert-id>/` dan tulis file topik sesuai format di atas.
2. Tambahkan entri ke `content/certs.json` — sertakan `domains` dengan `topics` yang `file`-nya cocok.
3. Tambahkan `content/quiz/<cert-id>.json` dengan soal berbobot sesuai persentase domain ujian.
4. Jalankan `python3 build.py`, lalu cek halaman `/sertifikasi/<cert-id>/` dan `/sertifikasi/<cert-id>/ujian/`.

## Catatan

- Materi disusun mengikuti silabus resmi vendor; kode ujian, jumlah soal, durasi, dan nilai lulus diambil dari sumber penyelenggara.
- Contoh kode yang punya klaim output dijalankan sungguhan saat penulisan (JDK untuk materi Java, kluster Kubernetes untuk manifest CKAD, Docker untuk materi container).
- Ambang nilai pada simulasi ujian bukan pengganti nilai resmi bila berbeda; lihat catatan di tiap halaman ujian.
