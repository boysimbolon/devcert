---
title: Non-equijoin
minutes: 18
level: Menengah
badge: lengkap
summary: Join dengan operator selain sama dengan: BETWEEN, <, >, dan pola.
objectives:
  - Menulis join berbasis rentang
  - Memakai BETWEEN dalam join
  - Membedakan equijoin dan non-equijoin
---
## Kenapa topik ini diuji
Soal menyodorkan tabel tanpa kunci bersama (mis. grade gaji) dan menanyakan query yang benar.

## Konsep inti
```sql
SELECT e.last_name, e.salary, g.grade_level
  FROM employees e
  JOIN job_grades g
    ON e.salary BETWEEN g.lowest_sal AND g.highest_sal
 ORDER BY g.grade_level, e.salary;

-- non-equijoin dengan pola teks
SELECT a.nama, b.kategori
  FROM artikel a JOIN kategori b
    ON a.judul LIKE '%' || b.kata_kunci || '%';
```

Ciri: kondisi join memakai operator selain `=`; hasilnya bisa banyak baris per baris sumber (rentang).

## Jebakan
- `BETWEEN` inklusif; batas yang tumpang tindih menghasilkan duplikasi.
- Rentang yang bolong membuat baris hilang dari hasil.
- Non-equijoin lebih mahal karena tidak bisa memakai hash/merge join sederhana.
- `LIKE` dengan wildcard di depan tidak memakai index.

## Latihan
1. Mengapa non-equijoin bisa menggandakan baris?
2. Operator apa yang khas pada non-equijoin?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena satu baris bisa cocok dengan beberapa rentang/beberapa pola.</p>
<p><b>2.</b> Selain <code>=</code>: biasanya <code>BETWEEN</code>, <code>&lt;</code>, <code>&gt;</code>, atau <code>LIKE</code>.</p>
</details>
