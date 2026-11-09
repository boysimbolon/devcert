---
title: Reoptimization otomatis dan SQL Plan Directives
minutes: 20
level: Menengah
badge: lengkap
summary: Statistik feedback, reoptimization, dan direktif untuk estimasi yang salah.
objectives:
  - Menjelaskan automatic reoptimization
  - Membaca SQL Plan Directives
  - Membersihkan direktif yang tidak berguna
---
## Kenapa topik ini diuji
Fitur ini menjelaskan plan yang berubah tanpa perubahan SQL, dan sering jadi soal.

## Konsep inti
```sql
SELECT * FROM v$sql_reoptimization_hints;
SELECT * FROM dba_sql_plan_directives;
SELECT * FROM dba_sql_plan_dir_objects;
```

- **Statistics feedback**: optimizer menyesuaikan estimasi setelah eksekusi pertama.
- **Reoptimization**: plan dibuat ulang dengan informasi baru.
- **SQL Plan Directive**: catatan bahwa sebuah kolom butuh statistik tambahan (mis. extended statistics atau histogram).

```sql
-- mematikan sementara di sesi
ALTER SESSION SET optimizer_adaptive_statistics = FALSE;
```

## Jebakan
- Direktif menumpuk dan memperlambat kompilasi bila tidak dipelihara.
- Mematikan adaptive statistics bisa mengembalikan plan buruk.
- Perbaikan sebenarnya biasanya mengumpulkan statistik (histogram/extended stats).
- Direktif tidak mengubah data; hanya memengaruhi optimizer.

## Latihan
1. View untuk direktif?
2. Apa solusi jangka panjang untuk estimasi salah?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBA_SQL_PLAN_DIRECTIVES</code>.</p>
<p><b>2.</b> Mengumpulkan statistik yang tepat (histogram, extended statistics), bukan hanya mengandalkan direktif.</p>
</details>
