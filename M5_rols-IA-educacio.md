---
title: "Els 7 rols de la IA en educació"
module: M5
id: M5_rols-IA-educacio
review_status: esborrany
version: "1.0"
sources:
  - docs/decisions/arquitectura-quest-rol-nivell.md
  - public/exemples-rols-mihia.md
  - docs/fonts/laia-knowledge/rols-interaccio-ia.md
connections:
  - M5_arquitectura-proposit-rol-nivell
  - M5_proposits-aprenentatge
  - M5_nivells-delegacio-mihia
  - M2_carrega-friccio-cognitiva
  - M5_disseny-instruccional-amb-IA
detection:
  - "Quan cal assignar un rol a la IA per a una activitat"
  - "Quan cal triar quin rol és compatible amb un propòsit d'aprenentatge o un nivell de delegació"
  - "Quan cal entendre per què un rol col·lapsa a certs nivells de delegació"
---

# Els 7 rols de la IA en educació

> Document de referència per als skills: Assignador de Rols IA, Generador d'Activitats, Dissenyador d'Assistents
> Substitueix: `rols-interaccio-ia.md` (versió LAIA)

---

## Contingut

### 1. Els 7 rols: adaptació Mollick per a l'àmbit escolar

| # | Rol | La IA actua com a... | Què fa | Quan usar-lo |
|---|---|---|---|---|
| 1 | **Mentor Socràtic** | Guia que pregunta | Fa preguntes per guiar el pensament, no dóna respostes directes | Pensament crític, ètica, debat, aprofundiment conceptual |
| 2 | **Simulador / Actor** | Personatge o escenari | Representa situacions, personatges o contextos amb què l'alumne interactua | Història, llengües, ciències socials, FP (simulació professional) |
| 3 | **Crític / Editor** | Revisor exigent | Avalua la feina de l'alumne, detecta errors i suggereix millores sense reescriure | Escriptura, projectes, codi, presentacions |
| 4 | **Generador de Casos** | Creador de material | Genera exemples, dades, problemes, casos o escenaris per analitzar | Ciències, matemàtiques, economia, laboratori, FP |
| 5 | **Teachable Agent** | "Alumne" que aprèn | L'alumne ensenya a la IA; la IA simula malentesos; l'alumne detecta els propis buits | Consolidació, autoavaluació, ciències, tècnica |
| 6 | **Contrincant** | Devil's Advocate | Contradiu l'alumne sistemàticament per obligar-lo a argumentar i defensar posicions | Debat, argumentació, pensament crític, anàlisi literària |
| 7 | **Traductor / Adaptador** | Personalitzador | Adapta contingut a nivells, llengües, formats o necessitats específiques | Inclusió, NEE, lectura fàcil, multilingüisme, vocabulari tècnic |

### 2. Les tres famílies de rols

L'anàlisi dels 21 exemples del document `exemples-rols-mihia.md` revela que els 7 rols es comporten diferentment segons el nivell de delegació. Aquesta diferència és estructural, no accidental:

#### Rols procesuals (N2-N3 nadiu, col·lapsen a N4)

**Rols**: Mentor Socràtic, Teachable Agent, Contrincant

**Per què col·lapsen a N4**: la seva essència és el **procés d'interacció** — l'alumne pensa, pregunta, defensa, ensenya. A N4, la IA genera el diàleg complet i el rol perd la seva raó de ser: l'alumne ja no pensa, llegeix un producte.

**Implicació operativa**: aquests rols no haurien d'usar-se a N4 llevat que l'objectiu explícit sigui aprendre enginyeria de prompts, no el contingut del domini.

**Indicador de fricció**: indueixen principalment **Resistència** (l'alumne defensa posicions) i **Descoberta** (l'alumne veu buits que no veia).

#### Rols mixtos (N2-N4 viable)

**Rols**: Crític / Editor, Simulador

**Per què funcionen a N4**: poden operar tant en iteració (N2-N3, l'alumne revisa i millora) com en generació completa (N4, l'alumne rep un producte per avaluar). El canvi de nivell no destrueix l'essència del rol, sinó que canvia el tipus d'activitat cognitiva.

**Indicador de fricció**: indueixen principalment **Recursivitat** (iteració fins estabilitzar) i **Descoberta** (veure el que no es veia).

#### Rols productius (N3-N4 nadiu, N2 queda limitat)

**Rols**: Generador de Casos, Traductor / Adaptador

**Per què N4 és l'hàbitat natural**: la seva naturalesa és **produir** — material, adaptacions, traduccions. La fricció productiva es trasllada al moment en què l'alumne **treballa amb** el producte generat, no a la interacció amb la IA mateixa.

**Indicador de fricció**: la fricció no resideix en la interacció amb la IA, sinó en l'activitat posterior (anàlisi dels casos generats, verificació de l'adaptació).

### 3. Comportament dels rols per nivell de delegació

| Rol | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| **Mentor Socràtic** | — | Context | **Ús nadiu** | **Ús nadiu** | ⚠️ Col·lapse | Meta-disseny |
| **Simulador** | — | Context | **Ús nadiu** | **Ús nadiu** | Viable amb risc | Meta-disseny |
| **Crític / Editor** | — | Context | **Ús nadiu** | **Ús nadiu** | Viable | Meta-disseny |
| **Generador de Casos** | — | Context | Limitat | **Ús nadiu** | **Ús nadiu** | Meta-disseny |
| **Teachable Agent** | — | Context | **Ús nadiu** | **Ús nadiu** | ⚠️ Col·lapse | Meta-disseny |
| **Contrincant** | — | Context | **Ús nadiu** | **Ús nadiu** | ⚠️ Col·lapse | Meta-disseny |
| **Traductor / Adaptador** | — | Context | Limitat | **Ús nadiu** | **Ús nadiu** | Meta-disseny |

**Llegenda**:
- **Ús nadiu**: el rol funciona amb sentit pedagògic ple a aquest nivell
- **Viable**: funciona però amb canvi de tipus d'activitat cognitiva
- ⚠️ **Col·lapse**: el rol perd l'essència; l'alumne ja no pensa, llegeix
- **Limitat**: la naturalesa productiva del rol no s'aprofita plenament
- **Context**: la IA proporciona informació, no encarna el rol
- **Meta-disseny**: l'alumne dissenya el sistema (N5 = alfabetització IA, no contingut)

### 4. Regles d'assignació de rols

1. **Dir "Usa la IA com a [Rol]"**, mai "usa ChatGPT". El rol defineix el comportament esperat.
2. **El rol determina el prompt**: un Mentor Socràtic requereix un prompt diferent d'un Generador de Casos. El prompt ha de codificar el comportament del rol.
3. **El rol ha de ser coherent amb el nivell MIHIA**: un Teachable Agent implica N1-N3, mai N4. Un Generador de Casos pot ser N3-N4.
4. **Es poden seqüenciar rols** dins d'una mateixa activitat: Fase 1 (Generador → material) → Fase 2 (Mentor Socràtic → anàlisi) → Fase 3 (Crític → refinament).
5. **Verificar la família del rol** abans d'assignar un nivell: si és un rol procesual, N4 col·lapsa el sentit pedagògic.

### 5. Matriu Rol × Moviment de Fricció

| Rol | Descoberta | Recursivitat | Resistència |
|---|---|---|---|
| Mentor Socràtic | ★★ | ★ | ★★ |
| Simulador | ★★ | ★★ | ★ |
| Crític / Editor | ★ | ★★ | ★ |
| Generador de Casos | ★★ | ★ | — |
| Teachable Agent | ★★ | ★ | ★★ |
| Contrincant | ★ | ★★ | ★★ |
| Traductor / Adaptador | ★ | ★ | — |

★★ = moviment principal, ★ = moviment secundari, — = no induït típicament.

### 6. Recomanacions per etapa

| Etapa | Nivells MIHIA predominants | Rols prioritaris |
|---|---|---|
| **ESO 1r cicle** (12-14) | N0-N2 | Mentor Socràtic, Teachable Agent, Crític |
| **ESO 2n cicle** (14-16) | N1-N3 | Tots, èmfasi en Crític i Simulador |
| **Batxillerat** (16-18) | N1-N4 segons objectiu | Contrincant, Generador de Casos, Cocreació |
| **FP Grau Mitjà** | N1-N4 contextual | Simulador, Adaptador, Generador (cas tècnic) |
| **FP Grau Superior** | N2-N5 segons mòdul | Tots, incloent disseny d'agents (N5) |

### 7. Guia ràpida: quin rol per a quin objectiu?

| Si l'objectiu és... | Rol recomanat | Per què |
|---|---|---|
| Aprofundir en un concepte | Mentor Socràtic | Guia sense donar respostes; indueix Descoberta |
| Practicar una situació real | Simulador | Context segur per experimentar; indueix Recursivitat |
| Millorar un treball propi | Crític / Editor | Feedback específic sense reescriure; indueix Recursivitat |
| Analitzar dades o casos | Generador de Casos | Material fresc i divers per a anàlisi autònoma |
| Consolidar aprenentatge | Teachable Agent | Ensenyar = aprendre millor; indueix Resistència + Descoberta |
| Argumentar i defensar | Contrincant | Obliga a justificar posicions; indueix Resistència |
| Adaptar a necessitats | Traductor / Adaptador | Personalització (NEE, llengües, nivells) |

---

## Connexions

| Document | Relació |
|---|---|
| `M5_arquitectura-proposit-rol-nivell` | Els rols són la **capa d'implementació** dins l'arquitectura P>R>N |
| `M5_proposits-aprenentatge` | La matriu Propòsit × Rol determina quins rols serveixen cada propòsit d'aprenentatge |
| `M5_nivells-delegacio-mihia` | El rang de nivells nadius de cada rol i el col·lapse a N4 dels procesuals |
| `M2_carrega-friccio-cognitiva` | Les 3 famílies deriven de l'anàlisi de quina càrrega externalitzen i quina fricció generen |
| `exemples-rols-mihia.md` | 21 exemples concrets (7 rols × 3 etapes × 6 nivells), cadascun amb propòsit d'aprenentatge assignat |

> **Decisió Xat 6 (abril 2026):** es mantenen els 7 rols originals (Mollick). Les 3 famílies (procesuals, mixtos, productius) donen prou estructura. Cap fusió ni eliminació.

---

## Detecció

Activar aquest document quan:

- Cal **triar quin rol** assignar a la IA per a una activitat
- Cal entendre per què un **rol procesual no funciona a N4**
- Cal **seqüenciar rols** dins d'una activitat o tasca complexa
- Cal verificar la **coherència entre rol i nivell MIHIA**
- Cal **dissenyar un assistent institucional** alineat amb rols explícits (Criteri E d'assistents)
- Cal escriure un **prompt pedagògic** que codifiqui el comportament d'un rol

---

*Versió 1.0 · Esborrany · Jesuïtes Educació Catalunya · 2026*
