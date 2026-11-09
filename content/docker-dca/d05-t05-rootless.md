---
title: Rootless mode dan hardening host
minutes: 20
level: Menengah
badge: lengkap
summary: Menjalankan daemon tanpa root dan mengurangi risiko host.
objectives:
  - Menjelaskan rootless Docker
  - Menyebutkan batasannya
  - Menerapkan hardening dasar
---
## Konsep inti
```bash
dockerd-rootless-setuptool.sh install
export DOCKER_HOST=unix:///run/user/1000/docker.sock
systemctl --user status docker
```

Batasan rootless: tidak bisa memakai port <1024 tanpa bantuan, sebagian storage driver/plugin tidak didukung, dan performa jaringan sedikit berbeda (`slirp4netns`/`pasta`).

Hardening host: patch rutin, firewall, audit log, jangan buka 2375, batasi akses socket, gunakan `--read-only` + `tmpfs` bila memungkinkan, dan pisahkan host database/CI.

## Jebakan
- Akses ke `/var/run/docker.sock` = root efektif; jangan di-mount ke container sembarangan.
- Rootless bukan pengganti segmentasi jaringan.
- `--read-only` butuh tmpfs untuk path sementara agar aplikasi tetap jalan.
- CI runner dengan Docker socket terbuka adalah target serangan umum.

## Latihan
1. Mengapa socket Docker berbahaya bila di-mount?
2. Flag agar filesystem container read-only?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena siapa pun yang mengaksesnya bisa membuat container privileged setara root host.</p>
<p><b>2.</b> <code>--read-only</code> (plus <code>--tmpfs</code> untuk path yang perlu ditulis).</p>
</details>
