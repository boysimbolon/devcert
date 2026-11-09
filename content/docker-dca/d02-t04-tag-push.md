---
title: Tag, push, dan pull image
minutes: 20
level: Dasar
badge: lengkap
summary: Konvensi tag, registry login, dan distribusi image.
objectives:
  - Menandai image dengan benar
  - Login dan push ke registry
  - Menarik image berdasarkan digest
---
## Konsep inti
```bash
docker build -t myrepo/api:1.0 -t myrepo/api:latest .
docker tag myrepo/api:1.0 registry.local:5000/team/api:1.0
docker login registry.local:5000
docker push registry.local:5000/team/api:1.0
docker pull registry.local:5000/team/api@sha256:abc...
docker image ls --digests
```

Format nama: `[registry[:port]/][namespace/]nama[:tag]`. Tanpa registry, default `docker.io`; tanpa tag, default `latest`.

## Jebakan
- `latest` bukan "versi terbaru otomatis"; hanya tag default yang tidak informatif untuk produksi.
- Satu image bisa punya banyak tag; `docker push` mengirim per tag.
- Push ke registry lokal via HTTP butuh `insecure-registries` di `daemon.json`.
- Digest bersifat immutable, tag tidak — pin digest untuk reproducibility.
- Push image `amd64` ke node `arm64` bisa gagal jalan (butuh buildx multi-arch).

## Latihan
1. Apa arti `latest`?
2. Cara memastikan image identik antar lingkungan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tag default bila tidak disebutkan, bukan jaminan versi terbaru.</p>
<p><b>2.</b> Rujuk digest <code>@sha256:...</code>.</p>
</details>
