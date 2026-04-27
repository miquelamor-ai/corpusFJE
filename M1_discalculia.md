---
modul: M1
titol: "Discalcúlia"
tipus: caracteristica
subtipus: constitutiva
descripcio: "Discalcúlia: trastorn específic de l'aprenentatge en matemàtiques, models Triple Code (Dehaene) i sentit numèric (Butterworth), subtipus procedimental/verbal/visuoespacial (Geary), progressió CPA, ansietat matemàtica i adaptacions per grau"
review_status: esborrany
generat_at: 2026-04-27T00:00:00
variables_configurables:
  - nom: subtipus_principal
    etiqueta: "Subtipus principal (Geary)"
    tipus: enum
    valors: [procedural, verbal, visuoespacial, mixt]
    obligatori: true
    defecte: procedural
    descripcio: "Procedural: dificultat en algoritmes i seqüència d'operacions. Verbal: no recupera fets aritmètics de la memòria (taules). Visuoespacial: errors d'alineament, confusió valor posicional. Mixt: dos o més subtipus actius simultàniament"
    impacte: "Procedural: fragmentar cada algoritme en passos explícits numerats. Verbal: proporcionar taules i fórmules; no exigir recuperació de memòria. Visuoespacial: usar graelles alineades, codis de color per columnes. Mixt: combinar les tres estratègies"
  - nom: grau
    etiqueta: "Grau de severitat"
    tipus: enum
    valors: [lleu, moderat, sever]
    obligatori: true
    defecte: moderat
    descripcio: "Lleu: compensable amb suport puntual. Moderat: necessita suport sistemàtic d'estructura i representació. Sever: dificultats persistents; requereix material manipulatiu i representació concreta (fase C de CPA)"
    impacte: "Lleu: estructura clara, problemes d'un sol pas. Moderat: CPA sistemàtic, taules proporcionades, problemes fragmentats. Sever: representació concreta i pictòrica; prescindir de notació abstracta quan sigui possible"
  - nom: ansietat_matematica
    etiqueta: "Ansietat matemàtica present"
    tipus: boolean
    obligatori: false
    defecte: false
    descripcio: "Resposta d'estrès fisiològicament mesurable davant tasques numèriques: bloqueig, evitació, rendiment disminuït fins i tot en tasques possibles. Afecta la memòria de treball disponible durant el càlcul (Ashcraft & Krause, 2007)"
    impacte: "Si sí: framing neutre ('explora' i 'comprova' en lloc de 'calcula' i 'resol'); eliminar pressió temporal; validar estratègies no convencionals; primer èxit petit i assequible abans d'incrementar la complexitat"
  - nom: memoria_treball_afectada
    etiqueta: "Memòria de treball visuoespacial significativament afectada"
    tipus: boolean
    obligatori: false
    defecte: false
    descripcio: "La memòria de treball visuoespacial és especialment crítica en aritmètica. Quan és deficient, l'alumne perd el fil en problemes multi-pas i l'algoritme es desfà a mig camí (Baddeley, 2000)"
    impacte: "Si sí: externalitzar la memòria de treball — proporcionar la cadena de passos visible i permanent durant la tasca; limitar a 2-3 elements simultanis; escriure cada pas intermedi de manera explícita"
---

### 1. CONTINGUT ESPECÍFIC

#### Descripció del tret

##### Definició i base neurobiològica

La discalcúlia és un trastorn específic de l'aprenentatge de base neurobiològica que afecta l'adquisició i el processament de les habilitats matemàtiques. El **DSM-5-TR** la classifica com a "Trastorn específic de l'aprenentatge amb dificultat en matemàtiques" (*Specific Learning Disorder with impairment in mathematics*, SLD-M), i l'**ICD-11** com a "Trastorn del desenvolupament de l'aprenentatge amb dificultat en matemàtiques" (6A03.2).

Els criteris diagnòstics centrals (DSM-5-TR / ICD-11):
- Rendiment matemàtic significativament per sota del nivell esperat per edat, instrucció rebuda i nivell d'intel·ligència general
- Les dificultats persisteixen malgrat la instrucció adequada i continuada
- Afecten significativament el funcionament acadèmic o de la vida quotidiana
- No s'expliquen millor per altres trastorns ni per discapacitats sensorials o intel·lectuals

La **base neurobiològica** es localitza principalment al **solc intraparietal (IPS)**, regió cortical implicada en la representació de la magnitud numèrica. Estudis de neuroimatge (fMRI) mostren consistentment una reducció d'activació bilateral de l'IPS en individus amb discalcúlia durant tasques de comparació numèrica, fins i tot les més simples. La connexió entre l'IPS i les regions prefrontals —implicades en la memòria de treball— és menor en persones amb discalcúlia, el que explica la dificultat per mantenir i manipular informació numèrica mentalment.

##### Prevalença i perfil

- Afecta aproximadament el **3-7% de la població** en edat escolar, depenent dels criteris diagnòstics
- Distribució similar en nens i nenes (el biaix masculí clàssic respon a biaixos de derivació)
- **Alta comorbiditat**: ~40-60% amb dislèxia, ~30-40% amb TDAH, freqüent solapament amb trastorn del desenvolupament de la coordinació (TDC)
- La discalcúlia **coexisteix amb capacitats intel·lectuals normals o altes** — no és baixa intel·ligència

##### Models teòrics fonamentals

**Model del Triple Codi (Dehaene, 1992/2011)**

Stanislas Dehaene proposa que els humans representem els nombres en tres formats corticals independents:

| Representació | Àrea cortical | Funció | Vulnerable a discalcúlia? |
|---|---|---|---|
| **Magnitud analògica** (línia mental dels nombres) | IPS bilateral | Comparar, aproximar, estimar | ✅ Sí — nucli del trastorn |
| **Forma visual aràbiga** (1, 2, 3...) | Còrtex occipitotemporal | Reconèixer i llegir xifres | ✅ Parcialment — subtipus visuoespacial |
| **Paraules numèriques** ("un", "dos"...) | Perisylvian esquerre | Recuperar fets aritmètics verbals | ✅ Parcialment — subtipus verbal |

La discalcúlia afecta principalment la representació de **magnitud analògica** (la "línia mental dels nombres"), el que explica per què l'alumne no "sent" intuïtivament que 97 és gairebé 100, o que 1/4 és menor que 1/3.

**Hipòtesi del Dèficit de Sentit Numèric (Butterworth, 1999/2019)**

Brian Butterworth postula que la discalcúlia es deu a un dèficit nuclear en el **sistema numèric nuclear** (*core number system*): la capacitat innata d'enumerar i comparar petites quantitats. El **subitizing** —reconeixement immediat d'1 a 4 objectes sense comptar— és un marcador precoç i robust de discalcúlia. Sense un sentit numèric sòlid com a fonament, l'aritmètica resta un conjunt de procediments memoritzats sense comprensió de magnitud: fràgils, lents i propensos a errors.

**Subtipus de Geary (1993/2004)**

David Geary descriu tres perfils cognitius diferenciats, que sovint coexisteixen:

| Subtipus | Descripció | Senyal típic a l'aula |
|---|---|---|
| **Procedimental** | Dificultat per executar algoritmes (suma amb portada, divisió). Comptar-ho tot des del principi | Usa els dits quan els iguals ja no els necessiten |
| **Recuperació verbal** | No recupera fets aritmètics de la memòria a llarg termini (taules de multiplicar) | "Tres per quatre" → no sap, no fa estimació; errors aleatoris |
| **Visuoespacial** | Dificultat en la representació espacial dels nombres: alineació de columnes, valor posicional, fraccions | Suma la columna equivocada; "52" escrit com "25" |

**Progressió CPA (Bruner, adaptat per matemàtiques inclusives)**

La progressió Concret → Pictòric → Abstracte és el marc pedagògic amb evidència més robusta per a la discalcúlia (National Council of Teachers of Mathematics, NCTM; What Works Clearinghouse):
- **C (Concret)**: manipulació d'objectes físics (blocs, àbac, monedes, regletes Cuisenaire)
- **P (Pictòric)**: representació visual (diagrames de barres, línies numèriques, dibuix d'agrupaments)
- **A (Abstracte)**: notació simbòlica estàndard (xifres i símbols +, −, ×, ÷)

L'alumne amb discalcúlia necessita un temps significativament superior a les fases C i P, i no s'ha de forçar el salt a A fins que la comprensió conceptual estigui consolidada en els nivells anteriors.

**Memòria de treball (Baddeley, 1986/2000)**

La discalcúlia coexisteix freqüentment amb dèficits de la **memòria de treball visuoespacial** (l'agenda visuoespacial del model de Baddeley), crítica per mantenir xifres en ment durant el càlcul, per alinear columnes i per seguir algoritmes multi-pas. Quan la memòria de treball és deficient, les estratègies compensatòries —escriure els passos intermedis, usar calculadora— no són "trampes" sinó adaptacions legítimes i necessàries.

#### Manifestació per etapa educativa

| Etapa | Matemàtiques | Altres àrees | Impacte emocional |
|-------|-------------|--------------|-------------------|
| **Infantil (I3–I5)** | Dificultat en subitizing (no reconeix 3 daus sense comptar); recomptes inestables; no ordena quantitats petites de manera fiable | — | — |
| **Primària (1r–3r)** | Compta des del 1 quan els iguals compten des del nombre gran; errors persistents en suma i resta; no automatitza la taula de l'1 | Dificultat amb rellotges, calendaris, seqüències temporals | Frustració creixent, vergonya |
| **Primària (4t–6è)** | Algoritmes (multiplicació de dues xifres, divisió) fràgils o impossibles; fraccions opaces; errors de valor posicional freqüents | Gràfiques i estadística bàsica, mesures, escales | Evitació de tasques matemàtiques, baixa autoestima |
| **ESO** | No automatitza operacions: cada problema de primer pas ocupa tota l'atenció; àlgebra molt difícil; proporcionalitat opaca | Física (fórmules), economia, música (fraccions de compàs) | Síndrome de l'impostor, convicció de "ser dolent en mates" |
| **Batxillerat/FP** | Funcions, càlcul, estadística: errors sistemàtics; dificultat de transferència de procediments nous | Ciències experimentals, tecnologia, comptabilitat (FP) | Por a exàmens, bloqueig, possible abandó de línies científiques |

#### Barreres d'aprenentatge

*   **Sentit numèric (magnitud):** Dificultat per accedir intuïtivament a la representació de magnitud. L'alumne no "sent" que 8 és força menys que 100, o que 0,5 és la meitat. Barrera nuclear que impacta tota la matemàtica.
*   **Procedimental:** No automatitza algoritmes: cada operació requereix la reconstitució completa del procediment, esgotant la memòria de treball. Usar els dits en etapes en què els iguals ja no ho fan és el senyal extern més visible.
*   **Visuoespacial:** Dificultat per organitzar xifres a l'espai (alineació, valor posicional, descomposició de nombres). Errors d'escriptura en mirall ("52" → "25"), confusió de columnes (desenes per unitats).
*   **Recuperació verbal:** No recupera fets aritmètics bàsics (fets de suma fins a 20, taules de multiplicar) de la memòria a llarg termini. No és "no estudiar-les": la ruta de recuperació verbal és estructuralment fràgil.
*   **Emocional — Ansietat matemàtica:** Resposta d'estrès fisiològicament mesurable davant les matemàtiques (Ashcraft & Krause, 2007; Beilock & Maloney, 2015). L'ansietat ocupa recursos de la memòria de treball, creant un cercle viciós: ansietat → rendiment pitjor → confirmació del fracàs → més ansietat.

#### Necessitats prioritàries

1. **Instrucció basada en la comprensió (CPA)**: No accelerar cap a l'abstracte. Consolidar la comprensió de la magnitud amb materials manipulatius (blocs multibase, àbac, línia numèrica física) abans de passar al simbòlic.
2. **Externalització de la memòria de treball**: Proporcionar taules aritmètiques de referència, permet calculadora en les fases de consolidació conceptual, escriure els passos intermedis dels algoritmes de manera explícita.
3. **Mapeig explícit procediment → concepte**: Connectar cada algoritme amb la seva representació CPA corresponent; l'alumne ha d'entendre *per què* funciona, no només *com* s'executa.
4. **Reducció de l'ansietat matemàtica**: Framing de tasques com a exploració, no avaluació; errors com a dades, no fracassos; primers èxits assequibles per trencar el cicle negatiu.
5. **Adaptació d'avaluació**: Permetre l'ús de taules, calculadora i paper de treball. Puntuar el raonament i la comprensió de la magnitud per sobre de la fluïdesa de càlcul.

#### Fortaleses a aprofitar

*   Raonament verbal i comprensió oral sovint preservats o superiors (canal de compensació natural)
*   Pensament narratiu: comprenen problemes millor quan s'expliquen en context real i significatiu
*   Habilitats espacials globals (diferent del processament numèric-espacial concret afectat)
*   Creativitat i resolució de problemes no rutinaris quan la càrrega de càlcul és baixa
*   Alta motivació quan les estratègies d'externalització eliminen la barrera i experimenten l'èxit

#### Senyals identificadors a l'aula

**Senyals d'alarma precoç (Infantil/1r Primària):**
*   No reconeix immediatament grups de 2-3 elements (dificultat subitizing)
*   Recomptes inestables: "1, 2, 3, 4, 3, 5..."
*   No compara quantitats petites sense comptar un a un
*   No estableix correspondència un a un de manera precisa i consistent

**Senyals consolidats (Primària–ESO):**
*   Usa els dits per a operacions que els iguals resolen de memòria
*   Errors de valor posicional: confon desenes i unitats, inverteix xifres
*   Taules de multiplicar: no automatitzades malgrat pràctica repetida i intensiva
*   Errors d'alineació en operacions escrites (suma la columna equivocada)
*   No detecta que un resultat és clarament impossible (p.ex. 1000 × 5 = 50)
*   Gran discrepància entre comprensió verbal d'un problema i capacitat d'execució del càlcul

**Anti-senyals (que no apunten a discalcúlia):**
*   Dificultats úniques en problemes de text però no en operacions bàsiques (pot ser barrera lèxica, no numèrica)
*   Errors aritmètics puntuals per distracció o descuit, no sistemàtics ni coherents
*   Millora ràpida i sostinguda amb instrucció addicional ordinària
*   Dificultats aparegudes recentment i sense historial de dificultat en comptar o comparar quantitats

#### Perfils associats i comorbiditats

*   **Discalcúlia + Dislèxia**: Comorbiditat estimada en un 40-60% dels casos. Comparteixen dèficits en processament simbòlic (lletres i números) i memòria fonològica. La doble barrera és especialment aclaparadora en problemes de text matemàtic. Veure M1_dislexia-dificultats-lectores.md.
*   **Discalcúlia + TDAH**: Comorbiditat ~30-40%. La impulsivitat en l'execució d'algoritmes i el dèficit de memòria de treball s'amplifiquen mutuament. Veure M1_TDAH.md i creuament a M1_creuament-variables-dependencies.md.
*   **Discalcúlia + TEA**: Perfil heterogeni: alguns alumnes amb TEA mostren habilitats numèriques superiors (pensament sistemàtic), d'altres presenten discalcúlia comòrbida. Cal avaluació individual. Veure M1_alumnat-TEA.md.
*   **Discalcúlia + Trastorn del desenvolupament de la coordinació (TDC)**: El subtipus visuoespacial de la discalcúlia sol coexistir amb dispraxia. Veure M1_trastorn-coordinacio-dispraxia.md.
*   **Discalcúlia + Ansietat matemàtica**: Pot existir ansietat matemàtica sense discalcúlia (per experiències negatives) i discalcúlia sense ansietat (quan s'ha tingut bon suport). La coexistència és freqüent i s'autoreforça.

#### Principis d'actuació

*   **Adaptar continguts:** Simplificar la càrrega de càlcul sense simplificar el raonament. Proporcionar les dades numèriques necessàries (taules, fórmules) perquè l'alumne pugui centrar-se en el concepte. No confondre discalcúlia amb baixa capacitat intel·lectual: raonar matemàticament i calcular són habilitats diferents.
*   **Adaptar activitats:** Prioritzar la fase concreta i pictòrica (CPA). Permetre estratègies no convencionals si condueixen al resultat correcte (p.ex. sumar xifra per xifra en lloc de memoritzar la taula). Fraccionar problemes complexos en sub-tasques seqüenciades i explícites.
*   **Adaptar avaluació:** Permetre l'ús de materials de suport (taules, calculadora) en les fases de consolidació conceptual. Valorar el raonament i la comprensió de la magnitud per sobre de la fluïdesa de càlcul. Donar temps addicional, especialment si hi ha ansietat matemàtica.
*   **Adaptar interacció:** Activar les variables configurables (subtipus, grau, ansietat, memòria de treball). Evitar la pressió temporal visible (cronòmetre, valoració de la rapidesa). Framing positiu: "Com pots comprovar que aquest resultat té sentit?" en lloc de "Quant és 7 × 8?"

#### Línies vermelles

*   **No diagnosticar discalcúlia** basant-se en errors aritmètics puntuals o manca d'estudi de les taules. **Per què?** La discalcúlia és un trastorn diagnòstic que requereix avaluació especialitzada (psicòleg educatiu, neuropsicòleg). Errors puntuals o per manca d'instrucció no constitueixen discalcúlia.
*   **No atribuir les dificultats a manca d'esforç o "no li agraden les mates".** **Per què?** La discalcúlia és de base neurobiològica. L'esforç de l'alumne per fer un càlcul senzill pot ser enorme i completament invisible.
*   **No eliminar les matemàtiques: adaptar el canal, no el contingut.** **Per què?** L'alumne amb discalcúlia pot comprendre conceptes matemàtics complexos si s'elimina la barrera del càlcul. La temptació de simplificar el contingut conceptual en lloc d'adaptar la representació priva l'alumne de l'accés al coneixement.
*   **No confondre el subtipus visuoespacial amb una habilitat matemàtica "baixa" global.** **Per què?** Un alumne pot excel·lir en raonament matemàtic verbal (problemes de lògica, probabilitat narrativa) i tenir grans dificultats en aritmètica escrita.
*   **No treure la calculadora ni les taules "perquè ha d'aprendre a fer-ho sense".** **Per què?** Per a l'alumnat amb discalcúlia moderada-severa, la calculadora i les taules de referència són tecnologies de suport legítimes, igual que les ulleres per a la vista. El seu ús no inhibeix l'aprenentatge conceptual; al contrari, l'allibera.

#### Detecció i protocols

##### Eines de cribatge i diagnosi

*   **Dyscalculia Screener** (Butterworth, 2003): avaluació computaritzada de la capacitat numèrica nuclear, dissenyada per a 6-14 anys. Referència internacional; no hi ha versió validada en català.
*   **MathPro** (Fritz et al., 2018): bateria europea per avaluar el desenvolupament del concepte de nombre en edats primerenques.
*   A Catalunya, el diagnòstic de discalcúlia s'emmarca en la valoració psicopedagògica de l'**EAP** (Equip d'Assessorament Psicopedagògic), dins el marc del **Decret 150/2017**.

##### Protocol a Catalunya (Decret 150/2017)

El Decret 150/2017 estableix el marc d'atenció a la diversitat per a totes les necessitats educatives específiques, incloent les dificultats específiques d'aprenentatge (DEA) com la discalcúlia. Els passos habituals:
1. **Detecció inicial**: tutor/a i equip docent. Senyals de dificultat persistent malgrat instrucció adequada.
2. **Mesures de suport ordinàries (Nivell 1)**: adaptacions metodològiques i de material a l'aula ordinària.
3. **Derivació a l'EAP** si les mesures de Nivell 1 no fan efecte o si es sospita un trastorn específic.
4. **Valoració psicopedagògica (EAP)**: confirma o descarta discalcúlia i altres DEA associades.
5. **Pla de Suport Individualitzat (PI)** si la valoració confirma el trastorn.

---

### 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M1_dislexia-dificultats-lectores**: Comorbiditat ~40-60%. Comparteixen dèficits en processament simbòlic. Problemes de text matemàtic: barrera doble (numèrica + lectora).
*   **M1_TDAH**: Comorbiditat ~30-40%. Impulsivitat en algoritmes + dèficit de memòria de treball s'amplifiquen mutuament.
*   **M1_alumnat-TEA**: Perfil heterogeni — pot coexistir o ser compensat per pensament sistemàtic. Avaluació individual necessària.
*   **M1_trastorn-coordinacio-dispraxia**: El subtipus visuoespacial de la discalcúlia freqüentment coexisteix amb TDC (dispraxia).
*   **M1_creuament-variables-dependencies**: Consultar per als creuaments discalcúlia × TDAH i discalcúlia × dislèxia.
*   **M2_DUA-principis-pautes**: "Múltiples mitjans de representació" és especialment rellevant — visualitzar els nombres, no només el símbol abstracte.
*   **M2_carrega-cognitiva-adaptacio-textos**: La càrrega de càlcul consumeix recursos cognitius que haurien d'anar al raonament.
*   **M3_lectura-facil-comunicacio-clara**: En problemes de text, la barrera lingüística amplifica la barrera numèrica (càrrega doble).

---

### 3. DETECCIÓ (Variables de Context)

*   **Senyals del docent:**
    *   "Usa els dits per a sumes simples que els companys ja resolen de memòria."
    *   "No automatitza les taules de multiplicar malgrat treballar-les molt i repetidament."
    *   "Comet errors d'alineació en les operacions escrites: suma la columna equivocada."
    *   "No detecta que el resultat d'un problema és clarament impossible."
    *   "Gran discrepància entre com raona el problema verbalment i el càlcul que acaba fent."
    *   "S'angoixa molt davant qualsevol tasca numèrica, fins i tot senzilla i familiar."
*   **Senyals de l'alumne:**
    *   Frustració o bloqueig davant tasques matemàtiques, fins i tot les familiars
    *   "Jo no serveixo per les matemàtiques" — convicció ferma i persistent, no excusa puntual
    *   Estratègies de comptatge primitives (compta-ho tot des d'1, en veu molt baixa)
    *   Evitació de tasques on apareguin xifres, fins i tot en contextos no matemàtics (pàgines d'un llibre, preus)
*   **Senyals de context:**
    *   Historial familiar de dificultats matemàtiques
    *   Dificultats persistents malgrat instrucció continuada i reforç individual
    *   Rendiment verbal i lector clarament superior al matemàtic
    *   Millora marcada quan se li permet usar taules, calculadora o material manipulatiu
*   **Anti-senyals:**
    *   Dificultats úniques en problemes de text però no en operacions bàsiques (pot ser barrera lèxica, no numèrica)
    *   Errors aritmètics puntuals per distracció o descuit, no sistemàtics ni coherents
    *   Millora ràpida i consistent amb instrucció addicional ordinària
    *   Dificultats recents, sense historial de dificultat en comptar o comparar quantitats

---

### 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

*   **Principi general:** L'agent ha de separar la *comprensió matemàtica* del *càlcul aritmètic*. L'alumne amb discalcúlia pot raonar matemàticament a un nivell adequat a la seva edat si s'elimina la barrera del càlcul. Proporcionar eines de suport (taules, calculadora, representació CPA) no és "fer-li trampes": és eliminar la barrera per accedir al contingut conceptual.

*   **Heurístiques per a l'Agent DOCENT:**

    *   **Nom:** Separar comprensió i càlcul
    *   **Quan aplica:** Quan un docent dissenya tasques matemàtiques o avaluació per a alumnat amb discalcúlia.
    *   **Fonament:** La discalcúlia afecta la fluïdesa aritmètica, no necessàriament el raonament lògico-matemàtic. Barrejar tots dos en una sola puntuació penalitza la comprensió per la barrera de càlcul.
    *   **Exemple complet de raonament:** "El docent vol avaluar si l'alumne comprèn el concepte de proporcionalitat. L'agent ha de raonar: si exigim el càlcul manual, la barrera aritmètica consumirà tots els recursos cognitius i no podrem mesurar la comprensió. L'estratègia: proporcionar la calculadora i valorar si l'alumne sap *quines* operacions fer i *per què*, no *si pot calcular-les*. La proporcionalitat és el concepte a avaluar; el càlcul és el vehicle, no l'objecte."

    *   **Nom:** Progressió CPA com a eina de diagnòstic pedagògic
    *   **Quan aplica:** Quan un alumne comet errors sistemàtics en un procediment matemàtic.
    *   **Fonament:** Butterworth i el NCTM proposen que els errors procedimentals revelen on s'ha trencat la comprensió conceptual. La progressió CPA permet identificar en quin nivell de representació falla la comprensió.
    *   **Exemple complet de raonament:** "Un alumne comet errors sistemàtics en la multiplicació de dues xifres. En lloc de repetir el procediment abstracte, l'agent suggerirà al docent: primer comprova si l'alumne comprèn la multiplicació com a suma repetida amb material concret (C); després, si pot representar-la en un diagrama d'àrea (P); si el model concret falla, el problema és de comprensió conceptual; si el model P falla però el C funciona, cal treballar el salt a la representació pictòrica. Cada nivell diagnostica on és la ruptura."

    *   **Nom:** Ansietat matemàtica — trencar el cicle
    *   **Quan aplica:** Quan l'alumne mostra bloqueig, evitació o angoixa davant qualsevol tasca numèrica.
    *   **Fonament:** Ashcraft & Krause (2007) demostren que l'ansietat matemàtica redueix els recursos de memòria de treball disponibles per al càlcul, generant errors fins i tot en tasques que l'alumne domina en condicions tranquil·les. No és "exagerar": és un efecte fisiològic mesurable.
    *   **Exemple complet de raonament:** "Una alumna que normalment resol bé les fraccions es bloqueja en un examen. L'agent ha de raonar: el primer pas no és repassar el procediment, és reduir l'activació d'ansietat. Recomanarà: (1) reformular la tasca com a exploració ('mira com es comporten aquestes quantitats') i no com a prova ('resol'); (2) començar per una tasca que l'alumna sap que pot fer per activar un primer èxit; (3) permetre l'ús de representació pictòrica o material de suport. L'objectiu a curt termini és trencar el bucle estrès → errors → més estrès."

*   **Heurístiques per a l'Agent ALUMNE:**

    *   **Nom:** Fer visible el que el cervell ha de retenir
    *   **Quan aplica:** Quan l'alumne perd el fil en problemes multi-pas o algoritmes llargs.
    *   **Fonament:** La memòria de treball visuoespacial és el coll d'ampolla en la discalcúlia. Externalitzar-la (escriure els passos, usar paper de treball visible) no és una debilitat: és la compensació correcta.
    *   **Exemple complet de raonament:** "Un alumne perd el fil a la meitat d'una divisió llarga. En lloc d'intentar-ho de nou mentalment, l'estratègia és escriure cada subresultat en un lloc visible i numerat: Pas 1: [...], Pas 2: [...]. Si perd el fil, sap exactament on ha quedat i pot reprendre. Tenir la 'memòria de treball externa al paper' és completament vàlid — és com un lector usa el dit per seguir la línia."

    *   **Nom:** Verificació per estimació de magnitud
    *   **Quan aplica:** Quan l'alumne ha obtingut un resultat i no sap si és correcte.
    *   **Fonament:** El sentit de magnitud —que és la barrera nuclear— es pot entrenar amb pràctica. Una estratègia compensatòria és "aproximar primer, calcular després" per tenir un ancoratge de raonabilitat.
    *   **Exemple complet de raonament:** "L'alumne ha calculat 48 × 3 = 204. L'agent proposa: 'Arrodoneja: 50 × 3 és 150. El teu resultat (204) és molt més gran que 150. Això et diu que alguna cosa no quadra.' El contrast entre l'estimació i el resultat activa la revisió sense requerir un nou algoritme complet. Amb el temps, repetir aquest patró entrena el sentit de magnitud."

---

## 6. INSTRUCCIONS D'ADAPTACIÓ TEXTUAL PER A L'LLM

### Barrera nuclear
**Sentit numèric (magnitud numèrica)**: L'alumnat amb discalcúlia té com a barrera principal l'accés a la representació de magnitud numèrica — no "senten" intuïtivament el pes dels nombres ni les relacions entre ells. Quan el text inclou operacions, seqüències de passos numèrics o raonaments abstractes sobre quantitats, la càrrega cognitiva s'acumula ràpidament i el contingut conceptual es perd rere la barrera aritmètica.

### Instruccions per al prompt LLM

```
PERFIL: Discalcúlia (Butterworth/Geary)
- Fragmentar problemes multi-pas: un sub-pas per línia, numerats explícitament
- Proporcionar suport visual per a magnituds (línia numèrica, diagrama de barres)
- No exigir recuperació de fets aritmètics: proporcionar taules si cal
- Acompanyar cada operació abstracta amb representació concreta o pictòrica (CPA)
- Si ansietat_matematica=true: framing exploratiu, eliminar pressió temporal, primer èxit petit
- Si memoria_treball_afectada=true: escriure cada pas intermedi, limitar a 2-3 elements simultanis
```

### Mapa barrera → instruccions (prioritzat)

| Prioritat | Instruccions activades | Justificació (barrera) |
|---|---|---|
| **1a (sentit numèric)** | M-02 (línia numèrica / magnitud visual), M-03 (representació CPA), M-05 (estimació com a verificació) | Barrera nuclear: magnitud |
| **2a (procedimental)** | M-01 (fragmentar passos, un per línia, numerats), M-04 (taules proporcionades, no memoritzar) | Barrera procedimental |
| **3a (visuoespacial)** | M-06 (graella alineació columnes, codi color per unitats/desenes/centenes), B-01 (paràgrafs curts) | Barrera visuoespacial |
| **4a (ansietat)** | M-07 (framing exploratiu), H-05 (primer èxit ràpid), M-08 (eliminar pressió temporal visible) | Reducció ansietat matemàtica |

### Exemple ABANS → DESPRÉS (Primària 5è, matemàtiques, problema multi-pas)

**Original:**
> Un supermercat compra 12 caixes de taronges. Cada caixa conté 24 taronges. El preu per taronja és de 0,15 €. Quant ha pagat el supermercat en total?

**Adaptat (discalcúlia procedural, grau moderat, DUA Core):**

## Text adaptat

**Problema: quant ha pagat el supermercat per totes les taronges?**

Fes-ho pas a pas. Pots usar la calculadora.

**Pas 1 de 3 — Quantes taronges hi ha en total?**
- El supermercat ha comprat **12 caixes**.
- Cada caixa té **24 taronges**.
- Quantes taronges hi ha en total?
  - 12 × 24 = _____ taronges

**Pas 2 de 3 — Recorda el preu**
- Cada taronja val **0,15 €**

**Pas 3 de 3 — Calcula el preu total**
- Total de taronges (Pas 1): _____
- Preu per taronja: 0,15 €
- Total pagat: _____ × 0,15 € = _____ €

> **Comprova**: "Tens moltes taronges (centenars) i cada una val pocs cèntims. El total ha de ser un nombre de desenes d'euros — no de milers ni de cèntims." Si el teu resultat és molt diferent, revisa el Pas 1.

---

## 5. FONTS DEL CORPUS

| # | Referència | Tipus | Any |
|---|-----------|-------|-----|
| 1 | Dehaene, S. *The Number Sense: How the Mind Creates Mathematics.* Oxford University Press. | Teoria cognitiva (Triple Code) | 1997/2011 |
| 2 | Butterworth, B. *Dyscalculia: From Science to Education.* Routledge. | Monografia clínica | 2019 |
| 3 | Geary, D.C. *Mathematical disabilities: Cognitive, neuropsychological, and genetic components.* Psychological Bulletin, 114(2), 345–362. | Subtipus (procedimental/verbal/visuoespacial) | 1993 |
| 4 | Ashcraft, M.H. & Krause, J.A. *Working memory, math performance, and math anxiety.* Psychonomic Bulletin & Review, 14(2), 243–248. | Ansietat matemàtica | 2007 |
| 5 | Beilock, S.L. & Maloney, E.A. *Math Anxiety: A Factor in Math Achievement Not to Be Ignored.* Policy Insights from Behavioral and Brain Sciences, 2(1), 4–12. | Ansietat matemàtica | 2015 |
| 6 | American Psychiatric Association. *DSM-5-TR: Diagnostic and Statistical Manual of Mental Disorders, 5a ed. revisada.* APA. | Marc diagnòstic | 2022 |
| 7 | OMS. *ICD-11: International Classification of Diseases, 11a revisió.* (6A03.2 Developmental Learning Disorder with impairment in mathematics) | Marc diagnòstic | 2022 |
| 8 | Generalitat de Catalunya. *Decret 150/2017, de 17 d'octubre, de l'atenció educativa a l'alumnat en el marc d'un sistema educatiu inclusiu.* DOGC 7477. | Marc normatiu Catalunya | 2017 |
| 9 | National Council of Teachers of Mathematics (NCTM). *Principles to Actions: Ensuring Mathematical Success for All.* NCTM. | Pedagogia CPA, evidència | 2014 |
| 10 | Butterworth, B. *Dyscalculia Screener.* GL Assessment. | Eina de cribatge | 2003 |
| 11 | Fritz, A., Haase, V.G. & Räsänen, P. (eds.) *International Handbook of Mathematical Learning Difficulties.* Springer. MathPro battery. | Eines diagnòstiques | 2019 |

*11 fonts referencials · document generat 2026-04-27 · review_status: esborrany*
