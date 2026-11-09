---
title: In-Memory dengan fitur lain
minutes: 20
level: Menengah
badge: lengkap
summary: Kombinasi IM column store dengan partisi, join, dan kompresi.
objectives:
  - Memakai IM pada tabel partisi
  - Menjelaskan in-memory join
  - Mengombinasikan dengan fitur lain tanpa konflik
---
## Kenapa topik ini diuji
Soal menanyakan bagaimana IM berinteraksi dengan partisi, join, dan opsi storage.

## Konsep inti
```sql
ALTER TABLE penjualan MODIFY PARTITION p2026_01 INMEMORY;
ALTER TABLE penjualan INMEMORY PRIORITY CRITICAL;

-- in-memory join (dua tabel sama-sama di memori)
SELECT /*+ inmemory_join(d) */ ...
  FROM penjualan p JOIN dimensi_waktu d ON d.id = p.waktu_id;

SELECT * FROM v$im_column_level;
SELECT * FROM v$im_segments_detail;
```

Bisa dikombinasikan dengan: partisi (per partisi), kompresi kolom berbeda per kolom, dan `INMEMORY` pada materialized view.

## Jebakan
- Tabel lebih besar dari `inmemory_size` → sebagian tetap di disk (populate parsial).
- Prioritas menentukan objek mana yang dipertahankan saat memori terbatas.
- IM tidak otomatis menaikkan performa OLTP titik.
- Perubahan besar pada tabel memerlukan populate ulang.

## Latihan
1. Prioritas untuk objek paling penting?
2. Apa yang terjadi bila data melebihi inmemory_size?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>PRIORITY CRITICAL</code> (atau HIGH).</p>
<p><b>2.</b> Hanya sebagian yang dimuat ke memori; sisanya tetap dibaca dari disk.</p>
</details>
