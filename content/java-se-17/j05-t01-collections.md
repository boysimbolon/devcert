---
title: Array, List, Set, Map, Deque
minutes: 24
level: Menengah
badge: lengkap
summary: Operasi dasar, urutan, duplikat, dan jebakan unmodifiable.
objectives:
  - Memilih koleksi sesuai kebutuhan
  - Memprediksi hasil operasi remove/update
  - Menghindari UnsupportedOperationException
---
## Kenapa topik ini diuji
Soal meminta output setelah serangkaian operasi koleksi.

## Konsep inti
| Jenis | Duplikat | Urutan | Implementasi umum |
|---|---|---|---|
| `List` | ya | terindeks | `ArrayList`, `LinkedList` |
| `Set` | tidak | `HashSet` acak, `TreeSet` terurut, `LinkedHashSet` sisip |
| `Map` | key unik | `HashMap`, `TreeMap`, `LinkedHashMap` |
| `Deque` | ya | dua ujung | `ArrayDeque` |

```java
var list = new ArrayList<>(List.of("b", "a", "c"));
list.sort(Comparator.naturalOrder());     // [a, b, c]
list.removeIf(s -> s.startsWith("c"));    // [a, b]

var map = new HashMap<String, Integer>();
map.merge("a", 1, Integer::sum);
map.computeIfAbsent("b", k -> 0);

List<String> fixed = List.of("x");
// fixed.add("y");                        // UnsupportedOperationException
```

## Jebakan
- `List.of`/`Set.of` immutable dan menolak `null`.
- `remove(int)` vs `remove(Object)` — `List<Integer>.remove(1)` menghapus indeks.
- `TreeSet`/`TreeMap` butuh `Comparable` atau `Comparator`, dan menolak `null` key.
- Iterasi sambil memodifikasi → `ConcurrentModificationException` (kecuali lewat iterator/`removeIf`).

## Latihan
1. Koleksi untuk antrean dua ujung?
2. Mengapa `List<Integer> l; l.remove(1)` bisa keliru?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ArrayDeque</code>.</p>
<p><b>2.</b> Karena memilih overload <code>remove(int index)</code>, bukan menghapus elemen bernilai 1.</p>
</details>
