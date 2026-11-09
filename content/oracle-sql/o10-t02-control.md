---
title: Mengendalikan transaksi
minutes: 18
level: Menengah
badge: lengkap
summary: COMMIT, ROLLBACK, SAVEPOINT, dan perilaku sesi.
objectives:
  - Memakai savepoint untuk rollback parsial
  - Menjelaskan efek commit pada sesi lain
  - Menghindari transaksi menggantung
---
## Kenapa topik ini diuji
Soal memberi urutan DML dan menanyakan state akhir data.

## Konsep inti
```sql
INSERT INTO dept_copy VALUES (10,'AKUNTANSI','JKT');
SAVEPOINT s1;
UPDATE dept_copy SET lokasi = 'BDG' WHERE id = 10;
SAVEPOINT s2;
DELETE FROM dept_copy WHERE id = 10;

ROLLBACK TO s2;     -- DELETE dibatalkan, UPDATE tetap
ROLLBACK TO s1;     -- UPDATE dibatalkan, INSERT tetap
ROLLBACK;           -- semua dibatalkan
COMMIT;
```

Savepoint hanya berlaku dalam transaksi berjalan; setelah commit, savepoint hilang.

## Jebakan
- `ROLLBACK` tanpa nama membatalkan seluruh transaksi, bukan hanya pernyataan terakhir.
- Savepoint tidak menyimpan data ke disk.
- Setelah `ROLLBACK TO s1`, savepoint `s2` hilang.
- Transaksi panjang menahan undo dan lock.

## Latihan
1. Apa efek `ROLLBACK TO s1` pada perubahan setelah s1?
2. Apakah savepoint bertahan setelah commit?

<details><summary>Jawaban</summary>
<p><b>1.</b> Semua perubahan setelah s1 dibatalkan; perubahan sebelum s1 tetap.</p>
<p><b>2.</b> Tidak; savepoint berakhir bersama transaksi.</p>
</details>
