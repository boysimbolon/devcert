---
title: Time model
minutes: 20
level: Menengah
badge: lengkap
summary: DB time, DB CPU, dan pemecahan waktu tunggu menjadi komponen yang bisa ditindak.
objectives:
  - Menjelaskan DB time dan hubungannya dengan response time
  - Membaca V$SYS_TIME_MODEL dan V$SESS_TIME_MODEL
  - Membedakan DB CPU dan wait time
---
## Kenapa topik ini diuji
Time model adalah kerangka utama: semua analisis performa berpangkal pada pembagian waktu.

## Konsep inti
```text
DB time = DB CPU + time waited on non-idle events
        (akumulasi seluruh sesi aktif, bukan waktu jam dinding)
```

```sql
SELECT stat_name, value/1e6 AS detik
  FROM v$sys_time_model
 WHERE stat_name IN ('DB time','DB CPU','background cpu time','parse time elapsed','hard parse elapsed time');

SELECT sid, stat_name, value/1e6 AS detik
  FROM v$sess_time_model
 WHERE sid = 140 AND stat_name = 'DB time';
```

Interpretasi: bila DB time jauh lebih besar dari DB CPU, sebagian besar waktu habis menunggu (I/O, lock, log sync). Bila DB CPU dominan, masalahnya di kerja CPU (parse, sort, join).

## Jebakan
- DB time bisa melebihi waktu jam dinding karena banyak sesi paralel.
- Background CPU tidak termasuk DB CPU.
- Time model kumulatif; gunakan selisih antar snapshot (AWR).
- Parse time besar menandakan hard parse berlebih (bind variable hilang).

## Latihan
1. Apa arti DB time >> DB CPU?
2. Bagaimana mengukur kontribusi parse?

<details><summary>Jawaban</summary>
<p><b>1.</b> Sebagian besar waktu dihabiskan menunggu (I/O, lock, log file sync).</p>
<p><b>2.</b> Statistik <code>parse time elapsed</code> dan <code>hard parse elapsed time</code> pada time model.</p>
</details>
