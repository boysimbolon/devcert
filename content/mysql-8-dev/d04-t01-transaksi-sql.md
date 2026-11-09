---
title: Mengendalikan transaksi dengan SQL
minutes: 20
level: Menengah
badge: lengkap
summary: START TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT, dan commit implisit.
objectives:
  - Menulis blok transaksi dengan benar
  - Memakai savepoint untuk rollback sebagian
  - Mengenali pernyataan yang memicu commit implisit
---
## Kenapa topik ini diuji
Banyak bug "perubahan tidak bisa di-rollback" berasal dari commit implisit DDL.

## Konsep inti
```sql
SET autocommit = 0;
START TRANSACTION;

UPDATE rekening SET saldo = saldo - 100 WHERE id = 1;
SAVEPOINT setelah_debit;
UPDATE rekening SET saldo = saldo + 100 WHERE id = 2;
-- ternyata salah tujuan
ROLLBACK TO SAVEPOINT setelah_debit;

COMMIT;
```

Commit implisit terjadi pada: `CREATE/ALTER/DROP` (DDL), `TRUNCATE`, `LOCK TABLES`, `GRANT/REVOKE`, dan beberapa pernyataan administratif. Setelah itu `ROLLBACK` tidak lagi membatalkan apa pun sebelumnya.

```sql
SELECT @@autocommit, @@transaction_isolation;
SELECT * FROM information_schema.INNODB_TRX;
```

## Jebakan
- Menjalankan DDL di tengah transaksi lalu kaget karena data sebelumnya sudah ter-commit.
- `TRUNCATE` tidak bisa di-rollback dan memicu commit implisit.
- Lupa `COMMIT` sehingga perubahan hanya terlihat di sesi sendiri.
- Transaksi dibiarkan terbuka → lock menumpuk dan undo membengkak.

## Latihan
1. Apakah `TRUNCATE` bisa di-rollback?
2. Perintah membatalkan sebagian transaksi?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak — TRUNCATE adalah DDL dan memicu commit implisit.</p>
<p><b>2.</b> <code>ROLLBACK TO SAVEPOINT nama;</code></p>
</details>
