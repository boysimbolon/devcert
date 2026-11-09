---
title: Menggabungkan tabel (join)
minutes: 22
level: Menengah
badge: lengkap
summary: INNER, LEFT, RIGHT, CROSS, dan self join beserta efek NULL.
objectives:
  - Memilih jenis join sesuai hasil yang diinginkan
  - Menangani NULL pada outer join
  - Menghindari perkalian baris yang tidak disadari
---
## Kenapa topik ini diuji
Soal join menguji pemahaman hasil, bukan sintaks: berapa baris, dan nilai NULL mana yang muncul.

## Konsep inti
```sql
-- INNER: hanya yang cocok di kedua sisi
SELECT p.id, c.nama
  FROM pesanan p JOIN pelanggan c ON c.id = p.pelanggan_id;

-- LEFT: semua pesanan, walau pelanggannya tidak ada
SELECT p.id, c.nama FROM pesanan p
  LEFT JOIN pelanggan c ON c.id = p.pelanggan_id;

-- pelanggan tanpa pesanan
SELECT c.id, c.nama FROM pelanggan c
  LEFT JOIN pesanan p ON p.pelanggan_id = c.id
 WHERE p.id IS NULL;

-- self join: atasan-bawahan
SELECT a.nama AS bawahan, b.nama AS atasan
  FROM karyawan a LEFT JOIN karyawan b ON b.id = a.atasan_id;
```

| Join | Hasil |
|---|---|
| INNER | irisan |
| LEFT | semua kiri + cocok kanan |
| RIGHT | semua kanan + cocok kiri |
| CROSS | perkalian kartesian |
| FULL OUTER | **tidak ada di MySQL**; tiru dengan UNION |

## Jebakan
- `FULL OUTER JOIN` tidak didukung; gunakan `LEFT JOIN ... UNION ... RIGHT JOIN`.
- Kondisi di `WHERE` untuk tabel kanan mengubah LEFT JOIN menjadi INNER.
- Join tanpa kondisi = CROSS JOIN (bisa meledakkan baris).
- Kolom join dengan tipe/collation berbeda → index tidak dipakai.

## Latihan
1. Bagaimana menemukan pelanggan tanpa pesanan?
2. Mengapa `WHERE c.kota='X'` pada LEFT JOIN mengubah hasil?

<details><summary>Jawaban</summary>
<p><b>1.</b> LEFT JOIN lalu <code>WHERE p.id IS NULL</code>.</p>
<p><b>2.</b> Karena baris dengan c.kota NULL (tanpa pasangan) ikut tersaring, sehingga hasilnya setara INNER JOIN.</p>
</details>
