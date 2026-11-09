---
title: Mengenal Zero Downtime Migration (ZDM)
minutes: 20
level: Menengah
badge: lengkap
summary: Alat migrasi Oracle dengan downtime minimal, arsitektur, dan prasyaratnya.
objectives:
  - Menjelaskan tujuan ZDM
  - Menyebutkan komponen dan prasyarat
  - Memilih jenis migrasi
---
## Kenapa topik ini diuji
Domain migrasi (15%) berpusat pada ZDM: apa yang bisa dan tidak bisa dilakukan.

## Konsep inti
ZDM = layanan/alat Oracle untuk memindahkan database dengan downtime nol atau sangat kecil, memakai ZDM service host (bisa di OCI) yang mengatur alur migrasi.

Dua jenis:

| Jenis | Metode | Downtime |
|---|---|---|
| Physical | Data Guard, atau backup/restore (RMAN) | sangat kecil |
| Logical | Data Pump / GoldenGate | minimal, lebih fleksibel lintas versi/endian |

Prasyarat umum: konektivitas, kredensial, versi database yang didukung, dan target yang sudah siap.

## Jebakan
- ZDM bukan alat untuk migrasi non-Oracle.
- Perbedaan versi/karakter set bisa membatasi pilihan fisik.
- Migrasi butuh bandwidth dan waktu sinkronisasi.
- Cutover tetap memerlukan jendela dan verifikasi.

## Latihan
1. Metode fisik utama pada ZDM?
2. Kapan migrasi logis lebih tepat?

<details><summary>Jawaban</summary>
<p><b>1.</b> Data Guard (atau backup/restore).</p>
<p><b>2.</b> Saat ada perbedaan versi/platform/endian atau butuh seleksi objek.</p>
</details>
