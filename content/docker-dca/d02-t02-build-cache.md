---
title: Build context dan layer caching
minutes: 22
level: Menengah
badge: lengkap
summary: Urutan instruksi, invalidasi cache, dan .dockerignore.
objectives:
  - Menjelaskan cara cache layer bekerja
  - Mengatur urutan agar build cepat
  - Mengurangi ukuran context
---
## Konsep inti
Setiap instruksi menghasilkan layer; cache dipakai bila instruksi dan input-nya identik. `COPY`/`ADD` memakai checksum isi file, sehingga perubahan satu file membatalkan cache untuk instruksi itu dan semua setelahnya.

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./        # jarang berubah -> cache awet
RUN npm ci
COPY . .                     # sering berubah -> ditaruh akhir
RUN npm run build
```

```bash
docker build -t app:1.0 .
docker build --no-cache -t app:1.0 .
docker build --target builder -t app:builder .
```

`.dockerignore` mengurangi context:

```text
node_modules
.git
*.log
```

## Jebakan
- `RUN apt-get update` dan `apt-get install` dalam satu layer; dipisah bisa memakai cache usang.
- Menyalin seluruh direktori sebelum `npm ci` membuat cache selalu batal.
- Context besar memperlambat build walau layer di-cache (dikirim ke daemon).
- `--no-cache` memaksa semua instruksi dijalankan ulang.

## Latihan
1. Mengapa `COPY . .` sebaiknya di akhir?
2. Berkas untuk mengecualikan file dari context?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agar perubahan kode tidak membatalkan cache langkah instalasi dependensi.</p>
<p><b>2.</b> <code>.dockerignore</code>.</p>
</details>
