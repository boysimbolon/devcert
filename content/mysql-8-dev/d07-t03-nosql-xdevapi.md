---
title: NoSQL dan X DevAPI
minutes: 20
level: Menengah
badge: lengkap
summary: Model dokumen MySQL, protokol X, dan konsep CRUD tanpa SQL.
objectives:
  - Menjelaskan document store di MySQL
  - Membedakan SQL dan X DevAPI
  - Menulis operasi CRUD dasar
---
## Kenapa topik ini diuji
Soal konsep: apa yang dimaksud document store, dan bagaimana aplikasi mengaksesnya.

## Konsep inti
MySQL document store = **collection** (mirip tabel tanpa skema tetap) yang menyimpan dokumen JSON. Di bawahnya tetap tabel InnoDB dengan kolom `doc` JSON dan `_id`.

```javascript
// MySQL Shell (JavaScript)
var session = mysqlx.getSession({user:'app', host:'localhost', port:33060});
var db = session.getSchema('appdb');
var col = db.getCollection('produk');

col.add({ _id: 'kopi-1', nama: 'Kopi Gayo', harga: 95000 }).execute();

col.find('harga < 100000').fields('nama','harga').execute();
col.modify('_id = "kopi-1"').set('harga', 99000).execute();
col.remove('harga > 200000').execute();
```

Setara SQL-nya:

```sql
SELECT doc->>'$.nama' FROM appdb.produk WHERE doc->>'$.harga' < 100000;
```

Perbedaan penting: X DevAPI memakai port **33060**, protokol X, dan tidak membutuhkan SQL.

## Jebakan
- Collection bukan tabel biasa; `_id` wajib unik.
- Tidak semua fitur SQL tersedia (mis. join lintas collection terbatas).
- Port 33060 harus dibuka dan didukung driver `mysqlx`.
- `session.getSchema` berbeda dari `getDefaultSchema`.

## Latihan
1. Port berapa untuk X DevAPI?
2. Apa padanan tabel pada document store?

<details><summary>Jawaban</summary>
<p><b>1.</b> 33060 (protokol X).</p>
<p><b>2.</b> Collection.</p>
</details>
