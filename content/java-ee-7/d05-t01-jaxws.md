---
title: SOAP Service dan Client dengan JAX-WS
minutes: 24
level: Menengah
badge: lengkap
summary: Menulis @WebService, mengatur binding style, dan membuat klien dari WSDL.
objectives:
  - Membuat SOAP endpoint dengan @WebService dan @WebMethod
  - Membedakan document/literal dan rpc/encoded
  - Menghasilkan klien dengan wsimport atau Dispatch
---
## Kenapa topik ini diuji
JAX-WS diuji lewat detail anotasi dan WSDL: parameter mana yang jadi bagian pesan, bagaimana nama elemen di XML, dan kapan memakai `@WebParam(mode=OUT)`.

## Konsep inti
```java
@WebService(serviceName = "HitungService", portName = "HitungPort",
            targetNamespace = "http://contoh.id/ws")
public class HitungEndpoint {

    @WebMethod(operationName = "tambah")
    public int tambah(@WebParam(name = "a") int a,
                      @WebParam(name = "b") int b) { return a + b; }

    @WebMethod(exclude = true)     // tidak diekspos sebagai operation
    public void internal() { }

    @WebMethod
    public void isiRiwayat(@WebParam(name = "id") String id,
                           @WebParam(name = "hasil", mode = WebParam.Mode.OUT)
                           Holder<String> hasil) { hasil.value = "ok"; }
}
```

- Endpoint bisa dipublikasikan sebagai servlet dengan `@WebService` + `@Stateless`, atau via `sun-jaxws.xml`/`web.xml`.
- `@SOAPBinding(style = SOAPBinding.Style.DOCUMENT, use = SOAPBinding.Use.LITERAL)` adalah konfigurasi dominan dan interoperable; `RPC`/`ENCODED` sudah usang.
- `@HandlerChain(file = "handler.xml")` menambahkan handler pesan (logging, security).
- Klien: `wsimport -keep http://host/HitungService?wsdl` menghasilkan kelas port; atau dinamis lewat `Dispatch<SOAPMessage>` / `Provider<T>`.

```java
// klien hasil wsimport
HitungService svc = new HitungService();
HitungPort port = svc.getHitungPort();
int hasil = port.tambah(2, 3);
```

## Jebakan ujian
- `exclude = true` pada `@WebMethod` menyembunyikan method dari WSDL, tetapi method `private` memang tidak pernah diekspos.
- `@WebParam(mode = OUT)` wajib memakai `Holder<T>`.
- `style` ditentukan di level binding, bukan per method.
- Endpoint `@WebService` harus punya konstruktor tanpa argumen (atau dikelola EJB).
- WSDL-first (dari XSD) berbeda dari code-first; ujian sering menyebut keduanya.

## Latihan
1. Anotasi apa untuk mengubah nama elemen parameter di SOAP body?
2. Bagaimana mengecualikan satu method publik dari kontrak WSDL?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@WebParam(name = "…")</code>.</p>
<p><b>2.</b> <code>@WebMethod(exclude = true)</code>.</p>
</details>
