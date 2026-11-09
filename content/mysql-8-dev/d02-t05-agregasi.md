---
title: Agregasi dan ringkasan data
minutes: 22
level: Menengah
badge: lengkap
summary: GROUP BY, HAVING, ROLLUP, dan window function MySQL 8.0.
objectives:
  - Menulis agregasi dengan GROUP BY dan HAVING
  - Memakai window function untuk peringkat dan subtotal
  - Menghindari kesalahan ONLY_FULL_GROUP_BY
---
## Kenapa topik ini diuji
Agregasi adalah inti pelaporan. Soal menguji hasil query dan perilaku GROUP BY.

## Konsep inti
```sql
SELECT kota, COUNT(*) AS jumlah, ROUND(AVG(total),2) AS rata
  FROM pesanan p JOIN pelanggan c ON c.id = p.pelanggan_id
 GROUP BY kota
HAVING COUNT(*) > 10
 ORDER BY jumlah DESC;

-- subtotal + total keseluruhan
SELECT kota, SUM(total) AS total FROM pesanan GROUP BY kota WITH ROLLUP;

-- window function: peringkat per kota
SELECT kota, id, total,
       RANK() OVER (PARTITION BY kota ORDER BY total DESC) AS rnk,
       SUM(total) OVER (PARTITION BY kota) AS total_kota
  FROM pesanan;
```

Fungsi yang sering dipakai: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP_CONCAT`, `RANK`, `DENSE_RANK`, `ROW_NUMBER`, `SUM() OVER`, `LAG`, `LEAD`.

## Jebakan
- `WHERE` tidak bisa memfilter hasil agregat; gunakan `HAVING`.
- `GROUP BY` tanpa semua kolom non-agregat → error pada `ONLY_FULL_GROUP_BY`.
- `COUNT(kolom)` mengabaikan NULL; `COUNT(*)` tidak.
- `WITH ROLLUP` menghasilkan baris NULL yang bisa tertukar dengan nilai asli.

## Latihan
1. Klausa mana untuk memfilter hasil agregasi?
2. Perbedaan `RANK` dan `DENSE_RANK`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>HAVING</code>.</p>
<p><b>2.</b> <code>RANK</code> melompati nomor setelah seri (1,1,3); <code>DENSE_RANK</code> tidak (1,1,2).</p>
</details>
