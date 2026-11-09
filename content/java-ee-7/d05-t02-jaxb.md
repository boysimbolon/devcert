---
title: Pemetaan Java ke XML dengan JAXB
minutes: 22
level: Menengah
badge: lengkap
summary: Anotasi JAXB, marshalling/unmarshalling, dan kontrol bentuk XML yang dihasilkan.
objectives:
  - Memetakan kelas ke elemen dan atribut XML
  - Melakukan marshal/unmarshal dengan JAXBContext
  - Mengendalikan wrapper koleksi dan field yang diabaikan
---
## Kenapa topik ini diuji
JAXB adalah lapisan di bawah JAX-WS dan JAX-RS. Soal menanyakan bentuk XML yang dihasilkan dari anotasi tertentu - kemampuan membaca anotasi secara mental.

## Konsep inti
```java
@XmlRootElement(name = "pesanan")
@XmlAccessorType(XmlAccessType.FIELD)
public class PesananXml {

    @XmlAttribute(name = "id") private Long id;          // jadi atribut
    @XmlElement(name = "item") private List<Item> item;  // elemen berulang
    @XmlElementWrapper(name = "daftarItem")              // bungkus koleksi
    private List<Item> itemTerbungkus;
    @XmlTransient private String internal;               // tidak dipetakan
    @XmlElement(required = true, nillable = false)
    private String pelanggan;
}

// marshal
JAXBContext ctx = JAXBContext.newInstance(PesananXml.class);
Marshaller m = ctx.createMarshaller();
m.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
m.marshal(pesanan, System.out);

// unmarshal
Unmarshaller u = ctx.createUnmarshaller();
PesananXml p = (PesananXml) u.unmarshal(new File("pesanan.xml"));
```

- `@XmlAccessorType(FIELD)` memetakan field; `PROPERTY` memetakan getter; `PUBLIC_MEMBER` (default) memetakan keduanya - sumber duplikasi elemen.
- `@XmlType(propOrder = {...})` menentukan urutan elemen, penting untuk skema ketat.
- `@XmlElementWrapper` hanya untuk koleksi; tanpa itu koleksi menjadi elemen berulang tanpa pembungkus.
- `xjc` menghasilkan kelas Java dari XSD; `schemagen` sebaliknya.

## Jebakan ujian
- Default `XmlAccessType` adalah `PUBLIC_MEMBER`, bukan `FIELD`.
- `@XmlAttribute` untuk atribut; `@XmlElement` untuk elemen - tertukar berarti kontrak berubah.
- `@XmlTransient` pada getter saja tidak cukup bila field juga dipetakan (tergantung access type).
- `JAXBContext` mahal dibuat; cache dan pakai ulang.
- Kelas hasil `xjc` tidak punya konstruktor tanpa argumen bila skema tidak mendukungnya - unmarshal bisa gagal.

## Latihan
1. Anotasi untuk membungkus `List<Item>` dalam elemen `<daftarItem>`?
2. Access type mana yang mencegah duplikasi antara field dan getter?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@XmlElementWrapper(name = "daftarItem")</code>.</p>
<p><b>2.</b> <code>@XmlAccessorType(XmlAccessType.FIELD)</code> atau <code>PROPERTY</code> - jangan biarkan <code>PUBLIC_MEMBER</code> memetakan keduanya.</p>
</details>
