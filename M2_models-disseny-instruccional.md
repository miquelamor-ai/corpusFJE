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

---

## Exemples concrets d'aplicació a l'aula

### 3. Fases de projecte (Marc FJE)

| Fase | Objectiu | Activitats típiques | Rol IA suggerit | Fricció esperada |
|---|---|---|---|---|
| 1. **Repte / Comprensió** | Comprendre el problema, activar previs | Pregunta motriu, pluja d'idees | Simulador, Gen.Casos | Descoberta |
| 2. **Investigació** | Cercar, analitzar, contrastar | Recerca, lectura, dades | Mentor Socràtic, Crític | Recursivitat |
| 3. **Síntesi / Creació** | Crear producte o solució | Redacció, disseny, producció | Crític/Editor, Traductor | Resistència |
| 4. **Acció / Comunicació** | Presentar, compartir, aplicar | Exposició, publicació | Traductor/Adaptador | Judici |

**Connexió amb el marc cognitiu**: les fases de projecte FJE generen naturalment progressió en els moviments de fricció (Descoberta → Recursivitat → Resistència). El disseny ha de verificar que la IA no curtcircuiti aquesta progressió — especialment a la Fase 2 (Investigació), on la temptació de delegar la cerca i l'anàlisi a la IA és màxima.

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
