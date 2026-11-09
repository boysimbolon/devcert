---
title: MySQL Enterprise Audit
minutes: 20
level: Menengah
badge: lengkap
summary: Pencatatan aktivitas terstruktur, filter per akun, dan rotasi file.
objectives:
  - Mengaktifkan audit plugin dan memilih format
  - Membuat filter untuk akun tertentu
  - Mengatur rotasi dan pembacaan log
---
## Kenapa topik ini diuji
Audit diuji karena kepatuhan: apa yang dicatat, dan bagaimana membatasinya.

## Konsep inti
```sql
INSTALL PLUGIN audit_log SONAME 'audit_log.so';

SET GLOBAL audit_log_format = 'JSON';
SET GLOBAL audit_log_policy = 'ALL';        -- ALL | LOGINS | QUERIES | NONE
SET GLOBAL audit_log_file = '/var/log/mysql/audit.log';
SET GLOBAL audit_log_rotate_on_size = 104857600;   -- 100 MB
SET GLOBAL audit_log_rotations = 10;
```

Filter:

```sql
SELECT audit_log_filter_set_filter('log_app',
  '{ "filter": { "class": { "name": "general" } } }');
SELECT audit_log_filter_set_user('app@%', 'log_app');
```

Isi log mencakup: waktu, user@host, event (connect, query, table_access), status, dan query.

## Jebakan
- `ALL` tanpa filter bisa menghasilkan puluhan GB/hari.
- Audit log berisi data sensitif (nilai dalam query) → perlakukan sebagai rahasia.
- Rotasi dan retensi wajib disetel; tanpa itu disk penuh.
- Plugin Enterprise tidak ada di Community; `general_log` bukan pengganti audit terstruktur.

## Latihan
1. Variabel untuk rotasi berdasarkan ukuran?
2. Mengapa policy ALL berisiko?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>audit_log_rotate_on_size</code> (dan <code>audit_log_rotations</code>).</p>
<p><b>2.</b> Karena mencatat semua event tanpa filter sehingga volume log sangat besar dan memuat data sensitif.</p>
</details>
