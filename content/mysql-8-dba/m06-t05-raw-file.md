---
title: Backup file mentah (raw file)
minutes: 20
level: Menengah
badge: lengkap
summary: Kapan menyalin file datadir langsung, dan bagaimana menjaga konsistensinya.
objectives:
  - Menjelaskan syarat konsistensi raw backup
  - Memakai FLUSH TABLES WITH READ LOCK dengan benar
  - Menilai risiko dan kecepatan metode ini
---
## Kenapa topik ini diuji
Raw file backup cepat tetapi mudah salah. Soal menguji syarat agar konsisten.

## Konsep inti
Raw backup = menyalin file datadir (`*.ibd`, `ibdata1`, `undo_*`, `binlog`). Cepat, tetapi **tidak konsisten** bila server menulis saat penyalinan.

Tiga cara mendapatkan konsistensi:

1. **Cold**: hentikan server (`innodb_fast_shutdown=0`), salin, start.
2. **Lock**: `FLUSH TABLES WITH READ LOCK;` lalu snapshot/salin, kemudian `UNLOCK TABLES`. Tidak cocok untuk downtime panjang.
3. **Snapshot storage** (LVM/EBS): flush + lock sebentar, ambil snapshot, unlock — nyaris instan.

```sql
FLUSH TABLES WITH READ LOCK;
-- jalankan snapshot/salin di sisi OS
UNLOCK TABLES;
```

Untuk menyalin satu tabel saja, gunakan transportable tablespace:

```sql
FLUSH TABLES appdb.pesanan FOR EXPORT;
-- salin pesanan.ibd dan pesanan.cfg ke server tujuan
UNLOCK TABLES;
```

## Jebakan
- Menyalin file saat server hidup tanpa lock/snapshot → backup rusak.
- Lupa menyalin `ibdata1` dan `undo_*`, sehingga hanya `.ibd` yang ada.
- Menyalin tabel InnoDB saja tanpa `.cfg` saat export tablespace.
- MyISAM tetap tidak aman walau dengan lock, karena tidak transaksional.

## Latihan
1. Mengapa menyalin datadir server hidup berbahaya?
2. Apa kegunaan file `.cfg` pada transportable tablespace?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena file bisa tersalin di tengah penulisan sehingga halaman dan log tidak sinkron.</p>
<p><b>2.</b> Menyimpan metadata tablespace agar bisa diimpor di server tujuan.</p>
</details>
