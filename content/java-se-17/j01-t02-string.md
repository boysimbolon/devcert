---
title: String, text block, dan StringBuilder
minutes: 22
level: Dasar
badge: lengkap
summary: Immutability, pool, method penting, dan text block Java 15+.
objectives:
  - Menjelaskan immutability dan string pool
  - Memakai method String yang sering diuji
  - Menulis text block dengan benar
---
## Kenapa topik ini diuji
Soal sering menanyakan output dari rangkaian method String atau kesalahan indentasi text block.

## Konsep inti
```java
String s = "  Java 17  ";
s.trim();                       // hasil dibuang (immutable)
System.out.println(s.length()); // 11
System.out.println(s.trim().length()); // 7

System.out.println("abc".substring(1, 2));   // b  (end exclusive)
System.out.println("a-b-c".split("-").length); // 3
System.out.println(String.join("/", "a", "b")); // a/b

var sb = new StringBuilder("ab");
sb.append(1).insert(1, "X").reverse();
System.out.println(sb);      // "ab" -> "ab1" -> "aXb1" -> "1bXa"
```

Text block:

```java
String json = """
        {
          "id": 1
        }
        """;
```

Aturan text block: dibuka `"""` diikuti newline, indentasi penutup menentukan jumlah spasi yang dibuang, escape `\s` untuk spasi di akhir baris, `\` untuk menyambung baris.

## Jebakan
- `==` membandingkan referensi; gunakan `equals`.
- `String` hasil `+` dengan literal compile-time masuk pool, hasil variabel tidak.
- `strip()` (unicode-aware) vs `trim()` (<= U+0020).
- Text block tanpa newline setelah `"""` pembuka → compile error.

## Latihan
1. Mengapa `s.trim()` tidak mengubah `s`?
2. Apa yang menentukan indentasi akhir text block?

<details><summary>Jawaban</summary>
<p><b>1.</b> String immutable; method mengembalikan objek baru.</p>
<p><b>2.</b> Indentasi baris penutup <code>"""</code> — spasi sekian dibuang dari setiap baris.</p>
</details>
