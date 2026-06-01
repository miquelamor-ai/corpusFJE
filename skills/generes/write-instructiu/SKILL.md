---
name: write-instructiu
description: 'Use when adapting or generating an instructiu text for students. Activates
  when genre_discursiu == "instructiu". Applies strict chronological order, single-verb
  steps, and independent steps. Output: instructiu in markdown with materials, numbered
  steps, and expected result.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: instructiu
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
  equals: instructiu
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-instructiu.md
font_version: 4.0.0-canonic
generat_at: '2026-06-01'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 3d1e320968642a3f
---

# Escriure/adaptar un text instructiu — skill operativa per a LLM

El text instructiu guia el lector pas a pas per realitzar una acció amb **ordre cronològic processal estricte**. El seu tret definitori és la doble estructura invariant: la **llista de materials** (sempre prèvia als passos) i els **passos numerats** (un verb imperatiu + un objecte per pas). A diferència del text divulgatiu (que explica per qué funciona un procés), l'instructiu no explica: prescriu accions.

**Tipologia MALL**: Instructiva/Prescriptiva.
**HCL principal**: Narrar — variant processal: on el conte narra fets que han passat, l'instructiu narra fets que han de passar; la seqüenciació és la mateixa, el temps verbal canvia (imperatiu present).
**HCL secundàries**: Descriure — llistar i quantificar els materials (A1-B1).
**No s'adapta a pre-A1**: l'instructiu requereix la interpretació del **verb imperatiu com a ordre adreçada al lector** — "Barreja la farina i l'água" prescriu una acció futura per a l'executor, no descriu un event ni explica un fenomen. Aquesta funció pragmàtica directiva del verb imperatiu (acte de parla prescriptiu) requereix base lecto-escriptora mínima i la comprensió del "tu" implícit com a executor. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Narrar processal com a variant de HCL Narrar*: el text instructiu és la variant processal de la HCL Narrar. La seqüenciació temporal és la mateixa que en el conte o la crònica, però el temps verbal canvia (imperatiu o futur) i el punt de vista passa de "narrador" a "instructor". Treballar l'instructiu és treballar la seqüenciació en mode actiu.
- *Verb d'acció com a ancoratge cognitiu*: el verb imperatiu ("agafa", "barreja", "posa") és la paraula amb màxima càrrega informativa. Per a alumnat nouvingut o amb dificultats de comprensió lectora, identificar el verb és identificar l'acció. Destacar els verbs és una bastida de lectura vàlida i transferible a altres gèneres prescriptius.
- *L'instructiu com a avaluació autèntica*: fer que l'alumne executi l'instructiu que ha escrit un company és avaluació autèntica. Si els passos no son independents o l'ordre no és clar, el resultat fallarà de forma visible i immediata. L'error és un feedback objectiu.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **text instructiu adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Materials (llista prèvia)**
- Completitud i ordre: Llista de 3-5 materials. Sense quantitats. 1 material per línia.

**2. Format dels passos**
- Claredat i precisió: Passos numerats. 1 verb + 1 objecte. ≤5 paraules per pas.

**3. Autonomia del pas**
- Independència operativa: Cada pas s'executa sense mirar el pas següent. Cap referència implícita.

**4. Ordre cronològic**
- Rigor processal: Ordre d'execució respectat. No reordenar per legibilitat.

**5. Resultat esperat**
- Verificabilitat: 1 frase: qué s'ha aconseguit. Com es nota que ha sortit bé.

**6. Criteris transversals**
- No instruccions en passiva: Cap instrucció en passiva. "Afegeix l'agua" (no "S'afegirà l'agua"). Imperatiu consistent.
- No condicionals niats: Cap condicional ("si X, fes Y"). Linealitat estricta.
- Fidelitat al text font: Fidelitat al procés principal i a l'ordre dels passos.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit la llista de materials. He escrit 3-5 passos numerats amb una acció cadascun."

### A1 — Inicial


**1. Materials (llista prèvia)**
- Completitud i ordre: Llista de 4-6 materials amb quantitats bàsiques ("1 tassa", "2 ous").

**2. Format dels passos**
- Claredat i precisió: Passos numerats. 1 verb + 1 objecte concret. ≤8 paraules per pas.

**3. Autonomia del pas**
- Independència operativa: Cada pas independent. Sense "després de fer el pas anterior".

**4. Ordre cronològic**
- Rigor processal: Ordre processal estricte. L'ordre és estructuralment obligatori.

**5. Resultat esperat**
- Verificabilitat: Resultat de 1-2 frases: qué s'obté i com es nota que és correcte.

**6. Criteris transversals**
- No instruccions en passiva: Idem. Cap construcció passiva ni impersonal ("s'ha d'afegir").
- No condicionals niats: Idem. Condicionals simples admesos en nota al final, no dins dels passos.
- Fidelitat al text font: Fidelitat al procés, a l'ordre i als materials essencials.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Cada pas té un verb i un objecte. He posat el resultat al final."

### A2 — Funcional


**1. Materials (llista prèvia)**
- Completitud i ordre: Llista completa amb quantitats i especificitats bàsiques. Materials en ordre d'ús.

**2. Format dels passos**
- Claredat i precisió: Passos numerats. 1 verb precís + 1 objecte + context breu si cal.

**3. Autonomia del pas**
- Independència operativa: Passos estrictament independents. Test: puc fer el pas 3 sense saber el pas 4?

**4. Ordre cronològic**
- Rigor processal: Ordre cronològic respectat sense excepcions. Cap inversió per "lògica narrativa".

**5. Resultat esperat**
- Verificabilitat: Resultat amb les característiques esperades del producte o procés acabat.

**6. Criteris transversals**
- No instruccions en passiva: Idem. El subjecte "tu" (implícit) és sempre l'executor.
- No condicionals niats: Idem. Alternatives opcionals en nota al final del pas, entre parèntesis.
- Fidelitat al text font: Fidelitat al procés, a l'ordre, als materials i als indicadors de qualitat.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Puc executar cada pas sense llegir el següent. He posat tots els materials a la llista."

### B1 — Estratègic


**1. Materials (llista prèvia)**
- Completitud i ordre: Materials amb quantitats, tipus i condicions si escau. Llista exhaustiva.

**2. Format dels passos**
- Claredat i precisió: Passos numerats. 1-2 accions estretament relacionades per pas. Pot incloure condicions simples.

**3. Autonomia del pas**
- Independència operativa: Independència total. Cap referència implícita a un pas anterior ni posterior.

**4. Ordre cronològic**
- Rigor processal: Ordre processal pur. Qualsevol reordenació trencaria el resultat final.

**5. Resultat esperat**
- Verificabilitat: Resultat amb criteris de qualitat o avaluació del producte.

**6. Criteris transversals**
- No instruccions en passiva: Idem. Pot incloure l'imperatiu de primera plural ("Barregem") si el context és col·lectiu.
- No condicionals niats: Idem. Pot incloure bifurcacions simples en paràgraf separat.
- Fidelitat al text font: Fidelitat a la complexitat tècnica del procés original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'instructiu té totes les quantitats i especificitats necessàries. El resultat descriu com ha de quedar."

### B2 — Acadèmic


**1. Materials (llista prèvia)**
- Completitud i ordre: Materials completament especificats. Alternatives si n'hi ha. Ordenats per fases si el procés és complex.

**2. Format dels passos**
- Claredat i precisió: Passos numerats. Completament autònoms. Precisió tècnica màxima. Pot incloure notes tècniques en cursiva.

**3. Autonomia del pas**
- Independència operativa: Passos absolutament autònoms i complets en si mateixos. Cap sobreentès.

**4. Ordre cronològic**
- Rigor processal: Ordre processal rigorós. Pot incloure passos previs de preparació clarament separats.

**5. Resultat esperat**
- Verificabilitat: Resultat amb criteris precisos i possibles variacions acceptables.

**6. Criteris transversals**
- No instruccions en passiva: Idem. Precisió tècnica màxima amb l'imperatiu adequat al registre professional.
- No condicionals niats: Condicionals simples admesos si el context professional ho requereix, però sempre en pas separat.
- Fidelitat al text font: Fidelitat a la complexitat, a la precisió tècnica i a les variacions del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'instructiu és complet i professional. Qualsevol persona podria fer el procés seguint els meus passos."

### C1+ — Crític


