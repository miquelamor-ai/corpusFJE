---
modul: M3
titol: "Adaptar un document d'activitat"
tipus: genere-discursiu
categoria_principal: generes
categories_secundaries: []
descripcio: "Instrument per adaptar un document d'activitat escolar (exercici o tasca): gènere híbrid Instructiu (consigna) + Explicatiu (context/dades). Invariant crític: la consigna i les dades del problema son INTOCABLES; es modula només la bastida lingüística del context introductori i la forma lingüística de la consigna (sense canviar-ne el contingut). Advertència PI/PAD: reduir variables, simplificar números o rebaixar el repte cognitiu és territori de Pla Individualitzat, no d'adaptació lingüística ordinària. HCL Interpretar (consigna) + les HCL que la pròpia activitat demana (Descriure, Explicar, Justificar, variable). Rúbrica gradada 8 passos × 6 nivells MECR (pre-A1→C1)."
mecr_range: [pre-A1, A1, A2, B1, B2, C1]
agent_roles: [adapter]
genre_key: activitat
macro_tipologia: hibrida
label_ca: "Activitat (exercici / tasca)"
translanguaging: true
multimodal: true
moduls_relacionats: [M3, M2, M4]
variables_configurables:
  subtipus: [exercici, tasca]
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: write-activitat@corpusFJE/skills/generes/write-activitat
review_status: revisat
version: 1.1.0
generat_at: 2026-06-25
actualitzat_at: 2026-06-25
notebooklm_review:
  data: 2026-06-25
  veredicte: validat
  notebook: MALL FJE
  notebook_id: c0615b8d-f57d-4444-b360-2cdb3bafc399
  conversation_id: f5f90250-7d3a-4611-b227-9a60e810a91a
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, invariant-consigna-intocable, advertencia-pi-pad-frontera-m3-m4, mecr-superficie-no-sostre-cognitiu]
  aplicades_post_review: [bastides-procedimentals-tea-adaptacio-m3-legitima-Q3]
  nota_validacio: "Validat NotebookLM MALL FJE 2026-06-25 (f5f90250). Gradació MECR correcta, consigna com a invariant pedagògicament impecable, frontera PI/PAD ben definida. Correcció post-review: bastides procedimentals per a TEA (checklists, sub-passos) són adaptació M3 legítima que no requereix PI — afegit al perfil TEA."
  comentari_key: null
---

# Adaptar un document d'activitat

## Descripció

El document d'activitat escolar és el **gènere híbrid de l'esfera acadèmica** per excel·lència: combina una **macro-tipologia Instructiva** (la consigna —"fes X"— que li dona forma i existència) i una **macro-tipologia Explicativa** (el context i les dades —"donades les dades X, Y..."— que li aporten el contingut sobre el qual actuar). El MALL el cita explícitament ("examen tipus test", "pla de treball") i identifica com a problema prioritari que "saben llegir però no entenen l'enunciat dels problemes" — el que confirma la necessitat d'una didàctica específica de la consigna i justifica la seva presència com a gènere autònom.

**Tipologia MALL (macro)**: Híbrida — Instructiva (dominant a la consigna) + Explicativa (dominant al context i les dades). El gènere opera amb dues macrotipologies simultàniament: la consigna mana fer ("Explica per què...", "Calcula...", "Ordena..."); el context dóna el marc sobre el qual fer-ho ("Donats els resultats de l'experiment...", "A partir del text següent..."). Adaptar l'activitat implica entendre on pertany cada part.
**HCL principal (invariant)**: Interpretar — l'alumne ha de llegir la consigna i inferir correctament la tasca demanada. Sense comprensió de la consigna, cap altra HCL és possible.
**HCL variables (depèn del tipus d'activitat)**: Descriure, Explicar, Justificar, Argumentar, Resumir — les que la pròpia activitat demana un cop la consigna és compresa. ATNE les preserva i no les rebaixa.
**S'adapta a tots els nivells (pre-A1→C1)**: el gènere és accessible a tots els nivells MECR perquè el contingut (la tasca) és independent de la forma lingüística que el vehicula. El MECR modula la **bastida lingüística** del context i la **forma** de la consigna, **no el repte cognitiu** ni la tasca demandada.

**Subtipus dins d'un sol gènere:**
- **Exercici**: pràctica focalitzada tancada, amb resposta esperada delimitada (Calcula, Encercla, Ordena, Omple). Context minimal o nul.
- **Tasca**: propòsit comunicatiu extern o obert, amb producte final (Escriu un article, Dissenya un experiment, Prepara una presentació). Context més ric i exigent.
Ambdós subtipus comparteixen la mateixa lògica consigna + dades i la mateixa regla d'intocabilitat. La variable `subtipus` al frontmatter permet declarar el tipus però la skill cobreix tots dos.

**Connexions MALL transversals:**
- *La consigna com a objecte epistèmic*: la consigna no és un text neutre — és la formulació precisa d'una operació cognitiva. Canviar la consigna (simplificar el verb, eliminar subconsignes) no és adaptar, és modificar la tasca demanada. Comprendre la consigna és la competència clau per a l'èxit acadèmic, especialment per a l'alumnat nouvingut.
- *BICS vs CALP a la consigna*: molts alumnes nouvinguts fracassen no per manca de coneixement del contingut sinó per no dominar el registre de consigna acadèmica (CALP). L'adaptació de la bastida lingüística de la consigna és, doncs, accés al contingut, no baixada de nivell.
- *Multimodalitat com a bastida d'accés*: imatges, taules, gràfics i pictogrames que acompanyen l'activitat formen part de la informació disponible per a l'alumne. Sovint redueixen la càrrega lingüística sense tocar el repte cognitiu.
- *Pont L1 per a la comprensió de la consigna*: a pre-A1/A1, la mediació oral en L1 de la consigna és legítima i necessària; no és tramperia, és accés. El principi MALL és que l'alumne entengui QUÈ se li demana per poder demostrar el que sap.
- *Advertència PI/PAD*: modificar el repte cognitiu de l'activitat (reduir el nombre de variables, simplificar els valors numèrics, eliminar subconsignes per rebaixar la complexitat de la tasca) pertany al Pla Individualitzat o al PAD i requereix coordinació amb l'equip docent. ATNE adverteix explícitament quan una sol·licitud supera la capa lingüística.

**Aclariment d'ús — distincions de gènere.**
- vs `write-instructiu`: l'instructiu dóna **passos per fer alguna cosa** (recepta, manual de muntatge); l'activitat planteja **un repte per resoldre** que demana una operació cognitiva específica.
- vs `write-informe`: l'informe **presenta resultats** ja elaborats; l'activitat **demana que l'alumne els elabori**.
- vs `write-manual`: el manual **explica conceptes**; l'activitat **aplica conceptes** en una situació concreta.

**Estructura típica del document d'activitat:**
1. Títol/nom de l'activitat
2. Context o situació d'aprenentatge (Macro Explicativa)
3. Dades, textos font, materials (variables — intocables)
4. Consigna(es) — 1 o més (Macro Instructiva): "A partir de X, fes Y"
5. Rúbrica/criteris (opcional, B1+)

## Principi general

**Regla de selecció simple.** Adapta un document d'activitat modulant SEMPRE la bastida lingüística del context introductori i la forma lingüística de la consigna (sense canviar-ne el contingut ni el repte cognitiu), i preservant **INTACTES** la consigna (el que l'alumne ha de fer), les dades del problema (valors, enunciats, textos font) i la(les) HCL demandada(es), segons el nivell MECR (pre-A1→C1).

**El MECR modula la forma lingüística, no el repte.** A pre-A1 i A1 NO es rebaixa la tasca demanada ni les operacions cognitives de l'activitat: es rebaixa la càrrega lingüística del context que envolta la consigna, i s'escala amb suport multimodal i mediació oral. Simplificar la forma lingüística de la consigna —mai canviar-ne el significat ni eliminar subconsignes. Si l'activitat demana Justificar, l'adaptació lingüística ajuda l'alumne a entendre QUÈ se li demana que justifiqui, sense eliminar l'operació de justificar.

**Límits del LLM (no judici curricular complex).** El LLM no ha de decidir si una activitat és adequada per al nivell del curs, si el nombre de subconsignes és excesiu o si els valors numèrics de l'exercici s'haurien de simplificar; només ha de garantir la preservació de la consigna i les dades, i ajustar la bastida lingüística al voltant. La idoneïtat curricular és responsabilitat del docent. Quan ATNE detecta una sol·licitud que podria implicar modificar el repte cognitiu, adverteix explícitament en lloc d'actuar.

**Advertència PI/PAD (obligatòria quan s'activa).** Si el docent sol·licita: reduir variables, simplificar números, eliminar subconsignes, rebaixar l'operació cognitiva (de Justificar a Descriure, per exemple) o modificar qualsevol element de la columna INVARIANT, ATNE genera el missatge següent abans de continuar:
> **⚠️ Avís ATNE:** La modificació sol·licitada afecta el repte cognitiu de l'activitat (no només la forma lingüística). Això és territori de Pla Individualitzat (PI) o Pla d'Atenció a la Diversitat (PAD), i requereix coordinació amb l'equip docent i, si escau, el pedagog/a o l'orientador/a. ATNE pot fer l'adaptació lingüística, però la decisió de modificar la tasca és del docent.

_Excepcions: no n'hi ha._

## Invariant disciplinari (ADAPTABLE | INVARIANT)

La taula distingeix què es modula per MECR (la bastida lingüística) del que es preserva intacte a TOTS els nivells (la consigna i les dades). La columna INVARIANT és el cor del gènere: canviar-la no és adaptar, és modificar l'activitat.

| Element | ADAPTABLE (modula per MECR) | INVARIANT (intacte pre-A1→C1) |
|---|---|---|
| **Consigna (verb + objecte)** | La bastida lingüística al voltant ("Fixa't en la taula i..." → "A partir de la taula..."); la forma sintàctica (sense canviar el significat) | El verb de la consigna i el seu objecte ("Explica per què", "Calcula la velocitat", "Ordena de menor a major"). Mai substituir per un verb d'operació cognitiva inferior. |
| **Dades del problema** | El text que les introdueix o contextualitza | Els valors, unitats, magnituds i textos font que l'alumne ha d'operar. Mai arrodonir, eliminar ni parafrasejar. |
| **Textos font de l'activitat** | El text del context introductori que emmarca el text font | El text font sobre el qual treballa l'alumne (si n'hi ha). No es reescriu ni se'n canvia el contingut. |
| **Subconsignes** | L'ordre de presentació, si s'afegeix numeració per claredat | El nombre i el contingut de les subconsignes. No s'eliminen subconsignes per "simplificar". |
| **HCL demandades** | Com es formula lingüísticament l'operació ("Descriu" → "Diga com és") per a pre-A1/A1 ÚNICAMENT i de manera excepcional, amb avís al docent | L'operació cognitiva real que l'alumne ha de fer: si la consigna demana Justificar, l'alumne ha de justificar. |
| **Context introductori** | TOT: longitud, vocabulari, connectors, estructura de les frases | El contingut informacional del context (no s'elimina informació que l'alumne necessita per respondre). |
| **Bastida lingüística** | TOT (longitud de frase, vocabulari, connectors, veu, senyaladors visuals) | — (és la dimensió que es modula) |

**Regla d'or.** Si una adaptació "simplifica" tocant la columna INVARIANT (canviar el verb de la consigna, eliminar una subconsigna, modificar un valor del problema, reescriure el text font), ha modificat l'activitat i ja no és una adaptació: és una nova activitat diferent. L'adaptació legítima viu NOMÉS a la columna ADAPTABLE i al context introductori.

## Regla de selecció per perfil

### alumne_general

**Aplica per defecte:**
- Modulació estricta de la bastida lingüística del context introductori i de la forma de la consigna, mantenint intacte l'INVARIANT.
- Tots els passos 1-8 actius segons les especificacions del nivell MECR declarat.
- Afegir senyaladors visuals (numeració, sagnat, separació visual entre consignes) a tots els nivells.

**Raonament pedagògic.** La rúbrica gradada pre-A1→C1 capta el gruix de la diferenciació; el nivell MECR és la variable principal de selecció de la forma lingüística del context i de la bastida de la consigna, mentre l'INVARIANT (consigna + dades) es manté constant.

### alumne_nouvingut_L1

**Disseny per capes (INVARIANT universal + L1 a la capa adaptable com a pont):**

- **INVARIANT universal i intacte.** La **consigna** (verb + objecte) i les **dades del problema** (valors, unitats, textos font) MAI es tradueixen ni es reemplacen per l'L1. "Calcula la velocitat mitjana si recorres 120 m en 15 s" conté dades invariants en qualsevol L1; la bastida introductòria és on entra el pont.
- **L1 NOMÉS a la capa adaptable, com a PONT (no reemplaçament):**
  - **Glossa bilingüe del terme clau de la consigna**: `terme_català (terme_L1)`, amb el **terme català sempre present i primer**. Exemples: `explica (explain)`, `justifica (justifik)`, `classifica (classifique)`. La glossa ajuda a interpretar QUÈ demana la consigna sense substituir el terme acadèmic català.
  - **Opcional**: **"instrucció clau en L1"** per a la consigna principal (1 línia màxim), marcada com a `[L1: instrucció_en_L1]`. No per a cada subconsigna. Ajuda l'alumne a comprendre la tasca global sense que sigui mediació completa.
- **Porta de decisió (L1 ESCRITA vs L1 ORAL):**
  - **L1 ESCRITA (glosses + instrucció clau)** quan `caracteristiques.nouvingut.alfabetitzacio_l1: true`.
  - **MEDIACIÓ ORAL en L1** (sense L1 escrita al document) quan `alfabetitzacio_l1: false` o desconegut. No posar mai L1 escrita que l'alumne no pugui llegir.
  - `caracteristiques.nouvingut.escolaritzacio: interrompuda` reforça la tendència cap a oral si `alfabetitzacio_l1` és desconegut.
- **Paper de `fase_lectora`.** La variable `fase_lectora` (`logografica` · `alfabetica_emergent` · `alfabetica_fluida`) mesura la descodificació lectora en català i condiciona la densitat de text català que l'alumne tolera al context introductori. No és la porta de decisió per a la L1 escrita.

**Exclou explícitament:**
- **L1 substituint l'INVARIANT** (traduir la consigna completa o els valors del problema a l'L1: esto violaría §Invariant disciplinari).
- **Traducció paral·lela completa** del document: violaria la funció del pont dirigit i desbordaria l'artefacte.

**Modulació operativa addicional:**
- Senyaladors visuals reforçats: cada consigna numerada, sagnat diferencial entre context i consigna.
- Glossari bilingüe complementari dels verbs de consigna acadèmics (Explicar, Justificar, Comparar, Analitzar...) **fora del document**, com a material de suport permanent del docent.

**Raonament pedagògic.** El fracàs acadèmic de l'alumnat nouvingut en activitats sovint no és de contingut sinó de comprensió de la consigna (CALP de la instrucció). El pont L1 a la consigna és, doncs, accés al contingut disciplinari, no baixada de nivell. El Principi 1 del MALL (TOLC, translanguaging) i els textos d'identitat lingüística (Cummins/LIT) sostenen el disseny per capes: la L1 com a pont d'accés i no com a substitut del registre acadèmic objectiu.

### alumne_DUA_acces

**Aplica:**
- Senyaladors visuals màxims: cada consigna en paràgraf propi, numeració clara, separació visual entre context i consigna.
- Marcadors [IMATGE: ...] o [ICONA: ...] sobre el verb de la consigna a pre-A1/A1 per ancorar l'operació cognitiva visualment.
- Reducció de la longitud del context introductori al mínim necessari per comprendre la consigna.
- Ressaltat tipogràfic del verb de la consigna (**negreta**) a tots els nivells.

**Raonament pedagògic.** El principi DUA d'accés demana minimitzar la càrrega de processament que no és nuclear a la tasca. A l'activitat, la càrrega no nuclear és el context introductori: simplificar-lo al màxim allibera memòria de treball per a la tasca real.

### alumne_TEA

**Aplica:**
- Estructura visual explícita: numeració de passos, espais de resposta delimitats, separació clara entre "Llegeix", "Mira" i "Fes".
- Consigna descomposta en parts si és complexa (sense eliminar subconsignes, sinó presentant-les seqüencialment i amb format diferencial).
- Eliminació de la informació contextual no essencial per a la tasca (però preservant tot el contingut necessari per respondre).
- Instruccions de format de resposta explícites ("Escriu 2-3 frases", "Marca amb una X", "Dibuixa i etiqueta").

**Bastides procedimentals com a adaptació M3 legítima (sense arribar a PI).** Abans d'activar l'advertència PI/PAD, ATNE pot proposar adaptacions que no toquen el repte cognitiu però sí la seva accessibilitat procedimental: (a) desglossament de la consigna en sub-passos numerats (`Pas 1: Llegeix...`, `Pas 2: Marca...`, `Pas 3: Escriu...`); (b) checklist de comprovació al final (`☐ He llegit la consigna sencera`, `☐ He identificat el que se m'demana`); (c) indicació del temps orientatiu per pas. Aquests recursos milloren l'autoregulació de l'alumne (funcions executives) sense reduir la complexitat de l'objectiu d'aprenentatge. Fonament: MALL DUA Pauta 6 (funcions executives) + Sanmartí (2010) autoregulació.

**Advertència especial PI/PAD per a TEA.** El MALL reconeix que per a alumnat TEA pot caldre una adaptació que va més enllà de la capa lingüística i estructural: la càrrega cognitiva (nombre d'estímuls simultanis, longitud de l'activitat, nombre de subconsignes) pot ser un obstacle real. ATNE adapta la capa lingüística i estructural; quan la sol·licitud implica modificar la càrrega cognitiva (eliminar preguntes, reduir l'extensió del text font, canviar el format de la tasca de manera substantiva), ATNE aplica l'Advertència PI/PAD (§Principi general) i deriva la decisió al docent.

**Raonament pedagògic.** L'alumnat TEA sovint té una comprensió lingüística i cognitiva adequada però es perd en la densitat visual i estructural del document. La intervenció primària (i legítimament ATNE) és l'organització visual i la claredat de la seqüència; la secundària (territoris PI) és la reducció del repte.

### alumne_AACC_o_capacitat_alta

**Inclou:**
- Context introductori més ric i amb vocabulari acadèmic ple.
- Subconsignes d'extensió o d'aprofundiment (marcades com a opcionals o d'ampliació) que no s'eliminen sinó que s'expliciten com a repte.
- Connexions interdisciplinàries al context introductori si el nivell lingüístic ho permet (B1+).

**Raonament pedagògic.** Per a AACC, l'adaptació pot incloure una bastida d'aprofundiment al context introductori sense modificar la consigna base; les extensions al repte s'afegeixen com a capes optatives, mai substituint el nivell de l'activitat original.

## Detecció

**Senyals docent** (quan adaptar com a activitat):
- El document és un full d'exercicis, una prova, un control o una tasca amb consignes explícites per a l'alumne.
- El text conté verbs imperatius d'acció cognitiva: Explica, Calcula, Ordena, Identifica, Compara, Justifica, Argumenta.
- El docent vol que l'alumne pugui fer la mateixa activitat amb una bastida lingüística adequada al seu nivell MECR.
- El text conté dades (valors, textos font, gràfics) sobre les quals l'alumne ha d'operar.

**Senyals alumne** (que indica que necessita bastida d'activitat):
- No entén QUÈ se li demana tot i saber el contingut (fracàs de comprensió de la consigna, no de contingut).
- Respon a una pregunta diferent de la demanada (ha interpretat erròniament la consigna).
- Deixa la consigna en blanc per bloqueig lingüístic, no per desconeixement del contingut.
- Confon l'operació cognitiva demanada (descriu en lloc de justificar, copia el text en lloc d'explicar-lo).

**Context favorable:**
- Qualsevol matèria amb tasques i exercicis escrits: Ciències, Matemàtiques, Ciències Socials, Llengua, Educació Física (fitxes), Arts.
- Proves i controls que el docent vol fer accessibles a l'alumnat nouvingut o NESE.
- Tasques de projecte on l'enunciat és llarg i complex.
- Activitats amb ús intensiu de vocabulari acadèmic a la consigna (CALP).

**Anti-senyals** (quan NO adaptar com a activitat):
- El text dóna instruccions pas a pas per fer alguna cosa sense plantejar un repte → instructiu.
- El text presenta resultats o informació sense demanar cap operació a l'alumne → informe o text divulgatiu.
- El text explica com funciona alguna cosa → manual o enciclopèdic.
- El document és una rúbrica d'avaluació sense consignes per a l'alumne → no és una activitat.
- No hi ha cap consigna: no hi ha res que l'alumne hagi de fer amb el text → el gènere activitat no aplica.

## Modulació per nivell

| Pas | Dimensió | pre-A1<br>Emergent | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1<br>Crític |
|---|---|---|---|---|---|---|---|
| **1. Títol i nom de l'activitat** | Orientació | Títol-etiqueta (1-3 paraules) + icona de l'acció. La consigna la llegeix oralment l'adult. | Títol curt (3-5 paraules) + icona o imatge de referència. | Títol clar + breu descripció de la tasca en 1 frase. | Títol informatiu + indicació de la HCL ("Expliqueu per què..."). | Títol precís que anticipa l'operació i el context. | Títol acadèmic amb formulació que inclou el repte i el marc disciplinari. |
| **2. Context introductori** | Bastida del marc | Absent o 1 oració mínima (SVO, present). Mediació oral de l'adult. Visual obligatori si hi ha dades. | 1-2 frases molt simples (SVO, vocabulari nuclear). Context ancorat en imatge o esquema. | 2-3 frases simples. Connectors bàsics ("i", "però", "perquè"). Context comprensible de manera autònoma. | 1-2 frases amb connector causal o temporal. Context que dona el marc suficient per a la consigna. | Paràgraf concís (3-5 frases) amb vocabulari acadèmic. Context que emmarca el problema amb precisió. | Context ric amb vocabulari disciplinari, connexions conceptuals i marc del problema ben delimitat. |
| **3. Dades, textos font i materials** | Invariant de contingut | Dades invariants. Imatge o esquema visual obligatori per a cada dada. Etiquetes mínimes. | Dades invariants. Representació visual de suport. Vocabulari de les etiquetes al mínim necessari. | Dades invariants. Taula o gràfic si existia al original. Petita llegenda si cal. | Dades invariants. Taula o gràfic etiquetat amb frase explicativa breu. | Dades invariants. Tots els elements del text font presents. Descripció objectiva si hi ha gràfics. | Dades invariants. Text font complet. Anàlisi de la relació entre les dades si la consigna ho demana. |
| **4. Consigna(es)** | Nucli de la tasca (INVARIANT de contingut) | 1 consigna: verb d'1 sílaba + objecte mínim ("Dibuixa X", "Encercla X"). Icona del verb. Mediació oral obligatòria. | 1 consigna: verb + objecte clar (3-5 paraules). Icona del verb obligatòria. 0-1 subconsigna. | 1-2 consignes curtes. Verb de la consigna en **negreta**. Numeració explícita si n'hi ha més d'una. | Consigna completa amb connector causal o condicional ("A partir de X, explica per què Y"). Subconsignes numerades. | Múltiples subconsignes jerarquitzades. Format visual que marca la jerarquia (numeració i sagnat). | Consigna acadèmica amb múltiples operacions cognitives encadenades. Formulació precisa i densa. |
| **5. Bastida lingüística (forma)** | Superfície del text | Etiquetes i paraules clau isolades. 0-1 frases per bloc. Mediació oral de l'adult. | Frases de 3-5 paraules. Vocabulari nuclear. 1 idea per frase. Senyaladors visuals màxims. | Frases simples (8-12 paraules). Connectors bàsics. Sagnat i separació entre context i consigna. | Frases amb connectors causals i condicionals. Separació visual clara entre parts. Registre funcional-acadèmic emergent. | Veu impersonal consistent. Vocabulari acadèmic. Estructura visual clara però sense senyaladors excessius. | Registre acadèmic ple. Precisió i densitat del llenguatge acadèmic. Sense bastides visuals addicionals. |
| **6. Indicadors de resposta** | Andamiatge del format | "Respon aquí: ___" amb espai grafiat o gràfic. L'adult inicia la resposta oralment. | "Escriu aquí:" + espai. Opció de dibuix o marca si la consigna ho permet. | "Escriu 1-2 frases." o "Marca amb X." Format de resposta explícit. | "Respon en 2-3 frases. Usa 'per tant' o 'perquè'." Connector guia explícit. | Format de resposta implícit en la consigna. Estructura esperada derivada de la HCL. | Cap indicador de format. L'alumne domina el format de resposta acadèmica. |
| **7. Rúbrica o criteris** | Metacognició avaluadora | Absent. L'adult dona feedback oral immediat. | Absent o 1-2 criteris en forma d'icona ("he dibuixat?", "he escrit el nom?"). | 1-2 criteris simples en forma de llista ("He respost la pregunta? Sí / No"). | Criteris breus (2-3) derivats de la HCL ("He explicat per què? He usat evidències?"). | Rúbrica amb criteris i nivells. Formulació acadèmica. Autoavaluació guiada. | Rúbrica analítica completa. L'alumne pot autoavaluar i argumentar la seva nota. |
| **8. Autoavaluació metacognitiva** | Reflexió sobre el procés | (oral, amb l'adult, mediada en L1 si cal) "He entès què havia de fer?" — l'adult acompanya l'alumne a valorar si ha comprès la consigna, no només si ha omplert l'espai. | (oral o escrit mínim) "He entès el que havia de fer? He fet el que deia la pregunta?" | "He respost el que se'm demanava." Autocomprovació senzilla de la correspondència consigna-resposta. | "La meva resposta respon la consigna? He usat la HCL correcta (explicar, justificar...)?" | "He completat totes les subconsignes i he usat el vocabulari acadèmic adequat." | "La meva resposta és rigorosa: respon exactament el que es demana, amb evidències i sense divagació." |

## Casos especials

### pre_A1_consigna_oral_mediada

**Trigger:** mecr_equals: pre-A1 AND fase_lectora_equals: logografica

**Modulació:**
- format_consigna: etiqueta_verb_amb_icona (el text escrit és mínim, la icona del verb porta el pes)
- mediacio_oral_adult: obligatoria (la consigna la llegeix i explica l'adult en L1 si cal)
- invariant_consigna: intacte (la tasca que es demana no canvia; canvia com es vehicula)
- longitud_context_max: 1 frase o absent
- espai_resposta: grafiat o dibuix si la consigna ho permet

**Raonament pedagògic.** A pre-A1 logogràfic, la consigna escrita és per a l'adult que fa de mediador, no per a l'alumne que la llegeix autònomament. L'alumne accedeix a la tasca pel canal oral i visual (icona del verb); el text escrit és el registre de la consigna. L'invariant (la tasca demanada) es manté; el vehicle canvia del text escrit a la mediació oral.

### A2_consigna_bastida_explicita

**Trigger:** mecr_equals: A2

**Modulació:**
- verb_consigna: en **negreta** sempre
- consignes_multiples: numerades explícitament
- connector_guia: afegit si la consigna implica relació entre dades ("Fixa't en X. Ara, ...")
- longitud_context_max: 3 frases simples
- format_resposta_explicat: "Escriu X frases" o format concret

**Raonament pedagògic.** A A2 l'alumne pot llegir consignes simples autònomament però perd el fil quan hi ha múltiples instruccions o quan la consigna és llarga. La numeració explícita i la bastida del connector guia descomponen el procés sense canviar la tasca.

### B1_connector_causal_obligatori

**Trigger:** mecr_equals: B1 AND hcl_includes: [explicar, justificar]

**Modulació:**
- consigna_format: inclou connector causal explícit ("A partir de X, explica per què Y")
- indicador_resposta: "Usa 'per tant' o 'perquè' a la teva resposta"
- subconsignes: jerarquitzades amb numeració i sagnat

**Raonament pedagògic.** A B1, les HCL Explicar i Justificar requereixen connectors causals que l'alumne en fase estratègica no produeix espontàniament. Modelar el connector a la consigna és una bastida de producció que s'elimina a B2 quan l'alumne ho ha interioritzat.

### C1_consigna_academica_encadenada

**Trigger:** mecr_equals: C1

**Modulació:**
- consigna_format: formulació acadèmica densa amb múltiples operacions cognitives encadenades
- rúbrica: analítica completa inclosa al document
- bastida_visual: absent (no ressaltar verbs, no indicadors de format)
- extensio_resposta: l'alumne determina el format a partir de la consigna

**Raonament pedagògic.** A C1 l'alumne ha de poder llegir i interpretar una consigna acadèmica complexa de manera autònoma. La bastida desapareix perquè la competència metacognitiva de lectura de consigna és part del que s'avalua.

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `countable` — llindar quantitatiu verificable mecànicament.
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici humà o LLM-jutge.
- `structural` — requereix anàlisi sintàctica o discursiva.
- `cross_source` — requereix accés al text font per comparar.
- `metacognitive` — descriptor de procés en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Títol i nom — Orientació | `binary` + `qualitative` | no | binary: presència de títol; qualitative: LLM-jutge sobre adequació al nivell i anticipació de la tasca |
| 2 Context introductori — Bastida | `structural` + `qualitative` | no | longitud i complexitat del context per nivell; LLM-jutge sobre suficiència per comprendre la consigna |
| 3 Dades i textos font — Invariant | `cross_source` + `binary` | **sí** (sempre) | binary/cross_source: valors, unitats i textos font del document original es conserven idèntics; detectar arrodoniments o omissions |
| 4 Consigna(es) — Nucli | `cross_source` + `binary` | **sí** (sempre) | binary/cross_source: el verb i l'objecte de la consigna originals es conserven; detectar canvis d'operació cognitiva o eliminació de subconsignes |
| 5 Bastida lingüística — Forma | `structural` + `qualitative` | no | longitud de frase i vocabulari del context per nivell; LLM-jutge sobre adequació MECR de la forma (no de la consigna) |
| 6 Indicadors de resposta — Andamiatge | `binary` + `qualitative` | no | binary: presència d'indicadors de format a pre-A1/A1/A2; qualitative: adequació al nivell i a la HCL demanada |
| 7 Rúbrica o criteris — Metacognició | `binary` | no | binary (B1+): presència de criteris derivats de la HCL demanada |
| 8 Autoavaluació metacognitiva | `metacognitive` | no | derivar a vista d'autoavaluació alumne + registre docent; LLM-jutge: la pregunta metacognitiva fa referència a la comprensió de la consigna |

**Notes:**
- La Consigna (Pas 4) i les Dades (Pas 3) son els descriptors més crítics i els més dependents del text font: requereixen comparar consigna a consigna, valor a valor, terme a terme. Qualsevol canvi a la columna INVARIANT és una deformació de l'activitat.
- Bastida lingüística (Pas 5) és la dimensió EXCLUSIVA d'actuació d'ATNE: aquí és on actua la graduació de la forma, mai al contingut.
- L'Advertència PI/PAD s'activa mecànicament quan es detecta qualsevol sol·licitud que afecti la columna INVARIANT; és un descriptor `binary` transversal a tots els passos.

## Heurístiques docent

**H1 — "La consigna és intocable: adapto el voltant, no el cor."**
Quan preparo l'adaptació, primer identifico el verb de la consigna (Explica, Calcula, Ordena, Justifica) i el marco com a INTOCABLE. Tot el que ve al voltant (el context introductori, la bastida visual, els senyaladors) és on treballo. Si em trobo reescrivint el verb o eliminant una subconsigna, m'atura: no estic adaptant, estic canviant l'activitat. Eficaç per a tots els nivells.

**H2 — "Primer la consigna; el context, al servei."**
Llegeixo l'activitat d'enrere cap endavant: primer miro QUÈ ha de fer l'alumne (la consigna) i QUINES dades necessita (l'invariant). Llavors decido quina bastida contextual mínima necessita l'alumne per arribar a la consigna. Evita el perill de simplificar tant el context que l'alumne ja no tingui prou informació per respondre, o de simplificar tant que la consigna se'n ressenti.

**H3 — "El verb de la consigna revela la HCL: no el rebaixis."**
Faig als meus alumnes un diccionari de verbs de consigna: "Explica = digues com i per què", "Justifica = dóna raons amb proves", "Calcula = fes l'operació matemàtica", "Compara = digues en que s'assemblen i en que difereixen". Quan l'alumne sap QUÈ demana cada verb, la barrera lingüística de la consigna cau i el contingut disciplinari queda accessible. Funciona especialment bé a A2-B1 i per a nouvinguts amb CALP en L1.

**H4 — "Separa visualment: llegeix / mira / fes."**
Estructuro visualment l'activitat en tres zones: la zona "Llegeix o Mira" (el context i les dades), la zona "Fes" (la consigna, en negreta i numerada), i la zona "Escriu aquí" (l'espai de resposta). Quan l'alumne veu on ha de llegir, on ha de mirar i on ha de respondre, la càrrega cognitiva d'interpretació del document baixa dràsticament. Eficaç des de pre-A1 (amb icones) fins a B1 (amb zones textuals). A B2+ desapareix.

**H5 — "Adverteix quan el repte és curricular, no lingüístic."**
Quan el docent em demana que "simplifiqui" una activitat i el que en realitat vol és reduir el nombre de variables, simplificar els números o eliminar preguntes, paro i aviso: "Això ja no és una adaptació lingüística: és una modificació de la tasca. Necessites un PI o un PAD." Saber distingir la barrera lingüística (que ATNE pot resoldre) de la barrera cognitiva (que requereix una intervenció pedagògica diferent) és la competència docent clau per usar bé l'eina.

**H6 — "Modela la resposta esperada (bastida de producció)."**
A A2 i B1, afegeixo un starter de frase al costat de la consigna: "La meva resposta: El resultat és ___ perquè ___." o "Jo crec que X perquè ___." Aquesta bastida de producció dona a l'alumne la motxilla lingüística per respondre sense haver de construir el format de resposta des de zero. No és fer la feina per l'alumne: és mostrar-li la forma que ha d'omplir amb el seu contingut.

## Encaix DUA

El document d'activitat és el gènere escolar on la càrrega lingüística i la càrrega cognitiva sovint es confonen — i on el DUA pot tenir l'impacte més gran. L'adaptació per DUA no és rebaixar el repte: és eliminar les barreres d'accés que no son el repte real.

**Representació múltiple.** La consigna es pot presentar en format textual, visual (icona del verb d'operació) i oral (mediació adulta o àudio). Les dades es poden presentar en format numèric, taula i gràfic simultàniament sense que l'invariant canviï. La bastida visual (zones "Llegeix / Mira / Fes") és representació múltiple de l'estructura del document.

**Acció i expressió múltiple.** L'espai de resposta pot admetre formats múltiples (text escrit, dibuix + etiqueta, enregistrament oral, taula de resposta) sense canviar la HCL demanada. Si la consigna demana Explicar, l'alumne pot explicar per escrit, oral o diagramàticament, sempre que la HCL sigui operativa.

**Implicació i motivació.** La connexió entre la tasca de l'activitat i el món real o el coneixement previ de l'alumne reforça la motivació. Quan el context introductori connecta amb l'experiència de l'alumne (rellevant a nouvinguts i DUA), la comprensió de la consigna millora.

**Distinció crítica DUA/PI.** El DUA opera sobre l'accés (bastida lingüística, representació múltiple, format de resposta); el PI opera sobre el repte (modificar la tasca, reduir la complexitat cognitiva). ATNE cobreix el primer; el segon pertany a la coordinació pedagògica. Quan la sol·licitud docent travessa aquesta frontera, ATNE aplica l'Advertència PI/PAD (§Principi general).

**Marc transversal de perfil**: `M1_discapacitat-visual.md` (perfil canon, `locked: true`) per a alumnat amb discapacitat visual: les dades en imatges o gràfics han de tenir equivalent textual. `M5_accessibilitat-digital.md` aporta marc complementari d'estàndards.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Activitat
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
### Context
### Dades
### Consigna
### Espai de resposta
```

**Sub-headers H3 opcionals** (literals exactes, apareixen condicionalment):
```
### Criteris                  ← B1+ si la consigna inclou rúbrica o criteris en l'original
### Com ho he fet             ← autoavaluació metacognitiva (derivat a vista alumne)
```

**Bullets / moments interns** (si aplica):
```
- Consignes múltiples: llista numerada dins de ### Consigna
- Subconsignes: sangrades amb lletra (a., b., c.) sota la consigna principal
```

**Marcadors inline obligatoris** (si aplica):
```
[IMATGE: descripcio_breu]         ← imatge present al document original
[TAULA: capçalera1 | capçalera2]  ← taula de dades present al document original
[GRAFIC: tipus|descripcio_breu]   ← gràfic present al document original
[ICONA: nom_accio]                ← icona del verb de consigna (pre-A1/A1)
[L1: text_en_L1]                  ← instrucció clau en L1 (nouvingut, 1 línia màx.)
[⚠️ PI/PAD: motiu_breu]          ← advertència quan la sol·licitud supera la capa lingüística
```

**Senyaladors tipogràfics obligatoris:**
```
**verb_consigna**   ← el verb de la consigna sempre en negreta (pre-A1 a B1)
1. / a. / b.        ← numeració explícita de consignes i subconsignes (pre-A1 a B2)
```

**Headers explícitament PROHIBITS:**
```
## Introducció
## Enunciat
## Pregunta
## Tasca
## Exercici
```
(Aquests headers substituirien l'estructura canònica i impossibilitarien el parsing automàtic.)

**Regla d'integritat estructural.** Sense el header literal `## Activitat` i sense els H3 en aquest ordre, el parser no detecta els blocs modulars i el descriptor Pas 4 (intocabilitat de la consigna) i Pas 3 (intocabilitat de les dades) no es pot aplicar mecànicament. La modulació per nivell (pre-A1/A1 sense `### Criteris`; B1+ amb `### Criteris` si l'original en tenia; C1 sense `### Espai de resposta`) determina quins H3 són obligatoris i quins opcionals. `### Dades` és opcional si l'activitat és un exercici sense dades externes.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): HCL Interpretar com a competència nuclear per a l'accés a l'activitat acadèmica. Cita explícita del gènere ("examen tipus test", "pla de treball") i del problema de comprensió de consignes ("saben llegir però no entenen l'enunciat dels problemes"). **Principi 1 (TOLC, translanguaging)** com a base del disseny per capes a `alumne_nouvingut_L1`.
- MALL Educació Secundària (MALL ESO): p. 13 (competència subjacent comuna, Cummins; l'accés al contingut disciplinari depèn de comprendre la instrucció en L2, no dels coneixements en si) i p. 21 (HCL com a operacions cognitives específiques que l'alumne ha de dominar en la nova llengua vehicular).
- MALL MOPI/PIN: p. 31 (efectes positius de l'ús de les llengües d'origen en la motivació i el rendiment; pont L1 per a la comprensió de la consigna com a accés, no com a substitut).
- Cummins, J. (2000): *Language, Power and Pedagogy* — distinció BICS/CALP aplicada a la comprensió de consignes acadèmiques: l'alumne nouvingut pot tenir el contingut però no el CALP de la instrucció. **Textos d'identitat lingüística (LIT)** com a justificació de la instrucció clau en L1.
- MELVIVES (Principi 10): "Acollir cada infant en la seva llengua reforça la seva competència lingüística" — suport per al pont L1 a la comprensió de la consigna.
- Gibbons, P. (2002): *Scaffolding Language, Scaffolding Learning* — bastides de producció (starters de frase, indicadors de format de resposta) com a andamiatge legítim que no rebaixa el repte cognitiu.
- Rose, D. i Martin, J.R. (2012): *Learning to Write, Reading to Learn* — els verbs de consigna com a operadors de les HCL; la comprensió del gènere instruccional acadèmic com a competència disciplinària.
- CAST (2018): *Universal Design for Learning Guidelines* — representació múltiple i acció i expressió múltiple com a principis d'accés sense modificació del repte.
- Decret 175/2022 (currículum Catalunya): competències transversals i competència comunicativa lingüística. Distinció entre adaptació curricular (PI/PAD) i adaptació d'accés (DUA).
