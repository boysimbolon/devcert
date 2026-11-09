---
title: Memantau pertumbuhan data dan kapasitas
minutes: 20
level: Menengah
badge: lengkap
summary: Mengukur ukuran tabel, laju pertumbuhan, dan merencanakan kapasitas disk.
objectives:
  - Mengukur ukuran data dan index per schema
  - Menghitung laju pertumbuhan dan proyeksi
  - Menentukan kapan menambah kapasitas
---
## Kenapa topik ini diuji
Soal kapasitas meminta perhitungan sederhana: ukuran sekarang, laju pertumbuhan, sisa waktu.

## Konsep inti
```sql
SELECT table_schema,
       ROUND(SUM(data_length)/1024/1024, 1) AS data_mb,
       ROUND(SUM(index_length)/1024/1024, 1) AS index_mb,
       ROUND(SUM(data_free)/1024/1024, 1) AS free_mb
  FROM information_schema.TABLES
 GROUP BY table_schema
 ORDER BY data_mb DESC;

SELECT table_name,
       ROUND((data_length+index_length)/1024/1024,1) AS total_mb,
       table_rows
  FROM information_schema.TABLES
 WHERE table_schema='appdb'
 ORDER BY (data_length+index_length) DESC LIMIT 10;
```

Proyeksi sederhana:

```text
tumbuh 2 GB/bulan, sisa disk 15 GB
-> sekitar 7 bulan sebelum kritis; sisakan buffer 30% untuk redo/undo/temp
```

Yang ikut diperhitungkan: binlog (bisa jauh lebih besar dari data), undo tablespace, temporary tablespace, redo log, dan backup di host yang sama.

## Jebakan
- `table_rows` di INFORMATION_SCHEMA hanya perkiraan statistik, bukan hitungan pasti.
- Lupa menghitung binlog: dengan `binlog_expire_logs_seconds` besar, disk bisa penuh.
- `data_free` menandakan ruang terbuang di dalam tablespace (fragmentasi), bukan ruang bebas disk.
- Backup di disk yang sama menggandakan kebutuhan.

## Latihan
1. Tabel mana yang paling perlu diperiksa ukurannya?
2. Mengapa binlog harus masuk perhitungan kapasitas?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tabel terbesar menurut <code>data_length+index_length</code>, biasanya tabel transaksi/log yang tumbuh terus.</p>
<p><b>2.</b> Karena binlog mencatat setiap perubahan dan bisa tumbuh lebih cepat daripada data itu sendiri.</p>
</details>
