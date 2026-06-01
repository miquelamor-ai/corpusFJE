---
name: write-entrevista
description: 'Use when adapting or generating an entrevista for students. Activates
  when genre_discursiu == "entrevista". Applies direct questions, first-person responses,
  visible labels, and preserved Q/A format. Output: entrevista in markdown with presentation
  and question/answer pairs.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: entrevista
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
  equals: entrevista
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-entrevista.md
font_version: 4.0.0-canonic
generat_at: '2026-06-01'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: d6162eecae9b5e0e
---

# Escriure/adaptar una entrevista — skill operativa per a LLM

L'entrevista és un gènere dialogat d'informació: una persona (entrevistador) pregunta i una altra (entrevistat) respon. El seu tret definitori és el **format P/R invariant**: la seqüència pregunta-resposta s'ha de mantenir sempre com a parells atribuïts i mai no es pot convertir en prosa narrativa. L'etiqueta visible (**P:** / **R:**) és el marcador gràfic del gènere.

**Tipologia MALL**: Dialogada/Informativa.
**HCL principal**: Descriure — qui és l'entrevistat i quines idees defensa.
**HCL secundàries**: Argumentar — quan l'entrevistat defensa una postura (B1+).
**No s'adapta a pre-A1**: l'entrevista requereix la comprensió de la **seqüència P/R com a relació dialogada**: entendre que "P:" i "R:" son torns de paraula atribuïts a persones different, i que una pregunta espera una resposta de la mateixa persona. Aquesta abstracció de relació dialogada i lectura d'etiquetes semàntiques no és accessible sense base lecto-escriptora mínima. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Format P/R com a seqüència conversacional*: l'entrevista és la representació escrita de la conversa pregunta-resposta, la seqüència d'adjacència més bàsica de la interacció. Treballar-la entrena la comprensió del torn de paraula i la relació entre interlocutors, que és la base de tota literacitat dialògica.
- *La pregunta com a eina cognitiva*: formular preguntes precises d'una sola idea és una competència de pensament crític. Diferenciar preguntes obertes, tancades, múltiples i retòriques és un aprenentatge metalingüístic transferible a totes les matèries.
- *HCL Argumentar en context accessible*: quan l'entrevistat defensa una postura, l'alumne veu la HCL Argumentar en acció dins d'un format accessible. L'entrevista és el pont entre la descripció (qui és) i l'assaig (per què ho defensa).

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu l'**entrevista adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Presentació de l'entrevistat**
- Context i rellevància: 1 frase: qui és i per qué.

**2. Format P/R (etiquetes)**
- Consistència gràfica: **P:** i **R:** en negreta. Consistent en tot el text.

**3. Preguntes directes (1 sola idea)**
- Precisió i focus: Preguntes de 1-2 paraules clau o 1 frase simple ("Qué fas?", "On vius?").

**4. Respostes en 1a persona**
- Veu i autenticitat: Respostes de 1-2 frases en primera persona.

**5. Nombre de parells P/R**
- Extensió i cobertura: 3-4 parells P/R.

**6. Criteris transversals**
- Termes tècnics de l'entrevistat: Sense termes tècnics (o amb explicació immediata entre parèntesi).
- No linearitzar: Cap frase de transició narrativa entre P/R ("l'entrevistat va contestar que..."). Format P/R pur.
- Fidelitat al text font: Fidelitat a les idees principals de l'entrevistat i al format P/R.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit qui és l'entrevistat. He escrit 3-4 preguntes i respostes marcades amb P i R."

### A1 — Inicial


**1. Presentació de l'entrevistat**
- Context i rellevància: 2 frases: qui és i per qué és rellevant entrevistar-lo.

**2. Format P/R (etiquetes)**
- Consistència gràfica: **P:** i **R:** en negreta. Format perfectament consistent.

**3. Preguntes directes (1 sola idea)**
- Precisió i focus: Preguntes directes d'una sola idea. Sense preguntes dobles ni retòriques.

**4. Respostes en 1a persona**
- Veu i autenticitat: Respostes de 2-3 frases. Primera persona consistent. Cap transformació a 3a persona.

**5. Nombre de parells P/R**
- Extensió i cobertura: 4-5 parells P/R.

**6. Criteris transversals**
- Termes tècnics de l'entrevistat: 1 terme tècnic màxim, explicat entre parèntesi o al costat.
- No linearitzar: Idem.
- Fidelitat al text font: Fidelitat a les idees, al registre bàsic i al format.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Cada pregunta té una sola idea. Les respostes son en primera persona."

### A2 — Funcional


**1. Presentació de l'entrevistat**
- Context i rellevància: 3-4 frases de context professional o personal que justifiquen l'entrevista.

**2. Format P/R (etiquetes)**
- Consistència gràfica: **P:** i **R:** en negreta. Cap ambigüitat sobre qui parla en cap moment.

**3. Preguntes directes (1 sola idea)**
- Precisió i focus: Preguntes d'una idea que exploren un aspecte concret. Sense preguntes retòriques.

**4. Respostes en 1a persona**
- Veu i autenticitat: Respostes de 3-4 frases amb matís. Veu de l'entrevistat preservada i recognoscible.

**5. Nombre de parells P/R**
- Extensió i cobertura: 5-6 parells P/R.

**6. Criteris transversals**
- Termes tècnics de l'entrevistat: Termes tècnics explicats entre claudàtors [terme: significat] o en nota al final.
- No linearitzar: Idem.
- Fidelitat al text font: Fidelitat a les idees, al registre, a la veu de l'entrevistat i al format.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Les meves preguntes exploren aspectes interessants. He explicat els termes difícils."

### B1 — Estratègic


**1. Presentació de l'entrevistat**
- Context i rellevància: Presentació completa amb context social o professional.

**2. Format P/R (etiquetes)**
- Consistència gràfica: **P:** i **R:** en negreta. La veu de l'entrevistat és lingüísticament diferenciable de la del periodista.

**3. Preguntes directes (1 sola idea)**
- Precisió i focus: Preguntes que conviden a defensar posicions o explicar processos complexos.

**4. Respostes en 1a persona**
- Veu i autenticitat: Respostes que mostren el punt de vista de l'entrevistat amb arguments i evidències.

**5. Nombre de parells P/R**
- Extensió i cobertura: 6-7 parells P/R. Pot incloure 1 pregunta de seguiment.

**6. Criteris transversals**
- Termes tècnics de l'entrevistat: Termes tècnics explicats naturalment dins del text.
- No linearitzar: Idem.
- Fidelitat al text font: Fidelitat a la complexitat de les idees i al to de l'entrevistat.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'entrevistat defensa una postura clara. He fet preguntes de seguiment."

### B2 — Acadèmic


**1. Presentació de l'entrevistat**
- Context i rellevància: Presentació que situa l'entrevistat en el seu camp i dona el marc de l'entrevista.

**2. Format P/R (etiquetes)**
- Consistència gràfica: **P:** i **R:** en negreta. La diferència de registre i veu entre entrevistador i entrevistat és evident.

**3. Preguntes directes (1 sola idea)**
- Precisió i focus: Preguntes que qüestionen, matisen o aprofundeixen. Pot incloure preguntes de seguiment.

**4. Respostes en 1a persona**
- Veu i autenticitat: Respostes que mostren la complexitat de la postura. Pot incloure matisos i contradiccions.

**5. Nombre de parells P/R**
- Extensió i cobertura: 7-10 parells P/R. Moments de tensió dialèctica quan el tema ho permet. La profunditat de cada rèplica és més rellevant que el nombre total.

**6. Criteris transversals**
- Termes tècnics de l'entrevistat: Termes tècnics integrats; glossari al final si hi ha molts.
- No linearitzar: Idem. Pot incloure una nota editorial breu entre claudàtors [nota de la redacció] si és rellevant.
- Fidelitat al text font: Fidelitat a la complexitat, al to, als matisos i als moments de tensió del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'entrevista mostra la complexitat de les idees de l'entrevistat. He revisat que no hi hagi linearització."

### C1+ — Crític


