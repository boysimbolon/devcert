---
title: Pemulihan InnoDB Cluster
minutes: 22
level: Lanjutan
badge: lengkap
summary: Menangani anggota yang gagal, rejoin, dan pemulihan total setelah outage.
objectives:
  - Mengembalikan anggota yang keluar dari grup
  - Menjalankan reboot cluster dari outage total
  - Memilih antara rejoin dan provisioning ulang
---
## Kenapa topik ini diuji
Soal skenario: cluster mati total atau satu anggota hilang. Perintahnya berbeda dan mudah tertukar.

## Konsep inti
Satu anggota hilang:

```bash
mysqlsh root@ic1:3306 -- cluster status
mysqlsh root@ic1:3306 -- cluster rejoin-instance('root@ic2:3306')
```

Bila data anggota sudah menyimpang, lakukan provisioning ulang:

```bash
mysqlsh root@ic1:3306 -- cluster.removeInstance('root@ic2:3306')
mysqlsh root@ic1:3306 -- cluster.addInstance('root@ic2:3306', {recoveryMethod:'clone'})
```

Outage total (semua anggota mati):

```bash
mysqlsh root@ic1:3306 -- dba.rebootClusterFromCompleteOutage('prodCluster')
mysqlsh root@ic1:3306 -- cluster status
```

Mode pemulihan: `auto`, `clone`, `incremental`. `clone` menyalin penuh dari donor; `incremental` memakai binlog bila memungkinkan.

## Jebakan
- `rebootClusterFromCompleteOutage` hanya untuk kasus semua anggota mati, bukan satu.
- `clone` butuh plugin clone terpasang di donor dan penerima.
- Rejoin pada anggota yang datanya menyimpang membuat error berulang; provisioning ulang lebih aman.
- Setelah outage, periksa `gtid_executed` agar tidak ada transaksi hilang.

## Latihan
1. Perintah untuk satu anggota yang tertinggal?
2. Kapan memakai `rebootClusterFromCompleteOutage`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>cluster.rejoinInstance('user@host:port')</code> (atau remove + add dengan recovery <code>clone</code> bila data menyimpang).</p>
<p><b>2.</b> Saat seluruh anggota cluster mati dan perlu dihidupkan kembali sebagai grup.</p>
</details>
