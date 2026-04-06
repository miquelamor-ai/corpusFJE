---
modul: M5
titol: "Arquitectura Quest-Rol-Nivell: sistema integrat"
tipus: marc
descripcio: "Sistema integrat Q>R>N per al disseny d'activitats amb IA: jerarquia conceptual, 4D×3 capes (SOBRE/PER A/AMB), cascada institució→docent→alumne, doble entrada i alternatives descartades"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Definició i principis

L'arquitectura del disseny d'activitats amb IA s'organitza en tres eixos jeràrquics:

*   **Quest** (missió pedagògica): "Què vull que passi cognitivament?"
*   **Rol** (funció de la IA): "Com ha d'actuar la IA per servir aquesta missió?"
*   **Nivell** (delegació MIHIA): "Quanta autonomia cedeix l'alumne a la màquina?"

La posició institucional canònica és **Quest-first** (Arquitectura D, ADR Xat 4). La pregunta pedagògica correcta és "què ha d'aprendre l'alumne?", no "quina eina vull usar?". Començar pel Rol indueix a *solution looking for a problem*. Coherent amb el backward design (Wiggins & McTighe), el principi d'antropocentrisme del marc general i el to de JE: primer formem pedagògicament, després donem eines.

### La seqüència de disseny del docent

| Pas | Pregunta | Eix |
|---|---|---|
| 1 | "Què ha d'aprendre l'alumne?" | Quest |
| 2 | "Com ha d'actuar la IA?" | Rol (matriu d'afinitats) |
| 3 | "Quanta autonomia?" | Nivell (rang nadiu × sostre d'etapa) |
| 4 | "Hi ha fricció productiva?" | Verificació (7 criteris del marc cognitiu) |

### Doble entrada

Tot i la jerarquia, la interfície d'ús permet doble entrada: per Quest → Rols compatibles → Nivell, o per Rol → Quests que serveix → Nivell. La mateixa informació, dos camins d'accés. Respecta la diversitat de partida dels docents (molts ja coneixen els Rols de Mollick).

### Dissolució dels Patrons A/B/C

Els tres patrons anteriors (Fonamentació / Diàleg Crític / Orquestració) es dissolen. No afegien valor que les Quests no proporcionin directament i introduïen una capa sintètica innecessària.

### Relació entre els 3 eixos

**Quest × Rol**: matriu dispersa d'afinitats (★★/★/—). Un Rol serveix diverses Quests; una Quest admet diversos Rols.

**(Quest, Rol) × Nivell**: cada combinació té un rang de Nivells nadiu. Fora del rang, el valor es degrada o el rol col·lapsa.

**Etapa × Nivell**: el mapa d'etapes estableix un sostre. Rang efectiu = rang nadiu ∩ sostre d'etapa.

### Les 4D × 3 capes: SOBRE, PER A i AMB la IA

El Model 4D (Dakan & Feller) és un marc de fluïdesa que vehicula els tres àmbits d'integració de la IA dins un únic esquema supra-curricular:

| D | SOBRE (saber) | PER A (saber fer) | AMB (aplicar) |
|---|---|---|---|
| **Delegació** | Com funcionen els sistemes IA | Decidir quan usar IA, per a què, amb quin grau | Triar el nivell adequat per a cada activitat |
| **Descripció** | Com processen els models | Formular instruccions precises | Dissenyar la interacció per a un objectiu d'aprenentatge |
| **Discerniment** | Biaixos, al·lucinacions, versemblança ≠ veracitat | Avaluar, verificar, detectar errors | Verificació sistemàtica dels outputs |
| **Diligència** | Privacitat, autoria, impacte, regulació | Declarar, protegir, responsabilitzar-se | Citar l'ús, protegir companys, triar eines autoritzades |

Aquesta lectura fa del 4D un marc **supra-curricular**: no depèn de cap currículum territorial i permet que cada centre o fundació d'EDUCSI mapi el seu currículum local al 4D.

### La cascada institució → docent → alumne

Les 4D operen a tres nivells d'agent encadenats:

| D | Institució | Docent | Alumne |
|---|---|---|---|
| **Delegació** | Decideix quins assistents existiran, quins N s'autoritzen | Decideix quina activitat incorpora IA, amb quin objectiu | Opera dins l'espai dissenyat; progressivament guanya autonomia |
| **Descripció** | Construeix l'assistent (system prompt, guardrails) | Dissenya la interacció (bastides, consignes) | Formula peticions; progressivament aprèn precisió |
| **Discerniment** | Testa, audita, mesura fiabilitat (crossover point) | Acompanya, modela la verificació | Avalua, contrasta, rebutja si cal |
| **Diligència** | Compliment normatiu (RIA UE, LOPD), seguretat | Modela l'ús responsable | Declara el seu ús, protegeix dades |

Tres implicacions: (1) l'alumne no decideix sol què delegar — opera dins un espai segur ja dissenyat; (2) dissenyar assistents institucionals és exercir les 4D al nivell d'agent més alt; (3) el camí de maduresa va de "operar dins un espai dissenyat per altri" a "dissenyar el propi espai" (N0→N5).

### El grau superior de fluïdesa: dissenyar artefactes

La fluïdesa en IA culmina en la capacitat de dissenyar artefactes digitals (assistents, agents, aplicacions) fent servir la IA com a eina de creació. No requereix una 5a D sinó l'exercici de les mateixes 4D a un nivell d'abstracció superior. Connexió directa amb N5 (Agència Autònoma).

### Alternatives descartades

| Alternativa | Per què descartada |
|---|---|
| Arq A — Quests + Rols paral·lels | Canonitza Mollick al mateix nivell que Khan/F/F. 2 vocabularis + taula de traducció. Massa complex |
| Arq B — Rol-first | Parteix de la màquina, no de la intenció pedagògica |
| Arq C — Triple simètric | El marc no pren posició pedagògica. Manual, no guia |
| Patrons A/B/C | Capa sintètica sense valor diferencial |
| 5a D (Disseny) | El disseny d'artefactes és N5 del 4D existent, no una competència nova |

## Autors i evidència clau

*   **Khan, S., Fisher, D., Frey, N., Marshall, H. W. & Hargrave, A. (2025)**: Les 10 Quests com a missions pedagògiques.
*   **Mollick, E. (2023)**: Els 7 rols d'interacció IA, repositioned com a capa d'implementació.
*   **Dakan, R. & Feller, M.**: Model 4D i AI Fluency. La lectura 4D×3 capes (SOBRE/PER A/AMB) és l'aportació de JE.
*   **Wiggins, G. & McTighe, J. (1998)**: Backward design. Fonament de l'arquitectura Quest-first.
*   **Fisher, D. & Frey, N.**: GRR. Fonament de la progressió de nivells i de la cascada docent→alumne.
*   **ADR Xat 4 (JE, 2026)**: Document de decisió que estableix l'arquitectura D i les alternatives descartades.

## Exemples concrets d'aplicació a l'aula

1.  **Seqüència completa Q>R>N (Ciències Socials, 3r ESO)**:
    Pas 1 — Quest: Perspective (explorar punts de vista sobre la deslocalització industrial).
    Pas 2 — Rol: Simulador (★★, encarnarà 3 personatges: empresari, treballador, ecologista).
    Pas 3 — Nivell: N2 (sostre ESO 1r cicle = N2; rang nadiu Simulador = N2-N3; intersecció = N2).
    Pas 4 — Verificació: Moviment esperat = Resistència (dialogar amb perspectives incòmodes). CFF = pre-compromís (l'alumne escriu la seva posició inicial). Mode ICAP = Interactive. Càrrega externalitzada = extrínseca (encarnació del personatge). ✓

2.  **Doble entrada per Rol (Llengua, 1r Batxillerat)**:
    Un docent diu: "Vull usar un Crític/Editor." L'agent mostra Quests compatibles: Critique (★★), Growth (★★), Compare (★), Clarity (★). El docent tria Critique: "Vull que l'alumne avaluï críticament el seu propi text." Nivell: N3 (cocreació iterativa, 3 rondes de revisió). El resultat és el mateix que si hagués entrat per Quest, però el camí és diferent.

3.  **Cascada institucional (Centre nou amb IA)**:
    Institució (D1): autoritza Mentor Socràtic, Crític/Editor i Generador de Casos. Sostre: N2 per a tot l'alumnat el primer any.
    Docent (D2): dissenya una activitat amb Crític/Editor a N2 per a textos argumentatius.
    Alumne (D3): escriu, envia a la IA, rep feedback, reescriu. Opera dins l'espai dissenyat.
    Segon any: el sostre puja a N3 per a ESO-2n cicle. Tercer any: N4 per a batxillerat.

## Errors comuns — què NO fer

1.  **Presentar les 10 Quests, els 7 Rols i els 6 Nivells com a 23 conceptes iguals.** Amb la jerarquia, el docent aprèn primer les Quests (vocabulari pedagògic) i els Rols apareixen com a opcions dins cada Quest. Sense jerarquia, el docent ha d'aprendre 23 conceptes abstractes + taula de traducció.

2.  **Obviar el pas 4 (verificació de fricció).** Triar Q, R i N no garanteix aprenentatge. Cal verificar que la combinació genera fricció productiva amb els 7 criteris del marc cognitiu. El pas 4 és la comprovació final.

3.  **Aplicar la cascada com a control jeràrquic en lloc de com a disseny de seguretat.** La cascada no és "la institució mana i l'alumne obeeix". És "la institució crea un espai segur perquè docents i alumnes hi puguin experimentar amb criteri". L'autonomia de l'alumne creix progressivament.

4.  **Ignorar la doble entrada.** Si el sistema força l'entrada per Quest i el docent ja té experiència amb Rols, genera frustració i rebuig. La doble entrada és una concessió deliberada d'interfície.

5.  **Proposar una 5a D.** El disseny d'artefactes no és una competència nova; és l'exercici de les 4D a meta-nivell (N5). Afegir una 5a D trencaria l'elegància del model.

## Matissos i excepcions

*   **El nombre de Quests no és definitiu.** Les 10 de Khan/Fisher/Frey podrien consolidar-se a 6-7. La decisió queda pendent.
*   **El nombre de Rols no és definitiu.** Els 7 de Mollick podrien revisar-se. La decisió queda pendent.
*   **La matriu (Quest,Rol) × Nivell amb rangs nadius complets queda pendent** per a l'especificació operativa.
*   **Afegir camp Quest als 21 exemples de `exemples-rols-mihia.md`** queda pendent.
*   **La portabilitat a EDUCSI** (Espanya) és un objectiu explícit. El 4D×3 capes és supra-curricular precisament per això.

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M5_quests-missions-aprenentatge**: Les 10 Quests (primer nivell de l'arquitectura).
*   **M5_rols-IA-educacio**: Els 7 Rols (capa d'implementació), les 3 famílies.
*   **M5_nivells-delegacio-mihia**: Els 6 Nivells (tercer eix), sostres d'etapa, col·lapse.
*   **M2_carrega-friccio-cognitiva**: Marc cognitiu que fonamenta el pas 4 (verificació).
*   **M5_disseny-instruccional-amb-IA**: Operacionalitza la seqüència de disseny.
*   **M2_models-disseny-instruccional**: GRR, granularitat didàctica, bastida progressiva.
*   **M5_AIA-TPACK-framework**: El TPACK s'enriqueix amb la tríada Q>R>N.
*   **Marc general d'integració de la IA**: §ALUMNAT → §Aprendre AMB la IA.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Com encaixen les Quests, els Rols i els Nivells en un sol sistema?"
*   "Per què hauria de començar per la Quest i no pel Rol?"
*   "Com dissenyo la progressió d'autonomia dels meus alumnes amb la IA?"
*   "Quin paper té la institució en decidir com s'usa la IA?"
*   "Puc usar el sistema amb el currículum del meu territori?"

**Senyals de l'alumne**
*   L'alumne pregunta "per què he de fer tot aquest procés i no puc demanar directament a la IA?" — necessita entendre la cascada i la raó de la progressió.

**Senyals de context**
*   Un centre vol adoptar un marc integrat per a la integració de la IA.
*   Es forma docents i cal un vocabulari i una estructura compartida.
*   Es dissenya el catàleg d'assistents institucionals.
*   Es vol portar el marc a un altre centre, fundació o territori d'EDUCSI.

**Anti-senyals**
*   La consulta és sobre un sol rol o un sol nivell concret sense necessitat d'entendre el sistema complet.
*   El docent ja domina l'arquitectura i necessita operacionalitzar (activar M5_disseny-instruccional-amb-IA en lloc d'aquest document).

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha de presentar l'arquitectura Q>R>N com un sistema integrat on cada eix té una funció diferent, i guiar el docent perquè l'apliqui amb la seqüència de 4 passos.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Presentar la jerarquia com a simplificació, no com a complicació.**
    *   **Quan aplica:** Quan el docent percep el sistema Q>R>N com a massa complex.
    *   **Fonament:** Sense jerarquia, el docent hauria d'aprendre 23 conceptes iguals i una taula de traducció. Amb jerarquia, aprèn les Quests (vocabulari pedagògic que ja coneix parcialment) i els Rols i Nivells apareixen com a opcions dins d'un camí guiat.
    *   **Exemple complet de raonament:** Un docent diu: "Quests, Rols, Nivells, 4D... és massa!" L'agent simplificaria: "En realitat, només has de respondre 4 preguntes en ordre: (1) Què vull que passi al cap del meu alumne? (2) Com ha d'actuar la IA? (3) Quanta autonomia dono? (4) L'alumne pensarà de veritat?" El sistema guia cada resposta: la 1 et porta a una Quest, la 2 a un Rol compatible, la 3 a un Nivell dins del sostre, la 4 et verifica amb el marc cognitiu. No cal memoritzar les 10 Quests; cal fer-se les 4 preguntes.

2.  **Heurística: Aplicar la cascada quan el centre comença de zero.**
    *   **Quan aplica:** Quan un centre vol integrar la IA i no sap per on començar.
    *   **Fonament:** La cascada institució→docent→alumne és la traducció organitzativa del GRR de Fisher & Frey. La institució modela (Jo faig), els docents practiquen amb suport (Nosaltres fem), els alumnes practiquen en grup (Vosaltres feu), i finalment operen autònomament (Tu fas). Cada nivell necessita el precedent.
    *   **Exemple complet de raonament:** Un director pedagògic pregunta: "Per on comencem?" L'agent suggerira: (1) Decidiu institucionalment quins assistents tindreu, quins rols, quins nivells autoritzeu (D1 institucional). (2) Formeu els docents perquè coneguin el sistema i l'hagin usat ells mateixos. (3) Primer any: sostres conservadors (N2), rols procesuals (Mentor Socràtic, Teachable Agent). (4) Segon any: amplieu a N3 i afegiu rols mixtos. (5) Avalueu cada any: pregunta Macnamara a escala de centre ("els nostres alumnes aprenen més o menys des que usen IA?").

3.  **Heurística: Explicar les 4D×3 capes per justificar la supra-curricularitat.**
    *   **Quan aplica:** Quan cal justificar que el marc funciona per a qualsevol currículum, no només el català.
    *   **Fonament:** Les 4D (Delegació, Descripció, Discerniment, Diligència) són competències transversals que no depenen de cap matèria ni de cap legislació territorial. La lectura en 3 capes (SOBRE/PER A/AMB) permet que cada centre mapi els seus continguts curriculars a les 4D. SOBRE = contingut teòric (què és la IA), PER A = habilitat pràctica (com usar-la), AMB = aplicació a l'aprenentatge (usar-la per aprendre).
    *   **Exemple complet de raonament:** Un centre d'EDUCSI al País Basc vol adoptar el marc però té un currículum diferent del català. L'agent explicaria que les 4D no depenen del currículum sinó de la interacció humà-IA. La D3 (Discerniment) és la mateixa a Catalunya que a Euskadi: avaluar críticament el que la IA genera. El que canvia és el contingut curricular a través del qual s'exerceix. El centre basc pot mapar les seves competències transversals a les 4D i usar les Quests com a vocabulari pedagògic compartit amb la resta d'EDUCSI.

4.  **Heurística: Usar la doble entrada com a eina d'acollida, no com a excepció.**
    *   **Quan aplica:** Quan el docent arriba amb experiència prèvia en rols (Mollick) i vol usar-los directament.
    *   **Fonament:** L'ADR Xat 4 estableix que la doble entrada és deliberada, no una concessió de debilitat. El docent que entra per Rol veurà les Quests compatibles i triarà Nivell. El resultat és el mateix; el camí és diferent. Forçar l'entrada per Quest a un docent que ja domina els Rols genera fricció innecessària (i no de la productiva).
    *   **Exemple complet de raonament:** Una docent diu: "Porto un any usant la IA com a Simulador per a anglès i funciona molt bé." L'agent no li diria "has de repensar-ho en termes de Quests". Li diria: "Genial. Saps que el Simulador serveix especialment bé la Quest Mission i la Quest Perspective? Quina de les dues s'acosta més al que fas?" La docent probablement triaria Mission (resoldre reptes en context simulat). Ara té el vocabulari per comunicar-ho a companys i per verificar coherència amb el nivell i la fricció.

5.  **Heurística: No afegir la 5a D.**
    *   **Quan aplica:** Quan algú proposa que "dissenyar amb IA" hauria de ser una dimensió nova.
    *   **Fonament:** El disseny d'artefactes (chatbots, agents, aplicacions) és l'exercici de les 4D a meta-nivell. La mateixa Delegació, Descripció, Discerniment i Diligència que l'alumne exerceix quan usa un assistent, les exerceix a un nivell d'abstracció superior quan en dissenya un. Això connecta amb N5 (Agència Autònoma): l'alumne que dissenya un sistema opera al nivell més alt de les 4D, no a una dimensió nova.
    *   **Exemple complet de raonament:** Un formador proposa que "crear un chatbot" és una competència diferent de les 4D. L'agent descompondria la tasca: crear un chatbot = decidir què farà i què no (D1, Delegació), escriure el system prompt (D2, Descripció), testar si funciona bé (D3, Discerniment), assegurar que compleix normativa i protegeix dades (D4, Diligència). Són les mateixes 4D, aplicades al disseny d'un sistema en lloc de a una interacció individual. Afegir una 5a D duplicaria conceptes i trencaria l'elegància del model.

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Fer-se les 4 preguntes en ordre.**
    *   **Quan aplica:** Quan l'alumne té llibertat per triar com interactuar amb la IA.
    *   **Fonament:** La seqüència de disseny del docent es pot traduir per a l'alumne: (1) Què vull aprendre? (2) Com m'ajudarà la IA? (3) Quanta feina li dono? (4) Estic pensant jo o la IA?
    *   **Exemple complet de raonament:** Un alumne obre la IA per estudiar història. L'agent li suggerira les 4 preguntes: "Què vull aprendre? → Entendre les causes de la Revolució Francesa. Com m'ajudarà la IA? → Em farà preguntes (Mentor Socràtic). Quanta feina li dono? → Jo escric primer, la IA qüestiona (N2). Estic pensant jo o la IA? → Jo penso, la IA provoca." Ara la interacció té intenció, rol, nivell i verificació.

2.  **Heurística: Entendre que "l'espai segur" no és una restricció sinó una protecció.**
    *   **Quan aplica:** Quan l'alumne percep les limitacions dels assistents institucionals com a obstacles.
    *   **Fonament:** La cascada institucional dissenya espais segurs perquè l'alumne no caigui en rendició cognitiva abans de tenir criteri per evitar-la. L'assistent que "no dona respostes directes" no limita l'alumne; el protegeix del patró per defecte (acceptar sense pensar). A mesura que l'alumne demostra criteri, l'espai s'amplia (progressió de nivells).
    *   **Exemple complet de raonament:** Un alumne es queixa: "L'assistent del centre no em deixa generar textos directament, sempre em fa preguntes primer." L'agent li explicaria: "Això és dissenyat així perquè, segons la recerca, els alumnes que reben respostes directes de la IA milloren els productes però no aprenen (paradoxa del rendiment). L'assistent et fa preguntes perquè vol que tu pensis primer. Quan demostris que pots generar textos de qualitat tu sol, podràs usar nivells més alts d'autonomia." La restricció es converteix en una oportunitat d'aprenentatge.

3.  **Heurística: Reconèixer que el grau superior és dissenyar, no delegar.**
    *   **Quan aplica:** Quan l'alumne avançat pregunta "com puc fer més amb la IA?"
    *   **Fonament:** El grau més alt de fluïdesa no és delegar més (N4), sinó dissenyar sistemes (N5). Un alumne que dissenya un chatbot per als seus companys exerceix les 4D a meta-nivell i aplica pensament computacional. Això és el cim de la fluïdesa, no la delegació total.
    *   **Exemple complet de raonament:** Un alumne de FP Superior pregunta com pot anar més enllà. L'agent li proposaria: "En lloc d'usar l'assistent del centre, dissenya'n un tu. Defineix què farà (D1), escriu el system prompt (D2), testa si funciona bé (D3), assegura't que protegeix les dades dels usuaris (D4). Estàs operant a N5: no estàs usant la IA, estàs creant eines per a altres persones."

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | ADR Arquitectura Quest-Rol-Nivell (JE, 2026) | file://docs/decisions/arquitectura-quest-rol-nivell.md |
| 2 | Khan, S., Fisher, D., Frey, N. et al. (2025). Teaching with AI | file://upload/Khan_Fisher_Frey_2025_TeachingWithAI.pdf |
| 3 | Mollick, E. (2023). Assigning AI: Seven Approaches | https://www.oneusefulthing.org/p/assigning-ai-seven-approaches-for |
| 4 | Dakan, R. & Feller, M. Model 4D / AI Fluency | file://upload/Dakan_Feller_4D_AIFluency.pdf |
| 5 | Wiggins, G. & McTighe, J. (1998). Understanding by Design | https://www.ascd.org/books/understanding-by-design |
| 6 | docs/marcs-teorics/friccio-cognitiva-extens.md | file://docs/marcs-teorics/friccio-cognitiva-extens.md |

*6 documents font · secció generada manualment*
