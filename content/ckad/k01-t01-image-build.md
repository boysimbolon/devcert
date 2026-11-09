---
title: Image container untuk Kubernetes
minutes: 20
level: Dasar
badge: lengkap
summary: Dockerfile minimal, tag, push, dan imagePullPolicy.
objectives:
  - Membangun image yang siap dipakai kluster
  - Memahami imagePullPolicy
  - Menghindari jebakan tag
---
## Kenapa topik ini diuji
CKAD adalah ujian praktik: image harus bisa di-pull oleh node, dan policy pull menentukan apakah perubahan terpakai.

## Konsep inti
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
docker build -t registry.local:5000/app:1.0 .
docker push registry.local:5000/app:1.0

kubectl create deployment web --image=registry.local:5000/app:1.0 --dry-run=client -o yaml > web.yaml
kubectl apply -f web.yaml
```

`imagePullPolicy`: `Always` (default untuk tag `latest`), `IfNotPresent` (default untuk tag lain), `Never` (hanya image lokal).

## Jebakan
- Tag `latest` + `Always` membuat setiap start menarik image; lambat dan bisa gagal bila registry tidak siap.
- Node tidak otomatis punya image lokal Anda; push ke registry yang bisa dijangkau kluster.
- `kubectl set image` lebih cepat daripada mengedit YAML untuk mengganti versi.
- Image privat butuh `imagePullSecrets` pada Pod/ServiceAccount.

## Latihan
1. Policy default untuk image `:latest`?
2. Cara mengganti image deployment tanpa mengedit file?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Always</code>.</p>
<p><b>2.</b> <code>kubectl set image deployment/web web=repo/app:1.1</code>.</p>
</details>
