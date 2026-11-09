---
title: Arsitektur MySQL HeatWave Cluster
minutes: 22
level: Menengah
badge: lengkap
summary: DB system, node HeatWave, in-memory column store, dan offload query analitik.
objectives:
  - Menjelaskan komponen HeatWave
  - Menjelaskan bagaimana query dialihkan
  - Membedakan beban OLTP dan OLAP pada layanan ini
---
## Kenapa topik ini diuji
HeatWave adalah layanan analitik MySQL di OCI; soal menguji arsitektur dan alur query.

## Konsep inti
```text
DB System (MySQL 8.0, komputasi + storage)
   ├── HeatWave plugin  -> manajemen cluster, penjadwalan query, mengembalikan hasil
   └── HeatWave Cluster -> beberapa node, data di memori (column store), eksekusi paralel
```

Alur query:

1. Aplikasi mengirim query SQL biasa ke DB system.
2. Optimizer memutuskan query cocok untuk offload (biasanya analitik: agregasi, scan besar, join).
3. HeatWave plugin mengirim query ke cluster, data dibaca dari **in-memory column store**.
4. Hasil dikembalikan ke DB system lalu ke klien.

Karakteristik: data analitik dimuat ke memori node; node tidak menyimpan data persisten (DB system tetap sumber kebenaran). Skala dengan menambah node.

```sql
-- memuat tabel ke HeatWave
ALTER TABLE penjualan SECONDARY_ENGINE=RAPID;
ALTER TABLE penjualan SECONDARY_LOAD;

-- melihat apakah query dialihkan
EXPLAIN SELECT kota, SUM(total) FROM penjualan GROUP BY kota;
```

## Jebakan
- HeatWave bukan pengganti OLTP; ia mempercepat analitik.
- Tabel harus dimuat ulang (`SECONDARY_LOAD`) setelah perubahan besar agar data analitik segar.
- Query yang tidak memenuhi syarat tetap dijalankan di DB system (tanpa percepatan).
- HeatWave adalah layanan OCI; tidak tersedia sebagai plugin on-prem.

## Latihan
1. Komponen mana yang menyimpan data analitik di memori?
2. Perintah memuat tabel ke HeatWave?

<details><summary>Jawaban</summary>
<p><b>1.</b> Node HeatWave (in-memory column store).</p>
<p><b>2.</b> <code>ALTER TABLE ... SECONDARY_ENGINE=RAPID;</code> lalu <code>ALTER TABLE ... SECONDARY_LOAD;</code></p>
</details>
