---
name: write-poster-cientific
description: 'Instrument per adaptar o generar un pòster científic escolar: síntesi
  visual-verbal d''una indagació o tema científic on dada i representació visual van
  lligades. HCL Explicar + Argumentar. Invariant disciplinari: dades, unitats, magnituds,
  símbols i termes tècnics no es verbalitzen fora ni es deformen; es modula només
  la bastida lingüística al voltant. Rúbrica gradada 8 passos × 6 nivells MECR (pre-A1→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 4.2.0-canonic
tools_required: []
agent_role: adapter
genre_key: poster_cientific
triggers:
- path: params.genere_discursiu
  equals: poster_cientific
macro_tipologia: explicativa
label_ca: Pòster científic
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
font_canonic: M3_genere-escriure-poster-cientific.md
font_version: 4.2.0-canonic
generat_at: '2026-06-28'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: b3a0e9e9d77b8ab9
---

# Escriure/adaptar un pòster científic — skill operativa per a LLM

El pòster científic escolar és la **síntesi visual-verbal** d'una indagació o d'un tema científic, pensada per ser exposada i comunicada a una audiència (companys, comunitat educativa). El seu tret definitori és que **la dada i la seva representació visual van lligades**: cap dada quantitativa no viu sola en prosa, i cap gràfic no viu sense la dada que el sustenta. A diferència de l'informe (text continu amb separació dades/conclusions), el pòster és **modular i espacial**: blocs breus, jerarquia visual, lectura no-lineal guiada per títols i imatges.

**Tipologia MALL (macro)**: Explicativa (amb HCL secundària argumentativa). El gènere pertany a la macro-tipologia **Explicativa** del M3 (vegeu `macro_tipologia: explicativa` al frontmatter); la dimensió argumentativa és secundària, no defineix una segona macro.
**HCL principal**: Explicar — fer comprensible la relació entre la pregunta, les dades i la conclusió.
**HCL secundària**: Argumentar — sostenir la conclusió amb les dades presentades (la conclusió no és una opinió: deriva de l'evidència visual-numèrica).
**S'adapta a tots els nivells (pre-A1→C1)**: el pòster és **multimodal per naturalesa**, i això el fa accessible a tots els nivells lingüístics. El MECR modula la **superfície lingüística** del text que envolta les dades, **no el sostre cognitiu** de l'alumne (vegeu §Principi general). Un alumne pre-A1 en català pot tenir CALP consolidat en L1: el pòster li dona canals d'accés no-lingüístics (imatge, gràfic, símbol) que fan viable treballar contingut científic real amb forma lingüística mínima.

**Connexions MALL transversals:**
- *La dada com a objecte inviolable*: a ciència, una dada amb la seva unitat (`9,8 m/s²`, `pH 7`, `−273 °C`) és l'objecte epistèmic nuclear. No es "simplifica" ni es verbalitza fora ("uns nou metres per segon cada segon") perquè perdria la precisió que la fa científica. El pòster preserva la dada i modula el text que l'explica.
- *Multimodalitat com a competència científica, no decoració*: llegir un gràfic, interpretar una taula o un esquema és part nuclear de la competència científica (no un afegit visual). El pòster és el gènere que millor operacionalitza la representació múltiple del DUA.
- *Síntesi com a operació cognitiva*: el pòster obliga a destil·lar una indagació a l'essencial (pregunta → evidència → conclusió) en un espai limitat. La restricció espacial força la jerarquització del que és important.
- *Pont L1 per capes (escrit i oral) + accés no-lingüístic*: per a l'alumnat nouvingut, el suport visual del pòster és l'andamiatge que permet accedir al contingut acadèmic abans que la llengua vehicular estigui consolidada. A més, l'L1 pot entrar com a **pont** dins l'artefacte (no com a substitut de l'invariant disciplinari): com a **glossa bilingüe** del terme clau —`terme_català (terme_L1)`, amb el terme català sempre present— per a alumnes alfabetitzats en L1, o com a **mediació oral** del docent per a fase logogràfica / no alfabetitzats en L1. La forma es simplifica cap avall; el contingut científic, mai es buida.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **pòster adaptat per a la LECTURA** de l'alumne (el model que llegeix/interpreta), no la producció autònoma de l'alumne — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast cognitiu, amb la forma lingüística ajustada al seu nivell.
**Sub-granularitat dins de pre-A1/A1**: es treballa amb `fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]`; a fase logogràfica el text es redueix a etiquetes mínimes sobre la imatge, amb mediació oral de l'adult.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Títol i pregunta/objectiu**
- Orientació: Títol-etiqueta (1-3 paraules) + imatge. La pregunta la formula oralment l'adult.

**2. Materials i mètode (breu)**
- Síntesi del procediment: Imatge dels materials amb etiquetes mínimes. Sense text de mètode.

**3. Resultats: dades + visual**
- Lligadura dada–visual: Dada nuclear amb la seva imatge/icona. La dada (valor + unitat) es manté intacta; el text és l'etiqueta.

**4. Invariant disciplinari**
- Inviolabilitat de l'objecte: Dades, unitats, símbols i termes tècnics INTACTES. El text mínim els envolta sense deformar-los.

**5. Bastida lingüística (forma)**
- Superfície del text: Etiquetes i paraules clau. Mediació oral de l'adult. Frase 0 o 1 idea per bloc.

**6. Conclusió**
- Tancament argumentatiu: Conclusió ancorada a la dada i la imatge amb el vincle causal preservat ("Flota per la densitat [valor]"), mediada oralment. Per a alumnes amb CALP en L1, admet conclusions més riques via oralitat/L1: el límit és la superfície lingüística, no l'operació cognitiva.

**7. Referències i fonts**
- Rigor i honestedat: No cal (mediació de l'adult).

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral, amb l'adult, mediada en L1 si cal) "El dibuix explica què passa?" — l'adult acompanya l'alumne a valorar si la representació triada (dibuix, icona, taula nuclear) deixa veure el fenomen, no només a constatar que ha dibuixat.

### A1 — Inicial


**1. Títol i pregunta/objectiu**
- Orientació: Títol curt + pregunta de 3-5 paraules ("Què flota?").

**2. Materials i mètode (breu)**
- Síntesi del procediment: Llista visual de materials (paraula + icona). Mètode en 1 frase molt simple.

**3. Resultats: dades + visual**
- Lligadura dada–visual: 2-3 dades amb representació visual simple (barres, símbols). Valor + unitat sempre.

**4. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Els termes tècnics poden portar un pictograma de suport.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases de 3-5 paraules. Vocabulari nuclear. 1 idea per bloc.

**6. Conclusió**
- Tancament argumentatiu: Conclusió simple amb vincle causal lligat a la dada ("El més pesat va al fons perquè la densitat és més alta"). Per a alumnes amb CALP en L1, admet conclusions més riques via oralitat/L1.

**7. Referències i fonts**
- Rigor i honestedat: No cal, o icona de "d'on ve" si és extern.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral o escrit mínim) "El meu dibuix i la dada expliquen què he trobat?"

### A2 — Funcional


**1. Títol i pregunta/objectiu**
- Orientació: Títol + pregunta o objectiu en 1 frase clara.

**2. Materials i mètode (breu)**
- Síntesi del procediment: Materials en llista. Mètode en 1-2 frases simples.

**3. Resultats: dades + visual**
- Lligadura dada–visual: Dades en taula o gràfic simple etiquetat. Frase que diu què mostra.

**4. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Els termes tècnics poden portar definició integrada molt breu.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases simples (8-12 paraules). Connectors bàsics ("perquè", "i").

**6. Conclusió**
- Tancament argumentatiu: 1-2 conclusions derivades de les dades. Connector "per tant".

**7. Referències i fonts**
- Rigor i honestedat: La font de les dades externes s'indica de forma simple.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He explicat què mostren les dades."

### B1 — Estratègic


**1. Títol i pregunta/objectiu**
- Orientació: Títol informatiu + pregunta d'indagació explícita.

**2. Materials i mètode (breu)**
- Síntesi del procediment: Materials + mètode en 2-3 frases. Què s'ha fet i com.

**3. Resultats: dades + visual**
- Lligadura dada–visual: Dades en gràfic/taula. Frase que descriu la tendència ("el valor puja quan...").

**4. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Definicions integrades on calgui.

**5. Bastida lingüística (forma)**
- Superfície del text: Frases amb connectors causals ("per tant", "ja que"). Veu impersonal emergent.

**6. Conclusió**
- Tancament argumentatiu: 2 conclusions justificades explícitament des de la dada (HCL Justificar: "X perquè la dada mostra Y") + 1 implicació.

**7. Referències i fonts**
- Rigor i honestedat: Totes les dades externes porten font atribuïda.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva conclusió surt de les dades del gràfic."

### B2 — Acadèmic


**1. Títol i pregunta/objectiu**
- Orientació: Títol precís + objectiu o hipòtesi formulada.

**2. Materials i mètode (breu)**
- Síntesi del procediment: Mètode concís amb variables identificades.

**3. Resultats: dades + visual**
- Lligadura dada–visual: Dades en gràfic adequat al tipus. Descripció objectiva de la relació.

**4. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Terminologia disciplinària plena.

**5. Bastida lingüística (forma)**
- Superfície del text: Veu impersonal consistent. Vocabulari acadèmic.

**6. Conclusió**
- Tancament argumentatiu: Conclusió argumentada + implicació o aplicació del resultat.

**7. Referències i fonts**
- Rigor i honestedat: Referències en format consistent, diferenciant fonts primàries (dades d'indagació pròpia) de secundàries (marc teòric).

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He mantingut les dades i unitats exactes i he argumentat la conclusió."

### C1+ — Crític


**1. Títol i pregunta/objectiu**
- Orientació: Títol acadèmic + pregunta de recerca i marc del problema.

**2. Materials i mètode (breu)**
- Síntesi del procediment: Mètode amb control de variables i justificació breu del disseny.

**3. Resultats: dades + visual**
- Lligadura dada–visual: Dades en format rigorós. Anàlisi de la relació i de la seva fiabilitat.

**4. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Rigor terminològic i simbòlic complet, sense glosses.

**5. Bastida lingüística (forma)**
- Superfície del text: Registre acadèmic ple. Precisió i economia del llenguatge de pòster.

**6. Conclusió**
- Tancament argumentatiu: Conclusió amb discussió de límits de les dades i obertura a noves preguntes.

**7. Referències i fonts**
- Rigor i honestedat: Rigor bibliogràfic complet: dades pròpies vs secundàries diferenciades amb format acadèmic, indicació de fiabilitat i traçabilitat de cada dada.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El pòster és rigorós: dades intactes, conclusió justificada, límits reconeguts."

