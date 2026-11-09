---
title: Perintah DEFINE dan VERIFY
minutes: 16
level: Dasar
badge: lengkap
summary: Mengelola nilai substitution dan menampilkan query sebelum/sesudah penggantian.
objectives:
  - Menetapkan nilai dengan DEFINE
  - Menghapus dengan UNDEFINE
  - Memakai VERIFY untuk memeriksa hasil penggantian
---
## Kenapa topik ini diuji
Soal kecil yang menguji pengetahuan lingkungan SQL*Plus, bukan sintaks SQL.

## Konsep inti
```sql
DEFINE dept = 10
SELECT last_name FROM employees WHERE department_id = &dept;

DEFINE nama = 'Budi'          -- teks perlu kutip
SELECT '&nama' FROM dual;

UNDEFINE dept

SET VERIFY ON
-- menampilkan "old: ... AND department_id = &dept"
--             "new: ... AND department_id = 10"
```

`DEFINE` tanpa argumen menampilkan semua variabel yang terdefinisi.

## Jebakan
- `DEFINE` menyimpan sebagai teks; angka tidak dikonversi otomatis.
- `VERIFY` hanya menampilkan, tidak mengubah hasil.
- Variabel hilang saat sesi berakhir.
- `&&` yang sudah terdefinisi memakai nilai lama tanpa bertanya.

## Latihan
1. Perintah menampilkan semua variabel terdefinisi?
2. Apa fungsi VERIFY?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DEFINE</code> tanpa argumen.</p>
<p><b>2.</b> Menampilkan teks query sebelum dan sesudah penggantian variabel.</p>
</details>
