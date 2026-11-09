---
title: Mengelola statistik optimizer
minutes: 20
level: Menengah
badge: lengkap
summary: DBMS_STATS, preferensi, retensi, dan pengumpulan bertahap.
objectives:
  - Mengumpulkan statistik dengan DBMS_STATS
  - Mengatur preferensi global
  - Menjaga riwayat statistik
---
## Kenapa topik ini diuji
Statistik adalah input optimizer; soal menanyakan cara dan jadwal pengumpulannya.

## Konsep inti
```sql
EXEC DBMS_STATS.GATHER_DATABASE_STATS(degree => 4);
EXEC DBMS_STATS.GATHER_SCHEMA_STATS('APP', cascade => TRUE);
EXEC DBMS_STATS.GATHER_TABLE_STATS('APP','PESANAN', partname => 'P2026_01');

-- preferensi
EXEC DBMS_STATS.SET_GLOBAL_PREFS('STALE_PERCENT','5');
SELECT * FROM dba_tab_stat_prefs;

-- riwayat
SELECT * FROM dba_tab_stats_history WHERE table_name='PESANAN';
EXEC DBMS_STATS.RESTORE_TABLE_STATS('APP','PESANAN', SYSTIMESTAMP-1);
```

## Jebakan
- `STALE_PERCENT` terlalu kecil → pengumpulan terlalu sering.
- Mengumpulkan statistik saat beban puncak dapat mengganggu.
- Statistik pada tabel partisi bisa per partisi atau global.
- `RESTORE_TABLE_STATS` hanya berguna bila retensi aktif.

## Latihan
1. Paket untuk mengumpulkan statistik?
2. Bagaimana mengembalikan statistik lama?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>DBMS_STATS</code>.</p>
<p><b>2.</b> <code>DBMS_STATS.RESTORE_TABLE_STATS</code> selama riwayat masih tersimpan.</p>
</details>
