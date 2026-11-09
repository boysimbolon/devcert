---
title: Mengelola transaksi database
minutes: 20
level: Menengah
badge: lengkap
summary: Transaksi, ACID, dan apa yang memulai serta mengakhiri transaksi di Oracle.
objectives:
  - Menjelaskan konsep transaksi dan ACID
  - Menyebutkan pemicu awal transaksi
  - Membedakan commit implisit dan eksplisit
---
## Kenapa topik ini diuji
Soal menanyakan perintah mana yang mengakhiri transaksi — banyak DDL yang melakukannya tanpa disadari.

## Konsep inti
Transaksi dimulai saat pernyataan DML pertama dijalankan, berakhir dengan `COMMIT` atau `ROLLBACK`.

| Peristiwa | Efek |
|---|---|
| `COMMIT` | menyimpan permanen |
| `ROLLBACK` | membatalkan semua perubahan |
| `SAVEPOINT nama` | titik rollback sebagian |
| DDL (CREATE, ALTER, DROP, TRUNCATE, RENAME) | **commit implisit** |
| `GRANT`/`REVOKE` | commit implisit |
| Keluar dari klien | biasanya commit (login normal) |

Sifat ACID: Atomicity, Consistency, Isolation, Durability. Oracle menjamin isolasi lewat **read consistency** dan **undo**.

## Jebakan
- DDL di tengah transaksi otomatis meng-commit DML sebelumnya.
- `TRUNCATE` tidak bisa di-rollback.
- Menutup SQL*Plus tanpa `EXIT` normal bisa membuat transaksi menggantung.
- `COMMIT` tidak bisa dibatalkan.

## Latihan
1. Apakah `ALTER TABLE` bisa di-rollback?
2. Kapan transaksi dimulai di Oracle?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak; DDL memicu commit implisit.</p>
<p><b>2.</b> Pada pernyataan DML pertama setelah transaksi sebelumnya berakhir.</p>
</details>
