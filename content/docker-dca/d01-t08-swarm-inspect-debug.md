---
title: Inspeksi dan troubleshooting swarm
minutes: 20
level: Menengah
badge: lengkap
summary: Membaca status task, log, dan penyebab task pending atau restart.
objectives:
  - Mendiagnosis task pending
  - Membaca riwayat task
  - Menggunakan log service
---
## Konsep inti
```bash
docker service ps --no-trunc web      # Error kolom menunjukkan penyebab
docker service logs --tail 50 web
docker node ls
docker node inspect --pretty node1 | head -40
docker system df
docker events --filter type=service
```

Penyebab umum task gagal:

| Pesan | Arti |
|---|---|
| `no suitable node` | constraint/label tidak cocok |
| `image not found` | registry/tag salah atau butuh login |
| `port already in use` | publish mode host bentrok |
| `unhealthy` | healthcheck gagal |
| `OOMKilled` | limit memori terlampaui |

## Jebakan
- Task `pending` bukan berarti cluster rusak; biasanya penjadwalan.
- Log service hanya dari task aktif; gunakan `--tail` agar tidak membanjiri terminal.
- Node `Down` tetap muncul; perlu `docker node rm` setelah yakin.
- Restart berulang bisa karena `restart_policy` + aplikasi crash (bukan masalah swarm).

## Latihan
1. Di mana kolom penyebab kegagalan task terlihat?
2. Arti `no suitable node`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Kolom <code>Error</code> pada <code>docker service ps</code>.</p>
<p><b>2.</b> Tidak ada node yang memenuhi constraint/resource.</p>
</details>
