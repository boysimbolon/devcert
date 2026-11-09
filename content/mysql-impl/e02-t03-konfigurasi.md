---
title: Mengonfigurasi MySQL Enterprise Server
minutes: 20
level: Menengah
badge: lengkap
summary: Option file, variabel kunci, dan konfigurasi khusus Enterprise.
objectives:
  - Menulis konfigurasi dasar server produksi
  - Mengatur variabel Enterprise yang relevan
  - Memverifikasi nilai efektif
---
## Kenapa topik ini diuji
Soal konfigurasi memberi skenario beban lalu menanyakan variabel mana yang diubah.

## Konsep inti
```ini
[mysqld]
datadir = /var/lib/mysql
port = 3306
bind-address = 10.0.0.5
max_connections = 500
innodb_buffer_pool_size = 8G
innodb_buffer_pool_instances = 8
innodb_flush_log_at_trx_commit = 1
innodb_log_file_size = 1G
slow_query_log = ON
long_query_time = 1
log_bin = mysql-bin
binlog_format = ROW

# Enterprise
thread_handling = pool-of-threads
thread_pool_size = 16
audit_log_format = JSON
```

```sql
SHOW VARIABLES LIKE 'thread_handling';
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SET PERSIST max_connections = 600;
SELECT @@global.max_connections, @@session.max_connections;
```

## Jebakan
- `thread_pool_size` sebaiknya mendekati jumlah core, bukan jumlah koneksi.
- `innodb_flush_log_at_trx_commit=2` mengorbankan durability.
- Menaruh konfigurasi di kelompok `[client]` sehingga server mengabaikannya.
- `SET PERSIST` menulis ke `mysqld-auto.cnf`, yang bisa menimpa asumsi saat rollback.

## Latihan
1. Variabel untuk model thread Enterprise?
2. Cara memastikan nilai konfigurasi benar-benar berlaku?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>thread_handling=pool-of-threads</code> dengan <code>thread_pool_size</code>.</p>
<p><b>2.</b> <code>SHOW VARIABLES</code> / <code>SELECT @@global...</code> pada server yang berjalan.</p>
</details>
