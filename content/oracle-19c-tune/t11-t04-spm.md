---
title: SQL Plan Management
minutes: 20
level: Menengah
badge: lengkap
summary: Plan baseline untuk menjaga plan stabil dan berevolusi secara terkendali.
objectives:
  - Menjelaskan plan baseline
  - Menangkap dan meng-evolve baseline
  - Membedakan baseline dan SQL profile
---
## Kenapa topik ini diuji
SPM mencegah regresi plan; soal menanyakan cara kerja dan perintahnya.

## Konsep inti
```sql
-- tangkap plan saat ini sebagai baseline
ALTER SYSTEM SET optimizer_capture_sql_plan_baselines = TRUE;

SELECT sql_handle, plan_name, enabled, accepted, fixed
  FROM dba_sql_plan_baselines;

-- evolve: uji plan baru, terima bila lebih baik
SET SERVEROUTPUT ON
DECLARE r PLS_INTEGER;
BEGIN
  r := DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE(sql_handle => 'SQL_xxx');
  DBMS_OUTPUT.PUT_LINE('evolved: '||r);
END;
/
```

Plan yang belum `ACCEPTED` tidak dipakai sampai di-verifikasi.

## Jebakan
- `optimizer_capture_sql_plan_baselines` global bisa menumpuk baseline.
- Baseline `FIXED` memaksa plan walau lebih buruk.
- SQL profile berbeda: ia menyesuaikan estimasi, bukan mengunci plan.
- Baseline tidak menyimpan statistik; regresi statistik tetap mungkin.

## Latihan
1. Apa bedanya baseline dan SQL profile?
2. Bagaimana plan baru bisa dipakai?

<details><summary>Jawaban</summary>
<p><b>1.</b> Baseline mengunci/memilih di antara plan yang terdaftar; SQL profile menyesuaikan estimasi optimizer.</p>
<p><b>2.</b> Di-evolve dan diterima (<code>ACCEPTED</code>) setelah terbukti lebih baik.</p>
</details>
