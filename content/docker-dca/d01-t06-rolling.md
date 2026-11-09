---
title: Rolling update dan rollback
minutes: 22
level: Menengah
badge: lengkap
summary: Update bertahap tanpa downtime dan kembali ke versi sebelumnya.
objectives:
  - Mengatur parameter rolling update
  - Menjalankan pembaruan image
  - Melakukan rollback
---
## Konsep inti
```bash
docker service update \
  --image nginx:1.26 \
  --update-parallelism 2 \
  --update-delay 10s \
  --update-order start-first \
  --update-failure-action rollback \
  web

docker service rollback web
docker service inspect --format '{{json .UpdateStatus}}' web
```

| Parameter | Arti |
|---|---|
| `--update-parallelism` | jumlah task diganti bersamaan |
| `--update-delay` | jeda antar batch |
| `--update-order` | `stop-first` (default) atau `start-first` |
| `--update-failure-action` | `pause`, `continue`, `rollback` |
| `--update-monitor` | lama memantau kesehatan setelah start |

## Jebakan
- `--update-delay 10s` saja tidak cukup untuk menjamin siap; gunakan healthcheck.
- `start-first` butuh resource ekstra (dua versi hidup bersamaan).
- Rollback hanya tersedia bila service pernah di-update (menyimpan spec sebelumnya).
- `docker service scale` bukan update image; jangan tertukar.

## Latihan
1. Urutan mana yang menghindari downtime sementara?
2. Aksi bila task baru gagal dalam pembaruan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>start-first</code>.</p>
<p><b>2.</b> Atur <code>--update-failure-action rollback</code> agar otomatis kembali.</p>
</details>
