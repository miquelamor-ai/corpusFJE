---
name: write-diari
description: 'Use when adapting or generating a diari entry for students. Activates
  when genre_discursiu == "diari". Applies first person, separation of facts and emotions,
  named emotions, and learning- oriented conclusion. Output: diari entry in markdown
  with date and entry body.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: diari
tipologia: Narrativa / Reflexiva
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
  equals: diari
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-diari.md
font_version: 4.0.0-canonic
generat_at: '2026-06-14'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 6da2ae5763cb4771
---

# Escriure/adaptar una entrada de diari — skill operativa per a LLM

L'entrada de diari és una narració en primera persona on l'escriptor processa una experiència viscuda des de tres dimensions obligatòries: els **fets** (qué ha passat), les **emocions** (com m'he sentit) i la **reflexió** (qué he après o qué en penso). El seu tret definitori és la **separació neta entre blocs**: fets, emocions i reflexió han d'aparèixer en espais discursius diferenciats i no barrejats.

**Tipologia MALL**: Narrativa/Reflexiva (personal) · Expositiva/Justificativa (diari acadèmic, B1+).
**HCL principal**: Narrar — seqüenciar l'experiència en primera persona · Interpretar/Valorar — reflexió orientada a l'aprenentatge.
**HCL secundàries**: Expressar emocions (A1-B1) · Explicar — relació entre fets i aprenentatge (B1+) · Justificar — diari acadèmic (B1+) · Argumentar — reflexió crítica sobre l'experiència (C1).
**No s'adapta a pre-A1**: el diari requereix la producció autònoma en primera persona de **tres blocs metacognitius simultanis** — la separació conscient entre "el que ha passat", "el que he sentit" i "el que he après" és una operació metacognitiva que no és accessible sense base lecto-escriptora mínima i sense el concepte del "jo" com a subjecte narratiu explícit. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Emoció nomenada com a competència*: nomenar emocions amb precisió és una competència sociolingüística i emocional. El diari és el gènere on s'entrena explícitament: "estava bé" no és informació, "estava nerviós però content" és una observació accionable. El vocabulari d'emocions és tan acadèmic com el vocabulari disciplinar.
- *Diari acadèmic com a pont BICS→CALP*: la mateixa estructura (fets/emocions/reflexió) s'omple amb HCL progressivament més acadèmiques (Narrar → Explicar → Justificar). A B1+, el bloc fets es transforma en "observació o resultats", les emocions en "valoració del procés" i la reflexió en "conclusions". La transició BICS→CALP és visible i gradual en el mateix gènere.
- *Metacognició com a competència d'aprenentatge*: la reflexió orientada a l'aprenentatge ("qué he après" i "com ho he après") és la porta d'entrada a la metacognició. A B1+, el diari deixa de ser memorialístic i es converteix en una eina de regulació de l'aprenentatge transferible a totes les matèries.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu l'**entrada de diari adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Data i encapçalament**
- Format i precisió: Data en format simple: "Dilluns" / "12/05".

**2. Bloc fets**
- Seqüència i rellevància: 1-2 frases de fets en passat simple. Ordre cronològic estricte.

**3. Bloc emocions**
- Precisió i ancoratge: 1 emoció nomenada: "Estava content." / "Tenia por."

**4. Bloc reflexió**
- Profunditat i orientació: 1 frase de reflexió orientada a l'aprenentatge: "He après que..."

**5. Primera persona**
- Consistència i naturalitat: Primera persona consistent: "he", "em", "vaig".

**6. Criteris transversals**
- Separació dels blocs: Tres seccions clarament separades, 1 frase per bloc. Cap barreja fets/emocions.
- Variant acadèmica (B1+): No s'aplica.
- Fidelitat al text font: Fidelitat als fets principals i a la veu en primera persona.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He dit qué ha passat, com m'he sentit i qué he après."

### A1 — Inicial


**1. Data i encapçalament**
- Format i precisió: Data completa: "Dilluns, 12 de maig de 2026".

**2. Bloc fets**
- Seqüència i rellevància: 3-4 frases de fets ordenats cronològicament. Connectors simples.

**3. Bloc emocions**
- Precisió i ancoratge: 2 emocions amb matís lleu: "Estava una mica nerviós però content."

**4. Bloc reflexió**
- Profunditat i orientació: Reflexió de 2 frases amb connector causal: "Per això crec que..."

**5. Primera persona**
- Consistència i naturalitat: Primera persona en tots els verbs principals. Cap canvi a tercera persona.

**6. Criteris transversals**
- Separació dels blocs: Tres blocs diferenciats per paràgraf o línia en blanc.
- Variant acadèmica (B1+): No s'aplica.
- Fidelitat al text font: Fidelitat als fets, a les emocions i a la reflexió essencial.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He separat els fets de les emocions. He nomenat com em vaig sentir."

### A2 — Funcional


**1. Data i encapçalament**
- Format i precisió: Data completa + context breu si escau ("Primer dia de campaments").

**2. Bloc fets**
- Seqüència i rellevància: Fets narrats amb causa explícita. Connectors temporals variats. Selecció dels moments clau.

**3. Bloc emocions**
- Precisió i ancoratge: 2-3 emocions variades i situades en el moment: "Quan vaig veure X, em vaig sentir Y."

**4. Bloc reflexió**
- Profunditat i orientació: Conclusió clara de 2-3 frases. Diari acadèmic (B1+): "Els resultats mostren que..."

**5. Primera persona**
- Consistència i naturalitat: Primera persona consistent i variada. Veu pròpia recognoscible.

**6. Criteris transversals**
- Separació dels blocs: Tres paràgrafs clarament diferenciats amb transicions naturals entre blocs.
- Variant acadèmica (B1+): Quan el context és acadèmic (diari de laboratori, projecte): bloc fets → "Observació"; bloc reflexió → "Conclusions" ("Els resultats mostren que..."). El to és acadèmic, no memorialístic.
- Fidelitat al text font: Fidelitat als fets, a les emocions, a la reflexió i al to personal.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit una conclusió que explica qué he après i per qué."

### B1 — Estratègic


**1. Data i encapçalament**
- Format i precisió: Data completa integrada naturalment a l'entrada.

**2. Bloc fets**
- Seqüència i rellevància: Fets en relació amb el context. Selecció conscient dels fets més rellevants per a la reflexió.

**3. Bloc emocions**
- Precisió i ancoratge: Emocions analitzades: no només nomenades, sinó explicades en relació als fets.

**4. Bloc reflexió**
- Profunditat i orientació: Reflexió que connecta l'experiència amb coneixements previs o futurs.

**5. Primera persona**
- Consistència i naturalitat: Primera persona natural, no forçada. Veu personal diferenciada.

**6. Criteris transversals**
- Separació dels blocs: Blocs integrats amb transicions elaborades que mantenen la distinció fets/emocions/reflexió.
- Variant acadèmica (B1+): Tots tres blocs amb vocabulari acadèmic. Fets → Observació o resultats. Emocions → Valoració del procés. Reflexió → Conclusions.
- Fidelitat al text font: Fidelitat a la complexitat emocional i reflexiva del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He analitzat les meves emocions i les he relacionat amb el context."

### B2 — Acadèmic


**1. Data i encapçalament**
- Format i precisió: Data completa. Pot incloure el context situacional si és rellevant per a la comprensió.

**2. Bloc fets**
- Seqüència i rellevància: Fets narrats amb perspectiva sobre la seva significació. Pot incloure contrast entre expectativa i realitat.

**3. Bloc emocions**
- Precisió i ancoratge: Emocions complexes o contradictòries amb reflexió sobre el seu origen i significat.

**4. Bloc reflexió**
- Profunditat i orientació: Reflexió metacognitiva: "com he après" i "qué m'ha sorprès", no només "qué he après".

**5. Primera persona**
- Consistència i naturalitat: Primera persona reflexiva: "m'he adonat que", "he reconsiderat", "em pregunto si".

**6. Criteris transversals**
- Separació dels blocs: Blocs fluïts però clarament discernibles per al lector. La integració no amaga la distinció.
- Variant acadèmica (B1+): Reflexió crítica sobre el procés d'aprenentatge, incloent limitacions i reptes.
- Fidelitat al text font: Fidelitat a la complexitat, als matisos i a les contradiccions si les hi ha.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He reflexionat sobre com he après, no només sobre qué he après."

### C1+ — Crític


