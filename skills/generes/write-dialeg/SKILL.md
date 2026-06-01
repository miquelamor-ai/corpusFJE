---
name: write-dialeg
description: 'Use when adapting or generating a dialeg (dialogue) for students. Activates
  when genre_discursiu == "dialeg". Applies character list, named attribution, present-tense
  stage directions, and explicit subtext. Output: dialeg in markdown with characters,
  stage directions, and turns.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: dialeg
tipologia: Dialogada
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
  equals: dialeg
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-dialeg.md
font_version: 4.0.0-canonic
generat_at: '2026-06-01'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 827f1dbb0a98af34
---

# Escriure/adaptar un diàleg — skill operativa per a LLM

El dialeg és un genere teatral que representa una conversa entre personatges amb estructura formal: llista de personatges, acotacions i torns de paraula clarament atribuïts per nom. El seu tret definitori és el **language-in-action**: el significat no és al text, sino a l'intercanvi entre personatges, al que es diu i al que no es diu (subtext). La seva funcio pedagogica és treballar la representacio de la interaccio social i emocional a traves del text escrit.

**Tipologia MALL**: Dialogada.
**HCL principal**: Narrar (language-in-action) — co-construir un intercanvi seqüenciat entre personatges amb tensio i resolucio.
**HCL secundaries**: Argumentar (conflicte verbal, B1+) · Interpretar/Valorar (subtext i intencio, B2+).
**Nota MALL**: el dialeg escrit és la bastida de la dramatitzacio oral. A A1, llegir els torns en veu alta amb el company és la primera produccio oral estructurada. El dialeg conecta l'eix oral (dramatitzacio) amb l'eix escrit (text formal) en un sol instrument.
**No s'adapta a pre-A1 (D6)**: el format teatral requereix llegir i atribuir torns per nom, seguir l'estructura formal de personatges i acotacions, i comprendre la relacio entre el que es diu i el que es fa (subtext). Aquesta doble cognicao (text + situacio dramatica) no és accessible sense base lectora. Per a pre-A1, millor dramatitzacio oral espontania sense format escrit.

**Connexions MALL transversals:**
- *Subtext com a pensament critic*: el subtext explícit a les acotacions fa visible la diferencia entre el que es diu i el que es pensa. És una entrada natural al pensament critic: "Que diu el personatge? Que vol dir realment?" Aquesta dualitat és la bastida del raonament interpretiu (HCL Interpretar/Valorar, B2+).
- *Atribucio com a responsabilitat discursiva*: aprendre a atribuir torns per nom (no per lletra) és aprendre a fer-se responsable de les paraules propies i alienes. La norma de l'atribucio por nom és una norma de claredad i de respecte.
- *Dramatitzacio com a mediacio*: el dialeg escrit és la bastida de la dramatitzacio oral. A A1, llegir els torns en veu alta per parelles és la primera produccio oral estructurada en la llengua nova (TILC).

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **dialeg adaptat per a la LECTURA** de l'alumne. **No descriu la produccio autonoma** — la produccio és tasca d'un derivat propi. Principi pedagogic MALL: l'alumne llegeix models al maxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logografic perque el genere requereix llegir i atribuir torns.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Llista de personatges**
- Presentació: 2 personatges llistats amb nom. Sense descripcio.

**2. Atribucio de torns**
- Claredat formal: Torns atribuïts per nom en negreta: **Marc:** / **Sofia:**. Mai amb inicials o lletres (A:, B:).

**3. Acotacions**
- Subtext i accio: Acotacio molt simple: "En Marc entra." / "La Sofia somriu." Present, 3a persona. 1 accio.

**4. Conflicte**
- Tensio dramatica: Tensio simple en 1 torn: "Vull X. — No pots."

**5. Nombre de torns**
- Extensio: 6-8 torns totals. 1-2 frases per torn.

**6. Criteris transversals**
- Format i fidelitat: Llista de personatges present al principi. Cap torn amb inicials. Cap acotacio amb ironia. Manté personatges i conflicte principals del text font.

**7. Autoavaluacio**
- Metacognicao: "He escrit qui parla a cada torn. He posat 6-8 torns entre 2 personatges."

### A1 — Inicial


**1. Llista de personatges**
- Presentació: 2 personatges amb 1 linia de descripcio cadascun.

**2. Atribucio de torns**
- Claredat formal: Torns atribuïts per nom en negreta. Format consistent al llarg del dialeg.

**3. Acotacions**
- Subtext i accio: 1 accio per acotacio, sense subordinades. Present, 3a persona. Subtext explícit senzill.

**4. Conflicte**
- Tensio dramatica: Conflicte simple i resolucio clara en 6-8 torns.

**5. Nombre de torns**
- Extensio: 8-10 torns. Frases fins a 10 paraules per torn.

**6. Criteris transversals**
- Format i fidelitat: Idem. Subtext explícit a les acotacions. La resolucio del conflicte és clara. Manté l'ordre i la resolucio del text font.

**7. Autoavaluacio**
- Metacognicao: "He posat acotacions que expliquen el que fa el personatge."

### A2 — Funcional


**1. Llista de personatges**
- Presentació: 2-3 personatges amb descripcio i relacio entre ells.

**2. Atribucio de torns**
- Claredat formal: Torns atribuïts per nom. L'atribucio mai és ambigua (cap torn "flotant").

**3. Acotacions**
- Subtext i accio: Acotacio amb subtext emocional explícit: "[La Sofia fa un pas enrere, preocupada.]"

**4. Conflicte**
- Tensio dramatica: Conflicte amb 2 punts de vista diferenciats. Inclou 1 moment d'argumentacio.

**5. Nombre de torns**
- Extensio: 10-12 torns. Frases de fins a 15 paraules per torn.

**6. Criteris transversals**
- Format i fidelitat: Idem. Les acotacions no confonen accio amb judici. Manté els punts de vista dels personatges del text font.

**7. Autoavaluacio**
- Metacognicao: "He escrit un conflicte i una resolucio. He explicat el subtext a les acotacions."

### B1 — Estratègic


**1. Llista de personatges**
- Presentació: 3-4 personatges amb tret diferenciador i funcio en el conflicte.

**2. Atribucio de torns**
- Claredat formal: Torns atribuïts amb nom + acotacio breu si la veu pot confondre's.

**3. Acotacions**
- Subtext i accio: Acotacions que revelen intencions no dites. 1 accio per acotacio.

**4. Conflicte**
- Tensio dramatica: Conflicte complex amb postures elaborades per cada personatge.

**5. Nombre de torns**
- Extensio: 12-15 torns. Frases elaborades.

**6. Criteris transversals**
- Format i fidelitat: Idem. Manté matisos i complexitat del conflicte original. L'acotacio pot contradir o matisar el torn si escau.

**7. Autoavaluacio**
- Metacognicao: "He escrit torns que mostren les postures dels personatges sense explicar-les totes."

### B2 — Acadèmic


**1. Llista de personatges**
- Presentació: 3-4 personatges amb motivacio i postura explícites.

**2. Atribucio de torns**
- Claredat formal: Torns atribuïts per nom. La veu de cada personatge és diferenciada lingüísticament.

**3. Acotacions**
- Subtext i accio: Acotacions detallades amb subtext complex. Sense ironia ni judicis sobre el personatge.

**4. Conflicte**
- Tensio dramatica: Conflicte de valors o de visions del mon. Resolucio no necessariament clara.

**5. Nombre de torns**
- Extensio: 12-15+ torns. Llargada variable segons el ritme dramatic.

**6. Criteris transversals**
- Format i fidelitat: Idem. Manté intencio retorica i matisos del text font. Sense monolegs interns llargs.

**7. Autoavaluacio**
- Metacognicao: "He creat un conflicte complex amb subtext ric i intencio retorica visible."

### C1+ — Crític


