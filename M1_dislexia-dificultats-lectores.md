---
modul: M1
titol: "Dislèxia i dificultats lectores"
tipus: caracteristica
subtipus: constitutiva
descripcio: "Dislèxia: definició IDA 2025, classificació neurocognitiva, detecció (PRODISCAT/APPA), adaptacions per ruta afectada i grau de severitat"
review_status: revisat
generat_at: 2026-03-18T15:28:19
actualitzat_at: 2026-03-25T22:00:00
variables_configurables:
  - nom: tipus_dislexia
    etiqueta: "Tipus de dislèxia (ruta afectada)"
    tipus: enum
    valors: [fonologica, superficial, mixta]
    obligatori: true
    defecte: fonologica
    descripcio: "Fonològica: falla via grafema-fonema, confon paraules similars en so. Superficial: falla via visual/lèxica, confon homòfons. Mixta: ambdues vies afectades, errors semàntics"
    impacte: "Fonològica: paraules freqüents, evitar vocabulari fonèticament complex. Superficial: paraules curtes, evitar homòfons. Mixta: màxima simplificació, redundància semàntica"
  - nom: grau
    etiqueta: "Grau de severitat"
    tipus: enum
    valors: [lleu, moderat, sever]
    obligatori: true
    defecte: moderat
    descripcio: "Lleu: compensable amb adaptacions bàsiques. Moderat: intervenció sistemàtica. Sever: dificultats persistents, text molt simplificat + suport multimodal"
    impacte: "Lleu: estructura clara, tipografia neta. Moderat: frases curtes, suport visual. Sever: text mínim, redundància en 3 canals (text+imatge+oral)"
  - nom: tipografia_adaptada
    etiqueta: "Tipografia adaptada per dislèxia"
    tipus: boolean
    obligatori: false
    defecte: false
    descripcio: "Activa tipografia palo sec (Arial/Verdana/OpenDyslexic), interlineat generós, espaiat ampli. Afecta renderitzat, no contingut"
    impacte: "Si sí: aplicar CSS amb font sans-serif, interlineat 1.5-2, espaiat entre lletres augmentat"
  - nom: columnes_estretes
    etiqueta: "Columnes estretes (màx. 44 caràcters/línia)"
    tipus: boolean
    obligatori: false
    defecte: false
    descripcio: "Limita l'amplada de text per reduir errors de seguiment de línia"
    impacte: "Si sí: format de columna estreta, màxim 44 caràcters per línia"
---

### 1. CONTINGUT ESPECÍFIC

#### Descripció del tret

##### Definició i base neurobiològica

La dislèxia és un trastorn específic de l'aprenentatge de base neurobiològica que afecta principalment la lectura precisa i fluida i l'ortografia. La definició de consens més actualitzada és la del projecte Delphi (Carroll et al., 2025), adoptada com a referència per la **International Dyslexia Association (IDA, 2025)**:

> *"Dyslexia is a specific learning disability characterized by difficulties in word reading and/or spelling that involve accuracy, speed, or both and vary across languages."*

Aquesta revisió de 2025 suposa avenços conceptuals rellevants:
- **Reconeix la dislèxia com a contínuum**, no com a categoria binària
- **Elimina el criteri de discrepància QI**, superat per la recerca
- **Afegeix la fluïdesa** (velocitat) com a dimensió nuclear, no només l'exactitud
- Reconeix que les manifestacions **varien entre sistemes ortogràfics** (transparents com el català vs. opacs com l'anglès)
- **Amplia les conseqüències secundàries**: comprensió lectora, vocabulari, expressió escrita, benestar emocional i oportunitats vitals

La base neurobiològica implica diferències en circuits cerebrals de processament fonològic (via parieto-temporal), automatització lectora (via occipito-temporal) i producció (via frontal). La recerca genètica de 2025 ha identificat **80 regions del genoma associades a la dislèxia**, 36 de noves, amb gens implicats en el desenvolupament cerebral primerenc i solapament amb TDAH.

La investigació de **Carreiras et al. (Basque Center on Cognition, 2025)**, dins el projecte europeu *Cortical Rhythmics*, evidencia que les **ones cerebrals corticals mostren diferències detectables des dels 4 mesos** i mig en infants que posteriorment presenten dislèxia, obrint la porta a biomarcadors precoços.

##### Prevalença i perfil

- Afecta aproximadament el **5-17% de la població** depenent dels criteris diagnòstics i la llengua
- Proporció similar en nens i nenes (el biaix masculí clàssic respon a biaixos de derivació)
- **Alta comorbiditat** amb TDAH, TDL (Trastorn del Desenvolupament del Llenguatge), discalcúlia i trastorn del desenvolupament de la coordinació (Carroll et al., 2025)
- La dislèxia **coexisteix amb capacitats intel·lectuals normals o altes**

##### Classificació neurocognitiva (rutes lectores)

| Tipus | Ruta afectada | Error característic | Adaptació textual específica |
|---|---|---|---|
| **Fonològica** | Via grafema-fonema | Confon paraules similars en so; problemes amb pseudoparaules | Paraules freqüents i conegudes, evitar vocabulari nou fonèticament complex |
| **Superficial** | Via visual/lèxica | Confon homòfons, regularitza paraules irregulars, velocitat decreix amb paraules llargues | Paraules curtes, evitar homòfons ambigus, estructures morfològiques simples |
| **Mixta/Profunda** | Ambdues vies | Errors semàntics (llegeix una paraula per una altra de significat similar) | Màxima simplificació, redundància semàntica, contextos molt explícits |

**Grau de severitat (DSM-5-TR)**:
*   **Lleu**: dificultats compensables amb suport i adaptacions bàsiques
*   **Moderat**: requereix intervenció especialitzada i adaptacions sistemàtiques
*   **Sever**: dificultats persistents malgrat intervencions intensives; necessita text molt simplificat i suport multimodal

**Variables de format visual** (Rello, 2020 — Change Dyslexia, 97 participants):
*   **Tipografia**: palo sec (Arial, Verdana, OpenDyslexic) vs. serif; evitar cursiva
*   **Interlineat i espaiat**: espaiat ampli redueix errors i augmenta velocitat lectora
*   **Amplada de columna**: màxim 44 caràcters/línia per reduir errors de seguiment

Aquestes variables afecten el renderitzat (CSS), no el contingut generat per la IA, però són part integral de l'adaptació per dislèxia.

#### Manifestació per etapa educativa

| Etapa | Senyals prelectores/lectores | Senyals d'escriptura | Impacte emocional |
|-------|------------------------------|----------------------|-------------------|
| **Infantil (I3–I5)** | Dificultat en rimes i segmentació sil·làbica; aprenentatge lent de lletres; historial familiar de dislèxia | — | Frustració en tasques de prereading |
| **Primària (1r–3r)** | Errors de decodificació, confusió b/d/p/q, lectura lenta i molt esforçada, pseudoparaules impossibles | Ortografia molt deficient, lletra irregular | Ansietat lectora, evitació |
| **Primària (4t–6è)** | Lectura mecànica sense fluïdesa, mala comprensió per excés d'esforç decodificador | Textos escrits molt curts i estructuralment simples | Baixa autoestima acadèmica |
| **ESO** | Lectura lenta persistent (fins i tot amb exactitud acceptable), problemes en exàmens amb molt text | Ortografia erràtica, expressió escrita pobra | Desmotivació, comparació negativa amb iguals |
| **Batxillerat/FP** | Lentitud en lectura extensiva, dificultats en idiomes estrangers escrits | Redaccions amb errors ortogràfics persistents | Síndrome de l'impostor, impacte en decisions vocacionals |

#### Barreres d'aprenentatge

*   **Fonològica:** Dificultat per manipular segments sonors de les paraules (fonemes, rimes, síl·labes). Base del dèficit nuclear en la majoria de casos
*   **Fluïdesa lectora:** Automatització deficient que ocupa recursos cognitius, empobrint la comprensió
*   **Velocitat de processament:** Lentitud generalitzada en tasques simbòliques
*   **Memòria de treball verbal:** Dificultats per mantenir seqüències d'instruccions o text oral mentre es processa
*   **Ortografia:** Representació ortogràfica inestable; errors persistents malgrat l'aprenentatge explícit
*   **Emocional/motivacional:** Cicle de frustració → evitació → menys pràctica → major retard. L'exposició acumulada a la lectura és un predictor clau del vocabulari i el coneixement general

#### Necessitats prioritàries

1.  **Instrucció lectora estructurada i explícita** (Structured Literacy): ensenyament sistemàtic de la correspondència grafema-fonema, síl·labes, morfemes. Evidència RCT extensa (Snowling, 2024)
2.  **Intervenció intensiva en fluïdesa lectora**: lectura repetida, paired reading, texts al nivell instruccional
3.  **Suport multimodal**: integrar canal auditiu (text a veu), visual i cinestèsic per consolidar associacions lletra-so
4.  **Adaptació de materials i avaluació** (veure variables_configurables): tipografia, interlineat, columnes estretes, temps addicional
5.  **Suport socioemocional**: adreçar la baixa autoestima acadèmica; treballar atribucions causals adaptatives

#### Fortaleses a aprofitar

*   Creativitat i pensament visual-espacial freqüentment preservats o destacats
*   Capacitat de raonament oral i comprensió auditiva sovint superiors a la lectura
*   Alta motivació quan se'ls ofereix el suport adequat i s'elimina la barrera de la decodificació
*   Pensament holístic i capacitat de connexió entre idees

#### Senyals identificadors a l'aula

**Senyals d'alarma precoç (Infantil/1r Primària):**
*   Dificultat per aprendre rimes i cançons
*   Lentitud en reconèixer el propi nom escrit
*   No automatitza el nom de les lletres malgrat l'exposició repetida
*   Historial familiar de dificultats lectores

**Senyals consolidats (Primària–ESO):**
*   Lectura molt lenta i esforçada, amb errors de decodificació (omissions, substitucions, inversions)
*   Gran discrepància entre capacitat oral i rendiment escrit
*   Ortografia erràtica en paraules conegudes
*   Evitació de tasques de lectura i escriptura
*   Millora notable amb temps addicional o lectura en veu alta

**Anti-senyals (que no apunten a dislèxia):**
*   Dificultats únicament en una llengua (L2), però no en L1
*   Dificultat en totes les matèries incloent matemàtiques sense component lector
*   Millora ràpida i completa amb instrucció ordinària

#### Perfils associats i comorbiditats

*   **Dislèxia + TDAH**: comorbiditat documentada en un 30-40% dels casos. La fatiga lectora esgota la capacitat atencional ja limitada. Veure dependència #7 a M1_creuament-variables-dependencies.md
*   **Dislèxia + TDL**: ambdós canals (oral i escrit) compromesos. Veure dependència #10
*   **Dislèxia + Altes capacitats (2e)**: masking mutu — la intel·ligència compensa la dislèxia i viceversa. Veure dependència #13
*   **Dislèxia + Nouvingut**: la barrera lingüística amplifica la fatiga lectora. Veure dependència #2
*   **Dislèxia + Discalcúlia**: comparteixen dèficits en processament simbòlic
*   **Dislèxia + Trastorn del desenvolupament de la coordinació** (Carroll et al., 2025)

#### Principis d'actuació

*   **Adaptar continguts:** Prioritzar la fluïdesa sobre l'exactitud en els textos generats: frases curtes, estructura predictible. No confondre dislèxia amb baixa intel·ligència ni amb manca d'esforç.
*   **Adaptar activitats:** Oferir alternatives d'accés multimodal (text a veu, representació visual, oral). Evitar tasques que depenguin exclusivament de la lectura autònoma per accedir al contingut.
*   **Adaptar avaluació:** En tasques escrites, valorar el contingut conceptual per sobre de la correcció ortogràfica. Permetre temps addicional, formats orals o tecnologia assistiva.
*   **Adaptar interacció:** Activar les variables configurables (tipografia, columnes, tipus de dislèxia) per personalitzar el renderitzat. No confondre dislèxia amb dificultats per L2 (però tenir present que poden coexistir).

#### Línies vermelles

*   **No diagnosticar dislèxia** basant-se únicament en errors ortogràfics puntuals. **Per què?** La dislèxia és un diagnòstic clínic que requereix avaluació especialitzada.
*   **No atribuir les dificultats a falta de motivació, mandra o baixa capacitat.** **Per què?** La dislèxia és de base neurobiològica; l'esforç que fa l'alumne per llegir pot ser enorme i invisible.
*   **No eliminar l'accés als textos: adaptar, no simplificar fins a buidar de contingut.** **Per què?** L'alumne amb dislèxia pot processar contingut complex — el problema és el canal, no la capacitat.
*   **No confondre el perfil de dislèxia fonològica amb el de dislèxia superficial.** **Per què?** Les adaptacions òptimes difereixen: la fonològica necessita vocabulari freqüent, la superficial paraules curtes.
*   **No considerar la dislèxia "superable" sense suport.** **Per què?** És un tret persistent que requereix acomodació continuada al llarg de tota l'escolarització.

#### Detecció i protocols

##### Principis de detecció (Response to Intervention / RTI)

La literatura actual defensa la detecció basada en resposta a la instrucció (RTI / Multi-Tiered Systems of Support), no en la discrepància QI-rendiment:
1.  **Nivell 1:** Instrucció universal de qualitat + cribatge universal
2.  **Nivell 2:** Intervenció en petit grup intensiva per a alumnat en risc
3.  **Nivell 3:** Intervenció individualitzada per a alumnat amb dificultats persistents

L'estudi de Vale De Oliveira et al. (2026) confirma que una intervenció fonosil·làbica multimodal sistemàtica aplicada a infants identificats precoçment elimina les diferències amb el grup de comparació en la majoria de casos, però subratlla la necessitat de suport individualitzat continuat per al subgrup amb dificultats persistents.

##### Protocols a Catalunya

*   **PRODISCAT** (Departament d'Ensenyament / Col·legi de Logopedes de Catalunya): protocol de cribatge per edats des d'I3 fins als 18 anys, per a ús dels docents a l'aula
*   **Projecte APPA** (Accions de Prevenció per Promoure l'Aprenentatge): pilot 2026 del Departament d'Educació amb 450 centres i 25.000 alumnes de 1r i 3r de primària per detecció precoç de dificultats lectores. Inclou derivació a Pediatria per a diagnòstic de trastorns específics com la dislèxia
*   **CLC — Trastorns del Desenvolupament de l'Aprenentatge (2025)**: guia clínica que inclou PRODISLEX, PROLEXIA i recomanacions d'avaluació multiaxial

### 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M1_TDAH**: Comorbiditat 30-40%. Veure dependència #7 (dislèxia × TDAH) al document de creuaments
*   **M1_TDL-trastorn-llenguatge**: Ambdós canals compromesos. Veure dependència #10 (dislèxia × TDL)
*   **M1_altes-capacitats**: Doble excepcionalitat (2e). Veure dependència #13 i secció 2e
*   **M1_alumnat-nouvingut**: La barrera L2 amplifica la fatiga lectora. Veure dependència #2
*   **M1_creuament-variables-dependencies**: Dependencies #2, #7, #10, #13
*   **M3_lectura-facil-comunicacio-clara**: Tècniques de simplificació directament aplicables
*   **M2_carrega-cognitiva-adaptacio-textos**: Gestió de la càrrega cognitiva per perfil lector
*   **M2_DUA-principis-pautes**: Marc general d'accessibilitat

### 3. DETECCIÓ (Variables de Context)

*   **Senyals del docent:**
    *   "Llegeix molt lentament i amb molts errors, tot i que entén bé quan li explico oralment."
    *   "La seva ortografia és molt erràtica, fins i tot en paraules que hem treballat moltes vegades."
    *   "Evita llegir en veu alta i es posa molt nerviós quan li toca."
    *   "Hi ha una gran diferència entre el que sap dir i el que pot escriure."
    *   "Confon lletres similars (b/d, p/q) de manera persistent."
    *   "Té dificultats en idiomes estrangers escrits que no corresponen amb la seva capacitat oral."
*   **Senyals de l'alumne:**
    *   Frustració o ansietat davant tasques de lectura
    *   Evitació sistemàtica de la lectura i l'escriptura
    *   Verbalitza que "és ximple" o que "no serveix per estudiar"
    *   Rendiment oral molt superior al rendiment escrit
*   **Senyals de context:**
    *   Historial familiar de dificultats lectores
    *   Dificultats persistents malgrat instrucció adequada i continuada
    *   Millora significativa amb temps addicional o amb suport oral
*   **Anti-senyals:**
    *   Les dificultats apareixen només en L2 però no en L1 (pot ser barrera lingüística, no dislèxia)
    *   Dificultat generalitzada en totes les àrees sense component lector específic
    *   Millora ràpida i completa amb instrucció ordinària
    *   Les dificultats es van iniciar recentment i no tenen historial

### 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

*   **Principi general:** L'agent ha d'adaptar el format i la complexitat lèxica del text segons el tipus de dislèxia i el grau de severitat, sense reduir la profunditat conceptual. La dislèxia afecta el canal, no la capacitat.

*   **Heurístiques per a l'Agent DOCENT:**

    *   **Nom:** Adaptació per ruta afectada
    *   **Quan aplica:** Quan el docent indica que l'alumne té dislèxia i es coneix el tipus.
    *   **Fonament:** La dislèxia fonològica, superficial i mixta requereixen estratègies lèxiques diferents. Aplicar una estratègia genèrica pot ser subòptim.
    *   **Exemple complet de raonament:** "El docent indica que l'alumna té dislèxia fonològica i necessita adaptar un text de ciències. L'agent ha de raonar que la via grafema-fonema està compromesa, per tant ha de prioritzar vocabulari freqüent i conegut, evitar paraules noves fonèticament complexes (o introduir-les amb molt suport), i usar contextos que facilitin la deducció del significat. No ha de simplificar el contingut conceptual — l'alumna pot entendre la fotosíntesi, però necessita que les paraules siguin predictibles per la via lèxica. A més, ha d'activar la tipografia adaptada si està disponible."

    *   **Nom:** Detecció vs. diagnòstic — el paper del docent
    *   **Quan aplica:** Quan un docent pregunta si un alumne "té dislèxia" basant-se en errors lectors.
    *   **Fonament:** El docent detecta senyals, no diagnostica. El protocol RTI estableix tres nivells de resposta abans del diagnòstic clínic.
    *   **Exemple complet de raonament:** "Un docent pregunta si un alumne nouvingut que llegeix malament 'podria tenir dislèxia'. L'agent ha de raonar que primer cal descartar que les dificultats siguin per la barrera lingüística (L2). Si l'alumne també llegeix amb dificultats en la seva L1, el senyal és més consistent. L'agent recomanaria al docent: (1) observar si hi ha dificultats en L1, (2) aplicar adaptacions de Nivell 1 (instrucció de qualitat), (3) si persisteix, derivar al logopeda o EAP per a cribatge amb PRODISCAT. No dir mai a la família que l'alumne 'té dislèxia' sense avaluació professional."

    *   **Nom:** Fluïdesa, no només exactitud
    *   **Quan aplica:** Quan es dissenyen activitats lectores per a alumnat amb dislèxia.
    *   **Fonament:** La definició IDA 2025 inclou la fluïdesa com a dimensió nuclear. Un alumne que llegeix exactament però molt lentament necessita suport tant com un que comet errors.
    *   **Exemple complet de raonament:** "Un docent diu que l'alumna 'ja llegeix bé' perquè no comet gaires errors. L'agent ha de raonar que l'exactitud no és l'únic indicador — si la lectura és molt lenta, l'alumna gasta tots els seus recursos cognitius en descodificar i no en comprendre. L'agent recomanaria avaluar la fluïdesa (paraules per minut) i, si és baixa, implementar pràctica de lectura repetida amb textos al nivell instruccional per automatitzar la decodificació."

*   **Heurístiques per a l'Agent ALUMNE:**

    *   **Nom:** Accés multimodal al contingut
    *   **Quan aplica:** Quan l'alumne ha de llegir un text per a una tasca.
    *   **Fonament:** La dislèxia afecta la lectura, no la comprensió auditiva ni el raonament. Oferir canals alternatius elimina la barrera.
    *   **Exemple complet de raonament:** "Un alumne amb dislèxia ha de llegir un capítol de novel·la per a classe. L'agent suggeriria: (1) escoltar l'audiollibre mentre segueix el text amb el dit, (2) llegir en veu alta amb un company (paired reading), (3) usar un lector de pantalla. L'objectiu és que accedeixi al contingut i pugui participar en la discussió a classe, no que demostri que sap descodificar."

    *   **Nom:** Gestió de la frustració lectora
    *   **Quan aplica:** Quan l'alumne expressa frustració, vergonya o evitació davant la lectura.
    *   **Fonament:** El cicle frustració → evitació → menys pràctica → major retard és el principal risc a llarg termini.
    *   **Exemple complet de raonament:** "L'alumne diu que 'no serveix per llegir'. L'agent ha de validar la frustració ('Entenc que llegir et costa molt esforç, i això és real — no és culpa teva'), explicar que la dislèxia afecta com el cervell processa les lletres però NO la intel·ligència, i proposar estratègies concretes per reduir la barrera (text a veu, tipografia adaptada, temps extra). L'objectiu és trencar el cicle d'evitació mantenint el contacte amb el text."

---

## 6. INSTRUCCIONS D'ADAPTACIÓ TEXTUAL PER A L'LLM

### Barrera nuclear
**Descodificació**: L'alumnat amb dislèxia té com a barrera principal la descodificació lectora — el processament fonològic i la conversió grafema-fonema. Les paraules llargues, poc freqüents o amb estructura morfològica complexa (prefixos+arrel+sufixos) generen fatiga lectora exponencial.

### Instruccions per al prompt LLM

```
PERFIL: Dislèxia (Dehaene/Wolf)
- Evita paraules compostes llargues: divideix o reformula
- Prefereix paraules d'alta freqüència lèxica
- Repeteix termes clau en lloc d'usar sinònims
- Frases 2-3 paraules més curtes que el màxim MECR
- Evita encadenar prefixos i sufixos
```

### Mapa barrera → instruccions (prioritzat)

| Prioritat | Instruccions activades | Justificació (barrera) |
|---|---|---|
| **1a (descodificació)** | H-07 (evitar compostos llargs), H-08 (alta freqüència, no sinònims), A-21 (descomposició compostos) | Barrera nuclear: descodificació |
| **2a (fatiga visual)** | I-01 (sans-serif 14pt), I-02 (interlineat 1.5), I-03 (columna estreta), I-04 (fons suau), I-05 (alineat esquerra) | Reduir fatiga visual (CSS/FE) |
| **3a (compensació)** | D-06 (text per veu alta), A-03 (coherència terminològica) | Canal oral com a complement |

### Exemple ABANS → DESPRÉS (B1, ciències naturals)

**Original:**
> La fotosíntesi és el procés bioquímic pel qual els organismes fotosintetis converteixen l'energia lluminosa en energia química, emmagatzemada en forma de compostos orgànics.

**Adaptat (dislèxia, B1, DUA Core):**

## Text adaptat
Les plantes fan el seu propi aliment. Aquest procés es diu **fotosíntesi**.

La planta usa la llum del sol.
La planta agafa aigua i diòxid de carboni.
Amb la llum, la planta fa **glucosa** (un sucre).

La **glucosa** és l'energia de la planta.
La planta guarda la glucosa per créixer.

> Nota: en lloc de "organismes fotosintetitzadors" → "plantes". Paraula curta i d'alta freqüència.

---

## 5. FONTS DEL CORPUS

| # | Referència | Tipus | Any |
|---|-----------|-------|-----|
| 1 | Carroll, J.M. et al. *Toward a consensus on dyslexia: findings from a Delphi study.* JCPP. | Revisió Delphi consens | 2025 |
| 2 | IDA *2025 Dyslexia Definition Project.* dyslexiaida.org | Definició oficial | 2025 |
| 3 | Snowling, M.J. *Dyslexia and Language: Disorder or Difference?* Gresham College. | Conferència evidència | 2024 |
| 4 | Vale De Oliveira et al. *Effects of a structured multisensory phonics-based intervention.* Frontiers in Education. | RCT intervenció | 2026 |
| 5 | Mountford, H. et al. *Genetic study of dyslexia (1.2M participants).* Translational Psychiatry. | Genètica | 2025 |
| 6 | Carreiras, M. et al. *Cortical Rhythmics project.* Basque Center on Cognition. | Biomarcadors | 2025 |
| 7 | Departament d'Educació Catalunya. *Projecte APPA.* 3Cat. | Protocol Catalunya | 2026 |
| 8 | PRODISCAT. *Protocol de Detecció i Actuació en la Dislèxia.* Col·legi Logopedes Catalunya. | Protocol Catalunya | Vigent |
| 9 | CLC. *Trastorns del Desenvolupament de l'Aprenentatge.* Guia BP_08. | Guia clínica | 2025 |
| 10 | Rello, L. *Change Dyslexia.* Investigació sobre llegibilitat tipogràfica. | Llegibilitat | 2020 |

*10 fonts referencials · document actualitzat 2026-03-25*
