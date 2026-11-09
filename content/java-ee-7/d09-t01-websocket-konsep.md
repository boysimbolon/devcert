---
title: Konsep dan Gaya Komunikasi WebSocket
minutes: 20
level: Menengah
badge: lengkap
summary: Handshake HTTP, koneksi full-duplex, dan kapan WebSocket lebih tepat dari polling.
objectives:
  - Menjelaskan handshake dan perbedaan dengan HTTP request-response
  - Memilih WebSocket vs polling/SSE
  - Memahami batas koneksi dan state
---
## Kenapa topik ini diuji
Soal menyukai konsep: apa yang terjadi pada handshake, dan mengapa WebSocket tidak cocok untuk semua kasus.

## Konsep inti
- Klien mengirim HTTP GET dengan header `Upgrade: websocket` dan `Sec-WebSocket-Key`; server menjawab `101 Switching Protocols`.
- Setelah itu koneksi TCP yang sama dipakai dua arah, **full-duplex**, tanpa overhead header HTTP per pesan.
- Endpoint punya state per koneksi (`Session`), berbeda dari servlet yang stateless per request.
- Frame bisa teks atau biner; ping/pong menjaga koneksi.

Kapan dipakai: chat, notifikasi realtime, kolaborasi dokumen, progres tugas panjang.
Kapan tidak: request-response sederhana, integrasi yang butuh cache/proxy HTTP, audiens sangat besar tanpa fan-out broker.

```javascript
// sisi klien
const ws = new WebSocket("wss://contoh.id/ws/chat");
ws.onopen = () => ws.send("halo");
ws.onmessage = (e) => console.log("diterima:", e.data);
ws.onclose = (e) => console.log("tutup:", e.code, e.reason);
```

## Jebakan ujian
- Handshake memakai HTTP, tetapi setelah 101 bukan HTTP lagi - proxy harus mendukung upgrade.
- WebSocket tidak otomatis punya session HTTP; otorisasi dilakukan saat handshake (`ServerEndpointConfig.Configurator`).
- `wss` adalah WebSocket di atas TLS.
- Server menyimpan satu `Session` per klien; menyimpan state global di endpoint adalah pola berbahaya.

## Latihan
1. Status HTTP apa yang menandai handshake berhasil?
2. Mengapa WebSocket butuh `Configurator` untuk keamanan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>101 Switching Protocols</code>.</p>
<p><b>2.</b> Karena handshake adalah HTTP, dan <code>modifyHandshake</code>/<code>checkOrigin</code> memberi tempat memeriksa identitas sebelum koneksi diterima.</p>
</details>
