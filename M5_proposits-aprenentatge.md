---
modul: M5
titol: "Catàleg: 10 propòsits d'aprenentatge per a activitats amb IA"
tipus: cataleg
descripcio: "Inventari dels 10 propòsits d'aprenentatge (missions pedagògiques) que defineixen la intenció cognitiva d'una activitat amb IA, organitzats en 3 famílies (Comprendre, Avaluar, Fer), amb fitxa per propòsit, moviment de fricció associat i rols nadius de la matriu P×R"
review_status: esborrany
generat_at: 2026-05-10T00:00:00
paraules_clau: ["propòsits d'aprenentatge", "missions pedagògiques", "P>R>N", "fricció cognitiva", "ICAP", "Anchor", "Clarity", "Critique", "disseny instruccional", "Mollick"]
---

## Què és aquest catàleg

Un **propòsit d'aprenentatge** és una missió pedagògica que defineix la intenció d'una activitat amb IA. Respon la pregunta del docent: **"Què vull que passi cognitivament en aquesta activitat?"**

Els propòsits d'aprenentatge són el **concepte de primer nivell** de l'arquitectura Propòsit–Rol–Nivell: no defineixen com actua la IA (això ho fan els Rols) ni quanta autonomia cedeix l'alumne (això ho fan els Nivells). Defineixen l'**objectiu cognitiu** de la interacció.

El catàleg és consumit principalment per docents que han de triar un propòsit com a punt de partida del disseny instruccional, i per assistents institucionals que han de seleccionar quina intenció pedagògica activa la interacció.

> **Nota terminològica (abril 2026):** el terme genèric "Quest" s'ha substituït per "propòsit d'aprenentatge". Els noms individuals dels 10 propòsits (Anchor, Clarity, Compare, etc.) es mantenen en anglès com a referència a Khan, Fisher, Frey, Marshall i Hargrave (2025).

## Criteris d'inclusió

Els 10 propòsits provenen de la classificació de Khan, Fisher, Frey, Marshall i Hargrave (2025), adaptada per Jesuïtes Educació (2026).

**Criteris de manteniment del catàleg:**
- S'inclou un propòsit si defineix un **objectiu cognitiu diferenciable** que no es redueix a cap altre propòsit de la llista.
- La cardinalitat és **10**. La decisió de no consolidar a 6-7 és explícita (Xat 6, abril 2026): cada propòsit ocupa un nínxol cognitiu distint i qualsevol fusió perd un matís rellevant. Les 3 famílies resolen el problema de navegació sense perdre granularitat.
- Les 3 famílies es fonamenten en la taxonomia de Fink (2003) pel seu caràcter no jeràrquic, en diàleg amb les bandes de Bloom (Anderson & Krathwohl, 2001) per al seu reconeixement entre docents.

**Font canònica:** Khan, Fisher, Frey, Marshall i Hargrave (2025); `docs/decisions/arquitectura-quest-rol-nivell.md`.

## Inventari

Els 10 propòsits s'organitzen en **tres famílies** que redueixen la càrrega cognitiva de navegació:

| Família | Intenció | Propòsits | Moviment de fricció dominant |
|---|---|---|---|
| **Comprendre** | Construir significat | Anchor, Clarity, Reverse | Descoberta |
| **Avaluar** | Jutjar, defensar, comparar | Compare, Critique, Perspective | Resistència |
| **Fer** | Produir, progressar, créixer | Level-Up, Repte integrador, Right-Sizing, Growth | Recursivitat |

La consonància entre famílies i moviments de fricció és una propietat emergent del sistema (no una imposició teòrica): en creuar els 10 propòsits amb la taula de fricció cognitiva, el patró apareix de manera natural.

---

### Anchor (Ancoratge)

**Resum (1 línia):** L'alumne activa coneixements previs i la IA l'ajuda a connectar-los visiblement amb el nou aprenentatge.
**Quan aplica:** Inici de tema o unitat; quan l'alumne ja té intuïcions però no les ha articulat; quan cal fer emergir coneixement implícit.
**Característiques:** Família Comprendre. Moviment de fricció: Descoberta. Càrrega externalitzada: extrínseca (organització). Mode ICAP: Constructive.
**Exemple:** "Escriu el que saps sobre herència. Després pregunta a la IA quines connexions veu entre el que has escrit i el concepte de gen."
**Rols nadius:** Mentor Socràtic ★★, Teachable Agent ★★, Generador de Casos ★.

---

### Clarity (Clarificació)

**Resum (1 línia):** L'alumne explica un concepte i la IA l'ajuda a refinar la comprensió fins que el significat s'estabilitza.
**Quan aplica:** Quan l'alumne creu que entén però la comprensió és superficial o imprecisa; quan cal fer emergir els malentesos.
**Característiques:** Família Comprendre. Moviment de fricció: Recursivitat. Càrrega externalitzada: extrínseca (formulació de preguntes). Mode ICAP: Interactive.
**Exemple:** "Explica amb les teves paraules la diferència entre mitosi i meiosi. La IA et farà preguntes per verificar que realment ho has entès."
**Rols nadius:** Mentor Socràtic ★★, Teachable Agent ★★, Crític/Editor ★.

---

### Compare (Comparació)

**Resum (1 línia):** L'alumne estableix semblances, diferències i relacions entre conceptes, i la IA introdueix casos nous que aprofundeixen la comparació.
**Quan aplica:** Quan cal construir comprensió estructural d'un camp; quan l'alumne veu elements aïllats però no les relacions entre ells.
**Característiques:** Família Avaluar. Moviment de fricció: Descoberta. Càrrega externalitzada: extrínseca (cerca i generació de casos). Mode ICAP: Constructive.
**Exemple:** "Compara el feudalisme europeu amb el sistema daimyō japonès. La IA et generarà un tercer cas (Imperi Otomà) perquè trobis patrons comuns."
**Rols nadius:** Generador de Casos ★★, Crític/Editor ★, Mentor Socràtic ★.

---

### Critique (Avaluació crítica)

**Resum (1 línia):** L'alumne jutja la qualitat, coherència o validesa d'un contingut o argument, i la IA el desafia a defensar i justificar el judici.
**Quan aplica:** Pensament crític, avaluació de fonts, debat, anàlisi d'arguments; quan l'objectiu és que l'alumne no accepti passivament.
**Característiques:** Família Avaluar. Moviment de fricció: Resistència. Càrrega externalitzada: cap o extrínseca mínima. Mode ICAP: Interactive.
**Exemple:** "Llegeix aquest article sobre canvi climàtic. Identifica 3 arguments febles. La IA defensarà aquests arguments i hauràs de respondre."
**Rols nadius:** Contrincant ★★, Crític/Editor ★★, Mentor Socràtic ★.

---

### Growth (Creixement personal)

**Resum (1 línia):** L'alumne reflexiona sobre el seu propi procés d'aprenentatge i la IA ofereix un mirall que fa visible el progrés metacognitiu.
**Quan aplica:** Metacognició, autoregulació, resiliència, habilitats socioemocionals; quan l'objectiu és que l'alumne es vegi a si mateix amb més claredat.
**Característiques:** Família Fer. Moviment de fricció: Descoberta interna. Mode ICAP: Constructive. La càrrega intrínseca és purament metacognitiva; la IA no substitueix la reflexió.
**Exemple:** "Descriu com has resolt l'últim problema difícil que has tingut. La IA et farà preguntes sobre les teves estratègies i et suggerirà alternatives."
**Rols nadius:** Crític/Editor ★★, Generador de Casos ★, Contrincant ★.

---

### Level-Up (Progressió)

**Resum (1 línia):** L'alumne practica i la IA adapta la dificultat dels reptes segons el rendiment, mantenint sempre una dificultat calibrada.
**Quan aplica:** Pràctica deliberada, adquisició de procediments, millora de fluïdesa; quan cal que la dificultat sigui lleugerament per sobre del nivell actual (zona de desenvolupament proper).
**Característiques:** Família Fer. Moviment de fricció: Recursivitat. Càrrega externalitzada: extrínseca (generació i calibratge d'exercicis). Mode ICAP: Active → Constructive.
**Exemple:** "Resol equacions de primer grau. La IA et genera exercicis cada cop més difícils segons els errors que comets."
**Rols nadius:** Generador de Casos ★★, Simulador ★, Traductor/Adaptador ★.

---

### Repte integrador (*Mission*)

**Resum (1 línia):** L'alumne resol un repte complex i autèntic que requereix mobilitzar múltiples competències en un context realista.
**Quan aplica:** Aprenentatge basat en problemes o projectes, situacions d'aprenentatge competencials, simulació professional; quan l'objectiu és la transferència a contextos reals.
**Característiques:** Família Fer. Moviment de fricció: Recursivitat (el repte requereix múltiples decisions i iteracions). Càrrega externalitzada: extrínseca (context, actors, dades). Mode ICAP: Interactive.
**Exemple:** "Ets l'equip de gestió d'un hospital durant una crisi sanitària. La IA simula les conseqüències de les teves decisions."
**Rols nadius:** Simulador ★★, Generador de Casos ★.

---

### Perspective (Perspectiva)

**Resum (1 línia):** L'alumne explora múltiples punts de vista sobre un tema complex i la IA encarna posicions que l'alumne no consideraria per si sol.
**Quan aplica:** Temes d'alta complexitat social, ètica o política; quan l'objectiu és l'empatia intel·lectual i la comprensió de la pluralitat de raons.
**Característiques:** Família Avaluar. Moviment de fricció: Resistència (l'alumne dialoga amb perspectives incòmodes). Càrrega externalitzada: extrínseca (encarnació de personatges). Mode ICAP: Interactive.
**Exemple:** "La IA actuarà com 3 personatges (empresari, ecologista, treballador) que opinen sobre la deslocalització industrial. Tu has de trobar punts de consens."
**Rols nadius:** Simulador ★★, Contrincant ★★, Mentor Socràtic ★, Traductor/Adaptador ★.

---

### Reverse (Enginyeria inversa)

**Resum (1 línia):** La IA proporciona un producte o solució acabat, i l'alumne el descompon per entendre com funciona per dins.
**Quan aplica:** Comprensió estructural i profunda; quan l'alumne pot reconèixer però no reconstruir; quan cal fer visible el mecanisme intern d'un producte o argument.
**Característiques:** Família Comprendre. Moviment de fricció: Descoberta (el mecanisme intern es fa visible). Càrrega externalitzada: extrínseca (el producte per analitzar). Mode ICAP: Constructive.
**Exemple:** "La IA et dóna un poema. Tu identifies els recursos estilístics, l'estructura i el tema. Després escrius el teu propi poema usant la mateixa estructura."
**Rols nadius:** Teachable Agent ★★, Crític/Editor ★, Generador de Casos ★, Mentor Socràtic ★.

---

### Right-Sizing (Ajustament)

**Resum (1 línia):** L'alumne adapta un contingut o producte a un context, audiència o necessitat específica, decidint conscientment què és essencial i què és accessori.
**Quan aplica:** Inclusió, diferenciació curricular, adaptació de format o nivell, comunicació tècnica a audiències no especialistes.
**Característiques:** Família Fer. Moviment de fricció: Judici selectiu (l'alumne decideix què canviar i per què). Càrrega externalitzada: extrínseca (l'adaptació tècnica del vocabulari o format). Mode ICAP: Constructive.
**Exemple:** "Tens un text sobre nutrició per a adults. Adapta'l per a alumnes de 10 anys. La IA t'ajuda amb el vocabulari, però tu decideixes quins conceptes simplificar i quins mantenir."
**Rols nadius:** Traductor/Adaptador ★★, Generador de Casos ★.

---

## Com triar entre les opcions

**Pas 1 — Identificar la família.** La pregunta és "Quin és l'objectiu cognitiu principal de l'activitat?":
- **Comprendre**: l'alumne construeix significat nou connectant idees → Anchor, Clarity, Reverse.
- **Avaluar**: l'alumne jutja, compara i defensa posicions → Compare, Critique, Perspective.
- **Fer**: l'alumne produeix, practica i progressa → Level-Up, Repte integrador, Right-Sizing, Growth.

**Pas 2 — Afinar dins la família.** Un cop triada la família:
- Dins Comprendre: Anchor si cal activar el que ja sap; Clarity si cal precisar una comprensió existent; Reverse si l'alumne ha de descompondre un producte acabat.
- Dins Avaluar: Compare si cal comparar elements; Critique si cal jutjar qualitat o validesa; Perspective si cal explorar punts de vista múltiples.
- Dins Fer: Level-Up si cal pràctica calibrada; Repte integrador si cal mobilitzar múltiples competències; Right-Sizing si cal adaptar a una audiència; Growth si l'objectiu és metacognitiu.

**Pas 3 — Verificar la matriu Propòsit × Rol.** Cada propòsit té rols nadius (★★) i rols possibles (★). Evitar les combinacions forçades (—). La matriu completa es troba a `M5_arquitectura-proposit-rol-nivell`.

**Matriu d'afinitats Propòsit × Rol (resum):**

| | Mentor S. | Simulador | Crític/Ed. | Gen.Casos | Teach.Ag. | Contrinc. | Traductor |
|---|---|---|---|---|---|---|---|
| **Anchor** | ★★ | — | — | ★ | ★★ | — | — |
| **Clarity** | ★★ | — | ★ | — | ★★ | — | — |
| **Compare** | ★ | — | ★ | ★★ | — | — | — |
| **Critique** | ★ | — | ★★ | — | — | ★★ | — |
| **Growth** | — | — | ★★ | ★ | — | ★ | — |
| **Level-Up** | — | ★ | — | ★★ | — | — | ★ |
| **Repte integrador** | — | ★★ | — | ★ | — | — | — |
| **Perspective** | ★ | ★★ | — | — | — | ★★ | ★ |
| **Reverse** | ★ | — | ★ | ★ | ★★ | — | — |
| **Right-Sizing** | — | — | — | ★ | — | — | ★★ |

★★ = nadiu · ★ = possible · — = forçat o incoherent

## Relació amb altres catàlegs

Aquest catàleg és el primer eix del **sistema P>R>N** (Propòsit–Rol–Nivell):

| Catàleg del sistema | Pregunta que respon | Relació amb aquest |
|---|---|---|
| `M5_proposits-aprenentatge` | **Què ha d'aprendre l'alumne cognitivament?** | **Aquest catàleg** — el punt de partida obligatori |
| `M5_rols-IA-educacio` | Com ha d'actuar la IA? | La matriu Propòsit × Rol determina quins rols serveixen cada propòsit |
| `M5_nivells-delegacio-mihia` | Quanta autonomia cedeix l'alumne? | Cada combinació (Propòsit, Rol) té un rang de nivells MIHIA nadius |

El docent sempre comença pel propòsit (**Propòsit-first**): triar el rol o el nivell sense haver definit la intenció cognitiva és *solution looking for a problem* i genera activitats sense coherència pedagògica.

**Connexió amb el marc cognitiu** (`M2_carrega-friccio-cognitiva`):

| Propòsit | Moviment de fricció | Càrrega externalitzada | Mode ICAP |
|---|---|---|---|
| Anchor | Descoberta | Extrínseca (organització) | Constructive |
| Clarity | Recursivitat | Extrínseca (formulació) | Interactive |
| Compare | Descoberta | Extrínseca (cerca de casos) | Constructive |
| Critique | Resistència | Cap o extrínseca mínima | Interactive |
| Growth | Descoberta interna | — | Constructive |
| Level-Up | Recursivitat | Extrínseca (generació d'exercicis) | Active → Constructive |
| Repte integrador | Recursivitat | Extrínseca (context, dades) | Interactive |
| Perspective | Resistència | Extrínseca (encarnació) | Interactive |
| Reverse | Descoberta | Extrínseca (producte a analitzar) | Constructive |
| Right-Sizing | Judici selectiu | Extrínseca (adaptació tècnica) | Constructive |

## 3. Connexions amb altres documents del corpus

- `M5_arquitectura-proposit-rol-nivell` — Els propòsits són el concepte de primer nivell de l'arquitectura P>R>N; aquí es troba la jerarquia completa i la matriu Propòsit × Rol ampliada.
- `M5_rols-IA-educacio` — La matriu d'afinitats Propòsit × Rol determina quins rols serveixen cada propòsit d'aprenentatge.
- `M5_nivells-delegacio-mihia` — Cada combinació (Propòsit, Rol) té un rang de nivells MIHIA nadius; el nivell efectiu intersecta amb el sostre d'etapa.
- `M2_carrega-friccio-cognitiva` — Cada propòsit s'associa a un moviment de fricció productiva, un tipus de càrrega externalitzada i un mode ICAP.
- `M5_disseny-instruccional-amb-IA` — Els propòsits d'aprenentatge són el punt de partida del pas 1 de la seqüència de disseny instruccional.

## 4. Detecció

Activar aquest document quan:

- Un docent pregunta **"què vull que passi cognitivament?"** en una activitat amb IA i necessita triar una intenció pedagògica.
- Cal **triar un propòsit d'aprenentatge** com a punt de partida per al disseny d'una activitat.
- Cal verificar la **compatibilitat Propòsit × Rol** abans de configurar un assistent o escriure el prompt.
- Cal connectar una activitat amb el **marc cognitiu** (fricció, càrrega, ICAP).
- Cal justificar per què una **combinació Propòsit-Rol és incoherent** (cel·les "—" de la matriu).

## 5. Fonts

- Khan, S., Fisher, D., Frey, N., Marshall, A. i Hargrave, M. (2025). *Khanmigo for Teachers: AI for Learning Design*. — Font dels 10 propòsits d'aprenentatge originals.
- Fink, L. D. (2003). *Creating Significant Learning Experiences*. Jossey-Bass. — Marc no jeràrquic per a les 3 famílies de propòsits.
- Anderson, L. W. i Krathwohl, D. R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing*. Longman. — Referència universal per al diàleg amb les bandes de Bloom.
- Chi, M. T. H. i Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist*, 49(4), 219-243. — Modes ICAP associats a cada propòsit.
- Jesuïtes Educació / MAGINIA (2026). *Arquitectura Propòsit-Rol-Nivell — Decisions de disseny* (Xat 6, abril 2026). Document intern.
- `docs/decisions/arquitectura-quest-rol-nivell.md` — ADR intern: decisió de mantenir els 10 propòsits i les 3 famílies.
