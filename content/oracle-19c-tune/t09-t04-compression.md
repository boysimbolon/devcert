---
title: Kompresi tabel
minutes: 20
level: Menengah
badge: lengkap
summary: Basic, OLTP, dan Hybrid Columnar Compression serta kapan dipakai.
objectives:
  - Membedakan jenis kompresi
  - Memilih kompresi untuk OLTP vs DW
  - Menjelaskan trade-off CPU vs I/O
---
## Kenapa topik ini diuji
Soal menanyakan kompresi mana untuk beban tertentu, dan apa konsekuensinya.

## Konsep inti
| Jenis | Cocok untuk | Catatan |
|---|---|---|
| `BASIC` | data jarang diubah | kompresi sederhana |
| `OLTP` (Advanced Compression) | OLTP | kompresi saat insert/update |
| `QUERY LOW/HIGH` (HCC) | data warehouse | rasio tinggi, butuh Exadata/hardware tertentu |
| `ARCHIVE` | data arsip | rasio tertinggi, hanya baca |

```sql
CREATE TABLE arsip_penjualan COMPRESS FOR OLTP AS SELECT * FROM penjualan;
ALTER TABLE penjualan COMPRESS FOR OLTP;
ALTER TABLE penjualan MOVE NOCOMPRESS;
```

## Jebakan
- HCC membutuhkan storage pendukung; tidak semua platform.
- Kompresi OLTP menambah CPU per DML.
- Data yang sudah dikompres tidak otomatis ter-kompres ulang saat diubah.
- Kompresi tidak menggantikan desain skema yang benar.

## Latihan
1. Kompresi untuk tabel OLTP yang sering di-update?
2. Mengapa HCC tidak bisa dipakai di semua lingkungan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>COMPRESS FOR OLTP</code>.</p>
<p><b>2.</b> Karena butuh dukungan storage/hardware khusus (mis. Exadata).</p>
</details>
