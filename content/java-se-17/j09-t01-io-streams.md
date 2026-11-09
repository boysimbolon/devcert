---
title: I/O Streams: baca/tulis console dan file
minutes: 22
level: Menengah
badge: lengkap
summary: InputStream/Reader, Buffered, dan console via System.in/out.
objectives:
  - Membedakan byte stream dan character stream
  - Membaca file dengan BufferedReader
  - Menulis file dengan buffered writer
---
## Kenapa topik ini diuji
Soal menanyakan kelas yang tepat dan urutan wrapping stream.

## Konsep inti
```java
try (var br = new BufferedReader(new FileReader("data.txt"))) {
    String line;
    while ((line = br.readLine()) != null) System.out.println(line);
}

try (var bw = new BufferedWriter(new FileWriter("out.txt"))) {
    bw.write("halo");
    bw.newLine();
}

// console
var scanner = new Scanner(System.in);
String nama = scanner.nextLine();
System.out.printf("Halo %s%n", nama);
```

| Kebutuhan | Kelas |
|---|---|
| byte | `InputStream`/`OutputStream` (`FileInputStream`) |
| karakter | `Reader`/`Writer` (`FileReader`) |
| buffering | `Buffered*` |
| data primitif | `DataInputStream`/`DataOutputStream` |

## Jebakan
- `read()` mengembalikan `int` -1 di akhir stream, bukan `byte`.
- Tanpa buffer, I/O per byte sangat lambat.
- `FileReader` memakai charset default platform; gunakan `Files.newBufferedReader` dengan charset eksplisit.
- Menutup inner stream sebelum outer bisa memutus buffer (gunakan try-with-resources berurutan).

## Latihan
1. Nilai kembali `read()` saat EOF?
2. Kelas untuk data primitif biner?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>-1</code>.</p>
<p><b>2.</b> <code>DataInputStream</code>/<code>DataOutputStream</code>.</p>
</details>
