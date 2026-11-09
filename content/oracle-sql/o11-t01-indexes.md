---
title: Mengelola index
minutes: 20
level: Menengah
badge: lengkap
summary: Membuat, menghapus, dan memilih index; kapan index diabaikan.
objectives:
  - Membuat index tunggal dan komposit
  - Menghapus index dan melihat definisinya
  - Menjelaskan kondisi index tidak dipakai
---
## Kenapa topik ini diuji
Soal optimasi dasar: index mana yang membantu, dan kapan tidak dipakai.

## Konsep inti
```sql
CREATE INDEX idx_emp_dept ON employees(department_id);
CREATE INDEX idx_emp_dept_job ON employees(department_id, job_id);
CREATE UNIQUE INDEX idx_emp_email ON employees(email);
CREATE BITMAP INDEX idx_emp_gender ON employees(gender);

DROP INDEX idx_emp_dept;

SELECT index_name, column_name, column_position
  FROM user_ind_columns WHERE table_name = 'EMPLOYEES' ORDER BY column_position;
```

Index membantu `WHERE`/`JOIN`/`ORDER BY` pada kolom selektif. Index komposit dipakai dari kolom **paling kiri**.

## Jebakan
- Fungsi pada kolom (`WHERE UPPER(nama)=...`) menghalangi index biasa.
- Index pada kolom kardinalitas rendah jarang membantu (kecuali bitmap).
- Terlalu banyak index memperlambat DML.
- Index unik otomatis dibuat untuk primary key dan unique constraint.

## Latihan
1. Index mana untuk `WHERE a=? AND b=?`?
2. Mengapa `UPPER(kolom)` menghalangi index?

<details><summary>Jawaban</summary>
<p><b>1.</b> Index komposit <code>(a,b)</code>.</p>
<p><b>2.</b> Karena index disimpan berdasarkan nilai kolom asli, bukan hasil fungsi; perlu function-based index.</p>
</details>
