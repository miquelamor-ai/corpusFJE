# Novetats — Dinàmiques de formació a M11 (2026-06-11)

Aquest document deixa constància d'una incorporació al corpus i serveix de **heads-up** per a l'equip i per als consumidors (ATNE, Scriptorium, Itinerarium).

## Què s'ha incorporat

El mòdul **M11 (Desenvolupament Professional)** passa a contenir **43 dinàmiques de formació docent**, organitzades pel cicle **Abans–Durant–Després (A-D-D)** i orientades als nivells d'impacte de Guskey.

- **On viuen (màster):** `dinamiques/M11_dinamica-<id>.md` — carpeta **plana**, un fitxer per dinàmica, **editable a Scriptorium**. La fase és metadada del frontmatter (`phase`), **no** una subcarpeta: algunes dinàmiques serveixen per a més d'una fase (p. ex. l'observació a l'aula, `durant` i `despres`), i així reclassificar-les és editar un camp, no moure un fitxer.
- **Tipus de document nou:** `tipus: dinamica` (vegeu l'especificació del corpus, §4.10). És a M11 el que `genere-discursiu`/`instrument` són a M3: una família derivada governada amb el mateix patró que les skills.
- **Fonamentació:** no es duplica a cada fitxa. CPA, A-D-D i Guskey viuen al marc [`M11_desenvolupament-professional-docent.md`](../M11_desenvolupament-professional-docent.md), enllaçat des de cada dinàmica.

## Com es consumeixen (regla màster → derivat)

```
dinamiques/M11_dinamica-<id>.md   (MÀSTER pla, s'edita aquí; phase = frontmatter)
        │  [GitHub Action: build-dinamiques.yml, determinista, sense IA]
        ▼
dinamiques/_dinamiques.json       (DERIVAT, el llegeixen les apps)
```

- La direcció és **única**: s'edita el `.md`, i el JSON es regenera sol. **Mai s'edita el JSON a mà.**
- El JSON derivat conserva l'esquema històric (`id, phase, block, title, stars, role, duration, guskey, purpose, objectives, schedule, materials, simple, indicators`), de manera que és un substitut directe per a qui ja el consumia.
- **Camp opcional nou:** `phases_aplicables` (llista) hi apareix **només** a les dinàmiques que serveixen per a més d'una fase A-D-D (23 de 43). Si no hi és, s'entén `= [phase]`. La fase **primària** segueix sent `phase`. És additiu: qui no el necessiti, l'ignora.
- Cada `id` és una **clau estable**: no canvia un cop publicada (encara que se'n reformuli el títol).

## Què implica per a cada consumidor

- **Scriptorium** — Les dinàmiques s'editen com qualsevol document M11 (un `.md` per fitxa). Cal que la navegació les llisti sota M11 recorrent la subcarpeta `dinamiques/` i que les tracti com a **editables** (no read-only).
- **Itinerarium** — La font de les dinàmiques passa a ser el corpus. El build-step de l'app ha d'apuntar a `corpusFJE/dinamiques/_dinamiques.json` (substitueix la còpia que vivia a l'app). El corpus posseeix els blocs reutilitzables; l'app, les composicions (plans, fitxes de formació).
- **ATNE** — De moment **no l'afecta**: aquestes dinàmiques són de formació docent, no d'adaptació de textos per a alumnat. El ganxo `moduls_relacionats` queda obert per a una reutilització futura (p. ex. tutories) sense reescriure res.

## Criteri editorial aplicat

- **Anti-apropiació del carisma** (vegeu `docs/guia-estil-veu-corpus.md`): cap dinàmica instrumentalitza un concepte espiritual ignasià com a nom o estructura de tècnica. Dues fitxes es van reformular conservant l'`id`: `examen-consciencia` → «Revisió reflexiva de la pràctica»; `portafoli` (un terme normalitzat). Les pràctiques universals (Lesson Study, DAFO, mapa d'empatia…) es mantenen tal qual.

## Nota tècnica col·lateral

S'ha corregit `\.github/scripts/build_manifest.py`, que classificava els fitxers de **M10 i M11 dins de M1** (la detecció de mòdul només llegia un dígit). El manifest ja reflecteix M10 i M11 com a mòduls propis.
