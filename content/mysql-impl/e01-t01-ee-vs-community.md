---
title: MySQL Enterprise Edition vs Community/Standard
minutes: 20
level: Dasar
badge: lengkap
summary: Apa yang membedakan edisi berbayar dari Community, dan kapan perbedaannya penting.
objectives:
  - Menyebutkan perbedaan lisensi dan dukungan
  - Menjelaskan fitur yang hanya ada di Enterprise
  - Memilih edisi sesuai kebutuhan organisasi
---
## Kenapa topik ini diuji
Ini soal pembuka ujian: perbedaan edisi. Jawabannya bukan "lebih cepat", tapi soal fitur, dukungan, dan lisensi.

## Konsep inti
| Aspek | Community | Enterprise (Standard + add-on) |
|---|---|---|
| Lisensi | GPLv2 | komersial |
| Dukungan | komunitas | 24×7 dari Oracle, SLA |
| Backup | mysqldump, file copy | + **MySQL Enterprise Backup** (hot, inkremental) |
| Monitor | manual, performance_schema | + **MySQL Enterprise Monitor** |
| Audit | general log | + **Enterprise Audit** (terfilter, JSON/XML) |
| Firewall | — | + **Enterprise Firewall** (allowlist) |
| Auth lanjutan | plugin dasar | + **Enterprise Authentication** (PAM, LDAP, FIDO) |
| Enkripsi | keyring_file (lab) | keyring terpusat (KMIP), TDE |
| Skalabilitas | thread per koneksi | **Thread Pool** |
| Diagnostik | manual | **Support diagnostics** (mysqldump terarah) |

Yang penting untuk ujian: fitur bertanda Enterprise **tidak tersedia** di Community — bukan sekadar tidak didukung.

```text
Contoh keputusan:
- startup kecil, beban rendah        -> Community
- butuh audit kepatuhan + backup hot -> Enterprise
- butuh analitik kolom tanpa ETL     -> HeatWave (OCI)
```

## Jebakan
- Mengira Community "kurang performa"; perbedaannya di fitur manajemen, bukan kecepatan dasar.
- Menganggap Enterprise Backup bisa dipasang di Community (tidak; paketnya terpisah).
- Lupa bahwa Standard Edition adalah nama lama edisi berbayar; Enterprise = Standard + fitur tambahan.
- Menyamakan HeatWave dengan Enterprise Edition: HeatWave adalah layanan cloud terkelola.

## Latihan
1. Dua fitur yang hanya ada di Enterprise dan sering diuji?
2. Apakah Thread Pool tersedia di Community?

<details><summary>Jawaban</summary>
<p><b>1.</b> MySQL Enterprise Backup dan MySQL Enterprise Audit (juga Firewall, Monitor, Authentication).</p>
<p><b>2.</b> Tidak, Thread Pool adalah fitur Enterprise.</p>
</details>
