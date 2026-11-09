---
title: Mengamankan lingkungan host MySQL
minutes: 20
level: Menengah
badge: lengkap
summary: Izin file datadir, akun OS, systemd hardening, dan pembatasan akses jaringan.
objectives:
  - Menetapkan kepemilikan dan izin yang benar
  - Menjalankan mysqld dengan akun non-root
  - Membatasi akses jaringan dan file
---
## Kenapa topik ini diuji
MySQL sekuat apa pun konfigurasinya bisa bobol lewat izin file longgar atau proses berjalan sebagai root.

## Konsep inti
```bash
ps -o user,cmd -C mysqld
id mysql

chown -R mysql:mysql /var/lib/mysql
chmod 750 /var/lib/mysql
chmod 600 /etc/mysql/my.cnf
```

Systemd hardening ringkas:

```ini
[Service]
User=mysql
Group=mysql
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
NoNewPrivileges=true
ReadWritePaths=/var/lib/mysql /var/log/mysql
```

```ini
[mysqld]
bind-address = 10.0.0.5
local_infile = OFF
secure_file_priv = /var/lib/mysql-files
skip_symbolic_links = ON
```

## Jebakan
- `datadir` dimiliki root setelah restore sehingga mysqld gagal start.
- `secure_file_priv` kosong berarti impor/ekspor ke path mana pun.
- `local_infile=ON` + aplikasi rentan = jalur pemuatan file berbahaya.
- Symlink di datadir bisa diarahkan ke file sistem.

## Latihan
1. Mengapa mysqld tidak boleh berjalan sebagai root?
2. Variabel untuk membatasi lokasi impor/ekspor file?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena kompromi pada server langsung berarti akses root ke host.</p>
<p><b>2.</b> <code>secure_file_priv</code> (arahkan ke direktori khusus).</p>
</details>
