---
title: Mengonfigurasi user dan role
minutes: 20
level: Menengah
badge: lengkap
summary: Membuat akun, mengatur host, membuat role, dan mencabut akses.
objectives:
  - Membuat akun dengan pembatasan host yang tepat
  - Membuat role dan mengaktifkannya
  - Mencabut akses tanpa menghapus akun
---
## Kenapa topik ini diuji
Soal praktis: perintah yang benar dan urutan yang aman.

## Konsep inti
```sql
CREATE USER 'report'@'10.0.0.%' IDENTIFIED BY 'Rahasia#2026' REQUIRE SSL;
CREATE ROLE 'baca_laporan';
GRANT SELECT ON appdb.laporan TO 'baca_laporan';
GRANT 'baca_laporan' TO 'report'@'10.0.0.%';
SET DEFAULT ROLE ALL TO 'report'@'10.0.0.%';

ALTER USER 'report'@'10.0.0.%' ACCOUNT LOCK;
ALTER USER 'report'@'10.0.0.%' ACCOUNT UNLOCK;
REVOKE INSERT ON appdb.* FROM 'report'@'10.0.0.%';
DROP USER 'report'@'10.0.0.%';
```

Praktik: satu akun per aplikasi, host dibatasi ke subnet aplikasi, role per fungsi, dan tidak ada akun bersama.

## Jebakan
- `'app'@'%'` membuka akses dari mana saja; batasi ke subnet.
- `DROP USER` langsung menghapus; untuk sementara gunakan `ACCOUNT LOCK`.
- Role tidak aktif otomatis tanpa `SET DEFAULT ROLE`.
- Akun dengan `REQUIRE SSL` gagal login bila klien tidak memakai TLS.

## Latihan
1. Perintah mengunci akun tanpa menghapus?
2. Mengapa host sebaiknya dibatasi subnet?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ALTER USER ... ACCOUNT LOCK;</code></p>
<p><b>2.</b> Mengurangi permukaan serangan; kredensial bocor tidak bisa dipakai dari jaringan lain.</p>
</details>
