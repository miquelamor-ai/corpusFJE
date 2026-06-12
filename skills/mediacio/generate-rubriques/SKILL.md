---
name: generate-rubriques
description: 'Use when the teacher has activated the "rubriques" complement. Generates
  a student-facing achievement rubric (rúbrica d''assoliment) for the production task
  derived from the adapted text. The rubric uses the FJE 4-level scale (NA/AS/AN/AE)
  written in first person so the student can self-assess. Modulated by MECR level
  and genre/subject. At Emergent/pre-A1: checklist with icons instead of rubric table.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: rubriques
agent_role: complements
tools_required: []
triggers:
- path: params.complements.rubriques
  equals: true
moduls_relacionats:
- M2
- M6
font_canonic: M3_instrument-generar-rubriques.md
font_version: 4.0.0-canonic
generat_at: '2026-06-12'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 6923f54163438e53
---

# Generar rúbriques d'autoavaluació — skill operativa per a LLM

La rúbrica generada és **alumne-facing**: escrita en **primera persona**, per a l'alumne, amb l'escala FJE: **NA** (No Assolit) · **AS** (Assolit Suficient) · **AN** (Assolit Notable) · **AE** (Assolit Excel·lent). Quan l'alumne llegeix "He argumentat la meva postura amb 2 evidències del text", aprèn QUÈ s'espera d'ell ABANS d'escriure. La rúbrica és una **bastida d'anticipació** i una eina d'autoregulació, no un formulari d'avaluació del docent.

**Tipologia MALL**: Mediació (autoavaluació i metacognició).
**HCL principals**: Avaluar · Autoregular · Reflexionar metacognitivament.
**Principi rector — AE com a salt qualitatiu**: si el descriptor AE és "he fet molt bé el que es demanava", la rúbrica no discrimina el creixement real. AE ha de capturar alguna cosa que **sorprèn, va més lluny, demostra apropiació autèntica** del gènere o la tasca. AE no és "AN + esforç" — és un salt de naturalesa diferent.

**Escala FJE:**
- **NA** (No Assolit): no compleix el descriptor mínim de la tasca.
- **AS** (Assolit Suficient): compleix el descriptor bàsic. Producte correcte però sense matisos.
- **AN** (Assolit Notable): compleix el descriptor i afegeix qualitat. Producte coherent i elaborat.
- **AE** (Assolit Excel·lent): salt qualitatiu. Sorprèn, va més lluny, demostra apropiació autèntica. NO és "AN + molt d'esforç".

**Pre-A1 — Checklist binari d'icones (no escala FJE)**: a pre-A1 l'escala de 4 nivells és massa abstracta. El format és un **checklist ✅ / ❌**: "He dibuixat els 3 moments" → ✅ o ❌. No hi ha gradació: l'alumne o ho ha fet o no ho ha fet. L'adult media la revisió oral.

**Diferència crítica amb `bastides_produccio` (Bloc C — Pauta d'interrogació):**
- `bastides_produccio` Bloc C: pauta d'interrogació DURANT el procés d'escriptura (checklist intern que guia la producció en curs).
- `rubriques`: autoavaluació del PRODUCTE acabat (avaluació post-producció, escala FJE).
Les dues eines son complementàries: bastida durant → rúbrica després.

**Perspectiva alumne-facing:**
- Primera persona en TOT el document: "He escrit...", "He usat...", "He argumentat...".
- Mai tercera persona ("L'alumne ha escrit...") ni segona ("Has escrit...").
- Descriptors observables (l'alumne pot comprovar si ho ha fet): "He escrit la idea principal a la 1a frase" és observable. "He escrit bé" no és observable.

**Connexions MALL transversals:**
- *Rúbrica com a bastida d'anticipació*: quan l'alumne llegeix la rúbrica ABANS d'escriure, té un mapa de qualitat. La rúbrica no és per al docent — és una eina de l'alumne per autoregular la seva producció.
- *AE com a aspiració, no com a recompensa*: el descriptor AE mostra a l'alumne quin és el salt qualitatiu que podria fer si s'hi esforça. No és una recompensa al treball dur; és una descripció del pensament expert.
- *Metacognició com a aprenentatge*: el procés de marcar la rúbrica (decidir en quin nivell estàs) és en si mateix un acte de comprensió. L'alumne que se situa a AS i sap per qué (li falta evidència) aprèn més que l'alumne que se situa a AN sense saber-ne el motiu.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **rúbriques d'autoavaluació que es generen per a l'alumne** (AUTOAVALUACIÓ MEDIADA). **No descriu la rúbrica del docent per a l'avaluació sumativa**: la rúbrica d'autoavaluació és per a l'alumne, no per al docent. Si el docent vol rúbriques per avaluar (perspectiva externa), ha d'usar les eines d'avaluació de centre.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → checklist d'imatges (dibuix sí/no); `fase_lectora: alfabetica_emergent` → checklist de paraules curtes (sí/no).

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Format**
- Estructura de l'instrument: Checklist d'icones: ✅ / ❌ per a cada ítem. Sense escala. Molt visual. Adult media la revisió oral.

**2. Nombre de criteris**
- Amplitud d'avaluació: 2-3 criteris molt concrets i visuals. Accionables a pre-A1 (He dibuixat / He assenyalat).

**3. Descriptors observables**
- Concretesa del descriptor: Acció visible: "He dibuixat els 3 moments." / "He assenyalat el personatge." Mai "He fet bé".

**4. Primera persona**
- Perspectiva alumne-facing: "He fet ___ / He posat ___." Molt concret i físic.

**5. Descriptor AE (salt qualitatiu)**
- Naturalesa de l'excel·lència: Cap descriptor AE: checklist binari.

### A1 — Inicial


**1. Format**
- Estructura de l'instrument: Taula simplificada: 2-3 criteris × 3 nivells (Encara no / Sí / Sí, i alguna cosa més). Sense vocabulari FJE.

**2. Nombre de criteris**
- Amplitud d'avaluació: 2-3 criteris accionables. Corresponen a les tasques concretes demandades.

**3. Descriptors observables**
- Concretesa del descriptor: Observable: "He escrit 3 passos numerats." Sense adjectius valoratius.

**4. Primera persona**
- Perspectiva alumne-facing: "He escrit ___ / He usat ___." Primera persona consistent en tota la rúbrica.

**5. Descriptor AE (salt qualitatiu)**
- Naturalesa de l'excel·lència: Descriptor AE = precisió o originalitat dins del límit: "He triat una paraula que no estava a la bastida però que explica exactament el que volia dir." No "he afegit coses" ni "ho he fet molt bé".

### A2 — Funcional


**1. Format**
- Estructura de l'instrument: Taula: 3-4 criteris × escala FJE completa (NA/AS/AN/AE). Primera escala gradada.

**2. Nombre de criteris**
- Amplitud d'avaluació: 3-4 criteris del gènere o la tasca concreta.

**3. Descriptors observables**
- Concretesa del descriptor: Observable amb indicadors: "He escrit la idea principal a la 1a frase, sense 'Aquest text parla de…'."

**4. Primera persona**
- Perspectiva alumne-facing: "He escrit / He usat / He inclòs ___." Primera persona en tot el document.

**5. Descriptor AE (salt qualitatiu)**
- Naturalesa de l'excel·lència: Descriptor AE = qualitat que transforma: una imatge pròpia, un connector inesperat, un exemple original no donat a la bastida.

### B1 — Estratègic


**1. Format**
- Estructura de l'instrument: Taula: 4-5 criteris × escala FJE. Descriptor breu per a cada criteri i nivell.

**2. Nombre de criteris**
- Amplitud d'avaluació: 4-5 criteris que cobreixen les HCL clau de la tasca (Argumentar, Descriure, Narrar...).

**3. Descriptors observables**
- Concretesa del descriptor: Apunta a la qualitat: "Cada argument inclou una evidència del text o una raó concreta."

**4. Primera persona**
- Perspectiva alumne-facing: "He argumentat / He justificat / He demostrat ___." HCL en primera persona.

**5. Descriptor AE (salt qualitatiu)**
- Naturalesa de l'excel·lència: Descriptor AE = habilitat que anticipa el nivell següent: un argument no donat per la bastida, una connexió pròpia entre dues idees del text.

### B2 — Acadèmic


**1. Format**
- Estructura de l'instrument: Taula: 5-6 criteris × escala FJE + descriptor observatble per a cada criteri i nivell.

**2. Nombre de criteris**
- Amplitud d'avaluació: 5-6 criteris que inclouen dimensió formal (llengua) i dimensió de contingut (idees).

**3. Descriptors observables**
- Concretesa del descriptor: Apunta a la relació: "He connectat les idees de seccions diferents usant connectors precisos."

**4. Primera persona**
- Perspectiva alumne-facing: "He analitzat / He contrastat / He elaborat ___." HCL acadèmiques en 1a persona.

**5. Descriptor AE (salt qualitatiu)**
- Naturalesa de l'excel·lència: Descriptor AE = evidència de pensament crític: detectar un biaix, contrastar fonts, plantejar una objecció fonamentada.

### C1+ — Crític


**1. Format**
- Estructura de l'instrument: Taula: 5-6 criteris × escala FJE + reflexió metacognitiva final (1-2 frases lliures).

**2. Nombre de criteris**
- Amplitud d'avaluació: 5-6 criteris amb criteri de reflexió metacognitiva ("He revisat el text i he millorat ___").

**3. Descriptors observables**
- Concretesa del descriptor: Metacognitiu: "He detectat i corregit al menys un error de coherència o un terme imprecís."

**4. Primera persona**
- Perspectiva alumne-facing: "He reflexionat / He avaluat / He detectat ___." Metacognició en 1a persona.

**5. Descriptor AE (salt qualitatiu)**
- Naturalesa de l'excel·lència: Descriptor AE = reflexió que demostra metacognició genuïna i transferència a altres contexts o tasques.

