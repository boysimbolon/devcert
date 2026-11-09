---
title: Penggunaan, manajemen, dan konfigurasi konektor
minutes: 22
level: Menengah
badge: lengkap
summary: Connection pooling, parameter penting, dan pengelolaan siklus koneksi.
objectives:
  - Mengonfigurasi pooling dengan benar
  - Mengenali parameter yang sering menyebabkan masalah
  - Mengelola siklus hidup koneksi
---
## Kenapa topik ini diuji
Soal konfigurasi menanyakan parameter spesifik: timeout, pooling, dan TLS.

## Konsep inti
Parameter JDBC yang paling berpengaruh:

| Parameter | Fungsi |
|---|---|
| `sslMode` | `DISABLED`, `PREFERRED`, `REQUIRED`, `VERIFY_CA`, `VERIFY_IDENTITY` |
| `serverTimezone` | zona waktu untuk konversi TIMESTAMP |
| `useSSL` | lama; digantikan `sslMode` |
| `useServerPrepStmts` | prepared statement di server, bukan emulasi klien |
| `cachePrepStmts` | cache prepared statement |
| `rewriteBatchedStatements` | batch insert lebih cepat |
| `allowPublicKeyRetrieval` | untuk `caching_sha2_password` tanpa TLS |
| `connectTimeout`, `socketTimeout` | batas waktu |

```java
// HikariCP: pool di sisi aplikasi
HikariConfig cfg = new HikariConfig();
cfg.setJdbcUrl("jdbc:mysql://db.internal:3306/appdb?sslMode=VERIFY_IDENTITY");
cfg.setUsername("app");
cfg.setPassword(System.getenv("DB_PASS"));
cfg.setMaximumPoolSize(20);
cfg.setConnectionTimeout(5000);
```

Praktik yang benar:

- Pool **kecil** (10-30) untuk OLTP; `max_connections` server harus lebih besar dari total pool semua instance aplikasi.
- Set `maxLifetime` lebih pendek dari `wait_timeout` server agar koneksi tidak diputus di tengah.
- Selalu tutup `ResultSet`, `Statement`, `Connection` (try-with-resources).

## Jebakan
- Pool 100 koneksi × 4 instance = 400 > `max_connections` → error "too many connections".
- `maxLifetime` lebih panjang dari `wait_timeout` → koneksi mati saat dipakai.
- `allowPublicKeyRetrieval=true` tanpa TLS membuka risiko MITM.
- Membuka koneksi baru per request tanpa pool → overhead handshake dan autentikasi.

## Latihan
1. Mengapa pool besar bisa merugikan?
2. Parameter untuk menghindari koneksi terputus oleh server?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena total koneksi melampaui kapasitas server, memakan memori per koneksi, dan menambah kontensi.</p>
<p><b>2.</b> <code>maxLifetime</code> di pool yang lebih pendek dari <code>wait_timeout</code> server.</p>
</details>
