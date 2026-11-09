---
title: Mengamankan koneksi dengan TLS
minutes: 22
level: Menengah
badge: lengkap
summary: Sertifikat otomatis, require_secure_transport, dan persyaratan TLS per akun.
objectives:
  - Mengaktifkan TLS dan memverifikasi status
  - Mewajibkan TLS secara global dan per akun
  - Membaca status cipher koneksi
---
## Kenapa topik ini diuji
MySQL 8.0 sudah membuat sertifikat sendiri; soal menguji apakah kamu tahu cara memaksakan penggunaannya.

## Konsep inti
MySQL 8.0 membuat sertifikat otomatis di datadir (`ca.pem`, `server-cert.pem`, `server-key.pem`) saat inisialisasi.

```ini
[mysqld]
ssl_ca = /var/lib/mysql/ca.pem
ssl_cert = /var/lib/mysql/server-cert.pem
ssl_key = /var/lib/mysql/server-key.pem
tls_version = TLSv1.2,TLSv1.3
require_secure_transport = ON
```

```sql
SHOW VARIABLES LIKE '%ssl%';
SHOW STATUS LIKE 'Ssl_cipher';

ALTER USER 'app'@'%' REQUIRE SSL;
ALTER USER 'app'@'%' REQUIRE X509;
ALTER USER 'app'@'%' REQUIRE CIPHER 'ECDHE-RSA-AES256-GCM-SHA384';
```

Klien memaksa TLS:

```bash
mysql --ssl-mode=REQUIRED -u app -p -h db.internal
mysql --ssl-mode=VERIFY_IDENTITY -u app -p -h db.internal
```

## Jebakan
- `require_secure_transport=ON` membuat akun tanpa TLS tidak bisa konek, termasuk replikasi.
- `REQUIRE X509` menuntut sertifikat klien, bukan hanya TLS.
- Sertifikat otomatis tidak dipercaya CA publik; klien perlu `--ssl-ca`.
- Replikasi juga butuh TLS terkonfigurasi (`SOURCE_SSL_*`).

## Latihan
1. Bagaimana memastikan sebuah akun hanya bisa konek lewat TLS?
2. Apa efek `require_secure_transport=ON` pada replikasi?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ALTER USER ... REQUIRE SSL;</code> (atau <code>REQUIRE X509</code> untuk sertifikat klien).</p>
<p><b>2.</b> Koneksi replikasi harus dikonfigurasi dengan TLS, kalau tidak akan gagal.</p>
</details>
