---
title: Replikasi untuk ketersediaan dan skalabilitas
minutes: 20
level: Dasar
badge: lengkap
summary: Model source-replica, manfaat HA, dan batasannya.
objectives:
  - Menjelaskan alur replikasi asinkron
  - Membedakan manfaat HA dan read scaling
  - Menyebutkan batasan replikasi asinkron
---
## Kenapa topik ini diuji
Soal konsep: replikasi memberi apa, dan apa yang tidak dijamin.

## Konsep inti
Alur asinkron:

```text
Source: transaksi commit -> binlog
        dump thread mengirim event
Replica: receiver thread -> relay log
         applier thread -> apply ke data
```

Manfaat:

- **Read scaling** — beban baca dibagi ke replica.
- **HA** — failover ke replica saat source mati.
- **Backup** — backup di replica tanpa membebani source.
- **Geografis** — data dekat pengguna.

Batasan:

- Asinkron: **bisa kehilangan transaksi** yang belum terkirim saat source mati.
- Replica tertinggal (lag) → data basi untuk pembacaan.
- Bukan solusi split-brain otomatis; butuh orchestrator (mis. InnoDB Cluster, MHA).

## Jebakan
- Menganggap replikasi = backup. Replikasi mereplikasi kesalahan (DROP TABLE ikut).
- Membaca dari replica untuk data yang harus real-time.
- Replica tunggal dianggap HA penuh tanpa mekanisme failover.
- `binlog_format=STATEMENT` pada query non-deterministik memberi hasil berbeda di replica.

## Latihan
1. Mengapa replikasi bukan pengganti backup?
2. Apa risiko utama replikasi asinkron?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena perubahan yang merusak (mis. DROP TABLE) langsung direplikasi; backup memungkinkan kembali ke keadaan sebelumnya.</p>
<p><b>2.</b> Kehilangan transaksi terakhir saat source gagal sebelum event terkirim.</p>
</details>
