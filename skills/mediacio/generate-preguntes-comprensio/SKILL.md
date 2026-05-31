---
name: generate-preguntes-comprensio
description: 'Use when the teacher has activated the "preguntes_comprensio" complement.
  Generates a comprehension reading guide following the MALL/TILC model: 3 reading
  moments (before, during, after) × 3 cognitive planes (literal, inferential, critical).
  Modulated by MECR level and literary vs informative register. Pre-A1: no autonomous
  writing — pointing, drawing, dramatisation, adult dictation only.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: preguntes_comprensio
agent_role: complements
tools_required: []
triggers:
- path: params.complements.preguntes_comprensio
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-preguntes-comprensio.md
font_version: 4.0.0-canonic
generat_at: '2026-05-31'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: c801776dff1ac28c
---

# Generar preguntes de comprensió — skill operativa per a LLM

Les preguntes de comprensió lectora segueixen el **model MALL de 3 moments × 3 plànols cognitius**: les preguntes acompanyen l'alumne **Abans / Durant / Després** de la lectura, i treballen progressivament els plànols **literal → inferencial → crític**. El complement no és un examen final: és un **guió actiu de lectura** que estructura el procés de construcció de sentit.

**Tipologia MALL**: Mediació cognitiva (guia del procés lector).
**HCL principals**: Comprendre (literal, A1+) · Inferir (inferencial, A2+) · Valorar críticament (crític, B1+).
**HCL secundàries**: Predir (Abans de llegir, A1+) · Monitorar (Durant, A2+) · Crear/Imaginar (crític creatiu, pre-A1+).
**Principi rector**: *"Menys és més"* (MALL) — màxim 10 preguntes totals. 6-8 és l'òptim. Una pregunta inferencial ben construïda genera més aprenentatge que cinc de literals.

**Translanguaging — Pas d'acarament L1↔L2**: el complement inclou explícitament, per a alumnat nouvingut (A1-C1), una pregunta d'acarament de llengues que invita a activar la L1 com a recurs cognitiu. És la implementació directa del TOLC (Transfer of Literacy and Cognition, Cummins).

**Interacció intra-pipeline amb `bastides-lectura`**: si tots dos complements son actius simultàniament, les preguntes han de ser **ortogonals** a les bastides. `preguntes_comprensio` **guanya** amb prioritat de dedup: si un ítem és equivalent a un de les bastides, es replanteja la pregunta o s'elimina. La bastida dona el procediment (com llegir); la pregunta, el contingut (qué entendre). Patró cross_source intra-pipeline confirmat al corpus-spec v2.7 (mineraIRAG).

**Pre-A1 SÍ (D6)**: les "preguntes" a pre-A1 son consignes d'acció (assenyalar, dibuixar, dramatitzar, dictat a l'adult). Els 3 plànols cognitius son accessibles des d'infantil: el plànol crític s'introdueix oralment ("Qué hauries fet tu?"). Cap escriptura autònoma.

**Connexions MALL transversals:**
- *3 moments × 3 plànols*: el model MALL canònic estructura tant la seqüència temporal (avant/durant/après) com la profunditat cognitiva (literal/inferencial/crític). Les preguntes implementen explícitament aquesta bidimensionalitat.
- *Propòsit de lectura*: l'activació prèvia ("Llegeix per saber [X concret]") és el factor amb major impacte demostrat en la comprensió lectora. Sense propòsit, l'alumne llegeix sense construir sentit.
- *Acarament L1↔L2 (TOLC)*: la pregunta "Com es diu X en la teva llengua?" no és decorativa. Activa la xarxa semàntica en L1, que dona suport cognitiu a la comprensió en L2. Per a nouvinguts, l'acarament és la bastida conceptual més efectiva.
- *Multimodalitat*: a pre-A1 i A1, les consignes d'acció i les imatges substitueixen el text escrit. El repte cognitiu (inferir, valorar) no requereix producció escrita.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **preguntes que es generen per guiar la comprensió del text adaptat** (LECTURA ACTIVA). **No descriu l'avaluació del docent ni la producció autònoma de l'alumne**. El complement no és un examen: l'alumne usa les preguntes per llegir millor, no per ser avaluat.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → consignes d'assenyalar/dibuixar, mediació oral total. `fase_lectora: alfabetica_emergent` → consigna escrita simple, 1-2 paraules de resposta.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Moment "Abans de llegir"**
- Activació + propòsit: Adult estableix el propòsit en veu alta. Consigna de predicció visual: "Assenyala la imatge que creus que explica de qué va el text."

**2. Moment "Durant la lectura"**
- Aturada estratègica: Adult atura i pregunta: "Mostra'm on és [element del text]." Assenyalar o apuntar.

**3. Moment "Després de llegir"**
- 3 plànols cognitius: Literal: "Assenyala la imatge de [element del text]" o "Dibuixa [element]." Inferencial: "Per qué creus que...?" (oral, mediat). Crític: "Qué hauries fet tu?" (oral).

**4. Criteris transversals**
- Format + modalitat + acarament: Consignes d'acció (mai V/F). Cap numeració: usar `-`. Cap etiqueta visible [Literal]. Màxim 6 consignes.

**5. Autoavaluació mediada**
- Metacognició: "He assenyalat les imatges que m'ha demanat el mestre." (oral, mediat per adult)

### A1 — Inicial


**1. Moment "Abans de llegir"**
- Activació + propòsit: Activació: "Escriu 1 paraula sobre el que saps de [tema]." Propòsit: "Llegeix per saber [X concret]."

**2. Moment "Durant la lectura"**
- Aturada estratègica: "Para a [punt]. Hi ha alguna paraula que no entens? Marca-la amb ?."

**3. Moment "Després de llegir"**
- 3 plànols cognitius: Literal: V/F senzill o omple buit amb llista tancada. Inferencial: inferència mínima connectada a evidència visual o mot clau del text ("Per qué creus que [element]? Mira [part del text]"). Crític: oral o dibuix ("T'ha agradat? Dibuixa com t'has sentit").

**4. Criteris transversals**
- Format + modalitat + acarament: Mai V/F de frase complexa. Mai "copia i enganxa" (resposta copiable sense processament). Frases pregunta: màxim 10 paraules. Màxim 8 preguntes totals. LITERARI: "Qui és el personatge? Com se sent?" INFORMATIU: "Quina és la informació més important?"

**5. Autoavaluació mediada**
- Metacognició: "He respost si és vertader o fals. He omplert els buits."

### A2 — Funcional


**1. Moment "Abans de llegir"**
- Activació + propòsit: Activació: "Escriu 2-3 coses que saps sobre [tema]." Propòsit: "Llegeix per trobar [2 informacions concretes]."

**2. Moment "Durant la lectura"**
- Aturada estratègica: "Para a [punt]. Escriu en 1 frase el que ha passat fins ara."

**3. Moment "Després de llegir"**
- 3 plànols cognitius: Literal: ordenar seqüències, relacionar amb fletxes. Inferencial: causa literal al text ("Per qué...? Busca-ho al text"). Crític: "Qué hauria passat si [canvi]?" Resposta breu.

**4. Criteris transversals**
- Format + modalitat + acarament: Frases pregunta: màxim 12 paraules. Màxim 10 preguntes. LITERARI: pregunta afectiva. INFORMATIU: pregunta de precisió. Acarament L1 (si nouvingut): "Com es diu [terme clau] en la teva llengua?"

**5. Autoavaluació mediada**
- Metacognició: "He ordenat les idees. He trobat la idea principal."

### B1 — Estratègic


**1. Moment "Abans de llegir"**
- Activació + propòsit: Activació + 2 preguntes pròpies: "Qué saps? Qué et preguntes?" Propòsit: "Llegeix per entendre com [causa-efecte o seqüència]."

**2. Moment "Durant la lectura"**
- Aturada estratègica: "Para a [punt]. Quina hipòtesi tens sobre el que passarà o dirà a continuació?"

**3. Moment "Després de llegir"**
- 3 plànols cognitius: Literal: 1-2 frases, resposta explícita al text. Inferencial: deducció relacional ("Quin efecte té [causa]? Argumenta-ho"). Crític: postura justificada (literari: sentiments; informatiu: fiabilitat de les dades).

**4. Criteris transversals**
- Format + modalitat + acarament: Frases pregunta: màxim 15 paraules. Màxim 10 preguntes. LITERARI: símbols i metàfores simples. INFORMATIU: jerarquitzar amb connectors. Acarament L1 (si nouvingut): "El text s'escriuria igual en la teva llengua?"

**5. Autoavaluació mediada**
- Metacognició: "He deduït informació que no estava explícita al text. He fet una hipòtesi durant la lectura."

### B2 — Acadèmic


**1. Moment "Abans de llegir"**
- Activació + propòsit: Activació del marc teòric o experiència prèvia. Propòsit d'avaluació: "Llegeix per avaluar si [afirmació] és vàlida."

**2. Moment "Durant la lectura"**
- Aturada estratègica: "Para a [punt]. Quina idea principal s'ha presentat fins ara? Com s'estructura argumentalment?"

**3. Moment "Després de llegir"**
- 3 plànols cognitius: Literal: resum de 3-5 frases amb jerarquització. Inferencial: justificació + referència al text. Crític: argumentació oberta + avaluació de la fiabilitat.

**4. Criteris transversals**
- Format + modalitat + acarament: Màxim 10 preguntes. LITERARI: veu narrativa i intenció estètica. INFORMATIU: fiabilitat de les dades. Acarament L1 (si nouvingut): contrast d'argumentació entre català i L1.

**5. Autoavaluació mediada**
- Metacognició: "He argumentat les meves respostes amb referències al text. He avaluat si les dades eren fiables."

### C1+ — Crític


**1. Moment "Abans de llegir"**
- Activació + propòsit: Propòsit d'anàlisi autorial: "Llegeix per analitzar com l'autor construeix la seva postura i quines proves aporta."

**2. Moment "Durant la lectura"**
- Aturada estratègica: "Para a [punt]. Quina és la postura de l'autor fins aquí? Quines proves ha aportat? N'hi ha d'absents?"

**3. Moment "Després de llegir"**
- 3 plànols cognitius: Literal: síntesi estructurada jerarquitzada. Inferencial: relacions implícites complexes, ironia, subtext. Crític: judici sobre intencionalitat, contrast amb fonts alternatives.

**4. Criteris transversals**
- Format + modalitat + acarament: Màxim 10 preguntes (prioritzar qualitat). LITERARI: intertextualitat i intencionalitat. INFORMATIU: contrast de fonts i biaix. Acarament L1 (si nouvingut): contrast metalingüístic i discursiu.

**5. Autoavaluació mediada**
- Metacognició: "He analitzat la intencionalitat de l'autor i he qüestionat les seves afirmacions. He contrastat amb el que ja sabia."

