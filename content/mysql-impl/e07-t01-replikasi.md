---
title: Replikasi MySQL
minutes: 22
level: Menengah
badge: lengkap
summary: Alur binlog, thread replikasi, GTID, dan replikasi semi-sinkron.
objectives:
  - Menjelaskan alur replikasi asinkron
  - Menyebutkan thread yang terlibat
  - Membedakan asinkron dan semi-sinkron
---
## Kenapa topik ini diuji
Soal konsep + perintah: siapa mengirim, siapa menerapkan, dan apa yang dijamin.

## Konsep inti
```text
Source: commit -> binlog -> dump thread
Replica: receiver thread -> relay log -> applier thread -> data
```

```sql
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='10.0.0.10', SOURCE_USER='repl', SOURCE_PASSWORD='***',
  SOURCE_AUTO_POSITION=1, SOURCE_SSL=1;
START REPLICA;
SHOW REPLICA STATUS\G
```

Mode sinkronisasi:

| Mode | Jaminan |
|---|---|
| Asinkron | source tidak menunggu replica; bisa kehilangan transaksi |
| Semi-sinkron | source menunggu minimal satu replica menerima (masuk relay log) |
| Sinkron (Group Replication) | mayoritas anggota menyetujui |

## Jebakan
- Semi-sinkron hanya menjamin **diterima**, belum tentu diterapkan.
- `server_id` sama → replikasi kacau.
- Replikasi bukan backup: kesalahan ikut tereplikasi.
- GTID harus aktif di kedua sisi untuk `SOURCE_AUTO_POSITION=1`.

## Latihan
1. Thread mana yang menulis relay log?
2. Apa batas jaminan semi-sinkron?

<details><summary>Jawaban</summary>
<p><b>1.</b> Receiver (IO) thread pada replica.</p>
<p><b>2.</b> Hanya menjamin transaksi diterima replica, bukan sudah diterapkan.</p>
</details>
