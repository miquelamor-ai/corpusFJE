---
modul: M5
titol: "Catàleg: nivells de delegació MIHIA (N0–N5)"
tipus: cataleg
descripcio: "Inventari dels 6 graus d'autonomia cedida a la IA (Model d'Integració Humà-IA), amb fitxa per nivell, perfil de fricció cognitiva, sostre per etapa educativa i regles de progressió"
review_status: esborrany
generat_at: 2026-05-10T00:00:00
paraules_clau: ["MIHIA", "nivells de delegació", "N0", "N4", "fricció cognitiva", "mapa d'etapes", "disseny instruccional", "AI Fluency"]
---

## Què és aquest catàleg

Inventari dels **6 graus d'autonomia** que un alumne (o docent) pot cedir a la IA en una activitat educativa. L'escala MIHIA (Model d'Integració Humà-IA) és el **tercer eix** de l'arquitectura Propòsit–Rol–Nivell: un cop definit el propòsit d'aprenentatge i assignat el rol de la IA, el nivell regula *quanta càrrega cognitiva es delega a la màquina*.

El catàleg és consumit per docents que dissenyen activitats, equips que defineixen sosstre de delegació per etapa, i dissenyadors d'assistents que han de configurar el grau d'autonomia dels sistemes institucionals.

**Nota important:** els nivells no són una escala de "millor a pitjor" ni de "més modern a menys modern". Cada nivell és l'opció correcta per a un propòsit d'aprenentatge i un moment formatiu concrets. N0 (sense IA) és una decisió pedagògica tan legítima com N4.

## Criteris d'inclusió

L'escala MIHIA és una adaptació institucional de Jesuïtes Educació a partir del Marc General sobre la Integració de la IA (MAGINIA, 2026), que al seu torn recull el *AI Fluency Framework* de Dakan i Feller (2026) i el mapa de delegació del Model 4D.

**Criteris de manteniment del catàleg:**
- S'inclou un nivell si defineix un **perfil de delegació diferenciable** que no es redueix a un altre nivell de l'escala.
- La cardinalitat és **6** (N0–N5). La decisió de no fusionar N2 i N3 (Suport i Cocreació) es fonamenta en el diferent paper de l'alumne: a N2 l'alumne genera primer i la IA reacciona; a N3 ambdós construeixen de manera iterativa des del principi.
- El sostre de nivell per etapa educativa és una decisió col·legiada de les direccions dels centres (MAGINIA, 2026); no és una recomanació externa.

**Font canònica:** `M5_arquitectura-proposit-rol-nivell` + `M0_marc-institucional-IA` (§ Model operatiu).

## Inventari

---

### N0 — No delegació

**Resum (1 línia):** L'alumne fa tota la tasca sense cap intervenció de la IA.
**Quan aplica:** Quan l'objectiu és que l'alumne exerciti una habilitat que la IA faria per ell; quan la dificultat és desitjable i cal preservar-la íntegrament (Bjork); quan l'activitat requereix fracàs productiu previ a qualsevol suport (Kapur); quan l'avaluació necessita evidència d'habilitat autònoma.
**Característiques:** Fricció màxima (intrínseca pura). 4D principal: D1 (decidir NO delegar). No hi ha risc de rendició cognitiva. **N0 és una decisió pedagògica, no una mancança**: és l'elecció correcta sempre que la fricció cognitiva sigui l'objectiu mateix de l'activitat.
**Exemple:** Examen d'escriptura argumentativa on l'alumne ha de demostrar que sap construir un argument des de zero, sense suport extern.
**Conflictes/incompatibilitats:** Risc d'ineficiència si s'aplica a tasques mecàniques on la IA podria alliberar temps per a activitats de més valor cognitiu.

---

### N1 — Exploració

**Resum (1 línia):** L'alumne utilitza la IA com a font d'informació, aclariment de dubtes o mirall d'idees; no es genera cap artefacte final.
**Quan aplica:** Ampliació del coneixement, pràctica del pensament crític, primers contactes supervisats amb la IA, familiarització amb com funciona un model de llenguatge.
**Característiques:** Fricció alta. 4D principals: D2 (formular preguntes clares) + D3 (avaluar respostes). L'alumne transforma informació en raonament propi. Risc baix: pot consumir passivament si no hi ha una tasca activa que el forci a processar.
**Exemple:** Primària Superior (guiat) — l'alumne pregunta a la IA sobre el cicle de l'aigua i contrasta la resposta amb el que ha observat en un experiment, identificant diferències.
**Conflictes/incompatibilitats:** Si l'alumne copia les respostes sense processar, l'activitat ha degenerat a consum passiu. Cal dissenyar una tasca de producció posterior que forci la transformació de la informació.

---

### N2 — Suport / Reacció

**Resum (1 línia):** L'alumne crea el contingut base primer; la IA revisa, corregeix o proposa millores sobre el que l'alumne ha fet.
**Quan aplica:** Escriptura, projectes, produccions on l'alumne necessita retroalimentació externa per millorar. L'alumne és l'autor; la IA és el revisor.
**Característiques:** **Zona de fricció productiva màxima.** 4D principals: D2 + D3 + D4. La seqüència crítica és: *primer l'alumne crea, després la IA reacciona*. Si s'inverteix l'ordre (la IA genera i l'alumne modifica), es degrada a N3–N4.
**Exemple:** ESO 1r cicle — l'alumne escriu un primer esborrany d'un text argumentatiu; llavors la IA li assenyala incoherències i preguntes sense respondre; l'alumne reescriu.
**Conflictes/incompatibilitats:** Risc moderat si la retroalimentació de la IA és massa completa i l'alumne simplement aplica els canvis sense entendre'ls. Cal que el docent exigeixi que l'alumne justifiqui cada canvi que fa.

---

### N3 — Cocreació

**Resum (1 línia):** L'alumne i la IA construeixen conjuntament un producte en un diàleg iteratiu bidireccional; l'alumne lidera i pren les decisions.
**Quan aplica:** Projectes complexos, producció creativa, recerca, quan la iteració entre humà i IA genera un resultat que cap dels dos podria produir sol.
**Característiques:** Fricció alta amb suport. Totes les 4D en joc. La clau és que **l'alumne lidera**: guia el procés, refina la direcció i integra les aportacions de la IA. Si la IA comença a liderar i l'alumne es limita a acceptar, l'activitat ha degenerat a N4.
**Exemple:** ESO 2n cicle — l'alumne dissenya un experiment científic co-creant el protocol amb la IA: proposa hipòtesis (humà), la IA suggereix metodologia (IA), l'alumne decideix i justifica (humà), la IA proposa materials (IA), l'alumne valida (humà).
**Conflictes/incompatibilitats:** Risc de desalineació: l'alumne segueix la IA en lloc de liderar-la. Cal establir explícitament que cada decisió de la IA requereix una decisió humana conscient que la validi o rebutgi.

---

### N4 — Delegació supervisada

**Resum (1 línia):** L'alumne defineix instruccions detallades i la IA genera un producte complet; l'alumne valida críticament, avalua i reelabora.
**Quan aplica:** Quan la generació ràpida d'un artefacte de qualitat serveix l'objectiu (Batxillerat, FP Grau Superior); quan l'objectiu d'aprenentatge recau en la validació i la reelaboració, no en la generació.
**Característiques:** Fricció baixa durant la generació; la fricció es trasllada a la validació i reelaboració. 4D principals: D2 (prompt sofisticat) + D3 (validació crítica) + D4 (responsabilitat final). **Risc alt de rendició cognitiva** si l'alumne no reelabora de manera substantiva.
**Exemple:** Batxillerat — l'alumne defineix el prompt per generar un primer esborrany d'un article científic; llavors el verifica factualment, en reescriu les conclusions i declara l'ús de la IA.
**Conflictes/incompatibilitats:** Els rols procesuals (Mentor Socràtic, Teachable Agent, Contrincant) **col·lapsen a N4**: la IA genera el diàleg complet i el rol perd l'essència pedagògica. Excepció: N4 amb rols procesuals és acceptable si l'objectiu explícit és aprendre enginyeria de prompts, no el contingut del domini.

---

### N5 — Agència autònoma

**Resum (1 línia):** L'alumne dissenya el sistema (prompt, agent, chatbot, flux de treball) i la IA opera autònomament dins els paràmetres que ell ha definit.
**Quan aplica:** FP Grau Superior, activitats d'alfabetització en IA i pensament computacional, formació de docents avançats. L'objectiu no és contingut curricular sinó el **disseny de sistemes**.
**Característiques:** Fricció mínima durant l'ús del sistema; **màxima durant el disseny**. 4D principals: D1 (definir paràmetres amplis) + D4 (auditoria ètica del sistema). L'alumne és el dissenyador i supervisor estratègic, no l'operador.
**Exemple:** FP Grau Superior (Administració de Sistemes) — l'alumne dissenya un chatbot d'atenció als alumnes de l'escola amb un conjunt de regles i restriccions; el posa a prova i n'audita el comportament.
**Conflictes/incompatibilitats:** **N5 és excepcional** i no és un objectiu per a la majoria d'etapes. Si s'aplica sense que l'alumne tingui la maduresa per dissenyar amb criteri, el risc ètic és elevat. Mai proposar N5 sense haver consolidat N3–N4 prèviament.

---

## Com triar entre les opcions

**Regla general — rang efectiu.** El nivell adequat per a una activitat concreta és la **intersecció** de dos factors:
1. **Rang nadiu** de la combinació (Propòsit, Rol) — quin nivell fa que el rol tingui sentit pedagògic ple.
2. **Sostre d'etapa** — el màxim que permet el mapa educatiu per a aquella etapa.

`Rang efectiu = rang nadiu ∩ sostre d'etapa`

**Sostre de nivell per etapa educativa:**

| Etapa | Sostre MIHIA | Nivells predominants |
|---|---|---|
| Infantil (I3-I5) | N0 | N0 — manipulació, sensorialitat, joc |
| Primària Inicial (PRI-CI) | N0–N1 | N0 — introducció conceptual: què és la IA |
| Primària Superior (PRI-CS) | N0–N1 | N0–N1 — exploració guiada i supervisada |
| ESO 1r cicle (12–14) | N0–N2 | N0–N2 — suport i reacció, fricció alta |
| ESO 2n cicle (14–16) | N0–N3 | N1–N3 — cocreació, iteració amb IA |
| Batxillerat (16–18) | N0–N4 | N1–N4 — delegació supervisada |
| FP Grau Mitjà | N0–N4 | N1–N4 — contextual al mòdul professional |
| FP Grau Superior | N0–N5 | N2–N5 — inclou disseny d'agents |

**El sostre és un màxim, no un objectiu.** Un alumne de batxillerat pot (i sovint ha de) treballar a N2.

**Regles de progressió:**
1. No saltar més d'un nivell sense haver consolidat l'anterior.
2. Progressió no lineal: un alumne pot treballar a N3 en una matèria i a N1 en una altra — el nivell depèn del domini de contingut, no només de l'edat.
3. GRR obligatori (Fisher & Frey): mai proposar ús autònom (N4–N5) sense modelatge previ del docent (N0–N1). L'alumne ha de veure com el docent usa la IA amb criteri.
4. N5 és excepcional: implica alfabetització en IA i pensament computacional; l'objectiu no és contingut curricular sinó disseny de sistemes.

## Relació amb altres catàlegs

Aquest catàleg és el tercer eix del **sistema P>R>N** (Propòsit–Rol–Nivell):

| Catàleg del sistema | Pregunta que respon | Relació amb aquest |
|---|---|---|
| `M5_proposits-aprenentatge` | Què ha d'aprendre l'alumne cognitivament? | El propòsit i el rol determinen el rang nadiu de nivells compatibles |
| `M5_rols-IA-educacio` | Com ha d'actuar la IA? | Les 3 famílies de rols tenen rangs nadius diferenciats; els rols procesuals col·lapsen a N4 |
| `M5_nivells-delegacio-mihia` | **Quanta autonomia cedeix l'alumne?** | **Aquest catàleg** |

La intersecció dels tres eixos (rang nadiu del propòsit, rang nadiu del rol, sostre d'etapa) determina el nivell efectiu de cada activitat. Consultar `M5_arquitectura-proposit-rol-nivell` per a la matriu completa.

**Connexió amb AI Fluency (Dakan-Feller, 2026):**

| Mode AI Fluency | Nivells MIHIA |
|---|---|
| Automation (IA executa tasques definides) | N1–N2 |
| Augmentation (IA col·labora, potencia) | N2–N4 |
| Agency (IA agent autònom dins paràmetres) | N4–N5 |

## 3. Connexions amb altres documents del corpus

- `M5_arquitectura-proposit-rol-nivell` — El nivell és el tercer eix de l'arquitectura P>R>N; aquí es troba la matriu completa i la jerarquia del sistema.
- `M5_rols-IA-educacio` — Les 3 famílies de rols (procesual, mixt, productiu) determinen el rang nadiu de cada rol; els procesuals col·lapsen a N4.
- `M5_proposits-aprenentatge` — El rang efectiu és la intersecció del rang nadiu (Propòsit, Rol) amb el sostre d'etapa d'aquest catàleg.
- `M2_carrega-friccio-cognitiva` — Cada nivell externalitza un tipus de càrrega cognitiva diferent; el perfil de fricció per nivell connecta directament amb la teoria CLT (Sweller).
- `M5_disseny-instruccional-amb-IA` — La tria del nivell és el pas 3 de la seqüència de disseny instruccional del docent.
- `M0_marc-institucional-IA` — El mapa de delegació pedagògica per etapes és la font canònica institucional del sostre per etapa.

## 4. Detecció

Activar aquest document quan:

- Cal **decidir el nivell de delegació** per a una activitat concreta.
- Cal verificar si el **sostre d'etapa** permet el nivell que s'ha triat.
- Cal entendre per què un **rol procesual no funciona a N4** (col·lapse del sentit pedagògic).
- Cal justificar per què **N0 és una decisió pedagògica vàlida**, no una limitació.
- Cal calcular el **rang efectiu** d'una combinació (Propòsit, Rol) per a una etapa concreta.
- Cal orientar la **progressió d'un alumne** d'un nivell al següent.

## 5. Fonts

- Dakan, E. i Feller, S. (2026). *AI Fluency Framework* (Model 4D: Delegation, Description, Discernment, Diligence). — Base del model de graus d'autonomia.
- Jesuïtes Educació / MAGINIA (2026). *Marc General sobre la Integració de la IA*. Document intern. — Font del mapa de delegació pedagògica per etapes.
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. — Fonament del concepte de dificultat desitjable (N0 com a elecció).
- Kapur, M. (2016). Examining productive failure, productive success, unproductive failure, and unproductive success in learning. *Educational Psychologist*. — Fonament del fracàs productiu previ al suport.
- Fisher, D. i Frey, N. (2014). *Better Learning Through Structured Teaching: A Framework for the Gradual Release of Responsibility*. — Fonament de la regla GRR (mai N4–N5 sense modelatge previ).
- `docs/decisions/arquitectura-quest-rol-nivell.md` — ADR intern: decisions de disseny de l'escala MIHIA.
- `docs/fonts/laia-knowledge/model-4d-mihia.md` — Versió LAIA del marc 4D (versió precedent).
