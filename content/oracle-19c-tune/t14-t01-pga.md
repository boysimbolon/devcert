---
title: Tuning PGA
minutes: 20
level: Menengah
badge: lengkap
summary: Sort, hash join, dan penggunaan memori per proses.
objectives:
  - Menilai kebutuhan PGA
  - Menemukan operasi yang memakai banyak PGA
  - Menyesuaikan pga_aggregate_target
---
## Kenapa topik ini diuji
Soal menanyakan gejala PGA kurang: sort/hash ke disk dan ORA-04030.

## Konsep inti
```sql
SHOW PARAMETER pga_aggregate_target;
SHOW PARAMETER workarea_size_policy;   -- AUTO | MANUAL

SELECT name, value FROM v$pgastat;
SELECT * FROM v$pga_target_advice;
SELECT sid, operation_type, policy, estimated_optimal_size/1024/1024 mb
  FROM v$sql_workarea_active ORDER BY mb DESC;

SELECT event, COUNT(*) FROM v$active_session_history
 WHERE event LIKE '%direct path%' OR event LIKE '%temp%' GROUP BY event;
```

Gejala: `Workarea executions - onepass/multipass` tinggi, `direct path write temp` besar.

## Jebakan
- `pga_aggregate_target` terlalu besar bisa mengurangi SGA (di AMM).
- Sort kecil tidak perlu diperbesar; fokus pada multipass.
- `workarea_size_policy=MANUAL` membuat `sort_area_size` per sesi — berisiko.
- ORA-04030 bisa berarti batas OS (ulimit), bukan parameter DB.

## Latihan
1. Statistik yang menandakan PGA kurang?
2. Apa risiko `MANUAL` workarea?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Workarea executions - multipass</code> dan aktivitas temp yang tinggi.</p>
<p><b>2.</b> Memori dialokasikan per sesi tanpa kendali agregat, mudah kehabisan.</p>
</details>
