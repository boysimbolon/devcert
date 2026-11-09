---
title: Trace file untuk memantau performa
minutes: 20
level: Menengah
badge: lengkap
summary: SQL trace, TKPROF, dan event 10046 untuk melihat kerja sebenarnya.
objectives:
  - Mengaktifkan SQL trace untuk sesi
  - Membaca keluaran TKPROF
  - Memakai event 10046 untuk wait detail
---
## Kenapa topik ini diuji
Soal trace menguji langkah: aktifkan, jalankan, matikan, format dengan TKPROF.

## Konsep inti
```sql
ALTER SESSION SET tracefile_identifier = 'uji';
ALTER SESSION SET events '10046 trace name context forever, level 12';
-- jalankan query
ALTER SESSION SET events '10046 trace name context off';

SELECT value FROM v$diag_info WHERE name = 'Diag Trace';
```

```bash
tkprof /path/trace/ORCL_ora_1234_uji.trc output.txt sys=no sort=exeela
```

Kolom TKPROF: `Parse`, `Execute`, `Fetch` dengan `count`, `cpu`, `elapsed`, `disk`, `query`, `current`, `rows`.

## Jebakan
- Trace level 12 menambahkan wait dan bind — paling informatif tetapi besar.
- Lupa mematikan trace → file tumbuh cepat.
- `tkprof` tanpa `sort` menyulitkan pencarian query mahal.
- Trace hanya sesi itu; tracing seluruh sistem butuh AWR/ASH.

## Latihan
1. Event apa untuk SQL trace level bind+wait?
2. Alat untuk memformat trace jadi ringkasan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>10046</code> level 12.</p>
<p><b>2.</b> <code>tkprof</code>.</p>
</details>
