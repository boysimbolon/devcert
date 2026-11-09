---
title: Mengonfigurasi index
minutes: 22
level: Menengah
badge: lengkap
summary: Jenis index, urutan kolom, dan kapan index tidak dipakai.
objectives:
  - Memilih jenis index sesuai kebutuhan
  - Menyusun composite index dengan urutan benar
  - Memeriksa index yang dipakai query
---
## Kenapa topik ini diuji
Index adalah keputusan desain yang paling sering ditanyakan pada level implementasi.

## Konsep inti
```sql
CREATE INDEX idx_pel_tgl ON pesanan (pelanggan_id, tanggal);
CREATE UNIQUE INDEX uq_email ON pelanggan (email);
CREATE FULLTEXT INDEX ft_nama ON artikel (judul, isi);
CREATE SPATIAL INDEX sp_lokasi ON tempat (posisi);
CREATE INDEX idx_prefix ON pelanggan (nama(20));
CREATE INDEX idx_expr ON pelanggan ((LOWER(email)));

SHOW INDEX FROM pesanan;
EXPLAIN SELECT * FROM pesanan WHERE pelanggan_id = 7;
```

| Jenis | Untuk |
|---|---|
| B-tree | perbandingan, urutan, range |
| FULLTEXT | pencarian kata di teks |
| SPATIAL | geometri (R-tree) |
| Prefix | kolom panjang (VARCHAR/TEXT) |
| Functional | ekspresi, mis. `LOWER(email)` |

## Jebakan
- Urutan kolom salah → index tidak dipakai untuk query yang sering.
- Index pada kolom dengan kardinalitas rendah jarang membantu.
- `LIKE '%x%'` tidak memakai B-tree.
- FULLTEXT punya aturan sendiri (stopword, panjang minimum kata).

## Latihan
1. Index untuk pencarian kata dalam artikel?
2. Mengapa urutan kolom composite penting?

<details><summary>Jawaban</summary>
<p><b>1.</b> FULLTEXT index.</p>
<p><b>2.</b> Karena index dipakai dari kiri: hanya kombinasi awal yang bisa dimanfaatkan.</p>
</details>
