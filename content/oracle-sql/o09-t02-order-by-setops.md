---
title: ORDER BY pada operasi set
minutes: 16
level: Menengah
badge: lengkap
summary: Posisi ORDER BY dan aturan nama kolom yang boleh dipakai.
objectives:
  - Menempatkan ORDER BY dengan benar
  - Memakai posisi kolom
  - Menghindari alias dari SELECT kedua
---
## Kenapa topik ini diuji
Soal memberi query gabungan lalu menanyakan apakah sintaksnya valid.

## Konsep inti
```sql
SELECT last_name AS nama FROM employees
UNION ALL
SELECT department_name AS nama FROM departments
ORDER BY nama;            -- boleh: nama dari SELECT pertama

SELECT last_name FROM employees
UNION
SELECT department_name FROM departments
ORDER BY 1;               -- boleh: posisi kolom
```

`ORDER BY` berlaku untuk hasil akhir, bukan per SELECT. Ia dievaluasi terakhir.

## Jebakan
- `ORDER BY` di dalam salah satu SELECT (kecuali dibungkus subquery) → error.
- Memakai alias dari SELECT kedua → ORA-00904.
- `ORDER BY` dengan ekspresi yang tidak ada di hasil → error.
- Tanpa `ORDER BY`, urutan hasil tidak dijamin.

## Latihan
1. Apakah alias dari SELECT kedua bisa dipakai di ORDER BY?
2. Di mana ORDER BY harus diletakkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak; gunakan nama/posisi kolom dari SELECT pertama.</p>
<p><b>2.</b> Di akhir, setelah SELECT terakhir.</p>
</details>
