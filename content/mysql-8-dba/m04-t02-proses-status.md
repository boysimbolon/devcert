---
title: Memantau proses dan status server
minutes: 22
level: Menengah
badge: lengkap
summary: PROCESSLIST, performance_schema, sys schema, dan metrik status yang penting.
objectives:
  - Menemukan query yang berjalan lama
  - Membaca metrik status kunci
  - Memakai sys schema untuk diagnosis cepat
---
## Kenapa topik ini diuji
Soal monitoring menanyakan alat mana untuk pertanyaan operasional spesifik: siapa yang menahan lock, query apa yang lambat, buffer pool cukup atau tidak.

## Konsep inti
```sql
SHOW FULL PROCESSLIST;
SELECT id, user, host, db, command, time, state, LEFT(info, 80) AS query
  FROM information_schema.PROCESSLIST
 WHERE command <> 'Sleep' ORDER BY time DESC LIMIT 10;

KILL 1234;                        -- putuskan koneksi
KILL QUERY 1234;                  -- hentikan query, koneksi tetap
```

Status yang perlu dihafal:

```sql
SHOW GLOBAL STATUS LIKE 'Threads_connected';
SHOW GLOBAL STATUS LIKE 'Questions';
SHOW GLOBAL STATUS LIKE 'Slow_queries';
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_reads';
SHOW GLOBAL STATUS LIKE 'Innodb_row_lock_waits';
SHOW GLOBAL STATUS LIKE 'Created_tmp_disk_tables';
```

`sys` schema memberi jawaban siap pakai:

```sql
SELECT * FROM sys.processlist WHERE time > 5;
SELECT * FROM sys.statement_analysis ORDER BY total_latency DESC LIMIT 10;
SELECT * FROM sys.innodb_lock_waits\G
SELECT * FROM sys.schema_unused_indexes;
SELECT * FROM sys.memory_global_total;
```

## Jebakan
- `KILL` memutus koneksi (transaksi di-rollback), `KILL QUERY` hanya menghentikan pernyataan berjalan.
- `Created_tmp_disk_tables` tinggi menandakan `tmp_table_size` terlalu kecil atau query butuh index.
- Metrik status bersifat **kumulatif**; yang berguna adalah selisih antar waktu, bukan angka mentah.
- `PROCESSLIST` hanya menampilkan query aktif; transaksi menganggur muncul sebagai `Sleep`.

## Latihan
1. Perbedaan `KILL` dan `KILL QUERY`?
2. Bagaimana menemukan transaksi yang menahan lock?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>KILL</code> memutus koneksi dan me-rollback transaksi; <code>KILL QUERY</code> hanya menghentikan pernyataan yang sedang berjalan.</p>
<p><b>2.</b> <code>SELECT * FROM sys.innodb_lock_waits</code> atau <code>performance_schema.data_locks</code> / <code>data_lock_waits</code>.</p>
</details>
