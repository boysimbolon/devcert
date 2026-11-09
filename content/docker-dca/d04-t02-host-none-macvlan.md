---
title: Host, none, dan macvlan
minutes: 22
level: Menengah
badge: lengkap
summary: Mode jaringan khusus dan konsekuensinya.
objectives:
  - Menjelaskan network host dan none
  - Mengonfigurasi macvlan
  - Memilih mode sesuai kebutuhan
---
## Konsep inti
```bash
docker run --network host nginx          # tanpa isolasi, pakai port host langsung
docker run --network none alpine ifconfig  # hanya loopback

docker network create -d macvlan \
  --subnet 192.168.1.0/24 --gateway 192.168.1.1 \
  -o parent=eth0 macnet
docker run -d --network macnet --ip 192.168.1.50 nginx
```

| Mode | Ciri |
|---|---|
| `host` | container memakai stack jaringan host; `-p` diabaikan (warning) |
| `none` | tidak ada interface eksternal |
| `macvlan` | container punya MAC/IP sendiri di LAN, muncul sebagai perangkat fisik |
| `ipvlan` | alternatif macvlan dengan MAC dibagi |

## Jebakan
- `-p` pada `--network host` diabaikan; port langsung dipakai host.
- macvlan: host **tidak** bisa berkomunikasi dengan container macvlan-nya sendiri (perlu sub-interface).
- macvlan butuh jaringan yang mengizinkan banyak MAC (bisa diblokir di cloud).
- `none` tidak punya DNS; `127.0.0.1` hanya loopback container.

## Latihan
1. Mode jaringan agar container tampil seperti host fisik di LAN?
2. Apa yang terjadi pada `-p` dengan `--network host`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>macvlan</code>.</p>
<p><b>2.</b> Diabaikan, disertai peringatan.</p>
</details>
