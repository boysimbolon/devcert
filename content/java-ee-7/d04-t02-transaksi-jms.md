---
title: Transaksi pada JMS API
minutes: 20
level: Menengah
badge: lengkap
summary: Transaksi lokal sesi JMS, transaksi terkelola container, dan pola kirim-terima atomik.
objectives:
  - Menjelaskan transaksi JMS lokal vs CMT
  - Menulis producer/consumer transaksional
  - Menghindari pesan hilang atau diproses ganda saat rollback
---
## Kenapa topik ini diuji
Soal transaksi JMS menguji apakah kamu tahu bahwa commit JMS dan commit database bisa berbeda kecuali digabung dalam satu transaksi global.

## Konsep inti
- **Sesi transaksional (lokal)**: `session = conn.createSession(true, Session.SESSION_TRANSACTED)` lalu `session.commit()/rollback()`. Semua kirim/terima dalam sesi itu satu unit.
- **CMT (global)**: MDB atau session bean dengan transaksi container. Kirim dan terima JMS ikut transaksi XA, bersama operasi DB.
- **BMT**: pakai `UserTransaction`; JMS ikut bergabung bila resource adapter mendukung XA.

```java
@Stateless
public class ProsesPesanan {

    @Resource(lookup = "java:app/jms/AntrianPesanan") Queue masuk;
    @Resource(lookup = "java:app/jms/AntrianSelesai") Queue keluar;
    @Inject JMSContext context;
    @PersistenceContext EntityManager em;

    @TransactionAttribute(TransactionAttributeType.REQUIRED)
    public void terima(Pesanan p) {
        em.persist(p);                                   // DB
        context.createProducer().send(keluar, p.id());   // JMS
        // keduanya commit bersama, atau rollback bersama
    }
}
```

Aturan praktis:

- `SESSION_TRANSACTED` tidak bisa dicampur dengan transaksi container pada sesi yang sama.
- Pada MDB dengan CMT, `onMessage` berjalan dalam transaksi; exception → rollback → pesan dikirim ulang.
- Redelivery bisa berulang tanpa batas kecuali dikonfigurasi (mis. `max-redelivery` pada activation config provider).
- Idempotensi konsumen adalah pertahanan praktis terhadap redelivery.

## Jebakan ujian
- Queue browser tidak mengonsumsi pesan (peek), sedangkan receiver mengonsumsi.
- Bila CMT rollback, pesan yang sudah dikirim dalam transaksi itu ikut dibatalkan.
- `JMSContext.commit()` hanya relevan untuk sesi transaksional yang kamu buat manual di BMT.
- `AUTO_ACKNOWLEDGE` + transaksi: acknowledgement efektif terjadi saat commit, bukan saat `onMessage` selesai.
- Exception checked di `onMessage` tidak boleh; bungkus jadi runtime agar rollback terjadi.

## Latihan
1. MDB melempar `RuntimeException` setelah `em.persist`. Apa yang terjadi pada pesan dan baris DB?
2. Bisakah satu method mengirim 3 pesan dan 1 insert DB secara atomik?

<details><summary>Jawaban</summary>
<p><b>1.</b> Transaksi rollback: baris DB dibatalkan dan pesan dikembalikan ke queue untuk dikirim ulang.</p>
<p><b>2.</b> Bisa, bila ketiganya berjalan dalam satu transaksi CMT/XA yang sama.</p>
</details>
