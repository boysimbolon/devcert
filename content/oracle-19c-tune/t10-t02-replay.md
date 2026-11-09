---
title: Database Replay
minutes: 20
level: Menengah
badge: lengkap
summary: Merekam beban produksi dan memutarnya ulang di lingkungan uji.
objectives:
  - Menjelaskan empat fase Database Replay
  - Menangkap beban kerja
  - Membandingkan hasil replay
---
## Kenapa topik ini diuji
Soal menanyakan fase-fase dan kapan Replay lebih tepat dari SPA.

## Konsep inti
Empat fase:

```text
1. Capture   : rekam beban di produksi (workload capture)
2. Preprocess: ubah capture jadi replay files
3. Replay    : jalankan di sistem uji
4. Analysis  : bandingkan (AWR, error, divergensi)
```

```sql
EXEC DBMS_WORKLOAD_CAPTURE.START_CAPTURE(name => 'cap_uji', dir => 'REPLAY_DIR');
EXEC DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE;
EXEC DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE('REPLAY_DIR');
```

Perbedaan dengan SPA: Replay menguji **seluruh beban** (termasuk konkurensi dan transaksi), SPA hanya kumpulan SQL.

## Jebakan
- Capture menambah overhead; jangan terlalu lama.
- Lingkungan uji harus setara (CPU, I/O, data) agar hasil bermakna.
- Replay tidak merekam data yang diubah di luar capture (mis. job eksternal).
- Butuh izin dan ruang untuk menyimpan capture.

## Latihan
1. Empat fase Database Replay?
2. Kapan memilih Replay daripada SPA?

<details><summary>Jawaban</summary>
<p><b>1.</b> Capture, preprocess, replay, analysis.</p>
<p><b>2.</b> Saat ingin menguji perubahan pada seluruh beban termasuk konkurensi, bukan hanya kumpulan SQL.</p>
</details>
