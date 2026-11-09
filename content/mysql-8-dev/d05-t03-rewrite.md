---
title: Menulis ulang query untuk optimasi
minutes: 22
level: Menengah
badge: lengkap
summary: Pola query yang membunuh index dan cara menulis ulang tanpa mengubah hasil.
objectives:
  - Mengenali pola yang menghalangi index
  - Menulis ulang subquery dan join
  - Menghindari SELECT * dan paginasi mahal
---
## Kenapa topik ini diuji
Soal memberi query lambat dan meminta versi yang setara tetapi lebih cepat.

## Konsep inti
```sql
-- buruk: fungsi pada kolom
SELECT * FROM pesanan WHERE DATE(tanggal) = '2026-03-01';
-- baik: rentang
SELECT * FROM pesanan WHERE tanggal >= '2026-03-01' AND tanggal < '2026-03-02';

-- buruk: LIKE dengan wildcard depan
SELECT * FROM pelanggan WHERE nama LIKE '%budi%';
-- baik: FULLTEXT atau pencarian terarah
SELECT * FROM pelanggan WHERE nama LIKE 'budi%';

-- buruk: NOT IN dengan subquery yang bisa NULL
SELECT * FROM pelanggan WHERE id NOT IN (SELECT pelanggan_id FROM pesanan);
-- baik: NOT EXISTS
SELECT c.* FROM pelanggan c WHERE NOT EXISTS (SELECT 1 FROM pesanan p WHERE p.pelanggan_id=c.id);

-- buruk: OFFSET besar
SELECT * FROM pesanan ORDER BY id LIMIT 10 OFFSET 100000;
-- baik: keyset
SELECT * FROM pesanan WHERE id > 100000 ORDER BY id LIMIT 10;
```

Juga: hindari `SELECT *` (mengambil kolom besar), dan ubah `OR` antar kolom berbeda menjadi `UNION ALL` bila perlu.

## Jebakan
- `NOT IN` dengan NULL di subquery mengembalikan hasil kosong.
- Mengubah query tanpa memeriksa hasil setara (semantik bisa berubah).
- Mengganti `DISTINCT` dengan `GROUP BY` tanpa alasan jelas.
- Paginasi keyset butuh urutan unik dan stabil.

## Latihan
1. Mengapa `NOT IN` bisa mengembalikan nol baris?
2. Alternatif keyset pagination?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena jika subquery menghasilkan NULL, perbandingan menjadi UNKNOWN sehingga tidak ada baris yang lolos.</p>
<p><b>2.</b> <code>WHERE id &gt; nilai_terakhir ORDER BY id LIMIT n</code>.</p>
</details>
