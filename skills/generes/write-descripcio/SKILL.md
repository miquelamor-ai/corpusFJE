---
name: write-descripcio
description: 'Use when adapting or generating a descripció for students. Activates
  when genre_discursiu == "descripcio". Applies explicit spatial order, concrete comparisons,
  and separation of physical and emotional traits. Output: descripció in markdown
  with title, general description, and characteristics.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: descripcio
tipologia: Expositiva / Descriptiva
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
  equals: descripcio
moduls_relacionats:
- M3
macro_tipologia: descriptiva
label_ca: Descripció
font_canonic: M3_genere-escriure-descripcio.md
font_version: 4.0.0-canonic
generat_at: '2026-06-21'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: add77b7c71a804e8
---

# Escriure/adaptar una descripció — skill operativa per a LLM

La descripció presenta les característiques d'un objecte, persona, lloc o fenomen amb **ordre espacial** i **concreció progressiva**. El seu tret definitori és el recorregut sistemàtic: de dalt a baix, de fora a dins, de conjunt a detall. A diferència del conte, no hi ha temps ni acció; a diferència de l'informe, no hi ha dades ni conclusions.

**Tipologia MALL**: Descriptiva.
**HCL principal**: Descriure — identificar i caracteritzar les parts d'un objecte, lloc, persona o fenomen.
**HCL secundàries**: Explicar — relacionar característiques entre si i amb la funció (B1+).
**S'adapta a pre-A1**: la descripció és el gènere que millor s'adapta a la fase emergent/logogràfica. A pre-A1, l'alumne assenyala, nomena oralment o dicta a l'adult; la imatge o l'objecte real fa de bastida total. L'adult medeia el significat sense que l'alumne hagi d'inferir res abstracte: cada part es pot assenyalar, cada adjectiu es pot il·lustrar. Filtre D6: (1) l'adult pot mediar amb imatges i gest sense que l'alumne infereixi cap abstracció; (2) el gènere no requereix plans simultanis, abstracció temporal ni significat diferit.

**Connexions MALL transversals:**
- *Descripció com a HCL fonamental*: la descripció és la HCL inicial de tot el currículum. Tots els gèneres complexos (biografia, informe, divulgatiu) contenen descripcions com a submòdul. L'alumne que aprèn a descriure bé té la base de tots els altres gèneres.
- *Ordre espacial com a bastida del pensament*: l'ordre "de dalt a baix" o "de fora a dins" no és una convenció literària; és una bastida cognitiva. Externalitza el recorregut del pensament i el fa visible.
- *Multimodalitat com a accés pre-A1*: a pre-A1 i A1, la imatge o l'objecte real és la descripció. L'alumne descriu el que veu; la producció lingüística és secundària o oral. Aquesta mediació visual és la porta d'entrada al gènere i es manté com a suport fins a A2.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **descripció adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast i en produeix els seus textos.
**Sub-granularitat dins de pre-A1 i A1**: es treballa amb `fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]`. A pre-A1 logogràfic, la descripció és oral i mediada; no hi ha text llegit per l'alumne, només el suport visual.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Identificació de l'objecte**
- Precisió i situació: Assenyalar i dir el nom oralment. Dictat a l'adult.

**2. Ordre espacial**
- Seqüència i coherència: Llista oral de noms (parts assenyalades a la imatge o objecte real).

**3. Adjectius**
- Varietat i precisió: Pictograma o imatge en lloc d'adjectius escrits.

**4. Comparacions concretes**
- Accessibilitat i precisió: Assenyalar l'objecte real o la imatge (sense text).

**5. Separació descripció física / funcional**
- Distinció i organització: Enumeració oral de parts (sense separació).

**6. Criteris transversals**
- Llargada: Enumeració oral. Dictat a l'adult (format llista).
- Adjectius subjectius: Cap adjectiu subjectiu (ni oral ni escrit). Tots referits a la imatge real.
- Fidelitat al text font: Fidelitat a les parts visibles de l'objecte o imatge presentat.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He assenyalat les parts i he dit el nom." (oral)

### A1 — Inicial


**1. Identificació de l'objecte**
- Precisió i situació: 1 frase que diu què és: "Això és un ocell."

**2. Ordre espacial**
- Seqüència i coherència: 3-4 característiques ordenades de dalt a baix o de fora a dins. Una per frase.

**3. Adjectius**
- Varietat i precisió: Adjectius molt freqüents i concrets: "vermell", "gran", "rodó".

**4. Comparacions concretes**
- Accessibilitat i precisió: Comparacions molt quotidianes: "és com una pilota", "és del color del cel".

**5. Separació descripció física / funcional**
- Distinció i organització: Descripció física únicament. Una característica per frase.

**6. Criteris transversals**
- Llargada: 3-4 frases. Format llista o frases simples.
- Adjectius subjectius: Cap adjectiu valoratiu genèric ("bonic", "especial"). Tots concrets i verificables.
- Fidelitat al text font: Fidelitat a les característiques principals de l'objecte o persona descrits.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He descrit 3-4 parts del [objecte/lloc/persona] en ordre."

### A2 — Funcional


**1. Identificació de l'objecte**
- Precisió i situació: Frase general que situa l'objecte amb categoria: "El colibrí és un ocell molt petit."

**2. Ordre espacial**
- Seqüència i coherència: 5-6 característiques en ordre espacial explícit amb connectors simples.

**3. Adjectius**
- Varietat i precisió: Adjectius variats i concrets. Sense subjectius genèrics ("bonic", "interessant").

**4. Comparacions concretes**
- Accessibilitat i precisió: Comparacions concretes i variades: "de la mida d'una mà", "tan llarg com un llapis".

**5. Separació descripció física / funcional**
- Distinció i organització: Distinció incipient entre descripció física i descripció funcional en frases separades. Al menys una frase conté el connector "serveix per" o "s'utilitza per".

**6. Criteris transversals**
- Llargada: 5-6 frases o 1-2 paràgrafs curts.
- Adjectius subjectius: Idem.
- Fidelitat al text font: Fidelitat a les característiques i a la funció essencial.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He descrit les característiques seguint un ordre de l'exterior a l'interior (o de dalt a baix)."

### B1 — Estratègic


**1. Identificació de l'objecte**
- Precisió i situació: Descripció general amb categoria i 1 tret diferencial: "El colibrí és un ocell diminut conegut pel seu vol estacionari."

**2. Ordre espacial**
- Seqüència i coherència: 6-8 característiques amb ordre espacial clar i progressiu. Connectors: "a la part superior", "al centre".

**3. Adjectius**
- Varietat i precisió: Adjectius precisos i variats del camp lèxic de la unitat. Sense superlatius sintètics.

**4. Comparacions concretes**
- Accessibilitat i precisió: Comparacions funcionals: "té X, que permet Y". Pot comparar amb elements de la mateixa categoria.

**5. Separació descripció física / funcional**
- Distinció i organització: Separació explícita entre descripció física i funció o impacte en paràgrafs o blocs diferenciats.

**6. Criteris transversals**
- Llargada: 1-2 paràgrafs amb 6-8 característiques.
- Adjectius subjectius: Idem.
- Fidelitat al text font: Fidelitat a les característiques, la funció i el to factual del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He relacionat algunes característiques entre si i amb la funció. He revisat que l'ordre sigui espacial."

### B2 — Acadèmic


**1. Identificació de l'objecte**
- Precisió i situació: Descripció general amb context i funció integrats.

**2. Ordre espacial**
- Seqüència i coherència: Ordre espacial respectat amb matisos i descripció funcional integrada.

**3. Adjectius**
- Varietat i precisió: Adjectius precisos del camp lèxic de la matèria. Superlatius analítics admissibles.

**4. Comparacions concretes**
- Accessibilitat i precisió: Comparació amb altres elements de la mateixa categoria amb matís.

**5. Separació descripció física / funcional**
- Distinció i organització: Descripció física, funcional i emocional ben diferenciades.

**6. Criteris transversals**
- Llargada: 2-3 paràgrafs complets.
- Adjectius subjectius: Idem. Superlatius d'ordre espacial o quantitatiu admissibles si son terminologia ("el punt més alt", "la zona més densa").
- Fidelitat al text font: Fidelitat a les característiques, la funció, el context i el to.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He fet una descripció detallada i precisa amb vocabulari específic. He separat descripció física i funcional."

### C1+ — Crític


**1. Identificació de l'objecte**
- Precisió i situació: Descripció general amb matisos conceptuals i terminologia precisa.

**2. Ordre espacial**
- Seqüència i coherència: Ordre espacial exhaustiu amb matisos conceptuals i terminologia específica de la disciplina.

**3. Adjectius**
- Varietat i precisió: Adjectius tècnics i de matís conceptual. Terminologia disciplinar.

**4. Comparacions concretes**
- Accessibilitat i precisió: Comparació de l'objecte amb arquetips o fenòmens de la mateixa disciplina per precisar-ne el matís diferencial.

**5. Separació descripció física / funcional**
- Distinció i organització: Distinció terminològica entre descripció observable i processos subjacents.

**6. Criteris transversals**
- Llargada: Text complet amb tots els matisos necessaris.
- Adjectius subjectius: Idem. Terminologia valorativa disciplinar admissible si s'usa en el camp lèxic corresponent.
- Fidelitat al text font: Fidelitat a la complexitat descriptiva del text original, incloent matisos i terminologia.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He descrit amb matisos conceptuals i he relacionat les característiques amb processos. He revisat que no hi hagi adjectius subjectius no disciplinars."

