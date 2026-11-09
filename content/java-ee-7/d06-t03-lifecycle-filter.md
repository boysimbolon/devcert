---
title: Lifecycle Servlet, Filter, dan Listener
minutes: 24
level: Menengah
badge: lengkap
summary: Urutan init-service-destroy, rantai filter, dan listener yang tepat untuk tiap event.
objectives:
  - Menjelaskan urutan lifecycle servlet dan filter
  - Menulis filter yang mengubah request/response
  - Memilih listener untuk inisialisasi aplikasi
---
## Kenapa topik ini diuji
Soal memberi kode dengan beberapa komponen lalu menanyakan urutan eksekusi. Ini murni pemahaman lifecycle.

## Konsep inti
Urutan untuk satu request:

1. Filter `doFilter` (pre) - sesuai `@WebFilter`/urutan `web.xml`
2. Servlet `service()` → `doGet`/`doPost`
3. Filter (post) setelah `chain.doFilter` kembali
4. Response dikirim

```java
@WebFilter(urlPatterns = "/*", dispatcherTypes = {DispatcherType.REQUEST})
public class AuthFilter implements Filter {

    public void init(FilterConfig cfg) { }             // sekali saat deploy

    public void doFilter(ServletRequest rq, ServletResponse rs, FilterChain chain)
            throws java.io.IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) rq;
        if (req.getSession(false) == null) {
            ((HttpServletResponse) rs).sendRedirect(req.getContextPath() + "/login");
            return;                                     // tidak memanggil chain = stop
        }
        chain.doFilter(rq, rs);                         // lanjut ke filter/servlet berikutnya
    }

    public void destroy() { }
}
```

Listener yang sering diuji:

| Listener | Event |
|---|---|
| `ServletContextListener` | aplikasi start/stop |
| `HttpSessionListener` | sesi dibuat/dihancurkan |
| `ServletRequestListener` | request masuk/keluar |
| `ServletContextAttributeListener` | atribut context berubah |

```java
@WebListener
public class StartApp implements ServletContextListener {
    public void contextInitialized(ServletContextEvent e) {
        e.getServletContext().setAttribute("started", System.currentTimeMillis());
    }
}
```

## Jebakan ujian
- Filter berjalan untuk forward/include hanya bila `dispatcherTypes` mencantumkannya (`FORWARD`, `INCLUDE`, `ERROR`, `ASYNC`).
- `chain.doFilter` wajib dipanggil bila ingin request lanjut; lupa memanggil = response kosong.
- `init(ServletConfig)` vs `init()`: menimpa yang tanpa parameter lebih aman; container memanggil `init(config)` yang memanggil `init()`.
- `destroy()` tidak menjamin penyimpanan state; hanya kesempatan membersihkan resource.
- `@WebFilter` tidak bisa dipetakan ke `/*` bersamaan dengan filter lain tanpa memperhatikan urutan alfabetis nama di `web.xml`.

## Latihan
1. Di mana tempat terbaik menginisialisasi connection pool ringan?
2. Apakah filter jalan untuk `RequestDispatcher.forward` secara default?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ServletContextListener.contextInitialized</code>, bukan <code>@PostConstruct</code> servlet (yang bergantung pada loadOnStartup).</p>
<p><b>2.</b> Tidak, kecuali <code>dispatcherTypes</code> menyertakan <code>FORWARD</code>.</p>
</details>
