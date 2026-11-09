---
title: Storage driver
minutes: 22
level: Menengah
badge: lengkap
summary: overlay2, vfs, btrfs, zfs, dan cara memeriksa pemakaiannya.
objectives:
  - Mengetahui driver yang tersedia
  - Memilih driver sesuai filesystem
  - Membaca pemakaian ruang
---
## Konsep inti
```bash
docker info --format '{{.Driver}}'
docker system df -v | head -20
```

| Driver | Catatan |
|---|---|
| `overlay2` | default pada ext4/xfs, paling umum |
| `overlayfs` | nama yang dilaporkan Docker versi baru untuk mekanisme overlay |
| `vfs` | tanpa copy-on-write, lambat, hemat kompatibilitas |
| `btrfs` / `zfs` | butuh filesystem pendukung, mendukung snapshot |
| `fuse-overlayfs` | untuk rootless |

Uji: driver harus cocok dengan filesystem `data-root`. Mengganti driver tidak mengonversi image lama — perlu rebuild/pull ulang.

## Jebakan
- `vfs` menggandakan pemakaian disk karena setiap layer disalin penuh.
- `devicemapper` sudah tidak dipakai pada versi modern.
- Mengganti storage driver menghapus akses ke image/container lama di data-root tersebut.
- `docker system df` memisahkan images, containers, volumes, build cache — bukan total disk host.

## Latihan
1. Driver default pada mayoritas instalasi Linux?
2. Mengapa `vfs` boros?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>overlay2</code> (dilaporkan <code>overlayfs</code> pada Docker versi baru).</p>
<p><b>2.</b> Karena tidak memakai copy-on-write sehingga tiap layer disalin utuh.</p>
</details>
