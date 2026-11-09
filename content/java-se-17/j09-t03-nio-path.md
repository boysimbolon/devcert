---
title: java.nio.file: Path, Files, dan traversal
minutes: 24
level: Menengah
badge: lengkap
summary: Path operations, Files read/write, walk, dan atribut file.
objectives:
  - Membuat dan memanipulasi Path
  - Membaca/menulis file dengan Files
  - Menelusuri direktori
---
## Kenapa topik ini diuji
Soal menanyakan hasil `relativize`, `resolve`, atau `normalize` dan perilaku `Files.copy` saat file ada.

## Konsep inti
```java
Path p = Paths.get("/data/laporan/2026.txt");
System.out.println(p.getFileName());        // 2026.txt
System.out.println(p.getParent());          // /data/laporan
System.out.println(Paths.get("/a/b").relativize(Paths.get("/a/c/d"))); // ../c/d
System.out.println(Paths.get("/a/./b/../c").normalize());              // /a/c

Files.writeString(p, "isi");
String s = Files.readString(p);
Files.copy(p, Paths.get("salin.txt"), StandardCopyOption.REPLACE_EXISTING);
try (var stream = Files.walk(Paths.get("/data"))) {
    stream.filter(Files::isRegularFile).forEach(System.out::println);
}
```

## Jebakan
- `resolve` dengan path absolut mengabaikan base.
- `Files.copy` tanpa opsi gagal bila target ada (`FileAlreadyExistsException`).
- `Files.walk` harus ditutup (Stream) dan butuh `try-with-resources`.
- `delete` pada direktori tidak kosong → `DirectoryNotEmptyException`.
- Path relatif di-resolve terhadap working directory, bukan lokasi kelas.

## Latihan
1. Method untuk menggabungkan path?
2. Opsi agar copy menimpa target?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>resolve()</code>.</p>
<p><b>2.</b> <code>StandardCopyOption.REPLACE_EXISTING</code>.</p>
</details>
