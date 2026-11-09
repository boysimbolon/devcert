---
title: Menampilkan hasil query
minutes: 18
level: Dasar
badge: lengkap
summary: Format keluaran, pembatasan baris, dan penyajian data yang terbaca.
objectives:
  - Memformat keluaran CLI
  - Membatasi dan mengurutkan hasil
  - Menyusun keluaran yang siap dipakai laporan
---
## Kenapa topik ini diuji
Soal praktis menanyakan opsi baris perintah atau cara menyusun keluaran.

## Konsep inti
```bash
mysql --table -e "SELECT id, nama FROM pelanggan LIMIT 5"
mysql -e "SELECT * FROM pesanan WHERE id=1\G"          # vertikal
mysql --batch --raw -e "SELECT ..." > hasil.tsv          # tab-separated
mysql --html -e "SELECT ..." > hasil.html
```

```sql
SELECT id, nama, total
  FROM pesanan
 ORDER BY total DESC
 LIMIT 10 OFFSET 20;      -- paginasi
```

Format nilai:

```sql
SELECT id,
       FORMAT(total, 2) AS total_fmt,
       DATE_FORMAT(tanggal, '%d-%m-%Y') AS tgl,
       CONCAT(nama, ' (', kota, ')') AS label
  FROM pesanan;
```

## Jebakan
- `LIMIT` tanpa `ORDER BY` memberi urutan tidak deterministik.
- Paginasi `OFFSET` besar melambat karena tetap memindai baris yang dilewati.
- `--batch` mengubah NULL menjadi `NULL` teks, bukan kosong.
- `\G` hanya untuk CLI, bukan untuk script yang mem-parsing hasil.

## Latihan
1. Opsi untuk keluaran vertikal?
2. Mengapa OFFSET besar lambat?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>\G</code> di akhir pernyataan (atau <code>--vertical</code>).</p>
<p><b>2.</b> Karena server tetap harus membaca dan melewati baris-baris sebelumnya; gunakan keyset pagination (<code>WHERE id &gt; ?</code>).</p>
</details>
