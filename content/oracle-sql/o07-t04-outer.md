---
title: OUTER join
minutes: 20
level: Menengah
badge: lengkap
summary: LEFT, RIGHT, dan FULL OUTER, serta tanda (+) gaya lama.
objectives:
  - Memilih arah outer join yang tepat
  - Menemukan baris tanpa pasangan
  - Menghindari filter yang membatalkan outer join
---
## Kenapa topik ini diuji
Soal sangat sering: "tampilkan departemen yang belum punya pegawai". Arah join menentukan jawaban.

## Konsep inti
```sql
-- semua departemen, termasuk tanpa pegawai
SELECT d.department_name, COUNT(e.employee_id) AS jumlah
  FROM departments d
  LEFT JOIN employees e ON e.department_id = d.department_id
 GROUP BY d.department_name;

-- setara gaya lama
SELECT d.department_name, e.last_name
  FROM departments d, employees e
 WHERE d.department_id = e.department_id(+);

-- FULL OUTER
SELECT d.department_name, e.last_name
  FROM departments d FULL OUTER JOIN employees e
    ON e.department_id = d.department_id;
```

## Jebakan
- Menambahkan `WHERE e.salary > 1000` membatalkan LEFT JOIN (jadi INNER). Pindahkan kondisi ke klausa ON.
- `COUNT(*)` pada outer join menghitung baris placeholder; gunakan `COUNT(kolom_kanan)`.
- MySQL tidak punya FULL OUTER, Oracle punya — jangan tertukar.
- Tanda `(+)` hanya di satu sisi; menaruhnya di dua sisi = error.

## Latihan
1. Join untuk departemen tanpa pegawai?
2. Mengapa filter di WHERE membatalkan outer join?

<details><summary>Jawaban</summary>
<p><b>1.</b> LEFT JOIN dari departments ke employees lalu filter <code>e.employee_id IS NULL</code>.</p>
<p><b>2.</b> Karena baris tanpa pasangan memiliki nilai NULL pada tabel kanan, sehingga kondisi WHERE menyaringnya.</p>
</details>
