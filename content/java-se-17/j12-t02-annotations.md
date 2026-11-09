---
title: Anotasi: Override, FunctionalInterface, Deprecated, SuppressWarnings, SafeVarargs
minutes: 18
level: Dasar
badge: lengkap
summary: Anotasi standar yang diuji dan efeknya pada kompilasi.
objectives:
  - Menjelaskan efek tiap anotasi standar
  - Memakai @SafeVarargs dengan benar
  - Menghindari warning yang tidak perlu
---
## Konsep inti
| Anotasi | Efek |
|---|---|
| `@Override` | kompilasi gagal bila bukan override sebenarnya |
| `@FunctionalInterface` | memastikan tepat satu abstract method |
| `@Deprecated` | menandai usang (bisa `since`/`forRemoval`) |
| `@SuppressWarnings("unchecked")` | menekan warning tertentu pada scope |
| `@SafeVarargs` | menandai method var-args generik aman (harus `static`/`final`/`private`) |

```java
@SafeVarargs
static <T> List<T> listOf(T... items) { return List.of(items); }

@SuppressWarnings("unchecked")
List<String> raw(List l) { return (List<String>) l; }
```

## Jebakan
- `@SafeVarargs` pada method non-final/non-static non-private → compile error.
- `@Override` pada static method → compile error (bukan override).
- `@SuppressWarnings` hanya menekan warning, bukan memperbaiki bug.
- Anotasi tanpa `@Retention(RUNTIME)` tidak terlihat via reflection.

## Latihan
1. Syarat method untuk `@SafeVarargs`?
2. Apa efek `@Override` saat signature salah?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>static</code>, <code>final</code>, atau <code>private</code> (Java 9+), dan var-args generik.</p>
<p><b>2.</b> Kompilasi gagal — kesalahan tertangkap lebih awal.</p>
</details>
