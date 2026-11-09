---
title: Relasi Bean, Anotasi, Injeksi, dan JNDI
minutes: 22
level: Menengah
badge: lengkap
summary: Cara container menemukan dependensi - dari @Inject dan @EJB sampai nama JNDI yang bisa dipanggil manual.
objectives:
  - Membedakan @Inject, @EJB, @Resource, @PersistenceContext
  - Menjelaskan namespace JNDI Java EE 7
  - Menulis lookup JNDI yang benar saat injeksi tidak mungkin
---
## Kenapa topik ini diuji
Soal sering menyodorkan kode yang gagal deploy lalu bertanya penyebabnya. Hampir selalu akar masalahnya salah memilih anotasi injeksi atau salah namespace JNDI.

## Konsep inti
Empat anotasi injeksi dan wilayahnya:

- `@Inject` - CDI. Untuk bean CDI, `@Produces` field, `Event`, dan juga boleh untuk EJB. Butuh `beans.xml` (mode `all` atau `annotated`) pada modul yang memakainya bila tidak ada dekorator/interceptor.
- `@EJB` - menyuntik session bean atau MDB, dengan opsi `name`, `beanName`, `lookup`.
- `@Resource` - menyuntik objek infrastruktur: `DataSource`, `JMSContext`, `Queue`, `ManagedExecutorService`, `UserTransaction`, `SessionContext`.
- `@PersistenceContext` - menyuntik `EntityManager`; `@PersistenceUnit` menyuntik `EntityManagerFactory`.

Namespace JNDI yang harus dihafal:

| Namespace | Cakupan |
|---|---|
| `java:comp/env` | khusus komponen; portabel |
| `java:module` | satu modul |
| `java:app` | satu aplikasi (EAR) |
| `java:global` | seluruh server |
| `java:comp/UserTransaction` | transaksi BMT |
| `java:comp/DefaultDataSource` | datasource default |
| `java:comp/DefaultManagedExecutorService` | executor default |

```java
@Stateless
public class NotifikasiService {

    @Inject  PesanFormatter formatter;                 // CDI bean
    @EJB     AuditService audit;                       // session bean
    @Resource(lookup = "java:comp/DefaultDataSource")
    DataSource ds;                                     // infrastruktur

    @PersistenceContext(unitName = "appPU")
    EntityManager em;

    // Lookup manual: hanya bila injeksi tidak mungkin (mis. kode utilitas statis)
    public void kirim(String teks) throws Exception {
        javax.naming.Context ctx = new javax.naming.InitialContext();
        AuditService a = (AuditService) ctx.lookup("java:app/audit/AuditService");
        a.catat(teks);
    }
}
```

Nama JNDI default sebuah EJB mengikuti pola `java:global/<app>/<module>/<bean>!<interface>` atau bentuk pendek `java:app/<module>/<bean>`. Untuk ujian, cukup ingat urutan namespace dari paling sempit ke paling luas.

## Jebakan ujian
- `@Inject` pada `DataSource` gagal - gunakan `@Resource`.
- `new InitialContext()` di dalam EJB tidak dilarang, tetapi injeksi selalu lebih disukai; soal menanyakan *best practice*, bukan sekadar valid.
- `@EJB` tanpa `name` mengandalkan nama field atau tipe; bentrok tipe berarti butuh `beanName`/`lookup`.
- `beans.xml` kosong cukup untuk mengaktifkan CDI (mode `annotated` di Java EE 7).

## Latihan
1. Anotasi mana untuk menyuntik `JMSContext`?
2. Sebutkan nama JNDI untuk mengambil `UserTransaction` di dalam EJB dengan BMT.

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@Resource</code> (atau <code>@Inject</code> pada <code>JMSContext</code> bila container mendukung injeksi CDI untuk JMS 2.0 - bentuk yang diuji adalah <code>@Resource</code>).</p>
<p><b>2.</b> <code>java:comp/UserTransaction</code>.</p>
</details>
