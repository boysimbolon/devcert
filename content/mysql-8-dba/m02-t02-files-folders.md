---
title: File dan folder hasil instalasi
minutes: 18
level: Dasar
badge: lengkap
summary: Datadir, konfigurasi, log, socket, dan direktori plugin beserta fungsinya.
objectives:
  - Menyebutkan lokasi file konfigurasi yang dibaca berurutan
  - Membedakan file data, log, dan runtime
  - Menemukan file yang relevan saat troubleshooting
---
## Kenapa topik ini diuji
Soal "di mana file X" muncul berulang. Menghafal peta ini menghemat waktu di ujian dan di produksi.

## Konsep inti
| Kategori | Lokasi umum |
|---|---|
| Data | `/var/lib/mysql` (`@@datadir`) |
| Konfigurasi | `/etc/my.cnf`, `/etc/mysql/my.cnf`, `/etc/mysql/mysql.conf.d/*.cnf`, `~/.my.cnf` |
| Binary | `/usr/sbin/mysqld`, `/usr/bin/mysql*` |
| Plugin | `@@plugin_dir` |
| Error log | `/var/log/mysql/error.log` |
| Slow/general log | `/var/log/mysql/slow.log`, `general.log` |
| Socket | `@@socket` (mis. `/var/lib/mysql/mysql.sock`) |
| PID | `@@pid_file` |
| TLS | `mysql-data-dir/*.pem` (auto-generated 8.0) |
| Secure file import | `@@secure_file_priv` |

Urutan pembacaan konfigurasi (yang terakhir menang):

```text
/etc/my.cnf
/etc/mysql/my.cnf
~/.my.cnf              (untuk klien)
--defaults-file=...    (menggantikan semua di atas)
```

Verifikasi lokasi nyata dari server yang berjalan:

```sql
SELECT @@datadir, @@basedir, @@plugin_dir, @@log_error, @@socket, @@pid_file;
SHOW VARIABLES LIKE 'secure_file_priv';
```

## Jebakan
- `--defaults-file` **mengganti** urutan default, bukan menambah.
- `--defaults-extra-file` dibaca paling awal, setelah itu file default tetap dipakai.
- `secure_file_priv` kosong berarti tanpa batas (berbahaya); NULL berarti tidak diizinkan.
- Log di beberapa distro bernama `mysqld.log` (RHEL) bukan `error.log`.

## Latihan
1. Opsi mana yang membuat `mysqld` mengabaikan semua file konfigurasi default?
2. Di mana file TLS yang dibuat otomatis MySQL 8.0?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>--defaults-file=/path/ke/file.cnf</code> (menggantikan seluruh urutan default).</p>
<p><b>2.</b> Di datadir, misalnya <code>ca.pem</code>, <code>server-cert.pem</code>, <code>server-key.pem</code>, dibuat saat inisialisasi.</p>
</details>
