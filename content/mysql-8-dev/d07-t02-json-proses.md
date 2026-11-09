---
title: Mengolah data dalam dokumen JSON
minutes: 22
level: Menengah
badge: lengkap
summary: JSON_TABLE, JSON_SET, JSON_CONTAINS, dan pencarian di dalam dokumen.
objectives:
  - Mengubah JSON menjadi baris relasional
  - Memodifikasi dokumen JSON
  - Mencari nilai di dalam array
---
## Kenapa topik ini diuji
Soal menguji `JSON_TABLE` dan fungsi pencarian, karena keduanya paling sering dipakai di aplikasi.

## Konsep inti
```sql
-- JSON menjadi tabel
SELECT jt.nama, jt.harga
  FROM produk,
       JSON_TABLE(produk.atribut, '$.varian[*]'
            COLUMNS (
              nama  VARCHAR(50) PATH '$.nama',
              harga DECIMAL(10,2) PATH '$.harga'
            )) AS jt;

-- modifikasi
SELECT JSON_SET(atribut, '$.stok', 10) FROM produk;
SELECT JSON_REMOVE(atribut, '$.tags[0]') FROM produk;
SELECT JSON_MERGE_PATCH(atribut, '{"diskon":0.1}') FROM produk;

-- pencarian
SELECT * FROM produk WHERE JSON_CONTAINS(atribut->'$.tags', '"arabika"');
SELECT * FROM produk WHERE JSON_SEARCH(atribut, 'one', 'Gayo') IS NOT NULL;
SELECT JSON_LENGTH(atribut->'$.tags');
SELECT JSON_VALID('{"a":1}');
```

## Jebakan
- `JSON_CONTAINS` butuh nilai JSON yang valid: string harus `'"arabika"'`.
- `JSON_MERGE_PATCH` menimpa nilai, `JSON_MERGE_PRESERVE` menggabungkan array.
- `JSON_TABLE` butuh path array; untuk objek tunggal gunakan `'$'`.
- Kolom JSON tidak bisa langsung `ORDER BY` dengan makna angka; cast dulu.

## Latihan
1. Fungsi untuk memecah array JSON menjadi baris?
2. Mengapa `JSON_CONTAINS` gagal dengan `'arabika'`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>JSON_TABLE</code>.</p>
<p><b>2.</b> Karena argumen harus nilai JSON; string JSON perlu tanda kutip ganda di dalamnya: <code>'"arabika"'</code>.</p>
</details>
