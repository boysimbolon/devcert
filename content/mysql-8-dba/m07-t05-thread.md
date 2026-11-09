---
title: Peran thread replikasi
minutes: 18
level: Menengah
badge: lengkap
summary: Receiver, coordinator, applier worker, dan pengaruhnya pada lag.
objectives:
  - Menyebutkan thread pada replica dan fungsinya
  - Menjelaskan paralelisme applier
  - Menghubungkan thread dengan lag
---
## Kenapa topik ini diuji
Soal menanyakan thread mana yang bermasalah ketika replikasi berhenti atau tertinggal.

## Konsep inti
| Thread | Fungsi | Terlihat di |
|---|---|---|
| **Receiver (IO)** | mengambil binlog dari source, menulis relay log | `Replica_IO_Running` |
| **Coordinator** | membagi transaksi ke worker | `Replica_SQL_Running` |
| **Applier worker** | menerapkan transaksi paralel | `Replica_parallel_workers` |
| **Dump thread** (source) | mengirim binlog ke replica | `SHOW PROCESSLIST` di source |

```sql
SHOW VARIABLES LIKE 'replica_parallel_workers';       -- 0 = single-threaded
SET PERSIST replica_parallel_type = 'LOGICAL_CLOCK';
SET PERSIST replica_preserve_commit_order = ON;
```

IO thread mati → masalah jaringan/kredensial/TLS. SQL/applier error → konflik data, constraint, atau event tidak cocok.

## Jebakan
- `Replica_IO_Running: Connecting` berarti belum berhasil menyambung, bukan sedang bekerja.
- Worker paralel menaikkan throughput tetapi bisa mengubah urutan commit bila `preserve_commit_order=OFF`.
- Thread dump di source menahan binlog selama replica belum membacanya.
- `Seconds_Behind_Source` bisa `NULL` saat IO thread mati — bukan berarti lag 0.

## Latihan
1. Thread mana yang bertanggung jawab mengambil binlog?
2. Apa efek `replica_preserve_commit_order`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Receiver (IO) thread pada replica.</p>
<p><b>2.</b> Menjaga urutan commit sama dengan source saat memakai worker paralel.</p>
</details>
