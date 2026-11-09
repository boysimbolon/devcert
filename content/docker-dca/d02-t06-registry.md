---
title: Menjalankan dan memakai registry
minutes: 22
level: Menengah
badge: lengkap
summary: Registry lokal, TLS, autentikasi dasar, dan alur push/pull.
objectives:
  - Menjalankan registry
  - Mengonfigurasi akses insecure atau TLS
  - Menguji push dan pull
---
## Konsep inti
```bash
docker run -d -p 5000:5000 --name registry \
  -v registry_data:/var/lib/registry registry:2

docker tag app:1.0 localhost:5000/app:1.0
docker push localhost:5000/app:1.0
curl http://localhost:5000/v2/_catalog
```

Untuk registry HTTP di host lain, daftarkan di `/etc/docker/daemon.json`:

```json
{ "insecure-registries": ["192.168.1.50:5000"] }
```

Autentikasi dasar dapat ditambahkan dengan `htpasswd` dan env `REGISTRY_AUTH`.

## Jebakan
- `localhost:5000` dianggap aman oleh Docker; IP/host lain dengan HTTP butuh `insecure-registries`.
- Tanpa TLS + auth, registry terbuka untuk siapa pun yang menjangkau port.
- Data registry hilang bila container dihapus tanpa volume.
- Nama image harus memuat host registry; kalau tidak, push menuju Docker Hub.

## Latihan
1. Endpoint untuk melihat daftar repository?
2. Mengapa push ke `1.2.3.4:5000` gagal tanpa konfigurasi tambahan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>/v2/_catalog</code>.</p>
<p><b>2.</b> Karena Docker menganggapnya insecure (HTTP) sehingga harus didaftarkan di <code>insecure-registries</code>.</p>
</details>
