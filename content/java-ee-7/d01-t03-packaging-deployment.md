---
title: Membuat, Memaketkan, dan Men-deploy Aplikasi
minutes: 25
level: Menengah
badge: lengkap
summary: WAR, EJB JAR, EAR, RAR - kapan dipakai, isi descriptor, dan bagaimana classloader melihatnya.
objectives:
  - Memilih tipe arsip yang tepat untuk komponen tertentu
  - Menulis web.xml dan application.xml minimal
  - Menjelaskan urutan classloading dan isolasi modul
---
## Kenapa topik ini diuji
Banyak kandidat hafal anotasi tapi gagal soal struktur: file apa ada di mana, dan mengapa sebuah kelas tidak ditemukan saat deploy. Ujian menanyakan isi arsip dan kebutuhan descriptor.

## Konsep inti
| Arsip | Isi | Kapan dipakai |
|---|---|---|
| WAR | Servlet, JSP, JSF, static, `WEB-INF/classes`, `WEB-INF/lib` | aplikasi web |
| EJB JAR | Session bean, MDB, `META-INF/ejb-jar.xml` | komponen bisnis reusable |
| EAR | Satu atau lebih WAR/EJB JAR/RAR + `META-INF/application.xml` | aplikasi enterprise multi-modul |
| RAR | Resource adapter JCA + `META-INF/ra.xml` | integrasi sistem eksternal |

Aturan lokasi yang sering ditanyakan:

- `WEB-INF/` tidak dapat diakses langsung lewat URL - ini yang membuatnya tempat aman untuk konfigurasi.
- `WEB-INF/classes` berisi kelas hasil kompilasi, `WEB-INF/lib` berisi JAR dependensi.
- Servlet tidak boleh dideklarasikan sebagai kelas publik di root WAR dan diakses lewat URL statis.
- Pada EAR, tiap modul punya classloader sendiri; kelas di `EAR/lib` dipakai bersama.

```xml
<!-- src/main/webapp/WEB-INF/web.xml -->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="3.1">
  <display-name>toko</display-name>
  <welcome-file-list>
    <welcome-file>index.xhtml</welcome-file>
  </welcome-file-list>
  <error-page>
    <error-code>404</error-code>
    <location>/404.xhtml</location>
  </error-page>
</web-app>
```

```xml
<!-- META-INF/application.xml -->
<application xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="7">
  <module><web><web-uri>toko.war</web-uri><context-root>/toko</context-root></web></module>
  <module><ejb>toko-ejb.jar</ejb></module>
</application>
```

Sejak Java EE 6/7, `web.xml` dan `ejb-jar.xml` **opsional** bila semua konfigurasi memakai anotasi. `application.xml` juga opsional untuk EAR sederhana, tetapi context root dan urutan modul lebih jelas bila ditulis.

## Jebakan ujian
- `WEB-INF/lib` untuk JAR dependensi aplikasi; JDBC driver boleh di sana atau sebagai resource container, keduanya sah.
- Satu EAR bisa memuat beberapa WAR dengan context root berbeda.
- `META-INF/context.xml` bukan standar Java EE - itu khusus Tomcat.
- Deploy ulang tanpa `undelpoy` bisa menyisakan session lama; ujian memakai istilah *redeploy*.

## Latihan
1. Di mana `persistence.xml` diletakkan untuk persistence unit yang dipakai EJB JAR di dalam EAR?
2. Apa akibatnya bila dua WAR dalam satu EAR mendefinisikan kelas dengan nama paket sama?

<details><summary>Jawaban</summary>
<p><b>1.</b> Di <code>META-INF/persistence.xml</code> dalam EJB JAR (atau di <code>WEB-INF/classes/META-INF</code> untuk unit yang didefinisikan web module).</p>
<p><b>2.</b> Tidak bentrok selama classloader modul terisolasi, tetapi kelas di <code>EAR/lib</code> dipakai bersama sehingga definisi ganda di sana menimpa.</p>
</details>
