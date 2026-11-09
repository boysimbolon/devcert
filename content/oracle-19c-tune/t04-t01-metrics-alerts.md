---
title: Metric threshold dan alert
minutes: 18
level: Menengah
badge: lengkap
summary: Server-generated alerts, metric baseline, dan ambang yang bisa diatur.
objectives:
  - Melihat metric dan alert
  - Mengatur threshold
  - Membedakan state warning vs critical
---
## Kenapa topik ini diuji
Soal menanyakan cara mengatur peringatan untuk metrik tertentu.

## Konsep inti
```sql
SELECT metric_name, value FROM v$sysmetric WHERE group_id = 2;
SELECT reason, object_name, message_type FROM dba_outstanding_alerts;
SELECT * FROM dba_alert_history ORDER BY creation_time DESC FETCH FIRST 10 ROWS ONLY;

-- mengatur ambang
EXEC DBMS_SERVER_ALERT.SET_THRESHOLD(
  metrics_id => DBMS_SERVER_ALERT.CPU_TIME_PER_CALL,
  warning_value => 5000000, critical_value => 10000000,
  observation_period => 1, consecutive_occurrences => 2,
  instance_name => NULL, object_type => DBMS_SERVER_ALERT.OBJECT_TYPE_SERVICE,
  object_name => 'svc_app');
```

State: `WARNING` dan `CRITICAL`. Alert juga bisa dikirim lewat email/EM.

## Jebakan
- Ambang terlalu ketat → alert fatigue.
- Threshold default jarang cocok untuk beban spesifik.
- Alert hilang setelah di-acknowledge; riwayat tetap di `dba_alert_history`.
- Metric % dari baseline butuh baseline yang sudah ada.

## Latihan
1. View untuk alert yang belum ditangani?
2. Fungsi untuk mengatur ambang?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBA_OUTSTANDING_ALERTS</code>.</p>
<p><b>2.</b> <code>DBMS_SERVER_ALERT.SET_THRESHOLD</code>.</p>
</details>
