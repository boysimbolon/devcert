---
title: Operator MINUS
minutes: 16
level: Menengah
badge: lengkap
summary: Selisih himpunan, arah operan, dan perbandingan dengan NOT IN.
objectives:
  - Memakai MINUS dengan arah benar
  - Membedakan MINUS dan NOT IN
  - Memahami perlakuan NULL
---
## Kenapa topik ini diuji
Arah operan MINUS sering dibalik, dan hasilnya berbeda.

## Konsep inti
```sql
-- departemen yang tidak punya pegawai
SELECT department_id FROM departments
MINUS
SELECT department_id FROM employees
ORDER BY department_id;

-- setara
SELECT d.department_id FROM departments d
 WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.department_id);
```

```text
A = {1,2,3}   B = {2,3,4}
A MINUS B = {1}      (bukan {4})
```

## Jebakan
- Urutan operan menentukan hasil; `B MINUS A` berbeda.
- MINUS menghapus duplikat.
- `NOT IN` dengan NULL bisa menghasilkan kosong; MINUS tidak bermasalah dengan NULL.
- Jumlah/tipe kolom harus cocok.

## Latihan
1. Hasil `{1,2,3} MINUS {2,3,4}`?
2. Operasi mana yang lebih aman terhadap NULL: MINUS atau NOT IN?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>{1}</code>.</p>
<p><b>2.</b> MINUS (NOT IN bisa kosong bila ada NULL).</p>
</details>
