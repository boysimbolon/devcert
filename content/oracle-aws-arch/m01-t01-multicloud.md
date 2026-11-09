---
title: Multicloud dan manfaatnya
minutes: 18
level: Dasar
badge: lengkap
summary: Apa itu multicloud, model penerapannya, dan kenapa organisasi memilihnya.
objectives:
  - Mendefinisikan multicloud
  - Menyebutkan manfaat utama
  - Membedakan multicloud dengan hybrid cloud
---
## Kenapa topik ini diuji
Domain pengantar (5%) memastikan kamu paham istilah dasar sebelum masuk ke arsitektur Oracle Database@AWS.

## Konsep inti
**Multicloud** = memakai layanan dari dua atau lebih penyedia cloud publik (mis. OCI + AWS) untuk menjalankan beban kerja, baik terpisah maupun terhubung.

| Istilah | Arti |
|---|---|
| Multicloud | ≥2 cloud publik |
| Hybrid cloud | cloud + data center on-premises |
| Polycloud | banyak cloud, beban terpisah tanpa integrasi mendalam |

Manfaat: menghindari vendor lock-in, memakai layanan terbaik per kebutuhan (mis. database Oracle + layanan analitik AWS), kepatuhan data per region, dan negosiasi biaya.

**Oracle Database@AWS** adalah contoh multicloud "di tingkat infrastruktur": perangkat Exadata milik Oracle berjalan di dalam data center AWS, dikelola OCI, tetapi dipesan dan dipantau lewat AWS.

## Jebakan
- Multicloud bukan sekadar punya akun di dua cloud tanpa konektivitas.
- Multicloud menambah kompleksitas: IAM ganda, jaringan, observability, biaya egress.
- Hybrid ≠ multicloud; soal sering menukar keduanya.
- Latensi antar-cloud harus dirancang, bukan diasumsikan.

## Latihan
1. Apa perbedaan multicloud dan hybrid cloud?
2. Apa tantangan utama multicloud?

<details><summary>Jawaban</summary>
<p><b>1.</b> Multicloud memakai ≥2 cloud publik; hybrid menggabungkan cloud dengan infrastruktur on-premises.</p>
<p><b>2.</b> Kompleksitas identitas, jaringan, pemantauan, dan biaya lintas penyedia.</p>
</details>
