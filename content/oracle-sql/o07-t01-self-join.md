---
title: Self join
minutes: 18
level: Menengah
badge: lengkap
summary: Menggabungkan tabel dengan dirinya sendiri memakai dua alias.
objectives:
  - Menulis self join
  - Menjelaskan mengapa alias wajib
  - Memakai untuk relasi hierarki
---
## Kenapa topik ini diuji
Self join menguji pemahaman alias dan kardinalitas.

## Konsep inti
```sql
SELECT e.last_name AS pegawai, m.last_name AS manajer
  FROM employees e
  LEFT JOIN employees m ON e.manager_id = m.employee_id
 ORDER BY e.last_name;

-- hierarki dua tingkat
SELECT e.last_name, m.last_name AS atasan, g.last_name AS atasan_atasan
  FROM employees e
  LEFT JOIN employees m ON e.manager_id = m.employee_id
  LEFT JOIN employees m2 ON m.manager_id = m2.employee_id;
```

Alias berbeda wajib: tanpa alias, Oracle tidak bisa membedakan dua peran tabel yang sama.

## Jebakan
- Tanpa alias → ORA-00918 kolom ambigu.
- INNER JOIN pada relasi manajer menghilangkan baris tanpa manajer; gunakan LEFT.
- Relasi hierarki dalam (CONNECT BY) berbeda dari self join biasa.
- Alias tabel harus dipakai pada semua referensi kolom untuk kejelasan.

## Latihan
1. Mengapa alias tabel wajib pada self join?
2. Join apa agar pegawai tanpa manajer tetap muncul?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agar dua kemunculan tabel yang sama bisa dibedakan.</p>
<p><b>2.</b> LEFT OUTER JOIN.</p>
</details>
