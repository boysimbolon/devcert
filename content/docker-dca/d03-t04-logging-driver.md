---
title: Logging driver
minutes: 20
level: Menengah
badge: lengkap
summary: json-file, local, journald, syslog, dan pembatasan ukuran log.
objectives:
  - Memilih logging driver
  - Membatasi ukuran log
  - Menjelaskan batasan docker logs
---
## Konsep inti
```bash
docker run -d --log-driver json-file --log-opt max-size=10m --log-opt max-file=3 nginx
docker run -d --log-driver syslog --log-opt syslog-address=udp://logs:514 nginx
docker info --format '{{.LoggingDriver}}'
docker logs --tail 100 <container>
```

Driver umum: `json-file` (default), `local`, `journald`, `syslog`, `fluentd`, `gelf`, `awslogs`, `splunk`, `none`.

## Jebakan
- `docker logs` hanya bekerja untuk driver yang menyimpan log lokal (`json-file`, `local`, `journald`); untuk `syslog`/`fluentd` perintah ini tidak menampilkan apa pun.
- Tanpa `max-size`/`max-file`, `json-file` bisa memenuhi disk.
- Opsi log bisa diatur global di `daemon.json` atau per container.
- `--log-driver none` membuang log sepenuhnya.

## Latihan
1. Driver log default?
2. Mengapa `docker logs` kosong saat memakai driver syslog?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>json-file</code>.</p>
<p><b>2.</b> Karena log dikirim ke tujuan eksternal sehingga Docker tidak menyimpan salinan lokal.</p>
</details>
