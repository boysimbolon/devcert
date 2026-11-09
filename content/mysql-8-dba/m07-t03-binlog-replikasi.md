---
title: Peran binary log dalam replikasi
minutes: 18
level: Menengah
badge: lengkap
summary: Format binlog, event, dan pengaruhnya pada konsistensi replica.
objectives:
  - Membedakan ROW, STATEMENT, dan MIXED
  - Menjelaskan mengapa ROW lebih aman
  - Membaca event binlog
---
## Kenapa topik ini diuji
Soal format binlog sering muncul karena dampaknya pada konsistensi dan ukuran log.

## Konsep inti
| Format | Isi | Kapan dipakai |
|---|---|---|
| `STATEMENT` | teks SQL | hemat, tapi rawan non-deterministik |
| `ROW` | perubahan baris sebelum/sesudah | aman, default 8.0 |
| `MIXED` | otomatis memilih | kompromi |

Query non-deterministik (`NOW()`, `UUID()`, `RAND()`, `LIMIT` tanpa ORDER BY) berbahaya pada `STATEMENT` karena dieksekusi ulang di replica dengan hasil berbeda.

```sql
SHOW VARIABLES LIKE 'binlog_format';
SHOW BINARY LOGS;
SHOW BINLOG EVENTS IN 'binlog.000042' LIMIT 10;
```

Membaca dalam bentuk terbaca:

```bash
mysqlbinlog --base64-output=DECODE-ROWS -v binlog.000042 | head -60
```

## Jebakan
- Mengubah `binlog_format` pada sesi berjalan tidak berlaku untuk semua koneksi.
- `ROW` menghasilkan binlog jauh lebih besar pada UPDATE massal.
- Tanpa PK, `ROW` mencatat seluruh baris → log membengkak.
- `log_replica_updates=OFF` pada replica yang menjadi source berikutnya membuat rantai putus.

## Latihan
1. Format binlog mana yang paling aman untuk replikasi?
2. Mengapa tabel tanpa primary key memperbesar binlog ROW?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ROW</code> (default 8.0).</p>
<p><b>2.</b> Karena perubahan dicatat per baris lengkap, tanpa kunci untuk mengidentifikasi baris secara ringkas.</p>
</details>
