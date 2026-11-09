---
title: Service dan Client JAX-RS
minutes: 25
level: Menengah
badge: lengkap
summary: Anotasi JAX-RS, binding parameter, MessageBodyReader/Writer, dan client API.
objectives:
  - Menulis resource class dengan @Path dan anotasi metode
  - Mengikat parameter path, query, header, form, dan bean
  - Membuat client dengan ClientBuilder
---
## Kenapa topik ini diuji
JAX-RS penuh anotasi dengan perilaku berbeda: `@PathParam` vs `@QueryParam`, dan `@Produces` vs `@Consumes` adalah dua pasangan yang paling sering tertukar.

## Konsep inti
```java
@Path("/pesanan")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class PesananResource {

    @Inject PesananService service;

    @GET
    public List<Pesanan> daftar(@QueryParam("status") String status,
                                @QueryParam("limit") @DefaultValue("20") int limit) {
        return service.cari(status, limit);
    }

    @GET @Path("/{id}")
    public Response satu(@PathParam("id") long id) {
        return service.cari(id)
            .map(p -> Response.ok(p).build())
            .orElse(Response.status(Response.Status.NOT_FOUND).build());
    }

    @POST
    public Response buat(Pesanan p, @Context UriInfo uri) {
        Pesanan baru = service.simpan(p);
        return Response.created(uri.getAbsolutePathBuilder().path(String.valueOf(baru.getId())).build())
                       .entity(baru).build();
    }

    @PUT @Path("/{id}")
    public void ganti(@PathParam("id") long id, Pesanan p) { service.ganti(id, p); }

    @DELETE @Path("/{id}")
    public void hapus(@PathParam("id") long id) { service.hapus(id); }
}
```

- `@Produces` = tipe response; `@Consumes` = tipe request body.
- `@BeanParam` menggabungkan beberapa anotasi parameter ke satu kelas.
- `@Provider` untuk `ExceptionMapper`, `MessageBodyReader/Writer`, filter, dan interceptor.
- Client:

```java
Client client = ClientBuilder.newClient();
WebTarget target = client.target("https://api.contoh.id").path("pesanan").path("{id}")
                          .resolveTemplate("id", 7);
Pesanan p = target.request(MediaType.APPLICATION_JSON).get(Pesanan.class);

Response res = client.target("https://api.contoh.id/pesanan")
    .request().post(Entity.json(pesananBaru));
int status = res.getStatus();
```

## Jebakan ujian
- `@ApplicationPath("/api")` pada subclass `Application` menggeser semua path.
- Tanpa `@Produces`, default-nya `*/*`; tanpa `MessageBodyWriter` untuk tipe itu → 500.
- `@PathParam` dari template `{id}`; `@QueryParam` dari `?id=`.
- `Response` harus di-close pada client untuk melepas koneksi.
- Sub-resource locator: method tanpa anotasi metode HTTP yang mengembalikan objek dengan `@Path` sendiri.

## Latihan
1. Anotasi mana yang menentukan tipe body request yang diterima?
2. Bagaimana mengubah exception menjadi response 400 secara global?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@Consumes</code>.</p>
<p><b>2.</b> Implementasi <code>ExceptionMapper&lt;IllegalArgumentException&gt;</code> beranotasi <code>@Provider</code>.</p>
</details>
