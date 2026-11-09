---
title: Healthcheck pada service
minutes: 18
level: Menengah
badge: lengkap
summary: Memeriksa kesehatan container dan dampaknya pada swarm.
objectives:
  - Menulis HEALTHCHECK di Dockerfile
  - Menimpa healthcheck saat run/service
  - Menjelaskan status unhealthy
---
## Konsep inti
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

```bash
docker run -d --health-cmd 'pg_isready' --health-interval 10s postgres:16
docker inspect --format '{{json .State.Health}}' <container>
docker service create --health-cmd 'curl -f localhost' --health-retries 3 nginx
```

Swarm tidak otomatis membunuh task `unhealthy`, tetapi statusnya terlihat di `docker service ps` dan dipakai saat update (`--update-monitor`).

## Jebakan
- `exit 1` menandai unhealthy; `exit 0` healthy. Kode lain = unhealthy.
- Tanpa `--start-period`, container yang lambat start bisa langsung dianggap gagal.
- Healthcheck menambah beban; jangan interval terlalu rapat.
- `docker ps` menampilkan status `(unhealthy)` hanya setelah retries habis.

## Latihan
1. Status yang terlihat bila semua retry gagal?
2. Direktif Dockerfile untuk healthcheck?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>unhealthy</code>.</p>
<p><b>2.</b> <code>HEALTHCHECK</code>.</p>
</details>
