---
title: Memantau dan memahami statistik index
minutes: 20
level: Menengah
badge: lengkap
summary: Cardinality, ANALYZE TABLE, histogram, dan dampaknya pada rencana query.
objectives:
  - Membaca cardinality dan artinya
  - Memperbarui statistik dengan tepat
  - Memakai histogram untuk kolom tidak merata
---
## Kenapa topik ini diuji
Optimizer memilih index berdasarkan statistik. Statistik salah = rencana salah, walau index-nya ada.

## Konsep inti
```sql
SHOW INDEX FROM pesanan;         -- kolom Cardinality
ANALYZE TABLE pesanan;           -- perbarui statistik
SELECT * FROM mysql.innodb_index_stats WHERE table_name='pesanan'\G
SELECT * FROM mysql.innodb_table_stats WHERE table_name='pesanan'\G

-- histogram (8.0) untuk distribusi tidak merata
ANALYZE TABLE pesanan UPDATE HISTOGRAM ON status WITH 32 BUCKETS;
SELECT * FROM information_schema.COLUMNS
 WHERE TABLE_NAME='pesanan' AND COLUMN_NAME='status'\G
ANALYZE TABLE pesanan DROP HISTOGRAM ON status;
```

`innodb_stats_persistent=ON` (default) menyimpan statistik agar stabil antar restart. `innodb_stats_persistent_sample_pages` menentukan jumlah halaman sampel — makin besar makin akurat tapi makin lambat.

## Jebakan
- `Cardinality` adalah perkiraan; nilainya bisa sangat meleset pada tabel besar.
- `ANALYZE TABLE` mengunci singkat dan bisa terasa mahal pada tabel raksasa.
- Histogram hanya membantu kolom dengan distribusi miring, bukan semua kolom.
- Setelah mass insert/delete besar, statistik bisa usang sampai dianalisis ulang.

## Latihan
1. Apa arti cardinality rendah pada sebuah index?
2. Kapan histogram berguna?

<details><summary>Jawaban</summary>
<p><b>1.</b> Nilai kolom tidak banyak berbeda, sehingga index kurang selektif dan optimizer mungkin memilih full scan.</p>
<p><b>2.</b> Saat distribusi nilai tidak merata (mis. 90% baris berstatus 'selesai'), sehingga perkiraan baris lebih akurat.</p>
</details>
