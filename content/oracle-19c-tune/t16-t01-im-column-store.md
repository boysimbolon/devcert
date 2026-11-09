---
title: In-Memory Column Store
minutes: 22
level: Menengah
badge: lengkap
summary: Menyimpan kolom di memori untuk scan analitik cepat.
objectives:
  - Mengonfigurasi IM column store
  - Mengisi dan memprioritaskan objek
  - Mengukur manfaatnya
---
## Kenapa topik ini diuji
Fitur 12c+ ini mengubah performa analitik secara drastis; soal menanyakan konfigurasi dan penggunaannya.

## Konsep inti
```sql
SHOW PARAMETER inmemory_size;
ALTER SYSTEM SET inmemory_size = 4G SCOPE=SPFILE;   -- butuh restart

ALTER TABLE penjualan INMEMORY;
ALTER TABLE penjualan INMEMORY PRIORITY HIGH;
ALTER TABLE penjualan INMEMORY MEMCOMPRESS FOR QUERY HIGH;

SELECT segment_name, inmemory_size/1024/1024 mb, populate_status
  FROM v$im_segments;

SELECT * FROM v$inmemory_area;
```

Format kompresi: `FOR DML`, `FOR QUERY LOW/HIGH`, `FOR CAPACITY LOW/HIGH` (rasio vs kecepatan).

## Jebakan
- `inmemory_size` statis; perubahan butuh restart.
- Data harus di-populate; `populate_status` bisa `STARTED`/`COMPLETED`.
- IM column store tidak menggantikan buffer cache untuk OLTP.
- Butuh In-Memory option (berbayar).

## Latihan
1. Parameter ukuran IM?
2. View untuk status populate?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>inmemory_size</code>.</p>
<p><b>2.</b> <code>V$IM_SEGMENTS</code>.</p>
</details>
