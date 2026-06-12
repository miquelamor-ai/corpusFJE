---
name: generate-cartes-conversacionals
description: 'Use when the teacher has activated the "cartes_conversacionals" complement.
  Generates role-based conversation cards for structured class discussion or debate:
  sentence starters per role (proposer, objector, mediator, summarizer) calibrated
  to MECR level. Designed for B1+ (secondary school). At A2: simplified pair-talk
  cards. At pre-A1/A1: not generated — oral interaction requires in-person scaffolding
  only.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: cartes_conversacionals
agent_role: complements
tools_required: []
triggers:
- path: params.complements.cartes_conversacionals
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-cartes-conversacionals.md
font_version: 4.0.0-canonic
generat_at: '2026-06-12'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: de9f447faf0ce158
---

# Generar cartes conversacionals — skill operativa per a LLM

Les cartes conversacionals bastiden la **participació oral** (o escrita en format debat) donant a cada alumne un **repertori d'iniciadors** associats al seu rol dins la conversa. Cada carta = 1 rol + descripció de la funció comunicativa + màxim 3 iniciadors. El rol allibera l'alumne de la por a "dir el que penso" — és el personatge qui argumenta, no ell. Especialment rellevant per a alumnat nouvingut o NESE amb baixa seguretat oral.

**Tipologia MALL**: Mediació (bastida de producció oral/dialogada).
**HCL principals**: Argumentar · Contrargumentar · Sintetitzar · Mediar.
**Principi rector**: Els iniciadors han de ser **específics de la pregunta de debat** del text. Si els iniciadors serveixen per a qualsevol debat de qualsevol tema, cal tornar a escriure'ls. La connexió amb el text font és la garantia de pertinença.

**2 tipus de conversa:**
- **Exploratòria** (A2-B1): posicions obertes, errors tolerats, raonament visible. L'objectiu és explorar conjuntament, no guanyar. Estil: "Jo penso que... però potser..." "I si...?".
- **Disputativa** (B2+): posicions definides, argumentació formal, citació d'evidències. L'objectiu és defensar una postura amb evidències. Estil: "Segons el text...", "D'acord amb...", "Però si observem que...".

**4 rols estàndard (B1+):**
- **Proposador/a**: formula la tesi i els arguments principals. Inicia la conversa.
- **Objector/a**: qüestiona la tesi. Planteja contraarguments i punts febles.
- **Mediador/a**: equilibra les posicions. Busca acord parcial i formula preguntes.
- **Sintetitzador/a**: tanca la ronda. Resumeix el que s'ha dit i formula l'element obert.

**Pre-A1/A1: NO generar.** La interacció oral a aquests nivells requereix suport docent directe en temps real (mediació de torn, reformulació, andamiatge). Les cartes conversacionals presuposen l'autonomia d'inici comunicatiu que s'assoleix a A2.

**Taulell de debat companion** (B1+): el MALL recomana combinar les cartes amb un taulell compartit (Arguments a favor / Arguments en contra / Punts d'acord / Preguntes obertes). Externalitza el raonament col·lectiu del grup.

**Connexions MALL transversals:**
- *Rol com a identitat comunicativa provisional*: el rol és una màscara pedagògica que permet a l'alumne experimentar posicions comunicatives que no necessàriament comparteix. L'Objector/a aprèn a contrargumentar; el Mediador/a aprèn a equilibrar. Aquesta experimentació de rols és la base del pensament dialèctic.
- *Iniciador com a frase de posada en marxa*: la por al silenci o al "no sé com dir-ho" és la barrera principal de la participació oral. Un iniciador concret ("Jo crec que... perquè...") desbloqueja el primer torn. Un cop l'alumne ha dit la primera frase, la conversa flueix.
- *Sintetitzador com a metacognició col·lectiva*: el rol del Sintetitzador és l'única funció metacognitiva del grup. "El que no hem resolt és ___" externalitza la consciència dels límits del coneixement col·lectiu. A C1, inclou la dimensió de fiabilitat de les fonts.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **cartes conversacionals que es generen per bastir el debat** (MEDIACIÓ DE LA PRODUCCIÓ ORAL). **No descriu l'avaluació del debat ni la qualitat de la participació de l'alumne**: el docent observa si l'alumne usa les cartes i si la conversa avança amb estructura.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Rols actius**
- Nombre i complexitat: NO generar.

**2. Nombre d'iniciadors per rol**
- Repertori lingüístic: NO generar.

**3. Tipus de conversa**
- Registre i objectiu: NO generar.

**4. Especificitat dels iniciadors**
- Connexió amb el text: NO generar.

**5. Element obert al Sintetitzador**
- Metareflexió del grup: NO generar.

### A1 — Inicial


**1. Rols actius**
- Nombre i complexitat: 2 rols: Proposador/a + Objector/a. Format simplificat per parelles.

**2. Nombre d'iniciadors per rol**
- Repertori lingüístic: 2 iniciadors per rol. Frases curtes i segures (Jo penso que ___ / Jo crec que no ___).

**3. Tipus de conversa**
- Registre i objectiu: Exploratòria: posicions obertes, errors tolerats, raonament visible. "I si...?" "Potser...".

**4. Especificitat dels iniciadors**
- Connexió amb el text: Iniciadors genèrics ("Jo penso que ___"). Curts i segurs. Fàcils de dir.

**5. Element obert al Sintetitzador**
- Metareflexió del grup: "Hem dit ___. Algú vol afegir alguna cosa?" (Element obert simple).

### A2 — Funcional


**1. Rols actius**
- Nombre i complexitat: 3-4 rols: Proposador + Objector + Mediador + Sintetitzador.

**2. Nombre d'iniciadors per rol**
- Repertori lingüístic: 3 iniciadors per rol. Frases completes adaptades a la HCL del rol (Argumentar, Contrargumentar, Mediar).

**3. Tipus de conversa**
- Registre i objectiu: Exploratòria o disputativa: comença explorant, pot formalitzar-se si el grup avança.

**4. Especificitat dels iniciadors**
- Connexió amb el text: Iniciadors específics de la pregunta de debat del text. Causals i justificatius ("El text diu que... i per això crec que...").

**5. Element obert al Sintetitzador**
- Metareflexió del grup: "La conclusió del grup és ___. El que no hem resolt és ___." (Tancament + obertura).

### B1 — Estratègic


**1. Rols actius**
- Nombre i complexitat: 4 rols complets amb registre formal i terminologia de debat.

**2. Nombre d'iniciadors per rol**
- Repertori lingüístic: 3 iniciadors amb vocabulari CALP i connectors argumentals (Malgrat que..., Tenint en compte que...).

**3. Tipus de conversa**
- Registre i objectiu: Disputativa: posicions definides, argumentació formal, citació d'evidències del text.

**4. Especificitat dels iniciadors**
- Connexió amb el text: Iniciadors que inclouen citació del text ("Segons el text...", "D'acord amb..."). Registre formal.

**5. Element obert al Sintetitzador**
- Metareflexió del grup: "El que no hem resolt és ___. Per resoldre-ho caldria saber ___." (Apertura epistemica).

### B2 — Acadèmic


**1. Rols actius**
- Nombre i complexitat: 4 rols + capa metacognitiva al Sintetitzador (detecció de biaixos i punts cecs).

**2. Nombre d'iniciadors per rol**
- Repertori lingüístic: 3 iniciadors dialèctics o retòrics que qüestionen la postura contrària (Si fos cert que X, llavors...).

**3. Tipus de conversa**
- Registre i objectiu: Disputativa amb metacognició: detecció de biaixos, qüestionament de la fiabilitat de les fonts.

**4. Especificitat dels iniciadors**
- Connexió amb el text: Iniciadors que qüestionen, matisen i detecten biaixos ("Però si pensem que X, el text podria estar ignorant...").

**5. Element obert al Sintetitzador**
- Metareflexió del grup: "El que queda obert és ___. Per respondre-ho, caldria contrastar amb ___ i revisar si els nostres arguments son fiables."

### C1+ — Crític


