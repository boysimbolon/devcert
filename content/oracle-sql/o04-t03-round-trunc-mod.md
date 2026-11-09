---
title: ROUND, TRUNC, dan MOD
minutes: 18
level: Dasar
badge: lengkap
summary: Pembulatan, pemotongan, dan sisa bagi — termasuk untuk tanggal.
objectives:
  - Membedakan ROUND dan TRUNC
  - Memakai MOD untuk sisa bagi
  - Menerapkan ROUND/TRUNC pada tanggal
---
## Kenapa topik ini diuji
Soal memberi angka desimal dan menanyakan hasil persis; ROUND dan TRUNC sering tertukar.

## Konsep inti
```sql
SELECT ROUND(45.923, 2)  FROM dual;   -- 45.92
SELECT ROUND(45.925, 2)  FROM dual;   -- 45.93
SELECT TRUNC(45.929, 2)  FROM dual;   -- 45.92
SELECT ROUND(45.923, -1) FROM dual;   -- 50
SELECT TRUNC(45.923, -1) FROM dual;   -- 40
SELECT MOD(10, 3)        FROM dual;   -- 1

-- pada tanggal
SELECT ROUND(SYSDATE, 'MM') FROM dual;   -- awal bulan terdekat
SELECT TRUNC(SYSDATE, 'MM') FROM dual;   -- awal bulan berjalan
SELECT TRUNC(SYSDATE, 'YYYY') FROM dual; -- 1 Januari tahun ini
```

## Jebakan
- `ROUND(x, -1)` membulatkan ke puluhan, bukan selalu ke atas.
- `TRUNC` tidak pernah membulatkan, hanya memotong.
- `MOD` dengan pembagi 0 mengembalikan nilai pertama (bukan error) di Oracle.
- ROUND/TRUNC tanggal memakai format (`'MM'`, `'YYYY'`, `'DD'`).

## Latihan
1. Hasil `TRUNC(45.999, 2)`?
2. Bagaimana mendapatkan hari pertama bulan berjalan?

<details><summary>Jawaban</summary>
<p><b>1.</b> 45.99.</p>
<p><b>2.</b> <code>TRUNC(SYSDATE, 'MM')</code>.</p>
</details>
