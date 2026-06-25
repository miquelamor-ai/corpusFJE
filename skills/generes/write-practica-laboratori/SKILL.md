---
name: write-practica-laboratori
description: 'Instrument per adaptar o generar una pràctica de laboratori escolar:
  document de treball del procés experimental que exigeix la cadena hipòtesi→mètode→dades→justificació.
  HCL principal Justificar (interpretar fenòmens connectant fets amb la teoria científica
  de referència); HCL secundàries Explicar (causa-efecte), Descriure (resultats, A2)
  i Argumentar (discussió d''errors, B2+). Invariant disciplinari: dades experimentals,
  unitats, hipòtesi i cadena lògica hipòtesi→procediment→resultats→conclusió no es
  modifiquen; es modula la bastida lingüística de cada bloc per MECR. Rúbrica gradada
  8 passos × 6 nivells MECR (pre-A1→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 1.0.0
tools_required: []
agent_role: adapter
genre_key: practica_laboratori
triggers:
- path: params.genere_discursiu
  equals: practica_laboratori
macro_tipologia: explicativa
label_ca: Pràctica de laboratori
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
font_canonic: M3_genere-escriure-practica-laboratori.md
font_version: 1.0.0
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 14460d06ebfdfc63
---

# Escriure/adaptar una pràctica de laboratori — skill operativa per a LLM

La pràctica de laboratori escolar és el **document de treball del procés experimental**: el registre intern d'una investigació controlada que l'alumne ha dissenyat o dut a terme al laboratori. El seu tret definitori és que **la cadena hipòtesi → procediment → resultats → conclusió és l'estructura invariant**: sense ella, no és una pràctica de laboratori, és un informe descriptiu genèric. A diferència del pòster científic (síntesi visual per comunicar a una audiència) i de l'informe genèric (pot ser merament expositiu), la pràctica de laboratori **exigeix l'HCL Justificar**: no n'hi ha prou amb dir **què** ha passat, cal interpretar els fenòmens connectant els fets observats amb la teoria científica de referència.

**Tipologia MALL (macro)**: Explicativa (amb HCL dominant Justificar). El gènere pertany a la macro-tipologia **Explicativa** del M3 (vegeu `macro_tipologia: explicativa` al frontmatter); la dimensió justificativa és la que el distingeix d'altres gèneres científics escolars. La dimensió argumentativa (discussió d'errors, B2+) és secundària.
**HCL principal**: Justificar — interpretar els fenòmens experimentals connectant els fets de la realitat amb el contingut de la teoria científica de referència (Izquierdo i Sanmartí, 1996).
**HCL secundàries**: Explicar (relació causa-efecte en el procediment i els resultats), Descriure (dades i representació, especialment a A2), Argumentar (discussió d'errors i limitacions metodològiques, B2+).
**S'adapta a tots els nivells (pre-A1→C1)**: la pràctica de laboratori és accessible a pre-A1/A1 si el format es redueix a esquema + etiquetes + taula de dades amb mediació oral del docent. L'operació cognitiva (predic → comprovo → concloig) es manté a tots els nivells: a pre-A1, la hipòtesi la pot formular oralment l'adult i l'alumne la valida amb un gest o una imatge. El MECR modula la **superfície lingüística**, **no el sostre cognitiu**.

**Diferència clau amb `write-informe`.**
L'informe és un gènere genèric que pot ser merament expositiu (descriure dades sense connectar-les amb la teoria). La pràctica de laboratori **exigeix Justificar**: la secció d'anàlisi i discussió (Pas 6) és constitutiva del gènere. Sense ella — sense la connexió explícita entre les dades obtingudes i la teoria científica de referència — el document és un registre de dades, no una pràctica de laboratori.

**Diferència clau amb `write-poster-cientific`.**
El pòster és el producte final de comunicació pública (síntesi visual exposable). La pràctica de laboratori és el document de treball del procés experimental (informe intern). El pòster es llegeix de lluny, en blocs breus i jerarquia visual; la pràctica de laboratori és text continu, seccional, amb seccions que s'encadenen lògicament.

**Diferència clau amb el diari de camp.**
El diari de camp recull observació naturalística, in situ, provisional; el camp és l'entorn. La pràctica de laboratori registra un experiment controlat, en laboratori, amb hipòtesi prèvia i variables controlades. La distinció observació vs. experiment és nuclear al MALL de ciències.

**Connexions MALL transversals:**
- *La hipòtesi com a objecte científic intocable*: la hipòtesi és la predicció que l'alumne fa ABANS de l'experiment. No es "corregeix" a posteriori. Si els resultats la refuten, la conclusió ho diu explícitament — i aquest és el moment epistèmic més valuós. Tocar la hipòtesi a posteriori destrueix l'operació cognitiva del gènere.
- *Les dades experimentals com a objecte inviolable*: els valors mesurats, les unitats i les condicions de l'experiment no s'arrodoneixen, no s'aproximen, no es "milloren" per fer-los coincidir amb la hipòtesi (vegeu §Invariant disciplinari).
- *La justificació com a operació epistèmica nuclear*: escriure la pràctica de laboratori força l'alumne a entendre per a què li servia fer la investigació. El 60% de l'alumnat de 2n d'ESO afirma que els connectors de la bastida els han ajudat a entendre "què volíem obtenir i per a què servia fer-ho" (Domènech, 2014, p. 249). L'escriptura no és el registre de l'experiment: és la condició per comprendre'l.
- *Multimodalitat com a competència científica*: taules de dades, gràfics i esquemes de muntatge no són decoració; són la representació formal dels resultats (mode visual) que la justificació escrita (mode verbal) ha de connectar amb la teoria.
- *Pont L1 per capes (escrit i oral)*: per a nouvinguts, l'L1 pot entrar a la capa adaptable (glosses del terme tècnic). Les dades experimentals (valors + unitats) i la hipòtesi no es tradueixen: pertanyen a l'invariant disciplinari.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **pràctica de laboratori adaptada per a la LECTURA** de l'alumne (el model que llegeix/interpreta), no la producció autònoma de l'alumne — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast cognitiu, amb la forma lingüística ajustada al seu nivell.
**Sub-granularitat dins de pre-A1/A1**: es treballa amb `fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]`; a fase logogràfica el text es redueix a etiquetes mínimes i esquema de muntatge, amb mediació oral de l'adult.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Títol i hipòtesi**
- Orientació i predicció: Títol-etiqueta (1-3 paraules). La hipòtesi la formula oralment l'adult; l'alumne la valida amb un gest o una imatge ("Sí/No").

**2. Material i muntatge**
- Identificació dels elements: Imatge o dibuix del muntatge amb etiquetes mínimes. L'adult llegeix la llista de materials.

**3. Procediment**
- Passos de la investigació: Adult guia oralment. L'alumne segueix el muntatge visual. Cap text de procediment.

**4. Resultats i dades**
- Registre de les observacions: Taula de dades simple preomplerta amb 1-2 valors nuclears (valor + unitat intactes). L'adult llegeix la taula. Imatge del resultat visible.

**5. Invariant disciplinari**
- Inviolabilitat de l'objecte: Dades, unitats, símbols, termes tècnics i hipòtesi original INTACTES. El text mínim els envolta.

**6. Anàlisi i discussió**
- HCL Justificar (el cor del gènere): Vincle causal mínim mediat oralment per l'adult: "[El resultat] passa perquè [terme tècnic]." L'adult verbalitza la connexió dada–teoria; l'alumne confirma. Per a alumnes amb CALP en L1, la connexió pot ser més rica via oralitat/L1.

**7. Conclusions**
- Tancament de la cadena: Conclusió oral mediada per l'adult: "La nostra predicció era [X]. Hem obtingut [Y]. [Confirmada/No confirmada]." Etiqueta visual.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés experimental: (oral, amb l'adult, mediada en L1 si cal) "La meva predicció i el resultat, coincideixen?" — l'adult acompanya l'alumne a valorar si allò que havia predit s'ha complert, sense corregir la hipòtesi original.

### A1 — Inicial


**1. Títol i hipòtesi**
- Orientació i predicció: Títol curt (3-5 paraules). Hipòtesi en 1 frase molt simple: "Crec que [el/la X] [fa/és]..." amb vocabulari nuclear.

**2. Material i muntatge**
- Identificació dels elements: Llista de materials (nom + icona si cal). Dibuix del muntatge etiquetat amb els noms dels elements.

**3. Procediment**
- Passos de la investigació: 2-3 passos en frases molt simples ("Primer... Després... Final..."). Imatge de cada pas clau.

**4. Resultats i dades**
- Registre de les observacions: Taula de dades amb valors mesurats (valor + unitat sempre). 1 frase que diu "He obtingut [X unitat]."

**5. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Els termes tècnics poden portar un pictograma de suport. La hipòtesi oral de l'adult es manté sense corregir.

**6. Anàlisi i discussió**
- HCL Justificar (el cor del gènere): 1 frase de justificació simple ancorada a la dada: "[X] ha passat perquè [raó nuclear]." Connector causal "perquè" obligatori.

**7. Conclusions**
- Tancament de la cadena: 1 frase que respon la hipòtesi: "La nostra hipòtesi [és certa / no és certa] perquè hem obtingut [X]."

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés experimental: (oral o escrit mínim) "La meva hipòtesi i el que he obtingut, coincideixen? Per què?"

### A2 — Funcional


**1. Títol i hipòtesi**
- Orientació i predicció: Títol + hipòtesi en 1 frase clara: "Crec que si [condició], llavors [resultat], perquè [raó breu]."

**2. Material i muntatge**
- Identificació dels elements: Llista de materials. Esquema del muntatge etiquetat. 1-2 frases del procediment principal.

**3. Procediment**
- Passos de la investigació: 3-5 passos numerats en frases simples (8-12 paraules). Connectors bàsics de seqüència ("primer", "a continuació", "finalment").

**4. Resultats i dades**
- Registre de les observacions: Taula de dades completa. Gràfic simple si escau. 1-2 frases que descriuen el resultat principal ("La temperatura ha pujat fins a [X °C].").

**5. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Els termes tècnics poden portar definició integrada molt breu. La hipòtesi escrita no es modifica.

**6. Anàlisi i discussió**
- HCL Justificar (el cor del gènere): 1-2 frases de justificació amb connector causal. Connexió directa resultat → explicació: "Els resultats mostren [X] perquè [principi científic simple]."

**7. Conclusions**
- Tancament de la cadena: 1-2 conclusions que responen la hipòtesi amb la dada: "La hipòtesi ha estat [confirmada/refutada] perquè [resultat + dada]."

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés experimental: "He explicat per què els meus resultats confirmen o refuten la hipòtesi."

### B1 — Estratègic


**1. Títol i hipòtesi**
- Orientació i predicció: Títol informatiu + hipòtesi amb relació entre variables: "Si augmento [variable independent], espero que [variable dependent] augmenti perquè [marc teòric breu]."

**2. Material i muntatge**
- Identificació dels elements: Materials llistats + esquema del muntatge. Procediment en 3-5 passos numerats. Identificació de la variable que es canvia.

**3. Procediment**
- Passos de la investigació: 5-7 passos numerats. Connectors de seqüència i frases amb veu activa. Inclusió de les condicions de control.

**4. Resultats i dades**
- Registre de les observacions: Taula + gràfic adequat al tipus de dada. 2-3 frases que descriuen la tendència ("A mesura que [X] augmenta, [Y] disminueix.").

**5. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Definicions integrades on calgui. La hipòtesi és la referència explícita de la conclusió.

**6. Anàlisi i discussió**
- HCL Justificar (el cor del gènere): 2-3 frases de justificació amb connexió explícita dada–teoria: "El valor de [X unitat] confirma que [principi científic], ja que [dada suport]." Veu impersonal emergent.

**7. Conclusions**
- Tancament de la cadena: 2-3 conclusions que responen la hipòtesi justificant amb les dades. 1 implicació o aplicació del resultat. Connexió explícita amb la teoria.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés experimental: "La meva justificació connecta les dades amb la teoria. He explicat les diferències si n'hi ha."

### B2 — Acadèmic


**1. Títol i hipòtesi**
- Orientació i predicció: Títol precís + hipòtesi formulada amb variables nomenades explícitament i fonamentació teòrica breu.

**2. Material i muntatge**
- Identificació dels elements: Materials + esquema. Procediment en passos numerats. Variables independent, dependent i controlades identificades.

**3. Procediment**
- Passos de la investigació: Passos numerats amb justificació breu de les condicions experimentals. Veu impersonal emergent.

**4. Resultats i dades**
- Registre de les observacions: Taula + gràfic. Descripció objectiva de la relació entre variables. Indicació de la unitat de mesura de cada valor.

**5. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Terminologia disciplinària plena. La hipòtesi s'esmenta explícitament a la conclusió ("La nostra hipòtesi ha estat [confirmada/refutada] perquè...").

**6. Anàlisi i discussió**
- HCL Justificar (el cor del gènere): Paràgraf d'anàlisi: justificació de cada resultat clau connectant amb la teoria de referència. Discussió si els resultats s'aparten de l'esperable. Connectors acadèmics ("per tant", "en conseqüència", "tot i que").

**7. Conclusions**
- Tancament de la cadena: Conclusions argumentades amb la hipòtesi com a referència. Discussió si hi ha discrepàncies entre els resultats i l'esperable. 1 implicació o aplicació real.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés experimental: "He justificat cada resultat clau amb la teoria i he discutit les diferències amb el valor esperat."

### C1+ — Crític


**1. Títol i hipòtesi**
- Orientació i predicció: Títol acadèmic + hipòtesi rigorosa amb relació de causalitat explícita, variables i marc teòric de referència citat.

**2. Material i muntatge**
- Identificació dels elements: Materials + esquema. Procediment detallat. Variables identificades i justificació breu del disseny experimental.

**3. Procediment**
- Passos de la investigació: Procediment detallat en veu impersonal. Justificació del control de variables. Pot incloure referències a protocols estàndard.

**4. Resultats i dades**
- Registre de les observacions: Taula + gràfic rigorosos. Descripció analítica de la relació, identificació de valors atípics i valoració de la repetibilitat.

**5. Invariant disciplinari**
- Inviolabilitat de l'objecte: Idem. Rigor terminològic i simbòlic complet. La hipòtesi és el fil conductor de tot el document.

**6. Anàlisi i discussió**
- HCL Justificar (el cor del gènere): Anàlisi rigorosa: connexió explícita dada–teoria amb citació de referència. Discussió de les fonts d'error experimental (error instrumental, error humà, condicions no controlades). Contrastació del resultat obtingut amb el valor teòric o experimental esperat.

**7. Conclusions**
- Tancament de la cadena: Conclusions rigoroses: resposta a la hipòtesi justificada per les dades, reconeixement dels límits de l'experiment (mostra, repeticions, condicions), obertura a noves preguntes de recerca.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés experimental: "L'experiment és rigorós: dades intactes, hipòtesi revisada honestament, fonts d'error reconegudes, conclusions justificades amb la teoria."

