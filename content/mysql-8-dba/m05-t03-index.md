---
title: Membuat index untuk meningkatkan performa
minutes: 24
level: Menengah
badge: lengkap
summary: B-tree, composite index, covering index, prefix, dan index tak terlihat.
objectives:
  - Memilih kolom dan urutan untuk composite index
  - Membuat covering index
  - Memakai invisible index untuk uji coba aman
---
## Kenapa topik ini diuji
Index adalah alat optimasi utama. Soal menguji urutan kolom dan mengapa index tidak terpakai.

## Konsep inti
```sql
-- composite: urutan penting (leftmost prefix)
CREATE INDEX idx_pel_tgl ON pesanan (pelanggan_id, tanggal);
-- dipakai untuk WHERE pelanggan_id = ? AND tanggal > ?
-- TIDAK dipakai optimal untuk WHERE tanggal > ? saja

-- covering index: semua kolom ada di index
CREATE INDEX idx_cover ON pesanan (pelanggan_id, tanggal, total);
SELECT tanggal, total FROM pesanan WHERE pelanggan_id = 7;   -- Extra: Using index

-- prefix index untuk kolom panjang
CREATE INDEX idx_email_prefix ON pelanggan (email(20));

-- index menurun (8.0)
CREATE INDEX idx_tgl_desc ON pesanan (tanggal DESC);

-- index tak terlihat: diuji tanpa memengaruhi optimizer
ALTER TABLE pesanan ALTER INDEX idx_pel_tgl INVISIBLE;
ALTER TABLE pesanan ALTER INDEX idx_pel_tgl VISIBLE;
```

```sql
SHOW INDEX FROM pesanan;
SELECT * FROM sys.schema_unused_indexes;
SELECT * FROM sys.schema_redundant_indexes;
```

## Jebakan
- Urutan kolom composite salah → index tidak terpakai untuk query yang sering.
- Index pada kolom dengan kardinalitas rendah (mis. boolean) jarang membantu.
- Terlalu banyak index memperlambat INSERT/UPDATE dan menambah ukuran.
- `LIKE '%kata'` tidak memakai index; hanya `LIKE 'kata%'`.

## Latihan
1. Index mana untuk `WHERE pelanggan_id=? ORDER BY tanggal DESC`?
2. Apa keuntungan invisible index?

<details><summary>Jawaban</summary>
<p><b>1.</b> Composite <code>(pelanggan_id, tanggal)</code> — kolom equality dulu, lalu kolom urutan.</p>
<p><b>2.</b> Bisa diuji dampaknya tanpa risiko mengubah rencana query secara langsung; cukup di-<i>invisible</i> lalu dihapus bila tidak berpengaruh.</p>
</details>
