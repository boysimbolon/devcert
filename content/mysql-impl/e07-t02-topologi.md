---
title: Topologi replikasi
minutes: 20
level: Menengah
badge: lengkap
summary: Single primary, chain, multi-source, delayed replica, dan group replication.
objectives:
  - Memilih topologi sesuai kebutuhan baca/tulis
  - Menjelaskan risiko tiap topologi
  - Memakai delayed replica untuk melindungi dari kesalahan operator
---
## Kenapa topik ini diuji
Soal pemilihan topologi: diberikan pola beban, pilih yang tepat.

## Konsep inti
| Topologi | Kegunaan | Risiko |
|---|---|---|
| Single primary → banyak replica | skalabilitas baca | lag, tidak otomatis failover |
| Chain (primary → intermediate → replica) | hemat koneksi source | lag berlapis |
| Multi-source (banyak source → 1 replica) | konsolidasi | konflik PK |
| Delayed replica | pemulihan dari human error | data tertinggal |
| Group Replication / InnoDB Cluster | HA otomatis | butuh 3+ anggota, quorum |

```sql
-- delayed replica: tertinggal satu jam
CHANGE REPLICATION SOURCE TO SOURCE_DELAY = 3600;
```

Cara memanfaatkan delayed replica: saat `DROP TABLE` tak sengaja terjadi, hentikan replica sebelum event itu diterapkan, lalu ambil data.

## Jebakan
- Chain menambah lag dan titik gagal; jangan untuk HA.
- Multi-source tanpa pemisahan skema → bentrok primary key.
- Delayed replica tidak membantu bila kesalahan terjadi lebih lama dari delay.
- Topologi tanpa Router/orchestrator tidak otomatis failover.

## Latihan
1. Topologi untuk melindungi dari DROP TABLE yang tidak disengaja?
2. Mengapa chain tidak cocok untuk HA?

<details><summary>Jawaban</summary>
<p><b>1.</b> Delayed replica (SOURCE_DELAY).</p>
<p><b>2.</b> Karena setiap tingkat menambah lag dan menjadi titik gagal tambahan.</p>
</details>
