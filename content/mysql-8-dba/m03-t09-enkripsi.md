---
title: Enkripsi data MySQL
minutes: 22
level: Menengah
badge: lengkap
summary: Enkripsi tablespace InnoDB, keyring, dan enkripsi backup.
objectives:
  - Menjelaskan perbedaan enkripsi at-rest dan in-transit
  - Mengaktifkan enkripsi tablespace dengan keyring
  - Mengelola kunci tanpa kehilangan data
---
## Kenapa topik ini diuji
Enkripsi at-rest butuh keyring; tanpa itu tidak ada enkripsi. Soal menguji ketergantungan ini.

## Konsep inti
| Lapisan | Mekanisme |
|---|---|
| Transit | TLS antar klien-server |
| At-rest | Tablespace encryption InnoDB (AES-256) |
| Backup | Enkripsi backup (Enterprise Backup, atau dump + GPG) |

```ini
[mysqld]
early-plugin-load = keyring_file.so
keyring_file_data = /var/lib/mysql-keyring/keyring
default_table_encryption = ON
```

```sql
CREATE TABLE pesanan (
  id BIGINT PRIMARY KEY,
  total DECIMAL(12,2)
) ENCRYPTION='Y';

ALTER TABLE pesanan ENCRYPTION='Y';
SELECT TABLE_NAME, CREATE_OPTIONS FROM information_schema.TABLES
 WHERE TABLE_SCHEMA='appdb';
```

```sql
SHOW VARIABLES LIKE 'default_table_encryption';
SELECT * FROM performance_schema.keyring_component_status;
```

## Jebakan
- Kehilangan keyring = kehilangan data terenkripsi; keyring harus dibackup terpisah.
- `ENCRYPTION='Y'` tanpa keyring aktif akan gagal.
- Enkripsi at-rest tidak melindungi dari user DB yang sah.
- `keyring_file` tidak disarankan untuk produksi.

## Latihan
1. Apa yang terjadi bila keyring hilang?
2. Apakah enkripsi tablespace melindungi dari SELECT oleh user berwenang?

<details><summary>Jawaban</summary>
<p><b>1.</b> Data terenkripsi tidak bisa dibuka; halaman terenkripsi tidak dapat dipulihkan.</p>
<p><b>2.</b> Tidak. Enkripsi at-rest melindungi file di disk/backup, bukan akses lewat akun berizin.</p>
</details>
