---
name: write-divulgatiu
description: 'Use when adapting or generating a text divulgatiu for students. Activates
  when genre_discursiu == "divulgatiu". Applies narrativitzed exposition, hook entradeta,
  short cites, and rounded figures. Output: text divulgatiu in markdown with title,
  entradeta, and narrative development.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: divulgatiu
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
  equals: divulgatiu
moduls_relacionats:
- M3
macro_tipologia: explicativa
label_ca: Text divulgatiu
font_canonic: M3_genere-escriure-divulgatiu.md
font_version: 4.0.0-canonic
generat_at: '2026-06-21'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 0950228492a445e6
---

# Escriure/adaptar un text divulgatiu — skill operativa per a LLM

El text divulgatiu explica continguts científics o tècnics de manera **narrativitzada** i accessible per a un públic no especialitzat. El seu tret definitori és la **narrativització**: el contingut no es llista com a fets separats, sinó que es construeix com una historia amb causa, efecte i implicació. L'entradeta captadora (pregunta o xifra sorprenent) és la porta d'entrada al gènere.

**Tipologia MALL**: Expositiva.
**HCL principal**: Explicar — construir la relació causa-efecte d'un fenomen de manera accessible i narrativitzada.
**HCL secundàries**: Descriure — context i situació (A1-A2) · Justificar — evidències científiques atribuïdes a fonts (B2+).
**No s'adapta a pre-A1**: el text divulgatiu requereix comprendre la **narrativització d'un fenomen com a abstracció explicativa** — no enumerar fets sinó construir-ne la causalitat i la implicació. La transició BICS→CALP que és el nucli pedagògic del gènere no és accessible sense base lingüística mínima: l'alumne ha d'entendre que "per tant" i "com a conseqüència" senyalen una relació d'idees, no una successió de fets. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Narrativització com a pont BICS→CALP*: el divulgatiu és el gènere que millor fa la transició del coneixement quotidià (BICS) al coneixement acadèmic (CALP). Narrativitzar un fenomen científic significa construir-ne la historia: per què passa, com passa, quines conseqüències té. Sense narrativització, la llista de fets no construeix comprensió.
- *Entradeta com a motivació i bastida*: la pregunta o xifra inicial activa el coneixement previ de l'alumne i crea expectativa. A A1-A2, l'entradeta és la bastida que dona context sense pressuposen coneixements tècnics.
- *Cita com a model de pensament científic*: atribuir una idea a un expert ensenya a diferenciar informació de font, principi bàsic del pensament crític (B1+).

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **text divulgatiu adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Títol captador**
- Claredat i captació: Títol clar i directe. Diu el tema sense metàfores.

**2. Entradeta (ganxo)**
- Motivació i context: 1 frase que anuncia el tema.

**3. Narrativització del contingut**
- Causa-efecte i coherència: 2-3 paràgrafs molt curts. Un fet explicat com a procés (no llista de fets).

**4. Xifres arrodonides**
- Accessibilitat i context: Xifres molt simples i arrodonides: "uns quants milers".

**5. Cites i atribució**
- Credibilitat i font: Sense cites (massa complex per a A1).

**6. Exemples concrets**
- Accessibilitat i connexió: 1 exemple per paràgraf, pres del context immediat de l'alumne.

**7. Criteris transversals**
- Tecnicismes: Sense tecnicismes o amb explicació immediata entre parèntesis.
- Llargada: 2-3 paràgrafs molt curts (2-3 frases cadascun) + entradeta (1 frase).
- Fidelitat al text font: Fidelitat al fenomen principal i a la relació causal bàsica.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit un títol clar i una frase d'introducció. He explicat el tema en 2-3 paràgrafs curts."

### A1 — Inicial


**1. Títol captador**
- Claredat i captació: Títol informatiu i lleugerament captador. Sense metàfores obscures.

**2. Entradeta (ganxo)**
- Motivació i context: 2 frases: ganxo inicial (pregunta o dada) + anunci del tema.

**3. Narrativització del contingut**
- Causa-efecte i coherència: 3-4 paràgrafs narrativitzats. No llista de fets. Exemple per paràgraf.

**4. Xifres arrodonides**
- Accessibilitat i context: Xifres arrodonides i contextualitzades: "gairebé dos milions".

**5. Cites i atribució**
- Credibilitat i font: 1 cita màxim, atribució simple: "diu la científica X".

**6. Exemples concrets**
- Accessibilitat i connexió: 1 exemple concret i quotidià per paràgraf. Accessible per a l'alumne.

**7. Criteris transversals**
- Tecnicismes: Tecnicismes en negreta + explicació breu integrada al text.
- Llargada: 4-5 paràgrafs curts + entradeta.
- Fidelitat al text font: Fidelitat al fenomen, a la relació causal i a l'entradeta captadora.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit una entradeta que capta l'atenció. He explicat el tema amb exemples quotidians."

### A2 — Funcional


**1. Títol captador**
- Claredat i captació: Títol captador (pregunta o xifra sorprenent). Clar i directe.

**2. Entradeta (ganxo)**
- Motivació i context: Entradeta clara que crea expectativa sense revelar tot el contingut.

**3. Narrativització del contingut**
- Causa-efecte i coherència: 4-5 paràgrafs. El contingut s'explica com una historia (causa → efecte → implicació).

**4. Xifres arrodonides**
- Accessibilitat i context: Xifres arrodonides amb comparació: "més de dos milions, una xifra equivalent a...".

**5. Cites i atribució**
- Credibilitat i font: 1-2 cites breus. Atribució clara: "com explica la doctora X, investigadora de...".

**6. Exemples concrets**
- Accessibilitat i connexió: Exemples concrets i variats. Connectats al text, no digressius.

**7. Criteris transversals**
- Tecnicismes: Tecnicismes amb explicació contextualitzada (no glossari extern).
- Llargada: 5-6 paràgrafs + entradeta + tancament.
- Fidelitat al text font: Fidelitat al fenomen, a la relació causal i al to divulgatiu del text original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He narrativitzat el contingut (no he fet una llista de fets). He posat una cita amb nom de l'expert."

### B1 — Estratègic


**1. Títol captador**
- Claredat i captació: Títol captador i precís. Pot tenir un subratllat temàtic.

**2. Entradeta (ganxo)**
- Motivació i context: Entradeta elaborada que contextualitza el fenomen i capta l'atenció.

**3. Narrativització del contingut**
- Causa-efecte i coherència: Narrativització elaborada. Cada paràgraf avança la comprensió del fenomen.

**4. Xifres arrodonides**
- Accessibilitat i context: Xifres precises amb font i comparació contextualitzada.

**5. Cites i atribució**
- Credibilitat i font: 2-3 cites ben atribuïdes. Contrast de perspectives si escau.

**6. Exemples concrets**
- Accessibilitat i connexió: Exemples concrets amb connexió explícita amb el concepte que il·lustren.

**7. Criteris transversals**
- Tecnicismes: Tecnicismes amb precisió disciplinar. Explicació en primera menció.
- Llargada: 6-7 paràgrafs ben estructurats.
- Fidelitat al text font: Fidelitat al fenomen, a les dades, al context i al to.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He relacionat causes i efectes del fenomen. He usat dades estadístiques amb la font."

### B2 — Acadèmic


**1. Títol captador**
- Claredat i captació: Títol complex i suggeridor. Pot ser provocatiu però no obscur.

**2. Entradeta (ganxo)**
- Motivació i context: Entradeta sofisticada que situa el tema en un context ampli i crea intriga.

**3. Narrativització del contingut**
- Causa-efecte i coherència: Text narrativitzat complet. Pot incloure controvèrsies científiques presentades de forma accessible.

**4. Xifres arrodonides**
- Accessibilitat i context: Xifres amb anàlisi crítica de la seva significació estadística.

**5. Cites i atribució**
- Credibilitat i font: Múltiples fonts ben atribuïdes. Pot incloure controvèrsia científica sobre el fenomen.

**6. Exemples concrets**
- Accessibilitat i connexió: Exemples variats, alguns trets de contexts no quotidians.

**7. Criteris transversals**
- Tecnicismes: Terminologia completa. Pot assumir coneixements previs en la primera menció.
- Llargada: Text complet amb tots els elements del gènere.
- Fidelitat al text font: Fidelitat a la complexitat causal del text original, incloent matisos i controvèrsies.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He presentat el tema des de diverses perspectives i he inclòs el context científic ampli."

### C1+ — Crític


