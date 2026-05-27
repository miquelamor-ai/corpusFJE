---
modul: M2
titol: "Models de disseny instruccional i seqüències didàctiques"
tipus: marc
descripcio: "Marc per estructurar propostes didàctiques amb IA: jerarquia de granularitat exercici/activitat/tasca/projecte, GRR de Fisher & Frey, fases de projecte FJE i tipologia de seqüències."
review_status: esborrany
generat_at: 2026-05-10
paraules_clau: [disseny instruccional, GRR, granularitat, seqüències didàctiques, scaffolding, projectes FJE, ZDP]
---

# Models de disseny instruccional i seqüències didàctiques

## Definició i principis

### 1. Jerarquia de granularitat didàctica

El docent pot dissenyar propostes de diferent abast. Cada nivell de granularitat implica una estructura, durada i integració IA diferent:

| Granularitat | Durada | Estructura | Integració IA |
|---|---|---|---|
| **Exercici** | 5-20 min | Una instrucció + resposta | Un sol rol, un sol nivell MIHIA |
| **Activitat** | 1 sessió (45-60 min) | Inici → Desenvolupament → Tancament | 1-2 rols, un nivell predominant |
| **Tasca** | 2-5 sessions | Seqüència d'activitats connectades | Diversos rols, progressió MIHIA |
| **Projecte** | 1-4+ setmanes | Fases FJE (Repte→Investigació→Síntesi→Acció) | Mapa complet de rols i nivells per fase |

```
PROJECTE (setmanes)
├── Tasca 1 (sessions)
│   ├── Activitat 1.1 (1 sessió)
│   │   ├── Exercici A (minuts)
│   │   └── Exercici B
│   └── Activitat 1.2
└── Tasca 2
    └── ...
```

> **Regla**: una tasca o projecte pot incloure fases amb IA i fases **sense IA** (N0). La no-delegació és una decisió pedagògica vàlida.

### Backward Design (Wiggins & McTighe): dissenyar a la inversa

El **Backward Design** o *disseny a la inversa* (Wiggins & McTighe, *Understanding by Design*, 2005) inverteix la lògica habitual de planificació. En lloc de partir dels continguts o activitats disponibles, parteix dels **resultats d'aprenentatge desitjats** i, només després, dissenya l'avaluació i les activitats:

| Estadi | Pregunta orientadora |
|---|---|
| 1. **Resultats desitjats** | Què han d'arribar a entendre, saber fer i ser els alumnes? |
| 2. **Evidència acceptable** | Com sabré que ho han assolit? Quina forma té l'avaluació autèntica? |
| 3. **Pla d'aprenentatge** | Quines experiències portaran fins a aquests resultats? |

L'ordre Resultats → Avaluació → Activitats té dues conseqüències:

- **L'avaluació es dissenya abans que les activitats**, no després; opera com a brúixola del disseny.
- **Les activitats** són els mitjans per assolir els resultats, no l'objectiu en si. Si una activitat no contribueix al resultat desitjat, per atractiva que sigui, és prescindible.

Aquesta lògica és complementària a la jerarquia de granularitat i al GRR: un projecte ben dissenyat parteix d'un resultat clar i gradua l'autonomia per assolir-lo.

---

## Autors i evidència clau

### 2. Model de Responsabilitat Gradual (GRR, Fisher & Frey)

| Fase | Nom | Qui lidera | Amb IA |
|---|---|---|---|
| 1 | **Jo faig** | Docent | Modela com usar la IA correctament |
| 2 | **Nosaltres fem** | Docent + Alumnat | Exercici col·lectiu amb IA, el docent guia |
| 3 | **Vosaltres feu** | Alumnat en grup | Grups usen IA amb pautes clares |
| 4 | **Tu fas** | Alumne individual | L'alumne usa IA autònomament amb criteri |

**Regla d'or**: mai proposar ús autònom de la IA (Fase 4) sense modelatge previ (Fase 1).

**Connexió GRR ↔ MIHIA ↔ Zona de Desenvolupament Proper** (Vygotsky):

| Fase GRR | MIHIA | ZDP |
|---|---|---|
| Jo faig | N0-N1 | El docent opera a la ZDP; l'alumne observa |
| Nosaltres fem | N1-N2 | Bastida col·lectiva dins la ZDP |
| Vosaltres feu | N2-N3 | Bastida entre iguals dins la ZDP |
| Tu fas | N3-N4 | Competència consolidada; retirada de bastida |

**Connexió amb el marc cognitiu**: el GRR gradua no només l'autonomia sinó la **fricció productiva**. A les fases inicials, el docent modela com gestionar la fricció (com no rendir-se davant la IA, com verificar, com iterar). Sense aquest modelatge, l'alumne no té un referent de com exercir les 4D.

### 4. Scaffolding (Bastida pedagògica)

| Principi | Descripció | Amb IA |
|---|---|---|
| **Temporal** | El suport es retira progressivament | Reduir el detall del prompt al llarg del curs |
| **Contingent** | S'ajusta al nivell de l'alumne | Adaptar la complexitat de la interacció |
| **Metacognitiu** | Fa visible el procés de pensament | La IA pregunta "per què ho fas així?" |
| **Procedimental** | Guia els passos a seguir | Prompt estructurat amb passos clars |

**Bastida progressiva de prompts**: documentada en detall a `M5_disseny-instruccional-amb-IA` (§3).

### Quatre espais d'aprenentatge (Go & Atienza, inspirats en Thornburg)

Go i Atienza (2019), reprenent la metàfora de Thornburg, proposen quatre configuracions d'espai d'aprenentatge —físic o virtual— que activen modes diferents de relació amb el contingut. Una bona unitat alterna deliberadament entre les quatre:

| Espai | Què hi passa | Pregunta orientadora | Quan és adequat |
|---|---|---|---|
| **Foguera** (*Campfire*) | Aprendre d'experts | "Què hem de saber?" | Modelatge, explicació, lectures |
| **Cafè** (*Café*) | Aprendre entre iguals | "Què en pensem?" | Discussió, contrast, construcció col·lectiva |
| **Cova** (*Cave*) | Aprendre de si mateix | "Què penso jo?" | Reflexió individual, escriptura, estudi |
| **Comunitat** (*Community*) | Aprendre del món | "Què en fem?" | Aplicació real, servei, impacte |

Una classe limitada a un sol espai —típicament la *Foguera*— empobreix les oportunitats d'aprenentatge. La integració d'IA modifica els quatre: pot expandir la *Foguera*, enriquir el *Cafè*, aprofundir la *Cova* o ampliar la *Comunitat*. El risc és que l'IA col·lapsi els quatre espais en una sola interacció, eliminant la riquesa relacional que cadascun aporta.

### Taxonomia SOLO (Biggs & Collis) com a verificador de profunditat

A l'hora de **dissenyar objectius d'aprenentatge**, la taxonomia SOLO (Prestructural / Unistructural / Multistructural / Relacional / Abstract estès) és una bona eina de verificació de profunditat:

| Nivell SOLO | Verb operatiu típic | Tipus d'evidència |
|---|---|---|
| Unistructural | identificar, anomenar | reconèixer un element |
| Multistructural | enumerar, descriure | llistar diversos elements |
| Relacional | explicar, comparar, contrastar | mostrar connexions entre elements |
| Abstract estès | generalitzar, hipotetitzar, transferir | aplicar a un context nou |

Backward Design (Wiggins-McTighe) i SOLO són complementaris: l'un fixa el "punt d'arribada" desitjat (objectiu); l'altre permet qualificar quan s'ha arribat amb prou profunditat. Una pràctica eficient és **etiquetar els objectius del projecte amb el nivell SOLO objectiu** i, en avaluar, mesurar quin nivell SOLO ha aconseguit cada alumne.

Vegeu [[M2_sequencia-aprenentatge-FJE]] § Mapatge amb taxonomies de profunditat per a la correspondència entre SOLO i els Cercles de la comprensió FJE.

### Cinc verbs operatius de l'alumne (Five ATEs, Go & Atienza)

Sintetitzen el que l'alumne ha de fer activament — cinc verbs que acaben en *-ate*:

| Verb | Significat | Connexió amb el procés |
|---|---|---|
| **Investigate** | Indagar, cercar fonts, preguntar | Inici i alimentació del cicle |
| **Contemplate** | Reflexionar, mirar amb profunditat | Reflexió en les tres dimensions (vegeu [[M0_PPI-paradigma-pedagogic-ignasia]] § Tres dimensions de la Reflexió) |
| **Create** | Produir, fer una obra pròpia | Materialització del que s'ha entès |
| **Communicate** | Compartir, fer-se entendre | Sortir de si mateix cap als altres |
| **Collaborate** | Construir amb altres | Aprenentatge dialògic i social |

El disseny d'una unitat es pot auditar preguntant-se quants d'aquests verbs activa realment l'alumne. Una unitat on l'alumne només "rep" —escolta, llegeix, copia— sense investigar, contemplar, crear, comunicar ni col·laborar és estructuralment passiva, encara que el docent posi entusiasme a explicar.

---

## Exemples concrets d'aplicació a l'aula

### 3. Fases de projecte FJE (Marc Horitzó+, Orientacions FJE 2024)

A partir del document *Orientacions psicopedagògiques per la implementació dels nous projectes FJE-LOMLOE* (Jesuïtes Educació, febrer 2024), la seqüència d'aprenentatge dels projectes FJE s'estructura en **cinc fases**:

| Fase | Objectiu | Activitats típiques | Rol IA suggerit | Fricció esperada |
|---|---|---|---|---|
| **01. Repte i comprensió** | Emmarcar els nous aprenentatges en una situació rellevant; connectar amb coneixements previs | Repte amb rellevància social, producte final versemblant, activitats de coneixements previs | Simulador, Generador de casos | Descoberta |
| **02. Planificació** | Compartir objectius generals; marcar objectius d'aprenentatge personals (DAP); formar equips amb compromisos i rols (QTC) | Lectura de la Guia, elaboració del DAP, distribució de rols al QTC | Suport a la planificació | Compromís |
| **03. Investigació** | Desenvolupar habilitats des de fonamentació fins a aplicació; espais regulars de regulació (STOP) i diàleg (Espai diàleg / Afrontem el dilema) | Activitats graduades en complexitat cognitiva, metodologia i agrupació; rutina per sessió (Obertura → Desenvolupament → Tancament) | Mentor Socràtic, Crític | Recursivitat |
| **04. Síntesi i difusió** | Aplicar aprenentatges al repte; mostrar el producte final a audiències reals dins i/o fora de la comunitat educativa | Aplicació en context, presentació pública, lliurament a destinataris reals | Crític/Editor, Traductor/Adaptador | Resistència |
| **05. Valoració i transferència** | Reflexionar sobre els aprenentatges en clau personal, conceptual i de procés (metacognició) | Recuperar preguntes inicials, valorar objectius (DAP), valorar treball d'equip (QTC) | Acompanyant metacognitiu | Judici |

**Notes operatives de les Orientacions FJE 2024:**

- **Espai 01–02 al servei del 03**: les fases inicials no són tràmits sinó cura pedagògica del context i del compromís. Sense la qualitat del repte i del DAP, les fases posteriors perden força.
- **Dins la Fase 03**, cada sessió segueix una **rutina d'aprenentatge** (Obertura amb element motivador + activació prèvia + objectius → Desenvolupament d'habilitats → Tancament amb síntesi i revisió d'objectius).
- **Espais STOP**: aturades regulars dins la Investigació perquè l'alumnat identifiqui què sap, resolgui dubtes, faci seguiment d'objectius i prengui decisions de millora.
- **Espai diàleg** (1r–2n NEI) / **Afrontem el dilema** (3r–4t TQE): espais de diàleg sobre situacions controvertides reals per desenvolupar pensament crític i valors de justícia/sostenibilitat.
- **Distinció avaluativa al cor de la Fase 03**: activitats d'avaluació formativa-formadora (feedback, sense qualificació) a l'inici i avaluació sumativa-qualificadora (evidències amb nota) cap al final. Vegeu [[M6_feedback-formatiu]].

**Connexió amb el marc cognitiu**: les cinc fases FJE generen una progressió natural en els moviments de fricció (Descoberta → Compromís → Recursivitat → Resistència → Judici). El disseny ha de verificar que la IA no curtcircuiti aquesta progressió — especialment a la Fase 03 (Investigació), on la temptació de delegar la cerca i l'anàlisi a la IA és màxima.

### 5. Tipus de seqüències didàctiques

| Tipus | Estructura | Integració IA suggerida | Propòsit afí |
|---|---|---|---|
| **Lineal** | Inici → Desenvolupament → Tancament | IA en Desenvolupament (suport) | Clarity, Level-Up |
| **Cíclica/Iterativa** | Prova → Feedback → Millora → Prova | IA com a font de feedback iteratiu | Critique, Growth |
| **Investigativa** | Pregunta → Hipòtesi → Dades → Conclusió | IA com a Generador de Casos/Dades | Compare, Reverse |
| **Projecte** | Repte → Investigació → Creació → Acció | IA en rols diferents per fase | Repte integrador (*Mission*) |
| **Flipped** | Contingut a casa → Aplicació a classe | IA per contingut previ, classe per fricció | Anchor, Clarity |
| **Socràtica** | Pregunta → Diàleg → Descobriment | IA com a Mentor Socràtic | Critique, Perspective |

**Connexió amb propòsits d'aprenentatge**: la columna "Propòsit afí" connecta cada tipus de seqüència amb els propòsits d'aprenentatge més naturals, permetent al docent triar el propòsit adequat segons el tipus de seqüència que ja utilitza.

---

## Errors comuns — què NO fer

- **Proposar ús autònom de la IA (Fase 4 del GRR) sense modelatge previ (Fase 1).** L'alumne no té referent de com usar la IA amb criteri si el docent no ho ha modelat primer.
- **Curtcircuitar la Fase d'Investigació (Fase 2 del projecte FJE) delegant la cerca i l'anàlisi a la IA.** És exactament la fase on la temptació és màxima i el risc de descàrrega cognitiva detrimental és més alt.
- **Tractar la no-delegació (N0) com a fracàs o manca d'innovació.** La no-delegació és una decisió pedagògica vàlida i de vegades la més adequada.
- **Usar la mateixa granularitat per a tots els objectius.** Un exercici de 10 minuts no es pot estructurar com un projecte, ni un projecte de 4 setmanes com un exercici.

---

## Matissos i excepcions

### 6. Factors d'aprenentatge a preservar

Documentats en detall a `M5_disseny-instruccional-amb-IA` (§10). Resum: activació cognitiva, elaboració, recuperació, espaiat, interleaving, feedback, metacognició, motivació intrínseca, transferència. Cada factor té un risc específic amb IA i una estratègia de preservació.

---

## 3. Connexions amb altres documents del corpus

- **`M2_carrega-friccio-cognitiva`** — El GRR gradua la fricció productiva; les fases de projecte generen progressió en els moviments de fricció
- **`M2_sequencia-aprenentatge-FJE`** — **Document marc autoritatiu** de la seqüència d'aprenentatge FJE (Orientacions FJE-LOMLOE 2024): cinc fases completes amb DAP, QTC, STOP, Espai diàleg, Cercles de la comprensió, pauta de planificació docent i orientacions per a direccions. Aquest document és la **referència institucional** que vehicula tot el desplegament Horitzó+ a NEI i TQE.
- **`M0_PPI-paradigma-pedagogic-ignasia`** — Fonament ignasià de la seqüència: dinamisme Experiència-Reflexió-Acció, triangle Docent-Alumne-Món, 6 Es i 3 dimensions de Reflexió (que la Fase 05 FJE operativitza com a personal/conceptual/de procés).
- **`M5_disseny-instruccional-amb-IA`** — Operacionalitza aquests models en criteris, auditoria i plantilla
- **`M5_arquitectura-proposit-rol-nivell`** — Els tipus de seqüència connecten amb propòsits d'aprenentatge específics
- **`M5_nivells-delegacio-mihia`** — La connexió GRR ↔ MIHIA gradua l'autonomia
- **`M5_rols-IA-educacio`** — Les fases de projecte FJE tenen rols suggerits per fase

## 4. Detecció

Activar aquest document quan:

- Cal **determinar la granularitat** d'una proposta (exercici, activitat, tasca, projecte)
- Cal aplicar el **GRR a una seqüència amb IA** i saber on situar cada nivell MIHIA
- Cal **estructurar un projecte FJE** amb integració IA per fases
- Cal triar un **tipus de seqüència didàctica** i connectar-lo amb propòsits d'aprenentatge
- Cal **graduar el scaffolding** d'una activitat (bastida temporal, contingent, metacognitiva)

## 5. Fonts

- Fisher, D. & Frey, N. — Model de Responsabilitat Gradual (GRR)
- Vygotsky, L. S. — Zona de Desenvolupament Proper (ZDP)
- Vendrell, M. & Johnston, S.-K. (2026) — Estructura temporal Sense-Amb-Sense IA
- Wiggins, G. & McTighe, J. (2005). *Understanding by Design* (2a ed.). Alexandria, VA: ASCD.
- Go, J. & Atienza, R. (2019). *Learning by Refraction: A Practitioner's Guide to 21st-Century Ignatian Pedagogy*. Quezon City: Loyola Schools Press.
- Thornburg, D. (2013). *From the Campfire to the Holodeck: Creating Engaging and Powerful 21st Century Learning Environments*. San Francisco: Jossey-Bass.
- Jesuïtes Educació (2024). *Orientacions psicopedagògiques per la implementació dels nous projectes FJE-LOMLOE*. Barcelona: Jesuïtes Educació, febrer 2024.
- Biggs, J. & Collis, K. (1982). *Evaluating the Quality of Learning: The SOLO Taxonomy*. New York: Academic Press.
