---
name: write-cronica
description: 'Use when adapting or generating a crònica for students. Activates when
  genre_discursiu == "cronica". Applies explicit chronology, visible chronicler perspective,
  and concrete sensory descriptions. Output: crònica in markdown with title and moments
  ordered chronologically.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: cronica
tipologia: Narrativa / Testimonial
mecr_range:
- A1
- A2
- B1
- B2
- C1
agent_role: adapter
tools_required: []
triggers:
- path: params.genere_discursiu
  equals: cronica
moduls_relacionats:
- M3
macro_tipologia: narrativa
label_ca: Crònica
font_canonic: M3_genere-escriure-cronica.md
font_version: 4.0.0-canonic
generat_at: '2026-06-21'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 7695fb453ef6f0c0
---

# Escriure/adaptar una crònica — skill operativa per a LLM

La crònica és una narració testimonial d'un esdeveniment real des de la perspectiva d'un **cronista** que l'ha viscut o observat directament. El seu tret definitori és la **doble presència**: els fets ordenats cronològicament i la perspectiva del cronista que els interpreta. A diferència de la notícia (que oculta el narrador), la crònica el fa visible; a diferència del diari (que és íntim), la crònica té vocació de comunicar l'experiència a un lector extern.

**Tipologia MALL**: Narrativa/Testimonial.
**HCL principal**: Narrar — seqüenciar un esdeveniment real amb perspectiva del cronista visible.
**HCL secundàries**: Descriure — descripció sensorial integrada a la narració (A1-B1) · Interpretar/Valorar — valoració separada dels fets al final (A2+) · Argumentar — valoració crítica que connecta l'experiència amb un context (B2+).
**No s'adapta a pre-A1**: la crònica requereix simultàniament la **distinció temporal** (cronologia de l'event), la **perspectiva del cronista** (primera persona que interpreta) i la **separació fets/valoració** (saber que "qué ha passat" i "qué penso que ha passat" son coses diferentes). Aquests tres conceptes son abstraccions accessibles oralment a partir de A1 mediat per l'adult, però no en producció escrita logogràfica/emergent. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Narrar vs. opinar com a bastida del pensament crític*: la crònica és el gènere que més clarament ensenya la distinció entre fets i opinions. La separació estructural (fets al cos, valoració al final) és una bastida cognitiva que precede l'assaig argumentatiu: l'alumne aprèn primer a separar, després a argumentar.
- *Perspectiva del cronista com a primer punt de vista*: la crònica introdueix la noció de punt de vista narratiu sense la complexitat del narrador literari. El cronista és real, la perspectiva és en primera persona i l'experiència és verificable. És el pont entre la narració factual (notícia) i la narració literària (conte).
- *Descripció sensorial integrada*: la descripció a la crònica no és una llista de característiques (com a la descripció pura) sinó un element narratiu que situa el lector en el moment. Aprendre a integrar-la als moments cronològics és una competència de cohesió textual.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **crònica adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Marcadors temporals**
- Seqüència i precisió: "Primer", "després", "al final". 3-4 moments.

**2. Perspectiva del cronista**
- Visibilitat i consistència: Primera persona plural ("vam veure", "vam anar"). Consistent.

**3. Moments ordenats**
- Organització i progressió: 3-4 moments en ordre cronològic estricte. 1-2 frases per moment.

**4. Descripcions sensorials**
- Concreció i atmosfera: 1 descripció sensorial per moment: qué es veu o s'escolta.

**5. Separació fets / valoració**
- Rigor i reflexió: Sense valoració final (no requerida a A1).

**6. Criteris transversals**
- Connectors: Almenys 2 connectors temporals diferents al llarg del text. Cap repetició sistemàtica del mateix connector.
- Especulació sobre tercers: Cap especulació sobre el que altres persones pensaven o sentien. Només el que el cronista ha observat directament.
- Fidelitat al text font: Fidelitat als fets principals i a la perspectiva testimonial bàsica.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He explicat 3-4 moments en ordre. He dit qué vaig veure."

### A1 — Inicial


**1. Marcadors temporals**
- Seqüència i precisió: "A les X", "de sobte", "llavors". 4-5 moments.

**2. Perspectiva del cronista**
- Visibilitat i consistència: Primera persona (singular o plural) visible i consistent en tot el text.

**3. Moments ordenats**
- Organització i progressió: 4-5 moments ordenats. 2-3 frases per moment. Connexió simple entre moments.

**4. Descripcions sensorials**
- Concreció i atmosfera: Descripció sensorial i emocional breu per moment.

**5. Separació fets / valoració**
- Rigor i reflexió: Valoració d'una frase al final, clarament separada dels fets.

**6. Criteris transversals**
- Connectors: Varietat mínima de 3 connectors temporals de tipus diferent. Cap connector repetit en moments consecutius.
- Especulació sobre tercers: Idem.
- Fidelitat al text font: Fidelitat als fets, a la perspectiva i a la valoració essencial.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He usat marcadors de temps. He dit com em vaig sentir."

### A2 — Funcional


**1. Marcadors temporals**
- Seqüència i precisió: Marcadors temporals precisos (hores concretes o expressions precises: "just quan", "a mesura que").

**2. Perspectiva del cronista**
- Visibilitat i consistència: Perspectiva del cronista consistent. Selecció d'allò que el cronista ha viscut directament.

**3. Moments ordenats**
- Organització i progressió: 4-5 moments amb connexió causal. La seqüència mostra progressió i evolució de l'event.

**4. Descripcions sensorials**
- Concreció i atmosfera: Descripcions sensorials integrades a la narració (no en llista separada).

**5. Separació fets / valoració**
- Rigor i reflexió: Valoració de 2-3 frases al final, en paràgraf separat. No barrejada amb els fets.

**6. Criteris transversals**
- Connectors: Combinació de connectors temporals i 1-2 causals. La varietat reflecteix la progressió i causalitat de l'event.
- Especulació sobre tercers: Idem. Les emocions d'altri s'infereixen de comportaments observats, no s'afirmen.
- Fidelitat al text font: Fidelitat als fets, a la perspectiva, a la valoració i al to testimonial.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He separat els fets de la meva opinió. He descrit cada moment de forma sensorial."

### B1 — Estratègic


**1. Marcadors temporals**
- Seqüència i precisió: Temporalitat precisa integrada naturalment a la narració.

**2. Perspectiva del cronista**
- Visibilitat i consistència: Perspectiva del cronista amb veu pròpia clarament diferenciada dels fets.

**3. Moments ordenats**
- Organització i progressió: 5-6 moments amb detall creixent i tensió narrativa.

**4. Descripcions sensorials**
- Concreció i atmosfera: Descripcions riques: visuals, auditives, olfactives o tàctils. Integrades al text.

**5. Separació fets / valoració**
- Rigor i reflexió: Valoració argumentada que connecta l'experiència amb un context més ampli.

**6. Criteris transversals**
- Connectors: Connectors temporals i causals variats i integrats naturalment al text. Cap patró de repetició visible.
- Especulació sobre tercers: Idem. Pot incloure cites textuals d'altres participants.
- Fidelitat al text font: Fidelitat als fets, a la perspectiva, a la valoració i al context.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit una valoració argumentada al final que connecta l'experiència amb el context."

### B2 — Acadèmic


**1. Marcadors temporals**
- Seqüència i precisió: Temporalitat elaborada que reflecteix el ritme de l'experiència viscuda.

**2. Perspectiva del cronista**
- Visibilitat i consistència: Perspectiva crítica: el cronista interpreta l'event, no només el narra.

**3. Moments ordenats**
- Organització i progressió: 5-6 moments amb variació de ritme narratiu (acceleració i aturada).

**4. Descripcions sensorials**
- Concreció i atmosfera: Descripcions elaborades que creen atmosfera i situen el lector en l'experiència.

**5. Separació fets / valoració**
- Rigor i reflexió: Valoració crítica que analitza l'impacte o el significat de l'event.

**6. Criteris transversals**
- Connectors: Connectors sofisticats que reflecteixen el ritme i la intensitat de l'experiència. Pot incloure adversatius o concessius.
- Especulació sobre tercers: Idem. La perspectiva dels altres s'atribueix amb marcadors ("semblava que", "ens va dir que").
- Fidelitat al text font: Fidelitat a la complexitat experiencial del text original, incloent matisos i contradiccions.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He analitzat l'impacte de l'event des de la meva perspectiva crítica."

### C1+ — Crític


