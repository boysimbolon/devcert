---
title: Content trust dan signing image
minutes: 20
level: Menengah
badge: lengkap
summary: DOCKER_CONTENT_TRUST, kunci penandatangan, dan verifikasi.
objectives:
  - Mengaktifkan content trust
  - Menandatangani image
  - Menjelaskan akibat pada pull
---
## Konsep inti
```bash
export DOCKER_CONTENT_TRUST=1
docker push myrepo/api:1.0        # otomatis menandatangani
docker trust key generate bea
docker trust signer add --key bea.pub bea myrepo/api
docker trust inspect --pretty myrepo/api:1.0
```

Dengan `DOCKER_CONTENT_TRUST=1`:
- `push` menandatangani image (butuh passphrase root key),
- `pull` hanya menerima image bertanda tangan,
- image tanpa tanda tangan ditolak.

## Jebakan
- Hanya berlaku pada tag, bukan digest.
- Root key bersifat offline dan sangat penting; hilang = tidak bisa menandatangani lagi.
- Registry harus mendukung Notary (Docker Hub dan DTR mendukung).
- `latest` dan tag lain diperlakukan terpisah.

## Latihan
1. Variabel untuk mengaktifkan content trust?
2. Apa yang terjadi saat pull image tak bertanda tangan dengan trust aktif?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DOCKER_CONTENT_TRUST=1</code>.</p>
<p><b>2.</b> Pull ditolak karena tidak ada tanda tangan yang dapat diverifikasi.</p>
</details>
