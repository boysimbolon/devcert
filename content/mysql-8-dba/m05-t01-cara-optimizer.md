---
title: Bagaimana MySQL mengoptimasi query
minutes: 24
level: Menengah
badge: lengkap
summary: Optimizer berbasis biaya, statistik, EXPLAIN, dan pemilihan akses.
objectives:
  - Menjelaskan cost-based optimizer
  - Membaca EXPLAIN dan EXPLAIN ANALYZE
  - Mengenali akses yang buruk (full scan, filesort, temporary)
---
## Kenapa topik ini diuji
Ini inti domain optimasi. Soal menanyakan arti kolom EXPLAIN dan mengapa index tidak dipakai.

## Konsep inti
MySQL memilih rencana berdasarkan **biaya** (I/O + CPU) memakai statistik index. Rencana bisa berubah ketika statistik berubah.

```sql
EXPLAIN SELECT * FROM pesanan WHERE pelanggan_id = 42 ORDER BY tanggal DESC;

EXPLAIN ANALYZE
SELECT * FROM pesanan WHERE pelanggan_id = 42 ORDER BY tanggal DESC;
```

Kolom penting:

| Kolom | Arti |
|---|---|
| `type` | `const`, `eq_ref`, `ref`, `range`, `index`, `ALL` (terburuk) |
| `key` | index yang dipakai |
| `rows` | perkiraan baris diperiksa |
| `filtered` | persentase baris lolos kondisi |
| `Extra` | `Using index` (covering), `Using temporary`, `Using filesort`, `Using where` |

```sql
EXPLAIN FORMAT=JSON SELECT ...\G
SHOW WARNINGS;                  -- setelah EXPLAIN, tampilkan query yang ditransformasi
```

## Jebakan
- `type=ALL` pada tabel besar = full scan; sering karena fungsi pada kolom (`WHERE DATE(tgl)=...`).
- `Using filesort` tidak selalu buruk, tapi mahal pada hasil besar.
- `Using temporary` muncul pada GROUP BY tanpa index pendukung.
- Statistik usang membuat optimizer memilih rencana salah; perbarui dengan `ANALYZE TABLE`.

## Latihan
1. Apa arti `type=ALL` dan kapan berbahaya?
2. Mengapa `WHERE DATE(kolom) = '2026-01-01'` menghalangi index?

<details><summary>Jawaban</summary>
<p><b>1.</b> Full table scan; berbahaya pada tabel besar karena membaca semua baris.</p>
<p><b>2.</b> Karena fungsi diterapkan pada kolom, sehingga index pada kolom itu tidak bisa dipakai; ubah menjadi rentang tanggal.</p>
</details>
