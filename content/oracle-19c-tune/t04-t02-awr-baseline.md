---
title: AWR baseline
minutes: 20
level: Menengah
badge: lengkap
summary: Menyimpan kondisi acuan untuk pembanding, tetap maupun bergerak.
objectives:
  - Membuat baseline tetap
  - Menjelaskan baseline bergerak (moving window)
  - Membandingkan periode dengan baseline
---
## Kenapa topik ini diuji
Soal menanyakan cara membandingkan performa sekarang dengan kondisi "normal".

## Konsep inti
```sql
-- baseline tetap dari rentang snapshot
EXEC DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE(
  start_snap_id => 100, end_snap_id => 110, baseline_name => 'beban_normal');

SELECT baseline_name, start_snap_id, end_snap_id FROM dba_hist_baseline;
EXEC DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE(baseline_name => 'beban_normal');
```

Baseline bergerak (AWR moving window) otomatis menyimpan jendela waktu bergulir; berguna untuk deteksi regresi tanpa baseline manual.

```sql
EXEC DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE(30);   -- hari
```

## Jebakan
- Baseline hanya berguna bila beban saat pengambilan representatif.
- Snapshot bisa terhapus oleh retensi → baseline tidak lengkap.
- Membandingkan periode dengan beban berbeda menghasilkan kesimpulan salah.
- Baseline tidak otomatis dipakai oleh ADDM kecuali diminta.

## Latihan
1. Fungsi membuat baseline tetap?
2. Apa keuntungan moving window baseline?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE</code>.</p>
<p><b>2.</b> Selalu tersedia pembanding bergulir tanpa harus membuat baseline manual.</p>
</details>
