---
title: Pilar OCI Well-Architected untuk Oracle Database@AWS
minutes: 18
level: Menengah
badge: lengkap
summary: Enam pilar dan cara menerapkannya pada arsitektur lintas cloud.
objectives:
  - Menyebutkan enam pilar
  - Menerapkan tiap pilar pada desain
  - Menilai trade-off antar pilar
---
## Kenapa topik ini diuji
Soal arsitektur tingkat profesional sering meminta penilaian trade-off antar pilar.

## Konsep inti
| Pilar | Fokus pada Oracle Database@AWS |
|---|---|
| Operational excellence | otomatisasi provisioning, IaC, runbook, observability |
| Security | IAM dua lapis, isolasi jaringan, enkripsi, audit |
| Reliability | RAC + Data Guard, uji failover, backup teruji |
| Performance efficiency | penempatan AZ, ukuran VM cluster, SQL tuning |
| Cost optimization | pilih serverless vs dedicated, kompresi, retensi backup |
| Sustainability | konsolidasi PDB, efisiensi kapasitas |

Trade-off nyata: HA lebih tinggi = biaya lebih besar; latensi lebih rendah = penempatan terbatas pada satu AZ.

## Jebakan
- Mengoptimasi biaya dengan mengorbankan reliabilitas tanpa perhitungan RTO/RPO.
- Menganggap satu pilar bisa dipenuhi tanpa memengaruhi pilar lain.
- Tidak mendokumentasikan keputusan arsitektur (ADR).
- Mengabaikan biaya egress lintas cloud.

## Latihan
1. Pilar yang menangani uji failover?
2. Contoh trade-off antara biaya dan reliabilitas.

<details><summary>Jawaban</summary>
<p><b>1.</b> Reliability.</p>
<p><b>2.</b> Menghapus standby Data Guard menghemat biaya tetapi menaikkan RTO/RPO saat bencana.</p>
</details>
