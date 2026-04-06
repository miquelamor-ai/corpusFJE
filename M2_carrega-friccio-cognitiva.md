---
modul: M2
titol: "Càrrega cognitiva, fricció productiva i disseny d'activitats amb IA"
tipus: marc
descripcio: "Marc teòric integrat: paradoxa del rendiment, CLT, ICAP, fricció productiva, funcions de forçat cognitiu i criteris de disseny i auditoria d'activitats amb IA"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Definició i principis

La IA pot millorar el rendiment immediat en una tasca i, alhora, socavar l'aprenentatge durable. Aquest fenomen s'anomena **paradoxa del rendiment** (Yan et al., 2025; Bastani et al., 2025) i és la troballa empírica més sòlida de la recerca sobre IA i aprenentatge. La resposta no és prohibir ni acceptar acríticament, sinó dissenyar activitats i assistents que preservin la càrrega cognitiva que genera aprenentatge i externalitzin únicament la que no hi aporta valor.

Les decisions sobre la IA en l'aprenentatge no són tecnològiques, sinó pedagògiques sobre qui fa la feina cognitiva. Com ha formulat Paul McCrea: *qui fa el pensament, s'emporta l'aprenentatge* (*cognitive ownership*).

### Arquitectura cognitiva

L'aprenentatge depèn de construir i modificar **esquemes mentals**. Construir esquemes exigeix processar informació amb la memòria de treball (capacitat limitada: ~4 elements en processament actiu). Qualsevol eina — inclosa la IA — que faci aquesta feina per l'alumne impedeix que es construeixi l'esquema. Es pot completar la tasca amb èxit, però la memòria a llarg termini no canviarà.

### Teoria de la Càrrega Cognitiva (CLT)

La CLT (Sweller, 1988; actualitzada per Kalyuga & Plass, 2025) distingeix tres tipus de càrrega:

*   **Càrrega intrínseca**: la dificultat inherent al contingut. No s'ha de reduir si és pedagògicament necessària.
*   **Càrrega extrínseca**: la dificultat afegida per mal disseny (format confús, distraccions). Cal minimitzar-la.
*   **Càrrega germana**: l'esforç actiu que genera aprenentatge profund (elaboració, connexió, síntesi). No s'ha d'eliminar — és la fricció productiva.

Principi CLT: reduir càrrega extrínseca per alliberar capacitat de treball i destinar-la a la càrrega germana. Kalyuga i Plass (2025) afegeixen que la motivació de l'alumne influeix en com distribueix l'esforç cognitiu: sense objectiu propi, l'alumne tendeix a minimitzar l'esforç i externalitzar la càrrega a qualsevol eina disponible.

### ICAP: modes d'implicació cognitiva (Chi & Wylie, 2014)

Quatre modes, de menor a major potencial d'aprenentatge: **Passiu** (rep sense fer res) < **Actiu** (selecciona, subratlla) < **Constructiu** (genera output nou que va més enllà del material) < **Interactiu** (construeix conjuntament en diàleg iteratiu). Un assistent que genera contingut i l'alumne el consumeix = Passiu/Actiu. Un assistent que força l'alumne a generar i hi dialoga = Constructiu/Interactiu. L'eix ICAP mesura directament si la IA augmenta o substitueix el pensament.

### La paradoxa del rendiment

Bastani et al. (2025, N≈1.000): alumnes amb GPT obert van millorar el rendiment mentre el tenien, però quan es va retirar van obtenir resultats pitjors que alumnes que mai l'havien tingut. Amb GPT configurat com a tutor amb guardrails pedagògics, la caiguda va desaparèixer. El factor causal és la pedagogia del disseny, no la presència de la IA.

### Mecanismes de la paradoxa

*   **Rendició cognitiva** (Shaw & Nave, 2026): l'usuari adopta els outputs de la IA amb escrutini mínim, anul·lant intuïció i deliberació. Evidència: 3 experiments preregistrats, N=1.372, Cohen's h=0,81 (molt gran). La confiança augmentava fins i tot quan la IA duia a error.
*   **Tres il·lusions** (Messeri & Crockett, 2024): il·lusió de profunditat explicativa, d'amplitud exploratòria i d'objectivitat.
*   **Decadència d'habilitats** (Macnamara et al., 2024): *skill decay* en experts i *skill development hindrance* en aprenents. Crossover point: per sota del 70% d'encert, l'automatització degrada el rendiment (Parasuraman & Manzey, 2010).
*   **Mandra metacognitiva** (Fan et al., 2024): els alumnes redueixen planificació, monitoratge i avaluació quan els outputs de la IA estan disponibles.
*   **Il·lusió de competència** (Lodge, 2023): la fluïdesa de la IA es confon amb profunditat d'aprenentatge.
*   **Bretxa d'equitat metacognitiva** (Lodge & Loble, 2026): els alumnes amb menys habilitats metacognitives fan més descàrrega detrimental. La IA pot amplificar desigualtats educatives.

### Principis de disseny

*   **Dificultats desitjables** (Bjork & Bjork): condicions que alenteixen l'adquisició inicial però milloren la retenció i la transferència. S2D2 framework (de Bruin et al., 2023): començar amb dificultat desitjable i quedar-s'hi.
*   **Fracàs productiu** (Kapur, 2008+; metaanàlisi 160 estudis, Sinha & Kapur, 2021): deixar que l'alumne fracassi abans d'instruir-lo. Les 4 A: Activació, Consciència, Afecte, Assemblatge. Fort en matemàtiques i ciències; requereix fase consolidativa posterior.
*   **Efecte generació** (Slamecka & Graf, 1978; Duplice, 2025): generar una resposta produeix millor retenció que rebre-la passivament.
*   **Propietat cognitiva** (McCrea, 2025): l'autoria no és només ètica sinó cognitiva — aprendre exigeix que l'alumne hagi pensat.

### Eines de disseny

**Fricció productiva** (Novokshanova, 2025): 3 moviments (Descoberta, Recursivitat, Resistència) + 3 fallades (Col·lapse, Desalineació, Delegació). Mapa de diagnòstic operatiu per dissenyar i avaluar activitats.

**Funcions de forçat cognitiu (CFF)** (Croskerry, 2003; Buçinca, Malaya & Gajos, 2021): 6 tècniques — pre-compromís, justificació prèvia, predicció, avaluació obligatòria, restricció, comparació múltiple. Operacionalitzables a nivell d'assistent: indicadors de confiança, primer demana-després suggereix, explicabilitat activa (XAI), confirmació de detalls crítics.

### Set criteris de disseny

1. L'activitat té un objectiu cognitiu explícit (quin esquema ha de construir l'alumne)
2. La IA es destina a reduir càrrega extrínseca, no germana
3. Hi ha un moment de generació autònoma abans que la IA entri
4. Hi ha una CFF activa
5. L'activitat indueix almenys un dels 3 moviments de fricció productiva
6. El mode ICAP resultant és Constructive o Interactive
7. Es pot avaluar l'aprenentatge sense IA

### Vuit preguntes d'auditoria

1. Quina càrrega s'externalitza? (Extrínseca → bo. Intrínseca → risc.)
2. L'alumne ha generat alguna cosa abans? (No → risc de paradoxa del rendiment.)
3. Hi ha CFF identificable? (No → risc de rendició cognitiva.)
4. Mode ICAP? (Passive/Active → reformular.)
5. En 10 repeticions, millorarà o perdrà l'habilitat? (pregunta Macnamara)
6. L'alumne ho pot fer sense IA? (No → risc de dependència.)
7. L'avaluació discrimina rendiment/aprenentatge? (No → cega a la paradoxa.)
8. Fiabilitat de l'assistent auditada? (Si < 70% → crossover point.)

### Criteris de disseny d'assistents institucionals

| Criteri | Descripció | 4D |
|---|---|---|
| A | No dóna solucions quan la solució és l'objectiu d'aprenentatge | D1 |
| B | Incorpora CFF per defecte (pregunta abans de respondre) | D2 |
| C | És auditor, no només productor | D3 |
| D | Rang de nivells N autoritzats per etapa | D1 |
| E | Alineat amb Quests i Rols explícits | D1+D2 |
| F | Desencoratja la rendició cognitiva | D2+D3 |
| G | Comportament pedagògic per defecte | D2 |
| H | Autoauditoria periòdica (crossover point 70%) | D3 |

## Autors i evidència clau

*   **Sweller (1988); Kalyuga & Plass (2025)**: Teoria de la Càrrega Cognitiva (CLT), amb actualització motivacional per a l'era IA.
*   **Chi & Wylie (2014)**: ICAP — modes d'implicació cognitiva (Passive < Active < Constructive < Interactive).
*   **Bastani et al. (2025, N≈1.000)**: Estudi randomitzat que demostra la paradoxa del rendiment — GPT obert perjudica aprenentatge durable, GPT tutor no.
*   **Shaw & Nave (2026, N=1.372)**: Rendició cognitiva i Tri-System Theory (Sistema 3). Cohen's h=0,81.
*   **Messeri & Crockett (2024)**: Tres il·lusions (profunditat, amplitud, objectivitat).
*   **Macnamara et al. (2024)**: Skill decay i skill development hindrance. Crossover point (Parasuraman & Manzey, 2010): 70%.
*   **Fan et al. (2024, 2025)**: Metacognitive laziness.
*   **Lodge (2023); Lodge & Loble (2026)**: Il·lusió de competència. Bretxa d'equitat metacognitiva. Offloading beneficiós vs. detrimental.
*   **Bjork & Bjork (1994, 2011)**: Dificultats desitjables. S2D2 (de Bruin et al., 2023).
*   **Kapur (2008+); Sinha & Kapur (2021, 160 estudis)**: Fracàs productiu.
*   **Novokshanova (2025)**: Fricció productiva (3 moviments + 3 fallades).
*   **McCrea (2025)**: Propietat cognitiva ("whoever does the thinking gets the learning").
*   **Croskerry (2003); Buçinca, Malaya & Gajos (2021)**: Funcions de forçat cognitiu.
*   **Chase & Galvin (2026)**: Disseny = avaluació. Respostes estructurals vs. discursives.
*   **Tai et al. (2018)**: Judici avaluatiu.
*   **Iqbal et al. (2025, N=465)**: Metacognició compartida vs. delegada.

## Exemples concrets d'aplicació a l'aula

1.  **ESO (14 anys): Text argumentatiu amb Crític/Editor a N2.**
    L'alumne escriu un text argumentatiu sobre els mòbils a l'institut (400 paraules). Després l'envia a la IA amb el prompt: "Assenyala 3 punts febles d'estructura, arguments i connectors. No reescriguis res, només explica." L'alumne rep el feedback, decideix quins canvis fa i reescriu ell mateix. CFF activa: pre-compromís (l'alumne ha escrit abans). Moviment de fricció: Resistència (ha de justificar si accepta o rebutja cada suggeriment). Mode ICAP: Constructive. Càrrega externalitzada: extrínseca (detecció d'errors), preservada: germana (reescriptura).

2.  **Batxillerat (17 anys): Dilema ètic amb Contrincant a N3.**
    L'alumne escriu la seva posició sobre cotxes autònoms (300 paraules). L'envia a la IA: "Defensa la posició contrària amb 3 contraarguments sòlids." L'alumne respon refutant. Iteració de 5-6 rondes, cada cop des d'un angle diferent. CFF: pre-compromís + avaluació obligatòria. Moviment: Resistència + Recursivitat. Mode ICAP: Interactive. L'alumne NO hauria de demanar "genera un debat complet" (seria N4, col·lapse del rol procesual).

3.  **FP Grau Mitjà (Cuina): Fitxa tècnica amb Crític a N2.**
    L'alumne crea la fitxa tècnica d'una crema catalana. L'envia a la IA: "Revisa gramatges, temps de cocció i passos. No reescriguis la fitxa, indica què corregir." L'alumne valida el feedback contrastant amb literatura gastronòmica i corregeix. CFF: pre-compromís. Moviment: Resistència (decidir si accepta correccions tècniques). Càrrega externalitzada: extrínseca (verificació numèrica), preservada: germana (competència de documentació tècnica).

## Errors comuns — què NO fer

1.  **Permetre que la IA generi el producte que l'alumne havia d'aprendre a fer.** Si l'objectiu és que l'alumne aprengui a redactar textos argumentatius, la IA no ha de redactar el text. Pot donar feedback, fer preguntes o generar contraarguments, però la generació del text és la càrrega germana que construeix l'aprenentatge. Quan la IA genera i l'alumne consumeix, el mode ICAP cau a Passiu i la paradoxa del rendiment s'activa.

2.  **Confondre un bon producte amb un bon aprenentatge.** Que l'alumne entregui un assaig excel·lent no vol dir que hagi après a escriure'l. Bastani et al. demostren que el rendiment immediat pot millorar alhora que l'aprenentatge durable empitjora. L'avaluació ha de discriminar entre el producte (amb IA) i la competència (sense IA).

3.  **No incloure cap CFF.** Sense una funció de forçat cognitiu, la rendició cognitiva és el patró per defecte. L'alumne accepta el primer output i l'entrega. Cada interacció amb la IA ha de tenir un mecanisme que obligui a aturar-se i reflexionar.

4.  **Usar rols procesuals a N4.** Mentor Socràtic, Teachable Agent i Contrincant col·lapsen a N4: la IA genera el diàleg complet i l'alumne llegeix un producte. El rol perd la seva essència. Només acceptable si l'objectiu és aprendre enginyeria de prompts.

5.  **Assumir que la IA és fiable sense auditar-la.** Si l'assistent no supera el 70% d'encert en el domini (crossover point, Macnamara/Parasuraman), pot estar fent més mal que bé. Cal mecanismes periòdics de verificació.

## Matissos i excepcions

*   **No tota la fricció és desitjable.** La fricció que prové de mal disseny (instruccions confuses, interfície complicada, format incoherent) és càrrega extrínseca, no germana. La IA SÍ ha de reduir aquesta fricció. La pregunta és: "aquesta dificultat construeix aprenentatge o distreu?"

*   **El fracàs productiu no és universal.** Fort en matemàtiques i ciències; menys evident en humanitats, llengües o arts. Requereix fase d'instrucció consolidativa posterior. Alumnes amb baixa autoeficàcia poden patir frustració excessiva si no hi ha bastides afectives.

*   **El nivell de fricció ha de ser personalitzat.** El que és fricció productiva per a un alumne pot ser aclaparador per a un altre. La bretxa d'equitat metacognitiva (Lodge & Loble) implica que els alumnes amb menys habilitats metacognitives necessiten més estructura, no menys.

*   **N4 no és dolent per defecte.** Quan l'alumne domina el contingut i la IA genera material auxiliar (no l'objectiu d'aprenentatge), N4 és delegació legítima. El problema és quan N4 s'aplica a càrrega germana.

*   **No totes les activitats necessiten IA.** N0 (no delegació) és una decisió tan legítima com qualsevol altra. A vegades la millor opció pedagògica és que l'alumne treballi sense cap eina.

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M5_arquitectura-quest-rol-nivell**: La seqüència de disseny del docent inclou verificar la fricció productiva com a pas 4. L'arquitectura Q>R>N s'ha de complementar amb els 7 criteris de disseny d'aquest marc.
*   **M5_rols-IA-educacio**: Les 3 famílies de rols (procesuals, mixtos, productius) deriven de l'anàlisi de quina càrrega externalitzen i quina fricció generen. El col·lapse a N4 dels rols procesuals s'explica des d'aquest marc.
*   **M5_nivells-delegacio-mihia**: El nivell de delegació determina quina càrrega s'externalitza. Cada nivell té un perfil de fricció diferent documentat en aquest marc.
*   **M5_quests-missions-aprenentatge**: Cada Quest s'associa a moviment de fricció, càrrega externalitzada i mode ICAP. La taula Quest × Fricció × ICAP es fonamenta en aquest marc.
*   **M5_disseny-instruccional-amb-IA**: Els 7 criteris de disseny i les 8 preguntes d'auditoria s'operacionalitzen en la plantilla de disseny.
*   **M2_DUA-principis-pautes**: El DUA proporciona múltiples mitjans de representació, acció i expressió que ajuden a gestionar la càrrega cognitiva per a la diversitat de l'alumnat.
*   **M2_models-disseny-instruccional**: GRR, LRI i bastida progressiva de prompts.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Els meus alumnes lliuren treballs excel·lents però no saben explicar-me com els han fet."
*   "Des que usen IA, els productes són millors però noto que aprenen menys."
*   "Com decideixo si en aquesta activitat la IA ajuda o perjudica?"
*   "Vull que els alumnes pensin, no que la IA pensi per ells."
*   "Necessito criteris per auditar si les activitats amb IA que fem funcionen."
*   "Com configuro un assistent que ensenyi en lloc de resoldre?"

**Senyals de l'alumne**
*   Accepta el primer output de la IA sense llegir-lo completament ni qüestionar-lo.
*   No modifica ni personalitza el resultat generat.
*   Ha millorat els productes però no pot fer la tasca sense IA.
*   Expressa frases com "fes-me el resum", "dona'm la resposta", "escriu-me un text sobre...".
*   Mostra confiança desproporcionada en les seves capacitats (il·lusió de competència).

**Senyals de context**
*   S'està introduint IA generativa en activitats d'aprenentatge per primera vegada.
*   Es debat si prohibir o permetre l'ús de IA en tasques avaluatives.
*   Es dissenyen assistents institucionals (chatbots, custom GPTs, agents).
*   S'observa una discrepància entre qualitat dels productes i resultats en avaluacions sense IA.
*   Es planifica formació docent sobre integració de la IA.

**Anti-senyals**
*   L'alumne usa la IA per a tasques purament mecàniques (format, ortografia, organització) sense implicació cognitiva profunda. Això és descàrrega beneficiosa, no cal intervenir.
*   El docent pregunta sobre aspectes tècnics de la IA (com funciona un LLM, què és un token) sense connexió amb disseny d'activitats pedagògiques.
*   La consulta és sobre regulació o normativa d'ús de IA, no sobre disseny pedagògic.
*   L'alumne ja domina el contingut i usa la IA com a eina de productivitat professional (delegació legítima a N4).

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha de guiar el docent perquè preservi la càrrega cognitiva que genera aprenentatge i dissenyi activitats on l'alumne pensi activament amb la IA, no passivament davant la IA.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Auditar la càrrega externalitzada.**
    *   **Quan aplica:** Quan un docent proposa una activitat amb IA i cal verificar si el disseny és sòlid.
    *   **Fonament:** La distinció entre descàrrega beneficiosa i detrimental (Lodge & Loble, 2026) és el criteri diagnòstic central. Si la IA s'emporta càrrega extrínseca (format, sintaxi, organització), allibera memòria de treball per a processos d'ordre superior. Si s'emporta càrrega intrínseca o germana (anàlisi, síntesi, generació), bypassa la construcció d'esquemes i l'aprenentatge s'atura.
    *   **Exemple complet de raonament:** Una docent de llengua proposa que els alumnes escriguin un text argumentatiu i la IA el corregeixi gramaticalment. L'agent analitzaria que la correcció gramatical és càrrega extrínseca (no és l'objectiu d'aprenentatge, que és argumentar), per tant la descàrrega és beneficiosa. Però si la docent proposa que la IA "millori l'argumentació", l'agent alertaria que argumentar és la càrrega germana que l'alumne ha de fer per aprendre. Suggerira que la IA assenyali febleses sense reescriure, per preservar la propietat cognitiva de l'alumne sobre l'estructura argumental.

2.  **Heurística: Verificar que hi ha generació autònoma prèvia.**
    *   **Quan aplica:** Quan l'activitat proposa que l'alumne interactuï amb la IA des del principi.
    *   **Fonament:** L'efecte generació (Slamecka & Graf, 1978; Duplice, 2025) demostra que generar una resposta activament produeix millor retenció que rebre-la passivament. El fracàs productiu (Kapur) afegeix que la lluita prèvia activa coneixements previs i revela buits cognitius. Si la IA entra massa aviat, l'alumne no té ocasió de fer els moviments d'Activació i Consciència.
    *   **Exemple complet de raonament:** Un docent de ciències vol que els alumnes explorin el canvi climàtic amb un Mentor Socràtic. L'agent suggerira que, abans de dialogar amb la IA, cada alumne escrigui en 5 minuts el que sap sobre el tema (pre-compromís). Això activa l'efecte generació: l'alumne construeix un primer esquema propi. Quan després la IA li fa preguntes socràtiques, l'alumne té un punt de referència per comparar, i la Descoberta (veure buits que no veia) és molt més potent que si la IA hagués començat de zero.

3.  **Heurística: Diagnosticar amb el semàfor de fricció.**
    *   **Quan aplica:** Quan cal avaluar ràpidament si una activitat existent genera aprenentatge o rendiment.
    *   **Fonament:** Novokshanova (2025) articula tres moviments de fricció productiva (Descoberta, Recursivitat, Resistència) i tres modes de fallada (Col·lapse, Desalineació, Delegació). Observar quins moviments realment es produeixen durant la interacció amb la IA és el diagnòstic més operatiu que tenim per distingir activitats on l'alumne pensa d'activitats on l'alumne consumeix.
    *   **Exemple complet de raonament:** Un docent descriu una activitat on els alumnes pregunten a la IA sobre un tema i copien les respostes. L'agent diagnosticaria Col·lapse (surt del bucle al primer output) + Delegació (no exerceix control). Suggerira reformular: l'alumne primer ha d'escriure la seva posició (pre-compromís), després la IA contradiu (Resistència), l'alumne respon i la IA torna a qüestionar (Recursivitat). Ara els tres moviments estan actius, i el mode ICAP puja d'Actiu a Interactiu.

4.  **Heurística: Incorporar CFF al disseny de l'activitat i de l'assistent.**
    *   **Quan aplica:** Quan es dissenya una nova activitat amb IA o es configura un assistent institucional.
    *   **Fonament:** Buçinca, Malaya i Gajos (2021) demostren experimentalment que les CFF redueixen l'excés de confiança en les respostes de la IA. Sense CFF, la rendició cognitiva és el patró per defecte: l'alumne accepta el primer output i l'entrega. Les CFF no són opcionals; són la condició mínima per evitar que la IA degradi l'aprenentatge.
    *   **Exemple complet de raonament:** Un centre vol crear un assistent institucional per a pràctica de llengües. L'agent recomanaria que l'assistent incorpori CFF al seu comportament per defecte: no mostra cap suggeriment fins que l'alumne ha escrit les primeres línies (primer demana, després suggereix); quan corregeix, explica per què (explicabilitat activa); davant d'un "tradueix-me això", respon amb "primer intenta-ho tu i jo t'ajudo amb el que et costi" (desencoratjament de rendició cognitiva). Aquestes CFF es codifiquen al system prompt de l'assistent, no depenen del docent.

5.  **Heurística: Separar rendiment d'aprenentatge en l'avaluació.**
    *   **Quan aplica:** Quan el docent avalua activitats on l'alumne ha usat IA i cal determinar si ha après.
    *   **Fonament:** Soderstrom i Bjork (2015) demostren que les condicions que milloren el rendiment sovint empitjoren l'aprenentatge. Chase i Galvin (2026) argumenten que una activitat en què la IA pot fer el treball cognitiu nuclear no és un problema ètic, és un problema de disseny: l'activitat ja no mesura el que pretén mesurar. L'avaluació ha d'incloure almenys una dimensió on l'alumne demostri la competència sense accés a l'assistent.
    *   **Exemple complet de raonament:** Un docent observa que des que els alumnes usen IA, les notes dels treballs han pujat, però els exàmens presencials no milloren. L'agent diagnosticaria paradoxa del rendiment: el producte és millor però l'alumne no ha millorat. Suggerira dos ajustaments: (1) redissenyar l'activitat amb IA perquè la IA no faci la part que s'avalua, i (2) incloure una fase d'avaluació sense IA que mesuri la transferència real. La pregunta clau per al docent seria: "L'alumne ha millorat el producte o ha millorat ell mateix com a aprenent?"

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Escriure primer, preguntar després.**
    *   **Quan aplica:** Quan l'alumne vol consultar la IA sobre un tema que està aprenent.
    *   **Fonament:** L'efecte generació demostra que generar una resposta pròpia abans de consultar una font externa millora significativament la retenció. L'esforç de recuperar el que ja es coneix (retrieval practice) és una de les dificultats desitjables més robustes. Si l'alumne pregunta a la IA sense haver intentat primer, se salta exactament el procés que construiria l'aprenentatge.
    *   **Exemple complet de raonament:** Un alumne de batxillerat ha de preparar un tema sobre la Revolució Francesa. Abans de preguntar a la IA, l'agent li suggerira que escrigui tot el que recorda del tema en 5 minuts, sense consultar res. Després, pot demanar a la IA: "He escrit això sobre la Revolució Francesa. Què em falta? Quins errors tinc?" D'aquesta manera, la IA actua com a Crític del seu coneixement previ, no com a generador d'un resum que l'alumne no ha construït. L'alumne detecta buits (Descoberta) i millora el seu esquema iterativament (Recursivitat).

2.  **Heurística: No acceptar el primer resultat.**
    *   **Quan aplica:** Quan l'alumne rep una resposta de la IA i tendeix a copiar-la directament.
    *   **Fonament:** La rendició cognitiva (Shaw & Nave, 2026) demostra que el patró per defecte és acceptar l'output amb escrutini mínim. Exigir-se a un mateix trobar almenys un error o una feblesa en la resposta de la IA és un acte de Resistència que activa el pensament crític. La IA genera informació versemblant, no necessàriament correcta; l'alumne que ho dóna per bo sense verificar no aprèn a discernir.
    *   **Exemple complet de raonament:** Un alumne ha demanat a la IA un resum de la fotosíntesi. L'agent li suggeriria: "Abans d'usar-lo, intenta trobar alguna cosa que la IA hagi simplificat massa o que no sigui del tot exacta." L'alumne rellegeix amb ull crític, potser detecta que la IA ha dit "les plantes converteixen CO₂ en oxigen" sense explicar el paper de l'aigua. Ara l'alumne ha exercit judici avaluatiu (Tai et al., 2018), ha practicat Resistència, i ha construït un esquema més complet que si hagués copiat el resum directament.

3.  **Heurística: Reconèixer quan NO usar la IA.**
    *   **Quan aplica:** Quan l'alumne vol usar la IA per a una tasca que hauria de fer sol per aprendre.
    *   **Fonament:** La delegació (D1 del Model 4D) no és sempre "usar la IA"; és decidir amb criteri quan usar-la i quan no. Macnamara et al. (2024) demostren que les habilitats que no es practiquen es degraden. Si l'alumne sempre redacta amb IA, perd la capacitat de redactar. La pregunta clau és: "si faig aquesta tasca 10 vegades amb IA, milloraré la meva habilitat o la perdré?"
    *   **Exemple complet de raonament:** Un alumne de FP vol usar la IA per redactar un correu professional a un client. L'agent li preguntaria: "Saps redactar aquest correu tu sol? Si sí, potser la IA et pot revisar l'ortografia (càrrega extrínseca) però la redacció hauries de fer-la tu per mantenir la competència. Si no saps, primer intenta-ho tu sol, envia'l a la IA per feedback, i reescriu tu la versió final." La IA com a Crític (N2) en lloc de com a Generador (N4) preserva la pràctica de l'habilitat que l'alumne necessita per a la seva professió.

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | Bastani, H. et al. (2025). Generative AI Can Harm Learning | https://doi.org/10.1287/mnsc.2024.01316 |
| 2 | Shaw, S. D. & Nave, G. (2026). Cognitive Surrender. Wharton School | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646 |
| 3 | Novokshanova, E. (2025). Productive Friction in Human-AI Feedback. GSU | file://upload/Novokshanova_2025_ProductiveFriction.pdf |
| 4 | Macnamara, B. N. et al. (2024). Skill Decay and AI | https://doi.org/10.1186/s41235-024-00579-x |
| 5 | Lodge, J. M. & Loble, L. (2026). Cognitive Offloading and Education. UTS | file://upload/Lodge_Loble_2026_CognitiveOffloading.pdf |
| 6 | Chase, A.-M. & Galvin, K. (2026). Thinking to Learn. AEHE | file://upload/Chase_Galvin_2026_ThinkingToLearn.pdf |
| 7 | McCrea, P. (2025). Cognitive Ownership | file://upload/McCrea_2025_CognitiveOwnership.pdf |
| 8 | Kapur, M. (2008+). Productive Failure | https://doi.org/10.1007/s10339-011-0396-z |
| 9 | Chi, M. T. H. & Wylie, R. (2014). ICAP Framework | https://doi.org/10.1080/00461520.2014.965823 |
| 10 | Sweller, J. (1988). Cognitive Load Theory | https://doi.org/10.1207/s15516709cog1202_4 |
| 11 | Messeri, L. & Crockett, M. J. (2024). Three Illusions of AI | https://doi.org/10.1038/s41586-024-07146-0 |
| 12 | Buçinca, Z., Malaya, M. B. & Gajos, K. Z. (2021). Cognitive Forcing Functions | https://doi.org/10.1145/3411764.3445379 |
| 13 | docs/marcs-teorics/friccio-cognitiva-extens.md | file://docs/marcs-teorics/friccio-cognitiva-extens.md |

*13 documents font · secció generada manualment*
