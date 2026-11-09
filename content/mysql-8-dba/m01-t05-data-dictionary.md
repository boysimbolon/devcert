---
title: Data dictionary dan INFORMATION_SCHEMA
minutes: 20
level: Menengah
badge: lengkap
summary: Dictionary transaksional MySQL 8.0, DDL atomik, dan cara membacanya.
objectives:
  - Menjelaskan perbedaan data dictionary dan INFORMATION_SCHEMA
  - Memahami DDL atomik dan hilangnya file .frm
  - Menggunakan SDI untuk inspeksi metadata
---
## Kenapa topik ini diuji
Data dictionary adalah perubahan besar di 8.0. Soal menanyakan di mana metadata disimpan dan apa keuntungannya.

## Konsep inti
- Metadata disimpan dalam **tabel InnoDB** di schema `mysql`, dalam tablespace `mysql.ibd` — disebut **transactional data dictionary**.
- Tidak ada lagi `.frm`; definisi tabel tidak lagi file per tabel.
- DDL menjadi **atomik**: `CREATE/ALTER/DROP` tidak meninggalkan state setengah jadi.
- `INFORMATION_SCHEMA` sekarang sebagian besar berupa **view** di atas data dictionary (bukan tabel temporer seperti versi lama), sehingga lebih cepat.
- **SDI** (Serialized Dictionary Information) menyimpan metadata dalam bentuk JSON di dalam file `.ibd` → berguna untuk *dump/load* metadata dan inspeksi file.

```sql
-- daftar objek
SELECT TABLE_SCHEMA, TABLE_NAME, ENGINE FROM information_schema.TABLES
 WHERE TABLE_SCHEMA = 'appdb';

-- metadata tabel lengkap
SHOW CREATE TABLE appdb.pesanan\G

-- dictionary internal (hati-hati: jangan dimodifikasi manual)
SELECT * FROM mysql.tables LIMIT 1;

-- SDI dari file ibd
-- shell: ibd2sdi /var/lib/mysql/appdb/pesanan.ibd
```

Perintah SDI:

```bash
ibd2sdi /var/lib/mysql/appdb/pesanan.ibd | head -40
```

## Jebakan
- Mengedit tabel `mysql.*` secara manual — dilarang dan bisa merusak instance.
- Menganggap INFORMATION_SCHEMA masih tabel temporer; di 8.0 banyak yang view atas dictionary, jadi perilakunya berubah.
- Lupa bahwa DDL atomik tidak otomatis membuat `ALTER TABLE` besar menjadi instan; itu urusan algoritma (`INSTANT`, `INPLACE`, `COPY`).
- Backup file `.ibd` tanpa metadata akan sulit dipulihkan; gunakan `ibd2sdi` atau backup logis.

## Latihan
1. Di mana definisi tabel disimpan di MySQL 8.0?
2. Apa keuntungan DDL atomik bagi DBA?

<details><summary>Jawaban</summary>
<p><b>1.</b> Di data dictionary transaksional pada tablespace <code>mysql.ibd</code>, dengan salinan SDI di dalam file <code>.ibd</code> tabel.</p>
<p><b>2.</b> Operasi DDL tidak meninggalkan objek setengah jadi saat crash; tidak perlu lagi membersihkan sisa <code>.frm</code> atau tabel yatim.</p>
</details>
