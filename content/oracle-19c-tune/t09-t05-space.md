---
title: Diagnosis dan tuning masalah ruang
minutes: 20
level: Menengah
badge: lengkap
summary: Tablespace penuh, undo besar, TEMP penuh, dan fragmentasi.
objectives:
  - Mendeteksi penyebab ruang habis
  - Menangani tablespace penuh
  - Mengelola undo dan temp
---
## Kenapa topik ini diuji
Soal menanyakan langkah pertama saat mendapat ORA-01652/01653.

## Konsep inti
```sql
SELECT tablespace_name, bytes/1024/1024 mb, autoextensible, maxbytes/1024/1024 max_mb
  FROM dba_data_files ORDER BY mb DESC;

SELECT tablespace_name, SUM(bytes)/1024/1024 used_mb
  FROM dba_segments GROUP BY tablespace_name ORDER BY used_mb DESC;

SELECT * FROM dba_free_space WHERE tablespace_name='USERS';

-- undo
SELECT status, SUM(bytes)/1024/1024 mb FROM dba_undo_extents GROUP BY status;
SELECT * FROM v$undostat ORDER BY begin_time DESC FETCH FIRST 5 ROWS ONLY;

-- temp
SELECT tablespace_name, SUM(bytes_used)/1024/1024 used_mb FROM v$tempseg_usage GROUP BY tablespace_name;
```

Tindakan: tambah datafile atau `RESIZE`, perbesar `undo_retention`, periksa SQL yang memakai sort besar.

## Jebakan
- `autoextensible=YES` tidak membantu bila disk penuh.
- Undo tidak bisa dipangkas selama ada transaksi/read view.
- TEMP penuh biasanya karena sort/hash besar, bukan karena kurang ruang.
- Fragmentasi tablespace jarang menjadi masalah pada locally managed tablespace.

## Latihan
1. View untuk pemakaian temp?
2. Mengapa menambah file tidak menyelesaikan ORA-01652 di TEMP?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>V$TEMPSEG_USAGE</code> dan <code>DBA_TEMP_FILES</code>.</p>
<p><b>2.</b> Karena ORA-01652 pada TEMP berarti temporary tablespace habis; perlu perbesar tempfile atau perbaiki query yang butuh sort besar.</p>
</details>
