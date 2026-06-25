---
name: write-diari-camp
description: 'Instrument per adaptar o generar un diari de camp: registre sistemàtic
  d''observacions empíriques amb data, lloc, metodologia i dades, per a treball de
  camp científic, antropològic o naturalístic. HCL Descriure + Narrar. HCL secundàries:
  Interpretar/Valorar (B1+), Justificar (B2+). Invariant disciplinari: el registre
  fidel de l''observació (data, lloc, condicions, allò vist/mesurat) és inviolable;
  el que es modula per MECR és la forma lingüística del registre. Les interpretacions
  s''etiqueten sempre com a tals. Rúbrica gradada 8 passos × 6 nivells MECR (pre-A1→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 1.1.0
tools_required: []
agent_role: adapter
genre_key: diari_camp
triggers:
- path: params.genere_discursiu
  equals: diari_camp
macro_tipologia: descriptiva
label_ca: Diari de camp
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
font_canonic: M3_genere-escriure-diari-camp.md
font_version: 1.1.0
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 1506ac44089babf3
---

# Escriure/adaptar un diari de camp — skill operativa per a LLM

El diari de camp és el **registre sistemàtic i fidel d'observacions empíriques** realitzades in situ: en un entorn natural, social o de laboratori. El seu tret definitori és que **l'observació és l'objecte epistèmic central**: allò que l'observador ha vist, mesurat, comptat o descrit en un moment i lloc determinats. A diferència del diari personal (narrativa reflexiva en esfera privada), el diari de camp pertany a l'**esfera científica i empírica**: és un document de treball provisional, intern, en construcció, on es registra la realitat tal com es presenta, no com es narra ni com es valora. Tret distintiu fonamental: les **interpretacions s'etiqueten sempre com a tals** i es separen de l'observació bruta — no es barregen.

**Tipologia MALL (macro)**: Descriptiva (dominant) + Narrativa (secundària). El gènere pertany a la macro-tipologia **Descriptiva** del M3 (objecte o fenomen en l'espai i el temps); la dimensió narrativa és secundària i sosté la seqüència temporal de les observacions (primer vaig veure X, després Y), sense ser el focus central.
**HCL principal**: Descriure — representar amb precisió allò observat (forma, mida, comportament, dada).
**HCL secundàries**: Narrar — seqüenciar les observacions en el temps (A2+); Interpretar/Valorar — donar sentit a allò observat en relació a un model o hipòtesi (B1+); Justificar — vincular l'observació a marc teòric o disciplinari (B2+).
**S'adapta a tots els nivells (pre-A1→C1)**: el diari de camp és **multimodal per naturalesa** (croquis, esquemes, mapes, fotografies, taules de dades), i això el fa accessible a tots els nivells lingüístics. A pre-A1 logogràfic, l'observació científica (mirar, comptar, mesurar) és plenament accessible; el que es gradua per MECR és la **forma escrita del registre**, mai la capacitat d'observar.

**Distinció canònica amb el diari personal.** Diari personal: macro-tipologia narrativa/reflexiva, esfera privada, primera persona emocional, no requereix data de camp ni condicions d'observació. Diari de camp: macro-tipologia descriptiva/observacional, esfera científica/empírica, registre objectiu, capçalera d'observació obligatòria (data, lloc, hora, condicions), observacions i interpretacions separades. Són gèneres autònoms: el diari de camp **no** és una variant del diari personal.

**Connexions MALL transversals:**
- *L'observació com a objecte inviolable*: allò que s'ha vist, mesurat o recollit no es pot "millorar", inferir retroactivament ni barrejar amb la interpretació. El registre d'observació és el que distingeix el diari de camp de l'assaig o l'informe elaborat.
- *Multimodalitat com a competència científica, no decoració*: el croquis, l'esquema d'observació, la taula de dades i la fotografia anotada no són afegits visuals — són formes nadives del registre de camp. Un diari de camp sense cap suport multimodal és inusualment atípic del gènere.
- *Procés vs. producte*: el diari de camp és un **document de procés** (in situ, provisional, evolutiu); el pòster científic és un **producte** (síntesi final, comunicació pública). Aquesta diferència estructural explica per què el diari admet imprecisions provisionals marcades com a tals, mentre que el pòster exigeix dades definitives. La modulació per MECR del diari afecta la forma del registre; la provisionalitat és constitutiva del gènere a tots els nivells.
- *Pont L1 per capes (escrit i oral)*: per a l'alumnat nouvingut, el canal no-lingüístic del diari (croquis, esquemes, mapes) permet accedir al contingut i contribuir a l'observació de camp abans que la llengua vehicular estigui consolidada. L'L1 pot entrar com a pont (glossa del terme d'observació) per a alumnes alfabetitzats en L1, sense substituir el registre en català.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **diari de camp adaptat per a la LECTURA** de l'alumne (el model que llegeix/interpreta i en aprèn l'estructura), no la producció autònoma. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast cognitiu, amb la forma lingüística ajustada al seu nivell.
**Sub-granularitat dins de pre-A1/A1**: es treballa amb `fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]`; a fase logogràfica el registre es redueix a croquis + etiquetes mínimes + capçalera numèrica, amb mediació oral de l'adult.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Capçalera d'observació**
- Contextualització: Pictograma de data (número del dia) + nom del lloc en 1 paraula + icona del temps meteorològic. L'adult completa la capçalera i la llegeix en veu alta.

**2. Objectiu de l'observació**
- Orientació: L'adult formula l'objectiu oralment. L'alumne pot assenyalar o dibuixar "què busquem".

**3. Observació sistemàtica**
- Registre fidel: Croquis de l'element observat + etiqueta d'1 paraula (nombre o nom). Mediació oral de l'adult ("Quants en veus?"). La dada (número, mesura) es manté intacta.

**4. Invariant del registre**
- Inviolabilitat de l'observació: Allò vist és allò vist. L'adult no omple el que l'alumne no ha observat. Croquis = document de camp.

**5. Bastida lingüística (forma)**
- Superfície del text: Etiquetes i números. Mediació oral de l'adult. 0 o 1 paraula per element observat.

**6. Interpretació / hipòtesi (etiquetada)**
- Salt inferencial explicit: No s'escriu. L'adult formula oralment la pregunta "Per què creus que...?" L'alumne respon oralment.

**7. Preguntes obertes / properes observacions**
- Projecció científica: L'adult formula oralment "Què vols veure la propera vegada?" L'alumne pot dibuixar-ho.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral, amb l'adult, mediada en L1 si cal) "El dibuix mostra el que has vist de veritat?" — l'adult acompanya l'alumne a valorar si el croquis és fidel a l'observació, no si és bonic. L'accent és la fidelitat al registre, no l'estètica.

### A1 — Inicial


**1. Capçalera d'observació**
- Contextualització: Data (dia/mes) + lloc en 1-2 paraules + 1 condició ambiental breu ("Sol", "Pluja").

**2. Objectiu de l'observació**
- Orientació: 1 frase molt simple ("Busquem ocells"). L'adult pot dictar.

**3. Observació sistemàtica**
- Registre fidel: Croquis + etiqueta (nom + número). "He vist [N] [element]." 1 observació per bloc.

**4. Invariant del registre**
- Inviolabilitat de l'observació: El nombre i el nom de l'element observat es mantenen exactes. L'adult no "corregeix" allò no observat.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases de 3-5 paraules. Verbs d'observació bàsics ("veig", "hi ha", "compto"). 1 idea per línia.

**6. Interpretació / hipòtesi (etiquetada)**
- Salt inferencial explicit: Oral o dibuix breu. L'adult escriu la idea de l'alumne amb l'etiqueta `[Idea:]`.

**7. Preguntes obertes / properes observacions**
- Projecció científica: 1 pregunta oral o en 1-3 paraules ("Vull veure [element]").

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral o escrit mínim) "El que he dibuixat/escrit és el que he vist de veritat?"

### A2 — Funcional


**1. Capçalera d'observació**
- Contextualització: Data completa + lloc + hora + 1-2 condicions ambientals en frase breu ("Fa sol i 20 °C").

**2. Objectiu de l'observació**
- Orientació: Objectiu en 1 frase clara ("Observem quines plantes creixen vora l'estany").

**3. Observació sistemàtica**
- Registre fidel: 2-3 observacions amb nom, número o mesura. Frases simples. Ús de "He vist", "He comptat", "He mesurat".

**4. Invariant del registre**
- Inviolabilitat de l'observació: Idem. Les observacions s'escriuen tal com s'han produït, no com "haurien" de ser.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases simples (8-12 paraules). Connectors temporals ("primer", "després"). Verbs de registre ("he observat", "he mesurat").

**6. Interpretació / hipòtesi (etiquetada)**
- Salt inferencial explicit: 1 frase d'interpretació, clarament separada i marcada `[Crec que:]`. Connector "potser".

**7. Preguntes obertes / properes observacions**
- Projecció científica: 1 pregunta breu ("La propera vegada miraré...").

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit el que he vist, no el que creia que hauria de veure."

### B1 — Estratègic


**1. Capçalera d'observació**
- Contextualització: Capçalera completa: data, lloc, hora, condicions meteorològiques/ambientals, observador. Frase per element.

**2. Objectiu de l'observació**
- Orientació: Objectiu d'observació explícit, pot incloure hipòtesi inicial.

**3. Observació sistemàtica**
- Registre fidel: Observació seqüenciada: hora/ordre + allò observat + dada. Inici de veu impersonal ("S'observa").

**4. Invariant del registre**
- Inviolabilitat de l'observació: Idem. Distinció explícita entre "he vist" (observació) i "crec que" (interpretació).

**5. Bastida lingüística (forma)**
- Superfície del text: Frases amb connectors temporals i causals. Veu impersonal emergent ("s'observa", "es registra").

**6. Interpretació / hipòtesi (etiquetada)**
- Salt inferencial explicit: Interpretació explícita i etiquetada (`[Interpretació:]`): "Potser X perquè he observat Y." Vincula observació i hipòtesi.

**7. Preguntes obertes / properes observacions**
- Projecció científica: 1-2 preguntes que deriven de les observacions d'avui. Connexió explícita.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva interpretació surt de les observacions que he registrat, no d'allò que esperava trobar."

### B2 — Acadèmic


**1. Capçalera d'observació**
- Contextualització: Capçalera completa amb precisió: coordenades del lloc si aplica, metodologia d'observació declarada en 1 frase.

**2. Objectiu de l'observació**
- Orientació: Objectiu formulat com a pregunta d'investigació + hipòtesi prèvia.

**3. Observació sistemàtica**
- Registre fidel: Registre sistemàtic amb variables declarades (hora, localització dins el transsecte, condicions locals). Veu impersonal consistent.

**4. Invariant del registre**
- Inviolabilitat de l'observació: Idem. Metodologia d'observació declarada i seguida; qualsevol desviació es registra.

**5. Bastida lingüística (forma)**
- Superfície del text: Veu impersonal consistent. Vocabulari tècnic d'observació (CALP). Precisió en la descripció.

**6. Interpretació / hipòtesi (etiquetada)**
- Salt inferencial explicit: Bloc `[Interpretació:]` amb argumentació: observació → hipòtesi → vinculació amb model de referència.

**7. Preguntes obertes / properes observacions**
- Projecció científica: 2-3 preguntes obertes formulades com a preguntes d'investigació. Suggeriment de propera observació.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He mantingut la separació observació–interpretació. Les meves dades són traçables."

### C1+ — Crític


**1. Capçalera d'observació**
- Contextualització: Capçalera de protocol científic: data, localització precisa, condicions ambientals amb mesures, observadors, protocol de mostratge.

**2. Objectiu de l'observació**
- Orientació: Objectiu amb marc teòric de referència: la pregunta d'investigació es situa en relació a models o estudis previs.

**3. Observació sistemàtica**
- Registre fidel: Registre de protocol: variables múltiples, mètode de mostratge explícit, referència al protocol declarat a la capçalera.

**4. Invariant del registre**
- Inviolabilitat de l'observació: Idem. Rigor metodològic complet: l'observació és traçable, reproductible en condicions similars, i els límits de l'observació es reconeixen.

**5. Bastida lingüística (forma)**
- Superfície del text: Registre acadèmic de camp ple. Terminologia disciplinària específica. Precisió i economia del llenguatge científic.

**6. Interpretació / hipòtesi (etiquetada)**
- Salt inferencial explicit: Discussió crítica de la interpretació: observació → hipòtesi → model de referència → límits de la inferència. Reconeixement del salt lògic.

**7. Preguntes obertes / properes observacions**
- Projecció científica: Propostes de millora del protocol + preguntes d'investigació derivades + connexió amb literatura o models teòrics.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu registre és fidel, la meva interpretació és explícita i els límits de la inferència estan reconeguts."

