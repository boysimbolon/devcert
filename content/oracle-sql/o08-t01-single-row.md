---
title: Subquery satu baris
minutes: 20
level: Menengah
badge: lengkap
summary: Subquery dengan operator =, <, >, dan kesalahan umumnya.
objectives:
  - Menulis subquery skalar
  - Menghindari ORA-01427
  - Memakai subquery di SELECT, WHERE, dan HAVING
---
## Kenapa topik ini diuji
Subquery satu baris harus mengembalikan tepat satu baris; kesalahan tipe ini sering jadi soal.

## Konsep inti
```sql
-- subquery di WHERE
SELECT last_name, salary
  FROM employees
 WHERE salary > (SELECT AVG(salary) FROM employees);

-- subquery di SELECT (skalar)
SELECT last_name,
       (SELECT department_name FROM departments d
         WHERE d.department_id = e.department_id) AS dept
  FROM employees e;

-- subquery di HAVING
SELECT department_id, AVG(salary)
  FROM employees
 GROUP BY department_id
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

Operator yang sah: `= < > <= >= <>`.

## Jebakan
- Subquery mengembalikan banyak baris → ORA-01427 "single-row subquery returns more than one row".
- Mengembalikan nol baris → hasil perbandingan NULL (tidak ada baris cocok), bukan error.
- Subquery skalar di SELECT yang mengembalikan >1 baris juga error.
- Subquery berkorelasi dieksekusi per baris → mahal bila tidak diindeks.

## Latihan
1. Error apa bila subquery memakai `=` tapi menghasilkan 3 baris?
2. Apa yang terjadi bila subquery tidak menghasilkan baris?

<details><summary>Jawaban</summary>
<p><b>1.</b> ORA-01427 single-row subquery returns more than one row.</p>
<p><b>2.</b> Perbandingan menjadi NULL sehingga tidak ada baris yang lolos (bukan error).</p>
</details>
