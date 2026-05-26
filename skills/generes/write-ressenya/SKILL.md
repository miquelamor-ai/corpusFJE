---
name: write-ressenya
description: 'Use when adapting or generating a ressenya for students. Activates when
  genre_discursiu == "ressenya". Applies description before valuation, fact/judgment
  separation, and concrete recommendation. Output: ressenya in markdown with work,
  description, valuation, and recommendation.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: ressenya
tipologia: Argumentativa / Avaluativa
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
  equals: ressenya
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-ressenya.md
font_version: 4.0.0-canonic
generat_at: '2026-05-26'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: f59b53f911f435f6
---

# Escriure/adaptar una ressenya — skill operativa per a LLM

La ressenya descriu i valora una obra (llibre, pel·lícula, disc, exposició, videojoc) des del posicionament personal argumentat de qui la fa. El seu tret definitori és la **seqüència invariant descripció → valoració**: primer s'explica qué és l'obra i de qué tracta (sense jutjar), i després es valora. La valoració sense descripció és una opinió buida; la descripció sense valoració és una sinopsi. La ressenya integra les dues en seqüència explícita.

**Tipologia MALL**: Argumentativa/Avaluativa.
**HCL principal**: Interpretar/Valorar — posicionar-se davant d'una obra i justificar el posicionament amb evidències de la pròpia obra.
**HCL secundàries**: Descriure — presentar l'obra en termes objectius (qui l'ha fet, de qué tracta, estructura) · Argumentar (B1+) — comparació entre obres o contrast de valoracions.
**Distinció clau MALL**: la ressenya activa Interpretar/Valorar, no Argumentar com a motor principal. L'assaig convènç sobre una tesi abstracta; la ressenya posiciona i valora una obra concreta. La diferència és el referent (abstracció vs. obra) i el grau de persuasió.
**No s'adapta a pre-A1**: la ressenya requereix la comprensió de la distinció entre fets i judicis com a operació metacognitiva — "La pel·lícula dura 2 hores" és un fet; "és massa llarga" és un judici. Aquesta separació entre el que existeix i el que s'opina sobre el que existeix requereix base lecto-escriptora mínima i capacitat metacognitiva mínima. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *HCL Interpretar/Valorar com a meta-competència*: la ressenya entrena la capacitat de llegir una obra, processar-la i prendre una postura argumentada. És la HCL que requereix més integració cognitiva: comprensió + interpretació + judici + comunicació. Transferible a la valoració de fonts científiques, arguments polítics i produccions culturals diverses.
- *Descripció primer com a bastida epistèmica*: l'alumne ha de demostrar que ha comprès l'obra ABANS de valorar-la. Això evita el judici buit i construeix una lògica de pensament transferible a totes les disciplines: evidència primer, interpretació després.
- *Fet vs. judici com a competència de pensament crític transversal*: la separació entre "La pel·lícula dura 2 hores" (fet objectiu) i "és massa llarga" (judici subjectiu) és la mateixa que la diferència entre dades i conclusions en ciència, entre observació i interpretació en història. La ressenya és el gènere que entrena aquesta separació de manera explícita.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **ressenya adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Identificació de l'obra**
- Completitud i context: Títol + autor/director. 1 frase.

**2. Descripció (SEMPRE primer)**
- Objectivitat i seqüència: 2-3 frases: de qué va l'obra. SENSE valorar. SEMPRE PRIMER.

**3. Separació fets/judicis**
- Metacognició i precisió: Senyals lingüístics visibles: "crec que", "m'ha agradat". Separació mínima visible.

**4. Arguments valoratius**
- Suport i credibilitat: 1 argument senzill: "m'ha agradat perquè…" + 1 fet de l'obra.

**5. Recomanació concreta**
- Perspectivisme: "La recomano / No la recomano." 1 frase.

**6. Sense spoilers**
- Control de la informació: No revelar el final.

**7. Criteris transversals**
- No sarcasme ni ironia a la valoració: Sense sarcasme ni ironia. Pot confondre alumnat nouvingut o amb TEA.
- No comparació sense context: Cap comparació amb obres que el lector probablement no coneix.
- Fidelitat al text font: Fidelitat a l'obra identificada i al contingut descriptiu bàsic.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He dit el títol i l'autor. He explicat de qué va. He dit si m'ha agradat i per qué."

### A1 — Inicial


**1. Identificació de l'obra**
- Completitud i context: Títol + autor/director + gènere + any. 1-2 frases.

**2. Descripció (SEMPRE primer)**
- Objectivitat i seqüència: 3-4 frases descriptives del contingut. Sense cap judici. SEMPRE PRIMER.

**3. Separació fets/judicis**
- Metacognició i precisió: Separació clara: bloc descriptiu → bloc valoratiu. Sense barrejar dins d'una frase.

**4. Arguments valoratius**
- Suport i credibilitat: 2 arguments concrets amb 1 fet de l'obra cadascun.

**5. Recomanació concreta**
- Perspectivisme: "La recomano a qui li agradi…" + 1 condició concreta.

**6. Sense spoilers**
- Control de la informació: No revelar girs principals de la trama si l'obra és narrativa.

**7. Criteris transversals**
- No sarcasme ni ironia a la valoració: Idem.
- No comparació sense context: Idem.
- Fidelitat al text font: Fidelitat a l'obra, als arguments principals i al to de la valoració.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He separat el que és l'obra del que en penso. He donat 1 argument per a la valoració."

### A2 — Funcional


**1. Identificació de l'obra**
- Completitud i context: Identificació completa + context breu (de qué va, per a qui és).

**2. Descripció (SEMPRE primer)**
- Objectivitat i seqüència: Descripció del contingut, estructura i elements principals. Sense valoració.

**3. Separació fets/judicis**
- Metacognició i precisió: Separació neta amb connectors de transició: "Pel que fa a la meva valoració…", "En la meva opinió…".

**4. Arguments valoratius**
- Suport i credibilitat: 3 arguments ben diferenciats (contingut, forma, impacte). Cada un amb evidència de l'obra.

**5. Recomanació concreta**
- Perspectivisme: Recomanació per a un públic específic amb justificació.

**6. Sense spoilers**
- Control de la informació: No revelar elements sorpresa. Indicar "sense revelar el final" si cal.

**7. Criteris transversals**
- No sarcasme ni ironia a la valoració: Idem. La ironia és admissible en ressenyes C1 quan el to de l'obra ho permet explícitament.
- No comparació sense context: Idem. La comparació és admissible si s'explica breument l'obra de referència.
- Fidelitat al text font: Fidelitat a l'obra, als arguments, als fets citats i a la recomanació essencial.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He donat 3 arguments per defensar la meva valoració. He evitat revelar el final."

### B1 — Estratègic


**1. Identificació de l'obra**
- Completitud i context: Identificació amb context cultural o biogràfic rellevant de l'autor.

**2. Descripció (SEMPRE primer)**
- Objectivitat i seqüència: Descripció completa amb elements formals (estructura, personatges, estil) si és rellevant.

**3. Separació fets/judicis**
- Metacognició i precisió: Distinció precisa entre el que és objectiu (fet de l'obra) i el que és subjectiu (judici argumentat).

**4. Arguments valoratius**
- Suport i credibilitat: Arguments elaborats amb exemples concrets i específics de l'obra.

**5. Recomanació concreta**
- Perspectivisme: Recomanació matisada: per a qui sí, per a qui potser no.

**6. Sense spoilers**
- Control de la informació: Control conscient de la informació revelada. El lector pot decidir si vol llegir-la.

**7. Criteris transversals**
- No sarcasme ni ironia a la valoració: Idem.
- No comparació sense context: Comparació amb obres del mateix autor o gènere admesa amb context.
- Fidelitat al text font: Fidelitat a la complexitat valorativa i al context de la ressenya original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Els meus judicis van acompanyats de fets concrets de l'obra. La recomanació és per a un públic concret."

### B2 — Acadèmic


**1. Identificació de l'obra**
- Completitud i context: Identificació amb context ampli: tradició, gènere, recepció crítica inicial.

**2. Descripció (SEMPRE primer)**
- Objectivitat i seqüència: Descripció precisa que permet al lector entendre l'obra sense haver-la llegit o vista.

**3. Separació fets/judicis**
- Metacognició i precisió: Distinció sofisticada entre descripció, interpretació i valoració com a tres capes explícites.

**4. Arguments valoratius**
- Suport i credibilitat: Arguments rigorosos amb cites o referències específiques a l'obra.

**5. Recomanació concreta**
- Perspectivisme: Recomanació crítica que pot contenir reserves o condicions.

**6. Sense spoilers**
- Control de la informació: Gestió precisa: descriure sense revelar, incitar sense enganyar.

**7. Criteris transversals**
- No sarcasme ni ironia a la valoració: Ironia admesa si el context cultural de l'obra i el del lector la fan accessible.
- No comparació sense context: Comparació intertextual admesa com a recurs analític.
- Fidelitat al text font: Fidelitat a la complexitat, als matisos i a les referències de la ressenya original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He distingit descripció, interpretació i valoració. La recomanació és matisada i argumentada."

### C1+ — Crític


