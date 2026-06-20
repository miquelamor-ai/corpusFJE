---
modul: M3
titol: "Escriure/adaptar un manual"
tipus: genere-discursiu
categoria_principal: generes
categories_secundaries: []
descripcio: "Instrument per adaptar o generar un manual: text expositiu organitzat en apartats progressius (simple→complex) amb termes tècnics definits, exemples concrets primer i connectors causals explícits. HCL Explicar + Descriure (conceptes nous). No s'adapta a pre-A1. Rúbrica gradada 7 passos × 5 nivells MECR (A1→C1)."
mecr_range: [A1, A2, B1, B2, C1]
agent_roles: [adapter, generator]
genre_key: manual
macro_tipologia: explicativa
label_ca: "Manual"
translanguaging: false
multimodal: false
moduls_relacionats: [M3]
variables_configurables:
  fase_lectora: [alfabetica_emergent, alfabetica_fluida]
skill_meta: write-manual@corpusFJE/skills/generes/write-manual
review_status: pilot-fusio-6
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, fidelitat-gradada-C2, variabilitat-cardinal-passos-D3]
  aplicades_post_review: []
  comentari_key: "glossari-final-complement-estructural-no-referencia-lateral-pas62-consistent"
---

# Escriure/adaptar un manual

## Descripció

El manual és un text expositiu organitzat en **apartats progressius** que presenta coneixements de manera sistemàtica, de simple a complex. El seu tret definitori és la **progressió epistèmica**: cada apartat es recolza conceptualment en l'anterior, els termes tècnics estan definits a la primera aparició, i els exemples concrets precedeixen sempre les abstraccions.

**Tipologia MALL**: Expositiva/Progressiva.
**HCL principal**: Explicar — exposar un conjunt de conceptes relacionats de manera progressiva i sistemàtica.
**HCL secundàries**: Descriure — definir i caracteritzar termes tècnics nous (A1-B1) · Justificar — explicar per qué els conceptes s'ordenen de la manera que s'ordenen (B1+).
**No s'adapta a pre-A1**: el manual requereix la comprensió de la **progressió simple→complex com a estructura epistèmica** — entendre que els apartats estan en un cert ordre perquè cada un es recolza conceptualment en l'anterior implica la comprensió de la jerarquia i la dependència conceptual entre idees. Aquesta abstracció estructural requereix base lecto-escriptora mínima i familiaritat mínima amb les categories de la matèria. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *HCL Explicar com a CALP operatiu*: el manual és el gènere on la HCL Explicar és més pura i sistemàtica. Llegir i escriure manuals és aprendre a estructurar l'exposició del coneixement: la competència acadèmica transversal per excel·lència, transferible a totes les matèries.
- *Desnominalitzar com a estratègia d'accés al CALP*: convertir noms abstractes en processos verbals ("l'oxidació" → "quan un metall s'oxida") és una estratègia de simplificació sense pèrdua de rigor. Permet l'accés al CALP des del BICS: l'alumne llegeix un concepte acadèmic en la seva forma processal accessible.
- *Exemple primer com a bastida ZDP*: presentar l'exemple concret ABANS del principi abstracte és aplicar la teoria de Vygotsky. L'alumne ancora el nou concepte en el que ja coneix i llavors pot generalitzar. L'ordre exemple→abstracció és la regla d'or del manual accessible.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **manual adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Principi general

**Regla de selecció simple.** Genera un manual estructurat en apartats progressius (simple→complex) amb una entradeta inicial que anuncia el contingut, termes tècnics definits a la primera aparició, exemple concret SEMPRE abans de l'abstracció, i connectors causals explícits entre afirmacions. El nombre d'apartats i la sofisticació del vocabulari es modulen segons MECR (A1: 3 apartats / 1 terme per apartat → C1: estructura completa amb subapartats i debat terminològic).

**Límits del LLM (no judici qualitatiu complex).** El LLM no ha de decidir quins són els conceptes nuclears de la matèria ni la jerarquia disciplinària profunda (què va abans de què en termes epistèmics): aquesta decisió la pren el docent o es deriva del text font. El LLM tampoc ha de jutjar la fidelitat conceptual al text original quan adapta — només preservar mecànicament els termes, exemples i progressió que ja són presents al font.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### default

**Aplica:**
- Columna MECR de la taula Modulació
- Respecta sempre l'ordre exemple→abstracció (Pas 4)
- Connector causal explícit (Pas 5)

**Raonament pedagògic.** Per defecte, la rúbrica 7×5 ja captura la modulació necessària: el LLM aplica mecànicament la cel·la corresponent al MECR declarat sense decisions addicionals.

### fase_lectora_alfabetica_emergent

**Aplica:**
- Força modulació A1 encara que el MECR sigui A2
- 3 apartats fixos
- 1 frase d'entradeta
- 1 terme per apartat amb definició entre parèntesis adjacent
- Connector causal simple per apartat

**Raonament pedagògic.** A fase lectora alfabètica emergent, la càrrega de descodificació és encara alta. Mantenir la modulació A1 (encara que el MECR sigui superior) preserva la memòria de treball per a la dependència conceptual entre apartats, que és el cor del gènere manual.

### fase_lectora_alfabetica_fluida

**Aplica:**
- Modulació segons MECR declarat (taula completa A1→C1)

**Raonament pedagògic.** Amb fluïdesa lectora, la modulació MECR estàndard és suficient: l'alumne pot dedicar recursos a la progressió epistèmica sense que la descodificació consumeixi memòria de treball.

### pre_A1

**Exclou explícitament:**
- L'skill NO genera manual

**Raonament pedagògic.** Decisió 6 canònica Fase B: el gènere manual requereix la comprensió de la progressió simple→complex com a estructura epistèmica, abstracció no accessible sense base lecto-escriptora mínima. Cal derivar a un gènere més accessible.

## Detecció

**Senyals docent** (quan adaptar a manual):
- El text font és un capítol de llibre de text, una entrada d'enciclopèdia extensa o un document formatiu.
- La unitat vol que l'alumne comprengui un conjunt de conceptes relacionats organitzats de manera progressiva.
- L'alumne ha de llegir per comprendre com funciona alguna cosa o per qué les parts d'un sistema estan relacionades.
- L'activitat preveu que l'alumne escrigui un manual o una guia per explicar un conjunt de conceptes a un company.

**Senyals alumne** (que indica que necessita bastida):
- Comprèn els termes aïllats però no la relació entre ells.
- No distingeix el concepte central dels exemples.
- No sap per qué els conceptes estan en l'ordre en qué estan.
- Comença amb el principi abstracte sense cap exemple previ.
- Usa termes tècnics sense definir-los.

**Context favorable**:
- Totes les matèries STEAM: manuals de laboratori, guies d'ús d'instruments, textos de ciències amb terminologia nova.
- Ciències Socials: textos expositius de geografia, economia o política.
- Qualsevol matèria: glossaris extensos, unitats d'introducció de terminologia.
- Alumnat nouvingut B1-B2: el manual és el gènere CALP per excel·lència per consolidar el vocabulari acadèmic disciplinar.

**Anti-senyals** (quan NO adaptar a manual):
- El text dóna instruccions pas a pas per fer alguna cosa → instructiu o receptari.
- El text narra events o experiències → crònica, diari o biografia.
- El text té una entradeta narrativa o un exemple anecdòtic com a ganxo → divulgatiu.
- El text argumenta una postura → assaig o opinió.
- Pre-A1: la comprensió de la progressió conceptual simple→complex no és accessible sense base lecto-escriptora.

## Modulació per nivell

| Pas | Dimensió | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1<br>Crític |
|---|---|---|---|---|---|---|
| **1. Entradeta** | Context i anunci | 1 frase que diu qué s'explicarà. Directa i concreta. | 2 frases: qué s'explicarà i per qué és útil. | Entradeta que anuncia els apartats i la seva progressió lògica. | Entradeta que contextualitza el manual i el seu objectiu dins del camp. | Entradeta professional que permet saber si el manual és el que es necessita abans de llegir-lo. |
| **2. Progressió simple→complex** | Estructura i coherència | 3 apartats. Ordre estricte: el més simple primer. Un concepte per apartat. | 3 apartats progressius. Cada un es recolza en l'anterior de manera explícita. | 3-5 apartats. Progressió lògica explicitada a l'entradeta o als subtítols. | 4-6 apartats. Progressió amb relació explícita entre ells. Pot tenir subapartats d'un nivell. | Estructura completa amb progressió rigorosa. Subapartats d'un o dos nivells si cal. |
| **3. Definició de termes tècnics** | Accessibilitat i precisió | 1 terme per apartat, definit al costat en parèntesi: "el fotó (una partícula de llum)". | 1 terme per apartat en negreta amb definició integrada a la frase. | Termes tècnics en negreta definits a la primera aparició. Cap terme tècnic sense definir. | Terminologia específica de la matèria, sempre definida a la primera aparició. Pot tenir glossari final. | Vocabulari tècnic ric i definit. Glossari final si hi ha molts termes. Pot incloure debat terminològic. |
| **4. Exemple concret primer** | Ordre i ancoratge ZDP | Exemple molt quotidià ABANS del principi abstracte. "La sal es dissol a l'agua → l'osmosi és...". | Exemple concret per apartat. L'abstracció ve SEMPRE DESPRÉS de l'exemple. | Exemple que connecta el concepte nou amb el que l'alumne ja sap (ZDP). L'ordre és sagrat. | Exemple elaborat + abstracció + connexió entre apartats. | Exemple + abstracció + extensió conceptual. Pot incloure exemples límit o de frontera. |
| **5. Connectors causals** | Explicitació de relacions | "Perquè", "per això". 1 per apartat. Simple i clar. | "Perquè", "per tant", "d'aquesta manera". Variats mínimament. | "Com a resultat", "per tant", "d'aquí se'n deriva". Variats. Distinció causa/efecte explícita. | Connectors causals precisos i variats. Distinció causa/conseqüència/condició. | Connectors sofisticats. Pot incloure concessius ("tot i que") i adversatius ("malgrat"). |
| **6. Criteris transversals** | Desnominalitzar processos | Convertir noms abstractes en processos verbals: "oxidació" → "quan s'oxida". A1: sempre. | Idem. "la fotosíntesi" → "quan les plantes fabriquen aliment". | Idem. La desnominalització és la estratègia principal per fer accessible el CALP. | Idem. Pot mantenir el nom abstracte si va precedit de la desnominalització. | Idem. El nom abstracte és admissible quan el context disciplinar ho requereix i el procés ja s'ha explicat. |
|  | No referència futura | Cap "ho veurem més endavant" ni referència a apartats posteriors. El text és autocontingut. | Idem. Cap referència lateral o nota al peu que interrompi el flux. | Idem. Cap nota al peu a A1-B1. | Idem. Notes al peu admeses si no interrompen el flux principal. | Idem. Notes al peu admeses per a matisos tècnics avançats. |
|  | Fidelitat al text font | Fidelitat als conceptes principals i a la progressió bàsica. | Fidelitat als conceptes, a la progressió i a les definicions essencials. | Fidelitat als conceptes, a la progressió, a les definicions i als connectors causals del text font. | Fidelitat a la complexitat conceptual i al context disciplinar del text original. | Fidelitat a la complexitat, als matisos i als debats terminològics si n'hi ha. |
| **7. Autoavaluació metacognitiva** | Reflexió sobre el procés | "He escrit 3 apartats. He explicat un terme difícil de cada apartat." | "He posat un exemple per a cada concepte. He usat 'perquè' o 'per això' per explicar les causes." | "Els meus apartats van de més simple a més complex. Cada terme tècnic té la seva definició." | "He relacionat els apartats entre si. He usat vocabulari específic de la matèria correctament." | "El meu manual explica el tema de manera completa, sistemàtica i progressiva, amb vocabulari precís." |

## Casos especials

### nouvingut_L1_CALP_disciplinar

**Trigger:** nouvingut_L1: true AND mecr_in: [B1, B2] AND context_matèria: STEAM_o_socials

**Modulació:**
- afegir_glossari_final_amb_L1: true (columna L1 si alfabet llatí; columna L1 + transliteració si no llatí)
- densitat_termes_tècnics_per_apartat: 1 (vs 2-3 default a B1+)
- desnominalitzar_obligatori: true (no admetre nom abstracte sense forma processal adjacent encara que B1+ ho permeti)

**Raonament pedagògic.** Per a nouvinguts B1-B2 el manual és el gènere CALP per excel·lència (Cummins) però la combinació de terminologia disciplinària nova + L2 acadèmica satura. El glossari amb L1 activa coneixement previ (translanguaging/TOLC) sense renunciar a la lectura del manual en català.

### DUA_acces

**Trigger:** dua_equals: Acces AND mecr_in: [A1, A2, B1]

**Modulació:**
- max_apartats: 3 (encara que el MECR permetés més)
- un_concepte_per_apartat: true (estricte)
- exemple_quotidià_obligatori_no_disciplinar: true (l'exemple ancorat al món viscut, no a un altre concepte acadèmic)
- connector_causal_per_apartat: 1 (simple: 'perquè', 'per això')
- prohibit: subapartats_d'un_nivell

**Raonament pedagògic.** El principi DUA d'accés demana minimitzar la càrrega cognitiva extrínseca per alliberar memòria de treball per al contingut. La progressió epistèmica del manual ja és cognitivament exigent; cal pelar tota la complexitat estructural perquè l'alumne pugui dedicar recursos a la dependència conceptual entre apartats.

### AACC

**Trigger:** aacc: true AND mecr_in: [B2, C1]

**Modulació:**
- afegir_apartat_debat_terminologic: true (a C1: exposar tensions o evolució del terme dins la disciplina)
- admetre_exemples_limit_o_frontera: true (casos on el principi general no aplica netament)
- densitat_connectors_sofisticats: alta (concessius 'tot i que', adversatius 'malgrat', condicionals 'sempre que')
- glossari_final_amb_etimologia: opcional

**Raonament pedagògic.** El manual per a AACC ha de mantenir la progressió simple→complex (no saltar-se-la) però oferir matís disciplinari real al final de cada apartat o al manual sencer. Saltar-se la progressió és infantilitzar; mantenir-la i afegir matís és respectar el ritme cognitiu i la set conceptual.

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
| 1 Entradeta — Context | `binary` + `qualitative` | no | binary: entradeta present (primer paràgraf o bloc); qualitative: LLM-jutge sobre si anuncia els apartats i la progressió (B1+) |
| 2 Progressió — Estructura | `countable` + `qualitative` | no | comptar apartats; qualitative: LLM-jutge sobre si la progressió és genuïnament simple→complex (no alfabètica ni temàtica aleatòria) |
| 3 Termes tècnics — Accessibilitat | `binary` + `qualitative` | no | binary: detectar termes tècnics no definits (paraules de camp lèxic acadèmic sense explicació adjacent); qualitative: LLM-jutge sobre adequació de la definició al nivell |
| 4 Exemple concret primer — Ordre ZDP | `structural` + `binary` | no | structural: detectar si l'abstracció apareix ABANS de l'exemple (inversió ZDP); binary: exemple present per apartat; patrons a detectar: terme tècnic al primer paràgraf sense exemple previ |
| 5 Connectors causals — Relacions | `structural` + `countable` | no | detectar i comptar connectors causals ("perquè", "per tant", "d'aquesta manera", "com a resultat"); verificar varietat per nivell; detectar absència de connectors en textos de B1+ |
| 6.1 Criteris — Desnominalitzar | `binary` + `qualitative` | no | binary: detectar noms abstractes sense desnominalització adjacent (A1-B1); qualitative: LLM-jutge sobre si la desnominalització és adequada i accessible |
| 6.2 Criteris — No referència futura | `binary` | no | regex: detectar "ho veurem", "a l'apartat X", "més endavant", "a continuació veurem" com a referència a contingut posterior no present |
| 6.3 Criteris — Fidelitat al text font | `cross_source` + `qualitative` | **sí** (si adaptació) | comparar conceptes principals, progressió i definicions original vs adaptats; LLM-jutge sobre si la simplificació preserva la integritat conceptual |
| 7 Autoavaluació metacognitiva | `metacognitive` | no | derivar a vista d'autoavaluació alumne + registre docent |

**Notes:**
- Progressió simple→complex (Pas 2): el criteri de progressió és el descriptor qualitatiu més difícil del manual. Un LLM-jutge ha de verificar que els apartats no estan en ordre alfabètic, temàtic o arbitrari sinó que cada un pressuposa l'anterior.
- Exemple primer (Pas 4): altament automatitzable per posició. Si un terme tècnic apareix a la primera frase d'un apartat sense exemple previ en la mateixa frase o en la frase anterior, és inversió ZDP.
- Desnominalitzar (Pas 6.1): detectable per llista de sufixos nominalitzadors (-ció, -ment, -isme, -itat) que identifiquen abstraccions susceptibles de desnominalització. Un LLM-jutge verifica si la forma desnominalitzada és present adjacent.

## Regles transversals

- **Forma sobre MECR**: la forma del gènere guanya sobre el nivell MECR. Si hi ha conflicte entre simplificar al MECR i preservar l'estructura formal del gènere (versos, torns, passos numerats, camps), guanya la forma. Es pot simplificar el VOCABULARI, però cal seguir l'estructura canònica que defineix la skill del gènere. Millor un text mínimament adaptat però formalment íntegre que un text aplanat que destrueixi el gènere.

## Heurístiques docent

**H1 — La seqüència d'apartats com a mapa conceptual previ.**
Proposo que l'alumne escrigui primer els títols dels apartats en una línia i els numeri per ordre: "1. Qué és → 2. Com funciona → 3. Per a qué serveix". Amb el mapa fet, cada apartat s'escriu sol. Funciona com a bastida de planificació per a qualsevol manual.

**H2 — "Primer mostra-m'ho, després explica-m'ho".**
Quan l'alumne comença un apartat amb el principi abstracte, li demano: "Posa'm primer un exemple que jo pugui imaginar." Un cop l'exemple és clar, el principi abstracte ve sol. Aquesta inversió (exemple → abstracció) és la regla d'or del manual accessible.

**H3 — El diccionari de termes com a bastida (A1-B1).**
Per a textos amb molts termes tècnics, proposo construir un glossari previ amb l'alumne: 5-8 termes, cada un amb una definició en veu pròpia. El glossari es posa al marge mentre l'alumne llegeix. Redueix la sobrecàrrega cognitiva i prepara la lectura del manual.

**H4 — El connector causal com a test de comprensió.**
Proposo el "test del perquè": l'alumne llegeix cada afirmació del manual i intenta completar "X... perquè...". Si no pot completar la frase, no ha comprès la relació. La impossibilitat d'usar un connector causal és un indicador fiable de comprensió superficial.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Manual
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
### Entradeta
### Apartats
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
**terme tècnic** (definició)
Per exemple, ...
perquè / per tant / com a resultat / d'aquesta manera
```

**Headers explícitament PROHIBITS:**
```
## Introducció
## Conclusió
## Resum
```

**Regla d'integritat estructural.** Sense `## Manual` + `### Entradeta` + `### Apartats` literals (amb cada apartat com a H4), el parser de pas3.html no detecta els apartats progressius com a unitats i els descriptors de Pas 1 (Entradeta) i Pas 2 (Progressió) queden sense àncora estructural.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): HCL Explicar, progressió BICS→CALP, desnominalització.
- Cummins, J. (2000): *Language, Power and Pedagogy* — desnominalització com a estratègia d'accés al CALP; distinció BICS/CALP.
- Vygotsky, L.S. (1978): *Mind in Society* — exemple concret com a ancoratge ZDP; progressió de simple a complex.
- Decret 175/2022 (currículum Catalunya): competència en comunicació lingüística i competència científica.
