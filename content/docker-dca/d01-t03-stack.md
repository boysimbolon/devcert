---
title: Stack dan deploy Compose
minutes: 26
level: Menengah
badge: lengkap
summary: docker stack deploy, prefiks nama, dan kunci deploy: di Compose.
objectives:
  - Mendeploy stack dari file Compose
  - Menjelaskan penamaan service pada stack
  - Memakai blok deploy di Compose v3
---
## Konsep inti
```yaml
# docker-compose.yml
services:
  web:
    image: nginx:1.25
    ports: ["80:80"]
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
      restart_policy:
        condition: on-failure
      placement:
        constraints: [node.role == worker]
  redis:
    image: redis:7
    deploy:
      replicas: 1
```

```bash
docker stack deploy -c docker-compose.yml mystack
docker stack ls
docker stack services mystack      # nama service: mystack_web
docker stack ps mystack
docker stack rm mystack
```

## Jebakan
- `docker stack deploy` mengabaikan kunci di luar `deploy:` untuk swarm (`build` tidak didukung — image harus sudah ada di registry).
- Nama service menjadi `<stack>_<service>`, sehingga `docker service ls` menampilkan prefiks.
- `docker stack rm` menghapus service dan network, tetapi **tidak** menghapus volume.
- Compose file yang dipakai stack harus versi 3+ (tanpa kunci `version` pun boleh di Compose v2 modern).

## Latihan
1. Bagaimana service `web` pada stack `mystack` diberi nama?
2. Apakah `build:` dijalankan oleh `docker stack deploy`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>mystack_web</code>.</p>
<p><b>2.</b> Tidak; image harus sudah dibangun dan tersedia di registry.</p>
</details>
