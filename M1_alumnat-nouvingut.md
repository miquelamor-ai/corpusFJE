---
modul: M1
titol: "Alumnat nouvingut — Perfil"
tipus: caracteristica
subtipus: contextual
descripcio: "Perfil, barreres, necessitats i principis d'actuació per a l'alumnat que s'incorpora al sistema educatiu. Inclou marcs teòrics (BICS/CALP, translanguaging, dol migratori), normativa vigent (D150/2017, D175/2022), protocol de derivació, perfil 2a generació i heurística d'escolarització nul·la."
review_status: revisat
generat_at: 2026-03-18T13:30:00
actualitzat_at: 2026-04-20T00:00:00
variables_configurables:
  - nom: L1
    etiqueta: "Llengua materna (L1)"
    tipus: text
    obligatori: true
    descripcio: "Idioma principal de l'alumne"
    impacte: "Determina la distància lingüística i els suports de traducció"
  - nom: familia_linguistica
    etiqueta: "Família lingüística"
    tipus: enum
    valors: [romanica, germanica, eslava, araboberber, sinotibetana, altra]
    obligatori: false
    defecte: null
    descripcio: "Es pot inferir automàticament de la L1. Indica la distància amb el català"
    impacte: "A més distància, més suport visual i estructural necessari"
  - nom: alfabet_llati
    etiqueta: "Alfabet llatí"
    tipus: boolean
    obligatori: true
    defecte: true
    descripcio: "L'alumne està alfabetitzat en alfabet llatí?"
    impacte: "Si no: cal suport visual reforçat, tipografia més gran, evitar text dens"
  - nom: escolaritzacio_previa
    etiqueta: "Escolarització prèvia"
    tipus: enum
    valors: [si, parcial, no]
    obligatori: true
    defecte: si
    descripcio: "Ha estat escolaritzat regularment al país d'origen?"
    impacte: "Sense escolarització: cal bastida cognitiva bàsica, no només lingüística"
  - nom: mecr
    etiqueta: "Nivell de català (MECR)"
    tipus: enum
    valors: [pre-A1, A1, A2, B1, B2]
    obligatori: true
    defecte: A1
    descripcio: "Nivell de competència en català segons el Marc Europeu"
    impacte: "Determina la complexitat lingüística màxima del text de sortida"
  - nom: calp
    etiqueta: "Llengua acadèmica (CALP)"
    tipus: enum
    valors: [inicial, emergent, consolidat]
    obligatori: false
    defecte: inicial
    descripcio: "Competència en llenguatge acadèmic (diferent del conversacional)"
    impacte: "Inicial: vocabulari acadèmic amb definicions integrades. Consolidat: termes tècnics sense bastida"
---

## Descripció de la situació
L'alumnat nouvingut és aquell que s'incorpora al sistema educatiu català havent estat escolaritzat prèviament en un altre sistema educatiu, sovint en un context cultural i lingüístic diferent. Aquest perfil ha experimentat un creixement continuat i significatiu en els darrers anys, passant de ser gairebé anecdòtic a principis dels anys noranta a representar un percentatge notable de l'alumnat, amb una distribució irregular al territori. Aquest perfil és extremadament heterogeni, ja que la "diversitat cultural és una de les múltiples diversitats que conformen la societat complexa" (DOC 2). No es tracta d'un grup homogeni, sinó d'individus amb "identitats de múltiples pertinences" (DOC 1, DOC 3), resultat de diverses identificacions flexibles i canviants. Generalment, la incorporació es produeix en els darrers vint-i-quatre mesos, o excepcionalment en els darrers trenta-sis mesos, especialment si procedeixen d'àmbits lingüístics i culturals molt allunyats del nostre. La seva arribada, especialment en les darreres dècades, ha estat ràpida i creixent, abastant totes les comarques catalanes (DOC 5). Aquest alumnat pot provenir de més de 150 estats diferents, amb experiències educatives prèvies molt variades, des de sistemes d'alta qualitat fins a escolaritzacions intermitents o inexistents. Aquesta diversitat s'amplifica amb factors socioeconòmics, d'edat i de gènere, que es combinen i fan difícil identificar grups culturals o socials uniformes (DOC 2). La globalització ha accelerat aquesta mobilitat, fent que les distàncies s'escurcin i la circulació d'informació i persones sigui extraordinària (DOC 4). Per tant, el perfil de l'alumnat nouvingut no es defineix per un origen comú, sinó per la seva recent incorporació i la necessitat d'adaptació a un nou entorn educatiu, social i lingüístic.

##### Marc normatiu vigent a Catalunya

- **Decret 150/2017**, de 17 d'octubre, de l'atenció educativa a l'alumnat en el marc d'un sistema educatiu inclusiu (DOGC 7477). Estableix el marc general d'atenció a la diversitat i els principis d'inclusió que regulen l'actuació amb tot l'alumnat, inclòs el nouvingut.
- **Decret 175/2022**, d'ordenació dels ensenyaments de l'educació bàsica. **Art. 24.8**: informes qualitatius trimestrals individuals obligatoris per a l'alumnat nouvingut. Aquests informes han de reflectir l'evolució lingüística, curricular i socioemocional.
- **Gestió del centre. Curs 2025-2026** (instruccions operatives del Departament d'Educació). Concreta les actuacions dels centres per al curs vigent, incloent-hi protocols d'acollida, recursos d'aula d'acollida i coordinació amb els serveis educatius.
- **Programa LIC-CCE** (Llengua, Interculturalitat i Cohesió Social — Centre de Competència Educativa). Programa institucional de la XTEC que estructura la formació docent, els recursos i els protocols per a l'atenció lingüística i la cohesió social als centres educatius catalans.

##### Marcs teòrics de referència

**1. BICS / CALP (Cummins, 1979–2000)**

Distinció fonamental entre les habilitats comunicatives bàsiques interpersonals (*Basic Interpersonal Communicative Skills*, BICS) i la competència lingüística acadèmica cognitiva (*Cognitive Academic Language Proficiency*, CALP). Les BICS s'adquireixen en 1-3 anys d'immersió i permeten la comunicació quotidiana; la CALP requereix 5-8 anys i és imprescindible per al rendiment acadèmic. **Implicació clau**: no confondre la fluïdesa oral amb la competència acadèmica. Un alumne que conversa amb naturalitat pot seguir necessitant suport intensiu per comprendre textos acadèmics. La variable `calp` del frontmatter opera sobre aquesta distinció: un valor `inicial` indica que l'alumne pot tenir BICS però manca de CALP; `consolidat` implica que el llenguatge acadèmic ja és funcional.

**2. Distància lingüística i alfabets**

La distància tipològica entre la L1 de l'alumne i el català determina la velocitat d'adquisició i el tipus de suport necessari. La variable `familia_linguistica` del frontmatter infereix automàticament aquesta distància. Cinc nivells de referència:

| Família lingüística | Distància amb el català | Exemples | Implicació |
|---|---|---|---|
| Romàniques | Mínima | Castellà, portuguès, italià, romanès | Transferència directa de lèxic i estructures |
| Germàniques | Moderada | Anglès, alemany, neerlandès | Estructures sintàctiques divergents, lèxic parcialment compartit |
| Eslaves | Alta | Ucraïnès, rus, polonès | Alfabet pot ser diferent (ciríl·lic), gramàtica molt divergent |
| Àrab-berber | Molt alta | Àrab, amazic, darija | Alfabet no llatí, direccionalitat d'escriptura inversa, fonologia molt diferent |
| Sinotibetanes | Màxima | Xinès mandarí, cantonès | Sistema logogràfic, tonalitat, absència de flexió morfològica |

**3. Translanguaging (García & Wei, 2014; Cen Williams, 1994)**

Marc que concep el repertori lingüístic de l'alumne com un sistema integrat, no com a llengües separades en compartiments estancs. Principis clau:
- La L1 és una bastida cognitiva, no un obstacle: pensar en L1 per produir en L2 és un procés natural i productiu.
- L'ús estratègic de les llengües de l'alumne redueix la càrrega cognitiva i facilita la comprensió de conceptes complexos.
- Les pràctiques de translanguaging (permetre apunts en L1, glossaris bilingües, debats amb codi mixt) són pedagogia legítima, no un dèficit.
- **Connexió amb el corpus**: M3_translanguaging-plurilinguisme.md desenvolupa aquest marc en profunditat.

**4. Dol migratori (Achotegui, 1999–2017)**

El procés migratori implica 7 tipus de dol: família, llengua, cultura, terra, estatus social, grup de pertinença i riscos per a la integritat física. Quan les condicions d'acollida són adverses (irregularitat administrativa, aïllament, racisme), el dol pot esdevenir el **Síndrome d'Ulisses**: un quadre d'estrès crònic amb símptomes d'ansietat, depressió, somatitzacions i confusió. Dades rellevants: els fills i filles de famílies migrades presenten índexs de salut mental més elevats que la població general, especialment quan acumulen factors de vulnerabilitat. **Implicació per al corpus**: el component emocional no és un complement de l'atenció educativa, sinó un **prerequisit**. Sense estabilitat emocional, les intervencions lingüístiques i curriculars perden efectivitat. L'heurística "L'àncora emocional" (secció 4) opera directament sobre aquest marc.

## Manifestació per etapa educativa

*   **Infantil/Primària:** En aquesta etapa, la barrera lingüística pot ser molt evident, afectant la comprensió de les instruccions i la interacció amb els companys. Els infants poden mostrar dificultats per seguir el ritme de l'aula, necessitar més suport visual i gestual, i tenir períodes d'adaptació emocional més intensos, manifestant timidesa o, en alguns casos, frustració. La socialització pot ser un repte inicial, tot i que la plasticitat d'aquesta edat sol afavorir una integració més ràpida un cop superada la barrera comunicativa inicial.
*   **ESO:** A l'educació secundària, les barreres lingüístiques es fan més complexes, ja que el llenguatge acadèmic és més abstracte i especialitzat. L'alumnat pot tenir dificultats per comprendre textos, participar en debats, i expressar idees complexes, afectant totes les àrees curriculars. La integració social és crucial, i poden sorgir problemes d'autoestima o desajustos de la personalitat (DOC 8) si no se senten acceptats o capaços. Es desenvolupen plans d'acollida específics, com els de matemàtiques, per facilitar la integració curricular i metodològica. La diferència cultural pot manifestar-se en la interpretació de normes socials o expectatives acadèmiques, i cal un seguiment acurat de les trajectòries educatives per prevenir l'abandonament escolar.
*   **Batxillerat/FP:** En aquestes etapes, l'alumnat nouvingut s'enfronta a una exigència acadèmica elevada i a la necessitat de prendre decisions sobre el seu futur. Les barreres lingüístiques i culturals poden limitar l'accés a continguts avançats i la participació en activitats que requereixen un alt nivell de competència comunicativa. La pressió per obtenir bons resultats i la incertesa sobre el reconeixement dels estudis previs poden generar ansietat. Les propostes d'actuació se centren en potenciar la continuïtat dels estudis, oferint orientació acadèmica i professional, i assegurant que les barreres lingüístiques i socioeconòmiques no limitin les oportunitats futures. L'autonomia, la motivació i la construcció d'un projecte de vida prenen un paper central.

## Barreres d'aprenentatge

*   **Lingüístic:** El "desconeixement de les dues llengües" o el "desconeixement de la llengua catalana" (DOC 8) és la barrera més immediata i significativa. Afecta la comprensió de les explicacions, la participació a l'aula, l'accés als continguts curriculars i la capacitat d'expressar-se oralment i per escrit.
*   **Cognitiu:** Pot haver-hi un "retard en les àrees instrumentals de dos cursos" o en el "desenvolupament del llenguatge a nivell d'estructuració i organització" (DOC 8), no per una dificultat intrínseca, sinó per la discontinuïtat o diferència del sistema educatiu d'origen, o per la dificultat d'accedir al coneixement a través d'una llengua no dominada. La manca d'hàbits d'estudi i de treball del sistema educatiu català, així com baixes expectatives d'èxit acadèmic, poden obstaculitzar el progrés.
*   **Emocional:** L'adaptació a un nou entorn pot generar "problemes d'autoestima i autoconcepte" (DOC 8), ansietat, por a equivocar-se, o sentiment de pèrdua per la cultura d'origen. El dol migratori —la pèrdua de referents, entorn familiar i cultural— la dificultat en la construcció d'una identitat múltiple, la inseguretat i la por al fracàs són factors de risc que afecten el desenvolupament personal. La "identitat de múltiples pertinències" (DOC 1) pot ser complexa de gestionar emocionalment.
*   **Social:** Dificultats per establir relacions amb els iguals, per comprendre les dinàmiques socials de l'aula o el centre, o per sentir-se part del grup. Pot haver-hi "desajustaments de la personalitat" o "necessitats afectives greus i permanents" (DOC 8) derivades del procés migratori o d'experiències prèvies.
*   **Sensorial:** Tot i que no és una barrera específica del nouvingut, qualsevol dificultat sensorial preexistent (com la deficiència visual o motriu esmentada en DOC 10) pot veure's agreujada per la barrera lingüística i la manca d'adaptació inicial.
*   **Curricular:** La diferència en els currículums d'origen i de destinació, els mètodes d'ensenyament i avaluació, o la manca de coneixements previs en àrees específiques poden generar un desfasament important.

## Necessitats prioritàries

1.  **Adquisició accelerada de la llengua vehicular:** És fonamental per a l'accés al currículum i la integració social. Les aules d'acollida són un "espai obert, flexible i dinàmic per atendre l'alumnat nouvingut" i "el lloc per excel·lència per desenvolupar el coneixement de la llengua de l'escola" (DOC 5).
2.  **Acollida emocional i social:** Crear un ambient segur i de confiança que faciliti la integració, el sentiment de pertinença i la gestió de les emocions associades al canvi.
3.  **Suport curricular adaptat:** Proporcionar estratègies i materials que permetin accedir als continguts, tenint en compte els coneixements previs i el ritme d'aprenentatge, diversificant procediments i activitats (DOC 8).
4.  **Reconeixement i valoració de la cultura d'origen:** Integrar les seves experiències i coneixements previs per construir ponts entre la seva identitat i la nova realitat educativa.
5.  **Orientació i acompanyament familiar:** Implicar les famílies en el procés educatiu i facilitar-los la comprensió del sistema.
6.  **Facilitar la incorporació al nou entorn escolar i a la societat d'acollida:** Orientació sobre el funcionament del centre, les normes, els espais i les oportunitats de participació perquè l'alumne pugui sentir-se part de la comunitat.
7.  **Facilitar l'accés al llenguatge acadèmic:** Estratègies per desenvolupar les habilitats lingüístiques necessàries per comprendre i expressar conceptes en les diferents àrees curriculars, distingint entre la llengua comunicativa i la llengua acadèmica.
8.  **Adquisició d'hàbits escolars i de treball:** Orientació en les rutines, normes i expectatives del sistema educatiu per fomentar l'autonomia i la seguretat en l'entorn escolar.

## Fortaleses a aprofitar

L'alumnat nouvingut aporta una "riquesa i un bé comú" (DOC 10) inestimable a l'aula. Les seves fortaleses inclouen:
*   **Plurilingüisme i pluriculturalitat:** Són portadors de diverses llengües i cultures, la qual cosa enriqueix el context educatiu i fomenta la "identitat de múltiples pertinences" (DOC 1). Aquesta diversitat és un recurs per a l'aprenentatge intercultural de tot l'alumnat.
*   **Resiliència i capacitat d'adaptació:** El procés migratori sovint implica una gran capacitat de superació i adaptació a nous contextos, que pot ser un motor per a l'aprenentatge.
*   **Noves perspectives:** Aporten punts de vista diferents sobre el món, la història, la geografia o les relacions socials, enriquint els debats i el pensament crític a l'aula.
*   **Coneixements previs diversos:** Poden tenir coneixements o habilitats en àrees no explorades pel currículum local, o una profunditat diferent en temes comuns.
*   **Motivació per aprendre:** Molts d'ells tenen una gran motivació per integrar-se i aprofitar les oportunitats educatives. Sovint, tant l'alumnat com les seves famílies tenen una alta motivació i expectatives respecte a l'educació com a via de progrés.

## Senyals identificadors a l'aula

*   **Dificultats comunicatives:** Manca de fluïdesa en català o castellà, ús de llenguatge no verbal per compensar, dificultat per seguir instruccions orals complexes, o per expressar idees de forma coherent.
*   **Aïllament social:** Poca interacció amb els companys, tendència a estar sols durant els patis o activitats grupals, o dificultat per formar part de grups de treball.
*   **Baix rendiment acadèmic inicial:** Especialment en àrees que requereixen un alt nivell de comprensió lectora o expressió escrita, que pot no reflectir la seva capacitat intel·lectual real.
*   **Comportaments d'observació:** Tendència a observar molt abans de participar, o a imitar les accions dels companys per entendre què s'espera d'ells.
*   **Preguntes sobre normes o rutines:** Dubtes sobre aspectes bàsics del funcionament de l'aula o del centre que la resta de l'alumnat ja coneix.
*   **Fatiga o desmotivació:** Després d'un esforç continuat per comprendre i adaptar-se, poden mostrar signes de cansament o desinterès.
*   **Informació de dades inicials:** L'expedient o el full de recollida de dades indica un país de procedència diferent, una data d'arribada recent a Catalunya i/o una escolarització prèvia irregular o nul·la.
*   **Fatiga o esgotament inusual** després de les sessions, resultat de l'esforç cognitiu i emocional constant d'adaptació i comprensió en una llengua no plenament dominada.
*   **Ús de la llengua materna en moments de tensió o estrès**, com a refugi comunicatiu quan la pressió supera la capacitat d'expressió en la llengua vehicular.

## Perfils associats i comorbiditats

L'alumnat nouvingut pot presentar, com qualsevol altre alumne, altres necessitats educatives o condicions. La "diversitat cultural és una de les múltiples diversitats" (DOC 2) i els "factors de vulnerabilitat i exclusió social" (DOC 2) poden afectar-los de manera més accentuada.
*   **Necessitats educatives especials (NEE):** Un alumne nouvingut pot tenir, per exemple, un "retard maduratiu", "trastorn de conducta", "discapacitat motriu" o "trastorn generalitzat del desenvolupament" (DOC 10), que es pot veure emmascarat o agreujat per la barrera lingüística inicial.
*   **Altes capacitats:** Un alumne nouvingut també pot ser d'"altes capacitats" (DOC 6, DOC 8), i les seves necessitats d'ampliació curricular poden passar desapercebudes si el focus es posa només en la llengua.
*   **Situacions de vulnerabilitat social:** Poden provenir de famílies en situació de pobresa, amb dificultats d'habitatge, o amb experiències traumàtiques derivades del procés migratori, que afecten el seu benestar emocional i el seu rendiment escolar.
*   **Problemes de salut crònics:** Condicions com l'asma (DOC 7) o altres malalties cròniques poden coexistir i requerir adaptacions, com en qualsevol altre alumne (DOC 8).
*   **Dificultats emocionals o de salut mental:** El procés migratori pot desencadenar o agreujar problemes d'ansietat, depressió o estrès posttraumàtic, riscos vinculats directament a les pèrdues i al canvi radical d'entorn que comporta la migració.

## Perfil adjacent: alumnat de 2a generació

L'alumnat de segona generació —nascut a Catalunya o arribat en edat molt primerenca, amb famílies d'origen migrat— no activa els protocols de "nouvingut" però pot presentar necessitats similars que passen desapercebudes:

- **Dicotomia lingüística**: la L1 domèstica (la llengua que es parla a casa) pot ser diferent de la llengua d'instrucció. L'alumne pot dominar el català oral quotidià però tenir mancances en el registre acadèmic de qualsevol de les seves llengües.
- **Conflicte d'identitat**: tensió entre la cultura familiar i la cultura d'acollida, que pot manifestar-se com a rebuig d'una de les dues identitats, doble pertinença conflictiva o sentiment de no encaixar en cap dels dos mons.
- **Risc de bretxa acadèmica**: el fenomen del *doble semillingüisme* (Cummins): quan l'alumne no assoleix competència acadèmica plena en cap de les seves llengües, el rendiment escolar global es ressent. Més freqüent en famílies amb baixa escolarització.
- **Menor visibilitat**: en no ser identificats com a "nouvinguts", aquests alumnes no accedeixen als recursos específics (aula d'acollida, suport LIC, informes trimestrals). Les seves dificultats s'atribueixen erròniament a manca de motivació o capacitat.
- **Implicació pràctica**: la variable `L1` pot indicar una llengua familiar diferent fins i tot per a alumnat nascut localment. Quan `L1 ≠ català` i `calp = inicial`, cal considerar aquest perfil encara que `escolaritzacio_previa = si`.

## Principis d'actuació

L'atenció a l'alumnat nouvingut ha de basar-se en un enfocament inclusiu que reconegui la diversitat com una riquesa (DOC 10). En primer lloc, és crucial una "bona acollida en un centre que sigui acollidor" (DOC 5), que va més enllà de la figura d'un tutor d'aula d'acollida i implica tot el claustre. Cal "identificar i suprimir barreres" (DOC 10) per a l'aprenentatge i la participació.

Per adaptar els continguts, és important "adaptar els continguts i activitats als coneixements previs de l'alumnat" (DOC 8), utilitzant materials visuals, llenguatge senzill i clar, i oferint suports lingüístics específics, com les aules d'acollida (DOC 5). Es poden introduir conceptes de forma gradual, connectant-los amb les seves experiències i cultures d'origen. L'etnomatemàtica, per exemple, pot ser un recurs intercultural per connectar amb els coneixements matemàtics previs de l'alumnat i validar els seus referents culturals.

Pel que fa a les activitats, cal "diversificar els procediments i activitats tant d'aprenentatge com d'avaluació" (DOC 8). Les activitats cooperatives són molt beneficioses per potenciar les relacions amb els iguals (DOC 6) i facilitar la interacció lingüística. S'ha de fomentar que "l'alumnat pugui presentar el treball de diverses maneres" (DOC 8). L'assignació d'un company tutor és una pràctica pedagògica concreta i eficaç per facilitar la integració quotidiana, aclarir dubtes i crear vincles entre l'alumnat nouvingut i la resta del grup.

L'avaluació ha de ser formativa i flexible, tenint en compte el procés d'adquisició lingüística. Els criteris d'avaluació poden ser els mateixos que la resta d'alumnat, però "més alguna qüestió relacionada amb el treball de cerca i d'ampliació que desenvolupi" (DOC 6), o adaptant les eines per avaluar la comprensió més enllà de l'expressió lingüística. "Es potencia l'autoavaluació i coavaluació, com a mesura d'autoregulació de l'aprenentatge" (DOC 8).

Finalment, la interacció a l'aula ha de ser respectuosa i inclusiva. El professorat ha de "reconèixer l'esforç que exigeix completar una tasca o el cansament que pugui provocar" (DOC 8) i "explicar l'objectiu que té cada classe" (DOC 8). Cal evitar la còpia i les activitats mecàniques (DOC 8), i promoure la discussió en parelles i petits grups (DOC 8). La coordinació amb els mestres de suport (LIC - Aula d'acollida, EAP) és clau per garantir una atenció integral (DOC 10).

La **coordinació amb la família i la comunitat** és un eix transversal d'actuació: cal establir canals de comunicació efectius amb les famílies, oferir informació clara sobre el funcionament del sistema educatiu i implicar-les en el procés educatiu dels seus fills, si cal amb mediació intercultural. Treballar en xarxa amb els serveis socials i altres entitats del territori reforça la xarxa de suport de l'alumne més enllà de l'escola.

## Línies vermelles

*   **No etiquetar l'alumne només pel seu origen:** Evitar reduir la persona a la seva condició de "nouvingut" o a la seva cultura d'origen. El perfil és "la suma de múltiples pertinences" (DOC 1), i no es pot identificar "grups culturals o socials homogenis" (DOC 2). Etiquetar pot portar a prejudicis i a no veure la seva individualitat i les seves capacitats.
*   **No aïllar l'alumne de l'aula ordinària de forma permanent:** L'aula d'acollida és un recurs temporal per a l'adquisició de la llengua, però "el lloc per excel·lència per desenvolupar el coneixement de la llengua de l'escola és l'aula ordinària" (DOC 5). Aïllar-lo impedeix la integració social i l'exposició al llenguatge natural de l'aula, dificultant la seva inclusió plena (DOC 10).
*   **No assumir un dèficit intel·lectual per la barrera lingüística:** La dificultat en la llengua no implica una menor capacitat cognitiva. Assumir-ho pot portar a reduir les expectatives acadèmiques i a no oferir reptes adequats, limitant el seu potencial.
*   **No ignorar la seva cultura i coneixements previs:** Desvaloritzar o ignorar la seva herència cultural i els aprenentatges anteriors és un error. És fonamental reconèixer i valorar les seves fortaleses i el que aporten.
*   **No delegar tota la responsabilitat d'acollida en un únic professional:** "Disposar d'un tutor per a l'aula d'acollida no suposa que la resta del claustre ja es pugui desentendre d'aquesta funció" (DOC 5). L'acollida és una tasca de tot el centre i de tots els professionals (DOC 5).
*   **No tenir baixes expectatives acadèmiques:** Assumir que l'alumnat nouvingut té menys potencial o que no pot assolir els mateixos objectius que els seus companys és un biaix que limita les seves oportunitats i el seu desenvolupament.
*   **No ignorar el component emocional i social:** Centrar-se exclusivament en l'aprenentatge de la llengua i el currículum, deixant de banda el benestar emocional i la integració social, és un error que pot portar al fracàs escolar i a l'abandonament.
*   **No deixar l'acollida a la improvisació:** El procés d'acollida és crucial i requereix una planificació detallada i la implicació de tota la comunitat educativa. Improvisar pot generar sentiments d'inseguretat i dificultar la integració.
*   **No centrar-se exclusivament en el dèficit lingüístic:** Tot i que l'adquisició de la llengua és fonamental, cal reconèixer i valorar les altres capacitats i coneixements previs de l'alumne, així com la seva llengua materna, com a recurs i no com a obstacle.

## 3. Connexions amb altres documents del corpus

- **`M1_acollida-marc-conceptual.md`** — El protocol d'acollida és l'instrument que gestiona la transició inicial; l'alumnat nouvingut és el seu destinatari principal; els dos documents s'han de llegir junts
- **`M1_diversitat-cultural-identitat.md`** — La diversitat cultural i la identitat de l'alumnat nouvingut no és obstacle sinó riquesa; el marc de diversitat cultural dona les eines per treballar l'alteritat i la pertinença
- **`M1_plans-individuals-PAD-PI.md`** — Quan l'alumne nouvingut té necessitats lingüístiques o acadèmiques específiques, el PI és l'instrument de resposta individualitzada
- **`M2_DUA-disseny-universal-aprenentatge.md`** — El DUA permet dissenyar accés al contingut per a alumnes en procés d'adquisició de la llengua vehicular: múltiples representacions i suports visuals i multimodals
- **`M7_participacio-families.md`** — La participació de les famílies nouvingudes és especialment complexa; requereix estratègies de mediació intercultural i recursos de traducció
- **`M0_cura-personalis.md`** — L'atenció integral és el fonament: l'alumnat nouvingut no és un expedient d'acollida sinó una persona amb una trajectòria de vida, un dol migratori i un projecte de futur

## 4. Detecció

**Senyals del docent**
*   "Observo que un alumne no participa en les converses de grup."
*   "Un alumne nou no entén les meves instruccions orals o escrites."
*   "Noto que un alumne nouvingut sembla aïllat durant el pati o les activitats lúdiques."
*   "Un alumne nou lliura treballs amb errors lingüístics significatius o amb contingut que no s'ajusta a la tasca."
*   "La família d'un alumne nouvingut expressa dificultats per entendre el funcionament del centre o comunicar-se amb mi."
*   "Un alumne nou mostra signes de frustració o desmotivació davant tasques que requereixen un alt nivell de llengua."

**Senyals de l'alumne**
*   L'alumne utilitza gestos o senyals no verbals per comunicar-se o per indicar que no entén.
*   L'alumne evita el contacte visual o la interacció amb els companys i el professorat.
*   L'alumne es mostra callat o amb por a equivocar-se en parlar en català o castellà.
*   L'alumne té dificultats per seguir el ritme de la classe o per completar les tasques en el temps establert.

**Senyals de context**
*   **Moment:** Recent incorporació al centre o a l'aula.
*   **Activitat:** Tasques que requereixen alta competència lingüística (lectura, escriptura, debat), o activitats socials no estructurades. Activitat que requereix alt nivell de llengua sense suports visuals, contextuals o lingüístics addicionals.
*   **Composició grup:** Presència d'altres alumnes nouvinguts que parlen la mateixa llengua o, per contra, absència total de referents lingüístics o culturals.

**Protocol de derivació recomanat (basat en D150/2017 i D175/2022)**

| Moment | Acció | Responsable |
|---|---|---|
| Matriculació | Recollida dades inicials (escolarització prèvia, L1, situació familiar) | Secretaria + Tutor/a |
| 1a setmana | Entrevista família + acollida al centre | Tutor/a + LIC |
| 1r mes | Avaluació inicial nivell MECR (comprensió oral, lectura, escriptura) | Aula d'acollida / LIC |
| Trimestral | Informe qualitatiu individual (obligatori D175/2022 art. 24.8) | Equip docent |
| Si persisteixen dificultats | Derivació EAP per valoració NEE | Tutor/a + EAP |

**Anti-senyals específics (alerta de confusió diagnòstica)**

- **Dificultats en L1 també** → possible TDL (Trastorn del Desenvolupament del Llenguatge) o dislèxia, no atribuïble únicament a la barrera L2. Derivar a logopèdia amb avaluació en L1 si és possible.
- **Dificultats persistents >2 anys amb suport adequat** → revaluar NEE. La barrera lingüística habitualment es redueix significativament en aquest termini; si no ho fa, cal descartar causes subjacents.
- **Retraïment sever, aïllament, resistència a anar a escola** → possible dol migratori complicat (Síndrome d'Ulisses). No confondre amb "timidesa" o "adaptació lenta". Derivar a salut mental si hi ha senyals d'alarma (somatitzacions, insomni, irritabilitat extrema).

**Anti-senyals** (quan NO activar malgrat les aparences)
*   Un alumne nou que es mostra callat però participa activament en tasques visuals o pràctiques i respon bé a suports no verbals: pot ser un estil d'aprenentatge o un període d'observació, no necessàriament una barrera insalvable.
*   Un alumne que parla una altra llengua a casa però mostra fluïdesa i comprensió en català a l'escola: la seva condició de nouvingut és només d'origen, no implica necessàriament barreres actives.
*   Un alumne que comet errors gramaticals però es comunica amb seguretat i comprèn el contingut: pot estar en una fase d'adquisició normal de la llengua, sense necessitat de suports intensius més enllà de la pràctica.
*   Les dificultats observades són generals i no específiques del procés migratori o d'integració, podent correspondre a altres necessitats educatives.

### Heurístiques

**Principi general:** Cal promoure una acollida integral i personalitzada, reconeixent la diversitat de l'alumnat nouvingut com una riquesa i facilitant la seva plena participació i aprenentatge.

**Heurístiques per al docent**

*   **Heurística: El pont lingüístic és la primera pedra.**
    *   **Quan aplica:** Quan un docent expressa preocupació per la manca de comprensió o expressió lingüística d'un alumne nouvingut.
    *   **Fonament:** El desconeixement de la llengua vehicular és la barrera més immediata i limitant per a l'accés al currículum i la integració. Les aules d'acollida són un recurs clau, però la llengua s'aprèn millor en contextos significatius i d'ús real.
    *   **Exemple complet de raonament:** Davant un docent preocupat perquè un alumne nouvingut no entén res a classe, la prioritat és establir un pont lingüístic. Això implica no només derivar a l'aula d'acollida si n'hi ha, sinó també oferir estratègies immediates a l'aula ordinària: suports visuals, gestos, llenguatge senzill i frases curtes. També es pot recórrer a la traducció automàtica per a conceptes clau o a la creació de glossaris il·lustrats. El raonament és que sense una base mínima de llengua, l'alumne no podrà accedir als continguts ni interactuar, i cada dia que passa sense aquest suport inicial, la bretxa s'amplia. A més, la interacció amb els companys en un context significatiu és vital per a l'adquisició natural de la llengua.

*   **Heurística: La inclusió comença a l'aula ordinària.**
    *   **Quan aplica:** Quan un docent es planteja com integrar socialment un alumne nouvingut o si ha de separar-lo per rebre suport.
    *   **Fonament:** L'aïllament de l'alumne, fins i tot amb la millor intenció de suport lingüístic, pot dificultar la seva integració social i el sentiment de pertinença. L'acollida és una responsabilitat de tot el claustre i l'aula ordinària és el context natural per a la socialització i l'aprenentatge entre iguals.
    *   **Exemple complet de raonament:** Davant un alumne nouvingut que passa la major part del temps a l'aula d'acollida i que, quan torna a l'aula ordinària, li costa interactuar amb els companys: si bé l'aula d'acollida és vital per a l'adquisició lingüística, la inclusió social i curricular s'ha de fomentar activament a l'aula ordinària. Estratègies útils: aprenentatge cooperatiu amb rols clars que no depenguin exclusivament de la llengua; parelles lingüístiques amb companys que puguin fer de referents; activitats on l'alumne nouvingut pugui compartir aspectes de la seva cultura o coneixements previs, valorant la seva aportació única. L'objectiu és que l'alumne se senti part del grup i que els companys també aprenguin a interactuar amb la diversitat, evitant la creació de guetos.

*   **Heurística: Valora la maleta cultural.**
    *   **Quan aplica:** Quan un docent busca maneres de connectar amb un alumne nouvingut o de fer el currículum més rellevant per a ell.
    *   **Fonament:** L'alumnat nouvingut no arriba amb un "full en blanc", sinó amb una "maleta" plena de coneixements, experiències i una cultura pròpia. Ignorar-ho és perdre una oportunitat d'enriquiment per a tota l'aula i de motivació per a l'alumne.
    *   **Exemple complet de raonament:** Davant un alumne nouvingut desinteressat en els continguts, és essencial connectar amb la seva "maleta cultural". Cal buscar maneres d'incorporar les experiències i coneixements previs de l'alumne en les activitats d'aula. Per exemple, si s'estudia geografia, es pot demanar a l'alumne que expliqui aspectes del seu país d'origen. Si es treballa història, es pot investigar sobre esdeveniments rellevants en la seva cultura. Això no només valida la identitat de l'alumne i la seva "identitat de múltiples pertinències", sinó que també enriqueix la perspectiva de la resta de la classe i fa que l'aprenentatge sigui més significatiu i rellevant per a ell.

*   **Heurística: Les expectatives altes són inclusives.**
    *   **Quan aplica:** Quan un docent dubta sobre el potencial acadèmic d'un alumne nouvingut a causa de les barreres inicials.
    *   **Fonament:** Assumir un dèficit intel·lectual per la barrera lingüística és un error. Mantenir expectatives altes, juntament amb els suports necessaris, és crucial per al desenvolupament del potencial de tot l'alumnat.
    *   **Exemple complet de raonament:** Davant un alumne nouvingut que, tot i esforçar-se, no aconsegueix els resultats esperats — i la temptació és atribuir-ho a manca de capacitat — és fonamental mantenir expectatives altes, ja que la barrera lingüística o la diferència curricular no equival a una manca de capacitat intel·lectual. Cal revisar les eines d'avaluació per assegurar-se que estan mesurant la comprensió del contingut i no només la fluïdesa lingüística. Es pot recórrer a avaluacions orals, projectes visuals o a l'ús de la llengua materna com a suport puntual. Cal oferir reptes intel·lectuals adequats, amb els suports lingüístics necessaris, per evitar la desmotivació per falta d'estímul i per demostrar a l'alumne que es confia en el seu potencial.

*   **Heurística: La flexibilitat metodològica és la clau.**
    *   **Quan aplica:** Quan un docent busca estratègies per adaptar la seva pràctica a la diversitat de l'alumnat nouvingut.
    *   **Fonament:** L'aula és un espai de "gran diversitat cultural i social" (DOC 8), i una metodologia rígida no pot atendre les necessitats de tots. La diversificació d'activitats i avaluacions és essencial.
    *   **Exemple complet de raonament:** Davant un grup amb diversos alumnes nouvinguts amb diferents nivells de llengua, la flexibilitat metodològica és indispensable. Cal "diversificar els procediments i activitats tant d'aprenentatge com d'avaluació" (DOC 8). Això pot incloure la combinació d'explicacions orals amb recursos visuals i interactius, activitats de recerca individual, treballs en petits grups amb rols diferenciats, i la possibilitat de presentar els treballs en formats diversos (oral, escrit, visual, digital). Cal "adaptar els continguts i activitats als coneixements previs de l'alumnat" (DOC 8) i donar temps per "assimilar-ho" (DOC 8), evitant "la còpia i les activitats mecàniques" (DOC 8). L'objectiu és que cada alumne pugui trobar la seva via d'accés al coneixement i demostrar el seu aprenentatge de la manera més efectiva.

*   **Heurística: "L'àncora emocional"**
    *   **Quan aplica:** Quan observes que un alumne nouvingut mostra signes d'aïllament, tristesa, irritabilitat o manca de motivació, indicant un possible dol migratori o dificultats d'adaptació emocional.
    *   **Fonament:** El benestar emocional és un prerequisit per a l'aprenentatge. El procés migratori pot generar pèrdues significatives (família, amics, cultura, estatus) que es manifesten com a dol migratori. Crear un vincle de confiança i un sentiment de pertinença és crucial per a l'estabilitat de l'alumne i per poder afrontar els reptes acadèmics i socials. La mediació cultural pot ser un recurs clau per acompanyar aquest procés.
    *   **Exemple complet de raonament:** En Joan, que va arribar del Marroc fa un mes, sovint està amb la mirada perduda i no s'implica en les activitats de grup. Quan els companys intenten parlar amb ell, es tanca. Això no és només una barrera lingüística, sinó que podria ser un senyal de dol migratori o de dificultat per establir nous vincles. En lloc de forçar la interacció, cal apropar-s'hi de forma individual, oferint-li un espai segur per expressar-se si ho desitja, potser amb l'ajuda d'un mediador cultural si n'hi ha. També convé buscar maneres d'incorporar elements de la seva cultura d'origen a l'aula, com ara mapes, música o històries, per validar la seva identitat i ajudar-lo a sentir-se més connectat amb el seu passat mentre construeix el seu present.

*   **Heurística: "La xarxa de suport"**
    *   **Quan aplica:** Quan l'alumne nouvingut presenta múltiples barreres (lingüístiques, emocionals, socials, curriculars) i necessita un acompanyament més enllà de l'aula.
    *   **Fonament:** La integració de l'alumnat nouvingut és una responsabilitat compartida de tota la comunitat educativa i social. Implicar la família, el personal de l'aula d'acollida, els serveis socials i altres agents educatius crea una xarxa de suport que maximitza les oportunitats d'èxit i benestar de l'alumne. Cap professional pot gestionar sol la complexitat de múltiples barreres simultànies.
    *   **Exemple complet de raonament:** En David està tenint moltes dificultats per adaptar-se. A més de la barrera lingüística, la seva família no ha pogut venir a les reunions i sembla que hi ha problemes a casa. Això suggereix la necessitat d'una xarxa de suport més àmplia. En lloc de gestionar-ho en solitari, cal coordinar-se amb el tutor de l'aula d'acollida per compartir informació sobre la seva evolució. També convé contactar amb el servei de mediació intercultural del centre o de l'ajuntament per facilitar la comunicació amb la família i entendre millor la seva situació. Cal proposar al departament d'orientació que valori si hi ha necessitats addicionals i buscar recursos externs si cal, assegurant que tots els actors rellevants treballin de manera coordinada per al seu benestar i progrés.

*   **Heurística: "Implicar activament la família"**
    *   **Quan aplica:** Des del moment de la matriculació i durant tot el procés d'adaptació, especialment si hi ha dificultats de comunicació o si el docent vol entendre millor el context de l'alumne.
    *   **Fonament:** Els documents subratllen la importància de "l'acollida de l'alumnat i les seves famílies" i que el pla d'acollida ha d'incloure actuacions referides a la matriculació i l'acollida inicial de les famílies. La família és un agent clau en el procés d'integració: quan se sent part de la comunitat educativa, l'alumne ho percep i se sent més segur.
    *   **Exemple complet de raonament:** Davant un docent que expressa "m'agradaria parlar amb la família del nou alumne, però no sé com comunicar-me amb ells perquè no parlen català ni castellà", cal recordar que la implicació familiar és crucial per a l'èxit de l'alumne. La via és contactar amb el servei de mediació intercultural del centre o de l'ajuntament, si n'hi ha, per facilitar la comunicació. Es poden utilitzar eines de traducció per a comunicacions escrites bàsiques (circulars, horaris) i organitzar una primera trobada amb un intèrpret per explicar el funcionament del centre, les expectatives i recollir informació rellevant sobre l'alumne (escolarització prèvia, interessos, situació familiar). L'objectiu és establir un canal de comunicació obert i de confiança que permeti a la família sentir-se part de la comunitat educativa i col·laborar en el procés d'aprenentatge del seu fill.

*   **Heurística: "Construir l'escola des de zero"**
    *   **Quan aplica:** Quan `escolaritzacio_previa = no` o `parcial`. L'alumne no ha estat escolaritzat de manera regular al país d'origen i desconeix les convencions bàsiques de l'entorn escolar.
    *   **Fonament:** La barrera no és només lingüística sinó cultural-cognitiva. L'alumne pot no saber què és un quadern, com funciona un horari, què significa "fer deures" o com s'organitza un espai d'aula. Aprendre a "ser alumne" precedeix l'aprenentatge de continguts. Forçar una acceleració sense aquesta bastida genera frustració, fracàs i retraïment. El Decret 150/2017 emfatitza que les mesures han de ser proporcionades a les necessitats reals, no a les expectatives curriculars del nivell d'edat.
    *   **Exemple complet de raonament:** Arriba l'Amadou, de 12 anys, procedent d'una zona rural de Guinea. No ha estat mai escolaritzat. El primer impuls pot ser incorporar-lo a 1r d'ESO amb suports lingüístics, però la prioritat és una altra: (1) **Orientació espaciotemporal**: que l'alumne entengui l'estructura del dia escolar, els espais del centre, les rutines bàsiques (seure, escoltar, demanar permís). (2) **Convencions escolars bàsiques**: ús del material (llapis, quadern, pissarra), dinàmiques d'aula (torns de paraula, treball individual vs. grupal), hàbits (puntualitat, ordre). (3) **Pre-lectoescriptura i pre-numeració**: si l'alumne no està alfabetitzat en cap llengua, cal un pla específic de lectoescriptura funcional, idealment coordinat amb l'aula d'acollida. (4) **Llengua en paral·lel**, no com a únic eix: el català s'aprèn mentre es construeixen les bases anteriors, no com a requisit previ. Cal coordinació amb l'EAP per dissenyar un pla d'incorporació progressiva, amb objectius realistes a curt termini i sense comparar el ritme amb el de l'alumnat escolaritzat. L'objectiu no és accelerar, sinó construir la bastida correcta perquè l'aprenentatge posterior sigui sòlid.

**Heurístiques per a l'alumne**

*   **Heurística: Demana ajuda per entendre.**
    *   **Quan aplica:** Quan un alumne nouvingut no entén el que s'explica a classe o una tasca.
    *   **Fonament:** La por a equivocar-se o a no saber expressar-se pot portar a l'aïllament. Demanar ajuda és un signe de fortalesa i una eina clau per superar la barrera lingüística i avançar en l'aprenentatge.
    *   **Exemple complet de raonament:** Davant un alumne nouvingut que pregunta què ha de fer quan no entén les explicacions del professor, "demanar ajuda per entendre" és la millor estratègia. Cal explicar-li que és normal no entendre-ho tot al principi i que el professor i els companys estan allà per ajudar. Convé animar-lo a no tenir por de preguntar, ja sigui aixecant la mà, utilitzant gestos per indicar que no ha entès, o demanant a un company que li expliqui amb paraules més senzilles. També es pot suggerir l'ús d'eines de traducció si les té a mà per buscar paraules clau. L'objectiu és que l'alumne entengui que la comunicació és bidireccional i que la seva participació activa en el procés de comprensió és fonamental per al seu èxit.

*   **Heurística: Connecta amb els teus companys.**
    *   **Quan aplica:** Quan un alumne nouvingut se sent sol o té dificultats per fer amics.
    *   **Fonament:** La interacció social és vital per a la integració i per a l'adquisició natural de la llengua. Els companys són un recurs valuós per a l'aprenentatge i el suport emocional.
    *   **Exemple complet de raonament:** Davant un alumne nouvingut que confessa sentir-se sol a l'escola i tenir dificultats per fer amics, "connectar amb els companys" és crucial per a la seva integració. Convé suggerir-li que busqui oportunitats per interactuar: participar en activitats de grup a classe, oferir-se a ajudar un company, o simplement somriure i saludar. Cal explicar-li que molts companys estaran contents de conèixer-lo i que, fins i tot amb poques paraules, es poden establir connexions. També es pot animar-lo a participar en activitats extraescolars no competitives (DOC 6) si n'hi ha, per trobar interessos comuns. L'objectiu és que l'alumne entengui que la socialització és un procés actiu i que, a mesura que interactuï, la seva confiança i la seva capacitat de comunicació milloraran.

*   **Heurística: La teva història és un tresor.**
    *   **Quan aplica:** Quan un alumne nouvingut dubta sobre compartir aspectes de la seva cultura o experiències, o se sent diferent.
    *   **Fonament:** La "identitat de múltiples pertinences" (DOC 1) i la diversitat cultural són una riquesa. Compartir la pròpia història i cultura pot empoderar l'alumne i enriquir l'experiència de tots.
    *   **Exemple complet de raonament:** Davant un alumne nouvingut que pregunta si hauria d'amagar que ve d'un altre país o que parla una altra llengua perquè se sent diferent, "la seva història és un tresor" i no l'ha d'amagar. Cal explicar-li que la seva cultura i les seves experiències són úniques i valuoses, i que poden aportar molt a la classe i als seus companys. Convé animar-lo a compartir aspectes de la seva vida, costums o coneixements quan se senti còmode, ja sigui en un projecte de classe, una presentació o una conversa informal. Cal recordar-li que la "diversitat és una realitat ineludible i la seva existència una riquesa i un bé comú" (DOC 10). L'objectiu és que l'alumne se senti orgullós de qui és i d'on ve, i que entengui que la seva identitat diversa és una fortalesa, no una feblesa.

*   **Heurística: "El meu espai segur"**
    *   **Quan aplica:** Quan un alumne nouvingut se sent sol, trist o amb por de no encaixar en el nou entorn escolar.
    *   **Fonament:** L'escola ha de ser un lloc segur on l'alumne se senti acceptat i protegit. Identificar adults de confiança i espais on sentir-se còmode és vital per al seu benestar emocional i la seva integració, permetent-li expressar les seves emocions i trobar suport.
    *   **Exemple complet de raonament:** Si em sento trist o sol, o si trobo a faltar la meva família o el meu país, recordaré que hi ha adults a l'escola que em poden ajudar. Puc parlar amb el meu tutor, amb el professor de l'aula d'acollida o amb algun altre adult amb qui em senti còmode. També puc buscar un espai tranquil a l'hora del pati si necessito un moment per mi. Recordaré que és normal sentir-se així al principi i que no estic sol. Intentaré apropar-me a algun company que em somrigui o que em sembli amable, encara que al principi em costi parlar. L'important és no guardar-me els sentiments i buscar suport, perquè parlar-ne ajuda a sentir-se millor.

---

## 5. Fonts

- Cummins, J. (2001). *Negotiating identities: Education for empowerment in a diverse society* (2a ed.). Los Angeles: California Association for Bilingual Education.
- Decret 150/2017, de 17 d'octubre, de l'atenció educativa a l'alumnat en el marc d'un sistema educatiu inclusiu. DOGC núm. 7477.
- Departament d'Educació (2020). *Acollida i integració de l'alumnat nouvingut*. Generalitat de Catalunya.
- Krashen, S. D. (1982). *Principles and practice in second language acquisition*. Oxford: Pergamon.
- OCDE (2015). *Helping immigrant students to succeed at school and beyond*. París: OECD Publishing.


## Connexions MALL

**HCL i progressió L2** (BICS/CALP): L'alumne nouvingut JA DOMINA les HCL en la seva L1. La bastida és per a la L2, no per a la cognició.
- A1-A2 → Narrar, Descriure (BICS en formació: 2-3 anys)
- B1 → Explicar
- B2-C1 → Justificar, Argumentar (CALP: 5-7 anys per consolidar)
**Bastida clau MALL**: TOLC — Language Identity Texts (LIT), dictats bilingües, collages lingüístics. Recasting i rephrasing com a feedback no interruptiu.
**Eix oral/escrit**: L'oralitat en L1 és el pont per a l'escriptura en L2.

## 6. INSTRUCCIONS D'ADAPTACIÓ TEXTUAL

### Barrera nuclear
**Lèxica i cultural**: L'alumnat nouvingut té com a barrera principal la comprensió lèxica (vocabulari en L2) i els referents culturals locals que desconeix. La distància lingüística entre L1 i català amplifica la dificultat.

### Especificació d'adaptació

```
PERFIL: Nouvingut
- Referents culturals: substitueix locals per universals o explica breument
- Glossari bilingüe amb traducció a L1 (al final)
- Suport visual: la comprensió visual no depèn de L2
- Redundància modal: text + imatge + esquema
- NO pressuposar coneixement cultural local
```

### Mapa barrera → instruccions (prioritzat)

| Prioritat | Instruccions activades | Justificació (barrera) |
|---|---|---|
| **1a (lèxica)** | A-01 (vocab freqüent), A-02 (termes en negreta), A-04 (referents explícits), A-05 (eliminar idiomàtiques), A-06 (eliminar polisèmia), A-20 (control densitat lèxica), A-21 (descomposició compostos) | Barrera nuclear: comprensió lèxica |
| **2a (cultural)** | E-08 (referents culturalment diversos), E-09 (evitar suposits culturals), E-10 (sensibilitat temes), G-01 (glossari bilingüe), G-05 (substitució referents) | Barrera cultural |
| **3a (sintàctica)** | A-07 (una idea per frase), A-09 (subjecte explícit), A-12 (limitació longitud frase), A-13 (eliminació subordinades), A-24 (present indicatiu), A-25 (formes verbals simples) | Barrera sintàctica |
| **4a (estructura)** | B-01 (paràgrafs curts), B-02 (blocs amb títol), B-07 (resum anticipatiu), C-05 (glossari previ Sweller), C-08 (anticipació vocabulari) | Suport discursiu |

### Exemple ABANS → DESPRÉS (A1, ciències naturals)

**Original:**
> La fotosíntesi és el procés bioquímic pel qual els organismes fotosintetis converteixen l'energia lluminosa en energia química, emmagatzemada en forma de compostos orgànics com la glucosa.

**Adaptat (nouvingut, A1, DUA Accés):**

## Paraules clau
- **Fotosíntesi**: les plantes fan menjar amb llum ☀️
- **Glucosa**: un tipus de sucre que fa la planta 🍬

## Text adaptat
Les plantes fan el seu menjar.
Les plantes usen la llum del sol. ☀️
Aquest procés es diu **fotosíntesi**.
La planta fabrica **glucosa** (un sucre).
La glucosa és l'aliment de la planta.

## Glossari català-àrab
| Català | العربية |
|--------|---------|
| planta | نبات |
| llum del sol | ضوء الشمس |
| menjar | طعام |

---

## 5. FONTS DEL CORPUS

| # | Referència | Tipus | Any |
|---|---|---|---|
| 1 | Decret 150/2017, de 17 d'octubre, de l'atenció educativa a l'alumnat en el marc d'un sistema educatiu inclusiu. DOGC 7477. | Normativa Catalunya | 2017 |
| 2 | Decret 175/2022, d'ordenació dels ensenyaments de l'educació bàsica. Art. 24.8. | Normativa Catalunya | 2022 |
| 3 | Departament d'Educació. Gestió del centre. Curs 2025-2026. | Instruccions operatives | 2025 |
| 4 | Programa LIC-CCE XTEC. Informes d'avaluació trimestral alumnat nouvingut. | Recurs institucional | 2025 |
| 5 | Cummins, J. (2000). *Language, Power and Pedagogy*. Multilingual Matters. | Marc teòric BICS/CALP | 2000 |
| 6 | García, O. & Wei, L. (2014). *Translanguaging: Language, Bilingualism and Education*. Palgrave. | Marc teòric translanguaging | 2014 |
| 7 | Achotegui, J. (2009). Migración y salud mental. El síndrome del inmigrante con estrés crónico. *Abendua*. | Dol migratori | 2009 |
| 8 | XTEC Ateneu — Formació escola inclusiva: alumnat nouvingut (b1-b3). Inclou: modul_1 (index, practica_2), modul_4 (index, practica_1), modul_2 (cadsuports), annex1_aules_nov_09, pla_ind_altes_capacitats, pi_del_burgar. | Formació docent | 2003–2009 |
| 9 | Coelho, E. (2012). *Language and Learning in Multilingual Classrooms*. Multilingual Matters. | Didàctica plurilingüe | 2012 |
| 10 | Huguet, À. & Navarro, J.L. (2006). Inmigración y resultados escolares. *Cultura y Educación*, 18(2). | Recerca local | 2006 |

*10 fonts · revisió completa 2026-03-26*

### Documents XTEC consultats (URLs operatius)

| # | Títol | URL |
|---|-------|-----|
| 1 | cursos:escola_inclusiva:deic:modul_4:index [Formació del professorat] | https://ateneu.xtec.cat/wikiform/wikiexport/cursos/escola_inclusiva/deic/modul_4/index |
| 2 | cursos:escola_inclusiva:deic:modul_1:index [Formació del professorat] | https://ateneu.xtec.cat/wikiform/wikiexport/cursos/escola_inclusiva/deic/modul_1/index |
| 3 | cursos:escola_inclusiva:deic:modul_4:practica_1 [Formació del professorat] | https://ateneu.xtec.cat/wikiform/wikiexport/cursos/escola_inclusiva/deic/modul_1/practica_2 |
| 4 | cursos:escola_inclusiva:deic:modul_1:practica_2 [Formació del professorat] | https://ateneu.xtec.cat/wikiform/wikiexport/cursos/escola_inclusiva/deic/modul_1/practica_2 |
| 5 | annex1_aules_nov_09_45cd56f376.pdf | http://xtec.gencat.cat/web/.content/alfresco/d/d/workspace/SpacesStore/0055/7192e6a8-1bb3-4030-b7f8-562ecd7ff933/annex1_aules_nov_09.pdf |
| 6 | pla_ind_altes_capacitats_756fd2c5a7.pdf | http://ateneu.xtec.cat/wikiform/wikiexport/_media/cursos/escola_inclusiva/diee3/modul_4/pla_ind_altes_capacitats.pdf |
| 7 | asma_d9939fd703.pdf | http://www.xtec.cat/~rgrau/exemples/asma.pdf |
| 8 | cadsuports_a8c7a072f0.pdf | http://ateneu.xtec.cat/wikiform/wikiexport/_media/cursos/escola_inclusiva/diee3/modul_2/cadsuports.pdf |
| 10 | pi_del_burgar_6348841d09.pdf | http://ateneu.xtec.cat/wikiform/wikiexport/_media/cursos/escola_inclusiva/diee/modul_2/pi_del_burgar.pdf |

*9 documents XTEC citats · URLs operatius per a traçabilitat*