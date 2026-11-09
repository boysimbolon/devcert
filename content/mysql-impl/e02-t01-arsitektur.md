---
title: Arsitektur MySQL
minutes: 22
level: Dasar
badge: lengkap
summary: Lapisan koneksi, SQL, storage engine, dan komponen yang berjalan di server.
objectives:
  - Menjelaskan lapisan arsitektur MySQL
  - Membedakan tugas server layer dan storage engine
  - Menyebutkan komponen background
---
## Kenapa topik ini diuji
Soal arsitektur menguji pemisahan tanggung jawab: mana yang diurus server, mana yang diurus engine.

## Konsep inti
Empat lapisan:

```text
1. Connection layer : menerima koneksi, autentikasi, TLS, thread per koneksi (atau pool)
2. SQL layer        : parser, optimizer, executor; cache metadata; akses kontrol
3. Storage engine   : InnoDB (default), MyISAM, MEMORY, TEMPORARY, CSV
4. File system      : datadir, redo/undo, binlog, tablespace
```

Komponen background InnoDB: **master thread**, **IO thread** (read/write/insert buffer), **purge thread**, **page cleaner**. Plus thread replikasi bila aktif dan `event_scheduler` bila dinyalakan.

```sql
SHOW ENGINES;                 -- engine yang tersedia & default
SHOW VARIABLES LIKE 'default_storage_engine';
SHOW ENGINE INNODB STATUS\G
```

Pemisahan penting: SQL layer memahami SQL, tapi **transaksi dan lock baris** adalah tanggung jawab storage engine (InnoDB). Karena itu tabel MyISAM tidak transaksional.

## Jebakan
- Mengira binlog dibuat storage engine; binlog dibuat **server layer** (karena itu konsisten lintas engine).
- `SHOW ENGINES` menampilkan status dukungan, bukan engine yang dipakai tabel tertentu.
- Memory engine hilang saat restart; bukan pengganti cache aplikasi.
- Thread Pool (Enterprise) mengganti model thread per koneksi.

## Latihan
1. Siapa yang menangani transaksi: server layer atau storage engine?
2. Mengapa binlog tetap ada walau engine berbeda?

<details><summary>Jawaban</summary>
<p><b>1.</b> Storage engine (InnoDB).</p>
<p><b>2.</b> Karena binlog dihasilkan server layer, setelah perubahan diterapkan engine, sehingga mencatat logis perubahan lintas engine.</p>
</details>
