---
title: Prasyarat onboarding
minutes: 20
level: Menengah
badge: lengkap
summary: Akun AWS, izin, aktivasi OCI, dan urutan yang harus dilalui.
objectives:
  - Menyebutkan prasyarat onboarding
  - Menjelaskan urutan aktivasi
  - Mengenali izin yang sering dilupakan
---
## Kenapa topik ini diuji
Soal menanyakan langkah pertama dan izin minimum; kesalahan urutan menggagalkan onboarding.

## Konsep inti
Urutan:

```text
1. Punya akun AWS (dan user dengan izin yang cukup)
2. Terima/ajukan penawaran di AWS Marketplace
3. Aktivasi akun OCI (tautan dari konsol AWS atau email)
4. Inisialisasi layanan Oracle Database@AWS di region target
5. Buat ODB network, lalu resource database
```

Izin AWS yang perlu diperhatikan (terutama bila ada Service Control Policy):

- `odb:GetOciOnboardingStatus` — tanpa ini layanan gagal diinisialisasi.
- `license-manager:ListReceivedGrants` — validasi grant lisensi.
- Izin Marketplace untuk menerima private offer.

Izin ini dapat dipanggil di `us-east-1` meski operasi dilakukan di region lain.

## Jebakan
- SCP yang membatasi region bisa memblokir inisialisasi walau region target diizinkan.
- Tanpa aktivasi OCI, dashboard tidak bisa dipakai.
- Akun OCI baru vs menautkan ke akun OCI yang sudah ada — pilihan di halaman aktivasi.
- Izin Market­place berbeda dari izin `odb:`.

## Latihan
1. Izin yang wajib ada agar layanan bisa diinisialisasi?
2. Mengapa SCP bisa menggagalkan onboarding?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>odb:GetOciOnboardingStatus</code> (dan <code>license-manager:ListReceivedGrants</code> untuk grant).</p>
<p><b>2.</b> Karena layanan memanggil API di <code>us-east-1</code> yang mungkin diblokir SCP.</p>
</details>
