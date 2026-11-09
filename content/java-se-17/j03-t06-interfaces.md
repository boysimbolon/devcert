---
title: Interface, functional interface, method default/static/private
minutes: 22
level: Menengah
badge: lengkap
summary: Aturan method di interface, pewarisan ganda, dan functional interface.
objectives:
  - Menulis default, static, dan private method di interface
  - Menyelesaikan konflik default method
  - Mengenali functional interface
---
## Kenapa topik ini diuji
Konflik dua default method dan aturan `@FunctionalInterface` sering muncul.

## Konsep inti
```java
interface A { default String hi() { return "A"; } }
interface B { default String hi() { return "B"; } }

class C implements A, B {
    public String hi() { return A.super.hi() + B.super.hi(); }  // wajib override
}

@FunctionalInterface
interface Konversi { int ubah(String s); }        // satu abstract method
```

Aturan:
- Method `private` di interface hanya bisa dipanggil dari dalam interface itu.
- `static` interface method tidak diwariskan.
- Field interface selalu `public static final`.
- Functional interface: tepat satu abstract method (default/static tidak dihitung).

## Jebakan
- Tidak meng-override konflik default → compile error.
- `@FunctionalInterface` dengan dua abstract method → compile error.
- Variabel/field di interface tidak bisa diubah nilainya.
- Interface tidak bisa punya constructor dan tidak bisa diinstansiasi.

## Latihan
1. Bagaimana memanggil implementasi default dari interface induk?
2. Berapa abstract method yang boleh dimiliki `@FunctionalInterface`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>NamaInterface.super.method()</code>.</p>
<p><b>2.</b> Tepat satu (method <code>Object</code> tidak dihitung).</p>
</details>
