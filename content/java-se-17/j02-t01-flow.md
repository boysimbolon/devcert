---
title: Kontrol alur: if/else, switch, loop
minutes: 22
level: Dasar
badge: lengkap
summary: switch statement vs switch expression, label, dan aturan break/continue.
objectives:
  - Menulis switch expression dengan yield
  - Menghindari fall-through yang tidak diinginkan
  - Menggunakan label pada loop bersarang
---
## Kenapa topik ini diuji
Switch expression adalah fitur Java 14+ dan paling sering muncul di soal output.

## Konsep inti
```java
int day = 3;
String type = switch (day) {
    case 1, 2, 3, 4, 5 -> "kerja";
    case 6, 7 -> { yield "libur"; }
    default -> throw new IllegalArgumentException("?");
};

// switch statement klasik dengan fall-through
switch (day) {
    case 1:
    case 2:
        System.out.println("awal pekan");
        break;
    default:
        System.out.println("lain");
}
```

```java
outer:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) continue outer;
        System.out.print(i + "" + j + " ");
    }
}
// 00 10 20
```

## Jebakan
- Switch expression wajib *exhaustive*: butuh `default` untuk non-enum/non-sealed, atau semua konstanta enum.
- Panah (`->`) tidak fall-through; titik dua (`:`) fall-through.
- `yield` hanya di dalam blok `{}` switch expression.
- `case null ->` hanya boleh di switch expression/statement dengan pola (Java 21+) — di Java 17 tidak didukung.
- Variabel di switch expression harus `final`/efektif final bila dipakai.

## Latihan
1. Kapan `yield` diperlukan?
2. Apa efek `continue outer`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Saat cabang switch expression memakai blok dan menghasilkan nilai.</p>
<p><b>2.</b> Melewati sisa iterasi loop luar dan melanjutkan ke iterasi berikutnya.</p>
</details>
