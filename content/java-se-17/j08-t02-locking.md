---
title: Kode thread-safe dan mekanisme locking
minutes: 24
level: Menengah
badge: lengkap
summary: synchronized, Lock, atomic, dan masalah visibility.
objectives:
  - Menulis critical section dengan benar
  - Membedakan synchronized dan ReentrantLock
  - Menghindari race condition dan deadlock
---
## Kenapa topik ini diuji
Soal menanyakan apakah hasil konsisten dan apa yang mencegah race.

## Konsep inti
```java
class Counter {
    private int nilai;
    synchronized void naik() { nilai++; }             // objek lock = this
    synchronized static void reset() { }              // lock = Class object
}

class Modern {
    private final AtomicInteger n = new AtomicInteger();
    void naik() { n.incrementAndGet(); }

    private final ReentrantLock lock = new ReentrantLock();
    void kerja() {
        lock.lock();
        try { /* critical */ } finally { lock.unlock(); }
    }
}
```

`volatile` menjamin *visibility*, **bukan** atomicity.

## Jebakan
- `nilai++` bukan operasi atomik (baca-ubah-tulis).
- Menyinkronkan dua objek berbeda = tidak saling mengecualikan.
- Lock yang tidak di-unlock di `finally` → deadlock.
- Urutan pengambilan lock berbeda antar thread → deadlock.
- `volatile` pada counter tetap menghasilkan hitungan salah.

## Latihan
1. Mengapa `volatile int` tidak cukup untuk counter?
2. Di mana `unlock()` harus diletakkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena <code>++</code> terdiri dari tiga langkah dan tidak atomik.</p>
<p><b>2.</b> Di blok <code>finally</code> agar selalu dilepas.</p>
</details>
