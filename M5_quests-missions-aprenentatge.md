---
modul: M5
titol: "10 Quests: missions pedagògiques per a activitats amb IA"
tipus: marc
descripcio: "Les 10 Quests (Khan, Fisher, Frey, Marshall & Hargrave, 2025): concepte de primer nivell que defineix la intenció cognitiva d'una activitat amb IA"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Definició i principis

Una Quest és una **missió pedagògica** que defineix la intenció d'una activitat amb IA. Respon la pregunta del docent: **"Què vull que passi cognitivament en aquesta activitat?"**

Les Quests són el concepte de primer nivell de l'arquitectura Quest-Rol-Nivell (decisió d'arquitectura D, Xat 4, abril 2026). No defineixen com actua la IA (això ho fan els Rols) ni quanta autonomia cedeix l'alumne (això ho fan els Nivells). Defineixen l'objectiu cognitiu.

La posició institucional és **Quest-first**: la pregunta pedagògica correcta és "què ha d'aprendre l'alumne?", no "quina eina vull usar?". Començar pel Rol indueix a *solution looking for a problem*. Començar per la Quest garanteix intencionalitat pedagògica, coherent amb el backward design (Wiggins & McTighe) i el principi d'antropocentrisme del marc general de JE.

### Les 10 Quests

**1. Anchor (Ancoratge)**: Activar coneixements previs i connectar-los amb nous aprenentatges. L'alumne parteix del que ja coneix i la IA ajuda a fer visible la connexió amb el que ha d'aprendre. Fricció: Descoberta (veure relacions que no es veien).

**2. Clarity (Clarificació)**: Aclarir conceptes, corregir malentesos, arribar a comprensió precisa. L'alumne intenta explicar un concepte i la IA l'ajuda a refinar la comprensió. Fricció: Recursivitat (iteració fins que el significat s'estabilitza).

**3. Compare (Comparació)**: Establir semblances, diferències i relacions entre conceptes, teories o fenòmens. La IA genera contraexemples, casos límit o perspectives alternatives que forcen una comparació més profunda. Fricció: Descoberta (buits i matisos emergents).

**4. Critique (Avaluació crítica)**: Avaluar qualitat, coherència, validesa o fiabilitat d'un contingut, argument o producte. L'alumne jutja i la IA actua com a provocadora intel·lectual. Fricció: Resistència (ha de justificar el judici).

**5. Growth (Creixement personal)**: Desenvolupar hàbits metacognitius, autoregulació, resiliència o habilitats socioemocionals. L'alumne reflexiona sobre el seu propi procés d'aprenentatge. Fricció: Descoberta interna (veure's amb més claredat).

**6. Level-Up (Progressió)**: Avançar progressivament en dificultat dins d'un domini, amb reptes calibrats. La IA adapta la dificultat segons el rendiment. Fricció: calibració dins la zona de desenvolupament proper.

**7. Mission (Missió)**: Resoldre un repte complex, autèntic i contextualitzat que requereix mobilitzar múltiples competències. La IA proporciona context, actors o dades. Fricció: Recursivitat (el repte requereix múltiples iteracions).

**8. Perspective (Perspectiva)**: Explorar múltiples punts de vista sobre un tema complex, desenvolupar empatia intel·lectual. La IA encarna posicions o actors que l'alumne no consideraria sol. Fricció: Resistència (dialogar amb perspectives incòmodes).

**9. Reverse (Enginyeria inversa)**: Descompondre un producte, argument o solució per entendre com funciona per dins. La IA proporciona el producte; l'alumne ha de desfer-lo. Fricció: Descoberta (el mecanisme intern es fa visible).

**10. Right-Sizing (Ajustament)**: Adaptar un contingut, producte o solució a un context, audiència o necessitat específica. L'alumne pren les decisions sobre què canviar i per què. Fricció: judici selectiu (què és essencial i què accessori).

### Matriu d'afinitats Quest × Rol

Cada Quest admet un subconjunt de Rols. La correspondència és una matriu dispersa d'afinitats (no 1:1 ni N:N pur):

| | Mentor S. | Simulador | Crític/Ed. | Gen.Casos | Teach.Ag. | Contrinc. | Traductor |
|---|---|---|---|---|---|---|---|
| Anchor | ★★ | — | — | ★ | ★★ | — | — |
| Clarity | ★★ | — | ★ | — | ★★ | — | — |
| Compare | ★ | — | ★ | ★★ | — | — | — |
| Critique | ★ | — | ★★ | — | — | ★★ | — |
| Growth | — | — | ★★ | ★ | — | ★ | — |
| Level-Up | — | ★ | — | ★★ | — | — | ★ |
| Mission | — | ★★ | — | ★ | — | — | — |
| Perspective | ★ | ★★ | — | — | — | ★★ | ★ |
| Reverse | ★ | — | ★ | ★ | ★★ | — | — |
| Right-Sizing | — | — | — | ★ | — | — | ★★ |

★★ = nadiu (combinació natural), ★ = possible, — = forçat o incoherent. Les combinacions amb "—" no haurien de constar al catàleg d'assistents.

### Quest × Moviment de fricció × Càrrega × ICAP

| Quest | Moviment de fricció | Càrrega que externalitza | Mode ICAP esperat |
|---|---|---|---|
| Anchor | Descoberta | Extrínseca (organització) | Constructive |
| Clarity | Recursivitat | Extrínseca (formulació) | Interactive |
| Compare | Descoberta | Extrínseca (cerca de casos) | Constructive |
| Critique | Resistència | Cap o extrínseca | Interactive |
| Growth | Descoberta (interna) | — | Constructive |
| Level-Up | Recursivitat | Extrínseca (generació d'exercicis) | Active → Constructive |
| Mission | Recursivitat | Extrínseca (context, dades) | Interactive |
| Perspective | Resistència | Extrínseca (encarnació) | Interactive |
| Reverse | Descoberta | Extrínseca (producte a analitzar) | Constructive |
| Right-Sizing | Judici (selectiu) | Extrínseca (adaptació tècnica) | Constructive |

## Autors i evidència clau

*   **Khan, S., Fisher, D., Frey, N., Marshall, H. W. & Hargrave, A. (2025)**: Proposta original de les 10 Quests com a missions pedagògiques per a activitats amb IA generativa. Les Quests deriven del marc de *Rigorous Curriculum Design* i del *Gradual Release of Responsibility* de Fisher & Frey, adaptats a l'era de la IA.
*   **Wiggins, G. & McTighe, J. (1998)**: *Understanding by Design* (backward design). La lògica Quest-first és coherent amb el principi de partir de l'objectiu d'aprenentatge i treballar cap enrere.
*   **Mollick, E. (2023)**: Els 7 rols d'interacció amb IA. La matriu Quest × Rol estableix la relació entre les missions pedagògiques i els rols de la IA.
*   **Novokshanova, E. (2025)**: Fricció productiva. La columna "Moviment de fricció" de la taula Quest × Fricció × ICAP es fonamenta en els tres moviments (Descoberta, Recursivitat, Resistència).
*   **Chi, M. T. H. & Wylie, R. (2014)**: ICAP. La columna "Mode ICAP esperat" mesura el grau d'implicació cognitiva.

## Exemples concrets d'aplicació a l'aula

1.  **Quest Anchor (Ciències, 2n ESO)**: Abans de començar el tema de genètica, cada alumne escriu en 5 minuts tot el que recorda sobre herència (pre-compromís). Després pregunta a la IA: "Quines connexions veus entre el que he escrit i el concepte de gen?" La IA assenyala relacions que l'alumne no havia vist (Descoberta). L'alumne reelabora el seu esquema inicial. Rol: Mentor Socràtic (★★). Nivell: N2.

2.  **Quest Critique (Història, 2n Batxillerat)**: L'alumne llegeix un article sobre la caiguda de l'Imperi Romà. Identifica 3 arguments febles. Envia els seus 3 arguments a la IA: "Defensa els punts que jo he criticat." L'alumne ha de respondre refutant la defensa. Rol: Contrincant (★★). Nivell: N3. Moviment: Resistència. Mode ICAP: Interactive.

3.  **Quest Mission (FP Grau Superior, Integració Social)**: La IA simula "Marta, 34 anys, mare sola, a punt de ser desnonada". L'alumne ha de conduir l'entrevista d'acollida completa (15-20 preguntes), gestionar emocions simulades, proposar recursos. Rol: Simulador (★★). Nivell: N2. Moviment: Recursivitat (ha d'adaptar preguntes segons respostes).

## Errors comuns — què NO fer

1.  **Confondre la Quest amb el tema curricular.** La Quest no és "fer un treball sobre el canvi climàtic". La Quest defineix el procés cognitiu: Critique (avaluar un argument sobre canvi climàtic), Compare (comparar dues polítiques climàtiques), Perspective (explorar el tema des del punt de vista d'un agricultor, un polític i un científic). Un mateix tema pot vehicular Quests molt diferents.

2.  **Triar la Quest després del Rol.** Si el docent decideix primer "vull usar un Simulador" i després busca quina Quest serveix, el disseny és incoherent amb l'arquitectura Quest-first. La Quest defineix la intenció; el Rol la implementa. La doble entrada (per Quest o per Rol) és una concessió d'interfície, no d'arquitectura.

3.  **Assignar una Quest sense verificar la matriu Quest × Fricció × ICAP.** Si la Quest és Critique (Resistència, Interactive) però l'activitat dissenyada posa l'alumne en mode Passiu (llegeix un text crític generat per la IA), la Quest no s'ha implementat correctament. El mode ICAP esperat ha de coincidir amb el real.

4.  **Usar una Quest amb un Rol incoherent.** Quest Right-Sizing + Contrincant no funciona: la Quest demana ajustament a audiència i el Rol contradiu. Verificar la matriu d'afinitats abans de configurar l'activitat.

5.  **No connectar la Quest amb el marc cognitiu.** Cada Quest ha d'associar-se a un moviment de fricció, una càrrega externalitzada i un mode ICAP. Sense aquesta connexió, la Quest és un nom bonic però no un instrument de disseny.

## Matissos i excepcions

*   **Nombre definitiu de Quests.** Les 10 de Khan/Fisher/Frey podrien consolidar-se a 6-7. Algunes Quests (Growth, Level-Up) tenen un solapament parcial. La decisió de consolidar queda pendent.

*   **Quests compostes.** Una activitat complexa pot combinar dues Quests seqüencialment: Anchor → Critique (primer activa coneixements previs, després avalua críticament). Però cada moment de l'activitat ha de tenir una Quest dominant clara.

*   **Quest Level-Up i el mode ICAP.** Level-Up comença en mode Active (l'alumne resol exercicis) i pot pujar a Constructive (l'alumne dissenya exercicis per a companys). El mode ICAP no és fix sinó que progressa.

*   **La doble entrada és real.** Tot i que el marc és Quest-first, molts docents ja coneixen els Rols (Mollick és àmpliament difós). Negar-los l'entrada per Rol seria contraproduent. La interfície d'ús permet entrar per Rol → veure Quests compatibles → triar Nivell.

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M5_arquitectura-quest-rol-nivell**: Les Quests són el concepte de primer nivell de l'arquitectura Q>R>N. La seqüència de disseny del docent comença per triar la Quest (pas 1).
*   **M5_rols-IA-educacio**: La matriu Quest × Rol determina quins rols serveixen cada Quest. La doble entrada permet accedir al sistema des dels Rols.
*   **M5_nivells-delegacio-mihia**: Cada combinació (Quest, Rol) té un rang de Nivells nadiu. El rang efectiu és la intersecció del rang nadiu amb el sostre d'etapa.
*   **M2_carrega-friccio-cognitiva**: Cada Quest s'associa a moviment de fricció, càrrega externalitzada i mode ICAP. El marc cognitiu fonamenta la taula Quest × Fricció × ICAP.
*   **M5_disseny-instruccional-amb-IA**: Les Quests són el punt de partida del pas 1 de la plantilla de disseny.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Què vull que passi cognitivament quan els meus alumnes usin la IA?"
*   "Tinc un objectiu d'aprenentatge clar però no sé com integrar-hi la IA."
*   "Vull que els alumnes comparin, critiquin, explorin perspectives... no que la IA els ho faci."
*   "Conec els rols de Mollick però no sé quan usar cada un."
*   "Com decideixo entre un Simulador i un Mentor Socràtic per a aquesta activitat?"

**Senyals de l'alumne**
*   L'alumne pregunta "per a què serveix la IA en aquesta activitat?" — necessita entendre la Quest.
*   L'alumne usa la IA de manera genèrica sense un objectiu cognitiu definit.

**Senyals de context**
*   Es dissenya una nova activitat amb IA i cal definir la intenció pedagògica.
*   Es revisa el catàleg d'assistents institucionals per verificar coherència Quest × Rol.
*   Es forma docents sobre integració de la IA i cal un vocabulari pedagògic compartit.

**Anti-senyals**
*   El docent ja ha definit clarament l'objectiu cognitiu i sap exactament quin rol vol. No cal passar per les 10 Quests si la intenció ja és clara.
*   La consulta és sobre aspectes tècnics de la IA, no sobre disseny pedagògic.

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha d'ajudar el docent a identificar la Quest adequada per al seu objectiu d'aprenentatge i verificar que la combinació Quest × Rol × Nivell genera fricció productiva.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Traduir l'objectiu d'aprenentatge a una Quest.**
    *   **Quan aplica:** Quan el docent expressa un objectiu d'aprenentatge sense vocabulari de Quests.
    *   **Fonament:** Les Quests codifiquen processos cognitius (comparar, criticar, explorar perspectives, ajustar) que el docent ja coneix però potser no anomena d'aquesta manera. El backward design (Wiggins & McTighe) estableix que el punt de partida és l'objectiu, no l'activitat. La Quest fa de pont entre l'objectiu i el disseny de la interacció amb IA.
    *   **Exemple complet de raonament:** Un docent de llengua diu: "Vull que els alumnes millorin els seus textos argumentatius." L'agent analitzaria el verb: "millorar" pot significar coses molt diferents. Si vol que detectin febleses en els seus propis textos, la Quest és Critique. Si vol que comparin el seu text amb un text model, és Compare. Si vol que els adaptin a una audiència diferent (per exemple, escriure per a alumnes de primària), és Right-Sizing. L'agent preguntaria al docent: "Què vols que passi cognitivament? Que l'alumne jutgi el seu text (Critique), que el compari amb un referent (Compare) o que l'adapti a un destinatari (Right-Sizing)?" La resposta determina la Quest, i la Quest determina el Rol.

2.  **Heurística: Verificar la coherència Quest × Moviment de fricció × Mode ICAP.**
    *   **Quan aplica:** Quan s'ha triat una Quest i cal comprovar que el disseny de l'activitat és coherent.
    *   **Fonament:** Cada Quest espera un moviment de fricció dominant i un mode ICAP mínim. Si la Quest és Critique (Resistència, Interactive) però l'activitat situa l'alumne en mode Passiu, el disseny falla. La taula Quest × Fricció × ICAP és l'eina de verificació.
    *   **Exemple complet de raonament:** Un docent tria la Quest Perspective i proposa que la IA generi un text amb múltiples perspectives que l'alumne llegeixi. L'agent diagnosticaria que el mode ICAP és Passiu (l'alumne llegeix, no interactua). La Quest Perspective espera Interactive (l'alumne dialoga amb perspectives incòmodes). Suggerira reformular: la IA encarna un personatge (Simulador) i l'alumne hi dialoga, després la IA canvia de personatge i l'alumne ha de trobar punts de consens. Ara el mode és Interactive i el moviment és Resistència.

3.  **Heurística: Usar la doble entrada per respectar la diversitat docent.**
    *   **Quan aplica:** Quan el docent ja coneix els Rols de Mollick i vol entrar al sistema des d'allà.
    *   **Fonament:** Tot i que la posició institucional és Quest-first, molts docents ja tenen experiència amb rols concrets. L'ADR Xat 4 estableix explícitament la doble entrada com a concessió d'interfície. Negar l'entrada per Rol seria contraproduent i generaria resistència innecessària.
    *   **Exemple complet de raonament:** Un docent diu: "Vull usar un Simulador perquè els alumnes practiquin anglès." L'agent no l'obligaria a repensar-ho en termes de Quests, sinó que partiria del Rol triat i mostraria les Quests compatibles: Mission (★★, resoldre un repte en context simulat), Perspective (★★, explorar punts de vista d'un personatge), Level-Up (★, pràctica progressiva). Preguntaria: "Vols que practiquin resolent un problema (Mission), explorant perspectives (Perspective) o avançant en dificultat (Level-Up)?" La resposta completa la tríada Q-R-N.

4.  **Heurística: Filtrar combinacions incoherents amb la matriu d'afinitats.**
    *   **Quan aplica:** Quan el docent proposa una combinació Quest-Rol que és forçada.
    *   **Fonament:** La matriu dispersa d'afinitats indica quines combinacions són nadiues (★★), possibles (★) o forçades (—). Les combinacions forçades generen activitats on la IA no serveix la intenció pedagògica.
    *   **Exemple complet de raonament:** Un docent proposa Quest Anchor (activar previs) + Contrincant (contradiu l'alumne). L'agent assenyalaria que la combinació és "—" a la matriu: Anchor busca connexions entre el que l'alumne sap i el que ha d'aprendre, i un Contrincant que contradiu no ajuda a fer emergir connexions sinó a defensar posicions. Suggerira Mentor Socràtic (★★, fa preguntes que revelen connexions) o Teachable Agent (★★, l'alumne intenta explicar el que sap i la IA fa emergir buits). La Quest es manté, el Rol canvia a un de compatible.

5.  **Heurística: Connectar el tipus de seqüència didàctica amb la Quest natural.**
    *   **Quan aplica:** Quan el docent ja té un tipus de seqüència definit i vol integrar-hi IA.
    *   **Fonament:** Cada tipus de seqüència didàctica (lineal, cíclica, investigativa, projecte, flipped, socràtica) té Quests afins. Per exemple, una seqüència socràtica és naturalment Critique o Perspective; una seqüència investigativa és Compare o Reverse. Això permet al docent que ja treballa amb un tipus de seqüència trobar la Quest sense canviar la seva metodologia.
    *   **Exemple complet de raonament:** Un docent de ciències ja fa servir seqüències investigatives (pregunta → hipòtesi → dades → conclusió). L'agent li mostraria que les Quests afins són Compare (comparar hipòtesi amb dades) i Reverse (descompondre un resultat per entendre el mecanisme). Si l'alumne formula una hipòtesi i després la IA li dóna dades que la contradiuen, la Quest és Compare i el Rol és Generador de Casos (★★). La seqüència investigativa es manté intacta, amb IA integrada a la fase de dades.

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Preguntar-se "què vull que passi al meu cap?" abans d'obrir la IA.**
    *   **Quan aplica:** Quan l'alumne va a interactuar amb la IA i no té clar l'objectiu.
    *   **Fonament:** La competència D1 (Delegació) del Model 4D comença per decidir per a què usar la IA. Sense intenció, la interacció tendeix cap a la delegació passiva. La Quest, traduïda a llenguatge d'alumne, és: "vull entendre millor?" (Clarity), "vull comparar?" (Compare), "vull practicar?" (Level-Up), "vull veure-ho des d'un altre punt de vista?" (Perspective).
    *   **Exemple complet de raonament:** Un alumne obre la IA per estudiar un tema d'història. L'agent li preguntaria: "Què vols aconseguir? Si vols entendre millor un concepte, demana a la IA que et faci preguntes (Clarity + Mentor Socràtic). Si vols veure el tema des de perspectives diferents, demana-li que encari un personatge (Perspective + Simulador). Si vols practicar per a l'examen, demana-li exercicis (Level-Up + Generador de Casos)." La tria conscient de la intenció canvia radicalment la qualitat de la interacció.

2.  **Heurística: Reconèixer que "la IA m'ho ha fet" no és la mateixa Quest que "he après amb la IA".**
    *   **Quan aplica:** Quan l'alumne ha acabat una interacció amb la IA i ha de valorar-ne el resultat.
    *   **Fonament:** La paradoxa del rendiment (Bastani et al., 2025) demostra que el producte pot ser excel·lent i l'aprenentatge nul. L'alumne que reconeix la diferència exerceix metacognició (judici avaluatiu, Tai et al., 2018). La pregunta clau de Macnamara aplica aquí: "si faig això 10 vegades, milloraré jo o millorarà el producte?"
    *   **Exemple complet de raonament:** Un alumne ha demanat a la IA que li generi 3 arguments a favor del feminisme per a un debat. Té un producte excel·lent. L'agent li preguntaria: "Has millorat tu com a argumentador o tens 3 arguments que no has pensat tu?" Si la resposta és la segona, suggerira canviar de Quest: en lloc de generar (productiu), criticar el que la IA ha generat (Critique) o defensar la posició contrària (Perspective). Ara l'alumne fa feina cognitiva amb el material, no el consumeix.

3.  **Heurística: Triar la Quest segons el que necessita aprendre, no segons el que vol entregar.**
    *   **Quan aplica:** Quan l'alumne vol usar la IA per completar una tasca ràpidament.
    *   **Fonament:** La distinció rendiment vs. aprenentatge (Soderstrom & Bjork, 2015) aplica directament: l'alumne que tria la Quest pensant en l'entrega optimitza rendiment; l'alumne que la tria pensant en el que vol aprendre optimitza aprenentatge. La IA facilita ambdues coses, però només la segona construeix esquemes duradors.
    *   **Exemple complet de raonament:** Un alumne ha de fer un treball comparatiu sobre dos sistemes econòmics. Per entregar ràpid, demanaria a la IA "compara capitalisme i socialisme" (delegació, N4). Per aprendre, faria primer la seva comparació (pre-compromís), la IA li generaria un tercer sistema (Generador de Casos, Quest Compare) perquè trobés patrons comuns, i l'alumne reelaboraria la seva comparació amb el nou punt de vista. El producte final potser és menys polit, però l'alumne ha construït un esquema comparatiu que retendrà.

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | Khan, S., Fisher, D., Frey, N., Marshall, H. W. & Hargrave, A. (2025). Teaching with AI | file://upload/Khan_Fisher_Frey_2025_TeachingWithAI.pdf |
| 2 | Wiggins, G. & McTighe, J. (1998). Understanding by Design | https://www.ascd.org/books/understanding-by-design |
| 3 | Mollick, E. (2023). Assigning AI: Seven Approaches | https://www.oneusefulthing.org/p/assigning-ai-seven-approaches-for |
| 4 | Novokshanova, E. (2025). Productive Friction | file://upload/Novokshanova_2025_ProductiveFriction.pdf |
| 5 | Chi, M. T. H. & Wylie, R. (2014). ICAP Framework | https://doi.org/10.1080/00461520.2014.965823 |
| 6 | ADR Arquitectura Quest-Rol-Nivell (JE, 2026) | file://docs/decisions/arquitectura-quest-rol-nivell.md |

*6 documents font · secció generada manualment*
