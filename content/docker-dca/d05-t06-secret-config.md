---
title: Secret, token, dan konfigurasi aman
minutes: 20
level: Menengah
badge: lengkap
summary: Menghindari rahasia di image dan memakai config object.
objectives:
  - Membedakan secret dan config
  - Menerapkan pola file-based secret
  - Menghindari kebocoran lewat build
---
## Konsep inti
```bash
docker config create nginx_conf ./nginx.conf
docker service create --name proxy --config source=nginx_conf,target=/etc/nginx/nginx.conf nginx

docker secret create tls_cert ./server.crt
docker service create --name tls --secret tls_cert nginx
```

| Objek | Terenkripsi | Lokasi |
|---|---|---|
| `secret` | ya (Raft) | `/run/secrets/<nama>` |
| `config` | tidak | `/nama` (default) |

Pola aman: aplikasi membaca file (`DB_PASSWORD_FILE=/run/secrets/db_password`), bukan env var yang muncul di `docker inspect`.

## Jebakan
- `config` tidak terenkripsi; jangan untuk password.
- Build arg/ENV berisi rahasia tersimpan di layer image selamanya.
- `docker service inspect` menampilkan nama secret, bukan isinya.
- Config tidak bisa diubah di tempat; buat baru dan update service.

## Latihan
1. Di mana config dipasang di container?
2. Mengapa ENV kurang aman dibanding secret?

<details><summary>Jawaban</summary>
<p><b>1.</b> Root filesystem container (default <code>/&lt;nama&gt;</code>).</p>
<p><b>2.</b> Karena nilainya terlihat di <code>docker inspect</code>, log, dan environment proses anak.</p>
</details>
