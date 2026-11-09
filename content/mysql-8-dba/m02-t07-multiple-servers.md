---
title: Menjalankan beberapa server di satu host
minutes: 20
level: Menengah
badge: lengkap
summary: Port, socket, datadir, dan PID terpisah, termasuk opsi mysqld_multi.
objectives:
  - Menyiapkan instance kedua tanpa bentrok
  - Mengelola beberapa instance dengan mysqld_multi
  - Menghindari konflik resource
---
## Kenapa topik ini diuji
Soal skenario: butuh dua instance untuk pengujian. Kandidat harus tahu parameter minimal yang wajib berbeda.

## Konsep inti
Empat hal yang **wajib** berbeda:

| Parameter | Contoh instance 2 |
|---|---|
| `port` | 3307 |
| `socket` | `/var/lib/mysql2/mysql.sock` |
| `datadir` | `/var/lib/mysql2` |
| `pid_file` | `/var/lib/mysql2/mysqld.pid` |

Disarankan juga berbeda: `log_error`, `server_id`, `relay_log`, `innodb_buffer_pool_size` (dibagi), `tmpdir`.

```ini
[mysqld1]
datadir = /var/lib/mysql
port = 3306
socket = /var/lib/mysql/mysql.sock
pid-file = /var/lib/mysql/mysqld.pid
server-id = 1

[mysqld2]
datadir = /var/lib/mysql2
port = 3307
socket = /var/lib/mysql2/mysql.sock
pid-file = /var/lib/mysql2/mysqld.pid
server-id = 2
```

```bash
mysqld_multi --defaults-file=/etc/my.cnf start 1,2
mysqld_multi report
mysqld_multi stop 2
```

Atau langsung:

```bash
mysqld --defaults-group-suffix=2 --datadir=/var/lib/mysql2 --port=3307 --socket=/var/lib/mysql2/mysql.sock
```

## Jebakan
- Dua instance dengan `server_id` sama → replikasi kacau.
- Tidak membagi RAM: dua buffer pool 4G di host 8G.
- Socket sama → klien lokal bingung harus ke instance mana.
- Lupa `--defaults-group-suffix` sehingga instance kedua membaca `[mysqld]` yang sama.

## Latihan
1. Empat parameter minimal yang harus berbeda antar instance?
2. Cara klien lokal memilih instance?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>port</code>, <code>socket</code>, <code>datadir</code>, <code>pid_file</code> (plus <code>server_id</code> untuk replikasi).</p>
<p><b>2.</b> Lewat <code>--socket</code> (atau <code>--host/--port</code> bila lewat TCP).</p>
</details>
