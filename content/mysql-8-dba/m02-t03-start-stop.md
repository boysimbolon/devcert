---
title: Menjalankan dan menghentikan MySQL
minutes: 18
level: Dasar
badge: lengkap
summary: systemd, mysqld_safe, mysqladmin shutdown, dan perilaku sinyal.
objectives:
  - Menghentikan server dengan cara yang bersih
  - Memilih antara systemd dan mysqld_safe
  - Mengenali sinyal dan efeknya
---
## Kenapa topik ini diuji
Soal operasional: bagaimana menghentikan tanpa merusak data, dan apa yang terjadi saat server dimatikan paksa.

## Konsep inti
```bash
# systemd (distro modern)
systemctl start mysqld
systemctl stop mysqld
systemctl status mysqld
systemctl restart mysqld

# manual
mysqld --daemonize --user=mysql --defaults-file=/etc/my.cnf
mysqld_safe --defaults-file=/etc/my.cnf &      # wrapper, restart otomatis

# menghentikan dengan bersih
mysqladmin -u root -p shutdown
```

Perilaku sinyal:

| Sinyal | Efek |
|---|---|
| `SIGTERM` | shutdown bersih (flush, tutup koneksi) |
| `SIGINT` | shutdown bersih |
| `SIGKILL` | mati paksa; recovery redo saat start |

Saat shutdown, InnoDB melakukan **checkpoint** dan menutup tablespace; setelah itu redo bisa dipangkas. Setelah `SIGKILL`, start berikutnya menjalankan crash recovery dari redo.

```sql
SHUTDOWN;                    -- dari sesi SQL (butuh privilege)
SHOW VARIABLES LIKE 'innodb_fast_shutdown';   -- 0=flush penuh, 1=default, 2=cepat
```

## Jebakan
- Menghentikan dengan `kill -9` lalu menganggap datanya rusak; recovery otomatis, tapi lebih lambat dan berisiko.
- `innodb_fast_shutdown=2` mempercepat shutdown tetapi perlu recovery panjang saat start.
- Lupa mematikan `mysqld_safe` sehingga server naik lagi setelah dihentikan.
- Menjalankan `systemctl stop` pada unit yang salah (mis. `mysql` vs `mysqld`).

## Latihan
1. Cara menghentikan server tanpa memutus data yang belum di-flush?
2. Apa efek membunuh proses dengan `SIGKILL`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>mysqladmin shutdown</code> atau <code>systemctl stop mysqld</code> — keduanya mengirim sinyal shutdown bersih.</p>
<p><b>2.</b> Server mati tanpa checkpoint; saat start berikutnya InnoDB menjalankan crash recovery dari redo log.</p>
</details>
