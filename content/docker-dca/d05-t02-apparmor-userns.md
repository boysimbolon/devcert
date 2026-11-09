---
title: AppArmor, SELinux, dan user namespace
minutes: 22
level: Menengah
badge: lengkap
summary: MAC host, label volume, dan pemetaan UID.
objectives:
  - Memakai profil AppArmor/SELinux
  - Menjelaskan label :z dan :Z
  - Mengaktifkan userns-remap
---
## Konsep inti
```bash
docker run --security-opt apparmor=docker-default nginx
docker run -v /data:/data:z nginx        # label bersama (SELinux)
docker run -v /data:/data:Z nginx        # label privat

# /etc/docker/daemon.json
{ "userns-remap": "default" }
```

Dengan `userns-remap`, root di container dipetakan ke UID tak berhak di host; image/container lama tidak terlihat setelah diaktifkan (data-root terpisah).

## Jebakan
- `:z` vs `:Z`: `Z` memberi label privat sehingga container lain tidak bisa akses.
- userns-remap memecahkan bind mount kepemilikan lama dan sebagian driver/plugin.
- AppArmor hanya di distro yang mendukung (Debian/Ubuntu/SUSE).
- SELinux enforcing tanpa label benar → permission denied meski mode file 777.

## Latihan
1. Arti opsi volume `:Z`?
2. Apa efek userns-remap pada container lama?

<details><summary>Jawaban</summary>
<p><b>1.</b> Memberi label SELinux privat untuk volume tersebut.</p>
<p><b>2.</b> Tidak terlihat/berjalan pada data-root baru; perlu dibuat ulang.</p>
</details>
