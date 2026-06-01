---
name: generate-bastides-lectura
description: 'Use when the teacher has activated the "bastides" complement. Generates
  reading scaffolds for the 3 moments (Abans / Durant / Després) and 3 planes (literal
  / inferencial / crític). Always active when bastides complement is on, regardless
  of whether production complements are active. At Emergent/pre-A1: physical and gestural
  activities only — zero written production. Modulated by MECR level.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: bastides
agent_role: complements
tools_required: []
triggers:
- path: params.complements.bastides
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-bastides-lectura.md
font_version: 4.0.0-canonic
generat_at: '2026-06-01'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: c7eaf50803179e8c
---

# Generar bastides de lectura — skill operativa per a LLM

Les bastides de lectura són **suports temporals i retirables** que guien l'alumne als tres moments del procés lector (**Abans / Durant / Després**) i als tres plànols de comprensió (**literal / inferencial / crític**). El complement `bastides` les activa sempre que el docent vol estructurar el procés lector de l'alumne. La seva funció no és substituir el treball de comprensió detallat (això és tasca del complement `preguntes_comprensio`), sinó aportar el **procediment** (com llegir).

**Tipologia MALL**: Mediació cognitiva (bastida de lectura).
**HCL principal**: Mediar — orientar el procés lector amb suports retirables.
**HCL secundàries**: Predir (Abans, A1+) · Inferir (Durant/Després, A2+) · Valorar críticament (Després, B1+).
**Principi rector**: *"Menys és més"* — màxim 3 ítems per moment. Una bastida ben triada aporta més que deu ítems genèrics.

**Connexions MALL transversals:**
- *3 moments × 3 plànols*: el model MALL canònic estructura tant la seqüència temporal (avant/durant/après) com la profunditat cognitiva (literal/inferencial/crític). Aquest instrument els implementa explícitament.
- *Multimodalitat*: a pre-A1 totes les bastides són **físiques i gestuals** (assenyalar, dramatitzar, dibuixar). A A1, suport visual encara recomanat.
- *Bastida retirable (Vygotsky)*: la bastida té vocació d'extingir-se. El docent la introdueix les primeres 2-3 sessions i progressivament elimina els ítems que l'alumne ja fa sol. Una bastida que no es retira es converteix en dependència.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **bastides que ATNE o el docent presenten a l'alumne perquè llegeixi un text adaptat** (LECTURA). **No descriu la producció autònoma de l'alumne** — això és tasca del derivat propi (rúbrica d'avaluació formativa) i, si la tasca implica escriure, del pilot complementari `bastides-produccio`.
**Sub-granularitat dins de pre-A1 i A1**: es treballa amb la variable independent `fase_lectora` del frontmatter (logografica · alfabetica_emergent · alfabetica_fluida), no amb columnes addicionals.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Moment Abans**
- Activació de previs: L'adult activa amb una imatge: "Què veus aquí?". L'alumne assenyala o anomena.
- Propòsit de lectura: Propòsit oral de l'adult: "Anem a saber què passa amb [X]".

**2. Moment Durant**
- Modalitat lectora: L'adult llegeix en veu alta. L'alumne assenyala, dramatitza o dibuixa el que entén. **Zero lectura autònoma.**

**3. Moment Després**
- Plànol literal — Resum: Dibuixar el que ha après. Dictat oral a l'adult. Ordenació d'imatges.
- Autoregulació (metacognició): "He fet el que m'ha dit el mestre." (registre oral/gestual de l'adult).

**4. Criteris transversals**
- Volum màxim per moment: 1-2 accions gestuals/orals per moment.
- No duplicar `preguntes_comprensio`: Les bastides donen el procediment; les preguntes detallades són del complement `preguntes_comprensio`.
- Especificitat del propòsit: Propòsit referit a una imatge o paraula concreta del text.
- Format obligatori: Secció `## Suports de lectura` + 3 subseccions (Abans/Durant/Després).

**5. Autoavaluació (per l'alumne)**
- Reflexió en primera persona: *(via adult)* "He assenyalat el que m'ha demanat el mestre."

### A1 — Inicial


**1. Moment Abans**
- Activació de previs: 1 pregunta d'activació de previs en frase simple ("Què saps de [tema]?").
- Propòsit de lectura: Propòsit explícit i concret: "Llegeix per saber [una cosa concreta]".
- Hipòtesi prèvia: Predicció pel títol: "De què creus que parlarà?". 1 paraula o frase mínima.

**2. Moment Durant**
- Modalitat lectora: Lectura mediada per l'adult; l'alumne segueix amb el dit. Subratlla 1 mot clau per paràgraf.

**3. Moment Després**
- Plànol literal — Resum: **Frase-buit** literal d'un sol buit: "El text parla de ___".
- Autoregulació (metacognició): "He llegit el text amb el mestre i he marcat la paraula difícil."

**4. Criteris transversals**
- Volum màxim per moment: Màxim 3 ítems per moment.
- No duplicar `preguntes_comprensio`: Idem.
- Especificitat del propòsit: Propòsit específic del text actual, no genèric.
- Format obligatori: Idem.

**5. Autoavaluació (per l'alumne)**
- Reflexió en primera persona: "He marcat una paraula important. He completat la frase-buit del resum."

### A2 — Funcional


**1. Moment Abans**
- Activació de previs: 2 preguntes d'activació + ancoratge a una experiència concreta.
- Propòsit de lectura: + propòsit operatiu amb verb d'acció: "Llegeix per identificar [X]".
- Hipòtesi prèvia: Predicció breu escrita: "Crec que el text dirà…".

**2. Moment Durant**
- Modalitat lectora: Lectura autònoma possible. Marca ✓ (entès) / ? (dubte) / ! (important) al marge.

**3. Moment Després**
- Plànol literal — Resum: Resum breu de 2-3 frases sobre què tracta el text.
- Plànol inferencial: 1 pregunta inferencial guiada: "Per què creus que…?".
- Autoregulació (metacognició): "He llegit i he marcat ✓/? / !. He fet el resum."

**4. Criteris transversals**
- Volum màxim per moment: Màxim 3 ítems per moment.
- No duplicar `preguntes_comprensio`: Idem.
- Especificitat del propòsit: Idem.
- Format obligatori: Idem.

**5. Autoavaluació (per l'alumne)**
- Reflexió en primera persona: "He marcat ✓/? /! mentre llegia. He escrit de què tracta el text."

### B1 — Estratègic


**1. Moment Abans**
- Activació de previs: Activació + predicció pel títol o imatge inicial.
- Propòsit de lectura: + propòsit jeràrquic: "Llegeix per distingir el fet principal del context".
- Hipòtesi prèvia: Hipòtesi pròpia formulada per escrit: "Hipòtesi: ___. Per què: ___".

**2. Moment Durant**
- Modalitat lectora: Lectura autònoma. Notes marginals breus (1-3 paraules per marca).
- Hipòtesi en curs: **Pausa obligatòria** marcada al text (símbol ⏸ o instrucció "Atura't aquí") on l'alumne escriu hipòtesi en curs: "Fins aquí, crec que el text dirà que…".

**3. Moment Després**
- Plànol literal — Resum: Resum estructurat de 3-4 frases (idea principal + 2 secundàries).
- Plànol inferencial: Inferència explícita: "Quin era l'objectiu de l'autor?" + "Què queda implícit?".
- Plànol crític / Valoració: Valoració simple: "Estàs d'acord amb el que diu el text? Per què?".
- Autoregulació (metacognició): "He revisat si la meva hipòtesi inicial era correcta o no."

**4. Criteris transversals**
- Volum màxim per moment: Màxim 3 ítems per moment.
- No duplicar `preguntes_comprensio`: Idem.
- Especificitat del propòsit: Idem.
- Format obligatori: Idem.

**5. Autoavaluació (per l'alumne)**
- Reflexió en primera persona: "He fet una hipòtesi abans de llegir. He comprovat si era correcta."

### B2 — Acadèmic


**1. Moment Abans**
- Activació de previs: + identificació del gènere i de l'autor/font.
- Propòsit de lectura: + propòsit avaluatiu: "Llegeix per avaluar la fiabilitat de les dades".
- Hipòtesi prèvia: + identificació del posicionament inicial probable de l'autor.

**2. Moment Durant**
- Modalitat lectora: + identificació explícita del posicionament de l'autor al marge.
- Hipòtesi en curs: + a la mateixa pausa, **revisió explícita** de la hipòtesi inicial: "La meva hipòtesi era X, ara crec Y, per què…".

**3. Moment Després**
- Plànol literal — Resum: Resum amb jerarquització explícita (titular + cos).
- Plànol inferencial: + detecció de pressuposicions i seleccions narratives no explícites.
- Plànol crític / Valoració: Avaluació de fiabilitat: "Fins a quin punt és objectiu l'autor? Quines proves dóna?".
- Autoregulació (metacognició): "He pensat si l'autor és imparcial. He comprovat si dóna proves de les seves afirmacions."

**4. Criteris transversals**
- Volum màxim per moment: Màxim 3 ítems per moment.
- No duplicar `preguntes_comprensio`: Idem.
- Especificitat del propòsit: Idem.
- Format obligatori: Idem.

**5. Autoavaluació (per l'alumne)**
- Reflexió en primera persona: "He identificat la postura de l'autor. He avaluat si les dades eren fiables."

### C1+ — Crític


**1. Moment Abans**
- Activació de previs: + l'alumne formula les seves pròpies preguntes de lectura abans de llegir.
- Propòsit de lectura: + propòsit metacognitiu: l'alumne formula el seu propi propòsit i justifica per què.
- Hipòtesi prèvia: + plantejament d'hipòtesis contrastades.

**2. Moment Durant**
- Modalitat lectora: + contrast actiu amb coneixements previs anotat: "Aquí diu X però jo sabia Y".
- Hipòtesi en curs: + a la mateixa pausa, **reformulació metacognitiva**: "Si la meva hipòtesi falla, què revela el text que jo no sabia?".

**3. Moment Després**
- Plànol literal — Resum: Resum sintètic + comparació amb hipòtesi inicial.
- Plànol inferencial: + anàlisi de l'enquadrament: "Què queda fora del marc del text? Per què?".
- Plànol crític / Valoració: Contrast crític: "Quines altres fonts caldrien per validar aquesta informació?".
- Autoregulació (metacognició): "He entès tot el que calia? Quines preguntes m'han quedat obertes? Quin pas faria a continuació?"

**4. Criteris transversals**
- Volum màxim per moment: Màxim 3 ítems per moment.
- No duplicar `preguntes_comprensio`: Idem.
- Especificitat del propòsit: Idem.
- Format obligatori: Idem.

**5. Autoavaluació (per l'alumne)**
- Reflexió en primera persona: "He formulat les meves pròpies preguntes abans de llegir i he comprovat si el text les responia."

