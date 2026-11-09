---
title: Menyimpan dan mengolah data temporal
minutes: 22
level: Menengah
badge: lengkap
summary: DATE, DATETIME, TIMESTAMP, zona waktu, dan fungsi tanggal.
objectives:
  - Membedakan DATETIME dan TIMESTAMP
  - Menangani zona waktu dengan benar
  - Memakai fungsi tanggal dan interval
---
## Kenapa topik ini diuji
Perbedaan DATETIME vs TIMESTAMP adalah soal klasik, begitu juga konversi zona waktu.

## Konsep inti
| Tipe | Rentang | Zona waktu |
|---|---|---|
| `DATE` | 1000-01-01 s.d. 9999-12-31 | tidak ada |
| `DATETIME` | 1000-9999 | disimpan apa adanya |
| `TIMESTAMP` | 1970-2038 | **dikonversi** ke UTC saat simpan, ke zona sesi saat baca |
| `TIME` | -838:59:59 s.d. 838:59:59 | durasi |
| `YEAR` | 1901-2155 | — |

```sql
CREATE TABLE acara (
  id INT PRIMARY KEY,
  mulai DATETIME NOT NULL,
  dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

SELECT NOW(), CURDATE(), UTC_TIMESTAMP();
SELECT DATE_ADD(mulai, INTERVAL 7 DAY) AS seminggu;
SELECT TIMESTAMPDIFF(HOUR, mulai, selesai) AS durasi_jam;
SELECT DATE_FORMAT(mulai, '%Y-%m-%d %H:%i') FROM acara;
SELECT * FROM acara WHERE mulai >= '2026-01-01' AND mulai < '2026-02-01';
```

## Jebakan
- `TIMESTAMP` terbatas sampai 2038 — jangan untuk tanggal jauh.
- Mengubah `time_zone` sesi mengubah nilai TIMESTAMP yang dibaca, bukan DATETIME.
- Membandingkan dengan fungsi (`DATE(mulai)=...`) menghalangi index.
- Menyimpan tanggal sebagai string menghasilkan perbandingan leksikografis yang salah.

## Latihan
1. Tipe mana yang berubah nilainya saat zona sesi berubah?
2. Mengapa `WHERE DATE(kolom) = ...` tidak memakai index?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>TIMESTAMP</code> (disimpan UTC, ditampilkan sesuai zona sesi).</p>
<p><b>2.</b> Karena fungsi diterapkan pada kolom; gunakan rentang <code>&gt;= awal AND &lt; akhir</code>.</p>
</details>
