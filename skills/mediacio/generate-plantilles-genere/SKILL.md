---
name: generate-plantilles-genere
description: 'Use when the teacher has activated the "plantilles_genere" complement.
  Generates a partially completed text model of the target genre — a concrete example
  that shows the student what the finished product looks like, with some sections
  filled in and others left as guided blanks. Distinct from base d''orientació (which
  is a procedure/GPS): a plantilla is a CONCRETE PARTIAL TEXT to imitate. Modulated
  by MECR, genre, and subject.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: plantilles_genere
agent_role: complements
tools_required: []
triggers:
- path: params.complements.plantilles_genere
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-plantilles-genere.md
font_version: 4.0.0-canonic
generat_at: '2026-06-06'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 3a6b8955a948edb9
---

# Generar plantilles de gènere — skill operativa per a LLM

La plantilla de gènere és un **text model parcial** que mostra a l'alumne com queda el gènere acabat, amb algunes seccions completes i d'altres deixades com a buits guiats per omplir. L'alumne no segueix passos: **imita i completa** un text que ja té la forma del gènere. La seva funció pedagògica és descarregar la **càrrega d'estructurar** (saber com s'organitza el gènere) perquè l'alumne pugui centrar-se en el contingut i la llengua.

**Tipologia MALL**: Mediació (bastida de textualització — Fase 4 de la Seqüència Didàctica).
**HCL associada**: cap HCL pròpia — la plantilla emmarca la HCL del gènere actiu. El text donat mostra la HCL en acció; els forats demanen que l'alumne la practiqui.
**Principi cognitiu**: la plantilla elimina la càrrega d'estructurar (pas 2 de la textualització de Flower-Hayes) perquè l'alumne pugui centrar-se en recuperar el contingut (pas 1) i codificar-lo en la nova llengua (pas 3).
**Principi rector**: els forats han de ser **específics del contingut real del text treballat**, no genèrics. "L'any ___, a ___, [nom del personatge concret del text] va..." és específic. "Un personatge va..." és genèric i desconnecta la plantilla del text llegit.

**Distinció fonamental amb la base d'orientació:**
- **Base d'orientació** (Bloc A de bastides-produccio): procediment (GPS de passos) — "1. Escriu el títol. 2. Situa el context..."
- **Plantilla de gènere**: text model parcial — mostra com queda el text acabat, amb buits per omplir.
L'alumne que usa la base d'orientació sap QUÈ fer en cada pas. L'alumne que usa la plantilla veu DIRECTAMENT com ha de quedar el text.

**Pre-A1 SÍ (D6)**: la plantilla visual (requadres + icones) és accessible a lectors logografics perquè no demana produir text autònom — demana dibuixar o enganxar dins d'un esquema estructurat. L'adult llegeix les instruccions en veu alta i l'alumne respon visualment. El significat es construeix per via concreta i visual, mediat per l'adult.

**Connexions MALL transversals:**
- *Text model explícit (Seqüència Didàctica)*: el MALL usa el text model per mostrar com s'escriu el gènere ABANS de demanar que l'alumne l'escrigui. La plantilla és el text model + els forats que converteixen la lectura/observació en producció activa.
- *Gradació dels forats com a ZDP operativa*: el forat petit (A1, 1-2 paraules) es situa a la zona confort; el forat gran (C1, producció lliure per secció) és el repte màxim. La plantilla manté l'alumne a la seva ZDP mentre avança cap a la producció autònoma.
- *Imitació com a aprenentatge legítim*: la plantilla no és una drecera deshonesta. Aprendre un gènere és aprendre les seves convencions, i la imitació guiada és el primer pas cap a la producció autònoma. El text donat és el model, no la còpia.
- *Forats específics com a ancoratge al contingut*: els buits genèrics desconnecten la plantilla del text que l'alumne ha llegit. Els forats específics ("En [nom del personatge del text]...") mantenen el vincle entre la comprensió lectora i la producció escrita.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **plantilla que es genera perquè l'alumne produeixi el seu text** (PRODUCCIÓ MEDIADA). **No descriu la producció autònoma de l'alumne**: la plantilla és el suport, la producció de l'alumne és el resultat. El docent observa si l'alumne completa els forats amb contingut rellevant del text treballat.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → plantilla visual pura (dibuixar/enganxar). `fase_lectora: alfabetica_emergent` → plantilla amb 1-2 paraules per forat, mediat per adult.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Tipus de plantilla**
- Format i densitat del text donat: Visual: 3-4 requadres amb icones. Cap text autònom. L'adult llegeix les instruccions.

**2. Especificitat dels forats**
- Concretesa del contingut del forat: Requadre de dibuix o icona per completar. Cap text a omplir autònomament.

**3. Vinculació al text adaptat**
- Ancoratge al contingut llegit: Forats completables amb imatges o paraules que apareixen al text. L'adult mostra on és la resposta.

**4. Densitat dels forats**
- Proporció text donat / forats: Maxima densitat visual: tota la plantilla és un esquema. Cap text en prosa.

**5. Autoavaluació mediada**
- Metacognició: "He dibuixat (o enganxat) el que passa al text." (oral, mediat per adult)

### A1 — Inicial


**1. Tipus de plantilla**
- Format i densitat del text donat: Text quasi complet: 70-80% donat, 20-30% forats. 1-2 paraules per forat.

**2. Especificitat dels forats**
- Concretesa del contingut del forat: Forats de 1-2 paraules: nom concret, verb d'acció, un adjectiu. Completables amb paraules del text adaptat.

**3. Vinculació al text adaptat**
- Ancoratge al contingut llegit: Forats completables amb paraules o noms extrets directament del text adaptat.

**4. Densitat dels forats**
- Proporció text donat / forats: Alta densitat forats: 1 forat cada 2-3 paraules. El text donat guia i contextualitza.

**5. Autoavaluació mediada**
- Metacognició: "He completat les paraules que faltaven amb informació del text."

### A2 — Funcional


**1. Tipus de plantilla**
- Format i densitat del text donat: Text parcialment donat: 50-60% donat, 40-50% forats. Frases curtes per completar.

**2. Especificitat dels forats**
- Concretesa del contingut del forat: Forats d'1 frase: "Els protagonistes son ___" · "El conflicte és ___". Completables amb reformulació del text.

**3. Vinculació al text adaptat**
- Ancoratge al contingut llegit: Forats que requereixen selecció i reformulació d'informació del text.

**4. Densitat dels forats**
- Proporció text donat / forats: Densitat moderada: 1 forat per frase o cada 2 frases. Text donat aporta estructura.

**5. Autoavaluació mediada**
- Metacognició: "He completat les seccions amb informació del text que he llegit."

### B1 — Estratègic


**1. Tipus de plantilla**
- Format i densitat del text donat: Text marc: 30-40% donat (connectors, estructura, termes disciplinars clau).

**2. Especificitat dels forats**
- Concretesa del contingut del forat: Forats de 2-3 frases construïdes per l'alumne amb les seves paraules a partir del text.

**3. Vinculació al text adaptat**
- Ancoratge al contingut llegit: Forats que requereixen inferència o selecció crítica d'informació del text.

**4. Densitat dels forats**
- Proporció text donat / forats: Densitat baixa: 1 forat per paràgraf. L'alumne aporta la major part del contingut.

**5. Autoavaluació mediada**
- Metacognició: "He completat la plantilla amb informació pròpia sobre el contingut. He verificat que els forats son coherents amb el gènere."

### B2 — Acadèmic


**1. Tipus de plantilla**
- Format i densitat del text donat: Plantilla minimalista: encapçalaments + 1 frase d'exemple per secció com a model de referència.

**2. Especificitat dels forats**
- Concretesa del contingut del forat: Forats que demanen elaboració argumentada (1 paràgraf) que va més enllà del text (connexió, anàlisi).

**3. Vinculació al text adaptat**
- Ancoratge al contingut llegit: Forats que requereixen elaboració que va més enllà del text (connexió amb altres fonts).

**4. Densitat dels forats**
- Proporció text donat / forats: Densitat mínima: 1 forat per secció. Quasi tot és producció pròpia.

**5. Autoavaluació mediada**
- Metacognició: "He usat la plantilla com a model de referència i he escrit el text amb les meves pròpies paraules."

### C1+ — Crític


**1. Tipus de plantilla**
- Format i densitat del text donat: Criteris de gènere i estil. Pràcticament sense text donat: el primer mot de cada secció com a únic ancoratge.

**2. Especificitat dels forats**
- Concretesa del contingut del forat: Forats de producció lliure coherent amb el gènere, inspirada però no limitada pel text.

**3. Vinculació al text adaptat**
- Ancoratge al contingut llegit: Forats de producció pròpia de l'alumne, inspirada però autònoma.

**4. Densitat dels forats**
- Proporció text donat / forats: Forat de producció completa per secció. La plantilla és una rúbrica de gènere.

**5. Autoavaluació mediada**
- Metacognició: "He usat els criteris de gènere per autoregular la meva producció sense suport directe."

