---
title: Alur ZDM ke Exadata di Oracle Database@AWS
minutes: 20
level: Menengah
badge: lengkap
summary: Langkah evaluasi, penyiapan target, sinkronisasi, dan cutover.
objectives:
  - Mengurutkan fase migrasi ZDM
  - Menyiapkan target Exadata
  - Merencanakan cutover
---
## Kenapa topik ini diuji
Soal memberi urutan langkah dan menanyakan fase berikutnya atau prasyaratnya.

## Konsep inti
```text
1. Assessment  : periksa kompatibilitas, ukuran, karakter set
2. Setup       : ODB network + peering + DNS; Exadata infra/VM cluster/database
3. Replikasi   : physical (Data Guard) atau logical (Data Pump/GoldenGate)
4. Validasi    : uji koneksi, bandingkan objek, uji aplikasi
5. Cutover     : hentikan beban sumber, selesaikan sinkronisasi, alihkan aplikasi
6. Pasca       : monitoring, backup, tuning, dekomisioning sumber
```

Konektivitas: ZDM host harus bisa menjangkau sumber dan target (lewat peering/VPN/Direct Connect).

## Jebakan
- Cutover tanpa uji aplikasi → masalah muncul setelah produksi pindah.
- TNS/service name target berbeda dari sumber; aplikasi harus disesuaikan.
- Data Guard memerlukan konfigurasi redo transport dan parameter yang cocok.
- Melupakan backup setelah migrasi.

## Latihan
1. Fase setelah replikasi?
2. Apa syarat jaringan untuk ZDM?

<details><summary>Jawaban</summary>
<p><b>1.</b> Validasi, lalu cutover.</p>
<p><b>2.</b> ZDM host harus bisa mencapai sumber dan target secara privat dengan bandwidth memadai.</p>
</details>
