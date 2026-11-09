---
title: MySQL Enterprise Firewall
minutes: 18
level: Menengah
badge: lengkap
summary: Mode perekaman dan penegakan, allowlist per akun, dan alur kerjanya.
objectives:
  - Menjelaskan cara kerja firewall berbasis allowlist
  - Merekam pola lalu menegakkannya
  - Menangani aplikasi dengan query dinamis
---
## Kenapa topik ini diuji
Fitur ini hanya ada di edisi Enterprise, dan diuji pada level konsep + perintah dasar.

## Konsep inti
Prinsip: pelajari query sah (**RECORDING**), lalu tolak yang tidak cocok (**PROTECTING**).

```sql
INSTALL PLUGIN mysql_firewall SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_users SONAME 'mysql_firewall.so';

CALL mysql.sp_set_firewall_mode('app@10.0.0.%', 'RECORDING');
CALL mysql.sp_set_firewall_mode('app@10.0.0.%', 'PROTECTING');

CALL mysql.sp_get_firewall_mode('app@10.0.0.%');
SELECT * FROM mysql.firewall_whitelist;
```

Mode: `OFF`, `RECORDING`, `PROTECTING`, `DETECTING` (mencatat pelanggaran tanpa memblokir).

## Jebakan
- Langsung `PROTECTING` tanpa masa perekaman → query sah ikut diblokir.
- Aplikasi dengan query dinamis sulit dibuat allowlist; gunakan `DETECTING` dulu.
- Firewall tidak menggantikan perbaikan injeksi.
- Butuh plugin Enterprise; di Community tidak tersedia.

## Latihan
1. Urutan mode yang benar saat menerapkan firewall?
2. Apa fungsi mode DETECTING?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>RECORDING</code> untuk mengumpulkan pola sah, lalu <code>PROTECTING</code> untuk menegakkan.</p>
<p><b>2.</b> Mencatat query yang tidak cocok tanpa memblokir — berguna untuk menguji kebijakan.</p>
</details>
