---
title: Inspeksi image: history, inspect, prune
minutes: 22
level: Menengah
badge: lengkap
summary: Membaca layer, metadata, dan membersihkan image tak terpakai.
objectives:
  - Membaca history layer
  - Menemukan konfigurasi image
  - Membersihkan image dengan aman
---
## Konsep inti
```bash
docker image history myrepo/api:1.0
docker image inspect myrepo/api:1.0 --format '{{.Config.Entrypoint}} {{.Config.Cmd}}'
docker image inspect --format '{{json .RootFS.Layers}}' myrepo/api:1.0
docker image ls -f dangling=true
docker image prune          # hanya dangling
docker image prune -a       # semua yang tidak dipakai container
docker system df
```

Metadata penting: `Config.Env`, `Config.ExposedPorts`, `Config.WorkingDir`, `Config.User`, `Os`/`Architecture`, `RepoTags`, `RepoDigests`.

## Jebakan
- `history` menunjukkan perintah, tetapi baris `<missing>` muncul untuk layer hasil build lain (mis. cache import).
- `prune -a` menghapus image yang tidak dipakai container, termasuk yang masih ingin dipakai untuk build berikutnya.
- Image yang dipakai container berhenti tidak ikut terhapus tanpa `-a`.
- Menghapus image yang dipakai container yang berjalan akan gagal (atau perlu `-f` dengan risiko).

## Latihan
1. Perintah melihat instruksi pembentuk image?
2. Perbedaan `prune` dan `prune -a`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>docker image history</code>.</p>
<p><b>2.</b> <code>prune</code> hanya image dangling; <code>-a</code> semua yang tidak dipakai container.</p>
</details>
