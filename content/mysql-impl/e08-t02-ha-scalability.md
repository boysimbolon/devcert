---
title: Fitur ketersediaan tinggi dan skalabilitas
minutes: 20
level: Menengah
badge: lengkap
summary: Failover, read scaling, thread pool, dan pola arsitektur pendukung.
objectives:
  - Membedakan HA dan skalabilitas
  - Menjelaskan peran Router dan replica
  - Menyebutkan fitur yang menaikkan kapasitas koneksi
---
## Kenapa topik ini diuji
Soal membedakan dua tujuan: tetap hidup (HA) vs menangani beban (skalabilitas).

## Konsep inti
| Tujuan | Mekanisme |
|---|---|
| HA | Group Replication + Router + quorum |
| Read scaling | replica + Router mode baca-saja |
| Write scaling | sharding aplikasi / multi-primary (hati-hati konflik) |
| Connection scaling | Thread Pool (Enterprise) |
| Geographic | replica di region lain |

```ini
[mysqld]
thread_handling = pool-of-threads
thread_pool_size = 16
```

Rumus kasar kapasitas koneksi:

```text
thread_pool_size ~ jumlah core
pool aplikasi total < max_connections
```

## Jebakan
- Menambah replica tidak menambah kapasitas tulis.
- Multi-primary memindahkan konflik ke lapisan aplikasi.
- Thread Pool bukan pengganti query yang efisien.
- Failover tanpa Router/orchestrator = manual.

## Latihan
1. Fitur Enterprise untuk banyak koneksi?
2. Apakah menambah replica menambah kapasitas tulis?

<details><summary>Jawaban</summary>
<p><b>1.</b> Thread Pool (<code>thread_handling=pool-of-threads</code>).</p>
<p><b>2.</b> Tidak; replica hanya menambah kapasitas baca.</p>
</details>
