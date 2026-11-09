---
title: Deployment dan ReplicaSet
minutes: 22
level: Dasar
badge: lengkap
summary: Membuat, memperbarui, dan memeriksa Deployment.
objectives:
  - Membuat Deployment cepat
  - Menjelaskan hubungan Deployment-ReplicaSet-Pod
  - Mengatur strategi update
---
## Konsep inti
```bash
kubectl create deployment web --image=nginx:1.27 --replicas=3 $do > web.yaml
kubectl apply -f web.yaml
kubectl get deploy,rs,pods -l app=web
kubectl describe deployment web
kubectl scale deployment web --replicas=5
kubectl set image deployment/web nginx=nginx:1.28
```

```yaml
spec:
  replicas: 3
  revisionHistoryLimit: 5
  strategy:
    type: RollingUpdate
    rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }
  selector:
    matchLabels: { app: web }
```

Hierarki: Deployment → ReplicaSet (per revisi) → Pod. Deployment mengelola ReplicaSet, bukan Pod langsung.

## Jebakan
- `selector` tidak bisa diubah setelah Deployment dibuat (immutable) — hapus dan buat ulang.
- `maxUnavailable: 0` + `maxSurge: 0` tidak valid (tidak ada progres).
- Mengubah label Pod secara manual membuat ReplicaSet membuat Pod baru.
- `kubectl delete deploy` menghapus Pod juga; PVC tetap.

## Latihan
1. Objek yang dibuat Deployment untuk menjaga jumlah Pod?
2. Mengapa selector tidak bisa diubah?

<details><summary>Jawaban</summary>
<p><b>1.</b> ReplicaSet.</p>
<p><b>2.</b> Karena akan mengubah kepemilikan Pod yang ada; field ini immutable.</p>
</details>
