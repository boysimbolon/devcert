---
title: Big Table Caching
minutes: 18
level: Menengah
badge: lengkap
summary: Memberi porsi buffer cache khusus untuk full scan tabel besar.
objectives:
  - Menjelaskan konsep big table cache
  - Mengatur ukuran dan perilakunya
  - Menilai kapan berguna
---
## Kenapa topik ini diuji
Fitur 12c+ yang jarang diketahui; soal menanyakan tujuannya.

## Konsep inti
```sql
SHOW PARAMETER db_big_table_cache_percent_target;

ALTER SYSTEM SET db_big_table_cache_percent_target = 30;
ALTER TABLE penjualan STORAGE (CELL_FLASH_CACHE KEEP);

SELECT * FROM v$bt_scan_cache;
SELECT * FROM v$bt_scan_obj_temps;
```

Tujuan: mencegah full scan tabel besar menggeser blok OLTP dari buffer cache. Oracle membagi cache: sebagian untuk objek "big table".

## Jebakan
- Hanya berguna bila ada full scan berulang pada tabel besar.
- Persentase terlalu besar mengurangi cache untuk OLTP.
- Perilaku bergantung pada estimasi ukuran tabel dan advisory.
- Bukan pengganti index atau partisi.

## Latihan
1. Parameter untuk mengatur porsi?
2. Masalah apa yang dicegah fitur ini?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>db_big_table_cache_percent_target</code>.</p>
<p><b>2.</b> Full scan tabel besar menggeser blok yang dipakai OLTP sehingga cache OLTP tergerus.</p>
</details>
