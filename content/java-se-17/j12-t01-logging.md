---
title: Dasar Java Logging API
minutes: 18
level: Dasar
badge: lengkap
summary: Logger, Level, Handler, Formatter, dan hierarki nama logger.
objectives:
  - Membuat Logger dan menetapkan Level
  - Menjelaskan hierarki logger dan handler
  - Menghindari logging yang membocorkan data
---
## Kenapa topik ini diuji
Silabus menyebut "basics of Java Logging API"; soal biasanya tentang level dan hierarki.

## Konsep inti
```java
Logger log = Logger.getLogger("com.app.servis");   // nama hierarkis
log.setLevel(Level.FINE);
log.info("mulai");
log.log(Level.WARNING, "lambat", new RuntimeException("x"));

Handler h = new ConsoleHandler();
h.setFormatter(new SimpleFormatter());
log.addHandler(h);
log.setUseParentHandlers(false);
```

Level (naik): `FINEST, FINER, FINE, CONFIG, INFO, WARNING, SEVERE`. Logger anak mewarisi level/handler induk bila tidak diset.

## Jebakan
- Pesan di bawah level logger tidak diproses sama sekali.
- Handler induk tetap menerima log bila `setUseParentHandlers(true)` (default).
- String concatenation di argumen log mahal; gunakan `log.log(Level.FINE, () -> ...)` atau `{0}`.
- Jangan mencatat password/token.

## Latihan
1. Level default `Logger` tanpa konfigurasi?
2. Bagaimana mencegah log ganda dari handler induk?

<details><summary>Jawaban</summary>
<p><b>1.</b> Mewarisi dari induk; akar biasanya <code>INFO</code>.</p>
<p><b>2.</b> <code>setUseParentHandlers(false)</code>.</p>
</details>
