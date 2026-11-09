---
title: Automatic Memory Management
minutes: 18
level: Menengah
badge: lengkap
summary: Satu parameter untuk SGA dan PGA, plus konsekuensinya.
objectives:
  - Mengaktifkan AMM
  - Menjelaskan kelebihan dan batasannya
  - Menghindari konflik dengan parameter lain
---
## Kenapa topik ini diuji
AMM mengubah cara memori dikelola; soal menanyakan syarat dan efeknya.

## Konsep inti
```sql
SHOW PARAMETER memory_target;
SHOW PARAMETER memory_max_target;

ALTER SYSTEM SET memory_target = 8G SCOPE=SPFILE;
-- restart diperlukan

SELECT * FROM v$memory_dynamic_components;
SELECT * FROM v$memory_target_advice;
```

Dengan AMM: `memory_target > 0`, `sga_target = 0`, `pga_aggregate_target = 0`.

## Jebakan
- AMM butuh `/dev/shm` cukup pada Linux dan memakai satu segmen memori.
- Beberapa fitur tidak kompatibel dengan AMM (mis. `USE_LARGE_PAGES` tertentu, HugePages).
- `memory_max_target` tidak bisa dinaikkan tanpa restart.
- AMM tidak selalu memberi hasil terbaik untuk beban sangat spesifik.

## Latihan
1. Parameter utama AMM?
2. Syarat parameter lain saat AMM aktif?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>memory_target</code> (batas <code>memory_max_target</code>).</p>
<p><b>2.</b> <code>sga_target=0</code> dan <code>pga_aggregate_target=0</code>.</p>
</details>
