---
title: Seccomp dan capability
minutes: 22
level: Menengah
badge: lengkap
summary: Membatasi syscall dan hak istimewa kernel.
objectives:
  - Menjelaskan profil seccomp default
  - Mengurangi capability
  - Menghindari --privileged
---
## Konsep inti
```bash
docker run --rm --security-opt seccomp=default.json alpine ls
docker run --rm --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx
docker run --rm --security-opt no-new-privileges alpine id
docker inspect --format '{{.HostConfig.CapAdd}} {{.HostConfig.Privileged}}' <container>
```

- Docker memasang profil **seccomp default** yang menolak sekitar 40+ syscall berisiko.
- Capability Linux dibagi; Docker membuang banyak capability secara default.
- `--privileged` memberi semua capability dan akses device — hindari.

## Jebakan
- `--privileged` menonaktifkan banyak proteksi sekaligus (seccomp, capability, device).
- `--cap-add=SYS_ADMIN` hampir setara root pada host.
- Profil seccomp kustom harus JSON valid; salah format membuat container gagal start.
- Aplikasi yang butuh port <1024 sebaiknya `cap-add=NET_BIND_SERVICE` daripada root.

## Latihan
1. Opsi untuk mencegah eskalasi lewat setuid?
2. Mengapa `--privileged` berbahaya?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>--security-opt no-new-privileges</code>.</p>
<p><b>2.</b> Karena memberi akses hampir penuh ke host (capability, device, seccomp longgar).</p>
</details>
