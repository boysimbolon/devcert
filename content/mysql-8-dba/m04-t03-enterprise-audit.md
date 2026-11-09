---
title: MySQL Enterprise Audit
minutes: 18
level: Menengah
badge: lengkap
summary: Merekam aktivitas akun, filter audit, dan pengelolaan file audit.
objectives:
  - Menjelaskan apa yang dicatat audit plugin
  - Membuat filter untuk akun tertentu
  - Mengelola rotasi dan pembacaan log audit
---
## Kenapa topik ini diuji
Audit adalah kebutuhan kepatuhan. Soal menguji perbedaan audit dan general log, serta cara membatasi apa yang dicatat.

## Konsep inti
Audit plugin mencatat **event** (login, query, perubahan privilege) ke file XML/JSON, dengan filter agar tidak membanjiri disk.

```sql
INSTALL PLUGIN audit_log SONAME 'audit_log.so';

SHOW VARIABLES LIKE 'audit_log%';
SET GLOBAL audit_log_policy = 'ALL';         -- ALL | LOGINS | QUERIES | NONE
SET GLOBAL audit_log_format = 'JSON';
SET GLOBAL audit_log_file = '/var/log/mysql/audit.log';
```

Filter per akun:

```sql
SELECT audit_log_filter_set_filter('log_app', '{ "filter": { "class": { "name": "general" } } }');
SELECT audit_log_filter_set_user('app@%', 'log_app');
SELECT audit_log_filter_remove_user('app@%');
```

Membaca hasil:

```bash
mysqlbinlog --help >/dev/null
# audit log berupa JSON per baris:
tail -5 /var/log/mysql/audit.log
```

## Jebakan
- `audit_log_policy=ALL` tanpa filter bisa menghasilkan puluhan GB per hari.
- Audit Enterprise berbeda dari `general_log`: audit tertata, bisa difilter, dan termasuk event login/DDL.
- Filter harus diset **sebelum** akun aktif untuk cakupan penuh.
- Rotasi wajib diatur; file audit yang tumbuh tak terkendali bisa memenuhi disk.

## Latihan
1. Apa perbedaan audit log dan general log?
2. Mengapa filter audit penting?

<details><summary>Jawaban</summary>
<p><b>1.</b> Audit log terstruktur dan dapat difilter per akun/event, termasuk login dan perubahan privilege; general log mencatat semua pernyataan tanpa filter.</p>
<p><b>2.</b> Karena tanpa filter volume log bisa memenuhi disk dan menyulitkan analisis.</p>
</details>
