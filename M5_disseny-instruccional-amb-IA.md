---
modul: M5
titol: "Disseny instruccional amb IA: criteris, auditoria i plantilla"
tipus: protocol
descripcio: "Protocol per dissenyar i auditar activitats amb IA: seqüència de cinc decisions P>R>N, set criteris de disseny, vuit preguntes d'auditoria i plantilla estructurada Fase 1/2/3."
review_status: esborrany
generat_at: 2026-05-10
paraules_clau: [disseny instruccional, protocol, P>R>N, auditoria, GRR, plantilla, fricció productiva]
---

# Disseny instruccional amb IA: criteris, auditoria i plantilla

## Context i propòsit

### 4. Disseny = avaluació (Chase & Galvin, 2026)

No hi ha dos actes seqüencials (primer "dissenyar l'activitat", després "dissenyar l'avaluació") sinó **un sol acte de disseny amb dues cares**. En l'era de la IA, aquesta lògica pren importància renovada:

- Una activitat en què la IA pot fer el treball cognitiu nuclear **no és un problema ètic, és un problema de disseny** — l'activitat ja no mesura el que pretén mesurar.
- Les **respostes discursives** (normes "podeu/no podeu usar IA") són insuficients. Cal **redisseny estructural** de la tasca.
- Un ús institucional madur exigeix un **llenguatge d'escala d'IA** (MIHIA) compartit per docents i alumnat.

**Marc operatiu en cinc passos** (adaptat de Griffin, Francis & Robertson, 2017):

1. **Alinear** els objectius d'aprenentatge amb la tasca
2. **Desempaquetar** els constructes: quines *big ideas* ha de demostrar entendre l'alumne?
3. **Desglossar** en capacitats: quines habilitats, coneixements i disposicions?
4. **Traduir** en indicadors observables: quines evidències concretes?
5. **Mapar** els indicadors sobre l'escala MIHIA: quins han de romandre íntegrament humans i quins poden ser suportats per IA?

> La decisió es pren **indicador per indicador**, no activitat per activitat. Això permet fases amb IA i fases sense IA dins la mateixa activitat.

---

## Prerequisits

### 2. Alliberament gradual de la responsabilitat (GRR) aplicat a la IA

Fisher & Frey estableixen quatre fases que s'apliquen a qualsevol activitat amb IA:

| Fase | Nom | Qui lidera | Amb IA |
|---|---|---|---|
| 1 | **Jo faig** | Docent | El docent modela com usar la IA correctament |
| 2 | **Nosaltres fem** | Docent + alumnat | Exercici col·lectiu amb IA, el docent guia |
| 3 | **Vosaltres feu** | Alumnat en grup | Grups usen IA amb pautes clares |
| 4 | **Tu fas** | Alumne individual | L'alumne usa IA autònomament amb criteri |

**Regla d'or**: mai proposar ús autònom de la IA (Fase 4) sense modelatge previ (Fase 1). L'alumne ha de **veure** com el docent usa la IA amb criteri.

**Connexió GRR ↔ MIHIA**:

| Fase GRR | Nivell MIHIA recomanat |
|---|---|
| Jo faig | N0-N1 (el docent demostra) |
| Nosaltres fem | N1-N2 (exploració/suport guiat) |
| Vosaltres feu | N2-N3 (suport/cocreació en grup) |
| Tu fas | N3-N4 (cocreació/delegació supervisada) |

### 8. Granularitat didàctica

| Granularitat | Durada | Integració IA |
|---|---|---|
| **Exercici** | 5-20 min | Un sol rol, un sol nivell MIHIA |
| **Activitat** | 1 sessió (45-60 min) | 1-2 rols, un nivell predominant |
| **Tasca** | 2-5 sessions | Diversos rols, progressió de nivells |
| **Projecte** | 1-4+ setmanes | Mapa complet: rols i nivells per fase |

> Una tasca o projecte pot incloure fases amb IA i fases **sense IA** (N0). La no-delegació és una decisió pedagògica vàlida.

---

## Fases

### 1. La seqüència de disseny del docent (v2)

El disseny d'una activitat amb IA segueix cinc decisions en cascada (arquitectura P>R>N v2, que incorpora l'estructura temporal de Vendrell & Johnston, 2026):

| Pas | Pregunta del docent | Decisió | Referència |
|---|---|---|---|
| **1** | "Què vull que passi cognitivament?" | Triar un **Propòsit d'aprenentatge** | `M5_proposits-aprenentatge` |
| **2** | "On poso la fricció i on la IA?" | Dissenyar l'**estructura temporal**: Fase 1 (sense IA: l'alumnat genera sol) → Fase 2 (amb IA: desafia, contrasta) → Fase 3 (sense IA: sintetitza, integra) | Vendrell & Johnston (2026) |
| **3** | "Com ha d'actuar la IA a la Fase 2?" | Triar un **Rol** compatible | `M5_rols-IA-educacio` — matriu d'afinitats |
| **4** | "Quanta autonomia a la Fase 2?" | Triar un **Nivell** | `M5_nivells-delegacio-mihia` — rang nadiu × sostre |
| **5** | "L'activitat preserva el pensament crític?" | **Checklist de verificació** (7 criteris cognitius + 8 principis Vendrell) | `M2_carrega-friccio-cognitiva` + ADR |

No tota activitat requereix les tres fases: una exploració breu (Propòsit: Anchor, N1) pot ser tota Fase 2. Però quan l'objectiu és aprenentatge profund (Critique, Perspective, Mission), la seqüència completa protegeix l'autonomia cognitiva.

---

## Documents i registres

### 3. Bastida progressiva de prompts

La competència de formular instruccions a la IA segueix una progressió:

| Nivell | Bastida | L'alumne... |
|---|---|---|
| **Principiant** | Prompt complet donat pel docent, l'alumne omple buits | Executa dins d'una estructura tancada |
| **Intermedi** | Estructura donada, l'alumne redacta el contingut | Decideix què preguntar dins d'un format |
| **Avançat** | L'alumne crea el seu propi prompt amb criteris de qualitat | Formula amb autonomia |
| **Expert** | L'alumne avalua, compara i optimitza prompts | Aplica judici meta sobre la interacció |

### 7. Plantilla de disseny d'una activitat amb IA

```
0. TIPUS I DURADA
   - Granularitat: Exercici / Activitat / Tasca / Projecte
   - Durada: Sessions / Setmanes
   - Nombre d'activitats (si Tasca o Projecte)

1. CONTEXT
   - Etapa educativa / Edat
   - Matèria / Àrea
   - Tema / Contingut curricular
   - Objectiu d'aprenentatge (formulat com a constructe, no com a tasca)

2. DISSENY PROPÒSIT-ROL-NIVELL (v2)
   - Propòsit d'aprenentatge triat i justificació
   - Estructura temporal: quines fases té l'activitat?
     · Fase 1 (sense IA): què genera l'alumnat sol?
     · Fase 2 (amb IA): rol + nivell + restriccions
     · Fase 3 (sense IA): com sintetitza i integra?
   - Rol de la IA a la Fase 2 (verificat a la matriu d'afinitats)
   - Nivell MIHIA a la Fase 2 (verificat: rang nadiu × sostre d'etapa)
   - Família del rol (procesual / mixt / productiu)

3. FASE 1 — SENSE IA (Fricció cognitiva)
   - Què fa l'alumnat autònomament (hipòtesi, argument, pla, esborrany...)
   - Activació de coneixements previs
   - CFF establerta (pre-compromís, predicció, justificació...)
   - Mode ICAP esperat (Constructive o Interactive)
   - Preparació docent (Jo faig): què modela el docent

4. FASE 2 — AMB IA (Interacció)
   - Prompt/instrucció (amb bastida progressiva segons nivell)
   - Restriccions i pautes
   - Funció de la IA: desafiar, contrastar, ampliar, provocar (no resoldre)
   - Moviment de fricció esperat (Descoberta / Recursivitat / Resistència)
   - Checkpoints d'avaluació durant la interacció (Vendrell P3)

5. FASE 3 — SENSE IA (Síntesi i metacognició)
   - Què fa l'alumnat amb el resultat de la IA
   - On resideix la propietat cognitiva (McCrea)
   - Documentació del procés: diari reflexiu, log de prompts, comparació abans/després
   - Verificació: càrrega externalitzada = extrínseca (no germana)

6. EVIDÈNCIA D'APRENENTATGE
   - Indicadors observables (pas 4 del marc Griffin)
   - Per a cada indicador: amb IA / sense IA / indiferent
   - Pregunta Macnamara: en 10 repeticions, millorarà?
   - Reflexió metacognitiva prevista
```

---

## Indicadors d'èxit

### 5. Set criteris de disseny

Derivats del marc cognitiu (`M2_carrega-friccio-cognitiva`, §7.1):

| # | Criteri | Pregunta de verificació |
|---|---|---|
| 1 | **Objectiu cognitiu explícit** | Quin esquema ha de construir l'alumne? Quin judici ha de desenvolupar? |
| 2 | **IA per a càrrega extrínseca, no germana** | La IA elimina esforç que construiria aprenentatge? |
| 3 | **Moment de generació autònoma** | L'alumne fa, prova o produeix alguna cosa ABANS que la IA l'assisteixi? |
| 4 | **CFF activa** | Quina funció de forçat cognitiu té la interacció? (pre-compromís, predicció, avaluació...) |
| 5 | **Fricció productiva induïda** | On i com es produirà Descoberta, Recursivitat o Resistència? |
| 6 | **Mode ICAP ≥ Constructive** | L'alumne genera o dialoga, no rep passivament? |
| 7 | **Avaluació sense IA possible** | Almenys una dimensió es pot avaluar sense assistent? |

---

## Revisió i seguiment

### 6. Vuit preguntes d'auditoria

Per a activitats existents que ja incorporen IA:

| # | Pregunta | Si la resposta és NO... |
|---|---|---|
| 1 | Quina càrrega s'externalitza? | Si intrínseca → risc |
| 2 | L'alumne ha generat alguna cosa abans? | Risc de paradoxa del rendiment |
| 3 | Hi ha CFF identificable? | Risc de rendició cognitiva |
| 4 | Mode ICAP? | Si Passive/Active → reformular |
| 5 | En 10 repeticions, millorarà o perdrà l'habilitat? | Risc de *skill decay/hindrance* |
| 6 | Ho pot fer sense IA? | No → risc de dependència |
| 7 | L'avaluació discrimina rendiment/aprenentatge? | Cega a la paradoxa |
| 8 | Fiabilitat de l'assistent auditada? | Si < 70% encert → *crossover point* |

---

## Situacions excepcionals

### 9. Distinció aprenentatge vs. gestió

> **Decisió Xat 5B (abril 2026).**

L'arquitectura Propòsit-Rol-Nivell i els criteris de disseny d'aquest document s'apliquen a **activitats d'aprenentatge** — situacions en què l'objectiu és que l'alumne construeixi esquemes, desenvolupi habilitats o exerciti el judici. En aquest context, la fricció productiva és un requisit i l'offloading de càrrega intrínseca o germana és un risc.

Quan la IA s'usa en **gestió** (administrativa, organitzativa, institucional), l'objectiu és **rendiment**, no aprenentatge. L'offloading de càrrega intrínseca és legítim perquè no hi ha esquema a construir — hi ha una tasca a completar. El risc, en canvi, no és la paradoxa del rendiment sinó l'**erosió del judici professional**: el gestor que delega anàlisi, priorització o redacció a la IA sense exercir-ne el criteri pot perdre la capacitat de detectar errors, matisos o implicacions que l'eina no captura.

| Dimensió | Aprenentatge | Gestió |
|---|---|---|
| **Objectiu** | Construir esquemes, habilitats, judici | Completar tasques amb eficiència |
| **Offloading legítim** | Només càrrega extrínseca | Qualsevol càrrega, amb supervisió |
| **Risc principal** | Paradoxa del rendiment (l'alumne no aprèn) | Erosió del judici professional (el gestor no detecta errors) |
| **Marc aplicable** | Criteris de disseny §5, auditoria §6 | Criteris d'assistents institucionals (en elaboració) |
| **Fricció** | Preservar-la: és el mecanisme d'aprenentatge | Reduir-la: no aporta valor a la tasca |

### 10. Factors d'aprenentatge a preservar

| Factor | Risc amb IA | Com preservar-lo |
|---|---|---|
| **Activació cognitiva** | La IA pensa per l'alumne | CFF: pre-compromís, predicció |
| **Elaboració** | La IA dóna tot elaborat | L'alumne elabora primer |
| **Recuperació** | La IA sempre té la info disponible | Exercicis de recuperació SENSE IA primer |
| **Espaiat** | La IA resol tot d'un cop | Activitats en fases amb intervals |
| **Interleaving** | La IA fa tot un sol tipus | Alternar tasques amb i sense IA |
| **Feedback** | La IA dóna feedback genèric | IA com a feedback específic i accionable |
| **Metacognició** | La IA no demana reflexió; si la consigna la demana, la pot generar la mateixa IA (**delegació recursiva**, vegeu `M2_carrega-friccio-cognitiva` §5.1) | Reflexió post-IA **ancorada al context local** (debat d'aula, vocabulari de la unitat, acords del grup) o feta **a l'aula sense IA**. Una consigna del tipus "marca què canviaries" en una tasca asíncrona no preserva metacognició: la mateixa conversa pot generar text i autocrítica versemblant |
| **Motivació intrínseca** | La IA fa la part interessant | L'alumne fa la part creativa |
| **Transferència** | L'alumne depèn de la IA | Tasques d'aplicació SENSE IA |

---

## Articulació amb el marc Horitzó+ FJE

Aquest protocol opera **dins** del marc institucional FJE, no al marge. La relació entre les fases del disseny instruccional amb IA (M5) i les fases del marc Horitzó+ (M2) és:

| Fase del marc FJE (Horitzó+) | Decisió de disseny IA aplicable |
|---|---|
| **Fase 01 — Repte i comprensió** | Definir si la IA participa de la contextualització del repte (recerca docent prèvia) |
| **Fase 02 — Planificació** | Per a cada objectiu del projecte: aplicar el marc Griffin (alinear-desempaquetar-desglossar-traduir-mapar) → quins indicadors són IA-permissius? Quins són IA-prohibits? |
| **Fase 03 — Investigació** | Aplicar P>R>N a cada activitat amb IA. Aplicar GRR (Jo faig→Tu fas) al llarg de la fase. Els espais STOP poden ser **checkpoints d'auditoria d'ús d'IA** |
| **Fase 04 — Síntesi i difusió** | Decidir si el producte final accepta intervenció d'IA, on, i a quin nivell MIHIA. Pregunta Macnamara aplicada al producte |
| **Fase 05 — Valoració i transferència** | Reflexió metacognitiva (clau personal) inclou: *"com he usat la IA? Com ha modificat el meu aprenentatge?"* — ancorada al context local per evitar delegació recursiva |

### Quan usar cada document

| Si la pregunta del docent és... | Document principal | Document complementari |
|---|---|---|
| "Com es desplega un projecte FJE de cap a peus?" | [[M2_sequencia-aprenentatge-FJE]] | (aquest) si hi ha IA |
| "Com integro la IA dins el projecte?" | **(aquest M5)** | [[M2_sequencia-aprenentatge-FJE]] per al marc global |
| "Quina fricció cognitiva preservo?" | [[M2_carrega-friccio-cognitiva]] | (aquest) per al disseny |
| "Quin rol IA escolliré per a aquesta activitat?" | [[M5_rols-IA-educacio]] | (aquest) per al P>R>N |
| "El producte final pot incloure IA?" | (aquest) §6 Evidència | [[M6_tipologia-instruments-avaluacio]] per a 4 Cs |
| "Com auditem un projecte ja fet?" | (aquest) §6 Vuit preguntes | [[M2_sequencia-aprenentatge-FJE]] §Indicadors qualitat |

### Mapatge de solapaments conceptuals

Diversos elements del marc Horitzó+ FJE i del disseny instruccional amb IA són **isomòrfics**: parlen d'allò mateix amb llenguatges diferents. Aquesta taula explicita les correspondències perquè un docent que conegui un dels dos marcs reconegui ràpidament l'equivalent:

| Concepte M5 (disseny amb IA) | Concepte FJE (Horitzó+) | Notes |
|---|---|---|
| Estructura temporal Fase 1 sense IA / Fase 2 amb IA / Fase 3 sense IA (Vendrell-Johnston) | Rutina per sessió: Obertura / Desenvolupament / Tancament | Ambdues estructures protegeixen un moment de generació autònoma i un moment de síntesi metacognitiva |
| GRR Jo faig → Nosaltres fem → Vosaltres feu → Tu fas (Fisher-Frey) | Codocència + STOP + autonomia progressiva | GRR és el principi; la codocència és el dispositiu institucional FJE |
| Bastida progressiva de prompts (Principiant→Expert) | Bastida lingüística del gènere textual (modelatge → producció guiada → autònoma) | Mateix patró: andamiatge cada cop més fi |
| Plantilla 6-blocs (Context/PRN/Fase1/Fase2/Fase3/Evidència) | Guia del projecte + DAP + QTC | Una és per a disseny d'activitat, l'altra per a disseny de projecte sencer |
| Set criteris de disseny (§5) | Indicadors de qualitat del projecte FJE (§ corresponent) | Els criteris de M5 són un subconjunt centrat en IA |
| Vuit preguntes d'auditoria (§6) | Heurístiques per al docent (M2) | Les heurístiques M2 són més globals; les preguntes M5 són específiques per a IA |
| Granularitat: exercici/activitat/tasca/projecte | Calendari tipus (10%/10%/60%/15%/5%) | Compatibles: un projecte FJE conté tasques i activitats |
| Distinció aprenentatge vs gestió | (no contemplada explícitament al marc FJE) | M5 cobreix un buit del marc FJE |

> **Conclusió operativa**: aquest document i el [[M2_sequencia-aprenentatge-FJE]] són **dos documents mestres complementaris**, no redundants. El primer és el marc institucional sencer; el segon és l'arquitectura crítica de disseny quan la IA hi participa.

## 3. Connexions amb altres documents del corpus

- **`M2_sequencia-aprenentatge-FJE`** — **Marc institucional FJE complet** (Horitzó+, NEI/TQE) on aquest protocol s'aplica. Aquest document és el marc operatiu de la seqüència d'aprenentatge a NEI i TQE. Vegeu §Articulació amb el marc Horitzó+ FJE més amunt
- **`M5_arquitectura-proposit-rol-nivell`** — La seqüència de disseny (5 passos, v2) opera dins l'arquitectura P>R>N v2
- **`M5_proposits-aprenentatge`** — Pas 1: triar propòsit d'aprenentatge
- **`M5_rols-IA-educacio`** — Pas 3: triar Rol compatible
- **`M5_nivells-delegacio-mihia`** — Pas 4: triar Nivell (rang × sostre)
- **`M2_carrega-friccio-cognitiva`** — Pas 5: verificar fricció. Criteris de disseny i auditoria
- **`M2_models-disseny-instruccional`** — Granularitat didàctica, GRR, fases de projecte FJE
- **`M6_feedback-formatiu`** — Distinció Assessment FOR vs OF Learning aplicada quan la IA dóna feedback
- **`M6_tipologia-instruments-avaluacio`** — Avaluació autèntica amb les 4 Cs aplicable al producte final
- **Doc futur `avaluacio-ia-disseny.md`** — AIAS, marc Griffin, enforcement pyramid

## 4. Detecció

Activar aquest document quan:

- Un docent vol **dissenyar una activitat amb IA** des de zero
- Cal **auditar una activitat existent** que incorpora IA
- Cal una **plantilla estructurada** per al disseny
- Cal verificar que el disseny **preserva la fricció productiva** i els factors d'aprenentatge
- Cal aplicar el **GRR** a una seqüència amb IA
- Cal decidir el **nivell de bastida** del prompt per a l'alumnat
- Cal justificar per què **dissenyar l'activitat i dissenyar l'avaluació és el mateix acte**

## 5. Fonts

- Vendrell, M. & Johnston, S.-K. (2026) — Estructura temporal Sense-Amb-Sense IA; *checklist* P1-P8
- Fisher, D. & Frey, N. — GRR (Gradual Release of Responsibility)
- Chase, J. & Galvin, T. (2026) — Disseny = Avaluació
- Griffin, P., Francis, M. & Robertson, P. (2017) — Marc operatiu de 5 passos per alinear objectius i avaluació
- Kosmyna, N. et al. (2025) — *Your Brain on ChatGPT* (MIT Media Lab); menor connectivitat neural (EEG) i menor record del propi text en escriure amb assistència LLM respecte a escriure sense ajuda
- Font interna: ADR Xat 5B (abril 2026) — distinció aprenentatge vs. gestió
- Font interna: docs/fonts/laia-knowledge/disseny-instruccional.md
