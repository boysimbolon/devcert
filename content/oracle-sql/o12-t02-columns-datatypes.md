---
title: Kolom dan tipe data
minutes: 20
level: Dasar
badge: lengkap
summary: Tipe data Oracle yang umum dan konsekuensinya.
objectives:
  - Memilih tipe data yang tepat
  - Menjelaskan perbedaan CHAR dan VARCHAR2
  - Mengetahui batas tipe
---
## Kenapa topik ini diuji
Soal desain menguji pemilihan tipe: VARCHAR2 vs CHAR vs CLOB, NUMBER presisi, DATE vs TIMESTAMP.

## Konsep inti
| Tipe | Keterangan |
|---|---|
| `CHAR(n)` | panjang tetap, padding spasi |
| `VARCHAR2(n)` | panjang variabel (maks 4000 byte) |
| `NVARCHAR2` | unicode |
| `NUMBER(p,s)` | numerik presisi/skala |
| `DATE` | tanggal + jam (detik) |
| `TIMESTAMP` | dengan pecahan detik |
| `CLOB`/`BLOB` | data besar |
| `RAW` | biner kecil |

```sql
CREATE TABLE contoh (
  kode   CHAR(3),
  nama   VARCHAR2(100),
  harga  NUMBER(10,2),
  dibuat DATE DEFAULT SYSDATE,
  catatan CLOB
);
```

`VARCHAR2` menyimpan hanya sepanjang nilai; `CHAR` selalu memadatkan ke panjang tetap.

## Jebakan
- `VARCHAR` (tanpa 2) sudah deprecated; gunakan `VARCHAR2`.
- `CHAR` membandingkan dengan padding; `'A '` = `'A'` untuk CHAR.
- `NUMBER` tanpa presisi menyimpan float — hati-hati untuk uang.
- `DATE` menyimpan jam; gunakan `TRUNC` untuk membandingkan per hari.

## Latihan
1. Tipe untuk uang?
2. Mengapa CHAR bisa mengejutkan saat perbandingan?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>NUMBER(p,2)</code> (mis. NUMBER(10,2)).</p>
<p><b>2.</b> Karena nilai dipadatkan dengan spasi, sehingga perbandingan mengikuti aturan padding.</p>
</details>
