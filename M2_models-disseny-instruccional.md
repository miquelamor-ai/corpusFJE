---
modul: M2
titol: "Models de disseny instruccional i seqüències didàctiques"
tipus: marc
descripcio: "Granularitat didàctica (exercici/activitat/tasca/projecte), GRR, fases de projecte FJE, scaffolding i connexió amb el marc cognitiu i l'arquitectura Quest-Rol-Nivell"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Definició i principis

Els models de disseny instruccional estructuren el "com ensenyem" en una seqüència coherent. En l'era de la IA, aquest "com" ha d'integrar decisions sobre quan, com i a quin nivell la IA participa en l'activitat. Això connecta directament amb l'arquitectura Quest-Rol-Nivell i amb el marc de fricció productiva: cada decisió de disseny instruccional és, simultàniament, una decisió sobre quina càrrega cognitiva es preserva i quina s'externalitza.

### Jerarquia de granularitat didàctica

El docent dissenya propostes de diferent abast. Cada granularitat implica una integració IA diferent:

| Granularitat | Durada | Estructura | Integració IA |
|---|---|---|---|
| **Exercici** | 5-20 min | Una instrucció + resposta | Un sol rol, un sol nivell MIHIA |
| **Activitat** | 1 sessió (45-60 min) | Inici → Desenvolupament → Tancament | 1-2 rols, un nivell predominant |
| **Tasca** | 2-5 sessions | Seqüència d'activitats connectades | Diversos rols, progressió MIHIA |
| **Projecte** | 1-4+ setmanes | Fases FJE | Mapa complet de rols i nivells per fase |

Una tasca o projecte pot incloure fases amb IA i fases sense IA (N0). La no-delegació és una decisió pedagògica vàlida.

### Model de Responsabilitat Gradual (GRR, Fisher & Frey)

| Fase | Nom | Qui lidera | Amb IA | MIHIA |
|---|---|---|---|---|
| 1 | Jo faig | Docent | Modela com usar la IA correctament | N0-N1 |
| 2 | Nosaltres fem | Docent + alumnat | Exercici col·lectiu amb IA | N1-N2 |
| 3 | Vosaltres feu | Alumnat en grup | Grups usen IA amb pautes | N2-N3 |
| 4 | Tu fas | Alumne individual | Ús autònom amb criteri | N3-N4 |

**Regla d'or**: mai proposar ús autònom (Fase 4) sense modelatge previ (Fase 1).

**Connexió amb el marc cognitiu**: el GRR gradua no només l'autonomia sinó la fricció productiva. A les fases inicials, el docent modela com gestionar la fricció (com no rendir-se davant la IA, com verificar, com iterar). Sense modelatge, l'alumne no té un referent de com exercir les 4D.

**Connexió amb la ZDP (Vygotsky)**: el nivell MIHIA adequat ha de situar l'alumne dins la zona de desenvolupament proper. A Fase 1, el docent opera a la ZDP; a Fase 4, la competència està consolidada i la bastida es retira.

### Fases de projecte (Marc FJE)

| Fase | Objectiu | Rol IA suggerit | Fricció esperada |
|---|---|---|---|
| 1. Repte / Comprensió | Comprendre el problema, activar previs | Simulador, Generador de Casos | Descoberta |
| 2. Investigació | Cercar, analitzar, contrastar | Mentor Socràtic, Crític | Recursivitat |
| 3. Síntesi / Creació | Crear producte o solució | Crític/Editor, Traductor | Resistència |
| 4. Acció / Comunicació | Presentar, compartir, aplicar | Traductor/Adaptador | Judici |

Les fases FJE generen naturalment progressió en els moviments de fricció (Descoberta → Recursivitat → Resistència). El disseny ha de verificar que la IA no curtcircuiti aquesta progressió, especialment a la Fase 2 (Investigació), on la temptació de delegar la cerca i l'anàlisi és màxima.

### Scaffolding (Bastida pedagògica)

| Principi | Descripció | Amb IA |
|---|---|---|
| Temporal | El suport es retira progressivament | Reduir el detall del prompt al llarg del curs |
| Contingent | S'ajusta al nivell de l'alumne | Adaptar la complexitat de la interacció |
| Metacognitiu | Fa visible el procés de pensament | La IA pregunta "per què ho fas així?" |
| Procedimental | Guia els passos a seguir | Prompt estructurat amb passos clars |

### Tipus de seqüències didàctiques i Quests afins

| Tipus | Estructura | IA suggerida | Quest afí |
|---|---|---|---|
| Lineal | Inici → Desenvolupament → Tancament | IA en Desenvolupament | Clarity, Level-Up |
| Cíclica/Iterativa | Prova → Feedback → Millora → Prova | IA com a font de feedback | Critique, Growth |
| Investigativa | Pregunta → Hipòtesi → Dades → Conclusió | IA com a Generador | Compare, Reverse |
| Projecte | Repte → Investigació → Creació → Acció | IA en rols per fase | Mission |
| Flipped | Contingut a casa → Aplicació a classe | IA per contingut previ | Anchor, Clarity |
| Socràtica | Pregunta → Diàleg → Descobriment | IA com a Mentor Socràtic | Critique, Perspective |

Aquesta columna "Quest afí" permet al docent que ja treballa amb un tipus de seqüència trobar la Quest adequada sense canviar la seva metodologia.

## Autors i evidència clau

*   **Fisher, D. & Frey, N.**: GRR. El model de responsabilitat gradual fonamentat en la ZDP de Vygotsky. La connexió GRR ↔ MIHIA és una aportació de JE.
*   **Vygotsky, L. S.**: Zona de Desenvolupament Proper. Fonament teòric del scaffolding i del GRR.
*   **Wiggins, G. & McTighe, J. (1998)**: Backward design (Understanding by Design). Partir de l'evidència d'aprenentatge i treballar cap enrere.
*   **Sweller, J. (1988)**: CLT aplicada al disseny instruccional. La gestió de la càrrega cognitiva determina l'eficàcia de la seqüència.
*   **Martin, A. J. et al. (2025)**: Load Reduction Instruction (LRI). Adaptació de la instrucció directa a contextos d'IA.

## Exemples concrets d'aplicació a l'aula

1.  **GRR complet (Anglès, 2n ESO, 4 sessions)**:
    Sessió 1 (Jo faig): El docent demostra com usar la IA com a Simulador ("londinenc a la parada d'autobús") per practicar anglès. Modela com formular preguntes, com gestionar respostes imprevisibles i com no acceptar traduccions directes (N1).
    Sessió 2 (Nosaltres fem): Tot el grup interactua conjuntament amb la IA projectada a la pantalla. El docent guia però els alumnes proposen les preguntes (N2).
    Sessió 3 (Vosaltres feu): Parelles d'alumnes interactuen amb la IA cadascuna pel seu compte, amb un guió-bastida preparat pel docent (N2-N3).
    Sessió 4 (Tu fas): Cada alumne manté una conversa individual amb la IA durant 10 minuts, sense guió, només amb criteri (N3).

2.  **Projecte FJE amb IA (Ciències Socials, 3r ESO, 3 setmanes)**:
    Fase 1 (Repte): La IA genera un cas simulat d'una ciutat que ha de decidir sobre un projecte urbanístic (Generador de Casos, N3). Descoberta.
    Fase 2 (Investigació): L'alumne investiga sense IA (N0) i després contrasta amb un Mentor Socràtic que fa preguntes sobre les seves fonts (N2). Recursivitat.
    Fase 3 (Síntesi): L'alumne escriu la seva proposta. Un Crític/Editor assenyala febleses sense reescriure (N2). Resistència.
    Fase 4 (Acció): L'alumne presenta. Si vol, un Traductor adapta la presentació a un format diferent (N3-N4). Aquí la delegació és legítima: el contingut ja és de l'alumne.

3.  **Exercici curt (Matemàtiques, 1r ESO, 15 min)**:
    Generador de Casos (N3-N4): "Crea'm 10 equacions de primer grau, dificultat mitjana, sense solucions." L'alumne les resol sol (N0 per a la resolució). Després verifica amb la IA. Un sol rol, un sol nivell, 15 minuts. Fricció: Recursivitat (pot demanar més si necessita més pràctica).

## Errors comuns — què NO fer

1.  **Saltar la fase "Jo faig" del GRR.** Si el docent no ha modelat com usar la IA amb criteri, els alumnes no tenen un referent. Donaran per bo el primer output, no verificaran, no iteraran. El modelatge no és opcional, és el fonament de tota la seqüència.

2.  **Posar IA a totes les fases d'un projecte.** Les fases FJE no requereixen IA a tot arreu. La Fase 2 (Investigació) pot beneficiar-se de moments sense IA (N0) on l'alumne lluita amb les fonts primàries. La temptació de "posar IA a tot" elimina la fricció de les fases on és més productiva.

3.  **No adaptar la granularitat a la integració IA.** Un exercici de 15 minuts no necessita 3 rols diferents ni progressió de nivells. Una activitat d'1 sessió pot tenir 1-2 rols. La complexitat de la integració ha de ser proporcional a la durada.

4.  **Confondre scaffolding amb simplificació.** La bastida no simplifica la tasca; la fa accessible mantenint el repte. Un prompt-bastida ("Pregunta a la IA com a [rol], que revisi [aspecte], sense [restricció]") no fa la tasca més fàcil; dóna estructura perquè l'alumne sàpiga per on començar. Es retira quan l'alumne pot formular el prompt sol.

5.  **Dissenyar la seqüència sense pensar en la fricció de cada fase.** Si totes les fases del projecte tenen el mateix tipus de fricció (o cap), la seqüència és plana. La progressió natural Descoberta → Recursivitat → Resistència ha de ser intencionada.

## Matissos i excepcions

*   **El GRR no sempre és lineal.** Un alumne que domina un tema pot entrar directament a Fase 3 (Vosaltres feu) o Fase 4 (Tu fas). El GRR és una lògica de progressió, no una seqüència rígida.

*   **La bastida progressiva de prompts depèn del domini, no de l'edat.** Un alumne de batxillerat novell en programació pot necessitar prompts-bastida tancats (principiant), mentre que un alumne de FP expert en cuina pot formular prompts avançats per si sol.

*   **No tots els projectes segueixen les 4 fases FJE.** Projectes curts (1-2 setmanes) poden tenir 2-3 fases. La integració IA s'adapta a la durada real, no al model complet.

*   **La instrucció directa (LRI) no és l'enemic.** En fases inicials d'un domini (l'alumne no té esquemes previs), la instrucció directa amb IA que redueix càrrega extrínseca és pedagògicament correcta. La fricció productiva és més efectiva quan ja s'han establert les bases.

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M2_carrega-friccio-cognitiva**: El GRR gradua la fricció productiva; les fases de projecte generen progressió en els moviments de fricció. La CLT determina com gestionar la càrrega a cada fase.
*   **M5_disseny-instruccional-amb-IA**: Operacionalitza aquests models en criteris, auditoria i plantilla. La granularitat didàctica determina la complexitat de la plantilla.
*   **M5_arquitectura-quest-rol-nivell**: La connexió GRR ↔ MIHIA i la seqüència de disseny del docent.
*   **M5_quests-missions-aprenentatge**: Cada tipus de seqüència didàctica té Quests afins.
*   **M5_nivells-delegacio-mihia**: El GRR mapeja directament als nivells MIHIA per fase.
*   **M5_rols-IA-educacio**: Les fases de projecte FJE tenen rols suggerits per fase.
*   **M2_DUA-principis-pautes**: El DUA s'integra amb el GRR per adaptar la seqüència a la diversitat.
*   **M2_ABP-aprenentatge-servei**: Les fases FJE són coherents amb l'ABP.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Com estructuro una unitat didàctica amb IA?"
*   "Quantes sessions necessito per integrar la IA correctament?"
*   "Com graduo la introducció de la IA al llarg del curs?"
*   "Vull fer un projecte amb IA però no sé per on començar."
*   "Com decideixo si una activitat necessita 1 sessió o 3 setmanes?"

**Senyals de l'alumne**
*   L'alumne no entén per què ha de passar per fases "sense IA" en un projecte que inclou IA.
*   L'alumne expressa que "la primera vegada que hem usat la IA no sabia què fer" — mancança de Fase 1.

**Senyals de context**
*   Es planifica un projecte interdisciplinari amb integració de IA.
*   Es dissenya una seqüència didàctica (lineal, cíclica, investigativa) amb IA.
*   Es forma docents sobre com graduar la introducció de la IA.
*   El centre vol un pla de progressió IA per al curs escolar.

**Anti-senyals**
*   El docent ja sap la granularitat i la seqüència que vol. Necessita detalls sobre Q, R o N concrets (activar M5_disseny-instruccional-amb-IA).
*   La consulta és sobre disseny d'avaluació, no de seqüència didàctica.

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha de guiar el docent perquè triï la granularitat, la seqüència i la progressió GRR adequades per a la seva activitat, integrant la IA de manera coherent amb el marc cognitiu.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Determinar la granularitat abans de triar Q, R i N.**
    *   **Quan aplica:** Quan el docent vol integrar IA i no sap si fer un exercici de 15 minuts o un projecte de 3 setmanes.
    *   **Fonament:** La granularitat determina la complexitat de la integració IA. Un exercici de 15 minuts necessita un sol rol i un sol nivell. Un projecte de 3 setmanes necessita un mapa de rols i nivells per fase. Triar Q, R i N sense saber la granularitat genera desajustaments: massa complexitat per a una activitat curta, o massa simplificació per a un projecte llarg.
    *   **Exemple complet de raonament:** Un docent diu: "Vull fer una cosa amb IA sobre el canvi climàtic." L'agent preguntaria primer: "Quant de temps hi vols dedicar?" Si la resposta és "15 minuts", suggerira un exercici amb un sol rol (Generador de Casos: "genera 3 arguments a favor i en contra que l'alumne ha d'avaluar"). Si la resposta és "3 setmanes", suggerira un projecte FJE amb rols per fase i progressió de nivells. La pregunta de granularitat precedeix la seqüència de disseny Q>R>N.

2.  **Heurística: Aplicar el GRR com a pla de curs, no com a sessió aïllada.**
    *   **Quan aplica:** Quan el centre introdueix IA per primera vegada.
    *   **Fonament:** El GRR no s'aplica a una sola activitat sinó a la progressió del curs sencer. Primer trimestre: Jo faig (el docent modela, N0-N1). Segon trimestre: Nosaltres/Vosaltres fem (l'alumnat practica amb guia, N2-N3). Tercer trimestre: Tu fas (autonomia progressiva, N3-N4). Aquesta progressió anual evita el salt directe a N4 que genera rendició cognitiva.
    *   **Exemple complet de raonament:** Un coordinador pedagògic pregunta com introduir la IA al llarg del curs. L'agent proposaria: setembre-novembre, el docent modela (una sessió al mes on el docent projecta la IA i demostra com l'usa). Desembre-febrer, pràctica col·lectiva (activitats en grup amb IA, el docent guia). Març-juny, pràctica progressivament autònoma (primer en parelles, després individual). Al juny, l'alumne ha vist, practicat i consolidat. L'any següent pot començar directament al segon trimestre.

3.  **Heurística: Verificar que cada fase del projecte té la fricció adequada.**
    *   **Quan aplica:** Quan es dissenya un projecte FJE amb integració IA.
    *   **Fonament:** Les fases FJE generen naturalment progressió en els moviments de fricció. La IA no ha de curtcircuitar aquesta progressió. Si la Fase 2 (Investigació) es fa íntegrament amb IA (la IA busca, analitza i contrasta), l'alumne no fa la feina cognitiva de la investigació i la Recursivitat no es produeix.
    *   **Exemple complet de raonament:** Un docent dissenya un projecte sobre sostenibilitat. Fase 1 (Repte): Generador de Casos crea un escenari (Descoberta). ✓ Fase 2 (Investigació): L'alumne investiga sense IA (N0, fonts primàries) i després contrasta amb Mentor Socràtic (N2, preguntes sobre les fonts). Fase 3 (Síntesi): L'alumne escriu la proposta, Crític assenyala febleses (Resistència). ✓ L'agent verificaria especialment la Fase 2: si l'alumne demana a la IA "investiga sobre sostenibilitat", la Recursivitat desapareix. La investigació amb fonts primàries (N0) seguida de contrast socràtic (N2) preserva la fricció.

4.  **Heurística: Retirar la bastida de prompts al llarg del curs.**
    *   **Quan aplica:** Quan el docent prepara els prompts per a l'alumnat.
    *   **Fonament:** El scaffolding temporal implica que el suport es retira progressivament. Al principi del curs, el docent dóna prompts complets. A meitat de curs, dóna l'estructura. Al final, l'alumne formula el seu propi prompt. Aquesta progressió és el GRR aplicat al nivell micro de la interacció amb la IA.
    *   **Exemple complet de raonament:** Setembre: el docent dóna el prompt complet ("Ets un crític de llengua. Llegeix el meu text i assenyala 3 punts febles sense reescriure"). Gener: el docent dóna l'estructura ("Demana a la IA que actuï com a [rol], que revisi [aspecte] i que [restricció]"). Abril: l'alumne escriu el seu propi prompt i el docent valida si és adequat. Juny: l'alumne formula, executa i avalua la interacció autònomament. Cada pas retira una capa de bastida.

5.  **Heurística: Connectar el tipus de seqüència amb la Quest natural.**
    *   **Quan aplica:** Quan el docent ja treballa amb un tipus de seqüència i vol integrar-hi IA.
    *   **Fonament:** Cada tipus de seqüència (lineal, cíclica, investigativa, projecte, flipped, socràtica) té Quests afins. Això permet que el docent trobi la Quest sense canviar la seva metodologia. La taula Seqüència → Quest és el pont entre la pràctica existent del docent i el sistema Q>R>N.
    *   **Exemple complet de raonament:** Un docent de ciències diu: "Jo faig servir seqüències investigatives." L'agent consultaria la taula i mostraria que les Quests afins són Compare i Reverse. El docent tria Compare: "Vull que l'alumne compari la seva hipòtesi amb dades generades per la IA." Rol: Generador de Casos (★★). Nivell: N3 (l'alumne i la IA creen junts un escenari de dades). La seqüència investigativa es manté intacta; la IA s'hi integra a la fase de dades.

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Entendre que les fases "sense IA" tenen un propòsit.**
    *   **Quan aplica:** Quan l'alumne pregunta per què no pot usar la IA a totes les fases d'un projecte.
    *   **Fonament:** Les fases N0 dins d'un projecte preserven la fricció productiva. Si l'alumne investiga sense IA (Fase 2), lluita amb les fonts primàries, activa coneixements previs (Activació de Kapur) i descobreix buits que no hauria vist si la IA li hagués donat un resum (Consciència). La lluita prèvia prepara el terreny perquè la instrucció posterior (o la interacció amb la IA posterior) s'arreli en esquemes ja activats.
    *   **Exemple complet de raonament:** Un alumne diu: "Per què he de buscar informació al llibre si la IA m'ho pot dir en 5 segons?" L'agent li explica: "Buscar al llibre t'obliga a llegir, seleccionar i processar. Això activa el teu cervell per al que ve després. Quan després la IA et faci preguntes sobre el que has trobat (Mentor Socràtic), les sorpreses seran més grans perquè has fet la primera feina tu. Si la IA t'ho diu de bon principi, tot et sembla obvi i no aprens tant."

2.  **Heurística: Reconèixer en quina fase del GRR està.**
    *   **Quan aplica:** Quan l'alumne vol més autonomia amb la IA.
    *   **Fonament:** L'alumne que sap en quina fase del GRR opera pot sol·licitar més autonomia de manera fonamentada: "He vist com el docent usa la IA (Fase 1), he practicat en grup (Fases 2-3), crec que puc provar-ho sol (Fase 4)." Això és metacognició aplicada a la pròpia progressió amb la IA.
    *   **Exemple complet de raonament:** Un alumne diu: "Ja sé usar la IA com a Crític, per què encara em doneu el prompt escrit?" L'agent validaria: "Si pots formular tu sol un prompt que defineixi el rol, l'aspecte a revisar i les restriccions, estàs a nivell avançat de bastida. Demostra-ho: escriu un prompt per a la pròxima activitat i mostra'l al docent. Si funciona, la bastida es retira." L'alumne passa de consumir bastides a demostrar que ja no les necessita.

3.  **Heurística: Adaptar la granularitat al que necessita.**
    *   **Quan aplica:** Quan l'alumne estudia per lliure amb IA.
    *   **Fonament:** Un alumne que vol "fer un repàs ràpid" necessita un exercici (15 min, un sol rol). Un alumne que vol "entendre un tema en profunditat" necessita una tasca (2-3 sessions, progressió de rols). Saber quanta estona dedicar i quin tipus d'interacció triar és una competència metacognitiva.
    *   **Exemple complet de raonament:** Un alumne diu: "Vull estudiar el romanticisme." L'agent preguntaria: "Quant de temps tens i què necessites?" Si 15 minuts: "Escriu el que recordes del romanticisme. Després demana a la IA 3 preguntes per verificar la teva comprensió (Clarity + Mentor Socràtic, N2)." Si 2 hores: "Sessió 1: escriu el que saps i la IA fa preguntes (Clarity, N2). Sessió 2: la IA genera un text romàntic i tu l'analitzes (Reverse, N3). Sessió 3: debat amb la IA sobre si el romanticisme és rellevant avui (Perspective + Contrincant, N3)."

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | Fisher, D. & Frey, N. Gradual Release of Responsibility | file://upload/Fisher_Frey_GRR.pdf |
| 2 | Wiggins, G. & McTighe, J. (1998). Understanding by Design | https://www.ascd.org/books/understanding-by-design |
| 3 | Sweller, J. (1988). Cognitive Load Theory | https://doi.org/10.1207/s15516709cog1202_4 |
| 4 | Martin, A. J. et al. (2025). Load Reduction Instruction | file://upload/Martin_2025_LRI.pdf |
| 5 | ADR Arquitectura Quest-Rol-Nivell (JE, 2026) | file://docs/decisions/arquitectura-quest-rol-nivell.md |
| 6 | Kapur, M. (2008+). Productive Failure | https://doi.org/10.1007/s10339-011-0396-z |

*6 documents font · secció generada manualment*
