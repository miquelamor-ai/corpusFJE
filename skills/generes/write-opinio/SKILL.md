---
name: write-opinio
description: 'Use when adapting or generating an opinió article for students. Activates
  when genre_discursiu == "opinio". Applies thesis-first structure, numbered arguments
  with evidence, and explicit argumentative connectors. Output: opinió in markdown
  with thesis, arguments, and conclusion.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: opinio
tipologia: Argumentativa
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
  equals: opinio
moduls_relacionats:
- M3
macro_tipologia: argumentativa
label_ca: Article d'opinió
font_canonic: M3_genere-escriure-opinio.md
font_version: 4.0.0-canonic
generat_at: '2026-06-20'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 554fa0285a4be904
---

# Escriure/adaptar un article d'opinió — skill operativa per a LLM

L'article d'opinió és un gènere **argumentatiu** que defensa una tesi amb arguments recolzats en evidències concretes. **No s'adapta a pre-A1**: el pensament abstracte de presa de posició requereix una base lingüística mínima d'A1 i un domini bàsic del raonament causa-conseqüència.

**Tipologia MALL**: Argumentativa (convèncer).
**HCL principal**: Argumentar — defensar una tesi per convèncer l'interlocutor.
**HCL secundàries**: Justificar amb evidències (A2+) · Interpretar i reconèixer altres posicions (B2+) · Avaluar fiabilitat de les fonts (B2+).

**Connexions MALL transversals:**
- *Translanguaging / TOLC*: a A1, permet paraules de la L1 entre claudàtors `[...]` per mantenir el fil argumentatiu. A B1+, s'espera que l'argumentació sigui íntegrament en català.
- *Eix oral / escrit*: a A1-A2, el docent pot acceptar una versió oral de la tesi i arguments abans de la versió escrita (transferència oral→escrit).
- *Multimodalitat*: a A1-A2, es pot complementar amb un esquema visual de la tesi + arguments (mapa conceptual d'argumentació). A B1+, el text és autosuficient.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **text d'opinió adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — això es treballa amb un derivat propi (rúbrica d'avaluació formativa). El gènere argumentatiu és especialment pertinent per al **debat d'aula** com a producció col·laborativa (vegeu H1 i H3), però aquesta vista no és l'instrument adequat per avaluar aquesta producció.
**Sub-granularitat dins d'A1 i A2**: es treballa amb la variable independent `fase_lectora` del frontmatter, no amb columnes addicionals.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Tesi**
- Formulació: Una sola oració que comença amb "Crec que…". Sense preàmbul.
- Posició al text: Primera frase del text.

**2. Arguments**
- Nombre: Màxim 2 arguments.

**3. Evidència per argument**
- Tipus d'evidència: Exemple de la vida quotidiana de l'alumne.
- Nombre per argument: 1 evidència per argument.

**4. Connectors argumentatius**
- Inventari per nivell: "perquè", "i", "però".
- Varietat funcional: N/A — només un tipus disponible.

**5. Reconeixement i refutació**
- Inclusió: No requerit.

**6. Conclusió**
- Format i funció: Una frase: "Per això, crec que…". Reprèn la tesi.

**8. Criteris transversals**
- Registre i persona gramatical: Primera persona singular. Registre informal tolerat.
- Llargada de frase: Frases de fins a 12 paraules.
- Retòrica: Cap ironia, cap pregunta retòrica, cap paral·lelisme complex.
- Unicitat de tesi: Una sola tesi.
- Fidelitat al text font: Fidelitat a la tesi i als arguments principals.
- No-atacs personals: Cap atac personal ni llenguatge valoratiu extrem.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He pensat què crec abans d'escriure, i he buscat 2 raons que m'ajudin a explicar-ho."

### A1 — Inicial


**1. Tesi**
- Formulació: Clara i directa, en primera persona. Una oració.
- Posició al text: Al primer paràgraf.

**2. Arguments**
- Nombre: 2-3 arguments.

**3. Evidència per argument**
- Tipus d'evidència: Exemple concret o dada simple.
- Nombre per argument: 1 evidència per argument.

**4. Connectors argumentatius**
- Inventari per nivell: "perquè", "per tant", "però", "a més".
- Varietat funcional: N/A — repertori limitat.

**5. Reconeixement i refutació**
- Inclusió: No requerit.

**6. Conclusió**
- Format i funció: 1-2 frases. Reprèn la tesi. No introdueix arguments nous.

**8. Criteris transversals**
- Registre i persona gramatical: Primera persona. Registre semiformal.
- Llargada de frase: Frases de fins a 15 paraules.
- Retòrica: Cap ironia, cap pregunta retòrica.
- Unicitat de tesi: Una sola tesi.
- Fidelitat al text font: Fidelitat a la tesi i als arguments principals.
- No-atacs personals: Cap atac personal ni llenguatge valoratiu extrem.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He comprovat que la meva tesi s'entén de seguida i que tinc un exemple per a cada raó."

### A2 — Funcional


**1. Tesi**
- Formulació: Clara i directa. Pot ser de 2 oracions. Primera persona o impersonal.
- Posició al text: Al primer paràgraf.

**2. Arguments**
- Nombre: 3 arguments.

**3. Evidència per argument**
- Tipus d'evidència: Dada, exemple concret o cita breu.
- Nombre per argument: 1 evidència per argument.

**4. Connectors argumentatius**
- Inventari per nivell: "en primer lloc", "a més", "per tant", "en conclusió".
- Varietat funcional: Es recomana variar: causa (perquè) + addició (a més) + conclusió (per tant).

**5. Reconeixement i refutació**
- Inclusió: Opcional ("Algú pot pensar que… però…").
- Refutació: Suggerida si s'inclou contraargument.

**6. Conclusió**
- Format i funció: 2-3 frases. Reprèn i reforça la tesi. Pot incloure una crida a l'acció.

**7. Fiabilitat de les evidències**
- Identificació i avaluació: Opcional: "D'on ve aquesta dada?".

**8. Criteris transversals**
- Registre i persona gramatical: Primera persona o impersonal. Registre formal.
- Llargada de frase: Frases de fins a 18 paraules.
- Retòrica: Cap ironia. Pregunta retòrica simple admissible si està marcada com a tal.
- Unicitat de tesi: Una sola tesi.
- Fidelitat al text font: Fidelitat a la tesi, arguments i evidències principals.
- No-atacs personals: Cap atac personal ni llenguatge valoratiu extrem.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He revisat si els meus arguments es relacionen entre ells i si la conclusió tanca el que vaig anunciar a la tesi."

### B1 — Estratègic


**1. Tesi**
- Formulació: Pot ser impersonal ("Cal considerar que…"). Elaborada però sense preàmbul.
- Posició al text: Al primer paràgraf.

**2. Arguments**
- Nombre: 3-4 arguments amb estructura interna.

**3. Evidència per argument**
- Tipus d'evidència: Dada estadística, cita d'expert o exemple complex.
- Nombre per argument: 1-2 evidències per argument.

**4. Connectors argumentatius**
- Inventari per nivell: "d'altra banda", "per contra", "en conseqüència", "en resum". **"Tanmateix" i "no obstant això" només a partir de B2**.
- Varietat funcional: **Obligatori**: cada argument introduït amb un tipus diferent (causa / contrast / addició / conclusió). No repetir el mateix tipus.

**5. Reconeixement i refutació**
- Inclusió: Obligatori: contraargument en paràgraf separat.
- Refutació: Refutació concreta amb evidència pròpia.

**6. Conclusió**
- Format i funció: 3-4 frases. Argumentada. Pot reformular la tesi amb matís.

**7. Fiabilitat de les evidències**
- Identificació i avaluació: Obligatori: el lector identifica la font de cada evidència principal.

**8. Criteris transversals**
- Registre i persona gramatical: Impersonal preferit. Registre acadèmic.
- Llargada de frase: Frases de fins a 22 paraules.
- Retòrica: Pot incloure ironia explícita o pregunta retòrica si l'argumentació la sustenta.
- Unicitat de tesi: Una sola tesi.
- Fidelitat al text font: Fidelitat a la tesi, arguments, evidències i, si hi és, contraargument.
- No-atacs personals: Cap atac personal ni llenguatge valoratiu extrem.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He pensat què diria algú que no opina com jo, i he intentat respondre-li al text. Així he vist on era forta o feble la meva postura."

### B2 — Acadèmic


**1. Tesi**
- Formulació: Complexa. Pot matisar la pròpia postura o ser paradoxal. Sense preàmbul.
- Posició al text: Al primer paràgraf.

**2. Arguments**
- Nombre: 3-5 arguments amb jerarquització explícita.

**3. Evidència per argument**
- Tipus d'evidència: Evidències múltiples i variades; pot incloure contrastos entre fonts.
- Nombre per argument: Múltiples, segons la complexitat de l'argument.

**4. Connectors argumentatius**
- Inventari per nivell: Connectors d'especialitat acadèmica propis de la disciplina. Variació rica i precisa.
- Varietat funcional: Cada relació lògica marcada amb el connector funcional adequat (causal, concessiu, consecutiu, contrastiu, additiu). Sense repetició de tipus.

**5. Reconeixement i refutació**
- Inclusió: Obligatori: contraargument elaborat amb matís.
- Refutació: Refutació fonamentada, integra el contraargument al raonament.

**6. Conclusió**
- Format i funció: Reformulació complexa de la tesi amb integració de les tensions identificades.

**7. Fiabilitat de les evidències**
- Identificació i avaluació: Obligatori: el lector avalua la credibilitat i la intencionalitat de cada font.

**8. Criteris transversals**
- Registre i persona gramatical: Registre acadèmic complet; pot usar primera persona per a posicionament explícit.
- Llargada de frase: Sense límit estricte; claredat com a criteri únic.
- Retòrica: Retòrica lliure si serveix l'argumentació; sense ambigüitat dels arguments.
- Unicitat de tesi: Una sola tesi.
- Fidelitat al text font: Fidelitat al matís, als punts de vista i a la complexitat argumental originals.
- No-atacs personals: Cap atac personal ni llenguatge valoratiu extrem.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He reflexionat sobre els límits de la meva pròpia postura: quines suposicions estic fent? Quines evidències em manquen?"

### C1+ — Crític


