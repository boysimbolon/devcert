---
title: MERGE statement
minutes: 20
level: Menengah
badge: lengkap
summary: Upsert — memperbarui yang ada dan menyisipkan yang baru dalam satu pernyataan.
objectives:
  - Menulis MERGE dengan MATCHED dan NOT MATCHED
  - Menentukan sumber data
  - Menghindari kesalahan umum pada ON
---
## Kenapa topik ini diuji
MERGE adalah "upsert" Oracle; soal menyodorkan kebutuhan sinkronisasi dua tabel.

## Konsep inti
```sql
MERGE INTO stok_target t
USING (SELECT product_id, qty FROM stok_sumber) s
   ON (t.product_id = s.product_id)
WHEN MATCHED THEN
  UPDATE SET t.qty = s.qty
WHEN NOT MATCHED THEN
  INSERT (product_id, qty) VALUES (s.product_id, s.qty);
```

Aturan: `ON` mendefinisikan kunci pencocokan; klausa `MATCHED` menangani baris yang ada; `NOT MATCHED` menangani yang baru. Bisa memakai `DELETE` di klausa MATCHED (dengan kondisi).

## Jebakan
- `ON` yang tidak unik membuat satu baris target ter-update berkali-kali → ORA-30926.
- Tidak bisa meng-update kolom yang dipakai di `ON`.
- MERGE tidak otomatis menghapus baris target yang tidak ada di sumber.
- Perlu hak INSERT dan UPDATE pada target.

## Latihan
1. Apa akibat `ON` yang tidak unik?
2. Bagaimana MERGE menghapus baris target yang hilang di sumber?

<details><summary>Jawaban</summary>
<p><b>1.</b> ORA-30926 unable to get a stable set of rows.</p>
<p><b>2.</b> Tidak otomatis; tambahkan <code>DELETE WHERE</code> di klausa MATCHED atau jalankan DELETE terpisah.</p>
</details>
