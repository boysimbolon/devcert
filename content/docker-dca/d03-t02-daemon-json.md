---
title: Konfigurasi daemon.json
minutes: 22
level: Menengah
badge: lengkap
summary: Opsi utama daemon, lokasi file, dan cara menerapkannya.
objectives:
  - Menulis konfigurasi daemon
  - Menjelaskan opsi yang sering diuji
  - Menerapkan perubahan dengan benar
---
## Konsep inti
`/etc/docker/daemon.json`:

```json
{
  "data-root": "/var/lib/docker",
  "storage-driver": "overlay2",
  "log-driver": "json-file",
  "log-opts": { "max-size": "10m", "max-file": "3" },
  "insecure-registries": ["registry.local:5000"],
  "registry-mirrors": ["https://mirror.example"],
  "live-restore": true,
  "default-address-pools": [{ "base": "172.30.0.0/16", "size": 24 }],
  "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:2376"]
}
```

```bash
docker info --format '{{.Driver}} {{.DockerRootDir}} {{.LoggingDriver}}'
```

Catatan versi: driver default historis adalah `overlay2`; Docker versi baru melaporkan `overlayfs`.

## Jebakan
- JSON tidak boleh memuat komentar; kesalahan sintaks membuat daemon gagal start.
- `"hosts"` di daemon.json bisa bertabrakan dengan flag `-H` di unit systemd (duplikasi = error).
- `live-restore` tidak berlaku untuk perubahan storage driver.
- Mengubah `data-root` tidak memindahkan image lama otomatis.

## Latihan
1. Lokasi konfigurasi daemon pada Linux?
2. Opsi agar container tetap jalan saat daemon restart?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>/etc/docker/daemon.json</code>.</p>
<p><b>2.</b> <code>"live-restore": true</code>.</p>
</details>
