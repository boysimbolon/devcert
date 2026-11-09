---
title: Lifecycle dan Scope EJB serta CDI Bean
minutes: 25
level: Menengah
badge: lengkap
summary: Kapan instance dibuat, kapan dihancurkan, dan callback apa yang dipanggil - termasuk perbedaan scope CDI dan EJB.
objectives:
  - Menjelaskan lifecycle stateless, stateful, singleton, dan MDB
  - Memilih scope CDI yang tepat untuk kebutuhan state
  - Menempatkan @PostConstruct dan @PreDestroy dengan benar
---
## Kenapa topik ini diuji
Ini topik favorit pembuat soal: satu skenario, kamu harus menentukan bean apa yang menyimpan state, dan callback mana yang jalan. Salah paham lifecycle hampir selalu berujung bug produksi berupa data tercampur antar pengguna.

## Konsep inti
**Session bean**

- `@Stateless` - instance dari pool, tidak menyimpan state antar pemanggilan; satu instance bisa melayani banyak klien bergantian.
- `@Stateful` - satu instance per klien, state bertahan sampai `@Remove` atau timeout; ada `@PostActivate`/`@PrePassivate` saat passivation.
- `@Singleton` - satu instance per JVM per aplikasi; `@Startup` membuatnya saat deploy, `@DependsOn` menentukan urutan.
- `@MessageDriven` - satu instance per pesan yang diproses (dari pool), tidak punya state klien.

**Scope CDI**

| Scope | Hidup selama | Catatan |
|---|---|---|
| `@Dependent` | mengikuti objek yang meng-inject | default bila tidak ada anotasi scope |
| `@RequestScoped` | satu request HTTP | aman untuk data per-permintaan |
| `@SessionScoped` | satu HttpSession | dipakai untuk keranjang belanja, login info |
| `@ApplicationScoped` | satu aplikasi | singleton gaya CDI, proxy |
| `@ConversationScoped` | satu conversation eksplisit | butuh `Conversation.begin()/end()` |
| `@Singleton` (EJB) | satu per aplikasi | bukan scope CDI, tidak punya proxy |

```java
@Stateful
public class KeranjangBean implements Keranjang {
    private final List<String> item = new ArrayList<>();

    @PostConstruct void init() { System.out.println("siap"); }   // setelah injeksi
    @PreDestroy    void tutup() { System.out.println("dibuang"); } // sebelum dihancurkan
    @PrePassivate  void diamkan() { }   // hanya stateful, sebelum passivation
    @PostActivate  void bangunkan() { } // hanya stateful, setelah activation

    public void tambah(String s) { item.add(s); }
    @Remove public void selesai() { item.clear(); }  // instance dihancurkan
}

@ApplicationScoped   // CDI: satu instance, diakses lewat proxy
public class Konfigurasi { }

@RequestScoped       // CDI: satu per request
public class HalamanInfo { }
```

## Jebakan ujian
- `@PostConstruct` jalan **setelah** dependency injection; konstruktor jalan sebelum injeksi - jangan akses injected field di konstruktor.
- `@PreDestroy` tidak dijamin dipanggil pada `@Stateless` saat pool menyusut; jangan taruh logika bisnis kritis di sana.
- `@Singleton` EJB bukan scope CDI; `@ApplicationScoped` adalah padanan CDI-nya, dan bedanya: CDI memakai proxy sehingga inject ke objek lain tetap aman.
- `@Stateful` yang tidak pernah memanggil `@Remove` akan dipassivate lalu dihapus setelah timeout.
- `@Dependent` membuat instance baru setiap kali di-inject; pada `@Stateless` ini bisa berarti banyak instance.

## Latihan
1. Sebuah bean menyimpan pilihan filter pencarian milik satu pengguna selama sesi login. Scope apa yang tepat?
2. Mengapa mengakses field hasil `@Inject` di dalam konstruktor berbahaya?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@SessionScoped</code> (CDI) atau <code>@Stateful</code> bila butuh transaksi per klien.</p>
<p><b>2.</b> Injeksi terjadi setelah konstruktor; field masih <code>null</code>. Gunakan <code>@PostConstruct</code>.</p>
</details>
