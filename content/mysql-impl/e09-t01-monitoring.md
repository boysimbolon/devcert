---
title: Teknik memantau MySQL
minutes: 22
level: Menengah
badge: lengkap
summary: Status counters, performance_schema, sys schema, log, dan Enterprise Monitor.
objectives:
  - Memilih alat pantau sesuai pertanyaan
  - Membaca metrik kunci
  - Menyusun baseline dan alert
---
## Kenapa topik ini diuji
Soal monitoring menanyakan sumber data untuk pertanyaan operasional tertentu.

## Konsep inti
| Pertanyaan | Sumber |
|---|---|
| Server sehat? | `SHOW GLOBAL STATUS`, uptime, `Threads_connected` |
| Query lambat? | slow query log, `sys.statement_analysis` |
| Lock menumpuk? | `sys.innodb_lock_waits`, `INNODB_TRX` |
| Buffer cukup? | hit rate `Innodb_buffer_pool_reads/read_requests` |
| Replikasi tertinggal? | `SHOW REPLICA STATUS`, heartbeat table |
| Historis & advisory | MySQL Enterprise Monitor |
| Perubahan konfigurasi | audit log, `performance_schema.variables_info` |

```sql
SELECT * FROM sys.metrics WHERE Variable_name IN
  ('Threads_connected','Threads_running','Questions','Slow_queries');
SELECT * FROM sys.statement_analysis ORDER BY total_latency DESC LIMIT 10;
```

Metrik status bersifat kumulatif — yang bermakna adalah **selisih per waktu** (rate), bukan angka mentah.

## Jebakan
- Melihat angka status absolut lalu menyimpulkan tren.
- Tidak punya baseline, jadi tidak tahu "normal" itu apa.
- Alert tanpa ambang yang masuk akal → alert fatigue.
- Mengabaikan metrik OS (disk, CPU steal) padahal DB bergantung padanya.

## Latihan
1. Metrik untuk menilai efektivitas buffer pool?
2. Mengapa baseline penting?

<details><summary>Jawaban</summary>
<p><b>1.</b> Hit rate: 1 − <code>Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests</code>.</p>
<p><b>2.</b> Tanpa baseline, angka tidak bisa ditafsirkan sebagai normal atau bermasalah.</p>
</details>
