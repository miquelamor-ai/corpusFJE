---
modul: M5
titol: "Catàleg: 7 rols de la IA en educació"
tipus: cataleg
descripcio: "Inventari dels 7 rols que pot adoptar la IA en activitats educatives (adaptació Mollick per a l'àmbit escolar), amb fitxa per rol, família d'ús (procesual/mixt/productiu), rang de delegació MIHIA nadiu i guia de selecció"
review_status: esborrany
generat_at: 2026-05-10T00:00:00
paraules_clau: ["rols IA", "Mollick", "Mentor Socràtic", "Simulador", "Teachable Agent", "Contrincant", "disseny instruccional", "MIHIA"]
---

## Què és aquest catàleg

Inventari dels **7 rols** que pot adoptar la IA en activitats educatives, basat en l'adaptació de Mollick per a l'àmbit escolar (Jesuïtes Educació, 2026). Un **rol** defineix el comportament que la IA ha d'adoptar en una interacció concreta — no la tecnologia utilitzada, ni el nivell de delegació, sinó la **funció pedagògica** que compleix.

El catàleg és consumit principalment per docents que dissenyen activitats i han de triar quin rol assignar a la IA, i per equips que dissenyen assistents institucionals i han de codificar un comportament de rol en el prompt de sistema.

**Relació amb el disseny instruccional:** la tria de rol és el segon pas de l'arquitectura P>R>N, **posterior al propòsit d'aprenentatge** i previ a la tria del nivell MIHIA. El rol no es tria per la seva popularitat o comoditat, sinó perquè serveix el propòsit d'aprenentatge escollit. La instrucció operativa és: **dir "Usa la IA com a [Rol]", mai "usa ChatGPT"**. El rol defineix el comportament esperat; el prompt ha de codificar-lo.

## Criteris d'inclusió

Els 7 rols provenen de la classificació de Mollick, adaptada a l'àmbit escolar (Jesuïtes Educació, 2026).

**Criteris de manteniment del catàleg:**
- S'inclou un rol si defineix un comportament de la IA **diferenciable i pedagògicament justificable** que no es redueix a cap altre rol de la llista.
- No s'inclouen rols purament tècnics (p. ex. "assistent de codi") sense funció d'aprenentatge pròpia.
- La cardinalitat és **7**. La decisió de no fusionar ni eliminar cap rol va ser explícita (Xat 6, abril 2026): les 3 famílies estructurals (procesuals, mixtos, productius) donen prou organització sense reduir la granularitat.

**Font canònica:** `M5_arquitectura-proposit-rol-nivell` + `exemples-rols-mihia.md` (21 exemples transversals: 7 rols × 3 etapes).

## Inventari

Els rols s'organitzen en **tres famílies** segons el rang de delegació MIHIA on funcionen de manera natural i el tipus de fricció cognitiva que indueixen.

| Família | Rols | Rang nadiu | Comportament a N4 |
|---|---|---|---|
| **A — Procesual** | Mentor Socràtic, Teachable Agent, Contrincant | N2–N3 | ⚠️ Col·lapsen: l'alumne llegeix en comptes de pensar |
| **B — Mixt** | Crític/Editor, Simulador | N2–N4 | Viable: canvia el tipus d'activitat cognitiva |
| **C — Productiu** | Generador de Casos, Traductor/Adaptador | N3–N4 | Nadiu: la fricció resideix en l'activitat posterior |

---

### Mentor Socràtic

**Resum (1 línia):** La IA guia el pensament de l'alumne fent preguntes, sense donar mai respostes directes.
**Quan aplica:** Pensament crític, discussió ètica, debat, aprofundiment conceptual.
**Característiques:** Família A (procesual). Indueix Descoberta ★★ i Resistència ★★. La IA mai pren posició: sempre pregunta ("Per què creus que...?", "Quina evidència tens?").
**Exemple:** ESO 2n cicle — debat sobre un dilema ètic de la IA; la IA desafia cada argument de l'alumne amb una nova pregunta fins que l'alumne ha de reconstruir la posició.
**Conflictes/incompatibilitats:** Col·lapsa a N4: si la IA genera el diàleg complet, el rol perd el sentit pedagògic. No usar a N4 llevat que l'objectiu explícit sigui aprendre enginyeria de prompts, no el contingut del domini.

---

### Simulador / Actor

**Resum (1 línia):** La IA representa un personatge, rol professional o escenari amb què l'alumne interactua de manera realista.
**Quan aplica:** Història, llengües, ciències socials, FP (simulació professional), jocs de rol amb finalitat d'aprenentatge.
**Característiques:** Família B (mixt). Indueix Descoberta ★★ i Recursivitat ★★. Funciona tant en iteració (N2–N3) com en generació completa (N4) sense destruir l'essència del rol.
**Exemple:** FP Grau Superior — la IA simula un client insatisfet en una atenció al públic; l'alumne ha de gestionar la situació professional en temps real, amb el docent observant.
**Conflictes/incompatibilitats:** A N4 canvia el tipus d'activitat cognitiva: l'alumne avalua el producte de la simulació en comptes de viure-la. Cal explicitar al prompt el nivell de realisme i les restriccions del personatge.

---

### Crític / Editor

**Resum (1 línia):** La IA avalua la feina de l'alumne, detecta errors i suggereix millores, sense reescriure per l'alumne.
**Quan aplica:** Escriptura, projectes, codi, presentacions — qualsevol producció on cal retroalimentació específica i exigent.
**Característiques:** Família B (mixt). Indueix principalment Recursivitat ★★. La restricció clau és "suggerir sense reescriure": si la IA reescriu, el rol es degrada a Generador i l'alumne perd l'autoria.
**Exemple:** Batxillerat — l'alumne entrega un esborrany d'assaig filosòfic; la IA assenyala incoherències lògiques i preguntes sense respondre, però no escriu cap frase nova.
**Conflictes/incompatibilitats:** Cal formular el prompt de manera que prohibeixi explícitament la reescriptura. Funciona a N2–N4 però el valor pedagògic màxim és a N2–N3.

---

### Generador de Casos

**Resum (1 línia):** La IA crea exemples, dades, problemes o escenaris nous per analitzar o resoldre.
**Quan aplica:** Ciències, matemàtiques, economia, laboratori, FP — quan cal material fresc i divers per a anàlisi autònoma de l'alumne.
**Característiques:** Família C (productiu). N3–N4 nadiu. La fricció productiva no resideix en la interacció amb la IA sinó en l'activitat posterior (anàlisi dels casos generats). A N2 queda limitat: no s'aprofita la naturalesa productiva del rol.
**Exemple:** ESO Ciències — la IA genera 5 casos de contaminació de sòls amb dades variades i context diferent; l'alumne analitza, compara i extreu conclusions per compte seu.
**Conflictes/incompatibilitats:** No usar quan el procés de generació de casos és en si mateix l'objectiu d'aprenentatge; en aquest cas, l'alumne hauria de generar-los.

---

### Teachable Agent

**Resum (1 línia):** La IA simula ser un "alumne" que aprèn: l'alumne li explica conceptes, la IA simula malentesos, l'alumne detecta els seus propis buits.
**Quan aplica:** Consolidació d'aprenentatge, autoavaluació, comprensió conceptual profunda — especialment ciències i tècnica.
**Característiques:** Família A (procesual). Indueix Descoberta ★★ i Resistència ★★. El mecanisme *learning by teaching* és molt efectiu: ensenyar obliga a estructurar i a detectar llacunes que la simple lectura amaga.
**Exemple:** Primària Superior (guiat, N1) — l'alumne explica el cicle de l'aigua a la IA-alumne; la IA pregunta "però llavors on va l'aigua quan s'evapora?", forçant l'alumne a aprofundir.
**Conflictes/incompatibilitats:** Col·lapsa a N4. Requereix un disseny de prompt acurat perquè la IA mantingui el rol d'"alumne confós" sense derrapar cap a "professor que explica".

---

### Contrincant

**Resum (1 línia):** La IA contradiu sistemàticament l'alumne (*devil's advocate*) per obligar-lo a argumentar i defensar les seves posicions.
**Quan aplica:** Debat, argumentació, pensament crític, anàlisi literària, dilemes ètics — quan l'objectiu és que l'alumne construeixi arguments sòlids sota pressió.
**Característiques:** Família A (procesual). Indueix Resistència ★★ (principal) i Recursivitat ★★. Similar al Mentor Socràtic però actiu: no pregunta, contraataca amb arguments.
**Exemple:** ESO 4t — l'alumne defensa una posició sobre una qüestió d'actualitat; la IA presenta contra-arguments de complexitat progressiva fins que l'alumne ha de revisar o enfortir la seva postura.
**Conflictes/incompatibilitats:** Col·lapsa a N4. Pot ser frustrant per a alumnes amb baixa autoeficàcia; el docent ha d'assegurar-se que el nivell de resistència és desafiador però no bloquejant.

---

### Traductor / Adaptador

**Resum (1 línia):** La IA adapta contingut a nivells, llengües, formats o necessitats específiques de l'alumne o el context.
**Quan aplica:** Inclusió, NEE, lectura fàcil, multilingüisme, adaptació de vocabulari tècnic, diferenciació curricular.
**Característiques:** Família C (productiu). N3–N4 nadiu. La fricció productiva resideix en l'activitat posterior: l'alumne treballa amb el contingut adaptat, no en la interacció amb la IA. A N2 queda limitat.
**Exemple:** M3 — la IA adapta un text científic a lectura fàcil per a alumnat amb dificultats de comprensió lectora; el docent verifica la precisió de l'adaptació i l'alumne el llegeix i respon preguntes de comprensió.
**Conflictes/incompatibilitats:** Cal especificar clarament el perfil d'adaptació al prompt (nivell, necessitat, format); una instrucció vaga genera adaptacions genèriques ineficaces.

---

## Com triar entre les opcions

**Pas 1 — Propòsit-first.** La pregunta no és "quin rol vull usar?" sinó "quin rol serveix millor el propòsit d'aprenentatge que he definit?". El propòsit determina el rol, mai a l'inrevés.

**Pas 2 — Verificar la família.** Un rol procesual (Mentor Socràtic, Teachable Agent, Contrincant) no funciona a N4: col·lapsa. Si el nivell de delegació que necessites és N4, tria un rol productiu o mixt.

**Pas 3 — Guia ràpida per objectiu:**

| Si l'objectiu és... | Rol recomanat | Família |
|---|---|---|
| Aprofundir en un concepte | Mentor Socràtic | Procesual |
| Practicar una situació real | Simulador | Mixt |
| Millorar un treball propi | Crític / Editor | Mixt |
| Analitzar dades o casos | Generador de Casos | Productiu |
| Consolidar aprenentatge | Teachable Agent | Procesual |
| Argumentar i defensar | Contrincant | Procesual |
| Adaptar a necessitats | Traductor / Adaptador | Productiu |

**Pas 4 — Seqüenciar rols.** Es poden combinar rols dins una mateixa activitat: Fase 1 (Generador → material) → Fase 2 (Mentor Socràtic → anàlisi) → Fase 3 (Crític → refinament).

**Per etapa educativa:**

| Etapa | Nivells MIHIA predominants | Rols prioritaris |
|---|---|---|
| ESO 1r cicle (12–14) | N0–N2 | Mentor Socràtic, Teachable Agent, Crític |
| ESO 2n cicle (14–16) | N1–N3 | Tots, èmfasi en Crític i Simulador |
| Batxillerat (16–18) | N1–N4 | Contrincant, Generador de Casos, Cocreació |
| FP Grau Mitjà | N1–N4 contextual | Simulador, Adaptador, Generador (cas tècnic) |
| FP Grau Superior | N2–N5 | Tots, incloent disseny d'agents (N5) |

## Relació amb altres catàlegs

Aquest catàleg forma part del **sistema P>R>N** (Propòsit–Rol–Nivell), el marc arquitectònic de disseny d'activitats amb IA de Jesuïtes Educació:

| Catàleg del sistema | Pregunta que respon | Relació amb aquest |
|---|---|---|
| `M5_proposits-aprenentatge` | Què ha d'aprendre l'alumne cognitivament? | El propòsit determina quin rol triar (sempre Propòsit-first) |
| `M5_rols-IA-educacio` | **Com ha d'actuar la IA?** | **Aquest catàleg** |
| `M5_nivells-delegacio-mihia` | Quanta autonomia cedeix l'alumne a la màquina? | El rang nadiu de cada rol condiciona quins nivells MIHIA són compatibles |

La matriu Propòsit × Rol (quins rols serveixen cada propòsit d'aprenentatge) es troba a `M5_arquitectura-proposit-rol-nivell`, que és la clau de volta del sistema.

**Matriu Rol × Moviment de fricció** (resum orientatiu):

| Rol | Descoberta | Recursivitat | Resistència |
|---|---|---|---|
| Mentor Socràtic | ★★ | ★ | ★★ |
| Simulador | ★★ | ★★ | ★ |
| Crític / Editor | ★ | ★★ | ★ |
| Generador de Casos | ★★ | ★ | — |
| Teachable Agent | ★★ | ★ | ★★ |
| Contrincant | ★ | ★★ | ★★ |
| Traductor / Adaptador | ★ | ★ | — |

★★ = moviment principal · ★ = moviment secundari · — = no induït típicament

## 3. Connexions

- `M5_arquitectura-proposit-rol-nivell` — Els rols són la capa d'implementació de l'arquitectura P>R>N; aquí es troba la matriu Propòsit × Rol i la jerarquia completa del sistema.
- `M5_proposits-aprenentatge` — Catàleg de propòsits d'aprenentatge; la tria de rol sempre és posterior a la tria de propòsit.
- `M5_nivells-delegacio-mihia` — Catàleg de nivells MIHIA N0–N5; el rang nadiu de cada rol i el col·lapse a N4 dels rols procesuals.
- `M2_carrega-friccio-cognitiva` — Marc teòric de base: les 3 famílies de rols deriven de l'anàlisi de quina càrrega cognitiva externalitzen i quina fricció generen.
- `M5_disseny-instruccional-amb-IA` — Protocol que usa aquest catàleg en el pas 2 del disseny instruccional.

## 4. Detecció

Activar aquest document quan:

- Cal **triar quin rol** assignar a la IA per a una activitat concreta.
- Cal entendre per què un **rol procesual no funciona a N4** (col·lapse del sentit pedagògic).
- Cal **seqüenciar rols** dins d'una activitat o tasca complexa.
- Cal verificar la **coherència entre el rol triat i el nivell MIHIA** de delegació.
- Cal **dissenyar un assistent institucional** amb comportament alineat a un rol explícit.
- Cal escriure un **prompt pedagògic** que codifiqui el comportament d'un rol.

## 5. Fonts

- Mollick, E. (2024). *Co-intelligence: Living and Working with AI*. Portfolio/Penguin. — Font dels 7 rols originals, adaptats per FJE a l'àmbit escolar.
- Jesuïtes Educació / MAGINIA (2026). *Arquitectura Propòsit-Rol-Nivell — Decisions de disseny* (Xat 6, abril 2026). Document intern.
- `exemples-rols-mihia.md` (MAGINIA/public) — 21 exemples concrets (7 rols × 3 etapes) que van generar l'anàlisi de les 3 famílies estructurals.
- `docs/decisions/arquitectura-quest-rol-nivell.md` — ADR intern: decisió de mantenir els 7 rols sense fusionar.
