---
title: Security Deklaratif dan Programatik
minutes: 24
level: Menengah
badge: lengkap
summary: @RolesAllowed, security-constraint di web.xml, dan pemeriksaan peran saat runtime.
objectives:
  - Mengamankan EJB dan URL dengan deklarasi
  - Memakai isUserInRole dan isCallerInRole
  - Memilih mekanisme autentikasi BASIC, FORM, atau DIGEST
---
## Kenapa topik ini diuji
Soal keamanan hampir selalu tentang letak konfigurasi: apakah di `web.xml`, anotasi EJB, atau kode. Salah tempat berarti tidak berlaku.

## Konsep inti
```java
@Stateless
@RolesAllowed({"admin"})
public class AdminService {
    @PermitAll public String info() { return "publik"; }
    @DenyAll   public void rahasia() { }
    @RolesAllowed({"admin","auditor"})
    public void laporan(javax.ejb.SessionContext ctx) {
        if (ctx.isCallerInRole("auditor")) { /* hanya baca */ }
    }
}
```

```xml
<security-constraint>
  <web-resource-collection>
    <web-resource-name>admin</web-resource-name>
    <url-pattern>/admin/*</url-pattern>
    <http-method>GET</http-method>
    <http-method>POST</http-method>
  </web-resource-collection>
  <auth-constraint><role-name>admin</role-name></auth-constraint>
  <user-data-constraint><transport-guarantee>CONFIDENTIAL</transport-guarantee></user-data-constraint>
</security-constraint>

<login-config>
  <auth-method>FORM</auth-method>
  <form-login-config>
    <form-login-page>/login.xhtml</form-login-page>
    <form-error-page>/login-error.xhtml</form-error-page>
  </form-login-config>
</login-config>

<security-role><role-name>admin</role-name></security-role>
```

- Programatik di servlet: `req.isUserInRole("admin")`, `req.login(...)`, `req.logout()`, `req.authenticate(res)`.
- Programatik di EJB: `SessionContext.isCallerInRole`, `getCallerPrincipal()`.
- `@DeclareRoles` mendeklarasikan peran pada EJB.
- Pemetaan peran ke user/grup dilakukan di container (realm), bukan di kode.

## Jebakan ujian
- `@RolesAllowed` hanya berlaku pada EJB; servlet memakai `web.xml` atau `@ServletSecurity`.
- `@PermitAll` dan `@DenyAll` menimpa aturan kelas.
- `transport-guarantee CONFIDENTIAL` memaksa HTTPS.
- FORM auth memakai `j_security_check`, `j_username`, `j_password`.
- Peran di `web.xml` tanpa `<security-role>` bisa diabaikan sebagian container.

## Latihan
1. Di mana `@RolesAllowed` tidak berpengaruh?
2. Method untuk mengetahui peran pemanggil di dalam EJB?

<details><summary>Jawaban</summary>
<p><b>1.</b> Pada servlet, JSP, dan managed bean - hanya EJB.</p>
<p><b>2.</b> <code>SessionContext.isCallerInRole("peran")</code>.</p>
</details>
