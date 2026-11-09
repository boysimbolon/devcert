---
title: DNS dan service discovery
minutes: 20
level: Menengah
badge: lengkap
summary: Resolusi nama container, service name di swarm, dan alias jaringan.
objectives:
  - Menjelaskan resolusi nama
  - Memakai alias dan network-scoped alias
  - Menemukan endpoint service
---
## Konsep inti
```bash
docker run -d --name db --network appnet --network-alias database postgres:16
docker run --rm --network appnet alpine nslookup database

docker service create --name api --network appnet --replicas 3 myrepo/api
docker exec -it <task> nslookup tasks.api     # daftar task
docker exec -it <task> nslookup api           # VIP service
```

Di swarm, nama service me-resolve ke **VIP** (virtual IP) yang meneruskan ke task sehat; `tasks.<service>` me-resolve ke task individual (dipakai untuk headless/`endpoint_mode: dnsrr`).

## Jebakan
- Alias hanya berlaku dalam network tempat ia didefinisikan.
- Container tidak bisa memakai nama container di network berbeda.
- DNS service discovery tidak berlaku pada default bridge.
- `dnsrr` (DNS round robin) dipilih bila butuh alamat task langsung, bukan VIP.

## Latihan
1. Ke apa nama service resolve di swarm?
2. Endpoint mode untuk round-robin DNS?

<details><summary>Jawaban</summary>
<p><b>1.</b> VIP service.</p>
<p><b>2.</b> <code>endpoint_mode: dnsrr</code>.</p>
</details>
