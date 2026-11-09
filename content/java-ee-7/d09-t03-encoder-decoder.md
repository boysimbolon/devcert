---
title: Encoder dan Decoder Pesan WebSocket
minutes: 20
level: Menengah
badge: lengkap
summary: Mengubah objek Java ke teks/biner dan sebaliknya untuk WebSocket.
objectives:
  - Menulis Text encoder dan decoder
  - Memilih tipe pesan (teks, biner, stream)
  - Mendaftarkan codec pada endpoint
---
## Kenapa topik ini diuji
Banyak yang bisa menulis endpoint tetapi gagal saat objek dikirim. Soal menanyakan antarmuka mana yang harus diimplementasikan untuk tipe tertentu.

## Konsep inti
```java
public class Pesan { public String dari, isi; }

public class PesanEncoder implements Encoder.Text<Pesan> {
    public String encode(Pesan p) throws EncodeException {
        return "{\"dari\":\"" + p.dari + "\",\"isi\":\"" + p.isi + "\"}";
    }
    public void init(EndpointConfig c) { }
    public void destroy() { }
}

public class PesanDecoder implements Decoder.Text<Pesan> {
    public Pesan decode(String s) throws DecodeException {
        Pesan p = new Pesan();
        p.dari = "?"; p.isi = s;
        return p;
    }
    public boolean willDecode(String s) { return s != null && !s.isEmpty(); }
    public void init(EndpointConfig c) { }
    public void destroy() { }
}

@ServerEndpoint(value = "/chat", encoders = PesanEncoder.class, decoders = PesanDecoder.class)
public class Chat { }
```

Tipe codec yang tersedia: `Text` (String), `TextStream` (Writer/Reader), `Binary` (ByteBuffer), `BinaryStream` (OutputStream/InputStream). Pilih `Binary` untuk data biner; `TextStream` berguna untuk payload besar bertahap.

## Jebakan ujian
- `willDecode` dipanggil sebelum `decode`; return `false` membuat pesan dibatalkan.
- `init`/`destroy` pada codec dipanggil container, bukan per pesan.
- Satu endpoint dengan dua decoder untuk tipe yang sama = ambigu.
- Encoder harus publik dan punya konstruktor tanpa argumen.
- `sendObject` gagal (`EncodeException`) bila tipe objeknya tidak punya encoder terdaftar.

## Latihan
1. Antarmuka mana untuk mengirim `ByteBuffer`?
2. Apa fungsi `willDecode`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Encoder.Binary</code> / <code>Decoder.Binary</code>.</p>
<p><b>2.</b> Memeriksa apakah pesan cocok untuk decoder itu, supaya container bisa memilih decoder yang tepat.</p>
</details>
