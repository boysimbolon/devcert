---
title: Penanganan Error di Servlet dan JSP
minutes: 20
level: Menengah
badge: lengkap
summary: error-page, exception handler, dan pola logging yang benar.
objectives:
  - Mengonfigurasi halaman error per kode status dan per exception
  - Menulis error page JSP yang aman
  - Menentukan kapan memakai sendError vs throw
---
## Kenapa topik ini diuji
Error handling adalah soal "apa yang dilihat pengguna". Jebakan klasik: stack trace bocor ke browser.

## Konsep inti
```xml
<!-- web.xml -->
<error-page>
  <error-code>404</error-code>
  <location>/error/404.html</location>
</error-page>
<error-page>
  <exception-type>java.lang.Throwable</exception-type>
  <location>/error/500.jsp</location>
</error-page>
```

```jsp
<%@ page isErrorPage="true" contentType="text/html;charset=UTF-8" %>
<% response.setStatus(500); %>
<h1>Terjadi kesalahan</h1>
<p>Kode: ${pageContext.errorData.statusCode}</p>
<%-- exception tersedia lewat implicit object exception --%>
```

Aturan praktis:

- `sendError(404)` memberitahu container agar memakai halaman error untuk kode itu.
- Melempar exception dari servlet memicu halaman error `exception-type`.
- `isErrorPage="true"` memberi akses implicit object `exception`.
- Jangan pernah menampilkan stack trace ke pengguna; catat ke log.

## Jebakan ujian
- Bila response sudah di-commit (`flushBuffer`), `sendError` tidak berpengaruh lagi.
- Error page untuk `Throwable` menangkap semua, jadi taruh yang paling spesifik lebih dulu (urutan penting).
- `errorPage` pada directive JSP hanya berlaku untuk JSP itu, bukan seluruh aplikasi.
- Status 500 vs 404: `sendError(404)` mengubah status, `setStatus(404)` tidak memakai halaman error.
- Error dalam filter tetap memicu error page bila response belum commit.

## Latihan
1. Apa yang terjadi bila `sendError` dipanggil setelah output di-flush?
2. Atribut JSP apa yang membuat objek `exception` tersedia?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak berefek; response sudah terkirim ke klien.</p>
<p><b>2.</b> <code>isErrorPage="true"</code> pada directive page.</p>
</details>
