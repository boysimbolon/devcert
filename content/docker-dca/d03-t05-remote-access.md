---
title: Akses daemon jarak jauh dan TLS
minutes: 22
level: Menengah
badge: lengkap
summary: DOCKER_HOST, sertifikat klien, dan port 2376.
objectives:
  - Mengaktifkan akses TCP
  - Mengamankan dengan TLS
  - Menguji koneksi klien
---
## Konsep inti
```bash
dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2376 \
  --tlsverify \
  --tlscacert=/etc/docker/ca.pem \
  --tlscert=/etc/docker/server-cert.pem \
  --tlskey=/etc/docker/server-key.pem

export DOCKER_HOST=tcp://10.0.0.5:2376
export DOCKER_TLS_VERIFY=1
export DOCKER_CERT_PATH=~/.docker
docker info
```

Atau lewat `daemon.json` dengan `"hosts": [..., "tcp://0.0.0.0:2376"]` dan `"tlsverify": true`.

## Jebakan
- Port 2375 = tanpa TLS; jangan dipakai di jaringan terbuka (setara root remote).
- Sertifikat klien harus memuat SAN/IP yang cocok, jika tidak verifikasi gagal.
- `DOCKER_HOST` tanpa `DOCKER_TLS_VERIFY` mengabaikan TLS.
- Firewall harus membuka 2376 hanya untuk jaringan admin.

## Latihan
1. Variabel untuk menunjuk daemon remote?
2. Mengapa 2375 berbahaya?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DOCKER_HOST</code>.</p>
<p><b>2.</b> Karena tanpa TLS dan memberi kendali penuh setara root kepada siapa pun yang bisa menjangkaunya.</p>
</details>
