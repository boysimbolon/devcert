---
title: Membuat database dan tabel
minutes: 22
level: Dasar
badge: lengkap
summary: DDL dasar, constraint, engine, dan charset yang benar.
objectives:
  - Membuat database dengan charset tepat
  - Menulis tabel dengan constraint yang melindungi data
  - Mengubah struktur tanpa kehilangan data
---
## Kenapa topik ini diuji
Soal praktis: menulis DDL yang benar, termasuk charset dan foreign key.

## Konsep inti
```sql
CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE appdb;

CREATE TABLE pelanggan (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(191) NOT NULL UNIQUE,
  nama VARCHAR(120) NOT NULL,
  aktif TINYINT(1) NOT NULL DEFAULT 1,
  dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE pesanan (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  pelanggan_id BIGINT UNSIGNED NOT NULL,
  total DECIMAL(12,2) NOT NULL,
  CONSTRAINT fk_pesanan_pelanggan FOREIGN KEY (pelanggan_id)
    REFERENCES pelanggan(id) ON DELETE RESTRICT ON UPDATE CASCADE
);

ALTER TABLE pesanan ADD COLUMN catatan VARCHAR(255) NULL;
```

Pilihan yang diuji: `ENGINE=InnoDB` (transaksional), `utf8mb4` (mendukung emoji), `ON DELETE RESTRICT` vs `CASCADE` vs `SET NULL`.

## Jebakan
- `utf8` (3 byte) tidak mendukung emoji; gunakan `utf8mb4`.
- Foreign key butuh index pada kolom anak (dibuat otomatis bila belum ada).
- `AUTO_INCREMENT` tidak menjamin tanpa celah setelah rollback.
- Mengubah charset kolom pada tabel besar butuh waktu dan ruang.

## Latihan
1. Charset untuk mendukung emoji?
2. Apa efek `ON DELETE CASCADE`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>utf8mb4</code>.</p>
<p><b>2.</b> Menghapus baris anak otomatis saat baris induk dihapus.</p>
</details>
