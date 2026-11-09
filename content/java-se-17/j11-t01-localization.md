---
title: Lokalisasi: Locale, ResourceBundle, format
minutes: 22
level: Menengah
badge: lengkap
summary: Locale, resource bundle, pesan, tanggal, dan angka/currency.
objectives:
  - Memilih Locale dan bundle yang tepat
  - Memformat tanggal dan angka per locale
  - Menjelaskan fallback bundle
---
## Kenapa topik ini diuji
Soal menanyakan bundle mana yang dipilih dan hasil format.

## Konsep inti
```java
Locale id = new Locale("id", "ID");             // atau Locale.of("id","ID") di 19+
var bundle = ResourceBundle.getBundle("Messages", id);

NumberFormat nf = NumberFormat.getInstance(id);
System.out.println(nf.format(1234567.89));      // 1.234.567,89

NumberFormat cur = NumberFormat.getCurrencyInstance(id);
System.out.println(cur.format(150000));

DateTimeFormatter f = DateTimeFormatter
    .ofLocalizedDate(FormatStyle.LONG).withLocale(id);
System.out.println(LocalDate.now().format(f));

System.out.println(MessageFormat.format(bundle.getString("halo"), "Bea"));
```

Fallback: `Messages_id_ID` → `Messages_id` → `Messages` (default).

## Jebakan
- `Locale` default JVM memengaruhi `String.format`, `toLowerCase`, dan parsing.
- `ResourceBundle.getBundle` melempar `MissingResourceException` bila bundle dasar tidak ada.
- `NumberFormat` tidak thread-safe; jangan dibagi antar thread.
- Pola tanggal `MM` (bulan) vs `mm` (menit) di `SimpleDateFormat`.

## Latihan
1. Nama file bundle untuk locale id_ID?
2. Apa yang terjadi bila bundle dasar tidak ada?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Messages_id_ID.properties</code>.</p>
<p><b>2.</b> <code>MissingResourceException</code>.</p>
</details>
