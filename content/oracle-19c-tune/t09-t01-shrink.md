---
title: Menyusutkan segmen
minutes: 18
level: Menengah
badge: lengkap
summary: SHRINK SPACE, MOVE, dan kapan masing-masing dipakai.
objectives:
  - Menjelaskan kapan segmen perlu disusutkan
  - Memakai SHRINK SPACE dengan benar
  - Membandingkan dengan MOVE
---
## Kenapa topik ini diuji
Setelah banyak DELETE, ruang tidak kembali ke OS; soal menanyakan cara mengembalikannya.

## Konsep inti
```sql
ALTER TABLE pesanan SHRINK SPACE CASCADE;   -- termasuk index
ALTER TABLE pesanan SHRINK SPACE COMPACT;   -- tanpa memindahkan HWM saat itu
ALTER INDEX idx_pesanan SHRINK SPACE;

ALTER TABLE pesanan MOVE;                   -- pindah segmen (butuh ruang ekstra)
ALTER TABLE pesanan ENABLE ROW MOVEMENT;    -- prasyarat SHRINK
```

`SHRINK` membutuhkan `ENABLE ROW MOVEMENT` dan bekerja online (dengan overhead); `MOVE` menulis ulang segmen dan membuat index unusable.

## Jebakan
- `SHRINK` tanpa `ROW MOVEMENT` gagal.
- `MOVE` membuat index tidak valid → harus rebuild.
- `SHRINK` tidak mengembalikan ruang bila ada baris di blok akhir yang padat.
- Datafile tidak mengecil otomatis; perlu `RESIZE` setelahnya.

## Latihan
1. Prasyarat SHRINK SPACE?
2. Apa efek MOVE pada index?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ALTER TABLE ... ENABLE ROW MOVEMENT;</code></p>
<p><b>2.</b> Index menjadi unusable dan harus di-rebuild.</p>
</details>
