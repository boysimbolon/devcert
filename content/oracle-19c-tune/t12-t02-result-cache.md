---
title: Result cache
minutes: 18
level: Menengah
badge: lengkap
summary: Cache hasil query dan fungsi, plus pengelolaannya.
objectives:
  - Mengaktifkan result cache
  - Memakai hint dan fungsi cache
  - Menghindari cache yang basi
---
## Kenapa topik ini diuji
Result cache memberi keuntungan besar untuk query berulang; soal menanyakan kapan cocok.

## Konsep inti
```sql
SHOW PARAMETER result_cache_mode;         -- MANUAL | FORCE
ALTER SYSTEM SET result_cache_mode = MANUAL;

SELECT /*+ result_cache */ department_id, COUNT(*)
  FROM employees GROUP BY department_id;

-- cache hasil fungsi
CREATE OR REPLACE FUNCTION f_harga(p_id NUMBER) RETURN NUMBER
  RESULT_CACHE RELIES_ON (produk) IS ...

EXEC DBMS_RESULT_CACHE.FLUSH;
SELECT * FROM v$result_cache_statistics;
```

## Jebakan
- Tabel yang berubah menginvalidasi cache terkait.
- `FORCE` bisa memboroskan memori untuk query yang jarang diulang.
- Result cache memakai memori dari shared pool (bisa menekan komponen lain).
- Query dengan `SYSDATE`/nilai tidak deterministik tidak cocok.

## Latihan
1. Hint untuk memakai result cache?
2. Kapan result cache tidak berguna?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>/*+ result_cache */</code>.</p>
<p><b>2.</b> Saat query jarang diulang atau datanya sering berubah (cache cepat invalid).</p>
</details>
