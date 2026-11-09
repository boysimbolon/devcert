---
title: Menangani error dan warning
minutes: 22
level: Menengah
badge: lengkap
summary: SQLSTATE, kode error umum, GET DIAGNOSTICS, dan SIGNAL.
objectives:
  - Membaca error dan warning dari server
  - Mengenali kode error yang sering
  - Melempar error sendiri dari stored program
---
## Kenapa topik ini diuji
Soal menanyakan kode error atau cara menanganinya di aplikasi/stored program.

## Konsep inti
```sql
SHOW WARNINGS;
SHOW ERRORS;
SELECT @@warning_count, @@error_count;

-- di stored procedure
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
  GET DIAGNOSTICS CONDITION 1
    @state = RETURNED_SQLSTATE, @errno = MYSQL_ERRNO, @msg = MESSAGE_TEXT;
  ROLLBACK;
  RESIGNAL;
END;

SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Stok tidak cukup';
```

Kode yang wajib dikenal:

| Errno | SQLSTATE | Arti |
|---|---|---|
| 1062 | 23000 | duplicate entry (unique) |
| 1451 | 23000 | FK constraint gagal saat hapus induk |
| 1452 | 23000 | FK constraint gagal saat insert anak |
| 1213 | 40001 | deadlock, transaksi di-rollback |
| 1205 | HY000 | lock wait timeout |
| 1048 | 23000 | kolom NOT NULL diberi NULL |
| 1406 | 22001 | data too long |
| 1264 | 22003 | out of range value |

## Jebakan
- Menangkap semua error dengan handler generik lalu menelan informasinya.
- `SIGNAL` butuh SQLSTATE 5 karakter; `45000` = error yang ditentukan pengguna.
- `RESIGNAL` tanpa argumen meneruskan error asli — sering lupa sehingga detail hilang.
- Deadlock bukan error fatal: aplikasi sebaiknya **retry**.

## Latihan
1. SQLSTATE untuk deadlock?
2. Perbedaan SIGNAL dan RESIGNAL?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>40001</code> (errno 1213).</p>
<p><b>2.</b> <code>SIGNAL</code> melempar error baru dengan pesan sendiri; <code>RESIGNAL</code> meneruskan error yang sedang ditangani.</p>
</details>
