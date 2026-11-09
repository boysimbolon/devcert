---
title: Backup logis dengan mysqldump dan mysqlpump
minutes: 22
level: Menengah
badge: lengkap
summary: Opsi penting, konsistensi transaksional, dan batasan pada data besar.
objectives:
  - Menulis perintah dump yang konsisten
  - Memilih opsi untuk rutin, trigger, dan GTID
  - Mengetahui status mysqlpump di MySQL 8.0
---
## Kenapa topik ini diuji
`mysqldump` adalah alat yang paling sering muncul di soal praktis, dan setiap opsi punya konsekuensi.

## Konsep inti
```bash
# konsisten tanpa mengunci (InnoDB)
mysqldump --single-transaction --quick \
  --routines --triggers --events --set-gtid-purged=OFF \
  --databases appdb > appdb.sql

# semua database + binlog position
mysqldump --single-transaction --all-databases --source-data=2 > all.sql

# restore
mysql < appdb.sql
```

Opsi penting:

| Opsi | Fungsi |
|---|---|
| `--single-transaction` | snapshot konsisten (InnoDB) |
| `--quick` | stream baris, hemat memori |
| `--routines`, `--triggers`, `--events` | ikutkan objek non-tabel |
| `--set-gtid-purged` | sertakan GTID (untuk replikasi) |
| `--source-data=2` | catat binlog position sebagai komentar |
| `--where` | dump sebagian data |

`mysqlpump`: versi paralel dengan opsi per-database, tetapi **deprecated** sejak 8.0.34; arah baru adalah `mysqldump` atau `mysqlsh` util.

## Jebakan
- Tanpa `--single-transaction`, dump bisa tidak konsisten pada tabel yang berubah.
- `--set-gtid-purged=OFF` membuat dump tidak bisa dipakai untuk replikasi berbasis GTID.
- Lupa `--routines` sehingga prosedur hilang saat restore.
- Restore besar lebih cepat dengan `--init-command="SET autocommit=0"` dan mematikan `unique_checks`/`foreign_key_checks` sementara.

## Latihan
1. Opsi apa untuk dump konsisten pada InnoDB yang aktif?
2. Mengapa mysqlpump tidak lagi disarankan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>--single-transaction</code>.</p>
<p><b>2.</b> Karena sudah deprecated sejak MySQL 8.0.34; gunakan <code>mysqldump</code> atau <code>mysqlsh</code> util.</p>
</details>
