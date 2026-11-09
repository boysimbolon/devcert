---
title: Ingress
minutes: 22
level: Menengah
badge: lengkap
summary: Aturan host/path, TLS, dan prasyarat controller.
objectives:
  - Menulis Ingress untuk dua host
  - Menambahkan TLS
  - Menjelaskan mengapa Ingress tidak bekerja
---
## Konsep inti
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
    - hosts: ["app.example.com"]
      secretName: tls-cert
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service: { name: web, port: { number: 80 } }
```

```bash
kubectl get ingress
kubectl describe ingress web
```

## Jebakan
- Tanpa Ingress controller (nginx/traefik), objek Ingress tidak berefek.
- `pathType` wajib: `Prefix`, `Exact`, `ImplementationSpecific`.
- `ingressClassName` harus cocok dengan class controller yang terpasang.
- TLS butuh Secret bertipe `kubernetes.io/tls` di namespace yang sama.

## Latihan
1. Prasyarat agar Ingress berfungsi?
2. Nilai pathType untuk pencocokan awal path?

<details><summary>Jawaban</summary>
<p><b>1.</b> Ingress controller yang berjalan di kluster.</p>
<p><b>2.</b> <code>Prefix</code>.</p>
</details>
