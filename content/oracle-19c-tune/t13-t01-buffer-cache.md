---
title: Tuning buffer cache
minutes: 20
level: Menengah
badge: lengkap
summary: Membaca advisory, hit ratio, dan menyesuaikan ukuran cache.
objectives:
  - Menilai apakah buffer cache kurang
  - Memakai V$DB_CACHE_ADVICE
  - Menghindari kesimpulan dari hit ratio saja
---
## Kenapa topik ini diuji
Soal menanyakan cara menentukan apakah buffer cache perlu diperbesar.

## Konsep inti
```sql
SELECT metric_name, value FROM v$sysmetric
 WHERE metric_name IN ('Buffer Cache Hit Ratio','Physical Reads Per Sec');

SELECT size_for_estimate, buffers_for_estimate, estd_physical_read_factor
  FROM v$db_cache_advice WHERE name='DEFAULT' AND block_size=8192;

SELECT component, current_size/1024/1024 mb FROM v$sga_dynamic_components;
SELECT COUNT(*) FROM v$bh WHERE status='free';
```

Interpretasi: `estd_physical_read_factor` menurunkan drastis sampai titik tertentu → di situlah ukuran optimal. Setelah itu tambahan memori tidak banyak membantu.

## Jebakan
- Hit ratio 99% bisa menyesatkan bila query membaca blok sama berulang.
- Cache tidak bisa mengalahkan I/O buruk akibat full scan berulang.
- Menambah cache mengurangi memori untuk komponen lain.
- `V$DB_CACHE_ADVICE` butuh advisory aktif (`DB_CACHE_ADVICE=ON`).

## Latihan
1. View untuk simulasi ukuran cache?
2. Kapan menambah cache tidak berguna?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>V$DB_CACHE_ADVICE</code>.</p>
<p><b>2.</b> Saat kurva advisory sudah datar atau bottleneck-nya I/O/latency, bukan kapasitas cache.</p>
</details>
