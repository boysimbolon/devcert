---
title: Tuning shared pool
minutes: 20
level: Menengah
badge: lengkap
summary: Hard parse, kontensi latch, dan ukuran shared pool yang tepat.
objectives:
  - Mendiagnosis masalah shared pool
  - Menentukan ukuran yang memadai
  - Mengurangi fragmentasi
---
## Kenapa topik ini diuji
Soal menanyakan gejala shared pool kurang: hard parse tinggi dan latch contention.

## Konsep inti
```sql
SELECT component, current_size/1024/1024 mb FROM v$sga_dynamic_components;
SELECT pool, name, bytes/1024/1024 mb FROM v$sgastat WHERE pool='shared pool'
 ORDER BY bytes DESC FETCH FIRST 10 ROWS ONLY;

SELECT name, value FROM v$sysstat WHERE name IN
  ('parse count (hard)','parse count (total)','execute count');

SELECT * FROM v$sgastat WHERE name LIKE '%free memory%';
```

Gejala: `ORA-04031 cannot allocate memory`, hard parse tinggi, `library cache lock`.

```sql
ALTER SYSTEM SET shared_pool_size = 1G SCOPE=BOTH;   -- bila SGA manual
```

## Jebakan
- Memperbesar shared pool tanpa memperbaiki bind variable hanya menunda masalah.
- Terlalu besar mengurangi ruang buffer cache (di AMM/ASMM dibagi otomatis).
- `CURSOR_SHARING=FORCE` mengurangi parse tetapi bisa mengubah plan.
- Pin objek sering dipakai bisa membantu, tetapi berisiko.

## Latihan
1. Error khas shared pool kurang?
2. Penyebab hard parse paling umum?

<details><summary>Jawaban</summary>
<p><b>1.</b> ORA-04031.</p>
<p><b>2.</b> SQL dengan literal berbeda (tanpa bind variable) dan DDL yang menginvalidasi cursor.</p>
</details>
