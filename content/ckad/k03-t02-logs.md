---
title: Log dan event
minutes: 18
level: Dasar
badge: lengkap
summary: kubectl logs, multi-container, previous, dan event kluster.
objectives:
  - Membaca log container
  - Menangani Pod multi-container
  - Membaca event untuk diagnosis
---
## Konsep inti
```bash
kubectl logs web-7d9f-abc
kubectl logs web-7d9f-abc -c sidecar
kubectl logs web-7d9f-abc --previous
kubectl logs -f deploy/web --tail=50
kubectl logs -l app=web --all-containers=true
kubectl get events --sort-by=.lastTimestamp
kubectl describe pod web-7d9f-abc | tail -20
```

## Jebakan
- Log hilang setelah container restart kecuali `--previous` (dan hanya untuk instance sebelumnya).
- Pod multi-container wajib `-c`.
- `kubectl logs deploy/x` memilih satu Pod; gunakan `-l` untuk semua.
- Event dibatasi retensi (~1 jam default) sehingga cepat hilang.

## Latihan
1. Cara melihat log container yang sudah restart?
2. Perintah log semua Pod dengan label app=web?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>kubectl logs &lt;pod&gt; --previous</code>.</p>
<p><b>2.</b> <code>kubectl logs -l app=web --all-containers=true</code>.</p>
</details>
