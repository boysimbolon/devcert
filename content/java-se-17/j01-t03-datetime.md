---
title: Date-Time API
minutes: 24
level: Menengah
badge: lengkap
summary: LocalDate, Instant, ZonedDateTime, Duration, Period, dan formatter.
objectives:
  - Memilih tipe waktu yang tepat
  - Melakukan aritmetika tanggal dengan benar
  - Memformat dan mem-parse tanggal
---
## Kenapa topik ini diuji
Soal memberi rantai method (`plusDays`, `with`, `atStartOfDay`) dan menanyakan hasilnya.

## Konsep inti
| Kelas | Isi |
|---|---|
| `LocalDate` | tanggal tanpa waktu/zona |
| `LocalTime` | jam tanpa tanggal |
| `LocalDateTime` | keduanya, tanpa zona |
| `ZonedDateTime` | + zona (aturan DST) |
| `Instant` | titik waktu UTC |
| `Duration` | selisih waktu (jam/menit/detik) |
| `Period` | selisih tanggal (tahun/bulan/hari) |

```java
var d = LocalDate.of(2026, 2, 28);
System.out.println(d.plusDays(1));       // 2026-03-01
System.out.println(d.plusMonths(1));     // 2026-03-28
System.out.println(d.withMonth(1).lengthOfMonth()); // 31

var z = ZonedDateTime.of(2026, 3, 29, 1, 30, 0, 0, ZoneId.of("Europe/Berlin"));
System.out.println(z.plusHours(1));      // lompat ke 03:30 (DST)

Duration dur = Duration.ofMinutes(90);
System.out.println(dur.toHours());       // 1
Period p = Period.of(1, 2, 3);
```

## Jebakan
- `LocalDate` immutable: hasil method harus ditampung.
- `Period` menambah bulan lalu menyesuaikan akhir bulan (31 Jan + 1 bulan = 28/29 Feb).
- `Duration` tidak bisa dipakai pada `LocalDate` (tanpa waktu) → `UnsupportedTemporalTypeException`.
- Format `yyyy` (year-of-era) vs `uuuu` (proleptic year) penting saat `parse`.
- `DateTimeFormatter` dengan pola salah → `DateTimeParseException`.

## Latihan
1. Kelas untuk selisih 3 hari 4 jam?
2. Mengapa `LocalDate.plus(Duration.ofHours(1))` gagal?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Duration</code> untuk jam, <code>Period</code> untuk tanggal; 3 hari 4 jam biasanya dihitung lewat <code>Duration</code> bila ada waktu.</p>
<p><b>2.</b> Karena <code>LocalDate</code> tidak mendukung satuan waktu (jam).</p>
</details>
