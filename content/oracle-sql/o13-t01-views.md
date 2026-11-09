---
title: Mengelola view
minutes: 20
level: Menengah
badge: lengkap
summary: Membuat, mengganti, dan membatasi view; updatable dan WITH CHECK OPTION.
objectives:
  - Membuat dan mengganti view
  - Menentukan view bisa di-update
  - Memakai WITH CHECK OPTION dan READ ONLY
---
## Kenapa topik ini diuji
Soal view menguji batasan update dan efek opsi.

## Konsep inti
```sql
CREATE OR REPLACE VIEW v_emp_50 AS
SELECT employee_id, last_name, salary, department_id
  FROM employees
 WHERE department_id = 50
 WITH CHECK OPTION CONSTRAINT ck_v50;

CREATE OR REPLACE VIEW v_total AS
SELECT department_id, SUM(salary) AS total
  FROM employees GROUP BY department_id;      -- read-only

CREATE OR REPLACE VIEW v_emp_ro AS
SELECT * FROM employees
WITH READ ONLY;

SELECT view_name, text FROM user_views;
```

Aturan updatable: satu tabel dasar, tanpa agregasi, `DISTINCT`, `GROUP BY`, subquery di SELECT, atau UNION.

## Jebakan
- `WITH CHECK OPTION` menolak baris yang keluar dari kondisi view.
- View dengan `GROUP BY` tidak bisa di-update.
- `CREATE OR REPLACE` mengubah definisi tanpa menghapus grant yang ada.
- View kolom dengan ekspresi harus diberi alias agar bisa dirujuk.

## Latihan
1. Opsi apa agar view tidak bisa di-update sama sekali?
2. Mengapa view agregasi read-only?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>WITH READ ONLY</code>.</p>
<p><b>2.</b> Karena satu baris view merangkum banyak baris tabel sehingga tidak bisa dipetakan balik.</p>
</details>
