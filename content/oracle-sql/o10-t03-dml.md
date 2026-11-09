---
title: INSERT, UPDATE, dan DELETE
minutes: 20
level: Dasar
badge: lengkap
summary: Menambah, mengubah, dan menghapus baris, termasuk insert dengan subquery.
objectives:
  - Menulis INSERT dengan kolom eksplisit
  - Memakai UPDATE berbasis subquery
  - Menghapus baris secara terkendali
---
## Kenapa topik ini diuji
Soal praktis DML dengan jebakan: lupa WHERE, kolom tidak cocok, atau constraint yang dilanggar.

## Konsep inti
```sql
INSERT INTO departments (department_id, department_name, location_id)
VALUES (300, 'RISET', 1700);

INSERT INTO dept_backup (department_id, department_name)
SELECT department_id, department_name FROM departments WHERE location_id = 1700;

UPDATE employees SET salary = salary * 1.1 WHERE department_id = 50;

DELETE FROM employees WHERE employee_id = 999;

UPDATE employees e
   SET salary = (SELECT AVG(salary) FROM employees x WHERE x.department_id = e.department_id)
 WHERE department_id = 30;
```

Selalu sebutkan kolom pada INSERT agar tidak bergantung urutan kolom tabel.

## Jebakan
- `INSERT INTO t VALUES (...)` tanpa nama kolom → gagal bila jumlah kolom berubah.
- `UPDATE`/`DELETE` tanpa `WHERE` mengenai seluruh tabel.
- Melanggar `NOT NULL`/`UNIQUE`/`FOREIGN KEY` → ORA-01400/00001/02291.
- Insert ke kolom `DATE` dengan string memakai NLS; gunakan `TO_DATE`.

## Latihan
1. Mengapa kolom sebaiknya disebut eksplisit pada INSERT?
2. Error apa bila nilai NULL masuk kolom NOT NULL?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agar tidak rusak bila urutan/jumlah kolom tabel berubah.</p>
<p><b>2.</b> ORA-01400 cannot insert NULL.</p>
</details>
