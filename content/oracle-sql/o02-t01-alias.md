---
title: Alias kolom
minutes: 16
level: Dasar
badge: lengkap
summary: Menamai ulang kolom pada keluaran, dengan atau tanpa AS, dan batasan tanda kutip.
objectives:
  - Menulis alias dengan dan tanpa AS
  - Memakai tanda kutip untuk alias dengan spasi
  - Mengetahui di mana alias boleh dipakai
---
## Kenapa topik ini diuji
Soal kecil tapi sering keluar: apakah alias bisa dipakai di WHERE, dan bagaimana menulis alias dengan spasi.

## Konsep inti
```sql
SELECT last_name AS nama, salary * 12 gaji_tahunan
  FROM employees;

SELECT last_name "Nama Lengkap", salary "Gaji (USD)"
  FROM employees;

SELECT salary * 12 AS gaji FROM employees WHERE salary * 12 > 100000;
-- WHERE tidak boleh memakai alias 'gaji'
```

Aturan:

- `AS` opsional; boleh dihilangkan.
- Alias dengan spasi/huruf kecil campur **wajib** tanda kutip ganda.
- Tanpa tanda kutip, alias disimpan huruf besar.
- Alias berguna di `ORDER BY` (boleh), tidak di `WHERE` (tidak boleh).

## Jebakan
- Memakai alias di `WHERE` → ORA-00904 invalid identifier.
- Alias dengan tanda kutip tunggal (`'Nama'`) salah; itu literal string.
- Alias tabel berbeda dari alias kolom.
- Alias tanpa kutip menjadi huruf besar — berpengaruh saat dipakai di aplikasi.

## Latihan
1. Bolehkah alias kolom dipakai di ORDER BY?
2. Bagaimana menulis alias "Total Gaji" yang mengandung spasi?

<details><summary>Jawaban</summary>
<p><b>1.</b> Boleh.</p>
<p><b>2.</b> <code>SELECT salary "Total Gaji" FROM employees;</code></p>
</details>
