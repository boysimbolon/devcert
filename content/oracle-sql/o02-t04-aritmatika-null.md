---
title: Ekspresi aritmatika dan NULL
minutes: 18
level: Dasar
badge: lengkap
summary: Operator aritmatika, presedensi dasar, dan perilaku NULL dalam perhitungan.
objectives:
  - Menulis ekspresi aritmatika pada SELECT
  - Menjelaskan efek NULL pada hasil
  - Memakai NVL untuk nilai pengganti
---
## Kenapa topik ini diuji
NULL adalah penyebab jawaban salah paling sering: hasil perhitungan menjadi NULL tanpa error.

## Konsep inti
```sql
SELECT salary, salary * 12 AS tahunan, salary + NVL(commission_pct,0)*salary AS total
  FROM employees;

SELECT 10 + NULL FROM dual;      -- NULL
SELECT NULL || 'x' FROM dual;    -- NULL (string)
SELECT NVL(NULL, 'kosong') FROM dual;
```

Aturan:

- Operasi aritmatika apa pun dengan NULL menghasilkan NULL.
- `NULL = NULL` tidak bernilai true; gunakan `IS NULL`.
- `ORDER BY` menempatkan NULL di akhir untuk ASC (di Oracle, NULL dianggap terbesar).

## Jebakan
- `salary + commission` tanpa `NVL` menghapus baris dari hasil hitungan.
- `WHERE kolom <> 'x'` tidak mengembalikan baris NULL.
- `COUNT(*)` menghitung baris NULL, `COUNT(kolom)` tidak.
- Oracle menganggap string kosong `''` sebagai NULL.

## Latihan
1. Hasil `5 + NULL`?
2. Bagaimana membuat perhitungan tetap menghasilkan angka saat kolom NULL?

<details><summary>Jawaban</summary>
<p><b>1.</b> NULL.</p>
<p><b>2.</b> Bungkus dengan <code>NVL(kolom, 0)</code> atau <code>COALESCE</code>.</p>
</details>
