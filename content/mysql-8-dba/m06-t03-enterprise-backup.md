---
title: Backup dan restore dengan MySQL Enterprise Backup
minutes: 24
level: Menengah
badge: lengkap
summary: Hot backup fisik, inkremental, apply-log, dan copy-back.
objectives:
  - Menjalankan full dan incremental backup
  - Menerapkan log agar backup siap restore
  - Melakukan restore ke lokasi yang benar
---
## Kenapa topik ini diuji
MEB adalah alat backup fisik resmi. Soal menguji urutan: backup → apply-log → copy-back.

## Konsep inti
```bash
# full backup (hot, InnoDB konsisten)
mysqlbackup --defaults-file=/etc/my.cnf \
  --user=dba --password --backup-dir=/backup/full \
  --compress --encrypt-password=*** backup-and-apply-log

# incremental
mysqlbackup --defaults-file=/etc/my.cnf \
  --user=dba --password --incremental \
  --incremental-base=dir:/backup/full \
  --backup-dir=/backup/inc1 backup-and-apply-log

# restore
mysqlbackup --defaults-file=/etc/my.cnf --backup-dir=/backup/full \
  --datadir=/var/lib/mysql-restore copy-back-and-apply-log
```

Langkah restore yang benar:

1. Hentikan server.
2. Siapkan datadir kosong dengan kepemilikan `mysql:mysql`.
3. `copy-back` (atau `copy-back-and-apply-log`).
4. Perbaiki izin, start server.

`mysqlbackup` butuh akun dengan privilege `BACKUP_ADMIN` (atau `RELOAD`, `PROCESS`).

## Jebakan
- Lupa `apply-log`: backup belum dalam kondisi konsisten.
- `copy-back` ke datadir yang masih berisi file lama → konflik.
- Izin file setelah restore masih milik root → server gagal start.
- Incremental tanpa `--incremental-base` yang benar menghasilkan rantai rusak.

## Latihan
1. Apa fungsi `apply-log`?
2. Perintah restore ke datadir yang sama?

<details><summary>Jawaban</summary>
<p><b>1.</b> Menerapkan redo/undo pada file backup sehingga menjadi konsisten dan siap dipakai.</p>
<p><b>2.</b> <code>mysqlbackup --backup-dir=... copy-back-and-apply-log</code> setelah server dihentikan dan datadir dikosongkan.</p>
</details>
