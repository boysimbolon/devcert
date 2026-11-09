---
title: Header, Parameter, dan Cookie
minutes: 22
level: Dasar
badge: lengkap
summary: Membaca input HTTP dan mengelola session vs cookie, termasuk atribut keamanan.
objectives:
  - Membaca parameter, header, dan body multipart
  - Membedakan cookie dan HttpSession
  - Mengatur atribut cookie yang aman
---
## Kenapa topik ini diuji
Soal menguji sumber data mana yang muncul di mana: query string, form body, header, cookie. Salah membaca sumber = nilai null.

## Konsep inti
```java
@WebServlet("/profil")
public class ProfilServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws java.io.IOException {
        String nama = req.getParameter("nama");            // query string atau form body
        String agent = req.getHeader("User-Agent");        // header
        String kunci = req.getHeader("X-Api-Key");

        Cookie c = new Cookie("tema", "gelap");
        c.setHttpOnly(true);
        c.setSecure(true);
        c.setPath("/");
        c.setMaxAge(60 * 60 * 24 * 30);                    // 30 hari
        res.addCookie(c);

        HttpSession sesi = req.getSession(true);           // buat bila belum ada
        sesi.setAttribute("user", nama);
        sesi.setMaxInactiveInterval(1800);                 // detik
    }
}
```

- `HttpSession` disimpan di server, ditautkan ke klien lewat cookie `JSESSIONID` (atau URL rewriting).
- Cookie disimpan di klien; isinya bisa dimanipulasi, jadi jangan simpan data sensitif.
- `getSession(false)` mengembalikan `null` bila belum ada sesi; `getSession()` membuat baru.
- Multipart: `@MultipartConfig` pada servlet, lalu `req.getPart("file")`.

```java
@WebServlet("/unggah")
@MultipartConfig(maxFileSize = 5 * 1024 * 1024, maxRequestSize = 10 * 1024 * 1024)
public class UnggahServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws Exception {
        Part p = req.getPart("berkas");
        p.write("/var/data/" + p.getSubmittedFileName());
    }
}
```

## Jebakan ujian
- `getParameter` tidak membaca header; dan tidak membaca JSON body.
- `setMaxAge(0)` menghapus cookie; `-1` berarti cookie sesi browser.
- `HttpOnly` mencegah akses JavaScript, `Secure` membatasi ke HTTPS, `SameSite` mencegah CSRF.
- `invalidate()` menghapus seluruh isi sesi; `removeAttribute` hanya satu atribut.
- URL rewriting (`;jsessionid=`) dipakai bila cookie dimatikan - risiko kebocoran id di log.

## Latihan
1. Di mana `JSESSIONID` disimpan dan siapa yang memilikinya?
2. Atribut cookie apa untuk mencegah pencurian lewat XSS?

<details><summary>Jawaban</summary>
<p><b>1.</b> Di klien (cookie), tetapi data sesi tetap di server; id-nya hanya kunci.</p>
<p><b>2.</b> <code>HttpOnly</code> (plus <code>Secure</code> untuk HTTPS).</p>
</details>
