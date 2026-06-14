---
name: write-reglament
description: 'Use when adapting or generating a reglament for students. Activates
  when genre_discursiu == "reglament". Applies one-rule-per- item, direct imperative
  voice, thematic grouping, and separated consequences. Output: reglament in markdown
  with title, grouped rules, and consequences.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: reglament
tipologia: Instructiva / Prescriptiva
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
  equals: reglament
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-reglament.md
font_version: 4.0.0-canonic
generat_at: '2026-06-14'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 02cb8ce47080ea50
---

# Escriure/adaptar un reglament — skill operativa per a LLM

El reglament és un text normatiu que regula conductes en un context social o institucional. El seu tret definitori és la **norma com a prescripció abstracta generalitzada**: cada ítem estableix una conducta esperada (o prohibida) que s'aplica a tothom, en qualsevol moment i sense necessitat de justificació interna. L'organització per temes i la separació estricta entre norma i conseqüència en garanteixen la llegibilitat i l'aplicabilitat.

**Tipologia MALL**: Normativa/Reguladora.
**HCL principal**: Narrar — variant prescriptiva: el reglament seqüencia conductes esperades i prescriu com a col·lectiu el que s'ha de fer. L'ordre temàtic i la separació de normes i conseqüències constitueixen la seqüència prescriptiva del text.
**HCL secundàries**: Justificar (B1+) — el reglament legitima les normes apel·lant a valors compartits (convivència, seguretat, equitat) quan s'inclou preàmbul · Argumentar (B1+) — per fonamentar per qué determinades normes són necessàries o han de canviar.
**No s'adapta a pre-A1**: el reglament requereix la comprensió de la **norma com a prescripció abstracta generalitzada** — "No córrer pels passadissos" prescriu una conducta futura aplicable a tothom en qualsevol moment i en qualsevol context d'aplicació. Aquesta funció prescriptiva-normativa, que opera sobre conductes abstractes i no sobre accions concretes i immediates, requereix base lecto-escriptora mínima i la comprensió del "tothom" implícit com a destinatari col·lectiu. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Reglament com a text de convivència democràtica*: elaborar i negociar normes de classe és una pràctica de ciutadania activa. Treballar el reglament en primera persona del plural ("Ens comprometem a...") canvia la norma imposada per la norma construïda col·lectivament. La HCL Argumentar (B1+) és la porta d'entrada a la democràcia participativa a l'aula.
- *Positiu primer com a principi pedagògic*: el reglament eficaç descriu el que s'ha de fer ("Demana la paraula") abans del que no s'ha de fer ("No interrompis"). Aquesta inversió és consistent amb la investigació pedagògica sobre disciplina positiva (Dreikurs, Nelsen) i amb els principis DUA d'autoregulació.
- *Norma i conseqüència com a estructura causal explícita*: separar la norma de la conseqüència és una bastida de comprensió de la causalitat social. "Si trenques la norma, passa X" és una estructura condicional amb valor educatiu: l'alumne aprèn que les conductes tenen efectes predecibles sobre la convivència.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **reglament adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Agrupació temàtica**
- Organització i coherència: 2 grups temàtics. Títol de grup molt curt (1-2 paraules: "A classe", "Al passadís"). 2-3 normes per grup.

**2. Format de la norma**
- Claredat i precisió: Verb imperatiu + objecte. ≤6 paraules per norma. 1 conducta per norma.

**3. Veu imperativa directa**
- Registre normatiu: Imperatiu de 2a singular consistent: "Respecta", "Escolta", "Guarda". Cap passiva ni impersonal.

**4. Una norma per ítem**
- Granularitat i claredat: Estrictament 1 conducta per ítem. Cap conjunció coordinada dins d'una norma ("i", "ni").

**5. Positiu primer**
- Orientació pedagògica: La norma formula el que s'ha de fer ("Demana la paraula"), no el que no s'ha de fer.

**6. Conseqüències separades**
- Estructura i claredat: Si hi ha conseqüències, estan en un bloc final separat de les normes. 1 frase per conseqüència.

**7. Criteris transversals**
- No justificació dins la norma: Cap "perquè" ni raonament dins de l'ítem de norma. La norma és una prescripció, no una argumentació.
- No passiva ni impersonal: Cap "s'ha de", "cal", "es prohibeix" als ítems de norma. Imperatiu directe consistent.
- Fidelitat al text font: Fidelitat a les normes principals i als grups temàtics del text font.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit normes en imperatiu. He posat 1 conducta per norma. He posat primer el que s'ha de fer."

### A1 — Inicial


**1. Agrupació temàtica**
- Organització i coherència: 2-3 grups temàtics amb títol curt. 3-4 normes per grup.

**2. Format de la norma**
- Claredat i precisió: Verb imperatiu + objecte + context breu. ≤10 paraules per norma.

**3. Veu imperativa directa**
- Registre normatiu: Idem. Imperatiu de 2a singular o de 2a plural ("Respecteu") si el context és col·lectiu.

**4. Una norma per ítem**
- Granularitat i claredat: Idem. Cap norma composta. Si es detecten dues conductes, es divideix en dos ítems.

**5. Positiu primer**
- Orientació pedagògica: Idem. Si cal una norma negativa, va darrere de la positiva equivalent.

**6. Conseqüències separades**
- Estructura i claredat: Bloc de conseqüències separat. Cada conseqüència lligada a un grup temàtic o a una norma concreta.

**7. Criteris transversals**
- No justificació dins la norma: Idem.
- No passiva ni impersonal: Idem.
- Fidelitat al text font: Fidelitat a les normes, als grups temàtics i a les conseqüències essencials.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He agrupat les normes per temes. He posat primer el que s'ha de fer. He separat les conseqüències."

### A2 — Funcional


**1. Agrupació temàtica**
- Organització i coherència: 3-4 grups temàtics. Títols de grup que expliciten l'àmbit ("A l'espai comú", "Amb els materials").

**2. Format de la norma**
- Claredat i precisió: Norma completa i autònoma. Pot incloure el context si determina l'aplicació ("Als passadissos, camina").

**3. Veu imperativa directa**
- Registre normatiu: Idem. Pot alternar imperatiu singular/plural segons el destinatari de cada grup temàtic.

**4. Una norma per ítem**
- Granularitat i claredat: Idem. Cada ítem és atòmic: no pot descompondre's en subnormes sense perdre sentit.

**5. Positiu primer**
- Orientació pedagògica: Idem. Revisió sistemàtica: cada "No X" té una formulació positiva equivalent.

**6. Conseqüències separades**
- Estructura i claredat: Bloc de conseqüències amb estructura "Si [norma incomplerta] → [conseqüència]". Conseqüència educativa.

**7. Criteris transversals**
- No justificació dins la norma: Idem. Si s'inclou un preàmbul amb la raó de ser del reglament, és un bloc separat i inicial.
- No passiva ni impersonal: Idem.
- Fidelitat al text font: Fidelitat a les normes, als grups temàtics, a les conseqüències i al to institucional del text font.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Cada norma és positiva i autònoma. El bloc de conseqüències está separat i lligat a les normes."

### B1 — Estratègic


**1. Agrupació temàtica**
- Organització i coherència: 4-6 grups temàtics. Progressió lògica dels àmbits (de l'individual al col·lectiu o d'intern a extern).

**2. Format de la norma**
- Claredat i precisió: Norma completa amb subjecte implícit clar. Pot incloure condicions d'aplicació simples.

**3. Veu imperativa directa**
- Registre normatiu: Idem. Pot usar l'infinitiu normatiu com a variant registral ("Respectar els torns de paraula").

**4. Una norma per ítem**
- Granularitat i claredat: Idem. La granularitat és coherent dins de cada grup temàtic.

**5. Positiu primer**
- Orientació pedagògica: Idem. El reglament reflecteix una orientació positiva global. Les normes negatives son excepcions justificades.

**6. Conseqüències separades**
- Estructura i claredat: Bloc de conseqüències graduat (amonestació / mediació / sanció). Lligat explícitament a les normes.

**7. Criteris transversals**
- No justificació dins la norma: Idem. El preàmbul (si n'hi ha) argumenta el context i els valors; les normes prescriuen sense justificar.
- No passiva ni impersonal: Idem.
- Fidelitat al text font: Fidelitat a la complexitat normativa i al marc institucional del text original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El reglament té preàmbul, normes per temes i conseqüències graduades. Totes les normes son en imperatiu."

### B2 — Acadèmic


**1. Agrupació temàtica**
- Organització i coherència: Estructura temàtica completa i coherent. Progressió que reflecteix la jerarquia de valors del reglament.

**2. Format de la norma**
- Claredat i precisió: Norma tècnicament precisa. Pot incloure l'abast ("tothom", "en tot moment") quan és rellevant.

**3. Veu imperativa directa**
- Registre normatiu: Idem. Imperatiu o infinitiu normatiu, consistents dins de cada grup temàtic. Registre institucional precís.

**4. Una norma per ítem**
- Granularitat i claredat: Idem. La granularitat és consistent a tot el reglament. Cap norma és redundant amb una altra.

**5. Positiu primer**
- Orientació pedagògica: Idem. El reglament equilibra normes de conducta esperada i normes de conducta prohibida. La ràtio positiu/negatiu reflecteix els valors del context.

**6. Conseqüències separades**
- Estructura i claredat: Bloc de conseqüències complet i proporcional. Pot incloure el procediment de resolució de conflictes.

**7. Criteris transversals**
- No justificació dins la norma: Idem. La distinció prescripció/argumentació és nítida a tot el document.
- No passiva ni impersonal: Idem. La passiva i l'impersonal son admissibles al preàmbul o al bloc de conseqüències, no als ítems.
- Fidelitat al text font: Fidelitat a la complexitat, al marc institucional i als procediments de resolució del text original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El reglament és complet, consistent i aplicable. Qualsevol persona podria complir-lo i aplicar-lo sense explicació addicional."

### C1+ — Crític


