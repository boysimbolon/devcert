---
title: Compile, jar modular, runtime image, dan migrasi
minutes: 22
level: Menengah
badge: lengkap
summary: javac, jar, jlink, jdeps, dan peran unnamed/automatic module.
objectives:
  - Menghasilkan jar modular dan non-modular
  - Membuat runtime image dengan jlink
  - Menjelaskan unnamed dan automatic module
---
## Kenapa topik ini diuji
Soal menanyakan perintah atau konsekuensi migrasi classpath → module path.

## Konsep inti
```bash
javac -d out --module-source-path src $(find src -name "*.java")
jar --create --file app.jar --main-class com.app.Main -C out/com.app .
jar --describe-module --file app.jar

jlink --module-path $JAVA_HOME/jmods:mods --add-modules com.app \
      --output image --launcher app=com.app/com.app.Main

jdeps --module-path mods --check com.app   # deteksi dependensi
```

| Jenis | Ciri |
|---|---|
| Named module | punya `module-info.class` di module path |
| Automatic module | jar tanpa `module-info` di module path; nama dari `Automatic-Module-Name` atau nama file |
| Unnamed module | semua isi classpath; membaca semua modul, tidak mengekspor |

## Jebakan
- Jar tanpa `module-info` di module path menjadi automatic module — semua paket diekspor.
- Kelas di classpath (unnamed) tidak bisa di-`requires` oleh named module.
- `jlink` hanya bisa memakai modul, bukan jar classpath.
- `jar --describe-module` untuk memeriksa isi modul sebelum migrasi.

## Latihan
1. Apa yang terjadi pada jar tanpa module-info di module path?
2. Alat untuk membuat runtime image minimal?

<details><summary>Jawaban</summary>
<p><b>1.</b> Menjadi automatic module yang mengekspor semua paket.</p>
<p><b>2.</b> <code>jlink</code>.</p>
</details>
