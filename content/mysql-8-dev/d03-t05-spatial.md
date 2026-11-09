---
title: Menyimpan dan mengolah data spasial
minutes: 20
level: Menengah
badge: lengkap
summary: Tipe GEOMETRY, SRID, fungsi spatial, dan index spasial.
objectives:
  - Menyimpan titik dan poligon dengan SRID benar
  - Memakai fungsi jarak dan relasi spasial
  - Membuat index spasial
---
## Kenapa topik ini diuji
Fitur spasial sering diabaikan, padahal soalnya cenderung lugas jika tahu fungsinya.

## Konsep inti
```sql
CREATE TABLE lokasi (
  id INT PRIMARY KEY,
  nama VARCHAR(100),
  posisi POINT NOT NULL SRID 4326,
  area POLYGON SRID 4326,
  SPATIAL INDEX (posisi)
);

INSERT INTO lokasi (id, nama, posisi)
VALUES (1, 'Kantor', ST_GeomFromText('POINT(106.8456 -6.2088)', 4326));

SELECT nama, ST_Distance_Sphere(posisi, ST_GeomFromText('POINT(106.9 -6.2)', 4326)) AS meter
  FROM lokasi
 ORDER BY meter LIMIT 5;

SELECT ST_Contains(area, ST_GeomFromText('POINT(106.8 -6.2)', 4326)) FROM lokasi;
```

Fungsi penting: `ST_GeomFromText`, `ST_AsText`, `ST_Distance_Sphere`, `ST_Contains`, `ST_Within`, `ST_Intersects`, `ST_Buffer`, `ST_Area`.

## Jebakan
- SRID berbeda antar kolom → error perbandingan.
- Index spasial hanya untuk kolom `NOT NULL` (di InnoDB) — perhatikan definisi.
- `ST_Distance` memakai satuan derajat; untuk meter gunakan `ST_Distance_Sphere`.
- Poligon harus tertutup (titik awal = titik akhir).

## Latihan
1. Fungsi untuk jarak dalam meter?
2. Mengapa kolom spasial sebaiknya NOT NULL untuk index?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ST_Distance_Sphere</code>.</p>
<p><b>2.</b> Karena index spasial InnoDB mensyaratkan kolom <code>NOT NULL</code>.</p>
</details>
