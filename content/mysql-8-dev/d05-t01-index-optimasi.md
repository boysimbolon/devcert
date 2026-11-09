---
title: Memakai index untuk optimasi
minutes: 22
level: Menengah
badge: lengkap
summary: Desain index untuk pola query aplikasi, covering index, dan index pada kolom hasil ekspresi.
objectives:
  - Memilih index berdasarkan pola WHERE dan ORDER BY
  - Memanfaatkan covering index
  - Memakai functional index MySQL 8.0
---
## Kenapa topik ini diuji
Soal optimasi developer menekankan pola query, bukan tuning server.

## Konsep inti
```sql
-- equality dulu, lalu kolom urutan
CREATE INDEX idx_pel_tgl ON pesanan (pelanggan_id, tanggal);

-- covering: semua kolom ada di index
CREATE INDEX idx_cover ON pesanan (pelanggan_id, tanggal, total);

-- functional index untuk ekspresi
CREATE INDEX idx_lower_email ON pelanggan ((LOWER(email)));
SELECT * FROM pelanggan WHERE LOWER(email)='budi@contoh.id';
```

Aturan praktis:

- Index membantu `WHERE`, `JOIN`, `ORDER BY`, `GROUP BY` pada kolom yang sama.
- Urutan kolom: kolom dengan `=` lebih dulu, lalu `range`, lalu `ORDER BY`.
- Satu index gabungan biasanya lebih baik daripada beberapa index tunggal.

## Jebakan
- Index tidak dipakai bila kolom dibungkus fungsi.
- `OR` antar kolom berbeda sering mematikan index.
- Terlalu banyak index memperlambat tulis.
- Index pada kolom sangat selektif lebih berguna; kolom boolean jarang membantu.

## Latihan
1. Index untuk `WHERE a=? AND b>? ORDER BY c`?
2. Apa itu covering index?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>(a, b, c)</code> — sesuai urutan akses dan pengurutan.</p>
<p><b>2.</b> Index yang memuat semua kolom yang dibutuhkan query sehingga tabel tidak perlu dibaca.</p>
</details>
