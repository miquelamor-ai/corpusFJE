---
name: generate-activitats-aprofundiment
description: 'Use when the teacher has activated the "activitats_aprofundiment" complement.
  Generates 2-3 cognitive challenge activities that extend the adapted text: interdisciplinary
  connections, critical thinking, guided research, debate and (when the text allows
  it) a plurilingual dimension. Modulated by stage and MECR.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: activitats_aprofundiment
agent_role: complements
tools_required: []
triggers:
- path: params.complements.activitats_aprofundiment
  equals: true
moduls_relacionats:
- M2
- M4
font_canonic: M3_instrument-generar-activitats-aprofundiment.md
font_version: 4.0.0-canonic
generat_at: '2026-06-06'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: ef0bfd256305893c
---

# Generar activitats d'aprofundiment — skill operativa per a LLM

Les activitats d'aprofundiment porten l'alumne **una passa més enllà del text**: connectar, qüestionar, investigar, argumentar. Són 2-3 activitats de repte cognitiu post-lectura. No son preguntes de comprensió literal; no son producció textual del gènere (bastides-produccio, plantilles-genere): son **extensió cognitiva** que activa els plànols inferencial i crític sobre el contingut treballat.

**Tipologia MALL**: Mediació (extensió cognitiva post-lectura).
**HCL principals**: Argumentar · Valorar críticament · Crear/Imaginar.
**HCL secundàries**: Investigar · Comparar · Connectar interdisciplinarment.
**5 tipus d'activitats**: connexions interdisciplinars · pensament crític ("i si...?") · recerca guiada · debat o reflexió argumentada · dimensió plurilingüe.
**Principi rector — Repte igualitari (MALL)**: adaptar l'**accés**, no el repte. Un alumne pre-A1 que ordena imatges per seqüència causal fa pensament d'alt nivell sense escriure. La dificultat cognitiva és equivalent per a tots els nivells; canvia la forma d'accedir-hi i de produir-la.

**Translanguaging — Dimensió plurilingüe (Pas 4)**: a A2+, una de les activitats pot invitar explícitament a comparar termes o conceptes entre L1 i el català. Aquesta activitat genera contingut en L1 (translanguaging actiu). La consigna **mai exposa cap alumne**: "Si coneixes la paraula en una altra llengua, comparteix-ho si vols."

**Pre-A1 SÍ (D6)**: les activitats d'aprofundiment son compatibles amb pre-A1 si son físiques o manipulatives i cognitiu-exigents. "Ordena les imatges de la cadena alimentària de la mes gran a la mes petita" és pensament crític. Cap escriptura autònoma.

**Diferència crítica amb complements propers:**
- `preguntes_comprensio`: comprensió del text (literal, inferencial, crític). **No va més enllà del text.**
- `activitats_aprofundiment`: extensió cognitiva post-lectura. **Va més enllà del text.**
- `bastides_produccio` / `plantilles_genere`: guia o bastida per a la producció textual del gènere.
- `cartes_conversacionals`: debat estructurat amb rols explícits i cartes de rol.

**Connexions MALL transversals:**
- *Repte igualitari*: el MALL advoca per activitats cognitivament exigents per a TOTS els alumnes, independentment del MECR. Un alumne nouvingut pre-A1 pot fer pensament de nivell superior si té accés multimodal al repte. Adaptar l'accés (llengua, format) no vol dir reduir el repte.
- *Consigna amb producte*: "Investiga sobre X" és una consigna vaga. "Busca 2 exemples de X a la teva vida quotidiana i explica per qué encaixen" és accionable. La consigna ha de dir sempre QUÈ cal fer i QUIN és el producte final (dibuix, llista, 1 frase, mapa, debat).
- *Dimensió plurilingüe com a recurs cognitiu*: la comparació entre L1 i L2 no és una concessió: és una activació de la xarxa conceptual completa de l'alumne. "Com ho anomenen en altres llengues?" obre la perspectiva conceptual i mostra la diversitat com a riquesa, no com a deficit.
- *Aprofundiment ≠ mes del mateix*: 3 preguntes literals de comprensió adicionals NO son aprofundiment. L'aprofundiment exigeix un salt qualitatiu en el nivell de pensament, no quantitatiu en el volum de preguntes.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **activitats d'aprofundiment que es generen per a l'alumne** (contingut post-lectura). **No descriu la producció autònoma de l'alumne ni l'avaluació del docent**: el docent observa si l'alumne completa l'activitat i si la seva resposta demostra aprofundiment real.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → activitats totalment físiques i manipulatives (ordenar, tocar, dramatitzar). `fase_lectora: alfabetica_emergent` → activitats físiques + dibuix + 1-2 paraules escrites.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Nombre i tipologia**
- Quantitat i varietat: 1-2 activitats físiques o manipulatives. Una sola consigna visual.

**2. Nivell cognitiu (Bloom)**
- Profunditat de pensament: Manipulatiu: ordenar, tocar, moure, dramatitzar, dibuixar. No requereix abstracció lingüística.

**3. Format de consigna**
- Producte esperat explícit: Indicació física i visual: "Ordena les imatges de [X] a [Y]." Producte: dibuix, ordenació, dramatització. Cap escriptura autònoma.

**4. Dimensió plurilingüe**
- Ús de L1 com a recurs: No generar.

**5. Autoavaluació mediada**
- Metacognició: "He ordenat les imatges / he dibuixat." (oral, mediat per adult)

### A1 — Inicial


**1. Nombre i tipologia**
- Quantitat i varietat: 2 activitats concretes i visuals. Evitar debats abstractes.

**2. Nivell cognitiu (Bloom)**
- Profunditat de pensament: Concret i visual. Màxim ancoratge en objectes o experiències familiars. Comparació simple.

**3. Format de consigna**
- Producte esperat explícit: Consigna molt concreta. Producte clar i assolible: 1 dibuix, 1 frase, 1 llista de 3 ítems.

**4. Dimensió plurilingüe**
- Ús de L1 com a recurs: No generar.

**5. Autoavaluació mediada**
- Metacognició: "He fet l'activitat. He escrit [producte]."

### A2 — Funcional


**1. Nombre i tipologia**
- Quantitat i varietat: 2-3 activitats. Combinació de connexió i "i si...?".

**2. Nivell cognitiu (Bloom)**
- Profunditat de pensament: Comparable i imaginatiu. "Com és X aquí vs. allà?" · "Qué passaria si...?".

**3. Format de consigna**
- Producte esperat explícit: Consigna accionable. Producte concret i delimitat: 1 fitxa, 1 mapa, 1 comparació de 3 elements.

**4. Dimensió plurilingüe**
- Ús de L1 com a recurs: Opcional: "Com es diu [terme clau] en altres llengues de l'aula? Comparteix-ho si vols." Cap exposició.

**5. Autoavaluació mediada**
- Metacognició: "He pensat més enllà del text. He fet la connexió o el 'i si...?'."

### B1 — Estratègic


**1. Nombre i tipologia**
- Quantitat i varietat: 2-3 activitats. Combinació de debat, connexió interdisciplinar i recerca guiada.

**2. Nivell cognitiu (Bloom)**
- Profunditat de pensament: Argumentatiu. Pren posicions i les justifica. Discrimina evidència de creença o opinió.

**3. Format de consigna**
- Producte esperat explícit: Consigna accionable amb producte i temps estimat (15-30 min): 1 argument escrit, 1 recerca a 2 fonts.

**4. Dimensió plurilingüe**
- Ús de L1 com a recurs: Opcional: comparació d'expressions o conceptes entre L1s dels alumnes si el text ho permet.

**5. Autoavaluació mediada**
- Metacognició: "He argumentat la meva postura i he usat evidència del text o d'una altra font."

### B2 — Acadèmic


**1. Nombre i tipologia**
- Quantitat i varietat: 2-3 activitats. Connexió entre matèries, contrast de fonts, intertextualitat.

**2. Nivell cognitiu (Bloom)**
- Profunditat de pensament: Analític. Contrastiu. Cerca relacions no evidents entre idees o camps disciplinars.

**3. Format de consigna**
- Producte esperat explícit: Consigna amb producte complex: argumentació de 2-3 paràgrafs, recerca comparada, informe breu.

**4. Dimensió plurilingüe**
- Ús de L1 com a recurs: Opcional: contrast d'equivalents culturals o termes tècnics entre les llengues que coneixes.

**5. Autoavaluació mediada**
- Metacognició: "He analitzat les relacions entre matèries i he contrastat informació de fonts diverses."

### C1+ — Crític


**1. Nombre i tipologia**
- Quantitat i varietat: 2-3 activitats. Reflexió crítica, hipòtesis contrafactuals, fonts contradictòries.

**2. Nivell cognitiu (Bloom)**
- Profunditat de pensament: Crític. Metacognitiu. Detecta biaixos, dilemes ètics, limitacions del coneixement i de les fonts.

**3. Format de consigna**
- Producte esperat explícit: Consigna oberta amb criteris de qualitat del producte. L'alumne decideix el format i justifica la tria.

**4. Dimensió plurilingüe**
- Ús de L1 com a recurs: Opcional: contrast metalingüístic i discursiu entre sistemes lingüístics i culturals.

**5. Autoavaluació mediada**
- Metacognició: "He detectat biaixos i limitacions del text. He qüestionat les afirmacions de l'autor amb arguments propis. He justificat la tria del format del meu producte segons l'objectiu de l'activitat."

