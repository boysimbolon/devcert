---
title: Bagaimana MySQL menyimpan data
minutes: 22
level: Dasar
badge: lengkap
summary: Peta datadir: tablespace, file per tabel, undo, redo, temp, dan binlog.
objectives:
  - Menjelaskan struktur datadir dan tablespace
  - Membedakan tablespace sistem, file-per-table, dan general
  - Menemukan file untuk database dan tabel tertentu
---
## Kenapa topik ini diuji
Soal tipe "file apa yang muncul setelah tabel dibuat" hanya bisa dijawab kalau kamu tahu peta datadir.

## Konsep inti
Semua data berada di **datadir** (biasanya `/var/lib/mysql`):

| Isi | Lokasi |
|---|---|
| Data dictionary | `mysql.ibd` |
| Tablespace sistem | `ibdata1` |
| Tabel InnoDB per tabel | `db/tabel.ibd` (bila `innodb_file_per_table=ON`) |
| Undo tablespace | `undo_001`, `undo_002` |
| Redo log | `#innodb_redo/` (8.0.30+) atau `ib_logfile0/1` |
| Binary log | `binlog.000001` + `binlog.index` |
| Relay log (replica) | `relay-bin.000001` |
| Temporary | `ibtmp1`, `#innodb_temp/` |
| Konfigurasi/socket/pid | `/etc/mysql/`, `mysql.sock`, `mysqld.pid` |

Setiap database = **direktori**, setiap tabel InnoDB = **file `.ibd`** yang berisi data + index + metadata (SDI). Sejak 8.0 tidak ada `.frm`; definisi tabel disimpan di data dictionary dan tercatat juga di dalam `.ibd`.

```sql
SELECT @@datadir, @@innodb_file_per_table, @@innodb_data_file_path;
SHOW TABLESPACES;                       -- daftar tablespace
SELECT * FROM INFORMATION_SCHEMA.FILES WHERE FILE_NAME LIKE '%tabel%';
```

Engine disimpan per tabel:

```sql
SHOW TABLE STATUS LIKE 'pesanan'\G
-- Engine: InnoDB, Row_format: Dynamic, Data_length, Index_length
```

## Jebakan
- `innodb_file_per_table=OFF` menaruh semua data di `ibdata1` — file itu tidak menyusut walau tabel dihapus.
- Redo log di 8.0.30+ berupa direktori `#innodb_redo`, bukan dua file `ib_logfile` seperti versi lama.
- MyISAM memakai tiga file (`.MYD`, `.MYI`, `.sdi`), bukan `.ibd`.
- `TRUNCATE` membuat tablespace baru; ukuran file lama tidak otomatis menyusut di sistem file.

## Latihan
1. Di mana definisi tabel InnoDB disimpan pada MySQL 8.0?
2. File apa yang menyimpan undo?

<details><summary>Jawaban</summary>
<p><b>1.</b> Di data dictionary (<code>mysql.ibd</code>), dan salinannya sebagai SDI di dalam file <code>.ibd</code> tabel itu.</p>
<p><b>2.</b> Undo tablespace: <code>undo_001</code>, <code>undo_002</code> (bertambah sesuai <code>innodb_undo_tablespaces</code>).</p>
</details>
