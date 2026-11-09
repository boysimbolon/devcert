---
title: MySQL Enterprise Firewall
minutes: 18
level: Menengah
badge: lengkap
summary: Allowlist per akun, mode RECORDING/PROTECTING, dan pengelolaan aturan.
objectives:
  - Menjelaskan cara kerja firewall
  - Menjalankan perekaman lalu penegakan
  - Menangani query dinamis
---
## Kenapa topik ini diuji
Soal konsep dan perintah dasar: urutan mode dan cara melihat aturan.

## Konsep inti
```sql
INSTALL PLUGIN mysql_firewall SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_users SONAME 'mysql_firewall.so';

CALL mysql.sp_set_firewall_mode('app@%', 'RECORDING');
-- jalankan beban normal beberapa waktu
CALL mysql.sp_set_firewall_mode('app@%', 'PROTECTING');

CALL mysql.sp_get_firewall_mode('app@%');
SELECT * FROM mysql.firewall_whitelist;
SELECT * FROM mysql.firewall_group_allowlist;
```

Mode: `OFF`, `RECORDING`, `PROTECTING`, `DETECTING`.

## Jebakan
- Langsung `PROTECTING` tanpa merekam → query sah diblokir.
- Aplikasi dengan SQL dinamis sulit dibuat allowlist.
- Firewall bukan pengganti perbaikan injeksi di aplikasi.
- Butuh plugin Enterprise; di Community tidak bisa dipasang.

## Latihan
1. Urutan mode yang benar?
2. Mode untuk menguji tanpa memblokir?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>RECORDING</code> lalu <code>PROTECTING</code>.</p>
<p><b>2.</b> <code>DETECTING</code>.</p>
</details>
