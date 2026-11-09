---
title: Mengurutkan data
minutes: 18
level: Dasar
badge: lengkap
summary: ORDER BY, ASC/DESC, NULLS FIRST/LAST, dan urutan berdasarkan alias atau posisi.
objectives:
  - Mengurutkan satu atau banyak kolom
  - Mengatur posisi NULL
  - Memakai alias dan nomor kolom di ORDER BY
---
## Kenapa topik ini diuji
Soal menguji perilaku NULL dan kemampuan mengurutkan dengan ekspresi.

## Konsep inti
```sql
SELECT last_name, salary, commission_pct
  FROM employees
 ORDER BY salary DESC, last_name ASC;

SELECT last_name FROM employees ORDER BY 1;          -- nomor kolom
SELECT last_name AS nama FROM employees ORDER BY nama; -- alias
SELECT last_name, commission_pct
  FROM employees ORDER BY commission_pct NULLS FIRST;
```

Aturan: `ASC` default; Oracle menempatkan NULL di **akhir** untuk ASC dan di **awal** untuk DESC — bisa diubah dengan `NULLS FIRST/LAST`.

## Jebakan
- `ORDER BY 1` mengacu posisi kolom, bukan nilai 1.
- Mengurutkan kolom VARCHAR berisi angka menghasilkan urutan leksikografis ('10' < '9').
- ORDER BY di subquery tidak menjamin urutan luar.
- Kolom LOB tidak bisa diurutkan langsung.

## Latihan
1. Bagaimana menempatkan NULL di awal?
2. Mengapa '10' muncul sebelum '9' pada kolom teks?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ORDER BY kolom NULLS FIRST</code>.</p>
<p><b>2.</b> Karena perbandingan teks bersifat leksikografis: karakter '1' lebih kecil dari '9'.</p>
</details>
