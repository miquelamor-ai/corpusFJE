---
name: write-informe
description: 'Use when adapting or generating an informe (report) for students. Activates
  when genre_discursiu == "informe". Applies executive summary, visual data presentation,
  and clear separation of facts and conclusions. Output: informe in markdown with
  resum executiu, objectiu, mètode, resultats, and conclusions.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: informe
tipologia: Expositiva
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
  equals: informe
moduls_relacionats:
- M3
macro_tipologia: explicativa
label_ca: Informe
font_canonic: M3_genere-escriure-informe.md
font_version: 4.0.0-canonic
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 44b06c58a2a4ac8c
---

# Escriure/adaptar un informe — skill operativa per a LLM

L'informe presenta fets, dades i conclusions sobre un tema de manera organitzada, **objectiva** i sense opinió personal. El seu tret definitori és la **separació neta entre dades i conclusions**: primer es presenten els resultats observats, i al final s'expliciten les conclusions derivades. La veu impersonal consistent és el marcador estilístic nuclear del gènere.

**Tipologia MALL**: Expositiva/Justificativa.
**HCL principal**: Explicar — relació entre dades observades i conclusions derivades.
**HCL secundàries**: Descriure — les dades i el context (A1-B1) · Justificar — conclusions argumentades amb dades (B1+) · Avaluar — discussió de limitacions i implicacions (B2+).
**No s'adapta a pre-A1**: l'informe requereix la **distinció fets/conclusions com a operació metacognitiva** — ser capaç de reconèixer que "observar" i "concloure" son actes epistèmics diferenciats (el que he vist vs el que puc deduir del que he vist). Aquesta abstracció de segon nivell, combinada amb la veu impersonal consistent i la presentació de dades en format tècnic, no és accessible sense base lecto-escriptora i sense coneixements acadèmics mínims. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *CALP en acció*: l'informe és el gènere acadèmic per excel·lència. La veu impersonal, les dades numèriques i les conclusions argumentades son el CALP en la seva expressió més pura. Llegir un informe és accedir al discurs científic formal.
- *Separació dades/conclusions com a bastida del pensament crític*: la capacitat de dir "he observat X" (descripció objectiva) i "per tant puc concloure Y" (inferència justificada) és la competència nuclear del mètode científic. El connector "per tant" marca l'epistemologia de l'informe.
- *Hipòtesi "Si..., llavors..." com a bastida del pensament científic*: formular una hipòtesi explícita és el primer pas del mètode científic (B1+). La bastida lingüística ("Si..., llavors...") és el pont entre la pregunta de recerca i la metodologia.
- *Multimodalitat al servei de la precisió*: taules i gràfics no son decoració sinó el format natiu de les dades quantitatives. A B2+, la capacitat de llegir i interpretar representacions visuals és part de la competència científica.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu l'**informe adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Introducció / Resum executiu**
- Orientació i síntesi: 1-2 frases que diuen de qué tracta l'informe.

**2. Presentació de dades**
- Format i objectivitat: 3-5 dades en frases simples o llista simple (dada / valor). Nombre + unitat. Taula de 2 columnes admissible com a bastida visual.

**3. Separació dades / conclusions**
- Rigor epistèmic: Dades primer ("hem vist que X"). Conclusions separades ("per tant, Y").

**4. Objectivitat (veu impersonal)**
- Coherència estilística: Sense frases personals ("jo crec que..."). Impersonal simple.

**5. Hipòtesi i metodologia**
- Rigor metodològic: Sense hipòtesi (massa complex per a A1). Una descripció mínima del procediment.

**6. Conclusions i recomanacions**
- Profunditat argumentativa: 1 conclusió simple derivada de les dades: "Hem après que..."

**7. Criteris transversals**
- Opinió personal: Cap frase en primera persona singular valorativa ("jo crec", "m'agrada", "penso que").
- Dades sense font: A A1: no cal font.
- Fidelitat al text font: Fidelitat a les dades principals i a la conclusió bàsica.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He presentat les dades i les conclusions per separat."

### A1 — Inicial


**1. Introducció / Resum executiu**
- Orientació i síntesi: Introducció de 2-3 frases: qué s'ha estudiat i per qué.

**2. Presentació de dades**
- Format i objectivitat: Dades organitzades en llista o taula simple. Unitats explícites.

**3. Separació dades / conclusions**
- Rigor epistèmic: Dades i conclusions en blocs separats. Connector explícit: "per tant", "com a conclusió".

**4. Objectivitat (veu impersonal)**
- Coherència estilística: Veu impersonal consistent: "s'observa que", "els resultats indiquen que".

**5. Hipòtesi i metodologia**
- Rigor metodològic: Pot incloure una pregunta inicial que l'informe respon.

**6. Conclusions i recomanacions**
- Profunditat argumentativa: 1-2 conclusions derivades de les dades. Connector "per tant".

**7. Criteris transversals**
- Opinió personal: Idem. Passiva o impersonal en tot el text.
- Dades sense font: A A2: la font de les dades s'indica si és externa.
- Fidelitat al text font: Fidelitat a les dades, a la conclusió i a la separació dades/conclusions.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He organitzat les dades. He escrit qué hem après al final."

### A2 — Funcional


**1. Introducció / Resum executiu**
- Orientació i síntesi: Resum executiu: 1 paràgraf que indica l'objectiu i la conclusió principal. No detalla les dades (per evitar duplicació amb el cos).

**2. Presentació de dades**
- Format i objectivitat: Dades organitzades per categories. Pot incloure comparació entre valors.

**3. Separació dades / conclusions**
- Rigor epistèmic: Separació neta entre resultats i conclusions en seccions diferenciades. Sense barreja.

**4. Objectivitat (veu impersonal)**
- Coherència estilística: Vocabulari objectiu i tècnic. Sense adjectius subjectius. Impersonal (es + verb) prioritari; passiva opcional.

**5. Hipòtesi i metodologia**
- Rigor metodològic: Hipòtesi "Si..., llavors..." explícita. Metodologia en 2-3 frases.

**6. Conclusions i recomanacions**
- Profunditat argumentativa: 2-3 conclusions argumentades. Pot incloure 1 recomanació derivada de les conclusions.

**7. Criteris transversals**
- Opinió personal: Idem. Les opinions es reformulen en impersonal o s'eliminen.
- Dades sense font: A B1+: totes les dades externes porten font atribuïda.
- Fidelitat al text font: Fidelitat a les dades, a la metodologia, a la conclusió i al to objectiu.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit la hipòtesi i la metodologia. Les conclusions deriven de les dades."

### B1 — Estratègic


**1. Introducció / Resum executiu**
- Orientació i síntesi: Resum executiu amb les conclusions principals davant dels resultats.

**2. Presentació de dades**
- Format i objectivitat: Dades en taules o gràfics simples. Descripció objectiva de les dades (sense conclusió).

**3. Separació dades / conclusions**
- Rigor epistèmic: Dades comentades objectivament i conclusions argumentades per separat amb connector explícit.

**4. Objectivitat (veu impersonal)**
- Coherència estilística: Objectivitat rigurosa. Pot incloure citació de fonts per a afirmacions.

**5. Hipòtesi i metodologia**
- Rigor metodològic: Hipòtesi i metodologia ben descrites. Variables identificades (independent/dependent).

**6. Conclusions i recomanacions**
- Profunditat argumentativa: Conclusions argumentades + recomanacions basades en les dades. Connexió explícita dades→conclusions.

**7. Criteris transversals**
- Opinió personal: Idem. Pot incloure valoració de la metodologia en impersonal ("la mostra podria ser més gran").
- Dades sense font: Idem. Les dades sense font son observacions pròpies (s'indica explícitament).
- Fidelitat al text font: Fidelitat a les dades, a la metodologia, al context i al to acadèmic.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Les meves conclusions estan argumentades amb dades. He separat dades d'opinions."

### B2 — Acadèmic


**1. Introducció / Resum executiu**
- Orientació i síntesi: Resum executiu professional que permet comprendre l'informe sense llegir el cos complet.

**2. Presentació de dades**
- Format i objectivitat: Dades en formats variats (taules, gràfics, diagrames). Anàlisi estadística si escau.

**3. Separació dades / conclusions**
- Rigor epistèmic: Separació rigorosa. Les conclusions deriven explícitament i raonada de les dades.

**4. Objectivitat (veu impersonal)**
- Coherència estilística: Objectivitat acadèmica amb reconeixement de limitacions i incerteses del procés.

**5. Hipòtesi i metodologia**
- Rigor metodològic: Hipòtesi, variables, limitacions metodològiques i fonts en la metodologia.

**6. Conclusions i recomanacions**
- Profunditat argumentativa: Conclusions amb discussió de les limitacions, propostes de recerca futures i reconeixement d'incerteses.

**7. Criteris transversals**
- Opinió personal: Les limitacions i els dubtes s'expliciten com a observació científica, no com a opinió.
- Dades sense font: Rigor bibliogràfic complet. Diferència entre dades pròpies, dades secundàries i estimacions.
- Fidelitat al text font: Fidelitat a la complexitat analítica del text original, incloent limitacions i debats.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'informe és rigorós, objectiu i les conclusions estan justificades. He reconegut les limitacions."

### C1+ — Crític


