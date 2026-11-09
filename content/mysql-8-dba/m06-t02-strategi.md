---
title: Menyusun strategi backup
minutes: 22
level: Menengah
badge: lengkap
summary: RPO/RTO, aturan 3-2-1, retensi, dan pengujian restore.
objectives:
  - Menentukan RPO dan RTO
  - Menyusun jadwal backup berlapis
  - Membuktikan backup bisa direstore
---
## Kenapa topik ini diuji
Soal strategi memberi skenario bisnis dan menanyakan jadwal yang memenuhi RPO/RTO.

## Konsep inti
- **RPO** (recovery point objective): seberapa banyak data boleh hilang → menentukan frekuensi binlog.
- **RTO** (recovery time objective): seberapa cepat harus pulih → menentukan jenis backup.

Pola berlapis:

```text
Mingguan : backup fisik penuh (Enterprise Backup) -> simpan 4-8 pekan
Harian   : backup logis/fisik + binlog -> simpan 7-14 hari
Berjalan  : binlog -> memungkinkan PITR sampai detik terakhir
Bulanan  : arsip off-site, terenkripsi
```

Aturan **3-2-1**: 3 salinan, 2 media berbeda, 1 di luar lokasi.

Wajib: **uji restore** berkala. Backup yang belum pernah direstore bukan backup, hanya harapan.

```bash
# jadwal contoh (cron)
0 2 * * *  /usr/bin/mysqlbackup --defaults-file=/etc/mysql/backup.cnf backup-and-apply-log
```

## Jebakan
- Menyimpan backup hanya di host yang sama — hilang bersama server.
- Tidak menyimpan binlog, sehingga RPO sebesar interval backup.
- Retensi tidak diatur: disk penuh dan backup terbaru gagal.
- Tidak pernah menguji restore sampai insiden nyata.

## Latihan
1. RPO 5 menit, apa yang harus disiapkan?
2. Mengapa aturan 3-2-1 penting?

<details><summary>Jawaban</summary>
<p><b>1.</b> Binlog harus tersimpan dan diarsipkan terus-menerus (mis. tiap 1-5 menit), bukan hanya backup harian.</p>
<p><b>2.</b> Karena satu media/lokasi bisa hilang sekaligus (disk rusak, bencana, ransomware).</p>
</details>
