---
title: Berbagai jenis join
minutes: 20
level: Menengah
badge: lengkap
summary: INNER, NATURAL, USING, ON, dan join lintas banyak tabel.
objectives:
  - Menulis join dengan ON dan USING
  - Menjelaskan risiko NATURAL JOIN
  - Menggabungkan lebih dari dua tabel
---
## Kenapa topik ini diuji
Sintaks `USING` dan `NATURAL` punya aturan khusus (kolom tidak boleh diberi prefix).

## Konsep inti
```sql
-- ON eksplisit (disarankan)
SELECT e.last_name, d.department_name
  FROM employees e JOIN departments d
    ON e.department_id = d.department_id;

-- USING: kolom muncul sekali, tanpa prefix
SELECT last_name, department_name
  FROM employees JOIN departments USING (department_id);

-- NATURAL: join otomatis pada semua kolom bernama sama (berisiko)
SELECT last_name, department_name
  FROM employees NATURAL JOIN departments;

-- tiga tabel
SELECT e.last_name, d.department_name, l.city
  FROM employees e
  JOIN departments d ON d.department_id = e.department_id
  JOIN locations l   ON l.location_id = d.location_id;
```

## Jebakan
- Pada `USING`, kolom join **tidak boleh** diberi alias tabel (`e.department_id` → ORA-25154).
- `NATURAL JOIN` bisa memakai kolom tak terduga yang kebetulan bernama sama.
- `NATURAL JOIN` tidak bisa memakai `ON`/`USING` sekaligus.
- Join tipe lama (`WHERE e.dept = d.dept`) masih valid, tetapi tidak mendukung OUTER.

## Latihan
1. Apa risiko NATURAL JOIN?
2. Mengapa `e.department_id` gagal saat memakai USING?

<details><summary>Jawaban</summary>
<p><b>1.</b> Join terjadi pada semua kolom bernama sama, yang mungkin bukan maksud query.</p>
<p><b>2.</b> Karena kolom join hanya muncul sekali dan tidak dimiliki alias mana pun.</p>
</details>
