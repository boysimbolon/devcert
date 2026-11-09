---
title: Opsi dan option file
minutes: 20
level: Menengah
badge: lengkap
summary: Kelompok konfigurasi, urutan pembacaan, include, dan cara memvalidasi nilai efektif.
objectives:
  - Menulis option file dengan kelompok yang benar
  - Memahami urutan dan prioritas konfigurasi
  - Memeriksa nilai efektif dari server berjalan
---
## Kenapa topik ini diuji
Banyak kandidat menulis konfigurasi di tempat yang salah, lalu bingung mengapa tidak berlaku. Soal menguji urutan prioritas.

## Konsep inti
```ini
[client]
port = 3306

[mysqld]
datadir = /var/lib/mysql
innodb_buffer_pool_size = 4G
max_connections = 300
slow_query_log = ON
long_query_time = 1

[mysqldump]
quick
single-transaction

!include /etc/mysql/conf.d/local.cnf
!includedir /etc/mysql/conf.d/
```

Urutan prioritas (dari lemah ke kuat):

```text
/etc/my.cnf -> /etc/mysql/my.cnf -> file include -> baris perintah (--opsi=nilai)
```

Memeriksa nilai efektif:

```bash
mysqld --verbose --help | grep -E "datadir|buffer_pool_size"
mysql -e "SHOW VARIABLES LIKE 'innodb_buffer_pool_size';"
mysql -e "SELECT @@global.max_connections, @@session.max_connections;"
```

Perubahan runtime:

```sql
SET GLOBAL max_connections = 400;         -- sementara, hilang saat restart
SET PERSIST max_connections = 400;        -- ditulis ke mysqld-auto.cnf
SET PERSIST_ONLY long_query_time = 2;     -- hanya simpan, tanpa apply
RESET PERSIST max_connections;            -- hapus override
```

## Jebakan
- Menaruh opsi `[mysqld]` di kelompok `[client]` — tidak berpengaruh ke server.
- `SET GLOBAL` tidak bertahan setelah restart; gunakan `SET PERSIST`.
- Opsi yang tidak dinamis tetap butuh restart (`innodb_buffer_pool_instances`).
- Kesalahan sintaks di option file membuat server gagal start; periksa dengan `--verbose --help`.

## Latihan
1. Apa perbedaan `SET PERSIST` dan `SET PERSIST_ONLY`?
2. Di mana `SET PERSIST` menyimpan nilainya?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>PERSIST</code> menyimpan dan langsung menerapkan bila variabel dinamis; <code>PERSIST_ONLY</code> hanya menyimpan, berlaku setelah restart (untuk variabel non-dinamis).</p>
<p><b>2.</b> Di <code>mysqld-auto.cnf</code> dalam datadir.</p>
</details>
