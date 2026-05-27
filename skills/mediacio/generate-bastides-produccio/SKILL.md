---
name: generate-bastides-produccio
description: 'Use when the teacher has activated the "bastides" complement AND at
  least one production complement is active (preguntes_comprensio or activitats_aprofundiment).
  Generates production scaffolds: (A) base d''orientació — genre-specific GPS with
  disciplinary reasoning steps; (B) catàleg de recursos — MECR-graduated connectors
  and HCL initiators; (C) pauta d''interrogació — self-assessment checklist. At Emergent/pre-A1:
  nothing generated — zero written production.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: bastides
agent_role: complements
tools_required: []
triggers:
- all_of:
  - path: params.complements.bastides
    equals: true
  - any_of:
    - path: params.complements.preguntes_comprensio
      equals: true
    - path: params.complements.activitats_aprofundiment
      equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-bastides-produccio.md
font_version: 4.0.0-canonic
generat_at: '2026-05-26'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: a02fd39f2a5d7efc
---

# Generar bastides de producció — skill operativa per a LLM

Les bastides de producció guien el procés d'escriptura de l'alumne en tres blocs complementaris: **(A) base d'orientació**, **(B) catàleg de recursos** i **(C) pauta d'interrogació**. Constitueixen el GPS de la producció textual: mostren a l'alumne el camí per construir el text del gènere treballat, pas a pas i amb els recursos lingüístics del seu nivell MECR.

**Tipologia MALL**: Mediació cognitiva (bastida de producció).
**HCL associada**: cap HCL pròpia — el complement suporta la HCL productiva del gènere actiu (Narrar, Argumentar, Descriure, Explicar, etc.). El Bloc B adapta els iniciadors a la HCL del gènere.
**Activació condicional**: ÚNICAMENT si hi ha producció activa al Pas 2. Si el docent activa "bastides" sense activar `preguntes_comprensio` o `activitats_aprofundiment`, aquest complement NO genera res. La senyera: "Sense producció no hi ha bastida de producció."
**Principi rector**: el Bloc A SEMPRE és disciplinar i específic del gènere i la matèria. Mai "introduccio / cos / conclusio". Una base d'orientació genèrica és pitjor que cap: desorientació disfressada d'estructura.

**No s'adapta a pre-A1 (D6)**: zero escriptura autònoma a fase logografica i alfabetica emergent primerenca. La producció requereix tenir la mecànica de la frase interioritzada com a mínim en la seva forma rudimentaria. A pre-A1 no hi ha cap bloc generat; si el docent activa el complement, es salta silenciosament.

**Diferència crítica amb bastides-lectura:**
- `bastides-lectura`: sempre actiu quan el docent activa "bastides"; guia el PROCÉS LECTOR.
- `bastides-produccio`: condicional (requereix producció activa); guia el PROCÉS D'ESCRIPTURA.
- Els dos complements son ortogonals i complementaris: mai duplicar contingut entre ells.

**Connexions MALL transversals:**
- *Base d'orientació com a GPS disciplinar*: el Bloc A no és un índex de seccions sinó el procediment mental expert per a aquell gènere i aquella matèria. Per a una crònica de ciències: "1. Quan, on i qui. 2. Quin fenomen. 3. Quines causes. 4. Quines conseqüències." Per a un assaig de filosofia: "1. Tesi pròpia. 2. Evidència 1 i refutació. 3. Evidència 2. 4. Conclusió-implicació." El gènere i la matèria determinen els passos.
- *Catàleg de recursos com a vocabulari actiu*: els iniciadors del Bloc B no son per llegir — son per usar mentre s'escriu. Menys iniciadors (2-3 per HCL) és millor que una llista inabastable. L'alumne ha de triar, no copiar mecànicament.
- *Pauta d'interrogació com a metaregulació*: el Bloc C desplaça la regulació externa del docent cap a la regulació interna de l'alumne. La pregunta "He justificat amb exemples del text?" activa el monitoratge metacognitiu que és el preludi de l'escriptura autònoma.
- *Bastida retirable (ZDP)*: el Bloc A es retira quan l'alumne ha internalitzat l'estructura del gènere. El Bloc B es retira quan l'alumne usa els connectors sense necessitat de consulta. El Bloc C es retira quan l'alumne s'autoavaluà espontàniament. La bastida té vocació d'extingir-se.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **bastides que es generen per orientar la producció escrita de l'alumne** (PRODUCCIÓ). **No descriu la producció autònoma de l'alumne ni l'avaluació del docent**: el docent observa si l'alumne usa la bastida com a suport i si la seva producció millorat amb ella.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: alfabetica_emergent` (frases simples, bastida mínima) i `alfabetica_fluida` (frases completes, bastida plena).

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Bloc A — Base d'orientació**
- GPS disciplinar: 2-3 passos molt concrets amb terminologia disciplinar de la matèria. Cada pas = 1 frase imperativa breu.

**2. Bloc B — Catàleg de recursos**
- Connectors + iniciadors HCL: 1 iniciador per HCL principal del gènere. Connectors: *i, però, perquè*. Llista curta (max 5 ítems).

**3. Bloc C — Pauta d'interrogació**
- Checklist d'autoavaluació: Cap pauta a A1: la bastida és el Bloc A i B.

**4. Autoavaluació mediada**
- Metacognició: "He seguit els passos de la bastida per escriure el meu text."

### A1 — Inicial


**1. Bloc A — Base d'orientació**
- GPS disciplinar: 3-4 passos + terminologia disciplinar específica. Cada pas indica QUÈ fer i AMB QUÈ.

**2. Bloc B — Catàleg de recursos**
- Connectors + iniciadors HCL: 2-3 iniciadors per HCL. Connectors: + *primer, llavors, per tant*. Connectors de causa-efecte.

**3. Bloc C — Pauta d'interrogació**
- Checklist d'autoavaluació: 2-3 ítems simples vinculats al gènere i la tasca concreta. Com a mínim un ítem sobre el destinatari o el propòsit (ex.: "A qui escric? He posat el nom del personatge?").

**4. Autoavaluació mediada**
- Metacognició: "He usat la bastida per estructurar el meu text. He completat el checklist."

### A2 — Funcional


**1. Bloc A — Base d'orientació**
- GPS disciplinar: Raonament disciplinar explícit: hipòtesi, evidència, causa, efecte. Vocabulari CALP del camp.

**2. Bloc B — Catàleg de recursos**
- Connectors + iniciadors HCL: Iniciadors inferencials i causals. Connectors: + *ja que, en canvi, tot i que*. Iniciadors de contrast.

**3. Bloc C — Pauta d'interrogació**
- Checklist d'autoavaluació: 4-5 ítems específics del gènere. Vinculats als criteris d'avaluació si estan disponibles.

**4. Autoavaluació mediada**
- Metacognició: "He seguit la base d'orientació i he usat els iniciadors per construir el meu argument."

### B1 — Estratègic


**1. Bloc A — Base d'orientació**
- GPS disciplinar: Superestructura completa del gènere amb lèxic CALP i indicadors de qualitat per secció.

**2. Bloc B — Catàleg de recursos**
- Connectors + iniciadors HCL: Iniciadors CALP argumentals. Connectors: + *no obstant, atès que, en conseqüència* (NOMES a B2+).

**3. Bloc C — Pauta d'interrogació**
- Checklist d'autoavaluació: Criteris d'avaluació específics amb indicadors observables. Inclou criteris de rigor disciplinar.

**4. Autoavaluació mediada**
- Metacognició: "He usat la pauta d'interrogació per revisar que el meu text compleix els criteris del gènere."

### B2 — Acadèmic


**1. Bloc A — Base d'orientació**
- GPS disciplinar: Contrast de fonts, biaix autorial, intertextualitat. El GPS inclou indicadors de rigor crític.

**2. Bloc B — Catàleg de recursos**
- Connectors + iniciadors HCL: Iniciadors dialèctics i retòrics. Connectors de concessió i contrast complexos.

**3. Bloc C — Pauta d'interrogació**
- Checklist d'autoavaluació: Reflexió metacognitiva sobre fiabilitat de les fonts, biaix i coherència interna de l'argument.

**4. Autoavaluació mediada**
- Metacognició: "He comprovat que les meves fonts son fiables i que el meu argument és coherent i honest."

### C1+ — Crític


