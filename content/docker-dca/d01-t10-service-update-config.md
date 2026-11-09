---
title: Konfigurasi lanjutan service
minutes: 20
level: Menengah
badge: lengkap
summary: Limit resource, restart policy, network, dan mount pada service.
objectives:
  - Menetapkan limit CPU/memori
  - Mengatur restart policy
  - Melampirkan network dan volume
---
## Konsep inti
```bash
docker service create --name api \
  --limit-cpu 0.5 --limit-memory 512M --reserve-memory 256M \
  --restart-condition on-failure --restart-max-attempts 3 \
  --network appnet \
  --mount type=volume,source=api_data,target=/data \
  --env-file .env \
  myrepo/api:1.4
```

Di Compose:

```yaml
deploy:
  resources:
    limits: { cpus: "0.50", memory: 512M }
    reservations: { memory: 256M }
  restart_policy:
    condition: on-failure
    max_attempts: 3
```

## Jebakan
- `--limit-memory` tanpa reserve membuat penjadwalan tidak mempertimbangkan kebutuhan minimum.
- Replika bisa `pending` karena memori tidak cukup di node (bukan error image).
- `--mount` lebih eksplisit dan aman daripada `-v`; bind mount di swarm bergantung pada path di setiap node.
- `--network` harus network overlay (attachable) agar bisa dipakai lintas node.

## Latihan
1. Mengapa replika bisa `pending` padahal image ada?
2. Jenis mount yang aman untuk data lintas node?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena resource (memori/CPU) tidak cukup atau constraint tidak cocok.</p>
<p><b>2.</b> Named volume dengan driver yang mendukung multi-node (mis. NFS/cloud), bukan bind mount lokal.</p>
</details>
