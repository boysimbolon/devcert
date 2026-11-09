---
title: NetworkPolicy
minutes: 22
level: Menengah
badge: lengkap
summary: Membatasi trafik ingress/egress antar Pod.
objectives:
  - Menulis policy ingress dan egress
  - Menjelaskan default deny
  - Memilih selector yang tepat
---
## Konsep inti
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: db-akses }
spec:
  podSelector:
    matchLabels: { app: db }
  policyTypes: ["Ingress"]
  ingress:
    - from:
        - podSelector: { matchLabels: { app: api } }
        - namespaceSelector: { matchLabels: { env: prod } }
      ports:
        - protocol: TCP
          port: 5432
```

```bash
kubectl get netpol
kubectl describe netpol db-akses
```

## Jebakan
- Policy bersifat **aditif** dan hanya membatasi; tidak ada policy = semua trafik bebas.
- Begitu satu policy `Ingress` memilih Pod, trafik lain yang tidak cocok diblokir (default deny untuk Pod itu).
- Butuh CNI yang mendukung NetworkPolicy (Calico, Cilium, kindnet versi baru). CNI sederhana bisa mengabaikannya tanpa error — uji dulu di kluster Anda.
- `podSelector` dan `namespaceSelector` dalam satu elemen `from` = AND; dalam elemen terpisah = OR.

## Latihan
1. Arti policy tanpa aturan `ingress`?
2. Mengapa NetworkPolicy bisa tidak berefek di kluster tertentu?

<details><summary>Jawaban</summary>
<p><b>1.</b> Menolak semua ingress ke Pod yang dipilih.</p>
<p><b>2.</b> Karena CNI-nya tidak mengimplementasikan NetworkPolicy.</p>
</details>
