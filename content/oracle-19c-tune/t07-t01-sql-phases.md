---
title: Fase pemrosesan pernyataan SQL
minutes: 20
level: Menengah
badge: lengkap
summary: Parse (soft/hard), execute, fetch, dan biaya tiap fase.
objectives:
  - Menyebutkan fase eksekusi SQL
  - Membedakan soft parse dan hard parse
  - Menjelaskan dampak bind variable
---
## Kenapa topik ini diuji
Hard parse berlebih adalah penyebab klasik "database lambat tanpa alasan jelas".

## Konsep inti
```text
1. Parse   : syntax check, semantic check, optimasi, plan generation
2. Execute : menjalankan plan (DML/DDL)
3. Fetch   : mengambil baris untuk SELECT
```

- **Soft parse**: plan sudah ada di shared pool (cache hit) → murah.
- **Hard parse**: harus mem-parse, mengoptimasi, mengalokasikan memori → mahal dan menambah latch.
- Penyebab hard parse: literal berbeda di setiap eksekusi (tidak memakai bind variable), perubahan skema, atau shared pool terlalu kecil.

```sql
SELECT name, value FROM v$sysstat
 WHERE name IN ('parse count (total)','parse count (hard)','execute count');
SELECT sql_id, COUNT(*) FROM v$sql GROUP BY sql_id HAVING COUNT(*) > 5;
```

## Jebakan
- Literal SQL menghasilkan child cursor baru walaupun teks hampir sama.
- `CURSOR_SHARING=FORCE` bisa menurunkan hard parse tetapi berisiko plan buruk.
- DDL memicu invalidasi cursor → hard parse.
- Hard parse bukan hanya masalah CPU, juga latch shared pool.

## Latihan
1. Perbedaan soft dan hard parse?
2. Bagaimana mengurangi hard parse dari aplikasi?

<details><summary>Jawaban</summary>
<p><b>1.</b> Soft memakai plan yang sudah ada; hard harus mem-parse dan mengoptimasi ulang.</p>
<p><b>2.</b> Gunakan bind variable (prepared statement), hindari literal dinamis.</p>
</details>
