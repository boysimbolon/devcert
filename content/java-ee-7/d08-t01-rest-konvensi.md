---
title: Konvensi REST dan Desain Resource
minutes: 22
level: Menengah
badge: lengkap
summary: Resource, URI, metode HTTP, status code, dan idempotensi.
objectives:
  - Memetakan operasi CRUD ke metode HTTP
  - Memilih status code yang tepat
  - Menjelaskan idempotensi dan safe method
---
## Kenapa topik ini diuji
Soal skenario REST menanyakan status code dan metode. Ini pengetahuan konvensi, bukan sintaks.

## Konsep inti
| Operasi | Metode | Status sukses | Idempoten |
|---|---|---|---|
| Baca koleksi | GET | 200 | ya |
| Baca satu | GET | 200 / 404 | ya |
| Buat | POST | 201 + `Location` | tidak |
| Ganti utuh | PUT | 200 / 204 | ya |
| Ubah sebagian | PATCH | 200 / 204 | tidak selalu |
| Hapus | DELETE | 204 / 404 | ya |

- Resource adalah kata benda jamak: `/pesanan`, `/pesanan/{id}/item`.
- Jangan menaruh kata kerja di URI; kata kerja adalah metode HTTP.
- HATEOAS menambahkan link relasional di response; opsional untuk ujian tetapi sering disebut.
- Representasi: `application/json`, `application/xml`; konten dinegosiasikan lewat `Accept`.

Status yang sering ditanyakan: 400 (input salah), 401 (belum autentikasi), 403 (terautentikasi tapi tidak berhak), 404, 405 (metode tidak diizinkan), 409 (konflik), 415 (media type tidak didukung), 422 (validasi gagal).

## Jebakan ujian
- `PUT` mengganti seluruh representasi; `PATCH` parsial - soal sering menukar keduanya.
- `POST` tidak idempoten; dua request identik bisa membuat dua resource.
- `DELETE` idempoten: memanggil dua kali hasil akhirnya sama.
- 201 harus menyertakan header `Location`.
- GET tidak boleh mengubah state (safe).

## Latihan
1. Status untuk permintaan POST yang berhasil membuat resource baru?
2. Mana yang idempoten: PATCH atau PUT?

<details><summary>Jawaban</summary>
<p><b>1.</b> 201 Created + <code>Location</code>.</p>
<p><b>2.</b> PUT idempoten; PATCH tidak dijamin.</p>
</details>
