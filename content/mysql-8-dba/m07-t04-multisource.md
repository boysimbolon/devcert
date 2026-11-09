---
title: Replikasi multisource
minutes: 20
level: Menengah
badge: lengkap
summary: Beberapa source ke satu replica dengan channel, dan penamaan yang benar.
objectives:
  - Mengonfigurasi beberapa channel replikasi
  - Mengelola channel secara terpisah
  - Menghindari konflik data antar source
---
## Kenapa topik ini diuji
Multisource dipakai untuk konsolidasi data. Soal menanyakan kata kunci `FOR CHANNEL`.

## Konsep inti
```sql
-- channel 1
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='10.0.0.10', SOURCE_USER='repl', SOURCE_PASSWORD='...',
  SOURCE_AUTO_POSITION=1 FOR CHANNEL 'cabang_jkt';
START REPLICA FOR CHANNEL 'cabang_jkt';

-- channel 2
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='10.0.0.11', SOURCE_USER='repl', SOURCE_PASSWORD='...',
  SOURCE_AUTO_POSITION=1 FOR CHANNEL 'cabang_sby';
START REPLICA FOR CHANNEL 'cabang_sby';

SHOW REPLICA STATUS FOR CHANNEL 'cabang_jkt'\G
STOP REPLICA FOR CHANNEL 'cabang_jkt';
```

Setiap channel punya relay log dan thread sendiri. Konflik muncul bila dua source menulis primary key yang sama di tabel yang sama.

## Jebakan
- Lupa `FOR CHANNEL` → perintah berlaku ke channel default `''`.
- Tanpa skema pemisahan (per source schema berbeda), konflik PK hampir pasti.
- `gtid_mode=ON` pada multisource memerlukan penanganan GTID yang benar; hindari mencampur sumber dengan riwayat GTID bertabrakan.
- `STOP REPLICA` tanpa channel menghentikan semua channel.

## Latihan
1. Kata kunci untuk menargetkan channel tertentu?
2. Bagaimana mencegah konflik PK antar source?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>FOR CHANNEL 'nama'</code>.</p>
<p><b>2.</b> Pisahkan data per schema/nama tabel atau gunakan rentang ID berbeda per source.</p>
</details>
