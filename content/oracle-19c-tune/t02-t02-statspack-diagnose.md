---
title: Diagnosis dengan Statspack
minutes: 18
level: Menengah
badge: lengkap
summary: Membaca laporan Statspack: top wait, top SQL, dan rasio yang berguna.
objectives:
  - Membaca bagian utama laporan Statspack
  - Menemukan SQL paling mahal
  - Menghindari rasio yang menyesatkan
---
## Kenapa topik ini diuji
Soal menyodorkan potongan laporan dan menanyakan kesimpulan yang sah.

## Konsep inti
Bagian penting laporan:

```text
Top 5 Timed Events   -> bottleneck utama
Load Profile         -> beban (redo size, logical reads, parses)
Instance Efficiency -> hit ratio (gunakan hati-hati)
Top SQL by elapsed   -> SQL yang harus diperbaiki
Instance Activity    -> statistik pendukung
```

```sql
-- setara dengan bagian Top SQL
SELECT sql_text, executions, elapsed_time/1e6
  FROM stats$sql_summary
 WHERE snap_id BETWEEN 10 AND 11
 ORDER BY elapsed_time_delta DESC FETCH FIRST 10 ROWS ONLY;
```

## Jebakan
- Hit ratio tinggi bisa menyesatkan (bisa tinggi karena query buruk membaca ulang).
- Membandingkan snapshot dengan beban berbeda menghasilkan kesimpulan salah.
- Top SQL berdasarkan elapsed_time berbeda dari berdasarkan CPU.
- Laporan mencakup seluruh instance; RAC butuh per-instance.

## Latihan
1. Bagian mana yang menunjukkan bottleneck utama?
2. Mengapa buffer hit ratio berbahaya sebagai target?

<details><summary>Jawaban</summary>
<p><b>1.</b> Top 5 Timed Events (atau Top 10 di AWR).</p>
<p><b>2.</b> Karena rasio bisa naik karena query membaca blok yang sama berulang, bukan karena efisien.</p>
</details>
