---
title: Mengonfigurasi InnoDB Cluster
minutes: 24
level: Lanjutan
badge: lengkap
summary: Dari instance kosong menjadi cluster tiga anggota dengan Router.
objectives:
  - Menyiapkan instance dengan persyaratan cluster
  - Membuat cluster dengan AdminAPI
  - Menambahkan anggota dan Router
---
## Kenapa topik ini diuji
Perintah `dba.*` spesifik dan mudah tertukar. Soal menanyakan urutan pembuatan.

## Konsep inti
Persyaratan tiap instance:

```ini
[mysqld]
server_id = 1
gtid_mode = ON
enforce_gtid_consistency = ON
binlog_format = ROW
log_replica_updates = ON
binlog_checksum = NONE
```

```bash
# 1. cek kesiapan instance
mysqlsh -- dba check-instance-configuration root@ic1:3306

# 2. buat cluster pada instance pertama
mysqlsh root@ic1:3306 -- dba create-cluster('prodCluster')

# 3. tambahkan anggota
mysqlsh root@ic1:3306 -- dba add-instance('prodCluster', 'root@ic2:3306')
mysqlsh root@ic1:3306 -- dba add-instance('prodCluster', 'root@ic3:3306')

# 4. status
mysqlsh root@ic1:3306 -- cluster status
```

Router:

```bash
mysqlrouter --bootstrap root@ic1:3306 --user=mysqlrouter
systemctl start mysqlrouter
```

Port Router: 6446 (baca-tulis), 6447 (baca-saja), 64460/64470 untuk mode klasik.

## Jebakan
- `binlog_checksum` harus `NONE` untuk Group Replication.
- Semua tabel wajib punya primary key.
- Instance harus kosong dari data konflik saat `add-instance` (atau pakai recovery).
- Router butuh bootstrap ulang bila metadata cluster berubah drastis.

## Latihan
1. Perintah membuat cluster?
2. Variabel apa yang wajib `NONE` untuk Group Replication?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>dba.createCluster('nama')</code> lewat MySQL Shell.</p>
<p><b>2.</b> <code>binlog_checksum</code>.</p>
</details>
