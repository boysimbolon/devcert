---
title: Masalah temporary tablespace
minutes: 20
level: Menengah
badge: lengkap
summary: ORA-01652, sort besar, dan pemakaian temp per sesi.
objectives:
  - Mendeteksi sesi yang memakai temp besar
  - Menambah tempfile dengan benar
  - Mengurangi kebutuhan sort
---
## Kenapa topik ini diuji
Soal menanyakan langkah penanganan ORA-01652 pada operasi sort.

## Konsep inti
```sql
SELECT tablespace_name, SUM(bytes)/1024/1024 mb FROM dba_temp_files GROUP BY tablespace_name;
SELECT username, sid, serial#, tablespace, segtype, SUM(bytes_used)/1024/1024 mb
  FROM v$tempseg_usage GROUP BY username, sid, serial#, tablespace, segtype;

ALTER TABLESPACE temp ADD TEMPFILE '/u01/oradata/temp02.dbf' SIZE 2G AUTOEXTEND ON NEXT 256M;
```

Penyebab umum: `ORDER BY`/`GROUP BY` besar, hash join tanpa memori cukup, indeks yang hilang.

## Jebakan
- Temp penuh sementara bukan berarti tablespace permanen kurang.
- `AUTOEXTEND` tanpa batas bisa memenuhi disk.
- Menambah tempfile tidak memperbaiki query yang boros.
- Sesi yang "menggantung" bisa menahan temp setelah query selesai.

## Latihan
1. View pemakaian temp per sesi?
2. Dua penyebab umum temp penuh?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>V$TEMPSEG_USAGE</code>.</p>
<p><b>2.</b> Sort/hash besar yang tumpah ke disk, dan kurangnya index sehingga query memindai/mengurutkan banyak baris.</p>
</details>
