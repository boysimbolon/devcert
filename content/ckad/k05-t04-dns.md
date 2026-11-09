---
title: DNS dan service discovery
minutes: 20
level: Menengah
badge: lengkap
summary: Nama service, FQDN, dan troubleshooting resolusi.
objectives:
  - Menjelaskan format nama DNS
  - Membedakan service dan pod DNS
  - Mendiagnosis resolusi gagal
---
## Konsep inti
```bash
kubectl run tmp --image=busybox:1.36 --rm -it --restart=Never -- nslookup web
kubectl get svc -n default
kubectl run tmp2 --image=busybox:1.36 --rm -it --restart=Never -- nslookup web.default.svc.cluster.local
```

Format:

```text
<service>.<namespace>.svc.cluster.local
<pod-ip-dengan-dash>.<namespace>.pod.cluster.local
```

Service headless mengembalikan IP Pod; Service biasa mengembalikan ClusterIP.

## Jebakan
- Nama pendek (`web`) hanya resolve dalam namespace yang sama.
- Pod harus memakai `dnsPolicy: ClusterFirst` (default) agar memakai CoreDNS.
- `nslookup` gagal bila container tidak punya tool; gunakan `getent hosts`.
- CoreDNS yang bermasalah membuat semua resolusi gagal; cek `kubectl -n kube-system get pods`.

## Latihan
1. FQDN Service `db` di namespace `prod`?
2. Mengapa `nslookup db` dari namespace lain gagal?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>db.prod.svc.cluster.local</code>.</p>
<p><b>2.</b> Karena nama pendek di-resolve pada namespace Pod yang meminta.</p>
</details>
