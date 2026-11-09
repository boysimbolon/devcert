---
title: Service untuk memantau performa aplikasi
minutes: 20
level: Menengah
badge: lengkap
summary: Mengelompokkan beban per aplikasi lewat service dan mengukur kinerjanya.
objectives:
  - Membuat dan memakai service
  - Melihat metrik per service
  - Menghubungkan service dengan workload
---
## Kenapa topik ini diuji
Service adalah cara Oracle memisahkan beban aplikasi; soal menanyakan manfaat dan perintahnya.

## Konsep inti
```sql
EXEC DBMS_SERVICE.CREATE_SERVICE('svc_app', 'svc_app');
EXEC DBMS_SERVICE.START_SERVICE('svc_app');

-- metrik per service
SELECT service_name, elapsed_time, cpu_time, db_time
  FROM v$service_stats;

SELECT * FROM v$servicemetric_history WHERE service_name = 'svc_app';
```

Aplikasi terhubung dengan `SERVICE_NAME=svc_app` di TNS/DSN. Memungkinkan: pembatasan resource (Resource Manager), metrik terpisah, dan failover per service di RAC.

## Jebakan
- Service tanpa `DBMS_SERVICE.START_SERVICE` tidak menerima koneksi.
- Metrik service hanya berguna bila aplikasi benar-benar memakai service tersebut.
- Nama service berbeda dari SID/instance.
- Pembersihan service yang tidak terpakai perlu `DELETE_SERVICE`.

## Latihan
1. Paket untuk membuat service?
2. Apa manfaat metrik per service?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBMS_SERVICE</code>.</p>
<p><b>2.</b> Memisahkan dan mengukur beban per aplikasi sehingga tuning lebih terarah.</p>
</details>
