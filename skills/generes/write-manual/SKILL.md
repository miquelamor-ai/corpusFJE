---
name: write-manual
description: 'Use when adapting or generating a manual (text expositiu instructiu)
  for students. Activates when genre_discursiu == "manual". Applies gradual progression
  (simple to complex), explicit causal connectors, and defined technical terms. Output:
  manual in markdown with title, entradeta, and ordered sections.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: manual
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
  equals: manual
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-manual.md
font_version: 4.0.0-canonic
generat_at: '2026-06-01'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 186ab4d2592520d2
---

# Escriure/adaptar un manual — skill operativa per a LLM

El manual és un text expositiu organitzat en **apartats progressius** que presenta coneixements de manera sistemàtica, de simple a complex. El seu tret definitori és la **progressió epistèmica**: cada apartat es recolza conceptualment en l'anterior, els termes tècnics estan definits a la primera aparició, i els exemples concrets precedeixen sempre les abstraccions.

**Tipologia MALL**: Expositiva/Progressiva.
**HCL principal**: Explicar — exposar un conjunt de conceptes relacionats de manera progressiva i sistemàtica.
**HCL secundàries**: Descriure — definir i caracteritzar termes tècnics nous (A1-B1) · Justificar — explicar per qué els conceptes s'ordenen de la manera que s'ordenen (B1+).
**No s'adapta a pre-A1**: el manual requereix la comprensió de la **progressió simple→complex com a estructura epistèmica** — entendre que els apartats estan en un cert ordre perquè cada un es recolza conceptualment en l'anterior implica la comprensió de la jerarquia i la dependència conceptual entre idees. Aquesta abstracció estructural requereix base lecto-escriptora mínima i familiaritat mínima amb les categories de la matèria. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *HCL Explicar com a CALP operatiu*: el manual és el gènere on la HCL Explicar és més pura i sistemàtica. Llegir i escriure manuals és aprendre a estructurar l'exposició del coneixement: la competència acadèmica transversal per excel·lència, transferible a totes les matèries.
- *Desnominalitzar com a estratègia d'accés al CALP*: convertir noms abstractes en processos verbals ("l'oxidació" → "quan un metall s'oxida") és una estratègia de simplificació sense pèrdua de rigor. Permet l'accés al CALP des del BICS: l'alumne llegeix un concepte acadèmic en la seva forma processal accessible.
- *Exemple primer com a bastida ZDP*: presentar l'exemple concret ABANS del principi abstracte és aplicar la teoria de Vygotsky. L'alumne ancora el nou concepte en el que ja coneix i llavors pot generalitzar. L'ordre exemple→abstracció és la regla d'or del manual accessible.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **manual adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Entradeta**
- Context i anunci: 1 frase que diu qué s'explicarà. Directa i concreta.

**2. Progressió simple→complex**
- Estructura i coherència: 3 apartats. Ordre estricte: el més simple primer. Un concepte per apartat.

**3. Definició de termes tècnics**
- Accessibilitat i precisió: 1 terme per apartat, definit al costat en parèntesi: "el fotó (una partícula de llum)".

**4. Exemple concret primer**
- Ordre i ancoratge ZDP: Exemple molt quotidià ABANS del principi abstracte. "La sal es dissol a l'agua → l'osmosi és...".

**5. Connectors causals**
- Explicitació de relacions: "Perquè", "per això". 1 per apartat. Simple i clar.

**6. Criteris transversals**
- Desnominalitzar processos: Convertir noms abstractes en processos verbals: "oxidació" → "quan s'oxida". A1: sempre.
- No referència futura: Cap "ho veurem més endavant" ni referència a apartats posteriors. El text és autocontingut.
- Fidelitat al text font: Fidelitat als conceptes principals i a la progressió bàsica.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit 3 apartats. He explicat un terme difícil de cada apartat."

### A1 — Inicial


**1. Entradeta**
- Context i anunci: 2 frases: qué s'explicarà i per qué és útil.

**2. Progressió simple→complex**
- Estructura i coherència: 3 apartats progressius. Cada un es recolza en l'anterior de manera explícita.

**3. Definició de termes tècnics**
- Accessibilitat i precisió: 1 terme per apartat en negreta amb definició integrada a la frase.

**4. Exemple concret primer**
- Ordre i ancoratge ZDP: Exemple concret per apartat. L'abstracció ve SEMPRE DESPRÉS de l'exemple.

**5. Connectors causals**
- Explicitació de relacions: "Perquè", "per tant", "d'aquesta manera". Variats mínimament.

**6. Criteris transversals**
- Desnominalitzar processos: Idem. "la fotosíntesi" → "quan les plantes fabriquen aliment".
- No referència futura: Idem. Cap referència lateral o nota al peu que interrompi el flux.
- Fidelitat al text font: Fidelitat als conceptes, a la progressió i a les definicions essencials.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He posat un exemple per a cada concepte. He usat 'perquè' o 'per això' per explicar les causes."

### A2 — Funcional


**1. Entradeta**
- Context i anunci: Entradeta que anuncia els apartats i la seva progressió lògica.

**2. Progressió simple→complex**
- Estructura i coherència: 3-5 apartats. Progressió lògica explicitada a l'entradeta o als subtítols.

**3. Definició de termes tècnics**
- Accessibilitat i precisió: Termes tècnics en negreta definits a la primera aparició. Cap terme tècnic sense definir.

**4. Exemple concret primer**
- Ordre i ancoratge ZDP: Exemple que connecta el concepte nou amb el que l'alumne ja sap (ZDP). L'ordre és sagrat.

**5. Connectors causals**
- Explicitació de relacions: "Com a resultat", "per tant", "d'aquí se'n deriva". Variats. Distinció causa/efecte explícita.

**6. Criteris transversals**
- Desnominalitzar processos: Idem. La desnominalització és la estratègia principal per fer accessible el CALP.
- No referència futura: Idem. Cap nota al peu a A1-B1.
- Fidelitat al text font: Fidelitat als conceptes, a la progressió, a les definicions i als connectors causals del text font.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Els meus apartats van de més simple a més complex. Cada terme tècnic té la seva definició."

### B1 — Estratègic


**1. Entradeta**
- Context i anunci: Entradeta que contextualitza el manual i el seu objectiu dins del camp.

**2. Progressió simple→complex**
- Estructura i coherència: 4-6 apartats. Progressió amb relació explícita entre ells. Pot tenir subapartats d'un nivell.

**3. Definició de termes tècnics**
- Accessibilitat i precisió: Terminologia específica de la matèria, sempre definida a la primera aparició. Pot tenir glossari final.

**4. Exemple concret primer**
- Ordre i ancoratge ZDP: Exemple elaborat + abstracció + connexió entre apartats.

**5. Connectors causals**
- Explicitació de relacions: Connectors causals precisos i variats. Distinció causa/conseqüència/condició.

**6. Criteris transversals**
- Desnominalitzar processos: Idem. Pot mantenir el nom abstracte si va precedit de la desnominalització.
- No referència futura: Idem. Notes al peu admeses si no interrompen el flux principal.
- Fidelitat al text font: Fidelitat a la complexitat conceptual i al context disciplinar del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He relacionat els apartats entre si. He usat vocabulari específic de la matèria correctament."

### B2 — Acadèmic


**1. Entradeta**
- Context i anunci: Entradeta professional que permet saber si el manual és el que es necessita abans de llegir-lo.

**2. Progressió simple→complex**
- Estructura i coherència: Estructura completa amb progressió rigorosa. Subapartats d'un o dos nivells si cal.

**3. Definició de termes tècnics**
- Accessibilitat i precisió: Vocabulari tècnic ric i definit. Glossari final si hi ha molts termes. Pot incloure debat terminològic.

**4. Exemple concret primer**
- Ordre i ancoratge ZDP: Exemple + abstracció + extensió conceptual. Pot incloure exemples límit o de frontera.

**5. Connectors causals**
- Explicitació de relacions: Connectors sofisticats. Pot incloure concessius ("tot i que") i adversatius ("malgrat").

**6. Criteris transversals**
- Desnominalitzar processos: Idem. El nom abstracte és admissible quan el context disciplinar ho requereix i el procés ja s'ha explicat.
- No referència futura: Idem. Notes al peu admeses per a matisos tècnics avançats.
- Fidelitat al text font: Fidelitat a la complexitat, als matisos i als debats terminològics si n'hi ha.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu manual explica el tema de manera completa, sistemàtica i progressiva, amb vocabulari precís."

### C1+ — Crític


