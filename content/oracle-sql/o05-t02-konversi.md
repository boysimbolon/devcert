---
title: Konversi tipe implisit dan eksplisit
minutes: 20
level: Dasar
badge: lengkap
summary: Kapan Oracle mengonversi otomatis, dan mengapa itu berbahaya.
objectives:
  - Membedakan konversi implisit dan eksplisit
  - Menjelaskan aturan konversi string-angka-tanggal
  - Menghindari konversi implisit yang mematikan index
---
## Kenapa topik ini diuji
Soal memberi perbandingan yang tampak benar tetapi gagal karena konversi implisit.

## Konsep inti
Oracle mengonversi otomatis bila tipe berbeda:

```sql
SELECT '100' + 50 FROM dual;                    -- 150 (string -> number)
SELECT * FROM employees WHERE hire_date = '01-JAN-2025';  -- string -> date
SELECT * FROM employees WHERE salary = '5000';  -- implisit
```

Konversi **eksplisit** selalu lebih baik:

```sql
SELECT TO_NUMBER('100') + 50 FROM dual;
SELECT * FROM employees WHERE hire_date = TO_DATE('2025-01-01','YYYY-MM-DD');
```

Bahaya implisit: format bergantung `NLS_DATE_FORMAT`/`NLS_NUMERIC_CHARACTERS`, dan `WHERE TO_CHAR(tanggal)='...'` atau `WHERE angka_kolom = '5000'` bisa menghalangi index (tergantung versi).

## Jebakan
- Format tanggal implisit berbeda antar sesi → query berhasil di satu mesin, gagal di mesin lain.
- Konversi implisit pada kolom yang di-index dapat membatalkan penggunaan index.
- `'1,000'` gagal dikonversi bila pemisah desimal berbeda.
- `TO_DATE` tanpa format memakai NLS.

## Latihan
1. Mengapa `WHERE tanggal = '01-JAN-25'` berisiko?
2. Cara eksplisit membandingkan tanggal?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena format ditafsirkan menurut NLS sesi; di lingkungan lain bisa gagal (ORA-01861).</p>
<p><b>2.</b> <code>TO_DATE('2025-01-01','YYYY-MM-DD')</code> atau literal <code>DATE '2025-01-01'</code>.</p>
</details>
