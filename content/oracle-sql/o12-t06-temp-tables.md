---
title: Temporary table
minutes: 18
level: Menengah
badge: lengkap
summary: GLOBAL TEMPORARY table, ON COMMIT DELETE ROWS vs PRESERVE ROWS.
objectives:
  - Membuat temporary table
  - Membedakan kedua mode commit
  - Menjelaskan cakupan data per sesi
---
## Kenapa topik ini diuji
Soal menanyakan di mana data temporary table terlihat dan kapan terhapus.

## Konsep inti
```sql
CREATE GLOBAL TEMPORARY TABLE tmp_keranjang (
  id     NUMBER,
  barang VARCHAR2(50)
) ON COMMIT DELETE ROWS;        -- default

CREATE GLOBAL TEMPORARY TABLE tmp_laporan (
  id NUMBER, total NUMBER
) ON COMMIT PRESERVE ROWS;
```

Ciri:

- Definisi tabel permanen (terlihat di `USER_TABLES` dengan `TEMPORARY='Y'`).
- Data **per sesi**; sesi lain tidak melihat.
- `ON COMMIT DELETE ROWS` menghapus baris saat commit.
- `ON COMMIT PRESERVE ROWS` menyimpan sampai sesi berakhir.
- Data disimpan di temporary tablespace.

## Jebakan
- Temporary table bukan tabel sementara yang otomatis hilang; definisinya tetap.
- Data tidak terlihat antar sesi, jadi bukan alat berbagi.
- Menghapus definisi = `DROP TABLE` biasa.
- Index pada GTT juga sementara untuk data.

## Latihan
1. Mode mana yang menghapus baris saat commit?
2. Apakah sesi lain bisa membaca isi GTT?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ON COMMIT DELETE ROWS</code>.</p>
<p><b>2.</b> Tidak; data bersifat privat per sesi.</p>
</details>
