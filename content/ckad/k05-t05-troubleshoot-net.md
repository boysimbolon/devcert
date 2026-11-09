---
title: Troubleshooting jaringan aplikasi
minutes: 20
level: Menengah
badge: lengkap
summary: Urutan diagnosis dari Service sampai container.
objectives:
  - Menguji konektivitas bertahap
  - Memeriksa endpoint dan policy
  - Memakai alat bantu sementara
---
## Konsep inti
```bash
kubectl get endpointslices -l kubernetes.io/service-name=web
kubectl describe svc web
kubectl exec web-xxx -- wget -qO- http://localhost:8080/healthz
kubectl run tmp --image=nicolaka/netshoot --rm -it --restart=Never -- curl -sv http://web:80
kubectl get netpol -A
```

Urutan: Pod Ready? → Service selector cocok (endpoint ada)? → targetPort benar? → NetworkPolicy mengizinkan? → DNS resolve? → Ingress controller ada?

## Jebakan
- Endpoint kosong = masalah selector/label, bukan jaringan.
- `targetPort` salah nama (named port) jika container tidak mendeklarasikan `name`.
- Policy egress bisa memblokir DNS (port 53) dan membuat semua koneksi gagal.
- Menguji dari Pod yang sama tidak menguji jalur Service (pakai Pod lain).

## Latihan
1. Tanda pertama Service tidak punya backend?
2. Mengapa policy egress bisa memutus DNS?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>kubectl get endpoints</code> kosong.</p>
<p><b>2.</b> Karena trafik ke CoreDNS (UDP/TCP 53) ikut diblokir bila tidak diizinkan.</p>
</details>
