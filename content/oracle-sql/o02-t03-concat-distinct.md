---
title: Operator konkatenasi, literal, q-quote, dan DISTINCT
minutes: 20
level: Dasar
badge: lengkap
summary: Menggabungkan string, menulis literal dengan aman, dan menghapus duplikat.
objectives:
  - Memakai operator || dan literal string
  - Menulis string dengan q-quote
  - Memakai DISTINCT dengan benar
---
## Kenapa topik ini diuji
Tiga hal kecil yang sering muncul: `||`, penanganan tanda kutip tunggal, dan kapan `DISTINCT` mengubah hasil.

## Konsep inti
```sql
SELECT last_name || ', ' || job_id AS label, 'Gaji: ' || salary AS info
  FROM employees;

-- tanda kutip di dalam string: gandakan
SELECT 'It''s fine' AS contoh FROM dual;

-- q-quote: pilih delimiter sendiri
SELECT q'[It's fine]' AS contoh FROM dual;
SELECT q'{Dia bilang "halo"}' AS contoh FROM dual;

SELECT DISTINCT department_id FROM employees;
SELECT DISTINCT department_id, job_id FROM employees;   -- kombinasi unik
```

`NULL` dalam konkatenasi membuat hasilnya `NULL` (bukan diabaikan).

## Jebakan
- `|| NULL` menghasilkan NULL; gunakan `NVL(kolom, '')` bila perlu.
- `DISTINCT` berlaku untuk **seluruh** daftar kolom, bukan satu kolom saja.
- `COUNT(DISTINCT kolom)` mengabaikan NULL.
- q-quote butuh pasangan delimiter: `q'[...]'`, `q'{...}'`, `q'(...)'`.

## Latihan
1. Bagaimana menulis string yang berisi tanda kutip tunggal?
2. Apakah `DISTINCT` pada dua kolom menghasilkan unik per kolom?

<details><summary>Jawaban</summary>
<p><b>1.</b> Gandakan kutip (<code>''</code>) atau pakai q-quote <code>q'[It's]'</code>.</p>
<p><b>2.</b> Tidak, keunikannya pada kombinasi kedua kolom.</p>
</details>
