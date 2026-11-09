---
title: Diagnosis dengan ASH
minutes: 20
level: Menengah
badge: lengkap
summary: Sampel sesi aktif per detik, pemakaian top event/session/module.
objectives:
  - Menjelaskan cara kerja sampling ASH
  - Menganalisis top event dan top SQL
  - Membedakan ASH report dan AWR
---
## Kenapa topik ini diuji
ASH menjawab "apa yang terjadi saat itu", berbeda dari AWR yang merangkum rentang.

## Konsep inti
ASH mengambil sampel sesi aktif tiap detik; `V$ACTIVE_SESSION_HISTORY` menyimpan sampel terakhir (in-memory), `DBA_HIST_ACTIVE_SESS_HISTORY` untuk historis.

```sql
SELECT event, COUNT(*) AS sampel
  FROM v$active_session_history
 WHERE sample_time > SYSTIMESTAMP - INTERVAL '10' MINUTE
 GROUP BY event ORDER BY sampel DESC;

SELECT sql_id, COUNT(*) sampel
  FROM v$active_session_history
 WHERE sample_time > SYSTIMESTAMP - INTERVAL '10' MINUTE AND sql_id IS NOT NULL
 GROUP BY sql_id ORDER BY sampel DESC FETCH FIRST 10 ROWS ONLY;

-- laporan ASH
@?/rdbms/admin/ashrpt.sql
```

## Jebakan
- ASH di memori hanya menyimpan beberapa jam (tergantung konfigurasi).
- Sampel bukan hitungan pasti; gunakan proporsi.
- Event idle tidak muncul sebagai "aktif".
- ASH report butuh rentang waktu; di luar retensi gunakan AWR.

## Latihan
1. View ASH real-time?
2. Apa keunggulan ASH dibanding AWR?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>V$ACTIVE_SESSION_HISTORY</code>; historis di <code>DBA_HIST_ACTIVE_SESS_HISTORY</code>.</p>
<p><b>2.</b> Resolusi per detik sehingga cocok untuk insiden singkat.</p>
</details>
