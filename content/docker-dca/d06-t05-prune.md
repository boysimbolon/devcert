---
title: Prune dan pembersihan ruang
minutes: 20
level: Menengah
badge: lengkap
summary: Menghapus resource tak terpakai tanpa menghapus data penting.
objectives:
  - Memahami perintah prune
  - Membedakan prune aman dan berisiko
  - Mengukur pemakaian disk
---
## Konsep inti
```bash
docker system df
docker container prune            # container berhenti
docker image prune                # dangling
docker image prune -a             # semua tanpa container
docker volume prune               # volume tanpa container  (HATI-HATI)
docker network prune              # network tanpa container
docker buildx prune               # cache build
docker system prune --volumes     # semuanya, termasuk volume
```

## Jebakan
- `volume prune` menghapus volume yang tidak dipakai container — data bisa hilang permanen.
- `system prune` default **tidak** menghapus volume; `--volumes` melakukannya.
- Image yang tidak dipakai container tetapi masih diperlukan untuk rollback ikut terhapus dengan `-a`.
- Build cache besar bisa menyamai ukuran image; `buildx prune` sering terlupakan.

## Latihan
1. Perintah menghapus volume tak terpakai?
2. Apakah `docker system prune` menghapus volume secara default?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>docker volume prune</code>.</p>
<p><b>2.</b> Tidak; perlu <code>--volumes</code>.</p>
</details>
