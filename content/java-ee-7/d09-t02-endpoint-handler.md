---
title: Endpoint Server dan Klien JSR 356
minutes: 24
level: Menengah
badge: lengkap
summary: @ServerEndpoint, @ClientEndpoint, callback lifecycle, dan Session.
objectives:
  - Menulis endpoint dengan anotasi lifecycle
  - Mengirim pesan ke satu klien atau semua
  - Memakai @PathParam pada endpoint
---
## Kenapa topik ini diuji
Soal memberi endpoint dengan beberapa callback lalu menanyakan urutan atau method mana yang dipanggil untuk pesan tertentu.

## Konsep inti
```java
@ServerEndpoint(value = "/chat/{ruang}", encoders = {PesanEncoder.class},
                decoders = {PesanDecoder.class})
public class ChatEndpoint {

    private static final Set<Session> SEMUA = ConcurrentHashMap.newKeySet();
    private Session sesi;

    @OnOpen
    public void buka(Session s, @PathParam("ruang") String ruang) {
        this.sesi = s; SEMUA.add(s);
        s.getUserProperties().put("ruang", ruang);
    }

    @OnMessage
    public void pesan(Pesan p, Session s) {
        SEMUA.stream().filter(Session::isOpen)
             .forEach(x -> x.getAsyncRemote().sendObject(p));   // encode otomatis
    }

    @OnError
    public void galat(Session s, Throwable t) { t.printStackTrace(); }

    @OnClose
    public void selesai(Session s) { SEMUA.remove(s); }
}
```

```java
@ClientEndpoint(decoders = PesanDecoder.class)
public class KlienChat {
    @OnOpen  public void buka(Session s) { s.getAsyncRemote().sendText("halo"); }
    @OnMessage public void terima(Pesan p) { System.out.println(p); }
}

WebSocketContainer c = ContainerProvider.getWebSocketContainer();
Session s = c.connectToServer(KlienChat.class, URI.create("ws://localhost:8080/app/chat/umum"));
```

- `getBasicRemote()` sinkron (memblokir), `getAsyncRemote()` mengembalikan `Future`.
- `sendObject` memakai encoder yang terdaftar; `sendText` untuk string mentah.
- Satu instance endpoint per koneksi; field instance aman untuk state per klien, tetapi koleksi statis harus thread-safe.

## Jebakan ujian
- `@OnMessage` bisa menerima `String`, `ByteBuffer`, `PongMessage`, atau tipe kustom dengan decoder - satu endpoint hanya boleh punya satu method per tipe.
- `@OnError` tanpa parameter `Session` juga sah.
- `@PathParam` pada endpoint hanya untuk template di `@ServerEndpoint`.
- Endpoint yang tidak di-deploy sebagai komponen terkelola tidak bisa memakai `@Inject` kecuali didukung container.

## Latihan
1. Method mana yang dipanggil saat klien memutus koneksi?
2. Remote mana yang tidak memblokir thread pengirim?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@OnClose</code>.</p>
<p><b>2.</b> <code>getAsyncRemote()</code>.</p>
</details>
