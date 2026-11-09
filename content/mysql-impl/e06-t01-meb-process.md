---
title: Proses MySQL Enterprise Backup
minutes: 22
level: Menengah
badge: lengkap
summary: Hot backup fisik, fase copy dan apply-log, serta inkremental.
objectives:
  - Menjelaskan tahapan MEB
  - Membedakan full dan incremental
  - Menentukan kapan backup konsisten tersedia
---
## Kenapa topik ini diuji
Soal proses: apa yang terjadi setelah `backup`, dan mengapa perlu `apply-log`.

## Konsep inti
```text
1. Backup   : salin tablespace + redo selama server melayani (hot)
2. apply-log: terapkan perubahan redo/undo agar konsisten
3. Restore  : copy-back ke datadir (server berhenti) atau restore selektif
```

```bash
mysqlbackup --defaults-file=/etc/my.cnf --user=dba --password \
  --backup-dir=/backup/full --compress \
  --encrypt-password=*** backup-and-apply-log
```

Inkremental memakai base backup sebelumnya:

```bash
mysqlbackup --defaults-file=/etc/my.cnf --incremental \
  --incremental-base=dir:/backup/full \
  --backup-dir=/backup/inc1 backup-and-apply-log
```

MEB butuh akun dengan `BACKUP_ADMIN`.

## Jebakan
- Tanpa `apply-log`, backup belum konsisten.
- `copy-back` ke datadir yang tidak kosong mencampur file lama.
- Izin file hasil restore harus `mysql:mysql`.
- Inkremental yang base-nya hilang tidak bisa dipakai.

## Latihan
1. Apa fungsi apply-log?
2. Apa syarat akun untuk MEB?

<details><summary>Jawaban</summary>
<p><b>1.</b> Menerapkan redo/undo pada file backup sehingga menjadi konsisten dan siap dipakai.</p>
<p><b>2.</b> Privilege <code>BACKUP_ADMIN</code> (plus akses baca sesuai kebutuhan).</p>
</details>
