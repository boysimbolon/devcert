---
title: Wait events
minutes: 22
level: Menengah
badge: lengkap
summary: Kelas wait, event umum, dan cara membaca siapa menunggu apa.
objectives:
  - Menyebutkan kelas wait utama
  - Mengenali event yang sering menjadi biang masalah
  - Membedakan idle dan non-idle
---
## Kenapa topik ini diuji
Soal memberi daftar wait event dan menanyakan penyebab atau tindakannya.

## Konsep inti
```sql
SELECT wait_class, COUNT(*) FROM v$event_name GROUP BY wait_class;
SELECT event, total_waits, time_waited_micro/1e6 detik, average_wait
  FROM v$system_event WHERE wait_class <> 'Idle'
 ORDER BY time_waited_micro DESC FETCH FIRST 15 ROWS ONLY;
SELECT sid, event, wait_class, seconds_in_wait, blocking_session
  FROM v$session WHERE wait_class <> 'Idle';
```

| Event | Arti | Arah perbaikan |
|---|---|---|
| `db file sequential read` | baca satu blok (index) | index/statistik, I/O |
| `db file scattered read` | baca multi-blok (full scan) | index, partisi, compression |
| `log file sync` | commit menunggu log ditulis | I/O redo, commit batch |
| `enq: TX - row lock contention` | rebutan baris | transaksi pendek, urutan akses |
| `library cache lock/pin` | kontensi shared pool | bind variable, cursor sharing |
| `latch: shared pool` | kontensi struktur memori | shared pool tuning |

## Jebakan
- Event `Idle` (mis. `SQL*Net message from client`) bukan masalah.
- `db file sequential read` bukan selalu buruk; banyaknya yang jadi masalah.
- Menyimpulkan dari satu sesi tanpa melihat total sistem.
- Wait event adalah gejala; akar masalah ada di SQL/desain.

## Latihan
1. Event untuk commit yang menunggu redo?
2. Bagaimana menemukan sesi yang memblokir?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>log file sync</code>.</p>
<p><b>2.</b> Kolom <code>blocking_session</code> di <code>v$session</code>.</p>
</details>
