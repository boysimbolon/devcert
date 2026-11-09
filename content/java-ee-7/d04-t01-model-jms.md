---
title: Model Messaging JMS dan Message-Driven Bean
minutes: 24
level: Menengah
badge: lengkap
summary: Queue vs Topic, API JMS 2.0 yang disederhanakan, dan MDB sebagai konsumen asinkron.
objectives:
  - Membedakan point-to-point dan publish/subscribe
  - Menulis produsen dengan JMSContext dan konsumen MDB
  - Memilih acknowledgement dan durable subscription dengan benar
---
## Kenapa topik ini diuji
JMS 2.0 memperkenalkan `JMSContext` yang memangkas kode lama, dan ujian sering membandingkan API klasik dengan yang baru. Soal juga menguji kapan pesan hilang.

## Konsep inti
| Model | Destinasi | Perilaku |
|---|---|---|
| Point-to-point | `Queue` | satu pesan untuk satu konsumen |
| Publish/subscribe | `Topic` | satu pesan untuk semua subscriber aktif |

```java
@Stateless
public class Pengirim {
    @Inject JMSContext context;                       // JMS 2.0, auto-close

    @Resource(lookup = "java:app/jms/AntrianPesanan")
    Queue antrian;

    public void kirim(Pesanan p) {
        context.createProducer()
               .setDeliveryDelay(1000)
               .setProperty("prioritas", p.prioritas())
               .send(antrian, p);
    }
}

@MessageDriven(activationConfig = {
    @ActivationConfigProperty(propertyName = "destinationLookup",
                              propertyValue = "java:app/jms/AntrianPesanan"),
    @ActivationConfigProperty(propertyName = "destinationType",
                              propertyValue = "javax.jms.Queue")
})
public class PemrosesPesanan implements MessageListener {
    @Override public void onMessage(Message m) {
        try {
            Pesanan p = m.getBody(Pesanan.class);
            // proses
        } catch (JMSException e) { throw new EJBException(e); }
    }
}
```

- `JMSContext` mengelola koneksi dan session; dengan CMT, commit mengikuti transaksi EJB.
- Acknowledgement: `AUTO_ACKNOWLEDGE` (default), `CLIENT_ACKNOWLEDGE`, `DUPS_OK_ACKNOWLEDGE`. Dengan transaksi, ack dikendalikan commit.
- Durable subscription untuk topic: subscriber tetap menerima pesan saat offline. Butuh `clientID` dan `subscriptionName`.
- MDB tidak punya tampilan klien, tidak mengembalikan nilai, dan `onMessage` tidak boleh melempar checked exception.

## Jebakan ujian
- Queue mengirim ke **satu** konsumen walau ada tiga MDB mendengarkan; topic mengirim ke **semua** subscriber.
- MDB dengan `@TransactionAttribute(REQUIRED)` akan me-rollback dan me-*redeliver* pesan jika exception runtime - hati-hati pesan berulang.
- `context.send()` pada `JMSContext` yang di-inject tidak perlu `close()`; pada API klasik `Session`/`Connection` wajib.
- `MessageListener` adalah antarmuka `javax.jms.MessageListener`, bukan `jakarta` pada Java EE 7.
- MDB bisa memakai `@Resource MessageDrivenContext` untuk `setRollbackOnly()`.

## Latihan
1. Dua MDB mendengarkan satu queue yang sama. Berapa MDB yang menerima satu pesan?
2. Bagaimana membuat subscriber topic tetap menerima pesan saat sedang mati?

<details><summary>Jawaban</summary>
<p><b>1.</b> Satu, dan pesan terdistribusi antar instance (load balancing).</p>
<p><b>2.</b> Durable subscription: set <code>clientID</code> pada koneksi dan <code>subscriptionName</code> saat membuat consumer.</p>
</details>
