---
title: SQL Trace dan optimizer trace
minutes: 18
level: Menengah
badge: lengkap
summary: Keluaran terformat untuk menemukan SQL buruk dan alasan pemilihan plan.
objectives:
  - Memakai tkprof untuk ringkasan
  - Mengaktifkan optimizer trace
  - Membaca alasan plan dipilih
---
## Kenapa topik ini diuji
Soal menanyakan alat untuk melihat mengapa optimizer memilih plan tertentu.

## Konsep inti
```sql
-- optimizer trace untuk satu sesi
ALTER SESSION SET events 'trace[SQL_Compiler.*] disk level=2';

-- alternatif klasik
ALTER SESSION SET events '10053 trace name context forever, level 1';
```

```bash
tkprof trace.trc hasil.txt sys=no sort=exeela
```

`10053` mencatat perhitungan biaya, kandidat plan, dan alasan pemilihan. Berguna untuk kasus "kenapa index tidak dipakai".

## Jebakan
- File trace besar; aktifkan hanya untuk satu SQL.
- 10053 menambah overhead signifikan.
- Keluaran sulit dibaca tanpa memahami istilah cost/cardinality.
- Trace tidak memengaruhi plan; hanya merekam prosesnya.

## Latihan
1. Event untuk optimizer trace?
2. Kapan optimizer trace dipakai?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>10053</code> (atau event trace SQL_Compiler di versi baru).</p>
<p><b>2.</b> Saat perlu tahu mengapa optimizer memilih plan tertentu, mis. index tidak dipakai.</p>
</details>
