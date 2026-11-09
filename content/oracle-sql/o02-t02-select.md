---
title: Pernyataan SELECT
minutes: 18
level: Dasar
badge: lengkap
summary: Struktur SELECT, proyeksi kolom, dan urutan eksekusi klausa.
objectives:
  - Menulis SELECT dasar
  - Menjelaskan urutan evaluasi klausa
  - Memakai SELECT * secara sadar
---
## Kenapa topik ini diuji
Urutan eksekusi klausa sering ditanyakan dan menjelaskan banyak kesalahan.

## Konsep inti
```sql
SELECT department_id, COUNT(*) AS jumlah
  FROM employees
 WHERE salary > 5000
 GROUP BY department_id
HAVING COUNT(*) > 3
 ORDER BY jumlah DESC
 FETCH FIRST 5 ROWS ONLY;
```

Urutan **evaluasi** (bukan penulisan):

```text
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> FETCH
```

Karena `SELECT` dievaluasi setelah `WHERE`, alias kolom tidak bisa dipakai di `WHERE` tetapi bisa di `ORDER BY`.

`SELECT *` mengambil semua kolom; berisiko pada aplikasi karena skema bisa berubah dan kolom besar ikut terbaca.

## Jebakan
- Mengira `SELECT` dievaluasi lebih dulu daripada `WHERE`.
- Memakai alias di `HAVING` (tidak boleh; ulangi ekspresinya).
- `FETCH FIRST` tanpa `ORDER BY` memberi baris acak.
- `SELECT *` pada join bisa menghasilkan kolom duplikat bernama sama.

## Latihan
1. Klausa mana dievaluasi lebih dulu: WHERE atau SELECT?
2. Apakah alias boleh di HAVING?

<details><summary>Jawaban</summary>
<p><b>1.</b> WHERE (SELECT dievaluasi setelah WHERE).</p>
<p><b>2.</b> Tidak; ulangi ekspresi agregatnya di HAVING.</p>
</details>
