---
title: Membatasi hasil grup
minutes: 18
level: Menengah
badge: lengkap
summary: HAVING vs WHERE, dan urutan evaluasi pada agregasi.
objectives:
  - Membedakan WHERE dan HAVING
  - Menulis HAVING dengan agregat
  - Menghindari alias di HAVING
---
## Kenapa topik ini diuji
Soal memberi filter dan menanyakan klausa mana yang harus dipakai.

## Konsep inti
```sql
SELECT department_id, COUNT(*) AS jumlah, AVG(salary) AS rata
  FROM employees
 WHERE salary > 3000            -- filter baris sebelum grup
 GROUP BY department_id
HAVING COUNT(*) > 5             -- filter grup setelah agregasi
 ORDER BY jumlah DESC;
```

| Klausa | Kapan dievaluasi |
|---|---|
| WHERE | sebelum pengelompokan, baris individual |
| HAVING | setelah pengelompokan, nilai agregat |

Filter pada kolom **non-agregat** sebaiknya di WHERE (lebih efisien). HAVING untuk kondisi agregat.

## Jebakan
- Memakai alias di HAVING → ORA-00904.
- Menaruh kondisi agregat di WHERE → ORA-00934 (group function not allowed here).
- HAVING tanpa GROUP BY memperlakukan seluruh tabel sebagai satu grup.
- Menaruh filter non-agregat di HAVING membuat query lebih lambat.

## Latihan
1. Klausa untuk `COUNT(*) > 5`?
2. Di mana filter `salary > 3000` sebaiknya diletakkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> HAVING.</p>
<p><b>2.</b> Di WHERE, karena menyaring baris sebelum agregasi.</p>
</details>
