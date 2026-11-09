---
title: Multi-stage build
minutes: 22
level: Menengah
badge: lengkap
summary: Memisahkan tahap build dan runtime untuk image kecil.
objectives:
  - Menulis multi-stage Dockerfile
  - Menyalin artefak antar tahap
  - Menilai pengurangan ukuran image
---
## Konsep inti
```dockerfile
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /out/app

FROM alpine:3.20
COPY --from=builder /out/app /usr/local/bin/app
ENTRYPOINT ["app"]
```

```bash
docker build --target builder -t app:builder .
docker build -t app:final .
docker image ls app
```

Hasil: image akhir tidak memuat compiler/SDK, sehingga jauh lebih kecil dan permukaan serangannya berkurang.

## Jebakan
- `COPY --from` bisa merujuk nama tahap, indeks (`--from=0`), atau image eksternal.
- Image builder tetap tersimpan di cache, tetapi tidak dikirim saat push image final.
- Binary statis lebih aman untuk `scratch`/`alpine`; binary dinamis butuh libc.
- Lupa `AS <nama>` membuat referensi tahap harus memakai indeks.

## Latihan
1. Sintaks menyalin dari tahap sebelumnya?
2. Manfaat utama multi-stage?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>COPY --from=builder /path /tujuan</code>.</p>
<p><b>2.</b> Image runtime kecil tanpa toolchain build.</p>
</details>
