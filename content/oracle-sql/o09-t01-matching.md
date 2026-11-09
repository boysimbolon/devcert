---
title: Menyesuaikan SELECT pada operasi set
minutes: 18
level: Menengah
badge: lengkap
summary: Jumlah kolom, tipe data, dan aturan kesesuaian antar query.
objectives:
  - Menyebutkan syarat operasi set
  - Menjelaskan aturan tipe data
  - Menentukan nama kolom hasil
---
## Kenapa topik ini diuji
Operasi set gagal bila jumlah/tipe kolom tidak cocok; soal menguji aturan itu.

## Konsep inti
```sql
SELECT employee_id, last_name FROM employees
UNION
SELECT department_id, department_name FROM departments;
```

Syarat:

1. Jumlah kolom **sama** pada semua SELECT.
2. Tipe data harus kompatibel (dikonversi ke tipe dengan presedensi lebih tinggi).
3. Nama kolom hasil mengikuti SELECT **pertama**.
4. `ORDER BY` hanya boleh di akhir, memakai nama/posisi kolom dari SELECT pertama.
5. Hanya satu `ORDER BY` untuk seluruh operasi.

## Jebakan
- Jumlah kolom beda → ORA-01789.
- Tipe tidak kompatibel → ORA-01790.
- `ORDER BY` di query antara tidak diizinkan.
- Nama kolom dari SELECT pertama; alias di query kedua diabaikan.

## Latihan
1. Dari query mana nama kolom hasil diambil?
2. Berapa ORDER BY yang boleh ada?

<details><summary>Jawaban</summary>
<p><b>1.</b> Dari SELECT pertama.</p>
<p><b>2.</b> Satu, di akhir seluruh operasi set.</p>
</details>
