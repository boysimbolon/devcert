---
title: Menghubungkan klausa SELECT dengan komponen ERD
minutes: 20
level: Dasar
badge: lengkap
summary: Entity jadi tabel, relationship jadi join, atribut jadi kolom.
objectives:
  - Memetakan entitas, atribut, dan relasi ke SQL
  - Menentukan join dari kardinalitas relasi
  - Mengenali kolom kunci di ERD
---
## Kenapa topik ini diuji
Soal menyodorkan ERD lalu menanyakan query yang benar untuk menghasilkan laporan tertentu.

## Konsep inti
| ERD | SQL |
|---|---|
| Entity | tabel |
| Attribute | kolom |
| Primary key | `PRIMARY KEY` |
| Foreign key | `FOREIGN KEY` |
| One-to-many | join dari sisi banyak ke kunci induk |
| Many-to-many | tabel perantara + dua join |
| Optional relationship (0..1) | LEFT OUTER JOIN |

Klausa `SELECT` yang dipetakan:

```text
SELECT kolom        <- atribut yang ditampilkan
FROM tabel          <- entitas
WHERE kondisi       <- filter baris (boleh dari relasi)
GROUP BY            <- tingkat ringkasan
HAVING              <- filter hasil agregat
ORDER BY            <- urutan keluaran
```

Contoh ERD: `departments (department_id PK)` dan `employees (employee_id PK, department_id FK)`.

```sql
-- menampilkan departemen beserta jumlah pegawai, termasuk yang kosong
SELECT d.department_name, COUNT(e.employee_id) AS jumlah
  FROM departments d
  LEFT JOIN employees e ON e.department_id = d.department_id
 GROUP BY d.department_name
 ORDER BY jumlah DESC;
```

## Jebakan
- Relasi opsional (0..1) butuh OUTER JOIN; INNER JOIN menghilangkan baris kosong.
- Many-to-many tanpa tabel perantara menghasilkan produk kartesian.
- Memilih kolom yang tidak ada di GROUP BY → error ORA-00979.
- Nama kolom kunci di ERD bisa berbeda dari nama kolom fisik.

## Latihan
1. Relationship one-to-many dipetakan ke join seperti apa?
2. Join apa untuk relasi opsional?

<details><summary>Jawaban</summary>
<p><b>1.</b> Join dari tabel sisi banyak ke primary key sisi satu.</p>
<p><b>2.</b> LEFT OUTER JOIN dari sisi wajib ke sisi opsional.</p>
</details>
