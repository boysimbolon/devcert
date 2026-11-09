---
title: Standar, Container, API, dan Service Java EE 7
minutes: 20
level: Dasar
badge: lengkap
summary: Peta besar Java EE 7 - apa yang dimaksud container, API, dan service, serta siapa yang mengurus apa.
objectives:
  - Menjelaskan komponen Java EE 7 dan spesifikasi yang menyusunnya (JSR 342)
  - Membedakan container dan tanggung jawabnya
  - Mengenali API mana yang dipakai untuk masalah apa
---
## Kenapa topik ini diuji
Soal pembuka ujian hampir selalu tentang pemetaan: diberikan satu skenario, kamu harus menyebut container atau API mana yang menanganinya. Kalau peta besarnya kabur, soal skenario yang lebih sulit juga ikut jatuh.

## Konsep inti
**Java EE 7 (JSR 342)** adalah kumpulan spesifikasi, bukan satu produk. Ia mendefinisikan kontrak; GlassFish, WildFly, WebLogic, dan Payara adalah implementasinya.

- **Container** menyediakan runtime: lifecycle, thread, transaksi, security, resource pooling. Kode kamu tidak membuat `new Thread()` atau mengelola koneksi DB sendiri.
- **Component** adalah unit kode yang dijalankan container: Servlet, JSP, JSF, EJB, application client.
- **API** adalah spesifikasi pemrograman yang kamu panggil: JPA, JMS, JAX-RS, JAX-WS, CDI, Bean Validation, Batch, Concurrency.
- **Service** adalah fasilitas runtime lintas komponen: transaksi, security, naming/JNDI, resource, messaging.

Profil menentukan paket API yang wajib ada:

| Profil | Isi wajib |
|---|---|
| Full Platform | Semua API Java EE 7, termasuk JMS, JAX-WS, Batch, Concurrency, JCA |
| Web Profile | Servlet, JSP, JSF, JAX-RS, CDI, Bean Validation, JPA, EJB Lite - tanpa JMS, JAX-WS, Batch |

Spesifikasi yang paling sering ditanyakan beserta JSR-nya:

- Servlet 3.1 (JSR 340), JSP 2.3 (JSR 245), JSF 2.2 (JSR 344)
- EJB 3.2 (JSR 345), JPA 2.1 (JSR 338), CDI 1.1 (JSR 346)
- JAX-RS 2.0 (JSR 339), JAX-WS 2.2 (JSR 224), JAXB 2.2 (JSR 222)
- JMS 2.0 (JSR 343), Bean Validation 1.1 (JSR 349), Batch 1.0 (JSR 352), Concurrency 1.0 (JSR 236), WebSocket 1.0 (JSR 356)

```java
// Tidak ada satu pun "new" untuk resource container di sini
@Stateless
public class LaporanService {
    @PersistenceContext(unitName = "appPU")
    EntityManager em;                       // container mengelola EntityManager

    @Resource(lookup = "java:comp/DefaultDataSource")
    DataSource ds;                          // container menyediakan datasource

    public long hitung() {
        return em.createQuery("SELECT COUNT(l) FROM Laporan l", Long.class)
                 .getSingleResult();
    }
}
```

## Jebakan ujian
- Pertanyaan "apakah tersedia di Web Profile?" - JMS, Batch, JAX-WS, dan Concurrency **tidak** termasuk Web Profile.
- "Container mana yang mengelola lifecycle EJB?" - EJB container, bukan web container.
- Jangan tertukar **JSR 342** (Java EE 7 platform) dengan **JSR 338** (JPA 2.1) atau **JSR 345** (EJB 3.2).
- `@Resource` untuk infrastruktur (DataSource, JMSContext, ManagedExecutorService); `@Inject` untuk CDI bean; `@PersistenceContext` khusus EntityManager.

## Latihan
1. Sebuah aplikasi hanya butuh Servlet, JSP, CDI, dan JPA. Profil mana yang paling tepat dan API apa yang harus dihindari?
2. Siapa yang membuat instance `EntityManager` yang di-inject ke EJB?

<details><summary>Jawaban</summary>
<p><b>1.</b> Web Profile. Yang tidak boleh dipakai: JMS, JAX-WS, Batch, dan Concurrency Utilities.</p>
<p><b>2.</b> Container, lewat <code>@PersistenceContext</code>. EntityManager bertipe container-managed proxy; kamu tidak memanggil <code>new</code> atau <code>createEntityManager()</code> di dalam EJB.</p>
</details>
