---
name: write-enunciat
description: 'Instrument per adaptar un enunciat escolar (exercici, activitat o tasca):
  el docent parteix d''una situació —més o menys globalitzada, concreta i situada
  o abstracta— i demana a l''alumne que la resolgui. Macro-tipologia instructiva:
  la consigna domina i dona existència al gènere, amb un component explicatiu fort
  al context i les dades. Invariant crític: la consigna i les dades del problema son
  INTOCABLES; es modula només la bastida lingüística del context introductori i la
  forma lingüística de la consigna (sense canviar-ne el contingut). Advertència PI/PAD:
  reduir variables, simplificar números o rebaixar el repte cognitiu és territori
  de Pla Individualitzat, no d''adaptació lingüística ordinària. Competència d''accés
  (prerequisit, no HCL): comprendre la consigna. Operació demandada (variable i intocable,
  la fixa la consigna): pot ser una HCL del MALL (Descriure, Definir, Explicar, Justificar,
  Argumentar, Demostrar) o una operació procedimental (calcular, resoldre, ordenar,
  classificar). Rúbrica gradada 8 passos × 6 nivells MECR (pre-A1→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 1.3.0
tools_required: []
agent_role: adapter
genre_key: enunciat
triggers:
- path: params.genere_discursiu
  equals: enunciat
macro_tipologia: instructiva
label_ca: Enunciat (exercici / activitat / tasca)
mecr_range:
- pre-A1
- A1
- A2
- B1
- B2
- C1
translanguaging: true
multimodal: true
moduls_relacionats:
- M3
- M2
- M4
font_canonic: M3_genere-escriure-enunciat.md
font_version: 1.3.0
generat_at: '2026-06-28'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 0a8478074ae52891
---

# Adaptar un enunciat escolar — skill operativa per a LLM

El document d'activitat escolar és el **gènere híbrid de l'esfera acadèmica** per excel·lència: combina una **macro-tipologia Instructiva** (la consigna —"fes X"— que li dona forma i existència) i una **macro-tipologia Explicativa** (el context i les dades —"donades les dades X, Y..."— que li aporten el contingut sobre el qual actuar). El MALL el cita explícitament ("examen tipus test", "pla de treball") i identifica com a problema prioritari que "saben llegir però no entenen l'enunciat dels problemes" — el que confirma la necessitat d'una didàctica específica de la consigna i justifica la seva presència com a gènere autònom.

**Tipologia MALL (macro)**: Instructiva (família canònica). La consigna —el que mana fer ("Explica per què...", "Calcula...", "Ordena...")— domina i dona existència al gènere; per això la macro-família és la **instructiva**. Ara bé, el gènere té un **component explicatiu fort**: el context i les dades ("Donats els resultats de l'experiment...", "A partir del text següent...") aporten el marc sobre el qual l'alumne ha d'operar. Adaptar l'enunciat implica entendre on pertany cada part: la consigna (instructiva, intocable) i el context (explicatiu, modulable).
**Competència d'accés (prerequisit, NO és una HCL)**: comprendre la consigna — l'alumne ha de llegir la consigna i inferir correctament la tasca demanada. No és una HCL del MALL, sinó la competència prèvia que habilita qualsevol operació posterior: sense comprensió de la consigna, cap HCL ni cap operació és possible. És, justament, el cor de la dificultat que el MALL assenyala ("saben llegir però no entenen l'enunciat dels problemes").
**Operació demandada (variable i INVARIANT — la fixa la consigna)**: un cop compresa la consigna, l'alumne ha d'executar l'operació que aquesta demani, i ATNE la preserva sense rebaixar-la mai. Pot ser de dos tipus:
- una **HCL del MALL** (operació cognitivolingüística: Descriure, Definir, Explicar, Justificar, Argumentar, Demostrar), quan la consigna demana verbalitzar o raonar discursivament. Exemples: "compara i contrasta les dues guerres" → Explicar/Argumentar; "argumenta per què" → Argumentar/Justificar; "demostra que..." → Demostrar.
- una **operació procedimental** (calcular, resoldre, ordenar, classificar, mesurar, encerclar...), que NO és una HCL lingüística però sí l'operació cognitiva nuclear de l'enunciat. Exemples: "calcula el màxim comú múltiple", "resol els exercicis de probabilitat", "ordena de menor a major".
Sovint es combinen ("calcula **i justifica** el resultat" = operació procedimental + HCL). Tant si l'operació és una HCL com si és procedimental, és INTOCABLE: ATNE adapta la forma lingüística de la consigna, mai l'operació que demana.
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
- vs `write-instruccions`: les instruccions donen **passos per executar** alguna cosa (recepta, manual de muntatge); l'enunciat planteja **un repte per resoldre** que demana una operació cognitiva específica.
- vs `write-informe`: l'informe **presenta resultats** ja elaborats; l'activitat **demana que l'alumne els elabori**.
- vs `write-manual`: el manual **explica conceptes**; l'activitat **aplica conceptes** en una situació concreta.

**Estructura típica del document d'activitat:**
1. Títol/nom de l'activitat
2. Context o situació d'aprenentatge (Macro Explicativa)
3. Dades, textos font, materials (variables — intocables)
4. Consigna(es) — 1 o més (Macro Instructiva): "A partir de X, fes Y"
5. Rúbrica/criteris (opcional, B1+)

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Títol i nom de l'activitat**
- Orientació: Títol-etiqueta (1-3 paraules) + icona de l'acció. La consigna la llegeix oralment l'adult.

**2. Context introductori**
- Bastida del marc: Absent o 1 oració mínima (SVO, present). Mediació oral de l'adult. Visual obligatori si hi ha dades.

**3. Dades, textos font i materials**
- Invariant de contingut: Dades invariants. Imatge o esquema visual obligatori per a cada dada. Etiquetes mínimes.

**4. Consigna(es)**
- Nucli de la tasca (INVARIANT de contingut): 1 consigna: verb d'1 sílaba + objecte mínim ("Dibuixa X", "Encercla X"). Icona del verb. Mediació oral obligatòria.

**5. Bastida lingüística (forma)**
- Superfície del text: Etiquetes i paraules clau isolades. 0-1 frases per bloc. Mediació oral de l'adult.

**6. Indicadors de resposta**
- Andamiatge del format: "Respon aquí: ___" amb espai grafiat o gràfic. L'adult inicia la resposta oralment.

**7. Rúbrica o criteris**
- Metacognició avaluadora: Absent. L'adult dona feedback oral immediat.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral, amb l'adult, mediada en L1 si cal) "He entès què havia de fer?" — l'adult acompanya l'alumne a valorar si ha comprès la consigna, no només si ha omplert l'espai.

### A1 — Inicial


**1. Títol i nom de l'activitat**
- Orientació: Títol curt (3-5 paraules) + icona o imatge de referència.

**2. Context introductori**
- Bastida del marc: 1-2 frases molt simples (SVO, vocabulari nuclear). Context ancorat en imatge o esquema.

**3. Dades, textos font i materials**
- Invariant de contingut: Dades invariants. Representació visual de suport. Vocabulari de les etiquetes al mínim necessari.

**4. Consigna(es)**
- Nucli de la tasca (INVARIANT de contingut): 1 consigna: verb + objecte clar (3-5 paraules). Icona del verb obligatòria. 0-1 subconsigna.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases de 3-5 paraules. Vocabulari nuclear. 1 idea per frase. Senyaladors visuals màxims.

**6. Indicadors de resposta**
- Andamiatge del format: "Escriu aquí:" + espai. Opció de dibuix o marca si la consigna ho permet.

**7. Rúbrica o criteris**
- Metacognició avaluadora: Absent o 1-2 criteris en forma d'icona ("he dibuixat?", "he escrit el nom?").

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral o escrit mínim) "He entès el que havia de fer? He fet el que deia la pregunta?"

### A2 — Funcional


**1. Títol i nom de l'activitat**
- Orientació: Títol clar + breu descripció de la tasca en 1 frase.

**2. Context introductori**
- Bastida del marc: 2-3 frases simples. Connectors bàsics ("i", "però", "perquè"). Context comprensible de manera autònoma.

**3. Dades, textos font i materials**
- Invariant de contingut: Dades invariants. Taula o gràfic si existia al original. Petita llegenda si cal.

**4. Consigna(es)**
- Nucli de la tasca (INVARIANT de contingut): 1-2 consignes curtes. Verb de la consigna en **negreta**. Numeració explícita si n'hi ha més d'una.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases simples (8-12 paraules). Connectors bàsics. Sagnat i separació entre context i consigna.

**6. Indicadors de resposta**
- Andamiatge del format: "Escriu 1-2 frases." o "Marca amb X." Format de resposta explícit.

**7. Rúbrica o criteris**
- Metacognició avaluadora: 1-2 criteris simples en forma de llista ("He respost la pregunta? Sí / No").

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He respost el que se'm demanava." Autocomprovació senzilla de la correspondència consigna-resposta.

### B1 — Estratègic


**1. Títol i nom de l'activitat**
- Orientació: Títol informatiu + indicació de la HCL ("Expliqueu per què...").

**2. Context introductori**
- Bastida del marc: 1-2 frases amb connector causal o temporal. Context que dona el marc suficient per a la consigna.

**3. Dades, textos font i materials**
- Invariant de contingut: Dades invariants. Taula o gràfic etiquetat amb frase explicativa breu.

**4. Consigna(es)**
- Nucli de la tasca (INVARIANT de contingut): Consigna completa amb connector causal o condicional ("A partir de X, explica per què Y"). Subconsignes numerades.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases amb connectors causals i condicionals. Separació visual clara entre parts. Registre funcional-acadèmic emergent.

**6. Indicadors de resposta**
- Andamiatge del format: "Respon en 2-3 frases. Usa 'per tant' o 'perquè'." Connector guia explícit.

**7. Rúbrica o criteris**
- Metacognició avaluadora: Criteris breus (2-3) derivats de la HCL ("He explicat per què? He usat evidències?").

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva resposta respon la consigna? He usat la HCL correcta (explicar, justificar...)?"

### B2 — Acadèmic


**1. Títol i nom de l'activitat**
- Orientació: Títol precís que anticipa l'operació i el context.

**2. Context introductori**
- Bastida del marc: Paràgraf concís (3-5 frases) amb vocabulari acadèmic. Context que emmarca el problema amb precisió.

**3. Dades, textos font i materials**
- Invariant de contingut: Dades invariants. Tots els elements del text font presents. Descripció objectiva si hi ha gràfics.

**4. Consigna(es)**
- Nucli de la tasca (INVARIANT de contingut): Múltiples subconsignes jerarquitzades. Format visual que marca la jerarquia (numeració i sagnat).

**5. Bastida lingüística (forma)**
- Superfície del text: Veu impersonal consistent. Vocabulari acadèmic. Estructura visual clara però sense senyaladors excessius.

**6. Indicadors de resposta**
- Andamiatge del format: Format de resposta implícit en la consigna. Estructura esperada derivada de la HCL.

**7. Rúbrica o criteris**
- Metacognició avaluadora: Rúbrica amb criteris i nivells. Formulació acadèmica. Autoavaluació guiada.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He completat totes les subconsignes i he usat el vocabulari acadèmic adequat."

### C1+ — Crític


**1. Títol i nom de l'activitat**
- Orientació: Títol acadèmic amb formulació que inclou el repte i el marc disciplinari.

**2. Context introductori**
- Bastida del marc: Context ric amb vocabulari disciplinari, connexions conceptuals i marc del problema ben delimitat.

**3. Dades, textos font i materials**
- Invariant de contingut: Dades invariants. Text font complet. Anàlisi de la relació entre les dades si la consigna ho demana.

**4. Consigna(es)**
- Nucli de la tasca (INVARIANT de contingut): Consigna acadèmica amb múltiples operacions cognitives encadenades. Formulació precisa i densa.

**5. Bastida lingüística (forma)**
- Superfície del text: Registre acadèmic ple. Precisió i densitat del llenguatge acadèmic. Sense bastides visuals addicionals.

**6. Indicadors de resposta**
- Andamiatge del format: Cap indicador de format. L'alumne domina el format de resposta acadèmica.

**7. Rúbrica o criteris**
- Metacognició avaluadora: Rúbrica analítica completa. L'alumne pot autoavaluar i argumentar la seva nota.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva resposta és rigorosa: respon exactament el que es demana, amb evidències i sense divagació."

