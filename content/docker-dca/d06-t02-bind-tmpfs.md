---
title: Bind mount dan tmpfs
minutes: 22
level: Menengah
badge: lengkap
summary: Perbedaan -v, --mount, bind, dan tmpfs.
objectives:
  - Membedakan volume, bind mount, tmpfs
  - Memakai sintaks --mount
  - Menghindari jebakan izin
---
## Konsep inti
```bash
# bind mount
docker run -d -v /srv/app:/app:ro --name web nginx
docker run -d --mount type=bind,source=/srv/app,target=/app,readonly nginx

# tmpfs (di memori)
docker run --tmpfs /tmp:size=64m alpine df -h /tmp
docker run --mount type=tmpfs,destination=/cache,tmpfs-size=104857600 alpine
```

| Jenis | Dikelola | Persisten | Kinerja |
|---|---|---|---|
| volume | Docker | ya | baik |
| bind | host path | ya (bergantung host) | baik, tergantung FS |
| tmpfs | memori | tidak | sangat cepat |

## Jebakan
- Bind mount ke path yang tidak ada akan dibuat sebagai direktori (pada Linux) tanpa peringatan.
- Izin file host bisa membuat container non-root gagal menulis.
- `-v` dan `--mount` berbeda perilaku saat source tidak ada: `-v` membuat, `--mount` gagal.
- tmpfs memakai RAM; isi hilang saat container berhenti.

## Latihan
1. Jenis mount untuk cache sementara di memori?
2. Mana yang gagal bila source tidak ada, `-v` atau `--mount`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>tmpfs</code>.</p>
<p><b>2.</b> <code>--mount</code> (lebih eksplisit).</p>
</details>
