---
title: Secret
minutes: 22
level: Menengah
badge: lengkap
summary: Membuat Secret, tipe umum, dan konsumsinya.
objectives:
  - Membuat Secret dari literal/file
  - Memakai Secret sebagai env dan volume
  - Menjelaskan batas keamanannya
---
## Konsep inti
```bash
kubectl create secret generic db-pass --from-literal=password='S3cr3t!'
kubectl create secret tls tls-cert --cert=tls.crt --key=tls.key
kubectl create secret docker-registry regcred \
  --docker-server=registry.local:5000 --docker-username=u --docker-password=p

kubectl get secret db-pass -o jsonpath='{.data.password}' | base64 -d
```

```yaml
env:
  - name: DB_PASSWORD
    valueFrom: { secretKeyRef: { name: db-pass, key: password } }
volumes:
  - name: secret-vol
    secret: { secretName: db-pass, defaultMode: 0400 }
```

Tipe: `Opaque` (default), `kubernetes.io/tls`, `kubernetes.io/dockerconfigjson`, `kubernetes.io/service-account-token`, `kubernetes.io/ssh-auth`.

## Jebakan
- Secret hanya base64, **bukan** enkripsi; siapa pun dengan akses baca bisa decode.
- `stringData` memudahkan penulisan plaintext di YAML (dikonversi otomatis).
- Env dari Secret tidak ter-update otomatis; volume iya.
- Secret di namespace lain tidak bisa dirujuk.

## Latihan
1. Field untuk menulis nilai Secret sebagai plaintext di YAML?
2. Apakah Secret terenkripsi secara default?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>stringData</code>.</p>
<p><b>2.</b> Tidak; hanya base64 kecuali enkripsi at-rest diaktifkan pada kluster.</p>
</details>
