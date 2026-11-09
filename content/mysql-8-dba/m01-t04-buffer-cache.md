---
title: Mengonfigurasi buffer dan cache
minutes: 22
level: Menengah
badge: lengkap
summary: Ukuran buffer pool, instance, dan cache lain yang menentukan performa baca-tulis.
objectives:
  - Menentukan innodb_buffer_pool_size yang wajar
  - Mengatur buffer pool instance dan chunk
  - Memilih cache pendukung sesuai beban
---
## Kenapa topik ini diuji
Pertanyaan tuning paling sering menyangkut buffer pool: berapa, bagaimana mengubahnya, dan bagaimana mengukur efektivitasnya.

## Konsep inti
```ini
[mysqld]
innodb_buffer_pool_size = 4G        # 50-75% RAM khusus DB
innodb_buffer_pool_instances = 4     # untuk buffer >= 1G, kurangi kontensi
innodb_buffer_pool_chunk_size = 128M
innodb_log_buffer_size = 64M
table_open_cache = 2000
table_open_cache_instances = 16
sort_buffer_size = 2M               # per koneksi
join_buffer_size = 2M               # per join, per koneksi
read_buffer_size = 1M
tmp_table_size = 64M
max_heap_table_size = 64M
```

`innodb_buffer_pool_size` bisa diubah **online** dan diterapkan bertahap:

```sql
SET GLOBAL innodb_buffer_pool_size = 8589934592;    -- 8G
SELECT @@innodb_buffer_pool_size/1024/1024/1024 AS gb;
SHOW STATUS LIKE 'Innodb_buffer_pool_pages_free';
SHOW STATUS LIKE 'Innodb_buffer_pool_read_requests';
SHOW STATUS LIKE 'Innodb_buffer_pool_reads';        -- hit rate = 1 - reads/read_requests
```

Cache lain dan fungsinya:

| Cache | Untuk apa |
|---|---|
| `table_open_cache` | deskriptor tabel terbuka |
| `sort_buffer_size` | ORDER BY/GROUP BY per koneksi |
| `join_buffer_size` | join tanpa index |
| `tmp_table_size` + `max_heap_table_size` | tabel sementara in-memory |
| `key_buffer_size` | index MyISAM (bukan InnoDB) |

## Jebakan
- Menghitung `sort_buffer_size` sebagai global: ia **per koneksi**, 500 koneksi × 2M = 1 GB.
- Memberi buffer pool 90% RAM sehingga OS kekurangan cache dan swap.
- `key_buffer_size` besar padahal semua tabel InnoDB — memori terbuang.
- Mengubah `innodb_buffer_pool_size` dengan nilai bukan kelipatan chunk → disesuaikan otomatis, hasilnya tidak seperti yang diminta.

## Latihan
1. Cara mengukur buffer pool hit rate dari status?
2. Mengapa `sort_buffer_size` berbahaya bila terlalu besar?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>1 - Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests</code>; target di atas 99% untuk OLTP.</p>
<p><b>2.</b> Karena dialokasikan per koneksi; nilai besar dikalikan banyak koneksi bisa menghabiskan RAM.</p>
</details>
