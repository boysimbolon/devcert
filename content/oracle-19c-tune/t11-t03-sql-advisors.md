---
title: SQL Access dan SQL Tuning Advisor
minutes: 20
level: Menengah
badge: lengkap
summary: Rekomendasi index, restrukturisasi SQL, dan cara menjalankannya.
objectives:
  - Menjalankan SQL Tuning Advisor
  - Menjalankan SQL Access Advisor
  - Membedakan keduanya
---
## Kenapa topik ini diuji
Soal menanyakan advisor mana untuk kebutuhan tertentu (index vs rewrite).

## Konsep inti
| Advisor | Menjawab |
|---|---|
| SQL Tuning Advisor | statistik, index, rewrite, SQL profile, plan baseline untuk **satu SQL** |
| SQL Access Advisor | set index/materialized view untuk **kumpulan SQL** |

```sql
DECLARE t VARCHAR2(100);
BEGIN
  t := DBMS_SQLTUNE.CREATE_TUNING_TASK(sql_id => 'abc123');
  DBMS_SQLTUNE.EXECUTE_TUNING_TASK(t);
END;
/
SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK('TASK_1') FROM dual;
```

## Jebakan
- Rekomendasi index harus diuji dampaknya pada DML.
- SQL Tuning Advisor menganalisis satu pernyataan; untuk beban gunakan STS + Access Advisor.
- Menerima rekomendasi tanpa verifikasi bisa memperburuk plan lain.
- Butuh Tuning Pack.

## Latihan
1. Advisor untuk rekomendasi index pada banyak SQL?
2. Advisor untuk satu SQL dengan plan buruk?

<details><summary>Jawaban</summary>
<p><b>1.</b> SQL Access Advisor.</p>
<p><b>2.</b> SQL Tuning Advisor.</p>
</details>
