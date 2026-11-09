---
title: ResourceQuota dan LimitRange
minutes: 20
level: Menengah
badge: lengkap
summary: Membatasi total pemakaian namespace dan default per container.
objectives:
  - Membuat quota namespace
  - Menetapkan default limit
  - Menjelaskan error akibat quota
---
## Konsep inti
```yaml
apiVersion: v1
kind: ResourceQuota
metadata: { name: quota-dev }
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    pods: "20"
    persistentvolumeclaims: "5"
---
apiVersion: v1
kind: LimitRange
metadata: { name: default-limits }
spec:
  limits:
    - type: Container
      default: { cpu: "500m", memory: "256Mi" }
      defaultRequest: { cpu: "250m", memory: "128Mi" }
      max: { cpu: "2", memory: "1Gi" }
```

## Jebakan
- Bila quota memuat `requests.cpu`, setiap Pod **wajib** punya request; jika tidak → `FailedCreate`.
- LimitRange hanya mengisi default saat pembuatan; Pod lama tidak berubah.
- Quota pada `pods` bisa memblokir Deployment membuat Pod baru.
- `kubectl describe quota` menunjukkan pemakaian aktual.

## Latihan
1. Apa yang terjadi bila Pod dibuat tanpa request di namespace yang punya quota request?
2. Objek untuk menetapkan default limit per container?

<details><summary>Jawaban</summary>
<p><b>1.</b> Pembuatan ditolak (<code>FailedCreate</code> / error validasi quota).</p>
<p><b>2.</b> <code>LimitRange</code>.</p>
</details>
