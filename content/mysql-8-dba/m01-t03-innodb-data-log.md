---
title: Cara InnoDB menyimpan data dan log
minutes: 24
level: Menengah
badge: lengkap
summary: Clustered index, buffer pool, redo, undo, doublewrite, dan change buffer.
objectives:
  - Menjelaskan struktur penyimpanan InnoDB
  - Membedakan fungsi redo log dan undo log
  - Menjelaskan peran doublewrite buffer dan change buffer
---
## Kenapa topik ini diuji
Ini inti arsitektur. Soal sering menanyakan perbedaan redo/undo, atau mengapa data tidak langsung ditulis ke disk.

## Konsep inti
- **Page** 16 KB adalah unit baca/tulis.
- **Clustered index**: data tabel disimpan terurut menurut primary key. Tanpa PK, InnoDB membuat clustered index tersembunyi.
- **Secondary index** menyimpan nilai kolom index + **primary key** (bukan pointer fisik), sehingga lookup kedua terjadi.
- **Buffer pool**: cache page di RAM; semua perubahan ditulis ke sini dulu.
- **Redo log**: catatan perubahan fisik untuk *crash recovery*; ditulis berurutan dan di-flush sesuai `innodb_flush_log_at_trx_commit`.
- **Undo log**: menyimpan versi lama baris untuk rollback dan **MVCC** (read view).
- **Doublewrite buffer**: menulis page ke area khusus sebelum ke tempat aslinya, mencegah *torn page*.
- **Change buffer**: menunda update index sekunder untuk baris yang tidak ada di buffer pool.

```sql
SHOW ENGINE INNODB STATUS\G           -- bagian LOG, BUFFER POOL AND MEMORY
SELECT @@innodb_flush_log_at_trx_commit,  -- 1 = paling aman (ACID)
       @@innodb_buffer_pool_size,
       @@innodb_log_file_size,
       @@innodb_flush_method;
```

Alur commit singkat:

```text
UPDATE -> page di buffer pool diubah -> redo entry ditulis -> commit
      -> redo di-flush (jika flush_log_at_trx_commit=1)
      -> page kotor ditulis belakangan oleh checkpoint
```

## Jebakan
- Menganggap redo log = binlog. Redo untuk recovery engine (fisik); binlog untuk replikasi dan PITR (logis).
- `innodb_flush_log_at_trx_commit=2` lebih cepat tetapi bisa kehilangan transaksi terakhir saat OS crash.
- Undo tidak bisa dibuang selama masih ada transaksi/read view yang membutuhkannya; history list length besar = ada transaksi panjang.
- Secondary index selalu membawa PK; index lebar memperbesar ukuran.

## Latihan
1. Apa yang terjadi pada commit bila `innodb_flush_log_at_trx_commit=0`?
2. Mengapa history list length panjang berbahaya?

<details><summary>Jawaban</summary>
<p><b>1.</b> Redo di-flush sekali per detik oleh thread background, bukan saat commit — transaksi bisa hilang bila server crash.</p>
<p><b>2.</b> Undo tidak bisa dipurge, tablespace membesar, dan query bisa melambat karena harus menelusuri banyak versi lama.</p>
</details>
