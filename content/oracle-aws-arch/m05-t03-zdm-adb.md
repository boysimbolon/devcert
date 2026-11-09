---
title: Alur ZDM ke Autonomous Database
minutes: 20
level: Menengah
badge: lengkap
summary: Migrasi ke ADB pada Oracle Database@AWS dan batasan yang perlu diperiksa.
objectives:
  - Menjelaskan alur migrasi ke ADB
  - Memeriksa kompatibilitas ADB
  - Menangani objek yang tidak didukung
---
## Kenapa topik ini diuji
ADB punya batasan khusus; soal menanyakan apa yang harus dievaluasi sebelum migrasi.

## Konsep inti
Alur:

```text
1. Siapkan target: ODB network + ADB (serverless) atau Autonomous VM cluster/ACDB (dedicated)
2. Assessment kompatibilitas ADB (fitur, parameter, objek sistem)
3. Pilih metode ZDM: logical online (umum untuk ADB)
4. Replikasi data dan objek, validasi
5. Cutover dan verifikasi aplikasi
```

Batasan umum ADB: kontrol parameter terbatas, beberapa fitur/privilege tidak tersedia, dan objek yang membutuhkan akses OS tidak didukung.

## Jebakan
- Menganggap semua fitur Exadata tersedia di ADB.
- Skema dengan privilege tinggi/objek sistem perlu penyesuaian.
- Karakter set dan versi harus cocok dengan dukungan ADB.
- Migrasi logis bisa lebih lambat untuk dataset sangat besar.

## Latihan
1. Metode ZDM yang umum untuk ADB?
2. Apa yang harus dievaluasi lebih dulu?

<details><summary>Jawaban</summary>
<p><b>1.</b> Logical online migration.</p>
<p><b>2.</b> Kompatibilitas fitur/parameter/objek terhadap batasan ADB.</p>
</details>
