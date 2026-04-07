---
title: "Disseny instruccional amb IA: criteris, auditoria i plantilla"
module: M5
id: M5_disseny-instruccional-amb-IA
review_status: esborrany
version: "1.0"
sources:
  - docs/marcs-teorics/friccio-cognitiva-extens.md
  - docs/decisions/arquitectura-quest-rol-nivell.md
  - docs/fonts/laia-knowledge/disseny-instruccional.md
connections:
  - M5_arquitectura-proposit-rol-nivell
  - M5_proposits-aprenentatge
  - M5_rols-IA-educacio
  - M5_nivells-delegacio-mihia
  - M2_carrega-friccio-cognitiva
  - M2_models-disseny-instruccional
detection:
  - "Quan un docent vol dissenyar una activitat que incorpora IA"
  - "Quan cal auditar una activitat existent que usa IA"
  - "Quan cal una plantilla per estructurar el disseny"
  - "Quan cal verificar que el disseny preserva la fricció productiva"
---

# Disseny instruccional amb IA: criteris, auditoria i plantilla

> Document de referència per als skills: Generador d'Activitats, Auditor Cognitiu, Dissenyador de Prompts
> Complementa: `disseny-instruccional.md` (versió LAIA, focus en granularitat i seqüències)

---

## Contingut

### 1. La seqüència de disseny del docent

El disseny d'una activitat amb IA segueix quatre decisions en cascada (arquitectura P>R>N):

| Pas | Pregunta del docent | Decisió | Referència |
|---|---|---|---|
| **1** | "Què vull que passi cognitivament?" | Triar un **Propòsit d'aprenentatge** | `M5_proposits-aprenentatge` |
| **2** | "Com ha d'actuar la IA?" | Triar un **Rol** compatible | `M5_rols-IA-educacio` — matriu d'afinitats |
| **3** | "Quanta autonomia?" | Triar un **Nivell** | `M5_nivells-delegacio-mihia` — rang nadiu × sostre |
| **4** | "Hi ha fricció productiva?" | Verificar amb el marc cognitiu | `M2_carrega-friccio-cognitiva` — 7 criteris |

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

### 3. Bastida progressiva de prompts

La competència de formular instruccions a la IA segueix una progressió:

| Nivell | Bastida | L'alumne... |
|---|---|---|
| **Principiant** | Prompt complet donat pel docent, l'alumne omple buits | Executa dins d'una estructura tancada |
| **Intermedi** | Estructura donada, l'alumne redacta el contingut | Decideix què preguntar dins d'un format |
| **Avançat** | L'alumne crea el seu propi prompt amb criteris de qualitat | Formula amb autonomia |
| **Expert** | L'alumne avalua, compara i optimitza prompts | Aplica judici meta sobre la interacció |

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

2. DISSENY PROPÒSIT-ROL-NIVELL
   - Propòsit d'aprenentatge triat i justificació
   - Rol de la IA assignat (verificat a la matriu d'afinitats)
   - Nivell MIHIA (verificat: rang nadiu × sostre d'etapa)
   - Família del rol (procesual / mixt / productiu)

3. PREPARACIÓ (Jo faig)
   - Què modela el docent
   - Com es presenta la tasca
   - Activació de coneixements previs
   - CFF establerta (pre-compromís, predicció, justificació...)

4. INTERACCIÓ AMB IA (Nosaltres fem → Tu fas)
   - Prompt/instrucció (amb bastida progressiva segons nivell)
   - Restriccions i pautes
   - Moviment de fricció esperat (Descoberta / Recursivitat / Resistència)
   - Mode ICAP esperat (Constructive o Interactive)

5. POST-IA (Fricció productiva)
   - Què fa l'alumne amb el resultat de la IA
   - On resideix la propietat cognitiva (McCrea)
   - Verificació: càrrega externalitzada = extrínseca (no germana)

6. EVIDÈNCIA D'APRENENTATGE
   - Indicadors observables (pas 4 del marc Griffin)
   - Per a cada indicador: amb IA / sense IA / indiferent
   - Pregunta Macnamara: en 10 repeticions, millorarà?
   - Reflexió metacognitiva prevista
```

### 8. Granularitat didàctica

| Granularitat | Durada | Integració IA |
|---|---|---|
| **Exercici** | 5-20 min | Un sol rol, un sol nivell MIHIA |
| **Activitat** | 1 sessió (45-60 min) | 1-2 rols, un nivell predominant |
| **Tasca** | 2-5 sessions | Diversos rols, progressió de nivells |
| **Projecte** | 1-4+ setmanes | Mapa complet: rols i nivells per fase |

> Una tasca o projecte pot incloure fases amb IA i fases **sense IA** (N0). La no-delegació és una decisió pedagògica vàlida.

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
| **Metacognició** | La IA no demana reflexió | Afegir pas de reflexió post-IA |
| **Motivació intrínseca** | La IA fa la part interessant | L'alumne fa la part creativa |
| **Transferència** | L'alumne depèn de la IA | Tasques d'aplicació SENSE IA |

---

## Connexions

| Document | Relació |
|---|---|
| `M5_arquitectura-proposit-rol-nivell` | La seqüència de disseny (4 passos) opera dins l'arquitectura P>R>N |
| `M5_proposits-aprenentatge` | Pas 1: triar propòsit d'aprenentatge |
| `M5_rols-IA-educacio` | Pas 2: triar Rol compatible |
| `M5_nivells-delegacio-mihia` | Pas 3: triar Nivell (rang × sostre) |
| `M2_carrega-friccio-cognitiva` | Pas 4: verificar fricció. Criteris de disseny i auditoria |
| `M2_models-disseny-instruccional` | Granularitat didàctica, GRR, fases de projecte FJE |
| `exemples-rols-mihia.md` | 21 exemples que segueixen (o poden millorar-se amb) aquesta plantilla |
| Doc futur `avaluacio-ia-disseny.md` | AIAS, marc Griffin, enforcement pyramid |

---

## Detecció

Activar aquest document quan:

- Un docent vol **dissenyar una activitat amb IA** des de zero
- Cal **auditar una activitat existent** que incorpora IA
- Cal una **plantilla estructurada** per al disseny
- Cal verificar que el disseny **preserva la fricció productiva** i els factors d'aprenentatge
- Cal aplicar el **GRR** a una seqüència amb IA
- Cal decidir el **nivell de bastida** del prompt per a l'alumnat
- Cal justificar per què **dissenyar l'activitat i dissenyar l'avaluació és el mateix acte**

---

*Versió 1.0 · Esborrany · Jesuïtes Educació Catalunya · 2026*
