---
name: write-receptari
description: 'Use when adapting or generating a receptari (recipe) for students. Activates
  when genre_discursiu == "receptari". Applies ingredients in order of use, single-verb
  steps, explicit quantities, and sensory indicators. Output: receptari in markdown
  with ingredients, preparation steps, and result.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: receptari
tipologia: Instructiva
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
  equals: receptari
moduls_relacionats:
- M3
macro_tipologia: instructiva
label_ca: Recepta
font_canonic: M3_genere-escriure-receptari.md
font_version: 4.0.0-canonic
generat_at: '2026-06-28'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: d9d4fb15bcc889a7
---

# Escriure/adaptar una recepta — skill operativa per a LLM

La recepta és un text instructiu especialitzat en processos culinaris. El seu tret definitori doble és la **llista d'ingredients ordenada per l'ordre en qué s'usen** i els **indicadors sensorials** ("fins que sigui daurat", "fins que l'escuma desaparegui") com a criteris d'avaluació autèntics dels passos clau. A diferència de l'instructiu genèric, la recepta porta inherentment la dimensió cultural: els plats son portadors d'identitat.

**Tipologia MALL**: Instructiva/Prescriptiva (culinària).
**HCL principal**: Narrar — seqüència processal culinària: la recepta ordena accions en el temps amb verb imperatiu com a vehicle.
**HCL secundàries**: Descriure — llistar i quantificar ingredients; descriure textures, colors i olors com a indicadors sensorials (A1-B1+).
**No s'adapta a pre-A1**: la recepta requereix la **lectura simultània de dos sistemes**: la llista d'ingredients (amb quantitats) i la seqüència de passos imperatius, amb la comprensió que els ingredients de la llista s'usen als passos en l'ordre en qué apareixen. Aquesta doble planificació i la comprensió de les mesures com a quantitats exactes ("200 g", "2 cullerades") no és accessible sense base lecto-escriptora mínima. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Recepta com a pont BICS→CALP*: el context culinari (BICS) és familiar i concret per a quasi tot l'alumnat. Les mesures, els temps i els indicadors sensorials son vocabulari CALP (termes tècnics precisos) en un entorn de seguretat cognitiva. La recepta és el gènere instructiu amb menor barrera d'entrada.
- *Indicador sensorial com a competència d'observació científica*: "fins que sigui daurat", "quan l'escuma desaparegui", "quan el tacte sigui elàstic" son instruccions d'autoavaluació en acció. L'alumne aprèn a observar i decidir, no només a seguir. Aquesta competència és transferible a la ciència (observació d'experiments) i a la tecnologia.
- *Recepta com a vehicle d'identitat cultural (TOLC)*: els plats son portadors d'identitat. Treballar receptes de les cultures familiars de l'alumnat és un acte de reconeixement identitari. En producció, la recepta en L1 traduïda al català és un acte de TOLC natural i motivador.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **recepta adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Llista d'ingredients**
- Completitud i format: Llista de 3-5 ingredients. Sense quantitats. 1 ingredient per línia.

**2. Ordre dels ingredients**
- Seqüència d'ús: Ingredients en qualsevol ordre (llista simple).

**3. Format dels passos**
- Claredat i precisió: Passos numerats. 1 verb + 1 objecte. ≤6 paraules per pas.

**4. Indicadors sensorials**
- Observació i verificació: 1 indicador per pas crític: "fins que sigui daurat".

**5. Temps de cocció**
- Precisió temporal: Temps global aproximat: "uns 20 minuts".

**6. Resultat esperat**
- Verificabilitat final: 1 frase: com ha de quedar (color o textura principals).

**7. Criteris transversals**
- No passiva en els passos: Cap instrucció en passiva. "Barreja la farina" (no "S'ha de barrejar la farina"). Imperatiu consistent.
- No ingredients a mig text: Cap ingredient nou als passos que no hagi estat a la llista prèvia.
- Fidelitat al text font: Fidelitat als ingredients principals i a l'ordre dels passos.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit la llista d'ingredients i els passos numerats."

### A1 — Inicial


**1. Llista d'ingredients**
- Completitud i format: Llista de 4-6 ingredients amb quantitats bàsiques ("1 tassa", "2 ous").

**2. Ordre dels ingredients**
- Seqüència d'ús: Ingredients ordenats aproximadament per l'ordre en qué s'usen.

**3. Format dels passos**
- Claredat i precisió: Passos numerats. 1 acció culinària + context breu. ≤10 paraules per pas.

**4. Indicadors sensorials**
- Observació i verificació: 1-2 indicadors sensorials per pas crític (color, textura, olor).

**5. Temps de cocció**
- Precisió temporal: Temps per a les fases principals: "fregir 5 minuts / coure 20 minuts".

**6. Resultat esperat**
- Verificabilitat final: 1-2 frases que descriuen el resultat en termes sensorials concrets.

**7. Criteris transversals**
- No passiva en els passos: Idem.
- No ingredients a mig text: Idem.
- Fidelitat al text font: Fidelitat als ingredients, a l'ordre, als temps bàsics i al resultat.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Cada pas té un verb i un objecte. He posat indicadors ('fins que...') a alguns passos."

### A2 — Funcional


**1. Llista d'ingredients**
- Completitud i format: Ingredients amb quantitats i unitats de mesura estàndard. Llista completa.

**2. Ordre dels ingredients**
- Seqüència d'ús: Ingredients ordenats estrictament per l'ordre d'ús. Separació per fases si cal.

**3. Format dels passos**
- Claredat i precisió: Passos numerats amb indicador sensorial o temporal si cal. 1-2 accions relacionades.

**4. Indicadors sensorials**
- Observació i verificació: Indicadors sensorials als passos clau. Permeten saber si el pas s'ha executat correctament.

**5. Temps de cocció**
- Precisió temporal: Temps específic per a cada pas que en requereix. Indicador sensorial alternatiu.

**6. Resultat esperat**
- Verificabilitat final: Resultat descrit amb 2-3 indicadors sensorials. Com saber que ha sortit bé.

**7. Criteris transversals**
- No passiva en els passos: Idem.
- No ingredients a mig text: Idem.
- Fidelitat al text font: Fidelitat als ingredients, als passos, als indicadors sensorials i al resultat.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Els ingredients estan en l'ordre d'ús. Puc executar cada pas sense llegir el següent."

### B1 — Estratègic


**1. Llista d'ingredients**
- Completitud i format: Ingredients completament especificats (graus, temps de repòs si cal).

**2. Ordre dels ingredients**
- Seqüència d'ús: Agrupació per fases de preparació si la recepta és complexa.

**3. Format dels passos**
- Claredat i precisió: Passos numerats complets i autònoms. Pot incloure condicions simples ("si bull, baixa el foc").

**4. Indicadors sensorials**
- Observació i verificació: Indicadors sensorials precisos i variats (color, so, tacte, olor). Sempre preferits al temps.

**5. Temps de cocció**
- Precisió temporal: Temps amb marge ("10-12 minuts") i indicador sensorial com a confirmació.

**6. Resultat esperat**
- Verificabilitat final: Resultat complet: aspecte, textura, olor i gust. Criteris de qualitat. Racions o quantitat final.

**7. Criteris transversals**
- No passiva en els passos: Idem.
- No ingredients a mig text: Idem.
- Fidelitat al text font: Fidelitat a la complexitat culinària i als indicadors de qualitat del text original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La recepta té totes les quantitats i especificitats. El resultat indica les racions."

### B2 — Acadèmic


**1. Llista d'ingredients**
- Completitud i format: Ingredients amb quantitats precises, variants i possibles substitucions explicitades.

**2. Ordre dels ingredients**
- Seqüència d'ús: Organització professional per fases i subfases si cal. Cada fase amb subtítol.

**3. Format dels passos**
- Claredat i precisió: Passos tècnicament precisos. Temperatures, temps i textures especificats sempre.

**4. Indicadors sensorials**
- Observació i verificació: Indicadors sensorials complets que permeten reproduir la recepta sense ajuda externa.

**5. Temps de cocció**
- Precisió temporal: Temps i temperatures precisos. Alternatives per a equipaments o altituds diferents.

**6. Resultat esperat**
- Verificabilitat final: Resultat professional: criteris precisos + variacions acceptables + errors comuns amb solució.

**7. Criteris transversals**
- No passiva en els passos: Idem. Imperatiu o infinitiu normatiu consistent.
- No ingredients a mig text: Idem. Variants opcionals en nota final, no intercalades als passos.
- Fidelitat al text font: Fidelitat a la complexitat, a les variants i als errors comuns del text original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La recepta és completa i professional. Qualsevol persona podria cuinar el plat seguint els meus passos."

### C1+ — Crític


