---
title: Fungsi tanggal
minutes: 20
level: Dasar
badge: lengkap
summary: SYSDATE, ADD_MONTHS, NEXT_DAY, LAST_DAY, MONTHS_BETWEEN, EXTRACT.
objectives:
  - Memakai fungsi tanggal umum
  - Menghitung selisih bulan
  - Menemukan akhir bulan
---
## Kenapa topik ini diuji
Fungsi tanggal sering muncul dalam soal perhitungan laporan.

## Konsep inti
```sql
SELECT SYSDATE, CURRENT_DATE, SYSTIMESTAMP FROM dual;

SELECT LAST_DAY(SYSDATE)            AS akhir_bulan,
       NEXT_DAY(SYSDATE, 'JUMAT')   AS jumat_depan,
       ADD_MONTHS(SYSDATE, -3)      AS tiga_bulan_lalu,
       MONTHS_BETWEEN(SYSDATE, hire_date) AS bulan_kerja,
       EXTRACT(YEAR FROM hire_date) AS tahun,
       EXTRACT(MONTH FROM SYSDATE)  AS bulan
  FROM employees;
```

`CURRENT_DATE` mengikuti zona waktu sesi; `SYSDATE` mengikuti zona server. `SYSTIMESTAMP` menyertakan pecahan detik dan zona waktu.

## Jebakan
- `NEXT_DAY` dengan nama hari memakai bahasa sesi (`NLS_DATE_LANGUAGE`).
- `ADD_MONTHS` pada akhir bulan menyesuaikan (31 Jan + 1 bulan = 28/29 Feb).
- `EXTRACT` hanya untuk YEAR/MONTH/DAY dari DATE, dan komponen waktu dari TIMESTAMP.
- `MONTHS_BETWEEN` bisa desimal.

## Latihan
1. Fungsi untuk akhir bulan?
2. Perbedaan SYSDATE dan CURRENT_DATE?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>LAST_DAY</code>.</p>
<p><b>2.</b> SYSDATE memakai zona waktu server; CURRENT_DATE memakai zona waktu sesi.</p>
</details>
