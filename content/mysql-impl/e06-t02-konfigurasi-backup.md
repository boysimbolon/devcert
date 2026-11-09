---
title: Mengonfigurasi backup MySQL
minutes: 20
level: Menengah
badge: lengkap
summary: Penjadwalan, retensi, enkripsi, dan verifikasi backup.
objectives:
  - Menyusun jadwal dan retensi
  - Mengamankan backup dengan enkripsi
  - Membuktikan backup bisa direstore
---
## Kenapa topik ini diuji
Soal skenario: RPO/RTO tertentu, jadwal mana yang memenuhi.

## Konsep inti
```bash
# defaults file khusus backup
cat > /etc/mysql/backup.cnf <<'EOF'
[mysqlbackup]
user=dba
password=***
backup-dir=/backup
compress
encrypt-password=***
EOF
chmod 600 /etc/mysql/backup.cnf

# jadwal harian
0 2 * * *  mysqlbackup --defaults-file=/etc/mysql/backup.cnf backup-and-apply-log
```

Strategi berlapis:

```text
Mingguan : full backup, retensi 8 pekan
Harian   : inkremental, retensi 14 hari
Berjalan : binlog, retensi 7 hari (PITR)
Bulanan  : arsip off-site, terenkripsi
```

Verifikasi wajib: restore ke instance uji, lalu `CHECK TABLE` dan hitung baris kunci.

## Jebakan
- Backup terenkripsi tanpa menyimpan password enkripsi = tidak bisa dipulihkan.
- Backup di host yang sama tidak melindungi dari kehilangan server.
- Retensi tanpa pembersihan otomatis membuat disk penuh.
- Tidak pernah menguji restore sampai insiden nyata.

## Latihan
1. Mengapa backup harus diuji restore?
2. Komponen apa untuk mencapai RPO beberapa menit?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena backup yang tidak pernah direstore belum terbukti dapat dipakai.</p>
<p><b>2.</b> Binlog yang diarsipkan terus-menerus (untuk PITR).</p>
</details>
