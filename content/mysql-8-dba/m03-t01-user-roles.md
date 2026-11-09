---
title: Membuat akun pengguna dan role
minutes: 20
level: Dasar
badge: lengkap
summary: Pola akun user@host, pembuatan role, dan pemberian role ke pengguna.
objectives:
  - Menulis CREATE USER dengan host yang tepat
  - Membuat role dan memberikannya ke beberapa pengguna
  - Menghapus akun dengan benar
---
## Kenapa topik ini diuji
Security adalah domain terbesar di ujian ini. Dasar yang paling sering ditanyakan: format `user@host` dan penggunaan role.

## Konsep inti
Akun selalu berpasangan **nama + host**:

```sql
CREATE USER 'app'@'10.0.0.%' IDENTIFIED BY 'Rahasia#2026';
CREATE USER 'report'@'localhost' IDENTIFIED BY 'Rahasia#2026';

-- role: objek tanpa password, bisa diberi privilege
CREATE ROLE 'app_read', 'app_write';
GRANT SELECT ON appdb.* TO 'app_read';
GRANT INSERT, UPDATE, DELETE ON appdb.* TO 'app_write';

GRANT 'app_read' TO 'app'@'10.0.0.%';
GRANT 'app_write' TO 'app'@'10.0.0.%';
SET DEFAULT ROLE 'app_read', 'app_write' TO 'app'@'10.0.0.%';
```

Penting: `'app'@'localhost'` dan `'app'@'%'` adalah **dua akun berbeda**. MySQL memilih baris paling spesifik di `mysql.user`.

```sql
SELECT user, host FROM mysql.user ORDER BY user, host;
SHOW GRANTS FOR 'app'@'10.0.0.%';
SHOW GRANTS FOR 'app'@'10.0.0.%' USING 'app_write';
```

## Jebakan
- Membuat `'app'@'%'` lalu mengira itu mencakup `localhost` — di banyak setup `localhost` memakai socket dan punya akun sendiri.
- Memberi role tetapi lupa `SET DEFAULT ROLE`, lalu aplikasi tidak punya izin saat connect.
- Menghapus pengguna tetapi role-nya tetap aktif di sesi berjalan.
- `DROP USER` tidak menghapus privilege yang diberikan lewat role lain.

## Latihan
1. Apakah `'app'@'%'` sama dengan `'app'@'localhost'`?
2. Perintah agar role otomatis aktif saat login?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak — itu dua akun berbeda; MySQL mencocokkan berdasarkan host yang paling spesifik.</p>
<p><b>2.</b> <code>SET DEFAULT ROLE 'nama_role' TO 'user'@'host';</code></p>
</details>
