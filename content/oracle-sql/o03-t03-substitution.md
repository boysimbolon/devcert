---
title: Substitution variable
minutes: 18
level: Dasar
badge: lengkap
summary: & dan && untuk parameter interaktif, serta kapan dipakai.
objectives:
  - Memakai & dan && dalam query
  - Membedakan keduanya
  - Menghindari salah tafsir pada string
---
## Kenapa topik ini diuji
Substitution variable adalah fitur khas Oracle SQL*Plus yang sering muncul di soal.

## Konsep inti
```sql
SELECT employee_id, last_name, salary
  FROM employees
 WHERE department_id = &dept;

-- && menyimpan nilai untuk dipakai ulang di sesi yang sama
SELECT &&kolom FROM employees WHERE department_id = 10;

-- dalam string
SELECT '&nama_karyawan' AS sapa FROM dual;
```

| Simbol | Perilaku |
|---|---|
| `&` | meminta nilai setiap kali muncul |
| `&&` | meminta sekali, dipakai ulang |
| `DEFINE` | menetapkan nilai lebih dulu |
| `UNDEFINE` | menghapus nilai |

## Jebakan
- `&` di dalam string tetap diganti; gunakan `SET DEFINE OFF` bila ingin literal.
- `&&` yang sudah terdefinisi tidak bertanya lagi — bisa membingungkan saat pengujian.
- Substitution variable hanya ada di klien (SQL*Plus/SQL Developer), bukan di SQL engine.
- Nilai berupa teks perlu kutip saat dipakai (`'&nama'`).

## Latihan
1. Perbedaan `&` dan `&&`?
2. Bagaimana menghentikan penggantian `&` pada teks biasa?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>&</code> meminta tiap kali; <code>&&</code> menyimpan untuk dipakai ulang.</p>
<p><b>2.</b> <code>SET DEFINE OFF</code>.</p>
</details>
