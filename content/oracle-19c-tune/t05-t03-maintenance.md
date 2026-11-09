---
title: Automated Maintenance Tasks
minutes: 18
level: Menengah
badge: lengkap
summary: Maintenance window otomatis: statistik, segment advisor, SQL tuning.
objectives:
  - Menyebutkan tiga task otomatis
  - Melihat riwayat eksekusi
  - Mengatur window maintenance
---
## Kenapa topik ini diuji
Soal menanyakan task apa yang berjalan otomatis dan kapan.

## Konsep inti
Task otomatis: **Automatic Optimizer Statistics Gathering**, **Automatic Segment Advisor**, **Automatic SQL Tuning Advisor**.

```sql
SELECT client_name, status FROM dba_autotask_client;
SELECT task_name, status FROM dba_autotask_task;
SELECT client_name, window_name, start_time, duration
  FROM dba_autotask_schedule ORDER BY start_time DESC FETCH FIRST 5 ROWS ONLY;

SELECT window_name, repeat_interval, duration FROM dba_scheduler_windows;
```

Window default: `MONDAY_WINDOW` … `SUNDAY_WINDOW`, berjalan malam hari.

## Jebakan
- Task berjalan hanya jika `STATISTICS_LEVEL` = `TYPICAL` atau `ALL`.
- Automatic SQL Tuning Advisor hanya *menyarankan*, tidak menerapkan otomatis.
- Window bisa dinonaktifkan, sehingga statistik tidak diperbarui.
- Segment Advisor hanya menandai kandidat, bukan mengecilkan segmen.

## Latihan
1. Tiga client autotask?
2. Apakah rekomendasi SQL Tuning otomatis diterapkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> auto optimizer stats collection, auto segment advisor, auto SQL tuning advisor.</p>
<p><b>2.</b> Tidak; hanya rekomendasi (kecuali fitur khusus di versi tertentu).</p>
</details>
