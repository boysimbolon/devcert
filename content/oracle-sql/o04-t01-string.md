---
title: Fungsi karakter pada SELECT dan WHERE
minutes: 20
level: Dasar
badge: lengkap
summary: UPPER, LOWER, INITCAP, SUBSTR, INSTR, LPAD, TRIM, REPLACE, LENGTH.
objectives:
  - Memakai fungsi karakter umum
  - Menerapkan fungsi pada WHERE
  - Menghindari fungsi yang mematikan index
---
## Kenapa topik ini diuji
Soal memberi ekspresi dan menanyakan hasil persisnya — termasuk posisi indeks yang dimulai dari 1.

## Konsep inti
```sql
SELECT UPPER(last_name), LOWER(job_id), INITCAP('budi santoso') FROM employees;

SELECT SUBSTR('Oracle Database', 1, 6)  AS a,   -- Oracle
       SUBSTR('Oracle Database', 8)     AS b,   -- Database
       INSTR('Oracle Database', 'a')    AS c,   -- posisi pertama
       LENGTH('Oracle')                 AS d,
       LPAD(salary, 10, '*')            AS e,
       TRIM('  teks  ')                 AS f,
       REPLACE('a-b-c','-','/')         AS g
  FROM dual;

SELECT last_name FROM employees WHERE UPPER(last_name) = 'KING';
```

## Jebakan
- `SUBSTR` dan `INSTR` berbasis 1, bukan 0.
- `INSTR` mengembalikan 0 bila tidak ditemukan (bukan NULL).
- `TRIM` hanya memangkas spasi di ujung; `REPLACE` mengganti semua kemunculan.
- `WHERE UPPER(kolom) = ...` menghalangi index; gunakan function-based index bila perlu.

## Latihan
1. Hasil `SUBSTR('Oracle', 3, 2)`?
2. Apa hasil `INSTR('abc','z')`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>'ac'</code> (mulai karakter ke-3, dua karakter).</p>
<p><b>2.</b> 0.</p>
</details>
