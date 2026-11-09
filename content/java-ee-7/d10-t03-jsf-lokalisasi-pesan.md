---
title: Lokalisasi dan Pesan di JSF
minutes: 20
level: Menengah
badge: lengkap
summary: ResourceBundle, f:loadBundle, Locale, dan FacesMessage.
objectives:
  - Memuat bundle pesan dan mengaksesnya dari EL
  - Mengatur locale per view atau per pengguna
  - Menampilkan dan membuat FacesMessage sendiri
---
## Kenapa topik ini diuji
Soal menanyakan cara menampilkan teks terlokalisasi dan dari mana pesan validasi berasal.

## Konsep inti
```xml
<!-- faces-config.xml -->
<application>
  <resource-bundle>
    <base-name>id.contoh.pesan</base-name>
    <var>msg</var>
  </resource-bundle>
  <locale-config>
    <default-locale>id</default-locale>
    <supported-locale>en</supported-locale>
  </locale-config>
</application>
```

Properties: `pesan_id.properties` dan `pesan_en.properties`.

```xml
<h:outputText value="#{msg.selamat_datang}"/>
<f:view locale="#{sesi.locale}">
  <h:messages globalOnly="false" layout="list"/>
</f:view>
```

```java
FacesContext ctx = FacesContext.getCurrentInstance();
ctx.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR,
        "Gagal", "Stok tidak cukup"));
ctx.getExternalContext().setLocale(new java.util.Locale("en"));
```

- `null` sebagai clientId berarti pesan global.
- `SEVERITY_INFO`, `WARN`, `ERROR`, `FATAL` menentukan styling.
- `h:message for="id"` menampilkan pesan satu komponen.

## Jebakan ujian
- Nama file bundle mengikuti locale: `base_en.properties`, `base_id_ID.properties`.
- `f:loadBundle` per view vs `<resource-bundle>` global di faces-config.
- Pesan validasi default berasal dari bundle JSF, bukan bundle aplikasi.
- `globalOnly="true"` menyembunyikan pesan milik komponen.
- Locale harus di-set sebelum render.

## Latihan
1. Bagaimana mengakses bundle `${msg.x}` tanpa `f:loadBundle`?
2. Client id apa untuk pesan global?

<details><summary>Jawaban</summary>
<p><b>1.</b> Daftarkan <code>&lt;resource-bundle&gt;</code> di <code>faces-config.xml</code> dengan <code>&lt;var&gt;</code>.</p>
<p><b>2.</b> <code>null</code>.</p>
</details>
