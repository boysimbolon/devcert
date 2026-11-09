---
title: Probe: liveness, readiness, startup
minutes: 24
level: Menengah
badge: lengkap
summary: Tiga jenis probe, parameter, dan dampaknya pada trafik.
objectives:
  - Menulis ketiga jenis probe
  - Menjelaskan konsekuasi masing-masing
  - Memilih handler yang tepat
---
## Kenapa topik ini diuji
Salah pilih probe membuat aplikasi di-restart terus atau tidak menerima trafik — soal skenario favorit.

## Konsep inti
```yaml
containers:
  - name: web
    image: nginx:1.27
    ports: [{ containerPort: 80 }]
    startupProbe:
      httpGet: { path: /, port: 80 }
      failureThreshold: 30
      periodSeconds: 2
    readinessProbe:
      httpGet: { path: /healthz, port: 80 }
      initialDelaySeconds: 3
      periodSeconds: 5
    livenessProbe:
      tcpSocket: { port: 80 }
      initialDelaySeconds: 10
      periodSeconds: 10
      failureThreshold: 3
```

| Probe | Gagal → |
|---|---|
| startup | container di-restart (selama start) |
| readiness | Pod dikeluarkan dari endpoint Service |
| liveness | container di-restart |

Handler: `httpGet`, `tcpSocket`, `exec`, `grpc`.

## Jebakan
- Liveness yang terlalu agresif → restart loop saat aplikasi lambat start; gunakan `startupProbe`.
- Readiness gagal tidak me-restart, hanya menghentikan trafik.
- `initialDelaySeconds` tidak berlaku untuk startup probe (yang dipakai `failureThreshold × periodSeconds`).
- Path health harus benar-benar cepat; query berat di liveness memperburuk keadaan.

## Latihan
1. Probe yang menghentikan trafik tanpa restart?
2. Probe untuk aplikasi dengan start lambat?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>readinessProbe</code>.</p>
<p><b>2.</b> <code>startupProbe</code> dengan <code>failureThreshold</code> besar.</p>
</details>
