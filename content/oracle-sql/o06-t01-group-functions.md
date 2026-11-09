---
title: Fungsi grup
minutes: 20
level: Menengah
badge: lengkap
summary: COUNT, SUM, AVG, MIN, MAX dan perlakuan NULL.
objectives:
  - Memakai fungsi agregat
  - Menjelaskan perbedaan COUNT(*) dan COUNT(kolom)
  - Menangani NULL dalam agregasi
---
## Kenapa topik ini diuji
Soal memberi tabel kecil dan menanyakan hasil agregasi dengan NULL.

## Konsep inti
```sql
SELECT COUNT(*)          AS semua_baris,
       COUNT(commission_pct) AS ada_komisi,
       SUM(salary)       AS total,
       AVG(salary)       AS rata,
       MIN(hire_date)    AS terlama,
       MAX(salary)       AS tertinggi
  FROM employees;
```

- `COUNT(*)` menghitung semua baris termasuk yang NULL.
- `COUNT(kolom)` hanya baris dengan kolom tidak NULL.
- `AVG(kolom)` membagi dengan jumlah nilai **tidak NULL**, bukan jumlah baris.
- `SUM`/`AVG` mengabaikan NULL; `AVG` bisa berbeda dari `SUM/COUNT(*)`.

```sql
SELECT AVG(NVL(commission_pct,0)) AS rata_dengan_nol,
       AVG(commission_pct)        AS rata_tanpa_null
  FROM employees;
```

## Jebakan
- Mengira `AVG(kolom)` = `SUM(kolom)/COUNT(*)`.
- `SUM` pada himpunan kosong = NULL, bukan 0.
- Fungsi agregat tidak boleh bercampur dengan kolom non-agregat tanpa GROUP BY.
- `COUNT(DISTINCT kolom)` mengabaikan NULL.

## Latihan
1. Mengapa dua AVG pada contoh bisa berbeda?
2. Hasil `SUM` bila tidak ada baris?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena versi NVL memasukkan nol untuk baris NULL, sedangkan AVG biasa mengabaikan baris itu.</p>
<p><b>2.</b> NULL (bukan 0).</p>
</details>
