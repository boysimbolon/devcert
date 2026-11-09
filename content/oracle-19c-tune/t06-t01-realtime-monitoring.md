---
title: Real-Time Database Operation Monitoring
minutes: 20
level: Menengah
badge: lengkap
summary: Melacak satu operasi bisnis lintas layer dengan DBMS_SQL_MONITOR.
objectives:
  - Menjelaskan konsep database operation
  - Memulai dan mengakhiri monitoring
  - Membaca laporan operasi
---
## Kenapa topik ini diuji
Fitur 12c+ ini menguji pemahaman monitoring berkelanjutan per operasi, bukan per SQL tunggal.

## Konsep inti
```sql
-- mulai memantau satu operasi
BEGIN
  DBMS_SQL_MONITOR.BEGIN_OPERATION(
    dbop_name => 'proses_tagihan_bulanan', forced_tracking => 'Y');
END;
/

-- ... jalankan serangkaian SQL aplikasi ...

BEGIN
  DBMS_SQL_MONITOR.END_OPERATION(dbop_name => 'proses_tagihan_bulanan');
END;
/

SELECT dbop_name, status, total_time, database_time
  FROM v$sql_monitor WHERE dbop_name = 'proses_tagihan_bulanan';
```

Laporan: DBMS_SQL_MONITOR.REPORT_SQL_MONITOR atau EM.

## Jebakan
- Data hanya tersedia bila monitoring aktif (`STATISTICS_LEVEL=TYPICAL/ALL`) atau forced.
- Operasi harus punya nama unik agar bisa dilacak.
- Monitoring jangka panjang butuh SQL Monitoring Repository.
- Overhead ada, walaupun kecil.

## Latihan
1. Prosedur memulai operasi monitoring?
2. Sumber data real-time-nya?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBMS_SQL_MONITOR.BEGIN_OPERATION</code>.</p>
<p><b>2.</b> <code>V$SQL_MONITOR</code> (dan repository untuk historis).</p>
</details>
