---
title: Membuat dan menyimpan dokumen JSON
minutes: 22
level: Menengah
badge: lengkap
summary: Tipe JSON, validasi otomatis, dan fungsi pembentuk dokumen.
objectives:
  - Menyimpan JSON dan memastikan validitasnya
  - Memakai JSON_OBJECT dan JSON_ARRAY
  - Mengindeks kolom JSON secara benar
---
## Kenapa topik ini diuji
JSON adalah domain baru di ujian developer; soalnya menguji fungsi dan path.

## Konsep inti
```sql
CREATE TABLE produk (
  id INT PRIMARY KEY,
  nama VARCHAR(100),
  atribut JSON
);

INSERT INTO produk VALUES (1, 'Kopi', JSON_OBJECT('asal','Gayo','berat',250,'tags',JSON_ARRAY('arabika','single-origin')));

SELECT atribut->'$.asal'        AS asal,       -- JSON
       atribut->>'$.asal'       AS asal_teks,  -- teks
       JSON_EXTRACT(atribut,'$.tags[0]') AS tag1
  FROM produk;
```

Validitas: kolom `JSON` menolak dokumen tidak valid secara otomatis (`Invalid JSON text`).

Index untuk JSON:

```sql
ALTER TABLE produk
  ADD COLUMN asal VARCHAR(50) GENERATED ALWAYS AS (atribut->>'$.asal') STORED,
  ADD INDEX idx_asal (asal);

-- multi-valued index (8.0.17+)
ALTER TABLE produk ADD INDEX idx_tags ((CAST(atribut->'$.tags' AS CHAR(30) ARRAY)));
```

## Jebakan
- `->` mengembalikan JSON (dengan tanda kutip), `->>` mengembalikan teks.
- Mengindeks kolom JSON langsung tidak bisa; pakai generated column atau multi-valued index.
- Path peka terhadap penulisan: `'$.asal'` vs `'$."asal"'`.
- Angka di JSON disimpan sebagai tipe JSON number, bukan string.

## Latihan
1. Perbedaan `->` dan `->>`?
2. Cara mengindeks atribut JSON?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>-&gt;</code> mengembalikan nilai JSON, <code>-&gt;&gt;</code> mengembalikan string/teks.</p>
<p><b>2.</b> Buat generated column dari ekspresi JSON lalu index kolom itu, atau multi-valued index untuk array.</p>
</details>
