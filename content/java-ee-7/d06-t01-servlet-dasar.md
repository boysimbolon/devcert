---
title: Servlet, URL Mapping, dan Metode HTTP
minutes: 22
level: Dasar
badge: lengkap
summary: Menulis servlet dengan @WebServlet, memahami pola URL, dan menangani GET/POST dengan benar.
objectives:
  - Membuat servlet dan memetakan URL
  - Menjelaskan aturan prioritas pola URL
  - Menulis doGet/doPost dengan karakter encoding yang benar
---
## Kenapa topik ini diuji
Servlet adalah fondasi semua framework web Java. Soal menguji pemetaan URL (exact vs path vs extension) dan siklus request-response.

## Konsep inti
```java
@WebServlet(name = "produk", urlPatterns = {"/produk", "/produk/*"}, loadOnStartup = 1)
public class ProdukServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, java.io.IOException {
        req.setCharacterEncoding("UTF-8");
        res.setContentType("text/html;charset=UTF-8");
        String id = req.getParameter("id");
        try (var out = res.getWriter()) {
            out.println("<h1>Produk " + (id == null ? "semua" : id) + "</h1>");
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws java.io.IOException {
        req.setCharacterEncoding("UTF-8");
        String nama = req.getParameter("nama");
        res.sendRedirect(req.getContextPath() + "/produk?id=" + nama);
    }
}
```

Aturan pemetaan (dari paling spesifik): exact (`/produk`), path (`/produk/*`), extension (`*.do`), default (`/`). Pola `/` menangkap semua yang tidak cocok dan menonaktifkan default servlet untuk file statis.

- `loadOnStartup >= 0` membuat servlet diinisialisasi saat deploy; `-1` (default) saat request pertama.
- `@WebServlet` dan `web.xml` tidak boleh mendeklarasikan servlet yang sama dengan nama berbeda.
- `sendRedirect` mengirim 302 dan klien membuat request baru; `RequestDispatcher.forward` tetap di server dan URL tidak berubah.

## Jebakan ujian
- `doGet`/`doPost` default memanggil `service()`; menimpa `service()` membuat `doGet` tidak dipanggil.
- `getParameter` pada body `application/x-www-form-urlencoded` hanya terbaca sekali; jangan campur dengan pembacaan `getInputStream()`.
- Encoding harus diset **sebelum** membaca parameter.
- Servlet adalah singleton per deklarasi: field instance dipakai bersama banyak thread - jangan simpan state request di field.
- `sendError(404)` vs `setStatus(404)` berbeda: yang pertama menghasilkan halaman error container.

## Latihan
1. Pola URL mana yang menang bila ada `/produk` dan `/produk/*`?
2. Mengapa menyimpan `HttpServletRequest` di field servlet berbahaya?

<details><summary>Jawaban</summary>
<p><b>1.</b> Exact <code>/produk</code> menang atas path <code>/produk/*</code>.</p>
<p><b>2.</b> Servlet dipakai banyak thread bersamaan; field akan tertimpa request lain (race condition dan kebocoran data).</p>
</details>
