---
modul: M3
titol: "Generar esquema visual"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: [generes]
descripcio: "Instrument de mediació visual que extreu l'estructura del text adaptat en forma de diagrama jeràrquic (arrel + ramificacions). Reforça la comprensió de relacions seqüencials, causa-efecte o jerarquia. Rúbrica gradada 5 passos × 6 nivells MECR."
mecr_range: [pre-A1, A1, A2, B1, B2, C1]
agent_roles: [complements]
complement_key: esquema_visual
multimodal: true
moduls_relacionats: [M2, M3, M5]
variables_configurables:
  genere_discursiu: [instructiu, receptari, manual, divulgatiu, narratiu, expositiu]
skill_meta: generate-esquema-visual@corpusFJE/skills/mediacio/generate-esquema-visual
review_status: nou-2026-05-31
version: 1.0.0-canonic
generat_at: 2026-05-31
actualitzat_at: 2026-05-31
notebooklm_review:
  data: pendent
  veredicte: pendent-revisio
  comentari_key: "M3 creat 2026-05-31 a partir de la directiva Python ATNE consolidada. Pendent validació pedagògica completa per NotebookLM."
---

# Generar esquema visual

## Descripció

L'esquema visual és un instrument de **mediació estructural**. Extreu del text adaptat la xarxa d'idees principals i les organitza en un diagrama jeràrquic amb una arrel (concepte central) i ramificacions (subtemes, passos, causes/conseqüències). El frontend ATNE renderitza el diagrama com a SVG (Mermaid flowchart) a partir d'una llista Markdown amb sagnia.

**Tipologia MALL**: Mediació estructural (suport).
**HCL principal**: Categoritzar — distingir el central del perifèric.
**HCL secundàries**: Ordenar (seqüència), Relacionar (causa-efecte), Identificar (parts d'un tot).
**Principi rector**: *"L'esquema visualitza la idea, no la suplanta"* — un bon esquema ajuda a recordar; un esquema sobrecarregat substitueix la lectura.

**Connexions MALL transversals:**
- *Multimodalitat (DUA Representació)*: l'esquema ofereix una via complementària de comprensió per a l'alumnat amb dificultats de seqüenciació textual o memòria de treball.
- *Bastida retirable*: a primària inicial, el docent presenta l'esquema com a mapa de lectura previ; a B1+, l'alumne el reprodueix per si mateix; a B2+, l'alumne en construeix de propis.
- *No-substitut de mapa conceptual*: l'esquema visual representa estructura **lineal o jeràrquica** (passos, parts, seqüències); el mapa conceptual representa **relacions etiquetades** entre nodes (cau-efecte, sinonímia, oposició). Tots dos coexisteixen al canon.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Descriu l'esquema visual **per a la LECTURA** de l'alumne (mediació presentada per l'eina/docent). NO descriu la producció autònoma de l'alumne (això és tasca dels SKILLs `generate-bastides-lectura` i `generate-rubriques`).

## Principi general

**Regla de selecció simple.** Genera un esquema com a llista markdown amb una sola arrel (concepte central) i ramificacions amb sagnia de 2 espais per nivell, ajustant nombre de nodes (2-3 a pre-A1 fins 10-15 a C1) i profunditat (1 nivell a pre-A1 fins 3-4 a C1) segons el MECR. Per a gèneres procedimentals (instructiu/receptari/manual) l'arrel SEMPRE és el PRODUCTE/OBJECTIU final, mai un apartat seqüencial (Materials, Passos, Ingredients).

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix si l'esquema substitueix la lectura ni si l'alumne concret en treu profit cognitiu; aquest judici el fa l'acompanyant a partir dels senyals d'aula (apartat Detecció) i les heurístiques H1-H4. El LLM tampoc no decideix si activar mapa conceptual en comptes d'esquema visual (decisió docent prèvia).

_Excepcions: no n'hi ha._

## Detecció

**Senyals docent** (quan activar esquema visual):
- El text té estructura clarament jeràrquica (parts, categories, taxonomies).
- El text té una seqüència de passos numerats (instructiu, receptari, protocol).
- El text té relacions causa-efecte explícites o implícites (text expositiu de ciències).
- El text adaptat té més de 100 paraules i l'alumne perd el fil al meitat.
- L'alumnat té dificultats de comprensió globalitzada (TEA, TDAH, dislèxia, DI).
- La matèria és STEM o ciències socials (estructures sovint jeràrquiques o seqüencials).

**Senyals alumne**:
- Pot recitar passos però no pot dibuixar com es relacionen.
- Pregunta "i això per què?" entre passos consecutius (no veu la connexió causal).
- En el resum oral, perd subordinació (tot al mateix nivell, sense distinció central-perifèric).

**Anti-senyals** (quan NO activar esquema visual):
- Text narratiu sense estructura jeràrquica (conte, poema, diari personal).
- Text molt curt (< 80 paraules) on l'estructura ja és transparent.
- Perfil AC (altes capacitats) que no necessita simplificació estructural — pot ser **expertise reversal** i infantilitzar.
- Text amb una sola idea i sense subdivisions naturals.

## Regla específica per a gèneres procedimentals (instructiu / receptari / manual)

**CRÍTIC**: per a textos del tipus instructiu/receptari/manual, el **node central (arrel)** de l'esquema ha de ser el **PRODUCTE FINAL** o l'OBJECTIU de la procedència, NO el primer apartat (Materials, Necessites, Ingredients) ni un pas seqüencial.

**Exemple correcte** (receptari "Com fer un titella amb una mitja"):
- Node central: `Titella de mitja`
  - Branca: `Materials` → mitja, botons, agulla, fil, farciment
  - Branca: `Passos` → posar farciment, lligar, cosir, dibuixar
  - Branca: `Resultat` → titella acabat amb el qual jugar

**Exemple INCORRECTE** (el que el LLM tendeix a fer sense aquesta regla):
- Node central: `Materials` (primer apartat del text → ERROR)
  - …

Justificació pedagògica: el concepte central és el QUÈ ES CONSTRUEIX, no el COM. Els materials i passos són sub-elements en relació al producte. Aquesta regla és **idènticament aplicable** a manuals tècnics, protocols mèdics, receptes culinàries i guies de muntatge.

## Modulació per nivell

| Pas | Dimensió | Pre-A1<br>Emergent | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1+<br>Crític |
|---|---|---|---|---|---|---|---|
| **1. Concepte central (arrel)** | Selecció | El concepte més imatge-amigable del text. Sovint un objecte concret amb pictograma. | El subjecte/tema principal explícit del títol. | El tema principal o producte final del text. | El concepte abstracte o procés que organitza el text. | El concepte clau analític del text. | El concepte estructurant del discurs (no necessàriament explícit). |
|  | Format de la cel·la arrel | Una sola paraula o frase de 2 paraules amb pictograma al costat. | Una sola paraula clau. | Una frase nominal curta (1-4 paraules). | Frase nominal (3-6 paraules). | Concepte abstracte expressat amb 1-2 paraules tècniques. | Concepte abstracte amb possible distinció disciplinar. |
| **2. Nombre de nodes** | Total nodes | 2-3 nodes. Seqüències temporals bàsiques (abans→després) o relacions imatge→paraula. | 3-4 nodes. Enumeració de qualitats o parts d'un objecte (descripció simple). | 4-6 nodes. Seqüència de passos d'instrucció o esdeveniments cronològics. | 6-8 nodes. Relacions causa-efecte o hipòtesi-evidència. | 8-12 nodes amb subnivells. Estructures complexes amb arrel + branques + sub-branques. | 10-15 nodes amb 3-4 nivells de profunditat. Estructures conceptuals amb categories i sub-categories. |
|  | Profunditat de l'arbre | 1 nivell (arrel + fills directes). | 1-2 nivells. | 2 nivells (arrel → branca → fulla). | 2-3 nivells. | 3 nivells. | 3-4 nivells. |
| **3. Format de presentació** | Marcat textual | Llista markdown amb guions `-` i sagnia de 2 espais per nivell. PICTOGRAMES inline obligatoris a l'arrel i a les fulles principals. | Llista markdown amb guions `-` i sagnia 2 espais. Pictogrames recomanats per a fulles concretes. | Llista markdown amb guions `-` i sagnia 2 espais. | Idem. | Idem. | Idem. |
|  | Format prohibit | NO fletxes Unicode (→, ↓, ↔). NO ASCII-art (\|, ├, └, ─). NO emojis decoratius. | Idem. | Idem. | Idem. | Idem. | Idem. |
| **4. Tipus de relacions** | Predominant | Seqüència temporal simple o relació part-tot. | Enumeració paral·lela (germans). | Seqüència cronològica o passos numerats. | Causa-efecte explícita o hipòtesi-evidència. | Categorització jeràrquica abstracta. | Estructures discursives complexes (tesi-arguments-refutació). |
|  | Etiquetes a les connexions | No (només estructura). | No. | Opcional ("primer", "després"). | Etiquetes amb connectors lògics (perquè, llavors). | Etiquetes amb connectors causals/contrastius. | Etiquetes amb metallenguatge ("contraargument", "pressupòsit"). |
| **5. Criteris transversals** | Una sola arrel | Una sola arrel per esquema. Sense múltiples nodes a profunditat 0. | Idem. | Idem. | Idem. | Idem. | Idem. |
|  | Node central canònic | A gèneres procedimentals (instructiu/receptari/manual): el node central és el PRODUCTE/OBJECTIU final, NO un apartat seqüencial. A gèneres expositius: el TEMA principal. A gèneres narratius: NO s'aplica esquema visual. | Idem. | Idem. | Idem. | Idem. | Idem. |
|  | No-soroll visual | Cap node decoratiu sense informació. | Idem. | Idem. | Idem. | Idem. | Idem. |
|  | Fidelitat al text font | Cada node ha de poder traçar-se a una frase o concepte del text adaptat. | Idem. | Idem. | Idem (i a derivacions justificades a B1+). | Idem. | Idem (els meta-discursius sí entren). |
| **6. Autoavaluació metacognitiva** | Reflexió sobre el procés | "He mirat l'esquema quan no entenia com es connectaven les coses." | "He buscat l'arrel quan no entenia de què parlava el text." | "He fet servir l'esquema per recordar l'ordre dels passos." | "He revisat l'esquema per veure quina idea és central i quines són secundàries." | "He construït el meu propi esquema d'un text similar per veure si entenia l'estructura." | "He reflexionat sobre si l'esquema captura l'estructura argumental real del text o és una simplificació." |

## Casos especials

### genere_procedimental_arrel_producte

**Trigger:** genere_discursiu_in: [instructiu, receptari, manual]

**Modulació:**
- node_arrel: PRODUCTE_O_OBJECTIU_FINAL del text (no un apartat com Materials, Ingredients, Necessites, Passos)
- branques_primer_nivell: agrupen Materials, Passos i Resultat com a fills de l'arrel-producte

**Raonament pedagògic.** El concepte central és el QUÈ ES CONSTRUEIX, no el COM. Evidència empírica: cas titella 2026-05-30, on el LLM tendia a posar "Materials" com a arrel en lloc de "Titella".

### genere_narratiu_no_aplica

**Trigger:** genere_discursiu_equals: narratiu

**Modulació:**
- no_generar_esquema: true
- avis_retornat: "l'esquema visual no aplica a text narratiu sense estructura jeràrquica"

**Raonament pedagògic.** Contes, poemes i diaris personals no tenen estructura part-tot ni causa-efecte explotables com a diagrama; forçar-ho infantilitza o distorsiona el text.

### pre_A1_pictogrames_obligatoris

**Trigger:** mecr_in: [pre-A1]

**Modulació:**
- densitat_pictogrames: obligatori a arrel + fulles principals
- format_cella_arrel: 1-2 paraules + [PICTO:]
- nombre_nodes_max: 3
- profunditat_max: 1 nivell

**Raonament pedagògic.** A la fase logogràfica/emergent la càrrega cognitiva visual ha de ser mínima i la imatge ancora el concepte abans que el codi escrit (DUA Representació + MALL multimodal).

### AACC_risc_infantilitzacio

**Trigger:** aacc: true AND mecr_in: [B1, B2, C1]

**Modulació:**
- valorar_no_generar: true (revisar si el text ja és estructuralment transparent per a l'alumne)
- si_es_genera: anar a sostre del rang (profunditat 3-4, etiquetes amb metallenguatge)

**Raonament pedagògic.** Expertise reversal — un esquema simplificat sobre un text que l'alumne ja domina estructuralment esdevé soroll cognitiu.

## Metadades de cel·la (per a `build_skills.py`)

| Dimensió | Tipus | Requires source text? | Validation hint |
|---|---|---|---|
| 1.1 Concepte central — Selecció | `qualitative` | **sí** (text adaptat) | LLM-jutge: el node arrel ha de coincidir amb el producte/tema central del text. Per a procedimentals: NO ha de ser un apartat (Materials, Passos) |
| 1.2 Concepte central — Format cel·la | `qualitative` | no | LLM-jutge: cel·la arrel ≤ N paraules segons nivell |
| 2.1 Nombre de nodes — Total | `countable` | no | comptar nodes; ha de ser dins el rang del nivell |
| 2.2 Nombre de nodes — Profunditat | `countable` | no | mesurar nivells d'indentació; ha de ser dins el rang del nivell |
| 3.1 Format — Marcat textual | `binary` | no | regex: cada línia comença amb `-` i indentació en múltiples de 2 espais |
| 3.2 Format — Format prohibit | `binary` | no | regex: cap caràcter de fletxa Unicode (→, ↓, ↔) ni caràcters de dibuix d'arbre (\|, ├, └) |
| 4.1 Tipus de relacions — Predominant | `qualitative` | **sí** (text adaptat) | LLM-jutge: el tipus de relació entre nodes ha de coincidir amb la tipologia del text |
| 4.2 Tipus de relacions — Etiquetes | `qualitative` | no | presència o absència d'etiquetes segons nivell |
| 5.1 Una sola arrel | `binary` | no | comptar nodes a indentació 0; ha de ser exactament 1 |
| 5.2 Node central canònic | `qualitative` | **sí** (text adaptat + gènere) | LLM-jutge: per a gèneres procedimentals, validar que el node arrel és el producte/objectiu |
| 5.3 No-soroll visual | `qualitative` | no | LLM-jutge: cada node ha d'aportar informació pedagògica |
| 5.4 Fidelitat al text font | `cross_source` | **sí** (text adaptat) | LLM-jutge: traçabilitat de cada node a una frase o concepte del text |
| 6 Autoavaluació metacognitiva | `metacognitive` | no | derivat doble: autoavaluació alumne + registre docent de la qualitat |

**Notes:**
- 5.2 (Node central canònic) és la regla MÉS CRÍTICA i causa de bugs reals (cas titella 2026-05-30: arrel "Materials" en lloc de "Titella"). LLM-jutge ha de prendre el gènere del text com a input addicional.
- 3.2 (Format prohibit) és **mecànic** (regex) — es pot validar sense LLM, baix cost.
- 4.x: les etiquetes a les connexions són un MUST per a B1+, perquè distingeixen aquest instrument del mapa conceptual.

## Heurístiques docent

**H1 — La regla del titella.**
Quan adapto un receptari, una recepta o un manual, l'esquema sempre té com a arrel el QUÈ ES CONSTRUEIX. Si l'esquema generat per ATNE té com a arrel "Materials" o "Ingredients", el rectifico manualment — l'arrel ha de ser el producte final ("titella", "pa de pessic", "tornavís muntat").

**H2 — Profunditat per nivell.**
A pre-A1/A1 limito l'esquema a un sol nivell (arrel + fills directes), per evitar sobrecàrrega visual. A B2+ permeto 3 nivells de profunditat per representar matissos disciplinars.

**H3 — No fletxes ni caràcters d'arbre.**
El frontend renderitza llistes markdown amb sagnia com a SVG (Mermaid). Si el LLM insereix fletxes Unicode (→) o ASCII-art (├, └), el render falla o es trunca. Sempre llista markdown amb guions i sagnia de 2 espais.

**H4 — Esquema VS mapa conceptual.**
Si el text té relacions etiquetades importants (causes contrastives, sinonímies, oposicions conceptuals), prefereixo activar **mapa conceptual** en lloc d'esquema visual. L'esquema és per a estructures jeràrquiques o seqüencials simples; el mapa conceptual és per a xarxes amb etiquetes.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Esquema visual
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
cap
```

**Bullets / moments interns** (si aplica — NO son H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
[PICTO: clau_arasaac|text_visible]
```

**Headers explicitament PROHIBITS:**
```
cap
```

**Regla d'integritat estructural.** Llista markdown amb guions `-` i sagnia múltiple de 2 espais; una sola línia a indentació 0 (arrel). Sense H3 interns, sense fletxes Unicode (→↓↔) ni ASCII-art (├└─). Pictogrames inline obligatoris a pre-A1, recomanats a A1. Sense aquesta estructura, ATNE no pot renderitzar el bloc Mermaid a partir de la llista markdown.

## Fonts

- M2_instruments-mediacio-pedagogica (MALL transversal)
- M5_TPACK + M5_recursos-digitals (representació multimodal segons DUA)
- Directiva Python ATNE consolidada 2026-05-27 (`adaptation/prompt_builder.py:1722`)
- Cas titella 2026-05-30 (evidència empírica del bug "node central = Materials")
