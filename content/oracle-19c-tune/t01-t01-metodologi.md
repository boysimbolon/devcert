---
title: Metodologi tuning
minutes: 20
level: Menengah
badge: lengkap
summary: Pendekatan sistematis: ukur, identifikasi, perbaiki, verifikasi — bukan menebak parameter.
objectives:
  - Menjelaskan metodologi tuning berbasis bukti
  - Mengurutkan langkah diagnosis
  - Menghindari tuning berdasarkan mitos
---
## Kenapa topik ini diuji
Soal metodologi menguji urutan: apa yang diukur dulu, dan kapan parameter diubah.

## Konsep inti
Alur yang dipakai Oracle:

```text
1. Tentukan tujuan bisnis & metrik (response time, throughput)
2. Ukur kondisi aktual (AWR, ASH, wait events)
3. Identifikasi bottleneck dominan (bukan yang paling mudah diperbaiki)
4. Perbaiki penyebab, bukan gejala
5. Verifikasi dengan pengukuran ulang
```

Prinsip penting: **tuning adalah mengurangi waktu tunggu**, bukan menaikkan angka cache. Bila 80% waktu habis di satu wait event, optimasi lain hampir tak terasa.

```sql
SELECT event, total_waits, time_waited_micro/1e6 AS detik
  FROM v$system_event
 WHERE wait_class <> 'Idle'
 ORDER BY time_waited_micro DESC FETCH FIRST 10 ROWS ONLY;
```

## Jebakan
- Mengubah banyak parameter sekaligus → tidak tahu mana yang berpengaruh.
- Tuning berdasarkan mitos ("buffer cache harus 80% RAM").
- Mengoptimasi query yang jarang dijalankan karena "kelihatannya lambat".
- Tidak punya baseline, jadi tidak bisa membuktikan perbaikan.

## Latihan
1. Apa fokus sebenarnya dari tuning?
2. Mengapa mengubah banyak parameter sekaligus buruk?

<details><summary>Jawaban</summary>
<p><b>1.</b> Mengurangi waktu tunggu (wait time) pada bottleneck dominan.</p>
<p><b>2.</b> Karena efeknya tidak bisa dipisahkan; perbaikan/regresi tidak terukur.</p>
</details>
