---
title: Menjadwalkan operasi database
minutes: 20
level: Menengah
badge: lengkap
summary: Event scheduler, ON SCHEDULE, dan pengelolaan job berkala.
objectives:
  - Mengaktifkan event scheduler
  - Membuat event berkala dan sekali jalan
  - Mengelola event yang berjalan
---
## Kenapa topik ini diuji
Event adalah penjadwal bawaan MySQL; soal menanyakan cara mengaktifkannya dan sintaksnya.

## Konsep inti
```sql
SET GLOBAL event_scheduler = ON;      -- atau di my.cnf: event_scheduler=ON
SHOW PROCESSLIST;                     -- ada thread 'event_scheduler'

CREATE EVENT ev_bersih_log
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP + INTERVAL 1 HOUR
ON COMPLETION PRESERVE
ENABLE
DO
  DELETE FROM audit_log WHERE dibuat < NOW() - INTERVAL 90 DAY;

CREATE EVENT ev_sekali
ON SCHEDULE AT '2026-12-31 23:59:00'
DO INSERT INTO audit_log (tabel, aksi) VALUES ('sistem','tahun_baru');

ALTER EVENT ev_bersih_log DISABLE;
DROP EVENT IF EXISTS ev_sekali;
SELECT EVENT_NAME, STATUS, INTERVAL_VALUE, LAST_EXECUTED FROM information_schema.EVENTS;
```

Hak akses: `EVENT` pada database terkait.

## Jebakan
- `event_scheduler=OFF` membuat event tidak pernah jalan (tidak ada error).
- Event berjalan sebagai `DEFINER`; definer yang dihapus membuat event gagal.
- Event berkala yang tumpang tindih bisa saling menimpa; jaga durasi singkat.
- `ON COMPLETION NOT PRESERVE` (default) menghapus event sekali jalan setelah dieksekusi.

## Latihan
1. Variabel untuk mengaktifkan penjadwal?
2. Apa efek ON COMPLETION PRESERVE?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>event_scheduler</code> (ON/OFF).</p>
<p><b>2.</b> Event tetap disimpan setelah selesai/kedaluwarsa, tidak dihapus otomatis.</p>
</details>
