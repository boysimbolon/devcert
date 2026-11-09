---
title: Meningkatkan versi MySQL
minutes: 22
level: Menengah
badge: lengkap
summary: Upgrade in-place, upgrade logis, alat pemeriksa, dan batasan downgrade.
objectives:
  - Memilih metode upgrade sesuai kondisi
  - Menjalankan pemeriksaan pra-upgrade
  - Mengetahui batasan downgrade
---
## Kenapa topik ini diuji
Upgrade adalah operasi berisiko yang diuji lewat urutan langkah: apa dulu, apa kemudian, dan apa yang harus di-backup.

## Konsep inti
Dua jalur:

1. **In-place**: ganti binary, jalankan upgrade internal.
2. **Logis**: dump dengan `mysqldump`/`mysqlpump`/`mysqlshell`, restore ke versi baru.

Urutan in-place yang aman:

```bash
# 1. backup penuh + binlog
mysqldump --single-transaction --routines --triggers --events --all-databases > all.sql

# 2. periksa kesiapan
mysqlsh -- util check-for-server-upgrade root@localhost --output-format=JSON

# 3. hentikan server, ganti paket, start
systemctl stop mysqld
apt install mysql-server-8.0     # atau versi target
systemctl start mysqld

# 4. jalankan upgrade internal (8.0.16+: tidak perlu mysql_upgrade)
mysqld --upgrade=FORCE --user=mysql
```

Sejak **8.0.16**, `mysql_upgrade` sudah dihapus; upgrade dilakukan otomatis saat start, dan bisa dipaksa dengan `--upgrade=FORCE` atau `--upgrade=MINIMAL`.

Yang perlu diperiksa sebelum upgrade:

- `innodb_fast_shutdown=0` agar shutdown bersih.
- Space disk untuk datadir sementara.
- Plugin yang tidak kompatibel.
- Akun dengan plugin autentikasi lama.

## Jebakan
- Melompati major version (5.7 → 8.0 harus langsung, tetapi 8.0 → 8.4 perlu pemeriksaan khusus).
- Downgrade tidak didukung secara umum; satu-satunya jalan aman adalah restore dari backup.
- Lupa menaikkan `innodb_fast_shutdown=0` sebelum upgrade → recovery lebih lama.
- Menjalankan `mysql_upgrade` di 8.0.16+ sehingga perintah tidak ditemukan.

## Latihan
1. Alat apa untuk memeriksa kompatibilitas sebelum upgrade?
2. Apakah downgrade 8.0 ke 5.7 didukung?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>mysqlsh -- util check-for-server-upgrade</code>.</p>
<p><b>2.</b> Tidak didukung secara in-place; harus restore dari backup logis/fisik yang dibuat sebelum upgrade.</p>
</details>
