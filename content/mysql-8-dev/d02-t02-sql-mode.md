---
title: Mengatur SQL Mode untuk mengubah perilaku
minutes: 22
level: Menengah
badge: lengkap
summary: STRICT_TRANS_TABLES, ONLY_FULL_GROUP_BY, ANSI_QUOTES, dan mode tradisional.
objectives:
  - Menjelaskan efek mode ketat pada INSERT/UPDATE
  - Mengenali mode yang mengubah sintaks
  - Mengatur mode per sesi dan global
---
## Kenapa topik ini diuji
SQL mode mengubah apakah sebuah pernyataan gagal atau "berhasil dengan peringatan" — inti banyak soal.

## Konsep inti
```sql
SELECT @@sql_mode;
SET SESSION sql_mode = 'STRICT_TRANS_TABLES,ONLY_FULL_GROUP_BY,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO';
SET GLOBAL sql_mode = 'TRADITIONAL';
```

Mode penting:

| Mode | Efek |
|---|---|
| `STRICT_TRANS_TABLES` | nilai tidak valid → error, bukan dipotong (default 8.0) |
| `ONLY_FULL_GROUP_BY` | kolom di SELECT harus ada di GROUP BY atau agregat |
| `NO_ZERO_DATE` / `NO_ZERO_IN_DATE` | menolak tanggal nol |
| `ANSI_QUOTES` | `"` menjadi identifier, bukan string |
| `PIPES_AS_CONCAT` | `||` menjadi concat, bukan OR |
| `ERROR_FOR_DIVISION_BY_ZERO` | pembagian nol menjadi error |
| `TRADITIONAL` | gabungan mode ketat |

```sql
-- dengan strict mode: error
INSERT INTO pelanggan (nama, umur) VALUES ('Budi', 'bukan angka');

-- tanpa strict: tersimpan 0 + warning
SHOW WARNINGS;
```

## Jebakan
- Mengira `sql_mode` hanya global; ia bisa per sesi dan berbeda antara aplikasi dan CLI.
- Mengubah mode global tidak mengubah sesi yang sedang berjalan.
- `ANSI_QUOTES` membuat query dengan `"string"` gagal — sering terjadi setelah migrasi.
- `ONLY_FULL_GROUP_BY` membuat query lama gagal; solusinya perbaiki query, bukan mematikan mode.

## Latihan
1. Apa yang terjadi pada INSERT dengan nilai tidak valid saat strict mode aktif?
2. Mode mana yang membuat `"` bukan string?

<details><summary>Jawaban</summary>
<p><b>1.</b> Pernyataan gagal dengan error (bukan dipotong dan warning).</p>
<p><b>2.</b> <code>ANSI_QUOTES</code>.</p>
</details>
