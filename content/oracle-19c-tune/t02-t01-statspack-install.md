---
title: Memasang dan mengonfigurasi Statspack
minutes: 18
level: Menengah
badge: lengkap
summary: Snapshot performa klasik, instalasi script, dan pengaturan interval.
objectives:
  - Memasang Statspack
  - Mengambil snapshot manual dan otomatis
  - Mengatur retensi snapshot
---
## Kenapa topik ini diuji
Statspack adalah pendahulu AWR dan masih muncul di soal sebagai alternatif tanpa Diagnostic Pack.

## Konsep inti
```sql
-- sebagai SYSDBA
@?/rdbms/admin/spcreate.sql      -- buat user PERFSTAT
-- menjawab nama tablespace & password

EXEC statspack.snap;              -- snapshot manual
@?/rdbms/admin/spreport.sql       -- laporan antar snapshot

-- otomatis tiap 30 menit
EXEC statspack.modify_statspack_parameter(i_snap_level => 6, i_snap_interval => 30);
```

Tabel utama: `stats$snapshot`, `stats$sysstat`, `stats$sql_summary`. Retensi diatur dengan menghapus snapshot lama (`sppurge.sql`) atau `stats$snapshot` sesuai kebijakan.

## Jebakan
- Statspack butuh tablespace dan user khusus (PERFSTAT).
- Snapshot terlalu sering membebani; 15-60 menit lazim.
- Statspack mengandalkan data kumulatif — laporan selalu per rentang.
- AWR lebih disarankan bila Diagnostic Pack tersedia.

## Latihan
1. Perintah membuat snapshot Statspack?
2. Berapa selang snapshot yang wajar?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>EXEC statspack.snap;</code></p>
<p><b>2.</b> 15-60 menit, tergantung tujuan analisis.</p>
</details>
