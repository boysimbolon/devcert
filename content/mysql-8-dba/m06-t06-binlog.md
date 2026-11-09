---
title: Backup binary log dan point-in-time recovery
minutes: 22
level: Menengah
badge: lengkap
summary: Mengamankan binlog, memakainya untuk PITR, dan mengatur retensi.
objectives:
  - Menjelaskan peran binlog dalam pemulihan
  - Menjalankan PITR dengan mysqlbinlog
  - Mengatur masa simpan binlog
---
## Kenapa topik ini diuji
PITR adalah soal favorit: dari backup penuh + binlog, pulihkan ke detik tertentu.

## Konsep inti
Binlog mencatat setiap perubahan data. Alur PITR:

```text
1. Restore backup penuh (mis. pukul 02:00)
2. Terapkan binlog dari 02:00 sampai waktu target
3. Verifikasi
```

```bash
# arsipkan binlog berjalan
mysqladmin -u root -p flush-logs
cp /var/lib/mysql/binlog.000042 /backup/binlog/

# lihat isi
mysqlbinlog --base64-output=DECODE-ROWS -v /backup/binlog/binlog.000042 | less

# terapkan sampai waktu tertentu
mysqlbinlog --stop-datetime="2026-03-14 10:30:00" /backup/binlog/binlog.000042 | mysql -u root -p
```

Pengaturan:

```sql
SHOW VARIABLES LIKE 'log_bin';
SHOW VARIABLES LIKE 'binlog_expire_logs_seconds';   -- mis. 1209600 = 14 hari
SET PERSIST binlog_expire_logs_seconds = 1209600;
SHOW BINARY LOGS;
SHOW BINLOG EVENTS IN 'binlog.000042' LIMIT 20;
```

## Jebakan
- Binlog tidak ikut terbackup → RPO sebesar interval backup.
- Menerapkan binlog tanpa `--stop-datetime`/`--stop-position` → melewati target.
- `binlog_expire_logs_seconds` terlalu pendek memutus rantai PITR.
- Menghapus binlog manual (`rm`) merusak indeks binlog; gunakan `PURGE BINARY LOGS`.

## Latihan
1. Apa dua komponen wajib untuk PITR?
2. Perintah menghentikan penerapan pada waktu tertentu?

<details><summary>Jawaban</summary>
<p><b>1.</b> Backup penuh yang konsisten dan binlog yang mencakup rentang waktu setelah backup.</p>
<p><b>2.</b> <code>mysqlbinlog --stop-datetime="..."</code> (atau <code>--stop-position</code>).</p>
</details>
