---
title: Menangani masalah lock dan deadlock
minutes: 22
level: Menengah
badge: lengkap
summary: Lock baris InnoDB, metadata lock, deadlock, dan cara menemukan penyebabnya.
objectives:
  - Membaca status lock dan waiting transaction
  - Menemukan penyebab metadata lock
  - Mengurangi deadlock lewat urutan akses
---
## Kenapa topik ini diuji
Query "menggantung" hampir selalu soal lock. Soal menanyakan cara menemukan siapa menahan apa.

## Konsep inti
InnoDB memakai **row-level lock**. Lock menunggu bila baris sama diubah transaksi lain. Metadata lock (MDL) muncul saat DDL menunggu transaksi yang masih memakai tabel.

```sql
-- siapa menunggu siapa
SELECT * FROM performance_schema.data_lock_waits\G
SELECT * FROM sys.innodb_lock_waits\G

-- lock yang dipegang
SELECT ENGINE_TRANSACTION_ID, OBJECT_NAME, INDEX_NAME, LOCK_TYPE, LOCK_MODE, LOCK_STATUS
  FROM performance_schema.data_locks LIMIT 20;

-- transaksi berjalan
SELECT trx_id, trx_state, trx_started, trx_mysql_thread_id, trx_query
  FROM information_schema.INNODB_TRX;
```

Deadlock: dua transaksi saling menunggu. InnoDB mendeteksi dan **me-rollback** salah satu; detail ada di `SHOW ENGINE INNODB STATUS` bagian `LATEST DETECTED DEADLOCK`.

```sql
SET GLOBAL innodb_print_all_deadlocks = ON;   -- catat semua deadlock ke error log
SET GLOBAL innodb_lock_wait_timeout = 10;
```

## Jebakan
- Transaksi menganggur (`Sleep`) yang tidak commit menahan lock; matikan dengan `KILL`.
- MDL: `ALTER TABLE` bisa menunggu selamanya karena satu sesi membuka tabel.
- `LOCK TABLES` MyISAM memblokir total; hindari di InnoDB.
- Deadlock bukan bug, tapi pola akses yang tidak konsisten (urutan baris berbeda).

## Latihan
1. Bagaimana menemukan transaksi yang menahan lock?
2. Cara mengurangi deadlock pada aplikasi?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>sys.innodb_lock_waits</code> atau <code>performance_schema.data_lock_waits</code>, lalu lihat <code>INNODB_TRX</code>.</p>
<p><b>2.</b> Akses baris dengan urutan konsisten, transaksi pendek, index yang tepat agar lock tidak melebar.</p>
</details>
