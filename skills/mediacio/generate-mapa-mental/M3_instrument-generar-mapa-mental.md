---
modul: M3
titol: "Generar mapa mental"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: []
descripcio: "Instrument de mediació per generar un mapa mental radial (Buzan): concepte central + branques associatives, preguntes generadores i connexions interdisciplinàries, graduat pel MECR. DIFERENT de generate-mapa-conceptual (Novak, jeràrquic, relacions etiquetades, comprensió del text): el mapa mental prioritza el pensament divergent i l'associació lliure, va MÉS ENLLÀ del text i és especialment útil per a altes capacitats, recapitulació i exploració creativa (B1+). Format markdown radial (central com a única arrel de llista en negreta, branques sagnades), exportable a Canva/MindMeister/XMind i renderitzable pel frontend ATNE com a SVG (Mermaid mindmap). Mai fletxes Unicode ni ASCII-art. Rúbrica gradada 6 passos × 6 nivells MECR (pre-A1→C1)."
mecr_range: [pre-A1, A1, A2, B1, B2, C1]
agent_roles: [complements]
complement_key: mapa_mental
translanguaging: false
multimodal: false
moduls_relacionats: [M2, M3]
skill_meta: generate-mapa-mental@corpusFJE/skills/mediacio/generate-mapa-mental
review_status: nou-2026-06-14
version: 1.0.0-canonic
generat_at: 2026-06-14
actualitzat_at: 2026-06-14
notebooklm_review:
  data: pendent
  veredicte: pendent-revisio
  comentari_key: "M3 canonitzat 2026-06-14 a partir del SKILL.md proto 1.0.0 (handoff ATNE editor de diagrames bloc B). Preserva la pedagogia Buzan del proto i la gradua a 6 nivells MECR. Pendent validació pedagògica NotebookLM MALL."
---

# Generar mapa mental

## Descripció

El mapa mental és un **organitzador visual radial** (Buzan): un concepte central del qual irradien branques d'associació lliure, preguntes generadores i connexions interdisciplinàries. A diferència del mapa conceptual (Novak, jeràrquic), el mapa mental no busca reconstruir l'estructura del text sinó **obrir-lo**: generar idees, connectar amb el que l'alumne ja sap i provocar preguntes noves. El frontend ATNE renderitza el diagrama com a SVG (Mermaid mindmap) a partir d'una llista Markdown amb sagnia.

**Tipologia MALL**: Mediació (organitzador visual divergent).
**HCL principal**: Connectar — associar idees i generar relacions noves més enllà del text.
**HCL secundàries**: Recapitular (obrir un tema), Preguntar (generar preguntes), Transferir (connexions interdisciplinàries).
**Principi rector**: *"El mapa mental no organitza el que el text diu, sinó el que l'alumne pot pensar a partir del text."* Una branca sense pregunta generadora ni connexió és una llista, no un mapa mental.

**Distinció fonamental amb `generate-mapa-conceptual` (instrument separat):**
- `mapa_conceptual` (Novak, A2-C1): "Llegir per comprendre" — contingut **dintre del text** adaptat; estructura jeràrquica; relacions **etiquetades** (provoca, es divideix en); el nom de la branca és la prova de comprensió.
- `mapa_mental` (Buzan, B1+): "Llegir per connectar" — contingut **més enllà del text**; estructura **radial** i divergent; associacions **no etiquetades**; preguntes generadores; per a alumnat amb AACC o exploració creativa.
Quan l'objectiu és comprendre l'estructura del text → `mapa_conceptual`. Quan l'objectiu és expandir, connectar i generar preguntes → `mapa_mental`.

**Connexions MALL transversals:**
- *Divergència vs. organització*: el mapa mental treballa el pensament divergent (obrir possibilitats); el mapa conceptual i l'esquema visual treballen el convergent (organitzar el que ja hi és). Són complementaris, no intercanviables.
- *Preguntes generadores com a motor*: la pregunta ("i si...?", "per què...?") és el que distingeix un mapa mental d'una llista de paraules. A B1+ cada branca hauria de poder generar almenys una pregunta.
- *Connexions interdisciplinàries com a valor afegit*: el rendiment cognitiu màxim del mapa mental és transferir un concepte a una altra matèria o a la vida quotidiana. Si el mapa no en conté cap, s'ha quedat curt.
- *El docent acaba la peça visual*: ATNE proveeix l'estructura semàntica (branques, preguntes, connexions); el color, les imatges i la disposició final els fa el docent a Canva o MindMeister.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Descriu el mapa mental **com a estímul de divergència** que es genera a partir d'un tema (sovint ancorat al text adaptat, però amb branques que van més enllà). NO descriu la producció autònoma avaluable de l'alumne (això és tasca de `generate-bastides-produccio` i `generate-rubriques`).

## Principi general

**Regla de selecció simple.** Genera un mapa mental com a llista markdown radial: una sola arrel (concepte central en negreta) i de 2 a 8 branques associatives segons el MECR, amb sub-idees, preguntes generadores i connexions interdisciplinàries graduades pel nivell. El concepte central és el tema obert que es vol explorar; les branques irradien associacions, no categories jeràrquiques etiquetades (això és el mapa conceptual).

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix si l'alumne concret es beneficia de la divergència ni si cal mapa mental en comptes de mapa conceptual (decisió docent prèvia segons perfil i objectiu). El LLM tampoc no força connexions interdisciplinàries artificioses: si una connexió no és pedagògicament honesta, val més no incloure-la.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### AACC_exploracio_creativa

**Inclou si:**
- Objectiu d'exploració, brainstorming o connexió més enllà del text.
- Alumnat amb altes capacitats que necessita obertura, no simplificació.
- Branques amb preguntes generadores i connexions interdisciplinàries (sostre del rang).

**Exclou explícitament:**
- Simplificació estructural del text (això és esquema visual o mapa conceptual).

**Raonament pedagògic.** Per a AACC el risc no és la sobrecàrrega sinó l'avorriment per infra-exigència. El mapa mental ofereix divergència i transferència, que mantenen el repte cognitiu (anti expertise reversal a l'inrevés).

### recapitulacio_o_introduccio

**Inclou si:**
- Obertura d'un tema nou (activar coneixement previ) o tancament/repàs creatiu.
- Branques associatives amb una idea per branca al nivell base.

**Exclou explícitament:**
- Estructuració jeràrquica per estudiar (mapa conceptual).

**Raonament pedagògic.** El mapa mental és un bon GPS d'obertura ("què sabem ja d'això?") i de tancament connectiu, no un esquema d'estudi convergent.

### pre_A1_A1_emergent

**Inclou si:**
- 2-3 branques amb paraula clau + imatge/emoji.
- Una sola sagnia (arrel + branques directes).

**Exclou explícitament:**
- Preguntes abstractes.
- Connexions interdisciplinàries abstractes.

**Raonament pedagògic.** A la fase emergent el patró radial només es sosté si és mínim i ancorat a la imatge; les preguntes abstractes i les connexions interdisciplinàries són prematures.

## Detecció

**Senyals docent** (quan activar el complement):
- Ha activat "Mapa mental" al Pas 2.
- L'objectiu és obrir un tema, generar idees o connectar amb altres matèries (no estructurar-lo per estudiar).
- Alumnat AACC que necessita repte i divergència.
- Inici o tancament d'una unitat: activar coneixement previ o connectar el que s'ha après.

**Senyals alumne** (que indica que aprofitarà el suport):
- Té idees però no les connecta entre si.
- S'avorreix amb organitzadors convergents perquè ja domina l'estructura.
- Fa preguntes laterals ("i això té a veure amb...?") que mereixen un espai.

**Anti-senyals** (quan NO activar):
- L'objectiu és comprendre o estudiar l'estructura del text → `mapa_conceptual`.
- L'objectiu és ordenar passos o parts d'un tot → `esquema_visual` (a `generate-mapa-conceptual`).
- L'objectiu és suport lexical → `glossari`.
- Mapa conceptual ja seleccionat: redundància; el docent ha de triar-ne un (si tots dos actius, prioritzar mapa conceptual per a tasques d'estudi).
- Pre-A1 sense alfabetització L1: el patró radial pot confondre; substituir per dibuix amb pictogrames lineals.
- Text molt curt (< 50 paraules): no hi ha prou matèria per generar branques significatives.

## Modulació per nivell

| Pas | Dimensió | Pre-A1 Emergent | A1 Inicial | A2 Funcional | B1 Estratègic | B2 Acadèmic | C1 Crític |
|---|---|---|---|---|---|---|---|
| **1. Concepte central** | Nucli radial | Tema o objecte familiar, 1 paraula + pictograma/emoji. | 1 paraula clau del tema. En negreta. | Frase nominal curta (1-3 paraules) del tema. En negreta. | Tema o concepte que es vol explorar. En negreta. | Concepte nuclear, pot ser abstracte. En negreta. | Concepte complex o tensió que es vol obrir. En negreta. |
| **2. Branques primàries** | Nombre de branques | 2 branques associatives. | 2-3 branques associatives. | 3-4 branques associatives. | 4-5 branques associatives. | 5-7 branques associatives. | 5-8 branques associatives. |
| **3. Profunditat** | Nivells d'expansió | 1 nivell: arrel i branques directes, sense sub-idees. | 1 nivell: arrel i branques directes. | 1-2 nivells: branca i, opcionalment, una sub-idea. | 2 nivells: branca i sub-idees. | 2-3 nivells: branca, sub-idees i matís. | 3 nivells: expansió completa amb tensions. |
| **4. Preguntes generadores** | Densitat i obertura | Cap pregunta abstracta: només paraula clau + imatge. | Cap pregunta abstracta: paraules clau soles. | Una idea curta per branca; encara sense preguntes generadores explícites. | 1-2 preguntes generadores ("per què...?", "què passaria si...?"). | Preguntes obertes a diverses branques que conviden a explorar. | Preguntes provocadores que obren tensions o contradiccions. |
| **5. Connexions transversals** | Associacions interdisciplinàries | Cap connexió interdisciplinària (massa abstracta a aquest nivell). | Cap connexió interdisciplinària. | 1 connexió concreta amb la vida quotidiana. | 1 connexió explícita amb una altra matèria. | 1-2 connexions interdisciplinàries. | Connexions interdisciplinàries + connexió amb fonts o debats externs. |
| **6. Format de sortida** | Estructura markdown radial | `## Mapa mental` + llista amb central com a única arrel en negreta (`- **CENTRAL**`) i branques sagnades 2 espais. Pictogrames/emoji inline a arrel i branques. Cap fletxa Unicode ni ASCII-art. | `## Mapa mental` + central arrel en negreta, branques sagnades 2 espais. Pictogrames recomanats. Cap ASCII-art. | `## Mapa mental` + central arrel en negreta, branques sagnades, fins a 2 nivells. Cap ASCII-art. | `## Mapa mental` + central arrel en negreta, branques i sub-idees sagnades (2 nivells). Cap ASCII-art. | `## Mapa mental` + central arrel en negreta, fins a 3 nivells de sagnia. Cap ASCII-art. | `## Mapa mental` + central arrel en negreta, fins a 3 nivells de sagnia amb tensions. Cap ASCII-art. |

## Casos especials

### pre_A1_radial_minim

**Trigger:** mecr_in: [pre-A1]

**Modulació:**
- max_branques: 2
- profunditat: 1 nivell (arrel + branques directes)
- pictogrames: obligatoris a arrel i branques
- preguntes_abstractes: cap

**Raonament pedagògic.** A la fase emergent el patró radial només es sosté amb un mínim de branques i amb la imatge com a àncora; afegir preguntes abstractes o sub-idees infantilitza o confon.

### mapa_conceptual_ja_seleccionat

**Trigger:** complement_actiu: mapa_conceptual

**Modulació:**
- valorar_no_generar: true (evitar redundància d'organitzadors)
- si_tots_dos_actius: prioritzar mapa conceptual per a tasques d'estudi tradicional

**Raonament pedagògic.** Mapa mental i mapa conceptual responen a objectius cognitius oposats (divergir vs. organitzar). Generar-los tots dos per al mateix text duplica esforç i confon l'alumne; el docent n'ha de triar un.

### text_massa_curt

**Trigger:** paraules_text: <50

**Modulació:**
- no_generar: true
- avis_retornat: "el text és massa curt per generar branques associatives significatives"

**Raonament pedagògic.** Sense prou matèria conceptual, el mapa mental genera branques buides o forçades, que no aporten divergència real.

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici humà o LLM-jutge.
- `countable` — llindar quantitatiu verificable mecànicament.
- `structural` — requereix anàlisi de l'estructura de la llista.
- `metacognitive` — descriptor de procés en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Concepte central | `qualitative` | parcial | LLM-jutge: el nucli és el tema que es vol explorar; pot ancorar-se al text però el mapa mental connecta MÉS ENLLÀ del text (no cal que tot el contingut hi aparegui literalment) |
| 2 Branques primàries | `countable` | no | comptar branques a nivell 1 (sagnia 1); ha de ser dins del rang del nivell (pre-A1: 2; A1: 2-3; A2: 3-4; B1: 4-5; B2: 5-7; C1: 5-8) |
| 3 Profunditat | `countable` | no | mesurar nivells d'indentació; ha de ser dins del rang del nivell (pre-A1/A1: 1; A2: 1-2; B1: 2; B2: 2-3; C1: 3) |
| 4 Preguntes generadores | `qualitative` | no | LLM-jutge: presència i obertura de preguntes segons nivell; a B1+ una branca sense cap pregunta generadora és una llista, no un mapa mental |
| 5 Connexions transversals | `qualitative` | parcial | LLM-jutge: presència de connexions interdisciplinàries o amb la vida quotidiana segons nivell; són el valor afegit del mapa mental |
| 6 Format de sortida | `structural` | no | regex: central com a única arrel de llista en negreta (`- **...**`), branques sagnades en múltiples de 2 espais; cap fletxa Unicode (→ ↔ 🌿) ni caràcter d'arbre (│ ├ └ ─) |

**Notes:**
- 6 (Format de sortida) és **mecànic** (regex) — baix cost, sense LLM. El central ha de ser l'única arrel de llista en negreta; si surt com a `###`, el renderitzador el filtra i es perd el central (mateix contracte estructural que mapa-conceptual).
- 4 (Preguntes generadores) és la diferència cognitiva clau amb una llista de paraules: a B1+ la pregunta és obligatòria de facto.
- 5 (Connexions transversals): són el rendiment màxim del mapa mental; el LLM no les ha de forçar si no són honestes (vegeu Principi general).

## Heurístiques docent

**H1 — La pregunta fa el mapa mental.**
Llegeixo les branques i em pregunto: "Hi ha alguna pregunta que obri el tema?" Una branca amb només paraules és una llista; una branca amb una pregunta generadora ("i si això passés a l'inrevés?") és un mapa mental. A B1+ exigeixo almenys una pregunta per mapa.

**H2 — Divergir, no organitzar.**
Si el que vull és que l'alumne entengui com s'estructura el text per estudiar-lo, NO és un mapa mental: és un mapa conceptual o un esquema visual. El mapa mental serveix per obrir, connectar i generar, no per ordenar.

**H3 — Les connexions transversals són el valor afegit.**
El millor d'un mapa mental és quan connecta el tema amb una altra matèria o amb la vida de l'alumne. Si el mapa generat no en té cap (a A2+), el considero curt i n'hi afegeixo.

**H4 — Cap fletxa ni caràcter d'arbre, mai.**
El frontend renderitza la llista markdown amb sagnia com a SVG (Mermaid mindmap). Si hi ha fletxes Unicode (→ ↔ 🌿) o ASCII-art (│ ├ └), el render falla o es trunca. Sempre llista markdown amb guions i sagnia de 2 espais, central com a arrel en negreta.

**H5 — Densitat segons nivell.**
Un mapa mental no és millor com més branques té. A pre-A1/A1 limito a 2-3 branques i 1 nivell per no saturar; a B2-C1 permeto 5-8 branques i fins a 3 nivells per representar la riquesa associativa. Si superat el sostre, fusiono branques redundants.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Mapa mental
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
cap
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
[PICTO: clau_arasaac|text_visible]
```

**Headers explícitament PROHIBITS:**
```
## Mapa
## Mapa conceptual
## Esquema visual
```

**Esquelet de sortida (literal — segueix-lo exactament):**

El concepte central és l'**única arrel de llista en negreta** i **mai un encapçalament `###`**. Les branques van **sagnades sota l'arrel**. Les sub-idees, preguntes i connexions van sagnades sota la branca.

_Mapa mental B1 — Tema: la fotosíntesi:_
```
## Mapa mental

- **FOTOSÍNTESI**
  - Què és?
    - transformació de llum en aliment
    - només les plantes ho fan?
  - Ingredients
    - aigua + diòxid de carboni + llum solar
    - connexió amb Química (matèria i energia)
  - On passa?
    - a les fulles (cloroplasts)
    - per què les fulles són verdes?
  - Per a què serveix?
    - per què respirem millor on hi ha boscos?
    - connexió amb Geografia (canvi climàtic)
```

**Estructura que TRENCA el mapa (no ho facis mai):**
```
### FOTOSÍNTESI      ← encapçalament ###: es filtra i es perd el concepte central
→ Què és?            ← fletxa Unicode: el renderitzador no la lliga a l'arrel
```

**Regla d'integritat estructural.** Un únic H2 `## Mapa mental`. Cap H3. El **concepte central és l'única arrel de llista en negreta** (`- **CENTRAL**`), **mai un `###`** (l'encapçalament es filtra i es perd el central). Les **branques van sagnades sota l'arrel**; les sub-idees, preguntes i connexions, sagnades sota la branca. PROHIBIT ASCII-art (│ ├ └) i fletxes Unicode (→ ↔ 🌿). Pictogrames inline a pre-A1 (obligatoris) i A1 (recomanats). Sense aquests literals ni aquesta estructura de llista, el frontend ATNE no detecta el complement ni pot renderitzar el bloc Mermaid mindmap a partir de la llista markdown.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): divergència vs. organització estructural; "llegir per connectar".
- Buzan, T. (1974): *Use Your Head*. BBC Books — mapa mental radial original.
- Novak, J.D. & Gowin, D.B. (1984): *Learning How to Learn* — mapa conceptual (contrast amb el mapa mental: estructura vs. associació).
- M2_instruments-mediacio-pedagogica (MALL transversal): organitzadors visuals divergents.
