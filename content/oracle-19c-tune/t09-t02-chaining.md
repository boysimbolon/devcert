---
title: Chaining dan migration baris
minutes: 18
level: Menengah
badge: lengkap
summary: Baris yang tersebar di banyak blok dan dampaknya pada I/O.
objectives:
  - Membedakan chaining dan migration
  - Mendeteksi dengan statistik
  - Mengurangi dengan PCTFREE dan block size
---
## Kenapa topik ini diuji
Soal menanyakan penyebab "table fetch continued row" tinggi.

## Konsep inti
- **Migration**: baris dipindah ke blok lain saat UPDATE memperbesar baris; pointer lama menunjuk ke blok baru.
- **Chaining**: baris terlalu besar untuk satu blok sehingga dipecah (umumnya karena `LONG`/`LOB` atau block size kecil).

```sql
SELECT table_name, chain_cnt FROM user_tables WHERE chain_cnt > 0;
SELECT name, value FROM v$sysstat WHERE name = 'table fetch continued row';
ANALYZE TABLE pesanan COMPUTE STATISTICS;   -- untuk mengisi chain_cnt (versi lama)
```

Solusi: naikkan `PCTFREE`, `MOVE`/rebuild tabel, atau pisahkan kolom besar ke tabel lain.

## Jebakan
- `chain_cnt` tidak terisi otomatis oleh `DBMS_STATS` kecuali diminta.
- Menambah `PCTFREE` mengurangi kapasitas baris per blok.
- Migration tidak hilang dengan `SHRINK` saja; perlu `MOVE`.
- Chaining pada kolom LOB normal, tetapi tetap membebani I/O.

## Latihan
1. Statistik yang menandakan chaining?
2. Cara mengurangi migration?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>table fetch continued row</code> dan <code>chain_cnt</code>.</p>
<p><b>2.</b> Naikkan <code>PCTFREE</code> dan lakukan <code>MOVE</code> pada tabel.</p>
</details>
