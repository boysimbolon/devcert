---
title: Mambaca execution plan
minutes: 20
level: Menengah
badge: lengkap
summary: DBMS_XPLAN, operasi plan, cardinality, dan cost.
objectives:
  - Menampilkan plan yang benar-benar dipakai
  - Membaca operasi dan cardinality
  - Mengenali operasi mahal
---
## Kenapa topik ini diuji
Soal menyodorkan plan dan menanyakan kenapa query lambat.

## Konsep inti
```sql
EXPLAIN PLAN FOR SELECT * FROM employees WHERE department_id = 50;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY());

-- plan yang benar-benar dipakai
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR('&sql_id', NULL, 'ALLSTATS LAST'));
```

Kolom: `Id`, `Operation`, `Name` (objek), `Rows` (cardinality), `Bytes`, `Cost`, `Time`.

Operasi penting: `TABLE ACCESS FULL`, `INDEX RANGE SCAN`, `INDEX UNIQUE SCAN`, `NESTED LOOPS`, `HASH JOIN`, `MERGE JOIN`, `SORT ORDER BY`, `TABLE ACCESS BY INDEX ROWID`.

## Jebakan
- `EXPLAIN PLAN` bisa berbeda dari plan aktual (peek, bind, adaptive).
- Cardinality jauh meleset menandakan statistik usang.
- `TABLE ACCESS FULL` bukan selalu buruk untuk tabel kecil atau selektivitas rendah.
- Plan dari `DISPLAY` tidak memuat statistik runtime; gunakan `DISPLAY_CURSOR ... ALLSTATS LAST`.

## Latihan
1. Cara melihat plan aktual dengan statistik runtime?
2. Apa arti cardinality yang terlalu kecil dari kenyataan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBMS_XPLAN.DISPLAY_CURSOR(sql_id, NULL, 'ALLSTATS LAST')</code>.</p>
<p><b>2.</b> Statistik tidak akurat sehingga optimizer memilih join/akses yang salah.</p>
</details>
