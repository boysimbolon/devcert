---
title: Plugin autentikasi
minutes: 20
level: Menengah
badge: lengkap
summary: caching_sha2_password, mysql_native_password, dan autentikasi berbasis sertifikat.
objectives:
  - Menjelaskan plugin default MySQL 8.0 dan implikasinya
  - Mengubah plugin autentikasi akun
  - Memilih plugin untuk kasus khusus
---
## Kenapa topik ini diuji
Perubahan default ke `caching_sha2_password` memecahkan banyak konektor lama. Soal sering menanyakan cara mengatasinya.

## Konsep inti
Plugin yang tersedia:

| Plugin | Catatan |
|---|---|
| `caching_sha2_password` | **default 8.0**, SHA-256 + cache, butuh TLS atau RSA untuk handshake awal |
| `mysql_native_password` | lama (SHA-1), kompatibilitas konektor usang, sudah deprecated |
| `sha256_password` | SHA-256 tanpa cache, butuh TLS/RSA |
| `auth_socket` | autentikasi lewat OS (cocok untuk akun admin lokal) |
| `authentication_ldap_*` / `authentication_pam` | Enterprise |
| `authentication_fido` | FIDO2 (8.0.30+) |
| `mysql_no_login` | akun tidak bisa login (untuk prosedur `SQL SECURITY DEFINER`) |

```sql
CREATE USER 'legacy'@'%' IDENTIFIED WITH mysql_native_password BY 'Rahasia#2026';
ALTER USER 'legacy'@'%' IDENTIFIED WITH caching_sha2_password BY 'Rahasia#2026';

SELECT user, host, plugin FROM mysql.user;
SHOW VARIABLES LIKE 'default_authentication_plugin';
```

Untuk klien lama tanpa TLS:

```ini
[mysqld]
default_authentication_plugin = mysql_native_password
```

## Jebakan
- Menurunkan default plugin ke `mysql_native_password` sebagai "solusi" — melemahkan keamanan, sebaiknya hanya per akun.
- Konektor lama gagal karena butuh jalur RSA `--get-server-public-key`.
- `auth_socket` membuat akun tidak bisa login lewat TCP.
- Plugin Enterprise butuh plugin terpasang; kalau tidak, `CREATE USER` gagal.

## Latihan
1. Mengapa klien lama gagal konek ke MySQL 8.0?
2. Plugin apa untuk akun admin yang hanya login dari OS?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena default <code>caching_sha2_password</code> membutuhkan TLS atau pertukaran kunci RSA yang tidak didukung klien lama.</p>
<p><b>2.</b> <code>auth_socket</code>.</p>
</details>
