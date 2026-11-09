---
title: Tipe data dalam database MySQL
minutes: 22
level: Dasar
badge: lengkap
summary: Memilih tipe yang tepat untuk angka, teks, waktu, JSON, dan spasial.
objectives:
  - Memilih tipe sesuai rentang dan presisi
  - Menjelaskan konsekuensi tipe yang salah
  - Mengenali tipe khusus (JSON, GEOMETRY, ENUM)
---
## Kenapa topik ini diuji
Soal desain selalu dimulai dari tipe data: pilihan yang salah memengaruhi ukuran, index, dan akurasi.

## Konsep inti
| Kelompok | Tipe | Catatan |
|---|---|---|
| Bilangan bulat | TINYINT, SMALLINT, MEDIUMINT, INT, BIGINT | pilih sesuai rentang, ada `UNSIGNED` |
| Desimal | DECIMAL(p,s) | uang; presisi tetap |
| Aproksimasi | FLOAT, DOUBLE | ilmiah; ada galat biner |
| Teks | CHAR, VARCHAR, TEXT | `CHAR` tetap, `VARCHAR` variabel |
| Biner | BINARY, VARBINARY, BLOB | data non-teks |
| Waktu | DATE, DATETIME, TIMESTAMP, TIME, YEAR | TIMESTAMP terbatas 2038 |
| Khusus | ENUM, SET, JSON, GEOMETRY | validasi bawaan |

```sql
CREATE TABLE contoh (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  kode CHAR(6) NOT NULL,
  nama VARCHAR(120) NOT NULL,
  harga DECIMAL(12,2) NOT NULL,
  berat DOUBLE,
  dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atribut JSON,
  lokasi POINT SRID 4326
);
```

## Jebakan
- `INT` untuk id yang bisa melebihi 2,1 miliar.
- `VARCHAR(255)` untuk semua kolom teks, membengkak pada tabel besar.
- `TIMESTAMP` untuk tanggal lahir (batas 2038).
- `ENUM` sulit diubah saat nilai baru muncul.

## Latihan
1. Tipe untuk nilai uang?
2. Mengapa `TIMESTAMP` tidak cocok untuk tanggal lahir?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DECIMAL(p,s)</code>.</p>
<p><b>2.</b> Karena rentangnya berakhir 2038 dan nilainya dikonversi zona waktu.</p>
</details>
