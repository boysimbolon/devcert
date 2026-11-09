---
title: UPDATE dan DELETE dengan subquery berkorelasi
minutes: 20
level: Menengah
badge: lengkap
summary: Memperbarui dan menghapus baris berdasarkan nilai dari tabel lain.
objectives:
  - Menulis UPDATE dengan subquery berkorelasi
  - Menulis DELETE dengan EXISTS
  - Menghindari update yang mengenai semua baris
---
## Kenapa topik ini diuji
Soal memberi tabel dan meminta perubahan data; kesalahan umum adalah menimpa semua baris.

## Konsep inti
```sql
UPDATE employees e
   SET salary = (SELECT AVG(salary) FROM employees x WHERE x.department_id = e.department_id)
 WHERE department_id IN (SELECT department_id FROM departments WHERE location_id = 1700);

DELETE FROM employees e
 WHERE EXISTS (SELECT 1 FROM departemen_tutup d WHERE d.department_id = e.department_id);

DELETE FROM employees
 WHERE department_id IN (SELECT department_id FROM departments WHERE location_id = 1700);
```

Subquery berkorelasi di `UPDATE` dievaluasi per baris; subquery tanpa korelasi dievaluasi sekali.

## Jebakan
- `UPDATE ... SET kolom = (subquery)` tanpa `WHERE` mengisi semua baris (dan bisa NULL bila subquery kosong).
- Subquery skalar di SET harus mengembalikan satu baris; jika banyak → ORA-01427.
- `DELETE` tanpa `WHERE` menghapus seluruh tabel.
- Mengubah tabel yang sama sambil membacanya di subquery bisa memberi hasil tak terduga di beberapa DBMS (Oracle umumnya aman, tetapi periksa).

## Latihan
1. Apa akibat subquery di SET mengembalikan lebih dari satu baris?
2. Bagaimana membatasi UPDATE hanya pada departemen tertentu?

<details><summary>Jawaban</summary>
<p><b>1.</b> ORA-01427 (single-row subquery returns more than one row).</p>
<p><b>2.</b> Tambahkan klausa WHERE, mis. <code>WHERE department_id IN (...)</code>.</p>
</details>
