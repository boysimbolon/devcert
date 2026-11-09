---
title: Menganalisis query untuk optimasi
minutes: 20
level: Menengah
badge: lengkap
summary: EXPLAIN, EXPLAIN ANALYZE, dan membaca rencana eksekusi.
objectives:
  - Membaca kolom penting EXPLAIN
  - Membedakan perkiraan dan hasil nyata
  - Menemukan penyebab rencana buruk
---
## Kenapa topik ini diuji
Soal memberi rencana eksekusi dan menanyakan masalahnya.

## Konsep inti
```sql
EXPLAIN SELECT c.nama, SUM(p.total)
  FROM pesanan p JOIN pelanggan c ON c.id = p.pelanggan_id
 WHERE p.tanggal >= '2026-01-01'
 GROUP BY c.nama;

EXPLAIN ANALYZE SELECT ...;      -- menjalankan query + waktu nyata
EXPLAIN FORMAT=JSON SELECT ...;
SHOW WARNINGS;                    -- query hasil transformasi optimizer
```

Yang dibaca:

- `type`: `ALL` (buruk) → `index` → `range` → `ref` → `eq_ref` → `const` (baik).
- `rows` dan `filtered`: perkiraan baris diperiksa.
- `Extra`: `Using temporary`, `Using filesort`, `Using index`, `Using where`.

`EXPLAIN ANALYZE` membandingkan `rows` perkiraan dengan `actual rows` — selisih besar menandakan statistik usang.

## Jebakan
- `Using filesort` tidak selalu bisa dihilangkan, tetapi mahal pada baris banyak.
- Perkiraan `rows` bisa sangat meleset; jangan mengambil kesimpulan tanpa ANALYZE.
- `Using temporary` pada GROUP BY besar bisa berarti memori/disk.
- EXPLAIN tidak menjalankan query; hasilnya rencana, bukan bukti performa.

## Latihan
1. Kolom mana menunjukkan metode akses?
2. Kapan memakai EXPLAIN ANALYZE?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>type</code> (dan <code>key</code> untuk index yang dipakai).</p>
<p><b>2.</b> Saat butuh waktu dan jumlah baris nyata, bukan hanya perkiraan.</p>
</details>
