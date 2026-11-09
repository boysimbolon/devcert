---
title: MySQL InnoDB Cluster
minutes: 22
level: Menengah
badge: lengkap
summary: Tiga komponen cluster, mode single-primary, dan peran Router.
objectives:
  - Menyebutkan komponen InnoDB Cluster
  - Menjelaskan syarat instance
  - Mengetahui fungsi Router dan port-nya
---
## Kenapa topik ini diuji
Soal arsitektur HA: komponen apa saja dan siapa menghadap aplikasi.

## Konsep inti
```text
MySQL Shell AdminAPI  -> membuat/mengelola cluster
Group Replication     -> konsistensi antar anggota (Paxos)
MySQL Router          -> routing aplikasi ke primary/secondary
```

Syarat instance:

```ini
[mysqld]
server_id = 1
gtid_mode = ON
enforce_gtid_consistency = ON
binlog_format = ROW
log_replica_updates = ON
binlog_checksum = NONE
```

Port Router: 6446 (baca-tulis), 6447 (baca-saja), 64460/64470 klasik.

```javascript
dba.configureInstance('root@ic1:3306');
var c = dba.createCluster('prodCluster');
c.addInstance('root@ic2:3306');
c.status();
```

## Jebakan
- Cluster 2 anggota tidak punya toleransi kegagalan (butuh quorum).
- Semua tabel harus punya primary key.
- `binlog_checksum` harus `NONE`.
- Router perlu bootstrap ulang bila metadata cluster berubah.

## Latihan
1. Port baca-tulis Router?
2. Berapa anggota minimum untuk toleransi satu kegagalan?

<details><summary>Jawaban</summary>
<p><b>1.</b> 6446.</p>
<p><b>2.</b> Tiga.</p>
</details>
