---
title: Membuat grup data
minutes: 20
level: Menengah
badge: lengkap
summary: GROUP BY satu atau banyak kolom, dan aturan kolom yang boleh dipilih.
objectives:
  - Menulis GROUP BY yang benar
  - Menjelaskan aturan kolom SELECT
  - Memakai GROUP BY dengan beberapa kolom
---
## Kenapa topik ini diuji
Kesalahan ORA-00979 (not a GROUP BY expression) adalah soal klasik.

## Konsep inti
```sql
SELECT department_id, job_id, COUNT(*) AS jumlah, SUM(salary) AS total
  FROM employees
 GROUP BY department_id, job_id
 ORDER BY department_id, job_id;

SELECT department_id, AVG(salary) FROM employees GROUP BY department_id;
```

Aturan: setiap kolom di `SELECT` yang bukan agregat **wajib** muncul di `GROUP BY`. Ekspresi juga harus sama persis.

```sql
SELECT EXTRACT(YEAR FROM hire_date) AS th, COUNT(*)
  FROM employees
 GROUP BY EXTRACT(YEAR FROM hire_date);
```

## Jebakan
- Memilih kolom yang tidak ada di GROUP BY → ORA-00979.
- Memakai alias di GROUP BY (tidak boleh; Oracle mengizinkan di ORDER BY saja).
- GROUP BY pada kolom NULL membentuk satu grup NULL.
- GROUP BY dengan ekspresi kompleks membuat query sulit dioptimasi.

## Latihan
1. Kapan ORA-00979 muncul?
2. Apakah GROUP BY membentuk grup untuk NULL?

<details><summary>Jawaban</summary>
<p><b>1.</b> Saat kolom non-agregat di SELECT tidak tercantum di GROUP BY.</p>
<p><b>2.</b> Ya, semua baris NULL dianggap satu grup.</p>
</details>
