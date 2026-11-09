---
title: Mengakses document store dengan MySQL Shell
minutes: 20
level: Menengah
badge: lengkap
summary: Mode SQL/JS/Python, session, dan utilitas impor JSON.
objectives:
  - Berpindah mode eksekusi di MySQL Shell
  - Membuat sesi ke document store
  - Mengimpor data JSON
---
## Kenapa topik ini diuji
MySQL Shell adalah alat resmi untuk X DevAPI; soal menanyakan perintah atau mode yang tepat.

## Konsep inti
```bash
mysqlsh                        # masuk ke shell interaktif
mysqlsh --uri app@localhost:33060 --js
mysqlsh --uri app@localhost:3306  --sql
```

Di dalam shell:

```javascript
\sql
\js
\py
\status

var session = mysqlx.getSession('app@localhost:33060');
var db = session.getSchema('appdb');
db.getCollections();

// impor dokumen dari file JSON (satu objek per baris)
util.importJson('/data/produk.json', {schema:'appdb', collection:'produk'});
```

```python
# mode Python
import mysqlsh
shell = mysqlsh.globals.shell
session = shell.get_session('app@localhost:33060')
db = session.get_schema('appdb')
```

Utilitas lain: `util.checkForServerUpgrade()`, `util.dumpInstance()`, `util.loadDump()`.

## Jebakan
- `\sql` mengirim ke port 3306 (protokol klasik); document store butuh 33060.
- `util.importJson` mengharapkan format JSON per baris (JSON Lines), bukan array besar.
- Mode shell (`\js`, `\py`, `\sql`) memengaruhi sintaks seluruh perintah berikutnya.
- Sesuaikan URI bila memakai TLS (`?ssl-mode=REQUIRED`).

## Latihan
1. Perintah berpindah ke mode JavaScript?
2. Format file untuk util.importJson?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>\js</code>.</p>
<p><b>2.</b> JSON Lines — satu dokumen JSON per baris.</p>
</details>
