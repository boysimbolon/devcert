---
title: Exception: try/catch/finally, try-with-resources, multi-catch
minutes: 24
level: Menengah
badge: lengkap
summary: Urutan catch, efek finally, suppressed exception, dan custom exception.
objectives:
  - Memprediksi output saat exception dan finally
  - Memakai try-with-resources dengan benar
  - Menulis exception kustom
---
## Kenapa topik ini diuji
Soal output hampir selalu memuat `finally` dan `return` di dalam try.

## Konsep inti
```java
try {
    System.out.println("try");
    throw new RuntimeException("x");
} catch (IllegalStateException | IllegalArgumentException e) {   // multi-catch
    System.out.println("catch");
} finally {
    System.out.println("finally");
}
```

Try-with-resources:

```java
class R implements AutoCloseable {
    public void close() { System.out.println("close"); }
}
try (R r = new R()) { System.out.println("body"); }
// body, close
```

Resource ditutup **terbalik** urutan pembuatan. Exception saat `close()` menjadi *suppressed* pada exception utama (`getSuppressed()`).

## Jebakan
- Catch subclass sebelum superclass, jika tidak → compile error.
- `finally` dengan `return` menimpa `return` di try.
- `close()` yang melempar exception tidak menggantikan exception utama, tetapi suppressed.
- Checked exception wajib ditangani atau dideklarasikan; `RuntimeException` tidak.

## Latihan
1. Apa efek `return` di `finally`?
2. Bagaimana mengakses exception dari `close()`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Menimpa nilai kembali dari blok <code>try</code>/<code>catch</code>.</p>
<p><b>2.</b> Lewat <code>getSuppressed()</code> pada exception utama.</p>
</details>
