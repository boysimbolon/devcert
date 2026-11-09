---
title: Service: ClusterIP, NodePort, LoadBalancer, headless
minutes: 24
level: Menengah
badge: lengkap
summary: Empat tipe Service dan kapan memakainya.
objectives:
  - Membuat Service untuk Deployment
  - Membedakan tipe Service
  - Menjelaskan headless service
---
## Kenapa topik ini diuji
Domain Services & Networking 20%: soal praktik meminta Service yang bisa diakses dengan cara tertentu.

## Konsep inti
```bash
kubectl expose deployment web --port=80 --target-port=8080 --type=ClusterIP
kubectl get svc,ep
kubectl port-forward svc/web 8080:80
```

```yaml
apiVersion: v1
kind: Service
metadata: { name: web }
spec:
  type: NodePort
  selector: { app: web }
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
```

| Tipe | Akses |
|---|---|
| `ClusterIP` (default) | hanya di dalam kluster |
| `NodePort` | IP node + port 30000-32767 |
| `LoadBalancer` | butuh penyedia cloud (atau MetalLB) |
| `ExternalName` | alias CNAME |
| headless (`clusterIP: None`) | DNS langsung ke Pod |

## Jebakan
- `port` (Service) ≠ `targetPort` (container); salah target = koneksi ditolak.
- Selector harus cocok dengan label Pod; cek `kubectl get endpoints`.
- `NodePort` tanpa `nodePort` dipilih acak dalam rentang.
- Service `LoadBalancer` di kluster lokal tetap `pending` untuk EXTERNAL-IP.

## Latihan
1. Tipe Service dengan IP stabil di dalam kluster?
2. Cara memeriksa apakah Service punya backend?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ClusterIP</code>.</p>
<p><b>2.</b> <code>kubectl get endpoints &lt;svc&gt;</code> — kosong berarti selector tidak cocok.</p>
</details>
