---
title: Menyimpan dan mengolah data string
minutes: 22
level: Menengah
badge: lengkap
summary: CHAR vs VARCHAR, collation, utf8mb4, dan fungsi string penting.
objectives:
  - Memilih tipe string yang tepat
  - Menjelaskan collation dan dampaknya pada perbandingan
  - Memakai fungsi string dan REGEXP
---
## Kenapa topik ini diuji
Collation dan charset adalah sumber bug halus; soal sering menanyakan hasil perbandingan.

## Konsep inti
| Tipe | Karakteristik |
|---|---|
| `CHAR(n)` | panjang tetap, padding spasi |
| `VARCHAR(n)` | panjang variabel, hemat untuk teks pendek |
| `TEXT` | panjang besar, tidak bisa di-index penuh |
| `ENUM` | satu nilai dari daftar |
| `SET` | banyak nilai dari daftar |

```sql
CREATE TABLE pelanggan (
  nama   VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  email  VARCHAR(191) NOT NULL UNIQUE
);
```

Fungsi yang sering dipakai:

```sql
SELECT CONCAT(nama,' - ',kota), CHAR_LENGTH(nama), UPPER(nama),
       SUBSTRING(email, LOCATE('@', email)+1) AS domain,
       TRIM(nama), REPLACE(nama,' ','_'),
       nama REGEXP '^[A-Z]' AS huruf_besar
  FROM pelanggan;
```

Collation menentukan perbandingan: `utf8mb4_0900_ai_ci` = case-insensitive dan accent-insensitive; `_bin` = peka huruf besar/kecil.

## Jebakan
- `CHAR` memangkas spasi di akhir saat dibaca.
- Index VARCHAR panjang dengan `utf8mb4` bisa melebihi batas index; pakai prefix index.
- Mencampur collation antar kolom pada JOIN → error "Illegal mix of collations".
- `LIKE '%kata%'` tidak memakai index; pertimbangkan FULLTEXT.

## Latihan
1. Apa arti akhiran `_ci` pada collation?
2. Mengapa `LIKE '%x%'` tidak memakai index?

<details><summary>Jawaban</summary>
<p><b>1.</b> Case-insensitive — perbandingan tidak membedakan huruf besar/kecil.</p>
<p><b>2.</b> Karena pola diawali wildcard, sehingga index B-tree tidak bisa mempersempit rentang.</p>
</details>
