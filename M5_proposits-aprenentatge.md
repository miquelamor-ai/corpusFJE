---
title: "10 propòsits d'aprenentatge: missions pedagògiques per a activitats amb IA"
module: M5
id: M5_proposits-aprenentatge
review_status: esborrany
version: "1.0"
sources:
  - docs/decisions/arquitectura-quest-rol-nivell.md
connections:
  - M5_arquitectura-proposit-rol-nivell
  - M5_rols-IA-educacio
  - M5_nivells-delegacio-mihia
  - M2_carrega-friccio-cognitiva
  - M5_disseny-instruccional-amb-IA
detection:
  - "Quan un docent vol dissenyar una activitat amb IA i necessita definir la intenció pedagògica"
  - "Quan cal triar quin propòsit d'aprenentatge serveix un objectiu concret"
  - "Quan cal connectar un propòsit d'aprenentatge amb els Rols i Nivells compatibles"
---

# 10 propòsits d'aprenentatge: missions pedagògiques per a activitats amb IA

> **Nota terminològica (abril 2026):** el terme genèric "Quest" s'ha substituït per **"propòsit d'aprenentatge"**. Els noms propis dels 10 propòsits individuals (Anchor, Clarity, Compare, etc.) es mantenen en anglès, com a referència a Khan, Fisher, Frey, Marshall & Hargrave (2025). L'arquitectura passa a denominar-se **Propòsit-Rol-Nivell**.

> Document de referència per als skills: Generador d'Activitats, Dissenyador d'Assistents
> Font: Khan, Fisher, Frey, Marshall & Hargrave (2025)

---

## Contingut

### 1. Què és un propòsit d'aprenentatge

Un propòsit d'aprenentatge és una **missió pedagògica** que defineix la intenció d'una activitat amb IA. Respon la pregunta del docent: **"Què vull que passi cognitivament en aquesta activitat?"**

Els propòsits d'aprenentatge són el **concepte de primer nivell** de l'arquitectura Propòsit-Rol-Nivell. No defineixen com actua la IA (això ho fan els Rols) ni quanta autonomia cedeix l'alumne (això ho fan els Nivells). Defineixen **l'objectiu cognitiu**.

### 2. Els 10 propòsits d'aprenentatge

#### Anchor (Ancoratge)

**Intenció**: activar coneixements previs i connectar-los amb nous aprenentatges.

L'alumne parteix del que ja coneix i la IA ajuda a fer visible la connexió amb el que ha d'aprendre. La fricció productiva resideix en la **Descoberta**: l'alumne veu relacions que no havia vist.

**Exemple**: "Abans de començar el tema de genètica, escriu el que saps sobre herència. Després pregunta a la IA quines connexions veu entre el que has escrit i el concepte de gen."

#### Clarity (Clarificació)

**Intenció**: aclarir conceptes, corregir malentesos, arribar a comprensió precisa.

L'alumne intenta explicar un concepte i la IA l'ajuda a refinar la seva comprensió mitjançant preguntes o feedback. La fricció productiva resideix en la **Recursivitat**: iteració fins que el significat s'estabilitza.

**Exemple**: "Explica amb les teves paraules la diferència entre mitosi i meiosi. La IA et farà preguntes per veure si realment ho has entès."

#### Compare (Comparació)

**Intenció**: establir semblances, diferències i relacions entre conceptes, teories o fenòmens.

L'alumne analitza elements i la IA genera contraexemples, casos límit o perspectives alternatives que forcen una comparació més profunda. La fricció resideix en la **Descoberta**: buits i matisos que emergeixen de la comparació.

**Exemple**: "Compara el feudalisme europeu amb el sistema daimyō japonès. La IA et generarà un tercer cas (Imperi Otomà) perquè trobis patrons comuns."

#### Critique (Avaluació crítica)

**Intenció**: avaluar qualitat, coherència, validesa o fiabilitat d'un contingut, argument o producte.

L'alumne jutja i la IA actua com a provocadora intel·lectual o com a font de material per avaluar. La fricció resideix en la **Resistència**: l'alumne ha de justificar el seu judici.

**Exemple**: "Llegeix aquest article sobre el canvi climàtic. Identifica 3 arguments febles. Després la IA t'oferirà una defensa d'aquests arguments i hauràs de respondre."

#### Growth (Creixement personal)

**Intenció**: desenvolupar hàbits metacognitius, autoregulació, resiliència o habilitats socioemocionals.

L'alumne reflexiona sobre el seu propi procés d'aprenentatge i la IA ofereix mirall, feedback o preguntes d'autoconeixement. La fricció resideix en la **Descoberta** interna: veure's a un mateix amb més claredat.

**Exemple**: "Descriu com has resolt l'últim problema difícil que has tingut. La IA et farà preguntes sobre les teves estratègies i et suggerirà alternatives."

#### Level-Up (Progressió)

**Intenció**: avançar progressivament en dificultat dins d'un domini, amb reptes calibrats.

L'alumne practica i la IA adapta la dificultat segons el rendiment. La fricció resideix en la calibració: la dificultat és sempre lleugerament per sobre del nivell actual (zona de desenvolupament proper).

**Exemple**: "Resol equacions de primer grau. La IA et genera exercicis cada cop més difícils segons els errors que comets."

#### Repte integrador (*Mission*)

**Intenció**: resoldre un repte complex, autèntic i contextualitzat que requereix mobilitzar múltiples competències.

L'alumne s'enfronta a un escenari real o simulat i la IA proporciona context, actors o dades. La fricció resideix en la **Recursivitat**: el repte requereix múltiples iteracions i decisions.

**Exemple**: "Ets l'equip de gestió d'un hospital durant una crisi sanitària. La IA simula les conseqüències de les teves decisions."

#### Perspective (Perspectiva)

**Intenció**: explorar múltiples punts de vista sobre un tema complex, desenvolupar empatia intel·lectual.

L'alumne considera perspectives diverses i la IA encarna posicions o actors que l'alumne no consideraria per si sol. La fricció resideix en la **Resistència**: l'alumne ha de dialogar amb perspectives incòmodes.

**Exemple**: "La IA actuarà com 3 personatges diferents (un empresari, un ecologista, un treballador) que opinen sobre la deslocalització industrial. Tu has de trobar punts de consens."

#### Reverse (Enginyeria inversa)

**Intenció**: descompondre un producte, argument o solució per entendre com funciona per dins.

L'alumne analitza un resultat i intenta reconstruir el procés que l'ha generat. La IA proporciona el producte; l'alumne ha de desfer-lo. La fricció resideix en la **Descoberta**: el mecanisme intern es fa visible.

**Exemple**: "La IA et dóna un poema. Tu has d'identificar-ne els recursos estilístics, l'estructura i el tema. Després escriuràs el teu propi poema usant la mateixa estructura."

#### Right-Sizing (Ajustament)

**Intenció**: adaptar un contingut, producte o solució a un context, audiència o necessitat específica.

L'alumne pren un material i l'ajusta conscientment a un destinatari concret. La IA pot fer l'adaptació tècnica, però l'alumne pren les decisions sobre què canviar i per què. La fricció resideix en el judici: què és essencial i què és accessori.

**Exemple**: "Tens un text sobre nutrició escrit per a adults. Adapta'l per a alumnes de 10 anys. La IA et pot ajudar amb el vocabulari, però tu decideixes quins conceptes simplificar i quins mantenir."

---

### 3. Les 3 famílies de propòsits

Per facilitar la navegació del docent, els 10 propòsits s'organitzen en tres famílies funcionals:

| Família | Intenció | Propòsits |
|---|---|---|
| **Comprendre** | Construir significat | Anchor, Clarity, Reverse |
| **Avaluar** | Jutjar, defensar, comparar | Compare, Critique, Perspective |
| **Fer** | Produir, progressar, créixer | Level-Up, Repte integrador (*Mission*), Right-Sizing, Growth |

El docent tria primer la família (3 opcions), després el propòsit dins la família (3-4 opcions). Això redueix la càrrega cognitiva de triar d'un llistat pla de 10 elements.

#### Fonamentació de les 3 famílies

Les tres famílies s'inspiren en la **taxonomia de Fink (2003)** pel seu caràcter explícitament no jeràrquic — les sis dimensions de Fink (*Foundational Knowledge, Application, Integration, Human Dimension, Caring, Learning How to Learn*) interactuen sense ordre obligat, igual que les nostres famílies són opcions paral·leles, no una escala. Alhora, dialoguen amb les **bandes de la taxonomia revisada de Bloom (Anderson & Krathwohl, 2001)** pel seu reconeixement universal entre docents:

| Família | Dimensions Fink | Bandes Bloom |
|---|---|---|
| **Comprendre** | Foundational Knowledge | Remember + Understand |
| **Avaluar** | Integration | Analyze + Evaluate |
| **Fer** | Application + Human Dimension + Learning How to Learn | Apply + Create |

A més, les 3 famílies mostren **consonància empírica amb els moviments de fricció productiva** del propi marc (`M2_carrega-friccio-cognitiva`): el moviment de fricció *dominant* de cada família coincideix amb un dels tres moviments de Novokshanova:

| Família | Moviment de fricció dominant | Operació cognitiva |
|---|---|---|
| **Comprendre** | **Descoberta** | L'alumne veu connexions que no veia |
| **Avaluar** | **Resistència** | L'alumne defensa posicions i justifica judicis |
| **Fer** | **Recursivitat** | L'alumne itera fins a estabilitzar un producte |

Aquesta consonància no és una imposició teòrica sinó una propietat emergent del sistema: en creuar els 10 propòsits amb la taula de fricció (§5), el patró apareix de manera natural. No és 1:1 perfecte (Clarity té Recursivitat, Compare té Descoberta), però el moviment dominant de cada família sí que coincideix.

> **Decisió Xat 6 (abril 2026):** es mantenen els 10 propòsits originals de Khan, Fisher, Frey, Marshall & Hargrave (2025). No es consoliden a 6-7 perquè cada propòsit ocupa un nínxol cognitiu distint i qualsevol fusió perd un matís rellevant. Les 3 famílies resolen el problema de navegació sense perdre granularitat. Fonamentació: Fink (2003) com a marc no jeràrquic, Bloom (2001) com a referència universal, moviments de fricció com a validació interna.

### 4. Matriu d'afinitats Propòsit × Rol

Cada propòsit d'aprenentatge admet un subconjunt de Rols. La correspondència no és 1:1 ni N:N pur; és una **matriu dispersa d'afinitats**:

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

**★★** = nadiu (combinació natural), **★** = possible, **—** = forçat o incoherent.

Les combinacions amb "—" no haurien de constar al catàleg d'assistents.

### 5. Propòsit × Moviment de fricció × Càrrega × ICAP

Cada propòsit d'aprenentatge s'associa al marc cognitiu (`M2_carrega-friccio-cognitiva`):

| Propòsit | Moviment de fricció principal | Càrrega que externalitza | Mode ICAP esperat |
|---|---|---|---|
| **Anchor** | Descoberta | Extrínseca (organització) | Constructive |
| **Clarity** | Recursivitat | Extrínseca (formulació) | Interactive |
| **Compare** | Descoberta | Extrínseca (cerca de casos) | Constructive |
| **Critique** | Resistència | Cap o extrínseca | Interactive |
| **Growth** | Descoberta (interna) | — | Constructive |
| **Level-Up** | Recursivitat | Extrínseca (generació d'exercicis) | Active → Constructive |
| **Repte integrador** | Recursivitat | Extrínseca (context, dades) | Interactive |
| **Perspective** | Resistència | Extrínseca (encarnació de personatges) | Interactive |
| **Reverse** | Descoberta | Extrínseca (producte a analitzar) | Constructive |
| **Right-Sizing** | Judici (selectiu) | Extrínseca (adaptació tècnica) | Constructive |

---

### 6. Decisions pendents

- ~~**Nombre definitiu de propòsits d'aprenentatge**~~: **Resolt (Xat 6)** — es mantenen els 10 originals, organitzats en 3 famílies (§3).
- **Reformulació de la taula màster** de propòsits d'aprenentatge amb columnes de fricció, càrrega i ICAP (columnes de la taula §5 ja prefiguren l'estructura). Pendent.
- ~~**Assignar propòsit d'aprenentatge als 21 exemples**~~ de `exemples-rols-mihia.md`: **Resolt (Xat 6)** — cada exemple té camp `Propòsit d'aprenentatge`.

---

## Connexions

| Document | Relació |
|---|---|
| `M5_arquitectura-proposit-rol-nivell` | Els propòsits d'aprenentatge són el concepte de primer nivell de l'arquitectura P>R>N |
| `M5_rols-IA-educacio` | La matriu Propòsit × Rol determina quins rols serveixen cada propòsit |
| `M5_nivells-delegacio-mihia` | Cada combinació (Propòsit, Rol) té un rang de Nivells nadiu |
| `M2_carrega-friccio-cognitiva` | Cada propòsit d'aprenentatge s'associa a moviment de fricció, càrrega i mode ICAP |
| `M5_disseny-instruccional-amb-IA` | Els propòsits d'aprenentatge són el punt de partida del pas 1 de la seqüència de disseny |

---

## Detecció

Activar aquest document quan:

- Un docent pregunta **"què vull que passi cognitivament?"** en una activitat amb IA
- Cal **triar un propòsit d'aprenentatge** com a punt de partida per al disseny d'una activitat
- Cal verificar la **compatibilitat Propòsit × Rol** abans de configurar un assistent
- Cal connectar una activitat amb el **marc cognitiu** (fricció, càrrega, ICAP)
- Cal justificar per què una **combinació Propòsit-Rol és incoherent** (cel·les amb "—" a la matriu)

---

*Versió 1.0 · Esborrany · Jesuïtes Educació Catalunya · 2026*
