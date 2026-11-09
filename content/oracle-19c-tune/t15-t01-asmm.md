---
title: Automatic Shared Memory Management
minutes: 20
level: Menengah
badge: lengkap
summary: ASMM membagi SGA otomatis antar komponen berdasarkan beban.
objectives:
  - Mengaktifkan ASMM
  - Melihat komponen SGA dinamis
  - Membandingkan ASMM dan manual
---
## Kenapa topik ini diuji
Soal menanyakan parameter mana yang mengaktifkan pembagian otomatis.

## Konsep inti
```sql
SHOW PARAMETER sga_target;
SHOW PARAMETER memory_target;      -- harus 0 untuk ASMM

ALTER SYSTEM SET memory_target = 0;
ALTER SYSTEM SET sga_target = 4G SCOPE=SPFILE;

SELECT component, current_size/1024/1024 mb, min_size/1024/1024, max_size/1024/1024
  FROM v$sga_dynamic_components;
```

ASMM mengatur buffer cache, shared pool, large pool, java pool secara dinamis. `sga_target > 0` dan `memory_target = 0` = ASMM.

## Jebakan
- `memory_target` dan `sga_target` bersamaan = AMM, bukan ASMM.
- `sga_max_size` hanya bisa dinaikkan dengan restart (kecuali diatur saat startup).
- Komponen dengan `min_size` besar membatasi fleksibilitas.
- ASMM tidak mengelola PGA.

## Latihan
1. Kombinasi parameter untuk ASMM?
2. Apakah ASMM mengatur PGA?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>sga_target &gt; 0</code> dan <code>memory_target = 0</code>.</p>
<p><b>2.</b> Tidak; PGA diatur terpisah (<code>pga_aggregate_target</code>).</p>
</details>
