---
title: Insert multi-tabel
minutes: 20
level: Menengah
badge: lengkap
summary: INSERT ALL, INSERT FIRST, dan pemakaian kondisi.
objectives:
  - Menulis INSERT ALL bersyarat
  - Membedakan ALL dan FIRST
  - Menghindari duplikasi baris
---
## Kenapa topik ini diuji
Fitur khas Oracle yang sering muncul di soal: arahkan baris ke beberapa tabel sekaligus.

## Konsep inti
```sql
INSERT ALL
  INTO dept_high (department_id, department_name) VALUES (department_id, department_name)
  INTO dept_low  (department_id, department_name) VALUES (department_id, department_name)
SELECT department_id, department_name FROM departments WHERE location_id = 1700;

INSERT FIRST
  WHEN salary > 10000 THEN
    INTO karyawan_senior (employee_id, salary) VALUES (employee_id, salary)
  WHEN salary > 5000 THEN
    INTO karyawan_mid (employee_id, salary) VALUES (employee_id, salary)
  ELSE
    INTO karyawan_junior (employee_id, salary) VALUES (employee_id, salary)
SELECT employee_id, salary FROM employees;
```

| Bentuk | Perilaku |
|---|---|
| `INSERT ALL` | semua klausa WHEN yang cocok dievaluasi (bisa banyak tabel) |
| `INSERT FIRST` | hanya klausa pertama yang cocok dipakai |

## Jebakan
- `INSERT ALL` bisa memasukkan satu baris ke beberapa tabel sekaligus (sering tidak diinginkan).
- `INSERT FIRST` berhenti pada kondisi pertama yang benar.
- Operasi ini atomik: satu kegagalan membatalkan seluruhnya.
- Tanpa `ELSE`, baris yang tidak cocok tidak dimasukkan.

## Latihan
1. Operator mana yang bisa mengirim satu baris ke dua tabel?
2. Apa efek ELSE pada INSERT FIRST?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>INSERT ALL</code> (jika dua klausa WHEN cocok).</p>
<p><b>2.</b> Menangkap baris yang tidak memenuhi kondisi sebelumnya, sehingga tetap dimasukkan ke tujuan ELSE.</p>
</details>
