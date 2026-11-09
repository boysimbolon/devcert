---
title: Menyimpan dan mengolah data numerik
minutes: 20
level: Menengah
badge: lengkap
summary: DECIMAL vs FLOAT, integer unsigned, overflow, dan nilai yang dibulatkan.
objectives:
  - Memilih tipe numerik yang tepat untuk uang dan pengukuran
  - Menghindari kesalahan pembulatan
  - Menangani overflow dan unsigned
---
## Kenapa topik ini diuji
Soal numerik biasanya soal jebakan: hasil pembulatan atau overflow yang tidak terduga.

## Konsep inti
| Tipe | Pakai untuk | Catatan |
|---|---|---|
| `TINYINT`/`SMALLINT`/`INT`/`BIGINT` | bilangan bulat | pilih sesuai rentang |
| `DECIMAL(p,s)` | uang, nilai eksak | presisi desimal tetap |
| `FLOAT`/`DOUBLE` | pengukuran ilmiah | pembulatan biner |
| `BIT(n)` | flag bit | jarang dipakai |

```sql
CREATE TABLE pembayaran (
  id BIGINT UNSIGNED PRIMARY KEY,
  jumlah DECIMAL(12,2) NOT NULL,
  rasio DOUBLE
);

SELECT 0.1 + 0.2 = 0.3;                    -- 0 (float biner!)
SELECT CAST(0.1 AS DECIMAL(10,1)) + CAST(0.2 AS DECIMAL(10,1)) = 0.3;  -- 1
SELECT ROUND(2.5), ROUND(-2.5), TRUNCATE(2.567, 2), CEIL(2.1), FLOOR(2.9);
```

Batas penting: `INT` maksimum 2147483647; `BIGINT UNSIGNED` sampai 18446744073709551615.

## Jebakan
- `FLOAT` untuk uang → selisih sen yang menumpuk.
- Overflow pada mode tidak ketat memotong nilai ke batas; strict mode memberi error.
- `DECIMAL(5,2)` tidak bisa menyimpan 1234.5 (butuh 6 digit).
- `ROUND` memakai pembulatan "half away from zero", bukan banker's rounding.

## Latihan
1. Tipe untuk menyimpan uang?
2. Mengapa `0.1 + 0.2 != 0.3` pada DOUBLE?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DECIMAL(p,s)</code>.</p>
<p><b>2.</b> Karena bilangan desimal disimpan dalam biner dan tidak semua nilai bisa direpresentasikan tepat.</p>
</details>
