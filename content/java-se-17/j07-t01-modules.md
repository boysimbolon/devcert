---
title: Java Platform Module System
minutes: 24
level: Menengah
badge: lengkap
summary: module-info, requires/exports/opens, provides/uses, dan reflection.
objectives:
  - Menulis module-info.java
  - Membedakan exports dan opens
  - Mendefinisikan service producer dan consumer
---
## Kenapa topik ini diuji
Soal meminta deklarasi modul yang benar untuk kasus tertentu (mis. akses reflection).

## Konsep inti
```java
// module-info.java
module com.app {
    requires java.sql;
    requires transitive com.util;      // diteruskan ke modul yang memakai com.app
    exports com.app.api;               // bisa diakses modul lain
    exports com.app.internal to com.test;
    opens com.app.model to com.fasterxml.jackson.databind;  // reflection
    uses com.app.spi.Plugin;
    provides com.app.spi.Plugin with com.app.impl.PluginImpl;
    requires static lombok;            // compile-time saja
}
```

| Direktif | Arti |
|---|---|
| `requires` | dependensi compile+runtime |
| `requires transitive` | dependensi ikut terlihat oleh pemakai modul |
| `requires static` | opsional saat runtime |
| `exports` | akses tipe publik (compile & runtime) |
| `opens` | akses reflection (runtime) |
| `uses` / `provides ... with` | service loader |

## Jebakan
- `exports` tidak membuka reflection; framework butuh `opens`.
- Tanpa `requires transitive`, pemakai modul bisa gagal compile memakai tipe dari dependensi.
- `opens` tanpa `to` membuka ke semua modul.
- `module-info.java` hanya satu per modul, di root source.

## Latihan
1. Direktif agar library bisa memakai reflection pada paket tertentu?
2. Perbedaan requires dan requires transitive?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>opens paket to modul.library;</code></p>
<p><b>2.</b> <code>transitive</code> meneruskan dependensi sehingga terlihat oleh modul yang bergantung pada modul kita.</p>
</details>
