---
title: Pengaruh statistik terhadap optimizer
minutes: 20
level: Menengah
badge: lengkap
summary: Statistik tabel/kolom/index, histogram, dan extended statistics.
objectives:
  - Menjelaskan statistik yang dipakai optimizer
  - Menentukan kapan butuh histogram
  - Memakai extended statistics untuk korelasi kolom
---
## Kenapa topik ini diuji
Hampir semua plan buruk berakar pada statistik yang salah atau tidak ada.

## Konsep inti
```sql
EXEC DBMS_STATS.GATHER_TABLE_STATS('HR','EMPLOYEES', cascade => TRUE);

SELECT table_name, num_rows, last_analyzed FROM user_tab_statistics;
SELECT column_name, num_distinct, histogram, last_analyzed FROM user_tab_col_statistics;

-- histogram untuk distribusi miring
EXEC DBMS_STATS.GATHER_TABLE_STATS('HR','EMPLOYEES',
     method_opt => 'FOR COLUMNS SIZE 254 department_id');

-- statistik gabungan kolom berkorelasi
SELECT DBMS_STATS.CREATE_EXTENDED_STATS(NULL,'EMPLOYEES','(department_id,job_id)') FROM dual;
```

Komponen: `NUM_ROWS`, `NUM_DISTINCT`, `NUM_NULLS`, histogram (frekuensi/height-balanced), dan clustering factor untuk index.

## Jebakan
- Statistik usang setelah load besar → plan berubah memburuk.
- Histogram pada kolom dengan sedikit nilai unik tidak perlu.
- Extended statistics diperlukan untuk kolom yang saling berkorelasi (mis. kota + provinsi).
- `DBMS_STATS` lebih disarankan daripada `ANALYZE`.

## Latihan
1. Kapan histogram dibutuhkan?
2. Masalah apa yang diselesaikan extended statistics?

<details><summary>Jawaban</summary>
<p><b>1.</b> Saat distribusi nilai tidak merata dan kolom dipakai di filter selektif.</p>
<p><b>2.</b> Estimasi yang salah akibat korelasi antar kolom.</p>
</details>
