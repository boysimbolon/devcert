---
title: Komponen per Tier dan Container
minutes: 20
level: Dasar
badge: lengkap
summary: Membedakan web component, business component, dan client component serta container yang menjalankannya.
objectives:
  - Memetakan komponen ke tier (presentation, business, integration, client)
  - Menentukan container yang menjalankan tiap komponen
  - Menjelaskan konsekuensi salah menempatkan logika
---
## Kenapa topik ini diuji
Soal tipe "komponen mana untuk tugas X" menguji keputusan arsitektur. Ujian ingin memastikan kamu tidak menaruh transaksi database di JSP atau memanggil EntityManager dari application client.

## Konsep inti
| Tier | Komponen | Container | Tanggung jawab |
|---|---|---|---|
| Client | Application client, applet (deprecated) | Application client container | UI desktop, akses remote ke EJB |
| Presentation | Servlet, JSP, JSF, WebSocket endpoint | Web container | HTTP, session, rendering |
| Business | Session bean, MDB | EJB container | transaksi, security, concurrency, messaging |
| Integration | JCA adapter, resource | EJB container | koneksi ke sistem eksternal |
| Persistence | Entity (JPA) | dikelola EJB/persistence provider | pemetaan objek ke tabel |

Aturan praktis yang dipakai ujian:

- **Web container tidak punya transaksi container-managed untuk method servlet.** Transaksi CMT hadir di session bean dan MDB.
- **Entity bukan komponen** yang punya lifecycle container sendiri; ia objek biasa yang dikelola EntityManager.
- **Application client** boleh memakai `@Inject` (CDI) dan memanggil EJB remote, tetapi tidak menjalankan servlet.
- **JSF** adalah framework presentasi di atas Servlet; managed bean-nya hidup di web container (atau CDI container pada Java EE 7).

```java
@Stateless                      // business tier
public class PesananService {
    @PersistenceContext EntityManager em;

    @TransactionAttribute(TransactionAttributeType.REQUIRED)
    public void simpan(Pesanan p) { em.persist(p); }
}

@WebServlet("/pesanan")         // presentation tier
public class PesananServlet extends HttpServlet {
    @EJB PesananService service; // memanggil business tier, bukan DB langsung

    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws java.io.IOException {
        service.simpan(new Pesanan(req.getParameter("item")));
        res.sendRedirect("daftar");
    }
}
```

## Jebakan ujian
- Servlet memanggil service EJB, bukan `EntityManager` langsung - kecuali memang ada persistence unit di web module dan itu bukan pola yang diuji.
- `@EJB` untuk menyuntik session bean; `@Inject` juga bisa (CDI) tetapi `@EJB` yang eksplisit untuk EJB.
- MDB tidak punya tampilan klien sama sekali: ia didorong pesan, bukan request HTTP.
- Komponen yang punya lifecycle callback container sendiri: servlet, filter, EJB, MDB, WebSocket endpoint.

## Latihan
1. Di mana `@TransactionAttribute` berlaku dan di mana tidak?
2. Komponen apa yang paling tepat untuk memproses pesan dari queue tanpa klien menunggu?

<details><summary>Jawaban</summary>
<p><b>1.</b> Hanya pada method bisnis session bean / MDB (business tier). Tidak berlaku pada method servlet atau JSF managed bean.</p>
<p><b>2.</b> Message-driven bean (MDB) di EJB container - asinkron, tidak punya antarmuka klien.</p>
</details>
