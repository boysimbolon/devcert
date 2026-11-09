---
title: Merancang, membuat, dan mengubah view
minutes: 22
level: Menengah
badge: lengkap
summary: View yang bisa di-update, ALGORITHM, WITH CHECK OPTION, dan keamanan definer.
objectives:
  - Membuat dan mengubah view
  - Menentukan kapan view bisa di-update
  - Mengatur hak akses lewat definer
---
## Kenapa topik ini diuji
Soal view menguji apakah kamu tahu batasan update dan efek algoritma.

## Konsep inti
```sql
CREATE OR REPLACE VIEW v_pesanan_aktif AS
SELECT p.id, p.total, c.nama
  FROM pesanan p JOIN pelanggan c ON c.id = p.pelanggan_id
 WHERE p.status = 'aktif'
 WITH CHECK OPTION;

ALTER VIEW v_pesanan_aktif AS SELECT ...;
DROP VIEW IF EXISTS v_pesanan_aktif;

SELECT TABLE_NAME, VIEW_DEFINITION, CHECK_OPTION, SECURITY_TYPE
  FROM information_schema.VIEWS WHERE TABLE_SCHEMA='appdb';
```

Aturan yang diuji:

- **Updatable** bila view memetakan satu tabel tanpa agregasi, `DISTINCT`, `GROUP BY`, subquery di SELECT, atau UNION — dengan batasan `INSERT` tidak boleh melewati kolom NOT NULL yang tak terlihat.
- **ALGORITHM=MERGE** (default) menggabungkan definisi ke query; **TEMPTABLE** membuat tabel sementara (tidak updatable).
- **WITH CHECK OPTION** menolak baris yang tidak memenuhi `WHERE` view.
- **SQL SECURITY DEFINER** menjalankan dengan hak pembuat (bisa jadi jalur eskalasi bila sembarangan).

## Jebakan
- View dengan `GROUP BY` tidak bisa di-update.
- Definisi view tidak menyimpan hasil; ia dieksekusi ulang setiap kali dipakai.
- `SQL SECURITY DEFINER` + akses luas = risiko keamanan.
- Menambah kolom tabel tidak otomatis muncul di view (`SELECT *` di view dibekukan saat pembuatan).

## Latihan
1. Apa efek `WITH CHECK OPTION`?
2. Mengapa view dengan agregasi tidak bisa di-update?

<details><summary>Jawaban</summary>
<p><b>1.</b> Menolak INSERT/UPDATE yang menghasilkan baris di luar kondisi <code>WHERE</code> view.</p>
<p><b>2.</b> Karena satu baris view tidak bisa dipetakan kembali ke satu baris tabel dasar.</p>
</details>
