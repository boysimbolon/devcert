---
title: Request, limit, dan kelas QoS
minutes: 22
level: Menengah
badge: lengkap
summary: Cara penjadwalan memakai request dan cara kernel menegakkan limit.
objectives:
  - Menetapkan request dan limit
  - Menjelaskan tiga kelas QoS
  - Memahami OOMKilled
---
## Konsep inti
```yaml
resources:
  requests: { cpu: "250m", memory: "128Mi" }
  limits:   { cpu: "500m", memory: "256Mi" }
```

| Kelas QoS | Syarat |
|---|---|
| `Guaranteed` | semua container punya request = limit untuk CPU **dan** memori |
| `Burstable` | ada request/limit, tetapi tidak sama |
| `BestEffort` | tidak ada request maupun limit |

```bash
kubectl get pod web -o jsonpath='{.status.qosClass}'
kubectl top pod
```

## Jebakan
- Melebihi limit memori → container `OOMKilled` (exit 137).
- CPU limit menyebabkan throttling, bukan pembunuhan proses.
- Request terlalu besar → Pod `Pending` karena tidak ada node yang cukup.
- Tanpa request, scheduler memakai perkiraan dan Pod mudah digeser.

## Latihan
1. Kelas QoS bila request = limit untuk CPU dan memori?
2. Mengapa Pod bisa Pending karena resource?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Guaranteed</code>.</p>
<p><b>2.</b> Karena total request tidak muat di node mana pun.</p>
</details>
