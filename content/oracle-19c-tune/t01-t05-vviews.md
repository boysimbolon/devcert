---
title: Diagnosis dengan V$ views
minutes: 22
level: Menengah
badge: lengkap
summary: View dinamis untuk sesi, SQL, I/O, dan segment statistics.
objectives:
  - Memilih V$ view sesuai pertanyaan
  - Menggabungkan V$SESSION dengan V$SQL
  - Menemukan SQL paling mahal
---
## Kenapa topik ini diuji
Soal menanyakan view mana yang memuat informasi tertentu.

## Konsep inti
| View | Isi |
|---|---|
| `V$SESSION` | sesi aktif, event, blocking |
| `V$SQL` | SQL di shared pool + statistik eksekusi |
| `V$SQLAREA` | agregat per teks SQL |
| `V$SQLSTATS` | statistik SQL yang lebih ringkas |
| `V$SYSSTAT` | statistik sistem |
| `V$SEGMENT_STATISTICS` | aktivitas per segmen |
| `V$FILESTAT` | I/O per file |
| `V$LOCK` / `V$LOCKED_OBJECT` | lock |
| `V$ACTIVE_SESSION_HISTORY` | sampel sesi aktif |

```sql
SELECT s.sid, s.username, s.event, q.sql_id, q.elapsed_time/1e6 detik
  FROM v$session s LEFT JOIN v$sql q ON q.sql_id = s.sql_id
 WHERE s.status = 'ACTIVE' AND s.type = 'USER';

SELECT sql_id, executions, elapsed_time/1e6 detik,
       elapsed_time/GREATEST(executions,1)/1e6 detik_per_exec
  FROM v$sql ORDER BY elapsed_time DESC FETCH FIRST 10 ROWS ONLY;
```

## Jebakan
- `V$SQL` hanya memuat SQL yang masih di shared pool (bisa terbuang).
- `V$SQLAREA` menggabungkan semua child cursor.
- Statistik kumulatif; bandingkan antar waktu atau gunakan AWR.
- Perlu privilege `SELECT_CATALOG_ROLE`/`V$` yang sesuai.

## Latihan
1. View untuk SQL paling banyak menghabiskan waktu?
2. Mengapa V$SQL bisa "kehilangan" query?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>V$SQL</code> diurutkan <code>elapsed_time</code> (atau <code>V$SQLSTATS</code>).</p>
<p><b>2.</b> Karena cursor bisa terbuang dari shared pool saat ada pressure/aging.</p>
</details>
