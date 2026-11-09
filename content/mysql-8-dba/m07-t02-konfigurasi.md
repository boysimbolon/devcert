---
title: Mengonfigurasi replikasi
minutes: 24
level: Menengah
badge: lengkap
summary: GTID, CHANGE REPLICATION SOURCE, START REPLICA, dan verifikasi.
objectives:
  - Menyiapkan source dan replica dengan server_id berbeda
  - Mengonfigurasi replikasi berbasis GTID
  - Memverifikasi replikasi berjalan
---
## Kenapa topik ini diuji
Langkah-langkahnya spesifik dan sering ditanyakan berurutan. Salah satu saja membuat replikasi gagal.

## Konsep inti
Source:

```ini
[mysqld]
server_id = 1
log_bin = mysql-bin
binlog_format = ROW
gtid_mode = ON
enforce_gtid_consistency = ON
```

Replica:

```ini
[mysqld]
server_id = 2
relay_log = relay-bin
gtid_mode = ON
enforce_gtid_consistency = ON
read_only = ON
super_read_only = ON
log_replica_updates = ON
```

Menyambungkan:

```sql
CREATE USER 'repl'@'10.0.0.%' IDENTIFIED BY 'Rahasia#2026';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'10.0.0.%';

-- di replica
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='10.0.0.10',
  SOURCE_USER='repl',
  SOURCE_PASSWORD='Rahasia#2026',
  SOURCE_AUTO_POSITION=1,
  SOURCE_SSL=1;

START REPLICA;
SHOW REPLICA STATUS\G
```

Yang diperiksa: `Replica_IO_Running: Yes`, `Replica_SQL_Running: Yes`, `Seconds_Behind_Source`, `Last_Error`.

## Jebakan
- `server_id` sama di source dan replica → replikasi tidak jalan/loop.
- `SOURCE_AUTO_POSITION=1` butuh GTID aktif di **kedua** sisi.
- `read_only` tidak menghalangi user dengan `SUPER`/`CONNECTION_ADMIN`; gunakan `super_read_only`.
- Replikasi tanpa TLS akan gagal bila `require_secure_transport=ON`.

## Latihan
1. Mengapa `server_id` harus berbeda?
2. Apa syarat `SOURCE_AUTO_POSITION=1`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agar server dapat membedakan event miliknya sendiri dan menghindari loop.</p>
<p><b>2.</b> <code>gtid_mode=ON</code> dan <code>enforce_gtid_consistency=ON</code> pada source maupun replica.</p>
</details>
