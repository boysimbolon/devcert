---
title: Laporan tingkat lanjut
minutes: 22
level: Lanjutan
badge: lengkap
summary: CTE, window function, pivot dengan CASE, dan laporan bertingkat.
objectives:
  - Memakai CTE untuk menyusun laporan bertahap
  - Membuat pivot kolom dinamis dengan CASE
  - Menyusun laporan berjalan (running total)
---
## Kenapa topik ini diuji
Soal laporan menguji kemampuan menyusun query kompleks tanpa prosedur.

## Konsep inti
```sql
WITH bulanan AS (
  SELECT DATE_FORMAT(tanggal,'%Y-%m') AS bln,
         SUM(total) AS total
    FROM pesanan
   GROUP BY bln
),
berjalan AS (
  SELECT bln, total,
         SUM(total) OVER (ORDER BY bln) AS kumulatif
    FROM bulanan
)
SELECT bln, total, kumulatif FROM berjalan ORDER BY bln;

-- pivot: penjualan per kota per tahun
SELECT kota,
       SUM(CASE WHEN YEAR(tanggal)=2025 THEN total ELSE 0 END) AS y2025,
       SUM(CASE WHEN YEAR(tanggal)=2026 THEN total ELSE 0 END) AS y2026
  FROM pesanan GROUP BY kota;
```

Teknik yang dipakai berulang: CTE untuk menyederhanakan, window untuk kumulatif/peringkat, `CASE` untuk pivot, dan `GROUP_CONCAT` untuk ringkasan teks.

## Jebakan
- Pivot dengan `CASE` harus menyebut kolom secara eksplisit; SQL tidak punya pivot dinamis tanpa dynamic SQL.
- `SUM(CASE ... ELSE 0)` — tanpa `ELSE 0` hasilnya NULL.
- Window function tidak bisa dipakai di `WHERE`; bungkus dengan CTE lalu filter.
- CTE rekursif membutuhkan `WITH RECURSIVE` dan kondisi berhenti.

## Latihan
1. Bagaimana memfilter hasil window function?
2. Mengapa `ELSE 0` penting pada pivot?

<details><summary>Jawaban</summary>
<p><b>1.</b> Bungkus query dalam CTE/subquery, lalu filter di query luar.</p>
<p><b>2.</b> Tanpa itu, baris yang tidak cocok menghasilkan NULL dan penjumlahan bisa NULL.</p>
</details>
