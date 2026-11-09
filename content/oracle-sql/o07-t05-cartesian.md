---
title: Produk kartesian
minutes: 16
level: Dasar
badge: lengkap
summary: Apa yang terjadi saat join tanpa kondisi, dan cara mengenalinya.
objectives:
  - Menjelaskan produk kartesian
  - Mengenali penyebabnya
  - Menghindari hasil yang meledak
---
## Kenapa topik ini diuji
Soal klasik: query menghasilkan 1400 baris padahal tabelnya 14 dan 100 — itu produk kartesian.

## Konsep inti
Produk kartesian = setiap baris tabel A digabung dengan setiap baris tabel B → jumlah baris = A × B.

```sql
-- tanpa kondisi join
SELECT e.last_name, d.department_name
  FROM employees e, departments d;      -- 107 x 27 baris

-- CROSS JOIN eksplisit
SELECT e.last_name, d.department_name
  FROM employees e CROSS JOIN departments d;
```

Penyebab umum: lupa `ON`/`WHERE`, kondisi join salah (kolom tidak berelasi), atau join ke tabel tanpa kunci.

## Jebakan
- Produk kartesian tidak selalu error — hasilnya hanya sangat besar dan salah.
- `CROSS JOIN` kadang disengaja (mis. membuat kombinasi tanggal × produk).
- Kondisi join yang menggunakan operator non-equijoin bisa menghasilkan banyak baris tanpa terlihat seperti kartesian.
- Join lima tabel tanpa kondisi bisa menghabiskan TEMP tablespace.

## Latihan
1. Berapa baris hasil 10 × 40 tabel tanpa kondisi?
2. Bagaimana mengenali produk kartesian tak sengaja?

<details><summary>Jawaban</summary>
<p><b>1.</b> 400 baris.</p>
<p><b>2.</b> Jumlah baris hasil sama dengan hasil kali jumlah baris tabel, dan nilainya tidak berelasi secara logis.</p>
</details>
