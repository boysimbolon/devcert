---
title: Memantau dan menangani masalah replikasi
minutes: 22
level: Menengah
badge: lengkap
summary: Membaca status, mengukur lag, dan memperbaiki error yang umum.
objectives:
  - Membaca SHOW REPLICA STATUS dengan benar
  - Mengukur lag secara akurat
  - Menangani error umum tanpa merusak data
---
## Kenapa topik ini diuji
Soal troubleshooting memberi status dan menanyakan langkah berikutnya.

## Konsep inti
```sql
SHOW REPLICA STATUS\G
-- fokus: Replica_IO_Running, Replica_SQL_Running, Last_IO_Error,
--        Last_SQL_Error, Seconds_Behind_Source, Retrieved_Gtid_Set, Executed_Gtid_Set

SHOW PROCESSLIST;                          -- thread sistem replikasi
SELECT * FROM performance_schema.replication_applier_status_by_worker;
```

Mengukur lag dengan benar: `Seconds_Behind_Source` bisa menipu. Gunakan heartbeat table atau timestamp sendiri.

```sql
-- GTID gap: cari transaksi yang hilang
SELECT GTID_SUBTRACT('uuid:1-100', 'uuid:1-95');
```

Error umum dan arah penanganan:

| Error | Penyebab | Tindakan |
|---|---|---|
| 1062 duplicate entry | data tidak sinkron | perbaiki baris, atau `SET GLOBAL sql_replica_skip_counter`/skip GTID |
| 1032 row not found | DELETE/UPDATE pada baris hilang | sinkronkan data, lalu lanjut |
| 1045 access denied | kredensial replikasi salah | `CHANGE REPLICATION SOURCE TO ...` ulang |
| 1236 could not find log | binlog dipangkas | restore dari backup + ulang replikasi |

```sql
-- melewati satu transaksi (dengan sadar risikonya)
SET GTID_NEXT = 'uuid:1234';
BEGIN; COMMIT;
SET GTID_NEXT = 'AUTOMATIC';
START REPLICA;
```

## Jebakan
- Skip error tanpa memperbaiki data → divergensi permanen.
- `sql_replica_skip_counter` tidak berlaku saat GTID aktif.
- Replikasi berhenti tetapi aplikasi tetap menulis ke source → ketertinggalan makin besar.
- Lag `NULL` menandakan thread mati, bukan nol.

## Latihan
1. Arti `Replica_SQL_Running: No`?
2. Cara melewati satu transaksi bermasalah pada GTID?

<details><summary>Jawaban</summary>
<p><b>1.</b> Applier thread berhenti, biasanya karena error saat menerapkan event (lihat <code>Last_SQL_Error</code>).</p>
<p><b>2.</b> Set <code>GTID_NEXT</code> ke GTID transaksi itu, commit kosong, lalu kembali ke <code>AUTOMATIC</code> dan start replica.</p>
</details>
