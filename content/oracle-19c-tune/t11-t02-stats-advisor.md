---
title: Optimizer Statistics Advisor
minutes: 18
level: Menengah
badge: lengkap
summary: Memeriksa cara statistik dikumpulkan dan memberi rekomendasi perbaikan.
objectives:
  - Menjalankan Statistics Advisor
  - Membaca temuan dan rekomendasi
  - Menerapkan rekomendasi
---
## Kenapa topik ini diuji
Fitur 12.2+ yang menilai praktik pengumpulan statistik, bukan statistik itu sendiri.

## Konsep inti
```sql
DECLARE
  t VARCHAR2(100);
BEGIN
  t := DBMS_STATS.CREATE_ADVISOR_TASK('adv_stats');
  DBMS_STATS.EXECUTE_ADVISOR_TASK('adv_stats');
END;
/

SELECT * FROM dba_advisor_findings WHERE task_name='ADV_STATS';
SELECT * FROM dba_advisor_recommendations WHERE task_name='ADV_STATS';
SELECT DBMS_STATS.REPORT_ADVISOR_TASK('adv_stats') FROM dual;
```

Rekomendasi bisa langsung diterapkan:

```sql
EXEC DBMS_STATS.IMPLEMENT_ADVISOR_TASK('adv_stats');
```

## Jebakan
- Advisor menganalisis kebijakan (mis. memakai `ANALYZE` manual), bukan kualitas data.
- Rekomendasi perlu ditinjau; ada yang mengubah preferensi global.
- Task harus dieksekusi sebelum ada findings.
- Butuh Tuning Pack untuk sebagian fitur.

## Latihan
1. Fungsi membuat task advisor statistik?
2. Apa yang dinilai advisor ini?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBMS_STATS.CREATE_ADVISOR_TASK</code>.</p>
<p><b>2.</b> Praktik pengumpulan statistik (kebijakan, preferensi), bukan isi data.</p>
</details>
