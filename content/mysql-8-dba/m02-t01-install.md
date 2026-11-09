---
title: Memasang server dan klien MySQL
minutes: 22
level: Dasar
badge: lengkap
summary: Instalasi dari repository resmi, paket yang dipilih, dan inisialisasi datadir.
objectives:
  - Memilih paket server dan klien yang tepat
  - Menjalankan inisialisasi datadir dengan aman
  - Memverifikasi instalasi berhasil
---
## Kenapa topik ini diuji
Soal instalasi menguji hal praktis: paket mana, perintah apa, dan bagaimana mengamankan instalasi baru.

## Konsep inti
Repository resmi (Debian/Ubuntu):

```bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.33-1_all.deb
dpkg -i mysql-apt-config_0.8.33-1_all.deb      # pilih mysql-8.0
apt update
apt install mysql-server mysql-client
```

RHEL/Oracle Linux:

```bash
dnf install https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
dnf install mysql-community-server mysql-community-client
```

Paket dan perannya:

| Program | Fungsi |
|---|---|
| `mysqld` | server |
| `mysql` | klien interaktif |
| `mysqladmin` | administrasi (status, shutdown, password) |
| `mysqldump`, `mysqlpump` | backup logis |
| `mysqlsh` | shell modern (AdminAPI, upgrade checker, util) |
| `mysqlbinlog` | membaca binlog |

Inisialisasi manual (bila tidak memakai paket):

```bash
mysqld --initialize --user=mysql --datadir=/var/lib/mysql
# --initialize menghasilkan temporary password di error log
# --initialize-insecure membuat root tanpa password (hanya untuk lab)
```

Verifikasi:

```bash
mysqladmin -u root -p ping
mysql -u root -p -e "SELECT VERSION(), @@datadir, @@socket;"
```

## Jebakan
- Menjalankan `--initialize-insecure` di server produksi.
- Lupa mencatat temporary password dari error log saat `--initialize`.
- Mencampur paket distro (`mariadb-server`) dengan paket Oracle MySQL — konflik.
- Menginstal hanya klien lalu bingung `mysqld` tidak ada.

## Latihan
1. Apa bedanya `--initialize` dan `--initialize-insecure`?
2. Perintah cepat memastikan server hidup tanpa membuka sesi interaktif?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>--initialize</code> membuat akun root dengan password sementara di log; <code>--initialize-insecure</code> membuat root tanpa password.</p>
<p><b>2.</b> <code>mysqladmin ping</code> (atau <code>mysqladmin status</code>).</p>
</details>
