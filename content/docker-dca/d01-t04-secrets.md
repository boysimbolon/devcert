---
title: Secret di swarm
minutes: 20
level: Menengah
badge: lengkap
summary: Menyimpan rahasia di Raft dan memasangnya ke container.
objectives:
  - Membuat dan memakai secret
  - Menjelaskan lokasi mount secret
  - Membedakan secret dan environment variable
---
## Konsep inti
```bash
printf 'S3cr3t!' | docker secret create db_password -
docker secret ls
docker secret inspect db_password
docker secret rm db_password

docker service create --name app --secret db_password alpine:3.20 \
  sh -c 'cat /run/secrets/db_password'
```

Secret di swarm:
- Disimpan **terenkripsi** di Raft log manajer.
- Hanya dikirim ke node yang menjalankan task terkait.
- Dipasang sebagai file di `/run/secrets/<nama>` (tmpfs, tidak di disk).

## Jebakan
- Secret tidak bisa di-update; buat baru lalu `docker service update --secret-rm lama --secret-add baru`.
- Secret hanya tersedia pada node **swarm manager** saat dibuat (perintah ditolak di worker).
- Environment variable terlihat di `docker inspect`; secret di file tidak.
- Nama secret bisa diberi target berbeda: `--secret source=db_password,target=pass`.

## Latihan
1. Di mana secret terlihat di dalam container?
2. Bisakah secret diperbarui di tempat?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>/run/secrets/nama_secret</code>.</p>
<p><b>2.</b> Tidak; ganti dengan secret baru melalui update service.</p>
</details>
