---
title: Diagnosis dengan ADDM
minutes: 20
level: Menengah
badge: lengkap
summary: Automatic Database Diagnostic Monitor: temuan otomatis dan rekomendasinya.
objectives:
  - Menjalankan ADDM untuk rentang snapshot
  - Membaca temuan dan rekomendasi
  - Membedakan symptom dan root cause
---
## Kenapa topik ini diuji
ADDM adalah alat diagnosis utama Oracle; soal menanyakan output dan cara menjalankannya.

## Konsep inti
```sql
EXEC DBMS_ADVISOR.SET_TASK_PARAMETER(
  task_name => 'ADDM:12345_12355', parameter => 'START_SNAPSHOT', value => 12345);

-- menjalankan untuk rentang snapshot
DECLARE t VARCHAR2(100);
BEGIN
  t := DBMS_ADDM.ANALYZE_DB('TASK_ADDM', 12345, 12355);
END;
/

SELECT task_name, description FROM dba_advisor_tasks WHERE advisor_name='ADDM';
SELECT * FROM dba_advisor_findings WHERE task_name='TASK_ADDM';
SELECT * FROM dba_advisor_recommendations WHERE task_name='TASK_ADDM';
```

ADDM menjawab: **apa** yang menghabiskan DB time dan **apa** rekomendasinya, dengan estimasi dampak.

## Jebakan
- ADDM menganalisis per rentang snapshot, bukan real time.
- Rekomendasi harus dinilai: tidak semua cocok untuk aplikasi.
- Temuan bisa berupa symptom (mis. "I/O lambat") dengan akar di SQL.
- Butuh Diagnostic/Tuning Pack untuk fitur penuh.

## Latihan
1. Dua keluaran utama ADDM?
2. Mengapa rekomendasi ADDM tidak selalu diterapkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Findings dan recommendations (+ estimasi dampak).</p>
<p><b>2.</b> Karena bisa mengubah perilaku aplikasi atau tidak sesuai kebijakan; tetap perlu penilaian DBA.</p>
</details>
