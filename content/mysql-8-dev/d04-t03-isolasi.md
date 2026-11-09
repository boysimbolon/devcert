---
title: Tingkat isolasi dan masalah konsistensi
minutes: 22
level: Menengah
badge: lengkap
summary: Empat level isolasi, fenomena yang dicegah, dan gap lock pada REPEATABLE READ.
objectives:
  - Memetakan level isolasi ke fenomena yang dicegah
  - Menjelaskan gap lock di REPEATABLE READ
  - Memilih level sesuai kebutuhan
---
## Kenapa topik ini diuji
Tabel isolasi vs fenomena adalah soal favorit, termasuk satu pengecualian khas MySQL.

## Konsep inti
| Level | Dirty read | Non-repeatable read | Phantom |
|---|---|---|---|
| READ UNCOMMITTED | bisa | bisa | bisa |
| READ COMMITTED | tidak | bisa | bisa |
| REPEATABLE READ (default) | tidak | tidak | **tidak** (via gap lock) |
| SERIALIZABLE | tidak | tidak | tidak |

MySQL berbeda dari standar SQL: pada REPEATABLE READ, `SELECT ... FOR UPDATE` mengunci **gap** sehingga phantom read dicegah.

```sql
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT @@transaction_isolation;

-- snapshot konsisten
START TRANSACTION WITH CONSISTENT SNAPSHOT;
```

READ COMMITTED sering dipilih untuk mengurangi lock pada aplikasi dengan banyak update; REPEATABLE READ aman untuk laporan dalam satu transaksi.

## Jebakan
- Menganggap READ COMMITTED dan REPEATABLE READ sama untuk SELECT biasa.
- Gap lock bisa memblokir INSERT di rentang yang tampak tidak terkait.
- `innodb_lock_wait_timeout` vs deadlock: yang pertama timeout, kedua rollback otomatis.
- Mengubah level isolasi global memengaruhi semua sesi baru, bukan yang berjalan.

## Latihan
1. Pada level apa phantom read dicegah oleh MySQL dan dengan mekanisme apa?
2. Level mana yang paling ketat?

<details><summary>Jawaban</summary>
<p><b>1.</b> REPEATABLE READ, lewat gap locking (bukan hanya snapshot).</p>
<p><b>2.</b> SERIALIZABLE (mengunci pembacaan seperti akses tulis).</p>
</details>
