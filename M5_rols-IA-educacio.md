---
modul: M5
titol: "Els 7 rols de la IA en educació"
tipus: marc
descripcio: "Set rols d'interacció IA-alumne (adaptació Mollick), tres famílies (procesuals, mixtos, productius), comportament per nivell i col·lapse a N4"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Definició i principis

Els 7 rols de la IA a l'aula defineixen **com actua la IA** durant una activitat d'aprenentatge. Són la capa d'implementació de l'arquitectura Quest-Rol-Nivell: la Quest defineix la intenció pedagògica, el Rol defineix el comportament de la IA, i el Nivell defineix el grau d'autonomia.

Els rols s'originen en l'adaptació d'Ethan Mollick (2023) per a l'àmbit educatiu, reconfigurats dins del marc de Jesuïtes Educació per integrar-se amb el Model 4D, els nivells MIHIA i el marc cognitiu de fricció productiva.

### Els 7 rols

| # | Rol | La IA actua com a... | Què fa |
|---|---|---|---|
| 1 | **Mentor Socràtic** | Guia que pregunta | Fa preguntes per guiar el pensament, no dóna respostes directes |
| 2 | **Simulador / Actor** | Personatge o escenari | Representa situacions, personatges o contextos amb què l'alumne interactua |
| 3 | **Crític / Editor** | Revisor exigent | Avalua la feina de l'alumne, detecta errors, suggereix millores sense reescriure |
| 4 | **Generador de Casos** | Creador de material | Genera exemples, dades, problemes o escenaris per analitzar |
| 5 | **Teachable Agent** | "Alumne" que aprèn | L'alumne ensenya a la IA; la IA simula malentesos |
| 6 | **Contrincant** | Devil's Advocate | Contradiu l'alumne sistemàticament per obligar-lo a argumentar |
| 7 | **Traductor / Adaptador** | Personalitzador | Adapta contingut a nivells, llengües, formats o necessitats |

### Les tres famílies de rols

L'anàlisi dels 21 exemples del document `exemples-rols-mihia.md` revela que els 7 rols es comporten diferentment segons el nivell de delegació. Aquesta diferència és estructural:

**Rols procesuals** (N2-N3 nadiu, **col·lapsen a N4**): Mentor Socràtic, Teachable Agent, Contrincant. La seva essència és el procés d'interacció — l'alumne pensa, pregunta, defensa, ensenya. A N4, la IA genera el diàleg complet i el rol perd la seva raó de ser: l'alumne ja no pensa, llegeix un producte. Indueixen principalment Resistència i Descoberta.

**Rols mixtos** (N2-N4 viable): Crític / Editor, Simulador. Funcionen tant en iteració (N2-N3) com en generació completa (N4). El canvi de nivell no destrueix l'essència del rol. Indueixen principalment Recursivitat i Descoberta.

**Rols productius** (N3-N4 nadiu, N2 queda limitat): Generador de Casos, Traductor / Adaptador. La seva naturalesa és produir. La fricció productiva es trasllada al moment en què l'alumne treballa amb el producte, no a la interacció amb la IA.

### Comportament per nivell

| Rol | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| Mentor Socràtic | — | Context | **Nadiu** | **Nadiu** | ⚠️ Col·lapse | Meta-disseny |
| Simulador | — | Context | **Nadiu** | **Nadiu** | Viable amb risc | Meta-disseny |
| Crític / Editor | — | Context | **Nadiu** | **Nadiu** | Viable | Meta-disseny |
| Generador de Casos | — | Context | Limitat | **Nadiu** | **Nadiu** | Meta-disseny |
| Teachable Agent | — | Context | **Nadiu** | **Nadiu** | ⚠️ Col·lapse | Meta-disseny |
| Contrincant | — | Context | **Nadiu** | **Nadiu** | ⚠️ Col·lapse | Meta-disseny |
| Traductor / Adaptador | — | Context | Limitat | **Nadiu** | **Nadiu** | Meta-disseny |

### Matriu Rol × Moviment de Fricció

| Rol | Descoberta | Recursivitat | Resistència |
|---|---|---|---|
| Mentor Socràtic | ★★ | ★ | ★★ |
| Simulador | ★★ | ★★ | ★ |
| Crític / Editor | ★ | ★★ | ★ |
| Generador de Casos | ★★ | ★ | — |
| Teachable Agent | ★★ | ★ | ★★ |
| Contrincant | ★ | ★★ | ★★ |
| Traductor / Adaptador | ★ | ★ | — |

## Autors i evidència clau

*   **Mollick, E. (2023)**: Proposta original dels rols d'interacció IA a l'aula. La classificació en 7 rols ha estat àmpliament difosa i adoptada en contextos educatius.
*   **Novokshanova, E. (2025)**: La matriu Rol × Moviment de Fricció es fonamenta en els tres moviments de fricció productiva (Descoberta, Recursivitat, Resistència).
*   **Document `exemples-rols-mihia.md` (JE, 2026)**: L'anàlisi dels 21 exemples (7 rols × 3 etapes × 6 nivells) revela el patró de les tres famílies i el col·lapse a N4.
*   **ADR Arquitectura Quest-Rol-Nivell (JE, 2026)**: Decisió de situar els rols com a capa d'implementació (no de primer nivell).

## Exemples concrets d'aplicació a l'aula

1.  **Mentor Socràtic a N2 (Filosofia, 4t ESO)**: L'alumne escriu la seva posició sobre cotxes autònoms (200 paraules). Envia el text a la IA: "Ets un filòsof socràtic. Llegeix la meva argumentació i fes-me 3 preguntes profundes que m'obliguin a pensar millor." La IA NO dóna respostes, només pregunta. L'alumne ha de respondre per escrit, millorant el seu raonament. Moviment: Resistència (ha de defensar la posició). Mode ICAP: Interactive.

2.  **Generador de Casos a N3 (Matemàtiques, 1r ESO)**: L'alumne demana: "Crea'm 10 equacions de primer grau de dificultat mitjana, sense solucions." Les resol manualment. Després demana les solucions per verificar. Pot demanar més exercicis si necessita més pràctica. Moviment: Recursivitat. La fricció no resideix en la interacció amb la IA sinó en la resolució autònoma.

3.  **Teachable Agent a N2 (Ciències, 2n ESO)**: La IA actua com "Alex, un alumne de 1r ESO que no entén la fotosíntesi". L'alumne ha d'explicar-li el procés. La IA fa preguntes ingènues amb malentesos típics. L'alumne corregeix i reformula. Moviment: Resistència + Descoberta (l'alumne veu els seus propis buits quan intenta ensenyar).

## Errors comuns — què NO fer

1.  **Dir "usa ChatGPT" en lloc de "usa la IA com a [Rol]".** El rol defineix el comportament esperat de la IA. Sense rol, l'alumne interactua amb una IA genèrica i la interacció tendeix cap a la delegació. El prompt ha de codificar el comportament del rol ("Ets un crític exigent que assenyala errors sense reescriure").

2.  **Usar rols procesuals a N4.** Mentor Socràtic, Teachable Agent i Contrincant col·lapsen a N4. Si l'alumne demana "genera un diàleg socràtic complet", la IA produeix un text que l'alumne llegeix passivament. El rol ha perdut la seva essència: l'alumne ja no pensa, consumeix. Excepció: si l'objectiu és aprendre enginyeria de prompts, no el contingut.

3.  **Assignar un rol sense verificar la matriu d'afinitats Quest × Rol.** No tots els rols serveixen totes les Quests. Un Traductor/Adaptador per a una Quest Critique és forçat. Un Contrincant per a una Quest Right-Sizing no té sentit. La matriu dispersa d'afinitats filtra les combinacions incoherents.

4.  **Confondre la família del rol i triar el nivell equivocat.** Un Generador de Casos (productiu) a N2 queda limitat perquè la seva naturalesa és produir, no dialogar. Un Mentor Socràtic (procesual) a N4 col·lapsa. Verificar la família abans d'assignar el nivell.

5.  **No seqüenciar rols dins d'una tasca complexa.** Una tasca de 3 sessions pot usar Generador de Casos (material) → Mentor Socràtic (anàlisi) → Crític (refinament). Cada fase demana un rol diferent. Usar un sol rol per a tota la tasca limita la varietat de fricció.

## Matissos i excepcions

*   **El Simulador és un cas especial.** Pot funcionar a N4 (la IA genera una entrevista completa amb un personatge històric), però aleshores l'activitat canvia de naturalesa: l'alumne ja no practica la interacció sinó que avalua un producte. Això pot ser pedagògicament vàlid si l'objectiu és l'anàlisi crítica del text generat, no la pràctica de la interacció.

*   **El Crític/Editor a N4 té un ús legítim.** Quan l'alumne envia un text i la IA el reescriu millorat, l'alumne pot comparar les dues versions i aprendre de les diferències. La fricció es trasllada a la comparació (Descoberta). Però si l'alumne simplement entrega la versió de la IA, no hi ha aprenentatge.

*   **Rols productius a N2.** Un Generador de Casos que només genera 2-3 exercicis senzills a petició de l'alumne funciona a N2, però no aprofita el potencial del rol. La naturalesa productiva del rol brilla a N3-N4, on la IA genera material divers i l'alumne hi treballa.

*   **Combinar rols no és barrejar-los.** Seqüenciar rols (primer Generador, després Mentor) és bo. Però demanar a la IA que sigui "Mentor Socràtic i Generador de Casos alhora" confon el comportament de la IA i dilueix la fricció.

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M5_arquitectura-quest-rol-nivell**: Els rols són la capa d'implementació dins l'arquitectura Q>R>N. La matriu Quest × Rol determina les combinacions vàlides.
*   **M5_quests-missions-aprenentatge**: Cada Quest admet un subconjunt de rols (matriu d'afinitats). El docent tria primer la Quest i després el Rol compatible.
*   **M5_nivells-delegacio-mihia**: Les 3 famílies tenen rangs nadius diferenciats. El col·lapse a N4 dels procesuals és un dels principis operatius més importants.
*   **M2_carrega-friccio-cognitiva**: Les 3 famílies deriven de l'anàlisi de quina càrrega externalitzen i quina fricció generen.
*   **M5_disseny-instruccional-amb-IA**: La tria del Rol és el pas 2 de la seqüència de disseny del docent.
*   **M5_prompt-engineering-educatiu**: El prompt ha de codificar el comportament del rol. Cada rol requereix un tipus de prompt diferent.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Vull que la IA faci preguntes, no que doni respostes."
*   "Quin tipus d'interacció hauria de tenir l'alumne amb la IA?"
*   "Puc combinar diferents rols de la IA en una mateixa activitat?"
*   "Per què quan demano als alumnes que facin un diàleg socràtic amb la IA, acaben copiant el diàleg sencer?"
*   "Necessito que la IA simuli un personatge per a un role-play."

**Senyals de l'alumne**
*   L'alumne interactua amb la IA de manera genèrica, sense un rol definit ("explica'm X", "fes-me Y").
*   L'alumne usa un rol procesual demanant productes complets ("genera un debat", "escriu un diàleg socràtic").
*   L'alumne aprofita la interacció amb un rol i mostra Resistència, Recursivitat o Descoberta.

**Senyals de context**
*   Es dissenya una nova activitat amb IA i cal decidir el tipus d'interacció.
*   Es configura un assistent institucional i cal definir el seu comportament per defecte.
*   Es revisen activitats existents per detectar per què "no funcionen" amb IA.

**Anti-senyals**
*   El docent pregunta sobre aspectes tècnics de la IA (tokens, models, configuració) sense connexió amb rols pedagògics.
*   L'alumne usa la IA per a tasques purament mecàniques (format, ortografia) on el concepte de "rol" no aplica.

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha de guiar el docent perquè triï el rol de la IA que millor serveixi la intenció pedagògica (Quest) i sigui coherent amb el nivell de delegació (MIHIA), verificant que la combinació genera fricció productiva.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Triar el rol des de l'objectiu, no des de l'eina.**
    *   **Quan aplica:** Quan el docent diu "vull usar ChatGPT" o "vull que la IA faci X" sense haver definit l'objectiu pedagògic.
    *   **Fonament:** L'arquitectura Quest-Rol-Nivell estableix que la pregunta correcta és "què vull que passi cognitivament?" (Quest), no "quina eina vull usar?" (Rol). Començar pel Rol indueix a *solution looking for a problem* (ADR Xat 4). El Rol ha de ser conseqüència de la Quest, no l'inrevés.
    *   **Exemple complet de raonament:** Un docent diu "vull usar la IA com a tutor". L'agent preguntaria: "Quin és l'objectiu d'aprenentatge?" Si és "que l'alumne aprofundeixi en la seva comprensió d'un tema", la Quest és Clarity i el Rol compatible és Mentor Socràtic. Si és "que practiqui habilitats en un context realista", la Quest és Mission i el Rol és Simulador. El mateix desig vague ("tutor") porta a rols molt diferents segons la intenció pedagògica. L'agent ha de resoldre la Quest primer.

2.  **Heurística: Verificar la família del rol abans d'assignar el nivell.**
    *   **Quan aplica:** Quan es tria un rol i un nivell de delegació per a una activitat.
    *   **Fonament:** Les tres famílies (procesuals, mixtos, productius) tenen rangs nadius diferenciats. Els rols procesuals col·lapsen a N4: la IA genera el producte complet i l'alumne ja no exerceix el procés cognitiu que el rol havia d'induir. Això és una conseqüència directa del marc de fricció (Novokshanova): el Col·lapse (surt del bucle massa aviat) esdevé inevitable quan la IA fa tot el bucle de cop.
    *   **Exemple complet de raonament:** Un docent vol que els alumnes facin un debat amb un Contrincant (rol procesual) i proposa N4: "La IA generarà un debat complet amb arguments i contraarguments." L'agent alertaria que el Contrincant és procesual i col·lapsa a N4: l'essència del rol és que l'alumne argumenti, no que llegeixi arguments. Suggerira N2-N3: l'alumne escriu la seva posició, la IA la contradiu, l'alumne respon, la IA ataca des d'un angle nou. Ara l'alumne pensa activament (Resistència) durant 5-6 rondes (Recursivitat).

3.  **Heurística: Seqüenciar rols dins de tasques complexes.**
    *   **Quan aplica:** Quan l'activitat dura més d'una sessió o té múltiples fases.
    *   **Fonament:** Cada fase d'una tasca pot requerir un tipus de fricció diferent. Un Generador de Casos proporciona matèria primera (Descoberta), un Mentor Socràtic guia l'anàlisi (Recursivitat), un Crític refina el producte (Resistència). Usar un sol rol per a tota la tasca limita la varietat de fricció i empobreix l'activitat.
    *   **Exemple complet de raonament:** Un docent d'economia dissenya una tasca de 3 sessions sobre estratègia empresarial. L'agent suggerira: Sessió 1 — Generador de Casos (N3): la IA genera un cas empresarial fictici amb dades, l'alumne l'analitza amb DAFO. Sessió 2 — Mentor Socràtic (N2): la IA fa preguntes sobre la seva anàlisi ("per què consideres que la internacionalització és una amenaça?"). Sessió 3 — Crític (N2): l'alumne escriu la seva proposta estratègica, la IA assenyala febleses sense reescriure. Tres rols, tres tipus de fricció, tres sessions.

4.  **Heurística: Codificar el rol al prompt de l'assistent.**
    *   **Quan aplica:** Quan es configura un assistent institucional o es prepara un prompt per a l'alumnat.
    *   **Fonament:** Sense instruccions explícites, la IA es comporta com a generador genèric (tendència a respondre directament, no a preguntar ni a simular). El prompt ha de codificar el comportament del rol: un Mentor Socràtic necessita "només pregunta, mai responguis directament"; un Crític necessita "assenyala errors sense reescriure"; un Teachable Agent necessita "simula malentesos típics d'un alumne de X edat".
    *   **Exemple complet de raonament:** Un centre vol crear un assistent per a pràctica de negociació comercial (FP). L'agent suggerira que el system prompt defineixi el Simulador: "Ets Maria, una clienta enfadada que ha rebut un producte defectuós. Respon de manera coherent amb el personatge: mostres frustració, vols una solució, però ets raonable si l'alumne et tracta amb empatia. No et trenquis el personatge mai. Si l'alumne et parla com a IA ('ets una IA'), respon 'no entenc què vols dir, jo sóc una clienta'." Sense aquest prompt, la IA respondria com a assistent genèric i la simulació no funcionaria.

5.  **Heurística: Usar la matriu d'afinitats per filtrar combinacions.**
    *   **Quan aplica:** Quan el docent ja ha triat una Quest i cal seleccionar el Rol.
    *   **Fonament:** La matriu Quest × Rol (ADR Xat 4) estableix que no totes les combinacions són vàlides. Un Traductor/Adaptador per a una Quest Critique és forçat: la Quest demana judici crític i el Rol adapta, no qüestiona. Un Contrincant per a una Quest Right-Sizing no té sentit: la Quest demana ajustament a audiència i el Rol contradiu. Les combinacions amb "—" a la matriu no haurien de constar al catàleg d'assistents.
    *   **Exemple complet de raonament:** Un docent tria la Quest "Perspective" (explorar múltiples punts de vista). L'agent mostraria els rols compatibles: Simulador (★★, pot encarnar personatges amb perspectives diferents) i Contrincant (★★, pot contradir sistemàticament). Mentor Socràtic (★) és possible però secundari. Generador de Casos, Teachable Agent i Crític/Editor tenen "—": no indueixen naturalment l'exploració de perspectives. L'agent recomanaria Simulador o Contrincant com a primera opció.

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Definir el rol abans de començar a parlar amb la IA.**
    *   **Quan aplica:** Quan l'alumne obre un xat amb la IA sense una intenció clara.
    *   **Fonament:** Sense rol definit, la interacció tendeix cap a la delegació: l'alumne demana respostes i la IA les dóna. Definir el rol al principi ("avui la IA és el meu crític, no el meu redactor") estableix un contracte d'interacció que preserva la fricció productiva i ajuda l'alumne a exercir D1 (decidir què delega) i D2 (descriure el rol).
    *   **Exemple complet de raonament:** Un alumne ha d'escriure un assaig sobre Kafka. Abans d'obrir la IA, l'agent li suggerira pensar: "Necessito que la IA m'escrigui l'assaig o que m'ajudi a millorar el meu?" Si és el segon, el rol és Crític. L'alumne escriu primer, després envia a la IA: "Ets un crític literari. Llegeix el meu assaig i digues-me 3 punts febles sense reescriure res." Ara la interacció preserva la propietat cognitiva de l'alumne sobre el contingut de l'assaig.

2.  **Heurística: Reconèixer quan el rol de la IA ha col·lapsat.**
    *   **Quan aplica:** Quan l'alumne nota que la IA "li ha fet la feina" en lloc d'ajudar-lo a pensar.
    *   **Fonament:** El col·lapse és una de les tres fallades de la fricció productiva (Novokshanova): l'alumne surt del bucle massa aviat i accepta el producte generat. Si l'alumne se n'adona, pot tornar a entrar al bucle: "Espera, no vull que m'escriguis el text. Vull que em facis preguntes sobre el que he escrit jo."
    *   **Exemple complet de raonament:** Un alumne ha demanat a la IA que generi un diàleg socràtic complet sobre ètica. Rep 8 preguntes amb respostes model. L'agent l'ajudaria a veure que ha passat de "pensar amb la IA" a "llegir el que la IA ha pensat". Suggerira: "Esborrem tot això. Escriu tu una idea sobre el tema. Ara digues a la IA: 'fes-me preguntes sobre el que he escrit, no em donis respostes.'" L'alumne recupera l'agència i el diàleg torna a ser Interactiu.

3.  **Heurística: Adaptar el rol a la seva necessitat, no usar el rol per defecte.**
    *   **Quan aplica:** Quan l'alumne té llibertat per triar com interactuar amb la IA.
    *   **Fonament:** El Model 4D situa la Delegació (D1) com la primera competència: decidir quan, per a què i amb quin grau d'autonomia usar la IA. Un alumne que sempre usa la IA com a Generador (N4) per a totes les tasques no exerceix D1. Triar conscientment entre "avui necessito un Crític" i "avui necessito un Simulador" és un acte de metacognició.
    *   **Exemple complet de raonament:** Un alumne de FP ha de preparar una entrevista d'acollida en serveis socials. L'agent li preguntaria: "Què necessites? Si vols practicar l'entrevista, la IA pot ser un Simulador (persona en situació vulnerable que respon les teves preguntes). Si vols revisar el teu protocol, la IA pot ser un Crític (llegeix el teu protocol i assenyala febleses). Si vols veure casos nous, pot ser un Generador de Casos." La tria conscient del rol és ja un exercici d'aprenentatge.

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | Mollick, E. (2023). Assigning AI: Seven Ways of Using AI in Class | https://www.oneusefulthing.org/p/assigning-ai-seven-approaches-for |
| 2 | Novokshanova, E. (2025). Productive Friction in Human-AI Feedback | file://upload/Novokshanova_2025_ProductiveFriction.pdf |
| 3 | ADR Arquitectura Quest-Rol-Nivell (JE, 2026) | file://docs/decisions/arquitectura-quest-rol-nivell.md |
| 4 | Exemples d'Aplicació dels 7 Rols (JE, 2026) | file://public/exemples-rols-mihia.md |
| 5 | docs/marcs-teorics/friccio-cognitiva-extens.md | file://docs/marcs-teorics/friccio-cognitiva-extens.md |

*5 documents font · secció generada manualment*
