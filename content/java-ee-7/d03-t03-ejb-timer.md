---
title: EJB Timer Service
minutes: 20
level: Menengah
badge: lengkap
summary: Membuat timer programatik dan kalender, menangani timeout, dan memahami timer persistent.
objectives:
  - Menulis @Schedule dan @Timeout
  - Membuat timer programatik dengan TimerService
  - Menjelaskan perilaku timer persistent saat restart
---
## Kenapa topik ini diuji
Timer adalah satu-satunya mekanisme penjadwalan bawaan Java EE. Soal menanyakan siapa yang membuat thread, apa yang terjadi saat aplikasi restart, dan bagaimana memakai `TimerHandle`.

## Konsep inti
Dua gaya: deklaratif (`@Schedule`/`@Schedules`) dan programatik (`TimerService.createCalendarTimer` / `createSingleActionTimer` / `createIntervalTimer`).

```java
@Singleton
@Startup
public class Penjadwal {

    @Resource TimerService timerService;

    @Schedule(minute = "0", hour = "2", dayOfWeek = "*", persistent = true)
    public void bersihkanHarian(Timer timer) {
        // dipanggil container sesuai jadwal
    }

    public void jadwalkanSekali(long delayMs, String id) {
        timerService.createSingleActionTimer(delayMs, new TimerConfig(id, true));
    }

    @Timeout
    public void padaWaktu(Timer timer) {
        Object info = timer.getInfo();
        if (timer.getTimeRemaining() == 0) { /* sudah waktunya */ }
    }
}
```

- Timer dijalankan oleh thread container, sehingga ikut aturan transaksi EJB (default `REQUIRED`).
- `TimerConfig(persistent=true)` menyimpan timer di DB sehingga bertahan setelah restart; `false` hilang saat JVM mati.
- `TimerHandle` memungkinkan pembatalan dari waktu ke waktu: `timer.cancel()` atau `getHandle().cancel()`.
- Timeout method boleh menerima parameter `Timer`; `@Schedule` menerima parameter apa pun (diabaikan) atau `Timer`.

## Jebakan ujian
- `@Schedule` dengan `persistent = true` membutuhkan dukungan timer store DB; bila tidak, container bisa menolak deploy.
- Timer pada `@Singleton` dengan `@Lock(WRITE)` akan memblokir method lain selama timeout berjalan.
- `TimerService` tidak tersedia di servlet/JSP - hanya di EJB.
- Timer yang dilempar exception tidak otomatis dijadwalkan ulang untuk one-shot.
- Zona waktu: `timezone = "Asia/Jakarta"` pada `@Schedule` mencegah kejutan UTC.

## Latihan
1. Bagaimana memastikan job terhapus saat aplikasi berhenti?
2. Apa parameter tambahan yang boleh diterima method `@Timeout`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Buat timer dengan <code>persistent = false</code>, atau batalkan lewat <code>@PreDestroy</code> dengan <code>timer.cancel()</code>.</p>
<p><b>2.</b> <code>Timer</code> (dan opsional parameter lain yang tidak dipakai) pada <code>@Schedule</code>; pada <code>@Timeout</code> umumnya <code>Timer</code>.</p>
</details>
