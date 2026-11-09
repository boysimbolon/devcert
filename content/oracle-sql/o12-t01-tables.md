---
title: Menggambarkan dan bekerja dengan tabel
minutes: 18
level: Dasar
badge: lengkap
summary: Melihat struktur, menyalin tabel, dan memberi komentar.
objectives:
  - Melihat struktur tabel
  - Menyalin struktur dan data
  - Menambahkan komentar
---
## Kenapa topik ini diuji
Soal praktis: perintah mana untuk melihat kolom, dan bagaimana menyalin tabel.

## Konsep inti
```sql
DESCRIBE employees;

SELECT column_name, data_type, nullable, data_default
  FROM user_tab_columns WHERE table_name = 'EMPLOYEES';

-- salin struktur dan data
CREATE TABLE emp_copy AS SELECT * FROM employees;
-- salin struktur saja
CREATE TABLE emp_kosong AS SELECT * FROM employees WHERE 1 = 0;

COMMENT ON TABLE employees IS 'Data pegawai';
COMMENT ON COLUMN employees.salary IS 'Gaji bulanan';
```

## Jebakan
- `CREATE TABLE AS SELECT` tidak menyalin constraint (kecuali NOT NULL) dan index.
- `WHERE 1=0` menyalin struktur tanpa baris.
- Nama objek tanpa tanda kutip disimpan huruf besar.
- `DESCRIBE` hanya di SQL*Plus/SQL Developer, bukan perintah SQL standar.

## Latihan
1. Bagaimana menyalin struktur tabel saja?
2. Apakah CTAS menyalin primary key?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>CREATE TABLE baru AS SELECT * FROM lama WHERE 1=0;</code></p>
<p><b>2.</b> Tidak; constraint perlu dibuat ulang.</p>
</details>
