---
title: Membuat dan mengakses document store
minutes: 20
level: Menengah
badge: lengkap
summary: Membuat collection, validasi skema, dan index pada dokumen.
objectives:
  - Membuat collection dan mengatur validasi
  - Mengindeks field dokumen
  - Mengakses collection dari aplikasi
---
## Kenapa topik ini diuji
Soal praktis: perintah membuat collection dan index, serta validasi JSON.

## Konsep inti
```sql
-- collection juga bisa dibuat lewat SQL
CREATE TABLE appdb.barang (
  doc JSON,
  _id VARCHAR(32) GENERATED ALWAYS AS (JSON_UNQUOTE(JSON_EXTRACT(doc,'$._id'))) STORED PRIMARY KEY
);

-- validasi skema
ALTER TABLE appdb.barang ADD CONSTRAINT chk_barang CHECK (
  JSON_SCHEMA_VALID('{"type":"object","required":["_id","nama"]}', doc)
);

-- index pada field JSON
ALTER TABLE appdb.barang
  ADD COLUMN nama VARCHAR(100) GENERATED ALWAYS AS (doc->>'$.nama') STORED,
  ADD INDEX idx_nama (nama);

-- multi-valued index untuk array
ALTER TABLE appdb.barang
  ADD INDEX idx_tag ((CAST(doc->'$.tags' AS CHAR(24) ARRAY)));
```

Lewat Shell:

```javascript
db.createCollection('barang');
db.barang.createIndex('idx_nama', {fields:[{field:'$.nama', type:'VARCHAR(100)'}]});
```

## Jebakan
- `JSON_SCHEMA_VALID` membutuhkan JSON Schema yang valid; kesalahan skema membuat insert gagal.
- Generated column `STORED` memakan ruang; `VIRTUAL` tidak bisa di-index primary.
- Collection tanpa `_id` unik bisa menerima duplikat.
- Index pada path JSON harus cocok dengan ekspresi yang dipakai query.

## Latihan
1. Fungsi untuk validasi dokumen terhadap JSON Schema?
2. Jenis generated column yang bisa di-index?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>JSON_SCHEMA_VALID</code> (dipakai dalam CHECK constraint).</p>
<p><b>2.</b> <code>STORED</code>; <code>VIRTUAL</code> juga bisa di-index pada MySQL 8.0, tetapi <code>STORED</code> lebih umum untuk kasus ini.</p>
</details>
