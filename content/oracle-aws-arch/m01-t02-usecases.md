---
title: Use case multicloud dan implementasinya di OCI
minutes: 20
level: Dasar
badge: lengkap
summary: Pola nyata: perluasan data center, migrasi bertahap, dan analitik lintas cloud.
objectives:
  - Menyebutkan use case umum
  - Memilih pola implementasi yang sesuai
  - Menjelaskan peran OCI dalam tiap pola
---
## Kenapa topik ini diuji
Soal skenario sering berbentuk "kebutuhan bisnis X, pola multicloud mana yang tepat".

## Konsep inti
| Use case | Pola implementasi |
|---|---|
| Menjalankan aplikasi AWS dengan database Oracle | Oracle Database@AWS (Exadata di data center AWS) |
| Migrasi bertahap dari on-premises | ZDM ke Exadata/ADB, aplikasi dipindah belakangan |
| Analitik lintas cloud | Zero-ETL ke Amazon Redshift, atau Data Guard/Data Pump |
| Kedaulatan data | region sesuai regulasi, replikasi lintas cloud |
| DR lintas penyedia | Data Guard/Active Data Guard ke cloud kedua |

Peran OCI: menyediakan layanan database terkelola yang berjalan dekat aplikasi AWS, dengan konsol AWS sebagai pintu masuk dan API AWS yang memanggil API OCI.

```text
Konsol/CLI AWS  ->  API AWS (odb:*)  ->  API OCI  ->  Exadata / ADB
```

## Jebakan
- Menempatkan aplikasi dan database di region berbeda tanpa menghitung latensi.
- Menganggap multicloud otomatis memberi DR; DR tetap harus dirancang.
- Melewatkan biaya transfer data antar-cloud.
- Memilih pola tanpa memeriksa dukungan region/feature.

## Latihan
1. Pola untuk aplikasi AWS yang butuh database Oracle dengan latensi rendah?
2. Apa peran API AWS pada Oracle Database@AWS?

<details><summary>Jawaban</summary>
<p><b>1.</b> Oracle Database@AWS di region/AZ yang sama dengan aplikasi.</p>
<p><b>2.</b> Meneruskan permintaan provisioning ke API OCI, sehingga pengguna tetap memakai alat AWS.</p>
</details>
