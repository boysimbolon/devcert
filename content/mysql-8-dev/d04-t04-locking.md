---
title: Mekanisme locking di MySQL
minutes: 20
level: Menengah
badge: lengkap
summary: Lock baris, lock tabel, metadata lock, dan opsi NOWAIT/SKIP LOCKED.
objectives:
  - Membedakan lock baris dan lock tabel
  - Memakai FOR UPDATE dengan benar
  - Mengenali metadata lock pada DDL
---
## Kenapa topik ini diuji
Soal lock menanyakan perintah mana yang mengunci apa, dan mengapa DDL menggantung.

## Konsep inti
```sql
-- lock baris eksklusif
SELECT * FROM stok WHERE id = 1 FOR UPDATE;

-- lock share
SELECT * FROM stok WHERE id = 1 FOR SHARE;

-- jangan menunggu
SELECT * FROM stok WHERE id = 1 FOR UPDATE NOWAIT;

-- lewati baris yang sedang dikunci (antrean job)
SELECT * FROM antrian WHERE status='baru' ORDER BY id LIMIT 10 FOR UPDATE SKIP LOCKED;

-- lock tabel eksplisit
LOCK TABLES pesanan WRITE;
UNLOCK TABLES;
```

| Lock | Cakupan | Catatan |
|---|---|---|
| Record lock | satu baris/index | default InnoDB |
| Gap lock | celah di antara nilai | di REPEATABLE READ |
| Next-key | record + gap | kombinasi |
| Table lock | seluruh tabel | `LOCK TABLES`, DDL |
| Metadata lock (MDL) | definisi tabel | muncul saat DDL menunggu sesi aktif |

## Jebakan
- `FOR UPDATE` tanpa index mengunci banyak baris (bahkan seluruh tabel).
- `LOCK TABLES` tidak kompatibel dengan transaksi InnoDB yang berjalan.
- `ALTER TABLE` menunggu MDL dari transaksi yang bahkan hanya `SELECT`.
- `SKIP LOCKED` bisa membuat baris terlewat dari laporan.

## Latihan
1. Perintah mengunci baris hanya untuk dibaca-banding?
2. Mengapa `ALTER TABLE` bisa menggantung lama?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>SELECT ... FOR SHARE</code> (shared lock).</p>
<p><b>2.</b> Karena ia menunggu metadata lock yang dipegang transaksi/ sesi yang masih membuka tabel.</p>
</details>
