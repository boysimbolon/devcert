---
title: ServiceAccount dan RBAC dasar
minutes: 22
level: Menengah
badge: lengkap
summary: Identitas Pod, Role/RoleBinding, dan pemeriksaan izin.
objectives:
  - Membuat ServiceAccount dan memasangnya
  - Memberi izin dengan Role
  - Menguji izin
---
## Konsep inti
```bash
kubectl create serviceaccount app-sa
kubectl create role pod-reader --verb=get,list,watch --resource=pods
kubectl create rolebinding app-read --role=pod-reader --serviceaccount=default:app-sa
kubectl auth can-i list pods --as=system:serviceaccount:default:app-sa
```

```yaml
spec:
  serviceAccountName: app-sa
  automountServiceAccountToken: false
```

| Objek | Cakupan |
|---|---|
| Role / RoleBinding | namespace |
| ClusterRole / ClusterRoleBinding | seluruh kluster |

## Jebakan
- Default ServiceAccount punya token otomatis; matikan bila aplikasi tidak butuh API.
- RoleBinding ke ServiceAccount memakai format `namespace:nama`.
- `can-i` tanpa `--as` memeriksa identitas Anda, bukan Pod.
- Izin `create pods` berbeda dari `create pods/exec`.

## Latihan
1. Objek untuk izin lintas namespace?
2. Perintah menguji izin ServiceAccount tertentu?

<details><summary>Jawaban</summary>
<p><b>1.</b> ClusterRole + ClusterRoleBinding.</p>
<p><b>2.</b> <code>kubectl auth can-i &lt;verb&gt; &lt;resource&gt; --as=system:serviceaccount:&lt;ns&gt;:&lt;sa&gt;</code>.</p>
</details>
