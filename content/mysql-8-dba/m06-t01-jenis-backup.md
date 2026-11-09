---
title: Jenis-jenis backup
minutes: 20
level: Dasar
badge: lengkap
summary: Logis vs fisik, panas vs dingin, penuh vs inkremental, dan snapshot.
objectives:
  - Membedakan backup logis dan fisik
  - Menjelaskan hot, warm, dan cold backup
  - Memilih jenis sesuai kebutuhan
---
## Kenapa topik ini diuji
Soal klasifikasi: diberikan kebutuhan, pilih jenis backup yang tepat. Ini pengetahuan yang harus otomatis.

## Konsep inti
| Dimensi | Pilihan | Catatan |
|---|---|---|
| Bentuk | **logis** (SQL) vs **fisik** (file) | logis portabel, fisik cepat |
| Kondisi server | **hot** (online), **warm**, **cold** (offline) | InnoDB mendukung hot backup |
| Cakupan | penuh, inkremental, diferensial | Enterprise Backup mendukung inkremental |
| Metode | dump, file copy, snapshot storage | snapshot = paling cepat |

Karakteristik:

- **Logis** (`mysqldump`): lambat untuk data besar, restore lambat, portabel antar versi, mudah diedit.
- **Fisik** (Enterprise Backup, file copy): cepat, cocok untuk TB, terikat versi/arsitektur.
- **Hot backup**: server tetap melayani; butuh mekanisme konsisten (snapshot/MVB).
- **Cold backup**: server berhenti; paling sederhana dan konsisten.

## Jebakan
- Menganggap `mysqldump` cukup untuk database 500 GB — restore bisa berjam-jam.
- Cold backup tanpa `innodb_fast_shutdown=0` → butuh recovery panjang.
- Backup fisik tidak otomatis konsisten bila file disalin saat server menulis.
- Lupa bahwa MyISAM tidak mendukung transaksi konsisten saat hot backup.

## Latihan
1. Kapan backup logis lebih tepat daripada fisik?
2. Mengapa cold backup paling konsisten?

<details><summary>Jawaban</summary>
<p><b>1.</b> Untuk database kecil/menengah, migrasi antar versi, atau kebutuhan selektif per tabel.</p>
<p><b>2.</b> Karena server berhenti sehingga tidak ada penulisan yang berlangsung saat file disalin.</p>
</details>
