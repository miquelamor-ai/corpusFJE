# Canon de gèneres derivable per a ATNE — decisions de canon

**Data:** 2026-06-19 · **Autor:** Claude (mineriaRAG), per a ATNE/Pas 2 · **Estat:** CANON ACTIU (implementat al PR de la branca `feat/canon-generes-skills-derivable`). Decisions traçades a `M3_generes-discursius.md` (font de veritat, dins aquest mateix repo).

> Aquest fitxer és la **còpia canònica** del document de canon, dins el repo de corpusFJE. Una còpia de treball idèntica existeix a `mineriaRAG/docs/` (on es va redactar originalment); si discrepen, **mana aquesta**.

> Aquest document resol les tres inconsistències de frontmatter de les skills `write-*` que bloquegen la detecció de gènere derivada al Pas 2 d'ATNE, i decideix l'estatus dels 6 candidats nous.

---

## 0. Principi rector

**El M3 canònic (`M3_generes-discursius.md`) és la font de veritat del catàleg de gèneres**, no el frontmatter de les skills `write-*`. Si discrepen, mana el M3. El frontmatter és un derivat operatiu i s'ha d'alinear, no a la inversa.

El M3 estableix dos eixos taxonòmics:
- **7 macro-tipologies** (Adam, criteri intern): Narrativa, Descriptiva, Explicativa, Argumentativa, Instructiva, Conversacional, Poètica.
- **22 subgèneres FJE** (Bakhtin, criteri extern), cadascun assignat explícitament a una macro dominant.

El catàleg de skills `write-*` té avui **23 entrades** (22 del M3 + `write-contrarelat-odi` que no és al M3 però sí al corpus operatiu).

---

## 1. Decisió — Família canònica única per gènere (resol la pregunta 1)

### El problema
El camp `tipologia` actual del frontmatter és heterogeni i compost: "Argumentativa / Reflexiva", "Narrativa / Expositiva", "Instructiva / Prescriptiva"... Reflecteix la realitat (els textos són heterogenis), però **no és agregable** per a un selector amb optgroups.

### La decisió
**Afegir un camp nou `macro_tipologia` al frontmatter de cada skill `write-*`, amb una sola paraula del vocabulari controlat del M3.** El camp `tipologia` actual es manté per a continuïtat (és informatiu i ric), però **NO és el que el selector llegeix**. El selector llegeix `macro_tipologia`.

**Vocabulari controlat (exactament les 7 macros del M3):**
- `narrativa`
- `descriptiva`
- `explicativa` *(NO "expositiva" — el M3 fixa "Explicativa o expositiva", canon = explicativa)*
- `argumentativa`
- `instructiva`
- `conversacional`
- `poetica`

### Qui defineix la família de cada gènere
**El M3, no la intuïció ni el frontmatter actual.** El M3 § "Taxonomia completa" + § "Catàleg dels 22 subgèneres FJE" assigna explícitament cada gènere a una macro dominant. Aquesta és la regla:

> *"La classificació es fa per **seqüència dominant** + secundàries, no per categoria única."* (M3, § "Heterogeneïtat com a norma")

I el M3 dóna la dominant de cada gènere. Aquí l'aplico:

### Taula d'assignació canònica (23 skills)

| skill | genre_key | macro_tipologia | Traça al M3 |
|---|---|---|---|
| write-conte | conte | **narrativa** | M3 §1 + §Catàleg "conte" |
| write-fabula | fabula | **narrativa** | M3 §1 + §Catàleg "faula" |
| write-biografia | biografia | **narrativa** | M3 §1 + §Catàleg "biografia" |
| write-noticia | noticia | **narrativa** | M3 §Catàleg "notícia" → "Narrativa (dominant) + Explicativa (secundària)" |
| write-cronica | cronica | **narrativa** | M3 §1 + §Catàleg "crònica" |
| write-diari | diari | **narrativa** | M3 §1 + §Catàleg "diari" (dominant narrativa/reflexiva) |
| write-descripcio | descripcio | **descriptiva** | M3 §2 + §Catàleg "descripció" |
| write-enciclopedic | enciclopedic | **descriptiva** | M3 §Catàleg "enciclopèdic" → "Descriptiva (dominant) + Explicativa (secundària)" |
| write-manual | manual | **explicativa** | M3 §3 + §Catàleg "manual" |
| write-divulgatiu | divulgatiu | **explicativa** | M3 §3 + §Catàleg "divulgatiu" |
| write-informe | informe | **explicativa** | M3 §3 + §Catàleg "informe" → "Explicativa / Científica" |
| write-resum | resum | **explicativa** | M3 §3 + §Catàleg "resum" |
| write-opinio | opinio | **argumentativa** | M3 §4 + §Catàleg "opinió" |
| write-ressenya | ressenya | **argumentativa** | M3 §Catàleg "ressenya" → "Argumentativa / Avaluativa" |
| write-assaig | assaig | **argumentativa** | M3 §4 + §Catàleg "assaig" |
| write-instructiu | instructiu | **instructiva** | M3 §5 + §Catàleg "instructiu" |
| write-receptari | receptari | **instructiva** | M3 §5 + §Catàleg "receptari" |
| write-reglament | reglament | **instructiva** | M3 §5 + §Catàleg "reglament" |
| write-carta | carta | **conversacional** | M3 §Catàleg "carta" → "Conversacional (dominant) + Argumentativa (si defensa) o Narrativa (si narra)" |
| write-entrevista | entrevista | **conversacional** | M3 §Catàleg "entrevista" → "Conversacional (dominant) + Explicativa (secundària)" |
| write-dialeg | dialeg | **conversacional** | M3 §6 + §Catàleg "diàleg" |
| write-poema | poema | **poetica** | M3 §7 + §Catàleg "poema" |
| write-contrarelat-odi | contrarelat_odi | **argumentativa** | NO és al M3. Decisió pròpia: el contrarelat és una resposta argumentada/reflexiva a un missatge d'odi → encaixa a §4 Argumentativa, HCL Argumentar/Justificar. **Recomanat afegir-lo al M3 com a subgènere de l'esfera d'educació en valors / ciutadania global.** |

### Resolucions concretes a la divergència frontmatter vs M3
- `write-descripcio.tipologia` = "Expositiva / Descriptiva" → **`macro_tipologia: descriptiva`** (el M3 §Catàleg ho posa a Descriptiva, no Expositiva).
- `write-divulgatiu.tipologia` = "Expositiva" → **`macro_tipologia: explicativa`** (el M3 fixa Explicativa com a nom canònic; "Expositiva" és sinònim secundari).
- `write-enciclopedic.tipologia` = "Expositiva" → **`macro_tipologia: descriptiva`** (el M3 §Catàleg posa la dominant a Descriptiva, no Expositiva).
- `write-carta.tipologia` = "Argumentativa / Dialogada" → **`macro_tipologia: conversacional`** (el M3 §Catàleg fixa la dominant a Conversacional). La dimensió argumentativa queda al camp `tipologia` informatiu.
- `write-poema.tipologia` = "Narrativa / Expressiva" → **`macro_tipologia: poetica`** (M3 §7 té una macro pròpia per al poema).

### Implicació per al selector d'ATNE
El selector del Pas 2 agrupa els gèneres per `macro_tipologia`. **7 optgroups** (no 5), perquè Conversacional i Poètica són macros pròpies al M3:

1. **Narrativa** — conte, faula, biografia, notícia, crònica, diari
2. **Descriptiva** — descripció, enciclopèdic
3. **Explicativa** — manual, divulgatiu, informe, resum
4. **Argumentativa** — opinió, ressenya, assaig, contrarelat d'odi
5. **Instructiva** — instructiu, receptari, reglament
6. **Conversacional** — carta, entrevista, diàleg
7. **Poètica** — poema

> ⚠️ Si el disseny d'ATNE havia previst només 5 optgroups, **cal expandir a 7** o re-aplegar (p.ex. Conversacional dins Dialogat, Poètica dins una categoria "Altres"). La meva recomanació: **7 optgroups**, perquè el canon ho és i el M3 ho justifica explícitament (§Macro-tipologia 6 i 7). Re-aplegar trairia el canon.

---

## 2. Decisió — Camps obligatoris i validació al build (resol la pregunta 2)

### Camps obligatoris al frontmatter de tota skill `write-*`
1. `name` — slug Agent Skills (p.ex. `write-noticia`). Ja existeix.
2. `genre_key` — clau curta sense `write-` (p.ex. `noticia`). Ja existeix.
3. `description` — descripció en anglès curt (Agent Skills standard). Ja existeix.
4. `macro_tipologia` — vocabulari controlat (les 7 macros, sense barres ni composicions). **CAMP NOU.**
5. `label_ca` — etiqueta visible per a la UI en català (vegeu §3). **CAMP NOU.**
6. `tipologia` — descripció rica i composta (continua existint, informatiu).
7. `mecr_range` — llista de nivells suportats.
8. `moduls_relacionats` — llista de mòduls.

### Cas concret: `write-contrarelat-odi`
Frontmatter actual: `tipologia` buida (l'usuari ho ha confirmat). Decisió:
- `macro_tipologia: argumentativa`
- `tipologia: "Argumentativa / Reflexiva / Educació en valors"` (pista informativa)
- `label_ca: "Contrarelat de l'odi"` (vegeu §3)
- `description`: redactar una en anglès curt (avui en català) per alinear amb la resta i amb el format Agent Skills.

### Validació al build de corpusFJE
**Decisió:** afegir un pas al workflow `build-skills.yml` que **falli el build** si una skill `write-*` (o `M3_genere-*.md`) no compleix:
- `name` no buit i comença per `write-`.
- `genre_key` no buit, snake_case, derivable de `name` sense `write-`.
- `description` no buit, >50 caràcters.
- `macro_tipologia` no buit i ∈ {narrativa, descriptiva, explicativa, argumentativa, instructiva, conversacional, poetica}.
- `label_ca` no buit i comença per majúscula.
- `tipologia` no buit (admet composts amb `/`).
- `mecr_range` és llista no buida, valors ∈ {pre-A1, A1, A2, B1, B2, C1, C2}.
- `moduls_relacionats` és llista no buida (p.ex. `["M3"]`).

El validador viu a `.tooling/validate_skills_writers.py` (nou) i es crida des de `build-skills.yml` **abans** del pas que genera SKILL.md derivat. Si falla, el build s'atura i no s'escriu res a producció — això **manté la canyeria coherent automàticament**: una skill incompleta no arriba mai a ATNE.

**Equivalent del que ja fa `build_skills.py`** (AGENT_SKILLS_REQUIRED `{"name", "description"}`), però estès amb la regla del catàleg derivable. La filosofia és la mateixa: *safety check* abans d'escriure a producció.

---

## 3. Decisió — Camp `label_ca` (resol la pregunta 3)

### El problema
El catàleg derivable necessita una **etiqueta visible per a la UI en català** que no sigui el `genre_key` snake_case ni el `name` slug. Sense això, ATNE ha de mantenir el mapeig hardcoded i el catàleg no és veritablement derivable.

### La decisió
**Afegir un camp `label_ca` al frontmatter de tota skill `write-*`.** Valor: nom canònic en català, comença per majúscula, sense article (l'article el posa la UI si cal).

### Taula de `label_ca` proposada (23 skills)

| genre_key | label_ca |
|---|---|
| conte | Conte |
| fabula | Faula |
| biografia | Biografia |
| noticia | Notícia de premsa |
| cronica | Crònica |
| diari | Diari personal |
| descripcio | Descripció |
| enciclopedic | Entrada enciclopèdica |
| manual | Manual |
| divulgatiu | Text divulgatiu |
| informe | Informe |
| resum | Resum |
| opinio | Article d'opinió |
| ressenya | Ressenya |
| assaig | Assaig |
| instructiu | Text instructiu |
| receptari | Recepta |
| reglament | Reglament |
| carta | Carta |
| entrevista | Entrevista |
| dialeg | Diàleg |
| poema | Poema |
| contrarelat_odi | Contrarelat de l'odi |

### Criteris seguits
- **Concisió** sense ambigüitat (UI: cap >25 caràcters).
- **Reconeixement** per al docent: noms d'aula, no slugs tècnics ("Notícia de premsa" > "Notícia", "Article d'opinió" > "Opinió", per evitar polisèmia).
- **Coincidència amb la `essència` del M3** sempre que sigui possible.
- **Suport futur multilingüe:** el nom del camp inclou el sufix `_ca` per poder afegir `label_es`, `label_en` sense trencar res.

### Bonus opcional — `label_descripcio_curta_ca`
Si la UI vol mostrar una **subetiqueta** al selector (tooltip o segona línia), es pot derivar del camp `description` de cada skill (resumint en català) o afegir un `label_descripcio_curta_ca`. **No és obligatori per al canon**, però queda anotat com a camp opcional si ATNE el necessita per a UX.

---

## 4. Estatus dels 6 candidats nous (consulta al M3)

Per a cada candidat, verifico tres criteris del M3:
- **(a) HCL nuclear pròpia?** (M3 § Llengua/pensament/HCL)
- **(b) Estructura prototípica reconeixible?** (M3 § Taxonomia)
- **(c) Esfera d'activitat sociocultural pròpia?** (Bakhtin/M3)

Si compleix els tres → **gènere de ple dret** (mereix skill).
Si en falla un o dos → **no és gènere**: és HCL, format, o categoria veïna.
Si el M3 no ho resol → **dubte per a NotebookLM/experts**.

### Candidat 1 — **Pòster científic**
- (a) HCL: bàsicament **Explicar + Argumentar/Justificar** (no és HCL pròpia).
- (b) Estructura prototípica: introducció + mètodes + resultats + conclusions, amb forta dimensió visual.
- (c) Esfera: comunicació científica acadèmica.
- **Veredicte: GÈNERE DE PLE DRET, candidat a skill `write-poster-cientific`.** Macro: **explicativa** (dominant) + secundàries argumentativa i descriptiva. És un format derivat de l'**informe** però amb especificitats pròpies (multimodalitat obligatòria, restricció d'espai, jerarquia visual). El M3 no el llista, però compleix els tres criteris i és pràctica d'aula reconeguda a secundària/batxillerat.
- **⚠️ Matís:** la multimodalitat forta el lliga al M2 (mediació) i a les skills de complement (`generate-illustracions`, `generate-esquema-visual`). Convé coordinar amb el catàleg M2 abans de tirar endavant.

### Candidat 2 — **Demostració**
- (a) HCL: **Demostrar** (variant pedagògica explícita al M3 §HCL nuclear Argumentativa).
- (b) Estructura prototípica: enunciat + premisses + cadena de passos + QED. Reconeixible.
- (c) Esfera: matemàtiques, lògica, ciències formals.
- **Veredicte: DUBTE per a NotebookLM/experts.** El M3 sí menciona "Demostrar" com a HCL (§Argumentativa), però **no la llista com a gènere als 22 subgèneres**. La demostració matemàtica és simultàniament una HCL i un format textual amb estructura pròpia. Hi ha dues lectures legítimes:
  - **Lectura A** (gènere): és un subgènere argumentatiu específic de ciències formals (com `assaig` ho és de les humanitats) → mereix skill `write-demostracio`.
  - **Lectura B** (HCL): és la HCL "Demostrar" que ja s'activa dins gèneres existents (informe matemàtic, exercici resolt) → no cal skill pròpia.
- **Recomanació:** consultar amb experts MALL FJE de matemàtiques abans de crear-la. Si es crea, macro = **argumentativa**, label_ca = "Demostració matemàtica".

### Candidat 3 — **Pràctica de laboratori**
- (a) HCL: **Justificar** (vincular observacions a models) + **Narrar** (seqüència processal).
- (b) Estructura prototípica: objectiu + materials + procediment + resultats + discussió + conclusions.
- (c) Esfera: ciències experimentals a l'aula.
- **Veredicte: NO és gènere nou — és una variant didàctica del gènere `informe`** ja existent (M3 §Catàleg "informe" → "Explicativa / Científica"). El M3 ho diu literalment al §"Connexions amb altres documents": *"informe (resultats)"* surt a Ciències experimentals. Una "pràctica de laboratori" és un informe amb un context i una estructura disciplinar específics, però NO té estructura prototípica ni HCL diferenciades respecte a `informe`.
- **Recomanació:** no crear skill nova. Si cal especificitat, fer-ho via **variable de matèria** dins `write-informe` (o, com a molt, un *exemple* nou a `write-informe/assets/exemple-laboratori-quimica.md`).

### Candidat 4 — **Diari de camp**
- (a) HCL: **Narrar + Descriure** (observacions) + **Interpretar/Valorar**.
- (b) Estructura prototípica: data + lloc + observacions descriptives + reflexions personals.
- (c) Esfera: ciències socials, antropologia, ciències naturals (treball de camp).
- **Veredicte: NO és gènere nou — és una variant del gènere `diari`** ja existent (M3 §Catàleg "diari" → "Narrativa / Reflexiva (personal) o Expositiva / Justificativa (acadèmic)"). El M3 ja contempla explícitament la variant acadèmica del diari. Un "diari de camp" és el diari aplicat a treball d'observació empírica, però comparteix HCL nuclear (Narrar + Interpretar) i estructura amb el `diari` genèric.
- **Recomanació:** no crear skill nova. Cobrible amb una variable o un exemple a `write-diari/assets/exemple-diari-camp.md`. Si la diferència es considera prou pedagògica per a separar-los, llavors **dubte per a NotebookLM** (preguntar si el diari de camp es treballa amb tractament prou diferenciat com per ser un subgènere autònom).

### Candidat 5 — **Certificat**
- (a) HCL: no clarament identificable (és un acte performatiu, no cognitiu-lingüístic).
- (b) Estructura prototípica: encapçalament institucional + cos declaratiu + signatura + segell. Sí, però **mínima i ritualitzada**.
- (c) Esfera: administrativa/jurídica.
- **Veredicte: NO és gènere de l'esfera educativa FJE en el sentit MALL.** El certificat és un **document administratiu performatiu** (com el rebut, el carnet, el títol acadèmic). El M3 §"Errors comuns" alerta de no convertir formats administratius en gèneres pedagògics. Cap esfera d'activitat educativa el demana com a producció de l'alumne (a diferència de la carta, que sí). HCL nul·la o quasi nul·la.
- **Recomanació:** **descartar com a skill.** Si en un futur cal (formació professional, mòdul de jurídic), reconsiderar — però avui no és prioritat MALL.

### Candidat 6 — **Exercici**
- (a) HCL: **qualsevol** (depèn del que demana l'exercici).
- (b) Estructura prototípica: **no en té** (un exercici és qualsevol enunciat amb una resposta esperada).
- (c) Esfera: **transversal a totes** (tots els gèneres es poden treballar via exercici).
- **Veredicte: NO és gènere — és un FORMAT didàctic.** "Exercici" és com diem a un tipus d'**activitat d'aula**, no a una pràctica discursiva. El M3 §"Errors comuns" ho avisaria explícitament: confondre format amb gènere. El que diferencia un exercici no és la HCL ni l'esfera; és la **funció didàctica** (avaluar/practicar). Això és terreny de **M6 (Avaluació)** o de M2 (instruments de mediació), no de M3.
- **Recomanació:** **descartar com a skill `write-*`.** Si cal generar "exercicis" derivats d'un text adaptat, ja existeix la skill de complement `generate-activitats-aprofundiment` i `generate-preguntes-comprensio` al catàleg M2. Aquí no hi ha un buit a omplir.

### Resum candidats

| Candidat | Veredicte | Acció |
|---|---|---|
| Pòster científic | ✅ Gènere de ple dret | Crear `write-poster-cientific`, macro=explicativa. Coordinar amb M2 (multimodal). |
| Demostració | ❓ Dubte per a NotebookLM | Consultar experts MALL matemàtiques. Si sí: macro=argumentativa. |
| Pràctica de laboratori | ❌ No és gènere nou | Cobrir amb exemple/variable dins `write-informe`. |
| Diari de camp | ❌ No és gènere nou (probable dubte menor) | Cobrir amb exemple/variable dins `write-diari`. Validar amb NotebookLM si la distinció pedagògica val skill pròpia. |
| Certificat | ❌ No és gènere MALL | Descartar. Document administratiu, no pràctica discursiva educativa. |
| Exercici | ❌ No és gènere | Descartar. És FORMAT didàctic, no gènere. Ja cobert per skills de complement M2. |

---

## 5. Síntesi del que cal canviar i on

### A corpusFJE (font de veritat)
1. **Frontmatter de les 23 skills `write-*`:** afegir `macro_tipologia` (vocabulari controlat) i `label_ca`. Completar `tipologia`+`description` a `write-contrarelat-odi`.
2. **`.tooling/validate_skills_writers.py`** (nou) — validador estricte amb les regles del §2.
3. **`.github/workflows/build-skills.yml`** — afegir step de validació abans del build. Si falla, el build s'atura.
4. **`M3_generes-discursius.md`** — afegir `contrarelat d'odi` al §Catàleg (subgènere de l'esfera valors/ciutadania, macro argumentativa). Validar la incorporació.
5. **(Opcional, futur)** crear `M3_genere-escriure-poster-cientific.md` + skill `write-poster-cientific/`, coordinat amb M2.

### A ATNE
- El Pas 2 llegeix `corpus/external/corpusFJE/skills/generes/*/SKILL.md` i deriva el catàleg de:
  - `genre_key` → valor del selector.
  - `label_ca` → text visible.
  - `macro_tipologia` → optgroup.
- **Cap mapeig hardcoded.** Afegir un gènere = afegir una skill ben formada al corpus + push.

### Quina pregunta queda oberta i per a qui
- **Macro-Conversacional i Poètica al selector:** confirmar que el selector pot tenir 7 optgroups (no 5). Si el disseny d'ATNE només admet 5, **decisió de UX** que cal fer abans (re-aplegar trairia el M3).
- **Demostració:** dubte real per a NotebookLM / experts MALL matemàtiques.
- **Diari de camp:** dubte menor per a NotebookLM (probable variable de `write-diari`).
- **Contrarelat d'odi al M3:** afegir-lo al catàleg M3 oficial (avui hi és com a skill però no com a entrada del marc canònic). Ordre lògic: primer M3, després skill.

---

## 6. Què NO canvia (perquè quedi explícit)

- Cap fitxer s'ha modificat amb aquest document. **Només decisions.**
- El camp `tipologia` actual es **manté** (no es buida ni se substitueix). El nou `macro_tipologia` el complementa, no el reemplaça. Així es preserva la riquesa informativa del M3 ("Narrativa / Testimonial", "Argumentativa / Reflexiva") sense perdre agregabilitat.
- Les 22 skills `write-*` existents que ja són al M3 **no canvien d'identitat**: només se'ls afegeixen dos camps. La skill `write-contrarelat-odi` rep frontmatter complet i s'incorpora al M3.
- Cap canvi de codi a ATNE (`skills_loader.py`, `prompt_builder.py`): el catàleg derivable l'aprofitarà el Pas 2 quan es construeixi; aquesta proposta no toca la lectura runtime.

---

*Document de canon. Quan en Miquel el validi, les peces d'implementació (frontmatter + validador + workflow + M3 actualitzat) van al repo `miquelamor-ai/corpusFJE`, no a ATNE — perquè el canon viu al corpus i ATNE l'hereta automàticament.*
