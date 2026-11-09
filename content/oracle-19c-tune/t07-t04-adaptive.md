---
title: Adaptive dan dynamic execution plan
minutes: 20
level: Menengah
badge: lengkap
summary: Adaptive plans, statistics feedback, dan plan yang berubah saat runtime.
objectives:
  - Menjelaskan adaptive plan
  - Membaca catatan di DBMS_XPLAN
  - Menilai kapan adaptif merugikan
---
## Kenapa topik ini diuji
Adaptive plan adalah fitur 12c+ yang sering muncul di soal, termasuk tanda-tandanya di plan.

## Konsep inti
Oracle dapat memilih join method saat runtime bila cardinality tidak pasti. Tanda di plan: `- this is an adaptive plan` dan operasi `HASH JOIN` yang bisa beralih ke `NESTED LOOPS`.

```sql
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, 'ADAPTIVE'));
SELECT * FROM v$sql WHERE is_resolved_adaptive_plan = 'Y';
```

Pengaturan:

```sql
ALTER SYSTEM SET optimizer_adaptive_plans = TRUE;
ALTER SESSION SET optimizer_adaptive_reporting_only = TRUE;   -- hanya laporkan
```

## Jebakan
- Plan bisa berbeda antar eksekusi → sulit direproduksi.
- Statistik yang baik membuat adaptive jarang perlu.
- `reporting_only` tidak mengubah plan, hanya memberi info.
- Adaptive plan tidak memperbaiki SQL yang memang buruk; hanya memilih join yang lebih baik.

## Latihan
1. Bagaimana menandai adaptive plan di DBMS_XPLAN?
2. Apa efek `optimizer_adaptive_reporting_only`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Muncul catatan <code>this is an adaptive plan</code> (format ADAPTIVE).</p>
<p><b>2.</b> Plan tidak diubah saat runtime; Oracle hanya melaporkan apa yang akan dilakukan.</p>
</details>
