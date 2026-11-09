---
title: Flash Cache
minutes: 18
level: Menengah
badge: lengkap
summary: Lapisan cache sekunder di storage flash untuk mengurangi I/O lambat.
objectives:
  - Menjelaskan peran flash cache
  - Mengatur kebijakan per objek
  - Menilai manfaatnya
---
## Kenapa topik ini diuji
Soal menanyakan lapisan cache tambahan dan cara mengatur prioritas objek.

## Konsep inti
```sql
SHOW PARAMETER db_flash_cache_size;
ALTER TABLE pesanan STORAGE (CELL_FLASH_CACHE KEEP);
ALTER TABLE arsip STORAGE (CELL_FLASH_CACHE NONE);

SELECT * FROM v$flash_cache_statistics;
```

Kebijakan `CELL_FLASH_CACHE`: `DEFAULT`, `KEEP`, `NONE`. `KEEP` memprioritaskan objek agar tetap di flash cache saat cache penuh.

## Jebakan
- Tidak semua platform punya flash cache (khas Exadata).
- `DEFAULT` bisa digeser oleh objek lain saat tekanan tinggi.
- Flash cache mengurangi latency, bukan menggantikan index/desain.
- Ukuran dan perilaku bergantung storage.

## Latihan
1. Nilai kebijakan untuk objek yang harus diprioritaskan?
2. Apakah flash cache tersedia di semua lingkungan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>KEEP</code>.</p>
<p><b>2.</b> Tidak; bergantung platform/storage (mis. Exadata).</p>
</details>
