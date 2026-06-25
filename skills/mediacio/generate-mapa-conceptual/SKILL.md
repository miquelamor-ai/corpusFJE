---
name: generate-mapa-conceptual
description: 'Use when the teacher has activated the "mapa_conceptual" complement.
  Generates a visual organiser adapted to MECR level: at pre-A1/A1 a simple visual
  schema (2-4 nodes, image→word or parts of a whole); from A2 a hierarchical concept
  map in structured markdown (central concept + branches + sub-elements). Output is
  NOT ASCII-art. Can be copy-pasted into Canva, MindMeister, XMind, Word SmartArt.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.2.0-canonic
complement_key: mapa_conceptual
agent_role: complements
tools_required: []
triggers:
- path: params.complements.mapa_conceptual
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-mapa-conceptual.md
font_version: 4.2.0-canonic
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: d6eaedbfe6bfbf82
---

# Generar mapa conceptual — skill operativa per a LLM

El mapa conceptual és un **organitzador visual** que externalitza les relacions entre conceptes del text adaptat. El MALL distingeix tres eines progressives dins d'aquest instrument: l'**esquema visual** (funció executiva, pre-A1/A1: ordena seqüències o parts d'un tot), el **mapa conceptual jeràrquic** (funció epistèmica, A2+: reconstrueix el coneixement en categories i relacions lògiques) i el **mapa de contrast** (funció crítica, C1: compara fonts o ideologies). La tria de l'eina depèn del MECR i de l'objectiu pedagògic.

**Tipologia MALL**: Mediació (organitzador visual cognitiu).
**HCL principals**: Recapitular/Organitzar (pre-A1/A1) · Categoritzar/Relacionar (A2-B1) · Contrastar/Analitzar (B2-C1).
**Principi rector**: La branca ha de dir la **relació**, no el contingut. La forma d'expressar la relació es **gradua pel MECR**: a **A2** és un **nom de categoria** ("Causes", "Conseqüències", "Tipus de", "Processos") com a bastida classificatòria; a **B1+** és un **verb o frase d'enllaç** de relació bàsica ("provoca", "es divideix en", "forma part de") que fa la proposició Novak llegible (concepte → enllaç → concepte); els connectors de matís/concessió/contrast ("en canvi", "tanmateix", "contrasta amb") es reserven a B2/C1. Si la branca s'anomena "Informació" o "Coses", no és un mapa conceptual — és una llista disfressada, a qualsevol nivell.
**Format obligatori**: Markdown jeràrquic (exportable a MindMeister/Canva/XMind). **Cap ASCII-art** (caixes │ ├ └ → fletxes).

**Distinció fonamental — 3 eines dins un instrument:**
- **Esquema visual** (pre-A1/A1): "Llegir per orientar-se". Seqüències temporals (antes/durant/après) o parts d'un tot (cap, cos, cua). El pas d'un node és immediat: imatge → paraula. No hi ha jerarquia lògica: és una cadena o un diagrama d'elements.
- **Mapa conceptual** (A2-B2, Novak): "Llegir per comprendre". Jerarquia etiquetada: concepte central → branques → detalls. Les branques expressen relacions lògiques, **graduades pel MECR**: a A2 com a **noms de categoria** (causes, efectes, tipus, processos); a B1+ com a **verbs d'enllaç** de relació bàsica (provoca, es divideix en), que reconstrueixen la proposició Novak. El contingut prové del text adaptat.
- **Mapa de contrast** (C1): "Llegir per avaluar". Dues columnes o dues branques en contraposició. El contingut compara dues fonts, dues ideologies o dos marcs interpretatius.

**Distinció crítica amb `generate-mapa-mental` (instrument separat):**
- `mapa_conceptual` (Novak): "Llegir per comprendre" — contingut **dintre del text** adaptat; estructura jeràrquica; relacions etiquetades; A2-C1.
- `mapa_mental` (Buzan, B1+): "Llegir per connectar" — contingut **més lluny del text**; radial i divergent; lliure; preguntes generadores; per a alumnat amb AACC o exploració creativa.
Quan l'objectiu és comprendre el text → `mapa_conceptual`. Quan l'objectiu és expandir i connectar → `mapa_mental`.

**Mapa com a bastida de composició**: l'alumne que fa el mapa conceptual ABANS d'escriure té ja l'estructura del text. El mapa és la planificació cognitiva que precedeix la producció textual. Per a TILC, el mapa conceptual és alhora instrument de comprensió i esquelet del text expositiu.

**Pre-A1 SÍ (D6)**: l'esquema visual a pre-A1 no demana abstracció ni relacions lògiques. "Ordena les parts" o "Quins moments té?" son operacions cognitives assolibles des de la fase logogràfica, amb imatges com a suport.

**Connexions MALL transversals:**
- *Esquema vs. mapa com a distinció cognitiva*: el pas d'esquema (ordena) a mapa (categoritza i relaciona) no és cosmètic — és cognitiu. Introduir el mapa conceptual a A2 és introduir el pensament categorial: la capacitat de nomenar categories i les relacions entre elles.
- *Noms de branca com a comprensió*: si l'alumne no pot nomenar la relació de la branca (la categoria a A2, "Causes"/"Efectes"; el verb d'enllaç a B1+, "provoca"/"es divideix en"), no ha comprès l'estructura. El nom de branca és la prova de comprensió, no el contingut de la branca.
- *Mapa com a metacognició*: construir el mapa DESPRÉS de llegir és diferent que llegir el mapa construït per un altre. La construcció activa (l'alumne organitza) desenvolupa comprensió profunda; la lectura passiva d'un mapa donat desenvolupa reconeixement.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **mapa conceptual / esquema visual que es genera com a organitzador del text adaptat** (COMPRENSIÓ ESTRUCTURADA). **No descriu la producció creativa de l'alumne**: el mapa es genera a partir del text adaptat; l'alumne el llegeix, l'usa com a bastida de comprensió i en pot fer un de propi com a activitat posterior.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → esquema de 2 imatges (imatge → paraula); `fase_lectora: alfabetica_emergent` → esquema de 2-3 nodes amb paraula curta.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Tipus d'eina**
- Funció cognitiva: Esquema visual: 2-3 nodes. Imatge → paraula o seqüència temporal (antes/durant/après).

**2. Concepte central**
- Nucli del mapa: Nom d'un personatge o objecte familiar del text. 1-2 paraules.

**3. Branques principals**
- Relació de branca (graduada MECR): 1-2 elements: parts o qualitats d'un tot. Noms simples i concrets (cap, pit, cua).

**4. Sub-elements**
- Detalls de les branques: Cap sub-element: l'esquema és pla (massa nivells per a pre-A1).

**5. Format de sortida**
- Estructura markdown: `## Esquema visual` + llista plana sense sangria. 2-3 ítems màxim.

**6. Enllaços creuats (Novak)**
- Nombre recomanat: 0 enllaços creuats. L'esquema visual és pla, sense relacions transversals.

### A1 — Inicial


**1. Tipus d'eina**
- Funció cognitiva: Esquema visual: 3-4 nodes. Parts d'un tot o qualitats simples d'un element concret.

**2. Concepte central**
- Nucli del mapa: 1 terme nuclear concret del text adaptat. En negreta.

**3. Branques principals**
- Relació de branca (graduada MECR): 2-3 branques concretes. Noms simples. Pot ser seqüència temporal (1r, 2n, 3r).

**4. Sub-elements**
- Detalls de les branques: Cap sub-element: l'esquema és pla (màxim 1 nivell).

**5. Format de sortida**
- Estructura markdown: `## Esquema visual` + llista amb sangria màxima 1 nivell. Cap ASCII-art.

**6. Enllaços creuats (Novak)**
- Nombre recomanat: 0 enllaços creuats. L'esquema visual és pla.

### A2 — Funcional


**1. Tipus d'eina**
- Funció cognitiva: Mapa conceptual: 2 nivells jeràrquics. Primera introducció guiada de branques etiquetades.

**2. Concepte central**
- Nucli del mapa: 1 terme nuclear precís del text adaptat. En negreta. Correspon a la idea central del text.

**3. Branques principals**
- Relació de branca (graduada MECR): 3-4 branques amb **nom de categoria** (Causes / Tipus / Efectes / Processos). Bastida classificatòria. Mai genèrics.

**4. Sub-elements**
- Detalls de les branques: 2-3 sub-elements per branca. Termes curts, no frases llargues. Del text adaptat.

**5. Format de sortida**
- Estructura markdown: `## Mapa conceptual` + 2 nivells de sangria. Branques en negreta. Cap ASCII-art.

**6. Enllaços creuats (Novak)**
- Nombre recomanat: 0 enllaços creuats. Primer mapa jeràrquic: el focus és nomenar categories, encara no creuar branques.

### B1 — Estratègic


**1. Tipus d'eina**
- Funció cognitiva: Mapa conceptual: 3 nivells. Concepte → categories disciplinars → detalls inferts del text.

**2. Concepte central**
- Nucli del mapa: 1 terme que organitza tot el coneixement del text. Terme disciplinar.

**3. Branques principals**
- Relació de branca (graduada MECR): 3-5 branques amb **verb d'enllaç de relació bàsica**: causa/conseqüència (provoca, és provocat per) o part/tot (es divideix en, forma part de). Proposició Novak llegible. **Sense connectors de matís/concessió/contrast.** Mai genèrics.

**4. Sub-elements**
- Detalls de les branques: 3-4 sub-elements per branca. Inferts del text, no copiats literalment.

**5. Format de sortida**
- Estructura markdown: `## Mapa conceptual` + 3 nivells de sangria. Branques en negreta. Cap ASCII-art.

**6. Enllaços creuats (Novak)**
- Nombre recomanat: 0-1 enllaços creuats. Opcional, només si hi ha una relació transversal evident entre dues branques.

### B2 — Acadèmic


**1. Tipus d'eina**
- Funció cognitiva: Mapa conceptual: 4 nivells màxim. Superestructura del gènere amb lèxic CALP.

**2. Concepte central**
- Nucli del mapa: 1 terme nuclear CALP. Pot ser un procés, un fenomen o un concepte abstracte.

**3. Branques principals**
- Relació de branca (graduada MECR): 4-6 branques amb **verb d'enllaç CALP**; s'hi afegeixen matís/concessió/condició (en canvi, a diferència de, depèn de, determina, condiciona). Reflecteixen l'estructura del gènere.

**4. Sub-elements**
- Detalls de les branques: Sub-elements amb matisos. Pot incloure relacions transversals entre branques.

**5. Format de sortida**
- Estructura markdown: `## Mapa conceptual` + 4 nivells màxim. Branques CALP en negreta. Cap ASCII-art.

**6. Enllaços creuats (Novak)**
- Nombre recomanat: 1-2 enllaços creuats. S'introdueixen explícitament per mostrar relacions entre branques diferents.

### C1+ — Crític


**1. Tipus d'eina**
- Funció cognitiva: Mapa de contrast: 2 columnes o branques en contraposició. Comparació de fonts o ideologies.

**2. Concepte central**
- Nucli del mapa: 2 termes en contrast o 1 concepte complex amb múltiples dimensions o perspectives.

**3. Branques principals**
- Relació de branca (graduada MECR): 2 columnes de contrast o 4-6 branques amb verb/connector de tensió explícita (contrasta amb, s'oposa a, tanmateix, mentre que).

**4. Sub-elements**
- Detalls de les branques: Sub-elements de contrast, evidències o cites de fonts. Pot incloure tensions entre branques.

**5. Format de sortida**
- Estructura markdown: `## Mapa de contrast` + 2 columnes (taula markdown) o mapa amb branques de contrast.

**6. Enllaços creuats (Novak)**
- Nombre recomanat: 2-3 enllaços creuats. Pocs però d'alt valor: mostren integració i tensions entre branques (Novak: el tret de pensament creatiu).

