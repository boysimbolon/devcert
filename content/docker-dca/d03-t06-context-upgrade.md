---
title: Context, upgrade, dan version pinning
minutes: 18
level: Menengah
badge: lengkap
summary: Mengelola banyak endpoint Docker dan memperbarui engine dengan aman.
objectives:
  - Membuat context untuk host berbeda
  - Merencanakan upgrade
  - Mengunci versi paket
---
## Konsep inti
```bash
docker context create prod --docker "host=tcp://10.0.0.5:2376,ca=ca.pem,cert=cert.pem,key=key.pem"
docker context ls
docker context use prod
docker context inspect prod

# upgrade terkendali
sudo apt-mark hold docker-ce docker-ce-cli containerd.io
sudo apt-get install -y docker-ce=5:27.3.1-1~debian.12~bookworm
```

`docker context use default` kembali ke socket lokal.

## Jebakan
- Context dan `DOCKER_HOST` bisa saling menimpa membingungkan; pakai satu cara.
- Upgrade engine butuh restart daemon → container berhenti kecuali `live-restore`.
- `apt upgrade` tanpa hold bisa melompat beberapa versi minor sekaligus.
- Perubahan storage driver/large version jump sebaiknya diuji di host lain.

## Latihan
1. Perintah berpindah endpoint?
2. Opsi agar container tetap hidup saat upgrade?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>docker context use &lt;nama&gt;</code>.</p>
<p><b>2.</b> Aktifkan <code>live-restore</code> di <code>daemon.json</code>.</p>
</details>
