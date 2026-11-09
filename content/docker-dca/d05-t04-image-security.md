---
title: Keamanan image
minutes: 22
level: Menengah
badge: lengkap
summary: Base image minimal, scanning, non-root, dan pin digest.
objectives:
  - Mengecilkan permukaan serangan image
  - Memindai kerentanan
  - Menjalankan sebagai non-root
---
## Konsep inti
```bash
docker scan myrepo/api:1.0          # bila plugin tersedia
docker scout quickview myrepo/api:1.0
docker image inspect --format '{{.Config.User}}' myrepo/api:1.0
```

Praktik:
- Pilih base minimal (`alpine`, `distroless`, `scratch`).
- `USER` non-root di Dockerfile.
- Pin versi/digest, jangan `latest`.
- Buang tool build dari image akhir (multi-stage).
- Pindai dan perbarui base secara berkala.

## Jebakan
- Image kecil belum tentu bebas CVE (paket tetap bisa rentan).
- `docker scan` memerlukan autentikasi/plugin; `docker scout` alternatif di versi baru.
- Menjalankan sebagai root memperbesar dampak bila container tertembus.
- Cache build bisa menyimpan rahasia (`ARG` password) — jangan taruh secret di layer.

## Latihan
1. Mengapa rahasia tidak boleh lewat ARG/ENV?
2. Cara memastikan versi image tetap sama?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena tersimpan pada layer/image dan terlihat lewat <code>docker history</code>/<code>inspect</code>.</p>
<p><b>2.</b> Pin digest <code>@sha256:...</code> atau tag versi yang immutable.</p>
</details>
