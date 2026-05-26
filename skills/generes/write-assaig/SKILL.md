---
name: write-assaig
description: 'Use when adapting or generating an assaig for students. Activates when
  genre_discursiu == "assaig". Applies clear thesis in the introduction, integrated
  citations, and defined academic vocabulary. Output: assaig in markdown with introduction,
  development, and conclusion.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: assaig
tipologia: Argumentativa / Reflexiva
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
  equals: assaig
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-assaig.md
font_version: 4.0.0-canonic
generat_at: '2026-05-26'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 83fb68215dec90ed
---

# Escriure/adaptar un assaig — skill operativa per a LLM

L'assaig és un text reflexiu i argumentatiu que defensa una **tesi explícita** amb arguments ordenats i, a partir de B1, amb evidències o cites integrades. A diferència de l'article d'opinió (que prioritza la persuasió directa i el posicionament personal), l'assaig té un to més reflexiu, una estructura formal visible i un vocabulari acadèmic progressiu.

**Tipologia MALL**: Argumentativa-reflexiva.
**HCL principal**: Argumentar — defensar una tesi amb arguments ordenats i evidència. A A1-A2, el pes real recau sobre la HCL Interpretar/Valorar (posicionar-se davant d'una idea i justificar el posicionament), que és el camí d'entrada a l'Argumentar formal.
**HCL secundàries**: Justificar (B1+, evidències vinculades a fonts) · Avaluar (B2+, contrast de postures i ponderació d'arguments).
**No s'adapta a pre-A1**: l'assaig requereix la producció d'una tesi explícita amb arguments ordenats, la comprensió de la relació entre tesi, argument i evidència com a estructura lògica abstracta, i la capacitat de refutar o matisar una postura contrària. Aquesta combinació d'operacions cognitives abstractes requereix base lecto-escriptora mínima i capacitat de pensament formal. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *CALP de Cummins — l'assaig com a cim de la llengua acadèmica*: l'assaig és el gènere on el CALP (llengua acadèmica de pensament abstracte) és més visible i dens. La gradació del vocabulari i les cites implementa la progressió BICS→CALP de manera explícita. Treballar l'assaig des de A1 (en format molt simplificat) construeix la base per a l'escriptura acadèmica de llarg recorregut.
- *Refutació com a pensament crític*: reconèixer i respondre al punt de vista contrari és el nucli del pensament crític. A B1, és la transició de "defenso la meva postura" a "entenc la postura dels altres i hi respoc". La HCL Argumentar no és un monòleg, és un diàleg amb l'interlocutor implícit.
- *Translanguaging*: a A1, l'alumne pot usar paraules de la L1 entre claudàtors [...] per mantenir el fil argumentatiu quan no troba el terme en català. A B1+, pot integrar cites en la L1 si s'acompanyen de traducció o paràfrasi en català.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **text adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Tesi o postura inicial**
- Claredat i explicitació: 1 frase que diu el que es defensa: "Crec que [tesi]." Al primer paràgraf.

**2. Arguments**
- Coherència i progressió: 1 argument simple. "Crec que... perquè...".

**3. Exemples i evidències**
- Suport i credibilitat: 1 exemple personal o molt proper per argument.

**4. Refutació o matís**
- Pensament crític: Sense refutació a A1 (massa complex). Acceptable que la postura sigui unilateral.

**5. Conclusió**
- Tancament i coherència: 1 frase: "Per tot això, crec que [tesi]." No introdueix arguments nous.

**6. Connectors argumentatius**
- Varietat i precisió: "Crec que... perquè..." (1 connector causal).

**7. Cites (B1+)**
- Integració i atribució: Sense cites a A1.

**8. Criteris transversals**
- No tesi implícita: Cap obertura vaga ("Hi ha moltes opinions sobre...") sense posicionar-se.
- Conclusió tancada: Cap argument nou a la conclusió que no hagi aparegut al cos del text.
- Fidelitat al text font: Fidelitat a la postura principal i als arguments centrals del text font.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit la meva opinió en una frase al principi. He donat 1 argument amb un exemple."

### A1 — Inicial


**1. Tesi o postura inicial**
- Claredat i explicitació: Tesi clara de 1-2 frases amb connector d'opinió. Al primer paràgraf.

**2. Arguments**
- Coherència i progressió: 2 arguments en paràgrafs separats. 1 connector causal per argument.

**3. Exemples i evidències**
- Suport i credibilitat: 1 exemple concret per argument. Pot ser un fet quotidià o una observació directa.

**4. Refutació o matís**
- Pensament crític: Reconeixement d'un punt de vista diferent en 1 frase: "Alguns pensen que... però jo crec que..."

**5. Conclusió**
- Tancament i coherència: Conclusió de 2 frases que reprèn la tesi. No obre noves preguntes.

**6. Connectors argumentatius**
- Varietat i precisió: "A més", "però", "per exemple", "per tot això". Variats mínimament.

**7. Cites (B1+)**
- Integració i atribució: Opcional: paràfrasi d'una idea d'algú altre sense cita formal.

**8. Criteris transversals**
- No tesi implícita: Idem.
- Conclusió tancada: Idem.
- Fidelitat al text font: Fidelitat a la postura, als arguments i a les evidències essencials.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit la tesi al principi. He donat 2 arguments amb un exemple cadascun."

### A2 — Funcional


**1. Tesi o postura inicial**
- Claredat i explicitació: Tesi explícita que anuncia el tema i la postura. La tesi delimita l'abast de l'assaig.

**2. Arguments**
- Coherència i progressió: 3 arguments ben diferenciats. 1 per paràgraf. Connector explícit per a cada un.

**3. Exemples i evidències**
- Suport i credibilitat: 1 exemple o evidència per argument. Pot ser un fet, una dada o una cita breu.

**4. Refutació o matís**
- Pensament crític: Refutació d'un argument contrari. Connector de contrast: "tot i que", "però", "tanmateix".

**5. Conclusió**
- Tancament i coherència: Conclusió de 3 frases: resum de la postura + una implicació breu (opcional).

**6. Connectors argumentatius**
- Varietat i precisió: "Tanmateix", "per contra", "en conseqüència", "d'una banda... de l'altra".

**7. Cites (B1+)**
- Integració i atribució: 1 cita breu integrada al text amb atribució clara. Explicació de per qué importa.

**8. Criteris transversals**
- No tesi implícita: Idem.
- Conclusió tancada: Idem.
- Fidelitat al text font: Fidelitat als arguments, a les evidències i als connectors argumentatius del text font.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit 3 arguments, 1 per paràgraf. He reconegut un punt de vista diferent."

### B1 — Estratègic


**1. Tesi o postura inicial**
- Claredat i explicitació: Tesi matisada que reconeix la complexitat del tema sense diluir la postura.

**2. Arguments**
- Coherència i progressió: 3-4 arguments jerarquitzats (del menys al més fort o a la inversa).

**3. Exemples i evidències**
- Suport i credibilitat: 1-2 evidències per argument. Cites breus amb atribució clara.

**4. Refutació o matís**
- Pensament crític: Refutació elaborada d'1-2 arguments contraris amb evidències de suport.

**5. Conclusió**
- Tancament i coherència: Conclusió argumentada que connecta la tesi amb el context més ampli.

**6. Connectors argumentatius**
- Varietat i precisió: Connectors argumentatius variats i precisos. Distinció entre contrast, causa i conclusió.

**7. Cites (B1+)**
- Integració i atribució: 2-3 cites integrades i comentades. Cada cita suporta l'argument del paràgraf.

**8. Criteris transversals**
- No tesi implícita: Idem.
- Conclusió tancada: Idem.
- Fidelitat al text font: Fidelitat a la complexitat argumentativa i al context disciplinar del text original.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He jerarquitzat els arguments i he refutat una objecció amb evidències."

### B2 — Acadèmic


**1. Tesi o postura inicial**
- Claredat i explicitació: Tesi sofisticada amb matisos conceptuals i posicionament acadèmic precís.

**2. Arguments**
- Coherència i progressió: 3-5 arguments amb relació entre si. Pot incloure argumentació per analogia.

**3. Exemples i evidències**
- Suport i credibilitat: Evidències variades (dades, cites, analogies). Jerarquitzades per credibilitat.

**4. Refutació o matís**
- Pensament crític: Refutació sistemàtica de les objeccions principals i integració dels matisos.

**5. Conclusió**
- Tancament i coherència: Conclusió que sintetitza, pot obrir noves preguntes i té veu acadèmica pròpia.

**6. Connectors argumentatius**
- Varietat i precisió: Connectors sofisticats. Pot usar modalitzadors i connectors concessius.

**7. Cites (B1+)**
- Integració i atribució: Múltiples cites ben atribuïdes i comentades críticament. Fonts diverses.

**8. Criteris transversals**
- No tesi implícita: Idem.
- Conclusió tancada: Idem.
- Fidelitat al text font: Fidelitat a la complexitat, als matisos i als debats del text original.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'assaig té tesi, arguments jerarquitzats, refutació i conclusió amb veu acadèmica pròpia."

### C1+ — Crític


