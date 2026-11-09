---
title: Menganalisis query dengan performance_schema dan slow log
minutes: 22
level: Menengah
badge: lengkap
summary: Menemukan query paling mahal, memakai sys schema, dan membandingkan sebelum-sesudah.
objectives:
  - Menemukan query teratas berdasarkan latensi
  - Membedakan biaya total dan biaya per eksekusi
  - Memverifikasi perbaikan dengan metrik
---
## Kenapa topik ini diuji
Soal optimasi selalu dimulai dengan "query mana yang harus diperbaiki" — bukan "bagaimana menulis index".

## Konsep inti
```sql
-- ringkasan per pola query (sys schema)
SELECT query, exec_count, total_latency, avg_latency, rows_examined_avg, full_scan
  FROM sys.statement_analysis
 ORDER BY total_latency DESC LIMIT 10;

-- query yang melakukan full scan
SELECT * FROM sys.statements_with_full_table_scans LIMIT 10;

-- query dengan temporary table / filesort
SELECT * FROM sys.statements_with_temp_tables LIMIT 10;
SELECT * FROM sys.statements_with_sorting LIMIT 10;

-- tabel yang paling banyak diakses
SELECT * FROM sys.schema_table_statistics ORDER BY total_latency DESC LIMIT 10;
```

Slow log untuk analisis historis:

```bash
mysqldumpslow -s t -t 20 /var/log/mysql/slow.log
```

Cara memilih target: urutkan berdasarkan **total_latency** (dampak keseluruhan), lalu periksa **avg_latency** (mahal per eksekusi) dan **exec_count** (frekuensi). Query 5 ms yang dieksekusi sejuta kali lebih penting daripada query 30 detik yang jarang.

## Jebakan
- Mengoptimasi query dengan `avg_latency` tinggi tetapi eksekusi hanya sekali sebulan.
- Melihat `total_latency` tanpa menormalkan terhadap waktu pengamatan.
- Mengabaikan `rows_examined_avg` — sering menunjukkan index yang tidak selektif.
- `performance_schema` harus aktif (`performance_schema=ON`) dan konsumen statement diaktifkan.

## Latihan
1. Metrik mana yang dipakai memilih query prioritas?
2. Mengapa `rows_examined_avg` penting?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>total_latency</code> untuk dampak keseluruhan, dibandingkan dengan <code>exec_count</code>.</p>
<p><b>2.</b> Karena banyaknya baris diperiksa menunjukkan index tidak selektif atau tidak dipakai.</p>
</details>
