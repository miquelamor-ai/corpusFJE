---
name: generate-mapa-mental
description: 'Use when the teacher has activated the "mapa_mental" complement. Generates
  a radial mind map (Buzan-style): central concept surrounded by primary branches
  with associative ideas, generating questions, and interdisciplinary connections.
  DIFFERENT from `generate-mapa-conceptual`: mind map prioritises divergent thinking
  and free association; concept map prioritises hierarchical structure and labelled
  relationships. Output is markdown that can be copy-pasted into Canva, MindMeister,
  XMind.

  '
author: FJE — Fundació Jesuïtes Educació
version: 1.1.0-canonic
complement_key: mapa_mental
agent_role: complements
tools_required: []
triggers:
- path: params.complements.mapa_mental
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-mapa-mental.md
font_version: 1.1.0-canonic
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 326a7b69817dc91d
---

# Generar mapa mental — skill operativa per a LLM

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

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Concepte central**
- Nucli radial: Tema o objecte familiar, 1 paraula + pictograma/emoji.

**2. Branques primàries**
- Nombre de branques: 2 branques associatives.

**3. Profunditat**
- Nivells d'expansió: 1 nivell: arrel i branques directes, sense sub-idees.

**4. Preguntes generadores**
- Densitat i obertura: Cap pregunta abstracta: només paraula clau + imatge.

**5. Connexions transversals**
- Associacions interdisciplinàries: Cap connexió interdisciplinària (massa abstracta a aquest nivell).

**6. Format de sortida**
- Estructura markdown radial: `## Mapa mental` + llista amb central com a única arrel en negreta (`- **CENTRAL**`) i branques sagnades 2 espais. Pictogrames/emoji inline a arrel i branques. Cap fletxa Unicode ni ASCII-art.

### A1 — Inicial


**1. Concepte central**
- Nucli radial: 1 paraula clau del tema. En negreta.

**2. Branques primàries**
- Nombre de branques: 2-3 branques associatives.

**3. Profunditat**
- Nivells d'expansió: 1 nivell: arrel i branques directes.

**4. Preguntes generadores**
- Densitat i obertura: Cap pregunta abstracta: paraules clau soles.

**5. Connexions transversals**
- Associacions interdisciplinàries: Cap connexió interdisciplinària.

**6. Format de sortida**
- Estructura markdown radial: `## Mapa mental` + central arrel en negreta, branques sagnades 2 espais. Pictogrames recomanats. Cap ASCII-art.

### A2 — Funcional


**1. Concepte central**
- Nucli radial: Frase nominal curta (1-3 paraules) del tema. En negreta.

**2. Branques primàries**
- Nombre de branques: 3-4 branques associatives.

**3. Profunditat**
- Nivells d'expansió: 1-2 nivells: branca i, opcionalment, una sub-idea.

**4. Preguntes generadores**
- Densitat i obertura: Una idea curta per branca; encara sense preguntes generadores explícites.

**5. Connexions transversals**
- Associacions interdisciplinàries: 1 connexió concreta amb la vida quotidiana.

**6. Format de sortida**
- Estructura markdown radial: `## Mapa mental` + central arrel en negreta, branques sagnades, fins a 2 nivells. Cap ASCII-art.

### B1 — Estratègic


**1. Concepte central**
- Nucli radial: Tema o concepte que es vol explorar. En negreta.

**2. Branques primàries**
- Nombre de branques: 4-5 branques associatives.

**3. Profunditat**
- Nivells d'expansió: 2 nivells: branca i sub-idees.

**4. Preguntes generadores**
- Densitat i obertura: 1-2 preguntes generadores ("per què...?", "què passaria si...?").

**5. Connexions transversals**
- Associacions interdisciplinàries: 1 connexió explícita amb una altra matèria.

**6. Format de sortida**
- Estructura markdown radial: `## Mapa mental` + central arrel en negreta, branques i sub-idees sagnades (2 nivells). Cap ASCII-art.

### B2 — Acadèmic


**1. Concepte central**
- Nucli radial: Concepte nuclear, pot ser abstracte. En negreta.

**2. Branques primàries**
- Nombre de branques: 5-7 branques associatives.

**3. Profunditat**
- Nivells d'expansió: 2-3 nivells: branca, sub-idees i matís.

**4. Preguntes generadores**
- Densitat i obertura: Preguntes obertes a diverses branques que conviden a explorar.

**5. Connexions transversals**
- Associacions interdisciplinàries: 1-2 connexions interdisciplinàries.

**6. Format de sortida**
- Estructura markdown radial: `## Mapa mental` + central arrel en negreta, fins a 3 nivells de sagnia. Cap ASCII-art.

### C1+ — Crític


**1. Concepte central**
- Nucli radial: Concepte complex o tensió que es vol obrir. En negreta.

**2. Branques primàries**
- Nombre de branques: 5-8 branques associatives.

**3. Profunditat**
- Nivells d'expansió: 3 nivells: expansió completa amb tensions.

**4. Preguntes generadores**
- Densitat i obertura: Preguntes provocadores que obren tensions o contradiccions.

**5. Connexions transversals**
- Associacions interdisciplinàries: Connexions interdisciplinàries + connexió amb fonts o debats externs.

**6. Format de sortida**
- Estructura markdown radial: `## Mapa mental` + central arrel en negreta, fins a 3 nivells de sagnia amb tensions. Cap ASCII-art.

