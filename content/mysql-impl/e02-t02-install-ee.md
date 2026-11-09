---
title: Memasang MySQL Enterprise Server
minutes: 22
level: Menengah
badge: lengkap
summary: Repository Enterprise, paket, dan langkah verifikasi instalasi.
objectives:
  - Menjelaskan sumber paket Enterprise
  - Memasang server dan komponen pendukung
  - Memverifikasi instalasi dan fitur Enterprise
---
## Kenapa topik ini diuji
Soal instalasi Enterprise menekankan bahwa paket berasal dari repository Oracle (bukan distro), dan fitur diverifikasi setelah instalasi.

## Konsep inti
```bash
# Debian/Ubuntu (repository Oracle, perlu kredensial support)
wget https://dev.mysql.com/get/mysql-apt-config_0.8.33-1_all.deb
dpkg -i mysql-apt-config_0.8.33-1_all.deb
apt update
apt install mysql-server mysql-client mysql-shell

# RHEL/Oracle Linux
dnf install https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
dnf install mysql-community-server mysql-community-client
```

Verifikasi:

```bash
mysql --version
mysqladmin -u root -p ping
mysql -e "SELECT VERSION(), @@version_comment;"
```

Cek fitur Enterprise:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS FROM information_schema.PLUGINS
 WHERE PLUGIN_NAME LIKE '%audit%' OR PLUGIN_NAME LIKE '%firewall%';
SHOW VARIABLES LIKE 'thread_handling';
```

## Jebakan
- Menggunakan paket distro (`mysql-server` dari repo OS) yang biasanya Community, lalu bingung fitur Enterprise tidak ada.
- `@@version_comment` menunjukkan edisi — cara cepat memastikan EE vs Community.
- Paket Enterprise butuh kredensial support Oracle untuk mengunduh.
- Instalasi ulang tanpa membersihkan datadir bisa memakai data lama.

## Latihan
1. Cara cepat mengecek edisi server?
2. Dari mana paket Enterprise diambil?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>SELECT @@version_comment;</code> atau <code>mysql --version</code>.</p>
<p><b>2.</b> Repository resmi Oracle (dev.mysql.com), bukan repository distro.</p>
</details>
