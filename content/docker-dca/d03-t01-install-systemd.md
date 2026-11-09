---
title: Instalasi dan layanan systemd
minutes: 20
level: Dasar
badge: lengkap
summary: Paket Docker, unit docker.service, dan verifikasi instalasi.
objectives:
  - Memasang Docker Engine
  - Mengelola layanan docker
  - Memverifikasi instalasi
---
## Konsep inti
```bash
# Debian/Ubuntu
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker
sudo systemctl status docker
docker version
docker info | head -20
sudo usermod -aG docker $USER     # agar tidak perlu sudo
```

Unit penting: `docker.service`, `docker.socket`, `containerd.service`. Restart daemon:

```bash
sudo systemctl restart docker
sudo systemctl reload docker    # memuat ulang sebagian konfigurasi
```

## Jebakan
- Menambahkan user ke grup `docker` = akses setara root; pertimbangkan rootless.
- `systemctl reload` tidak menerapkan semua perubahan (mis. storage driver butuh restart).
- Container dengan `--restart always` tidak otomatis kembali setelah daemon restart bila `live-restore` mati.
- Instalasi dari repo distro bisa memberi versi lama (`docker.io` di Debian).

## Latihan
1. Perintah memuat ulang konfigurasi daemon tanpa restart penuh?
2. Mengapa grup docker berisiko?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>sudo systemctl reload docker</code>.</p>
<p><b>2.</b> Anggotanya bisa menjalankan container sebagai root pada host.</p>
</details>
