---
title: Mengonfigurasi dan membaca log MySQL
minutes: 22
level: Dasar
badge: lengkap
summary: Error log, general log, slow query log, dan binlog: fungsi dan cara mengaktifkannya.
objectives:
  - Membedakan empat jenis log utama
  - Mengaktifkan slow query log secara dinamis
  - Menentukan isi dan rotasi log
---
## Kenapa topik ini diuji
Setiap masalah operasional dimulai dari log. Soal menanyakan log mana yang dipakai untuk kasus tertentu.

## Konsep inti
| Log | Isi | Aktif default |
|---|---|---|
| Error log | start/stop, error, warning | ya |
| General log | semua pernyataan yang diterima | tidak |
| Slow query log | query melebihi `long_query_time` | tidak |
| Binary log | perubahan data (untuk replikasi/PITR) | ya (8.0) |
| Relay log | binlog yang diterima replica | hanya replica |

```ini
[mysqld]
log_error = /var/log/mysql/error.log
slow_query_log = ON
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = ON
general_log = OFF
general_log_file = /var/log/mysql/general.log
min_examined_row_limit = 100
```

```sql
SHOW VARIABLES LIKE '%log%';
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 0.5;
SELECT * FROM mysql.slow_log\G           -- bila log_output=TABLE
SHOW VARIABLES LIKE 'log_output';         -- FILE, TABLE, atau keduanya
```

Membaca slow log:

```bash
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log      # 10 query terlama
pt-query-digest /var/log/mysql/slow.log               # ringkasan (Percona Toolkit)
```

## Jebakan
- `general_log=ON` di produksi: menulis setiap query, cepat menghabiskan disk dan membocorkan data.
- `long_query_time` hanya mencatat query yang **selesai** melewati batas; query yang menunggu lock juga tercatat.
- `log_output=TABLE` menulis ke `mysql.slow_log`, yang bisa membengkak.
- Rotasi log tanpa `FLUSH LOGS` bisa membuat file lama tetap dibuka proses.

## Latihan
1. Log mana untuk melihat query yang lambat beserta rencananya?
2. Perintah untuk memutar (rotate) log tanpa restart?

<details><summary>Jawaban</summary>
<p><b>1.</b> Slow query log (dengan <code>long_query_time</code>); analisis lanjutan lewat <code>EXPLAIN</code> atau <code>performance_schema</code>.</p>
<p><b>2.</b> <code>FLUSH LOGS;</code> (atau <code>mysqladmin flush-logs</code>).</p>
</details>
