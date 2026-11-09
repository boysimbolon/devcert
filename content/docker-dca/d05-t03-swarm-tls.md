---
title: Keamanan swarm: mTLS dan join token
minutes: 22
level: Menengah
badge: lengkap
summary: Enkripsi antar node, rotasi token, dan CA swarm.
objectives:
  - Menjelaskan mTLS otomatis
  - Merotasi join token
  - Mengelola sertifikat CA
---
## Konsep inti
```bash
docker swarm join-token worker
docker swarm join-token --rotate worker     # token lama langsung tidak berlaku
docker swarm join-token --rotate manager
docker swarm ca --rotate
docker swarm ca --rotate --cert-expiry 2160h
```

Swarm mengaktifkan **mutual TLS** otomatis antar node: setiap node mendapat sertifikat dari CA internal, dirotasi berkala. Trafik manajemen dan overlay terenkripsi.

## Jebakan
- Token manager memberi kendali penuh; jangan disimpan di repo/chat.
- Rotasi token worker tidak memutus node yang sudah bergabung.
- `docker swarm ca --rotate` memerlukan restart bertahap pada node untuk memakai CA baru (dokumentasi menyarankan urutan tertentu).
- Tanpa rotasi, token bocor = node asing bisa bergabung.

## Latihan
1. Perintah merotasi token worker?
2. Apakah TLS swarm perlu dikonfigurasi manual?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>docker swarm join-token --rotate worker</code>.</p>
<p><b>2.</b> Tidak; sudah otomatis (mTLS) saat swarm aktif.</p>
</details>
