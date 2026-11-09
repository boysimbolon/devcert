---
title: Subquery banyak baris
minutes: 20
level: Menengah
badge: lengkap
summary: IN, ANY, ALL, dan EXISTS untuk subquery yang mengembalikan banyak baris.
objectives:
  - Memakai IN dan NOT IN
  - Membedakan ANY dan ALL
  - Menghindari jebakan NULL pada NOT IN
---
## Kenapa topik ini diuji
Jebakan NULL pada `NOT IN` adalah soal favorit karena hasilnya kosong tanpa error.

## Konsep inti
```sql
SELECT last_name FROM employees
 WHERE department_id IN (SELECT department_id FROM departments WHERE location_id = 1700);

SELECT last_name FROM employees
 WHERE salary > ALL (SELECT salary FROM employees WHERE department_id = 30);

SELECT last_name FROM employees
 WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 30);

SELECT last_name FROM employees e
 WHERE EXISTS (SELECT 1 FROM departments d
                WHERE d.department_id = e.department_id AND d.location_id = 1700);
```

| Operator | Arti |
|---|---|
| `IN` | sama dengan salah satu |
| `> ALL` | lebih besar dari nilai terbesar |
| `> ANY` | lebih besar dari nilai terkecil |
| `EXISTS` | subquery mengembalikan minimal satu baris |

## Jebakan
- `NOT IN` dengan NULL di hasil subquery → hasil kosong. Gunakan `NOT EXISTS` atau tambahkan `IS NOT NULL`.
- `ANY` sering tertukar dengan `ALL`.
- `EXISTS` berhenti pada baris pertama (bisa lebih efisien).
- `IN` dengan daftar besar lebih baik sebagai join.

## Latihan
1. Mengapa `NOT IN` bisa mengembalikan nol baris?
2. Operator mana yang berarti "lebih besar dari semua nilai"?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena NULL di subquery membuat perbandingan menjadi UNKNOWN untuk semua baris.</p>
<p><b>2.</b> <code>&gt; ALL</code>.</p>
</details>
