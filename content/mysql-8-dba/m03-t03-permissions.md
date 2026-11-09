---
title: Mengendalikan izin pengguna dan role
minutes: 22
level: Menengah
badge: lengkap
summary: Tingkat privilege: global, database, tabel, kolom, rutin, dan dynamic privileges.
objectives:
  - Membedakan tingkat privilege dan cakupannya
  - Memakai dynamic privileges MySQL 8.0
  - Mencabut izin tanpa mengganggu akun lain
---
## Kenapa topik ini diuji
Soal privilege menguji presisi: level mana yang dipakai, dan apa efek pencabutannya.

## Konsep inti
Tingkatan:

| Level | Contoh |
|---|---|
| Global | `ON *.*` — `SELECT`, `PROCESS`, `RELOAD` |
| Database | `ON appdb.*` |
| Tabel | `ON appdb.pesanan` |
| Kolom | `(kolom1, kolom2)` |
| Rutin | `ON PROCEDURE appdb.hitung` |
| Dynamic | `BACKUP_ADMIN`, `SYSTEM_VARIABLES_ADMIN`, `AUDIT_ADMIN` |

```sql
GRANT SELECT, INSERT ON appdb.* TO 'app'@'10.0.0.%';
GRANT SELECT (id, nama) ON appdb.pesanan TO 'report'@'localhost';

GRANT BACKUP_ADMIN ON *.* TO 'dba'@'localhost';
GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO 'dba'@'localhost';

REVOKE INSERT ON appdb.* FROM 'app'@'10.0.0.%';
SHOW GRANTS FOR 'dba'@'localhost';
```

Prinsip yang dipakai ujian: **least privilege** — beri yang perlu saja, pada level paling sempit, lewat role agar mudah dicabut.

## Jebakan
- `GRANT ALL ON *.*` dipakai untuk kenyamanan lalu lupa dicabut.
- Mencabut privilege database tidak mencabut privilege tabel yang diberikan terpisah.
- `PROCESS`/`SUPER` membuka banyak data; di 8.0 `SUPER` dipecah menjadi dynamic privileges.
- Privilege kolom tidak bisa digabung dengan `SELECT *` di aplikasi.

## Latihan
1. Apa level privilege paling sempit untuk hanya membaca dua kolom?
2. Mengapa dynamic privileges lebih baik daripada `SUPER`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Level kolom: <code>GRANT SELECT (id, nama) ON db.tabel TO ...</code></p>
<p><b>2.</b> Karena memberi kemampuan spesifik (mis. <code>BACKUP_ADMIN</code>) tanpa memberi seluruh kekuasaan superuser.</p>
</details>
