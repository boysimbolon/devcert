---
title: Scaling manual dan HPA
minutes: 22
level: Menengah
badge: lengkap
summary: Scale manual, HorizontalPodAutoscaler, dan prasyarat metrics.
objectives:
  - Menskalakan manual
  - Membuat HPA dengan CPU
  - Menjelaskan mengapa HPA tidak bekerja
---
## Konsep inti
```bash
kubectl scale deployment web --replicas=6
kubectl autoscale deployment web --min=2 --max=10 --cpu-percent=70
kubectl get hpa
```

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata: { name: web }
spec:
  scaleTargetRef: { apiVersion: apps/v1, kind: Deployment, name: web }
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target: { type: Utilization, averageUtilization: 70 }
```

HPA butuh **metrics-server** dan container harus punya `resources.requests.cpu`.

## Jebakan
- Tanpa `requests.cpu`, HPA menampilkan `<unknown>/70%`.
- `kubectl top pods` gagal bila metrics-server tidak ada — HPA ikut tidak berfungsi.
- HPA dan replica manual bisa saling menimpa; pilih satu.
- Skala turun lebih lambat karena jendela stabilisasi (default 5 menit).

## Latihan
1. Prasyarat agar HPA CPU bekerja?
2. Perintah membuat HPA dari CLI?

<details><summary>Jawaban</summary>
<p><b>1.</b> metrics-server aktif dan <code>resources.requests.cpu</code> terdefinisi.</p>
<p><b>2.</b> <code>kubectl autoscale deployment web --min=2 --max=10 --cpu-percent=70</code>.</p>
</details>
