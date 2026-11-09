---
title: External table
minutes: 20
level: Menengah
badge: lengkap
summary: Membaca file di luar database tanpa memuat data ke dalamnya.
objectives:
  - Membuat external table
  - Menjelaskan kapan dipakai
  - Mengetahui keterbatasannya
---
## Kenapa topik ini diuji
Fitur khas Oracle: data tetap di file OS, tabel hanya "jendela" untuk membacanya.

## Konsep inti
```sql
CREATE OR REPLACE DIRECTORY data_dir AS '/data/input';

CREATE TABLE ext_penjualan (
  id     NUMBER,
  barang VARCHAR2(50),
  total  NUMBER
)
ORGANIZATION EXTERNAL (
  TYPE ORACLE_LOADER
  DEFAULT DIRECTORY data_dir
  ACCESS PARAMETERS (
    RECORDS DELIMITED BY NEWLINE
    FIELDS TERMINATED BY ','
  )
  LOCATION ('penjualan.csv')
)
REJECT LIMIT UNLIMITED;

SELECT COUNT(*), SUM(total) FROM ext_penjualan;
```

## Jebakan
- External table **read-only** untuk ORACLE_LOADER (kecuali ORACLE_DATAPUMP untuk menulis).
- Butuh DIRECTORY object dan hak READ pada direktori.
- `REJECT LIMIT` menentukan berapa baris buruk boleh dilewati.
- Tidak ada index; setiap query membaca file.

## Latihan
1. Bisakah data di-INSERT ke external table ORACLE_LOADER?
2. Objek apa yang memberi akses ke path OS?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak (read-only).</p>
<p><b>2.</b> DIRECTORY object plus privilege READ pada direktori itu.</p>
</details>
