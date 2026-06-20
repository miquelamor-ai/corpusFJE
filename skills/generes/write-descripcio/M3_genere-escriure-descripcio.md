---
modul: M3
titol: "Escriure/adaptar una descripció"
tipus: genere-discursiu
categoria_principal: generes
categories_secundaries: []
descripcio: "Instrument per adaptar o generar una descripció: presentació de les característiques d'un objecte, persona, lloc o fenomen en ordre espacial i amb concreció progressiva. HCL Descriure + Explicar (relació entre característiques, B1+). S'adapta a pre-A1 (enumeració oral mediada per l'adult, sense text escrit). Rúbrica gradada 7 passos × 6 nivells MECR (pre-A1→C1)."
mecr_range: [pre-A1, A1, A2, B1, B2, C1]
agent_roles: [adapter, generator]
genre_key: descripcio
macro_tipologia: descriptiva
label_ca: "Descripció"
translanguaging: false
multimodal: true
moduls_relacionats: [M3]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: write-descripcio@corpusFJE/skills/generes/write-descripcio
review_status: pilot-fusio-4
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, fidelitat-gradada-C2, variabilitat-cardinal-passos-D3]
  aplicades_post_review: [comparacio-c1-disciplinar-arquetip, separacio-A2-marcador-funcional, superlatius-B2-terminologia-disciplinar]
  comentari_key: "La descripció és l'instrument del corpus que millor operacionalitza el pre-A1 mitjançant la mediació visual i oral de l'adult, i el gènere fonamental sobre el qual es construeixen totes les HCL complexes."
---

# Escriure/adaptar una descripció

## Descripció

La descripció presenta les característiques d'un objecte, persona, lloc o fenomen amb **ordre espacial** i **concreció progressiva**. El seu tret definitori és el recorregut sistemàtic: de dalt a baix, de fora a dins, de conjunt a detall. A diferència del conte, no hi ha temps ni acció; a diferència de l'informe, no hi ha dades ni conclusions.

**Tipologia MALL**: Descriptiva.
**HCL principal**: Descriure — identificar i caracteritzar les parts d'un objecte, lloc, persona o fenomen.
**HCL secundàries**: Explicar — relacionar característiques entre si i amb la funció (B1+).
**S'adapta a pre-A1**: la descripció és el gènere que millor s'adapta a la fase emergent/logogràfica. A pre-A1, l'alumne assenyala, nomena oralment o dicta a l'adult; la imatge o l'objecte real fa de bastida total. L'adult medeia el significat sense que l'alumne hagi d'inferir res abstracte: cada part es pot assenyalar, cada adjectiu es pot il·lustrar. Filtre D6: (1) l'adult pot mediar amb imatges i gest sense que l'alumne infereixi cap abstracció; (2) el gènere no requereix plans simultanis, abstracció temporal ni significat diferit.

**Connexions MALL transversals:**
- *Descripció com a HCL fonamental*: la descripció és la HCL inicial de tot el currículum. Tots els gèneres complexos (biografia, informe, divulgatiu) contenen descripcions com a submòdul. L'alumne que aprèn a descriure bé té la base de tots els altres gèneres.
- *Ordre espacial com a bastida del pensament*: l'ordre "de dalt a baix" o "de fora a dins" no és una convenció literària; és una bastida cognitiva. Externalitza el recorregut del pensament i el fa visible.
- *Multimodalitat com a accés pre-A1*: a pre-A1 i A1, la imatge o l'objecte real és la descripció. L'alumne descriu el que veu; la producció lingüística és secundària o oral. Aquesta mediació visual és la porta d'entrada al gènere i es manté com a suport fins a A2.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **descripció adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast i en produeix els seus textos.
**Sub-granularitat dins de pre-A1 i A1**: es treballa amb `fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]`. A pre-A1 logogràfic, la descripció és oral i mediada; no hi ha text llegit per l'alumne, només el suport visual.

## Principi general

**Regla de selecció simple.** Genera o adapta un text descriptiu per a la LECTURA de l'alumne aplicant la cel·la de la rúbrica que correspon al seu nivell MECR (pre-A1→C1) i als 7 passos: identificació de l'objecte, ordre espacial, adjectius, comparacions concretes, separació físic/funcional, criteris transversals (llargada, adjectius subjectius, fidelitat al text font) i autoavaluació metacognitiva. NO genera la producció autònoma de l'alumne: només models de lectura.

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix el nivell MECR de l'alumne, ni la fase lectora, ni si el text font és pedagògicament adequat, ni si el contingut descrit és rellevant per a la unitat didàctica. Aquestes decisions són del docent (variables del perfil). El LLM tampoc decideix si un adjectiu marginal és subjectiu o concret en context ambigu: aplica la llista negra explícita i, en cas de dubte, manté l'adjectiu del text font.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### alumne_general

**Inclou si:**
- mecr_level com a variable principal de selecció (columna de la taula Modulació)
- aplicació literal dels 7 passos per a la columna MECR triada

**Exclou explicitament:**
- interpolació entre columnes de la taula Modulació
- modulació MECR a la baixa per AACC

**Raonament pedagògic.** La taula Modulació és la mascara principal: cada columna MECR conté els descriptors literals dels 7 passos. No s'interpola perquè cada nivell té integritat pròpia (principi de gradació discreta MALL).

### alumne_fase_lectora_variable

**Inclou si:**
- dins de pre-A1 i A1, la variable fase_lectora modula el format de sortida
- logogràfica → enumeració oral mediada sense text escrit
- alfabètica emergent → frases simples amb suport pictogràfic
- alfabètica fluida → frases simples sense pictograma obligatori

**Exclou explicitament:**
- text escrit autònom a pre-A1 logogràfic
- pictograma obligatori a alfabètica fluida

**Raonament pedagògic.** La fase lectora determina si l'alumne pot accedir al codi escrit. A logogràfica, forçar text és demanar descodificació no disponible (Kuhn, Cummins); la mediació oral i el suport visual són la porta d'entrada real al gènere.

### alumne_DUA_acces

**Inclou si:**
- augment de densitat de [IMG:...] i [PICTO:...] sobre la sortida del nivell MECR triat

**Exclou explicitament:**
- canvi de columna de la rúbrica (la modulació DUA acces no baixa el MECR)

**Raonament pedagògic.** El principi DUA d'Accés requereix vies alternatives d'entrada al significat sense reduir el sostre cognitiu. Els suports visuals s'apilen sobre la modulació MECR, no la substitueixen.

### alumne_AACC

**Inclou si:**
- manteniment del nivell MECR del perfil (no modula a la baixa)
- extensió opcional del Pas 4 (comparacions amb arquetips disciplinars) si el docent ho indica

**Exclou explicitament:**
- reducció automàtica del nivell de complexitat

**Raonament pedagògic.** L'alumnat AACC necessita sostre alt sense topall artificial. La rúbrica ja preveu nivells C1 amb arquetips disciplinars; el LLM no augmenta automàticament la complexitat — el docent puja el MECR objectiu si cal.

### alumne_nouvingut_L1

**Inclou si:**
- activació de la columna L1 a les comparacions concretes (Pas 4) si el cas especial nouvingut_L1_alfabet_no_llati s'activa
- priorització de comparacions amb camp lèxic comú (objectes domèstics, parts del cos, colors bàsics)

**Exclou explicitament:**
- modulació MECR per defecte (no baixa el nivell)
- referents culturals locals no universals

**Raonament pedagògic.** El nouvingut amb L1 no té el coneixement previ cultural local però sí el conceptual universal. La translanguaging al Pas 4 activa coneixement previ via comparacions concretes accessibles (Cummins & Early 2011).

## Detecció

**Senyals docent** (quan adaptar a descripció):
- El text font descriu un objecte, lloc, persona, animal o fenomen (fitxa tècnica, entrada enciclopèdica descriptiva, descripció d'un paisatge, d'un monument, d'un organisme).
- La unitat de Ciències Naturals, Ciències Socials, Tecnologia, Art o Llengua treballa les característiques d'un element.
- L'alumne ha de llegir per identificar i retenir les parts o característiques d'alguna cosa.

**Senyals alumne** (que indica que necessita bastida descriptiva):
- Descriu en ordre aleatori: barreja el color amb la funció, la mida amb la localització.
- Usa adjectius subjectius genèrics ("bonic", "interessant") però pocs concrets.
- No distingeix descripció física de funció o d'impacte emocional.
- Incompleta: atura la descripció sense haver cobert les parts principals.

**Context favorable**:
- Ciències Naturals: descripció d'un animal, planta, ecosistema o procés biològic.
- Ciències Socials: descripció d'un monument, paisatge, cultura o institució.
- Tecnologia: descripció d'un objecte tècnic, eines o màquines.
- Art i Música: descripció d'una obra, d'un instrument musical o d'una composició.
- Alumnat nouvingut pre-A1/A1: l'objecte real o la imatge és la porta d'entrada que no requereix coneixement previ de la tradició cultural local.

**Anti-senyals** (quan NO adaptar a descripció):
- El text narra una successió d'esdeveniments → conte o biografia.
- El text argumenta una postura → assaig o opinió.
- El text informa sobre resultats d'una recerca amb dades i conclusions → informe.
- El text defineix un terme amb fórmula categoria+especificitat → entrada enciclopèdica.

## Modulació per nivell

| Pas | Dimensió | pre-A1<br>Emergent | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1<br>Crític |
|---|---|---|---|---|---|---|---|
| **1. Identificació de l'objecte** | Precisió i situació | Assenyalar i dir el nom oralment. Dictat a l'adult. | 1 frase que diu què és: "Això és un ocell." | Frase general que situa l'objecte amb categoria: "El colibrí és un ocell molt petit." | Descripció general amb categoria i 1 tret diferencial: "El colibrí és un ocell diminut conegut pel seu vol estacionari." | Descripció general amb context i funció integrats. | Descripció general amb matisos conceptuals i terminologia precisa. |
| **2. Ordre espacial** | Seqüència i coherència | Llista oral de noms (parts assenyalades a la imatge o objecte real). | 3-4 característiques ordenades de dalt a baix o de fora a dins. Una per frase. | 5-6 característiques en ordre espacial explícit amb connectors simples. | 6-8 característiques amb ordre espacial clar i progressiu. Connectors: "a la part superior", "al centre". | Ordre espacial respectat amb matisos i descripció funcional integrada. | Ordre espacial exhaustiu amb matisos conceptuals i terminologia específica de la disciplina. |
| **3. Adjectius** | Varietat i precisió | Pictograma o imatge en lloc d'adjectius escrits. | Adjectius molt freqüents i concrets: "vermell", "gran", "rodó". | Adjectius variats i concrets. Sense subjectius genèrics ("bonic", "interessant"). | Adjectius precisos i variats del camp lèxic de la unitat. Sense superlatius sintètics. | Adjectius precisos del camp lèxic de la matèria. Superlatius analítics admissibles. | Adjectius tècnics i de matís conceptual. Terminologia disciplinar. |
| **4. Comparacions concretes** | Accessibilitat i precisió | Assenyalar l'objecte real o la imatge (sense text). | Comparacions molt quotidianes: "és com una pilota", "és del color del cel". | Comparacions concretes i variades: "de la mida d'una mà", "tan llarg com un llapis". | Comparacions funcionals: "té X, que permet Y". Pot comparar amb elements de la mateixa categoria. | Comparació amb altres elements de la mateixa categoria amb matís. | Comparació de l'objecte amb arquetips o fenòmens de la mateixa disciplina per precisar-ne el matís diferencial. |
| **5. Separació descripció física / funcional** | Distinció i organització | Enumeració oral de parts (sense separació). | Descripció física únicament. Una característica per frase. | Distinció incipient entre descripció física i descripció funcional en frases separades. Al menys una frase conté el connector "serveix per" o "s'utilitza per". | Separació explícita entre descripció física i funció o impacte en paràgrafs o blocs diferenciats. | Descripció física, funcional i emocional ben diferenciades. | Distinció terminològica entre descripció observable i processos subjacents. |
| **6. Criteris transversals** | Llargada | Enumeració oral. Dictat a l'adult (format llista). | 3-4 frases. Format llista o frases simples. | 5-6 frases o 1-2 paràgrafs curts. | 1-2 paràgrafs amb 6-8 característiques. | 2-3 paràgrafs complets. | Text complet amb tots els matisos necessaris. |
|  | Adjectius subjectius | Cap adjectiu subjectiu (ni oral ni escrit). Tots referits a la imatge real. | Cap adjectiu valoratiu genèric ("bonic", "especial"). Tots concrets i verificables. | Idem. | Idem. | Idem. Superlatius d'ordre espacial o quantitatiu admissibles si son terminologia ("el punt més alt", "la zona més densa"). | Idem. Terminologia valorativa disciplinar admissible si s'usa en el camp lèxic corresponent. |
|  | Fidelitat al text font | Fidelitat a les parts visibles de l'objecte o imatge presentat. | Fidelitat a les característiques principals de l'objecte o persona descrits. | Fidelitat a les característiques i a la funció essencial. | Fidelitat a les característiques, la funció i el to factual del text original. | Fidelitat a les característiques, la funció, el context i el to. | Fidelitat a la complexitat descriptiva del text original, incloent matisos i terminologia. |
| **7. Autoavaluació metacognitiva** | Reflexió sobre el procés | "He assenyalat les parts i he dit el nom." (oral) | "He descrit 3-4 parts del [objecte/lloc/persona] en ordre." | "He descrit les característiques seguint un ordre de l'exterior a l'interior (o de dalt a baix)." | "He relacionat algunes característiques entre si i amb la funció. He revisat que l'ordre sigui espacial." | "He fet una descripció detallada i precisa amb vocabulari específic. He separat descripció física i funcional." | "He descrit amb matisos conceptuals i he relacionat les característiques amb processos. He revisat que no hi hagi adjectius subjectius no disciplinars." |

## Casos especials

### pre_A1_fase_logografica

**Trigger:** mecr_equals: pre-A1 AND fase_lectora_equals: logografica

**Modulació:**
- no_escriptura_autonoma: true
- format_sortida: enumeracio_oral_mediada
- suport_obligatori: imatge_o_objecte_real
- reemplaca_text_per: pictograma_o_imatge_amb_etiqueta_oral
- max_items: 5_parts_assenyalables

**Raonament pedagògic.** A fase logogràfica l'alumne encara no descodifica grafies, només reconeix la imatge com a text; forçar escriptura autònoma és demanar CALP en context BICS (Cummins, Kuhn 1991). La mediació oral i el suport visual obligatori són la porta d'entrada al gènere.

### nouvingut_L1_alfabet_no_llati

**Trigger:** nouvingut_L1: true AND L1_script_in: [arab, han, cirillic, devanagari, hebreu]

**Modulació:**
- comparacions_camp_lexic_comu: prioritzar (objectes domestics, parts del cos, colors basics)
- evitar_referents_culturals_locals_no_universals: true
- oferir_pictograma_a_tota_part_nominada_fins_A2: true

**Raonament pedagògic.** Per al nouvingut amb L1 d'alfabet no llatí, el coneixement previ cultural local no és compartit; les comparacions han d'ancorar-se en camps lèxics universals (Cummins, MALL translanguaging). El pictograma supleix la falta de pont fonètic immediat fins a A2.

### MECR_low_DUA_acces

**Trigger:** mecr_in: [pre-A1, A1, A2] AND DUA_dimensio: acces

**Modulació:**
- densitat_imatges: alta (1 imatge per cada 2-3 parts descrites)
- ordre_espacial_visual_explicit: fletxes_o_numeracio_sobre_imatge
- reemplaca_adjectius_per: pictograma_quan_existeix

**Raonament pedagògic.** En perfils amb necessitat DUA d'Accés a MECR baix, el pictograma i les fletxes externalitzen el recorregut espacial i compensen la càrrega de descodificació. No són decoració sinó accés alternatiu al significat (DUA principi 1, MALL multimodalitat com a primera llengua).

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
| 1 Identificació — Precisió i situació | `qualitative` + `binary` | no | binary: presència de la categoria (X és un Y); qualitative: LLM-jutge sobre precisió i tret diferencial per nivell |
| 2 Ordre espacial — Seqüència | `structural` + `qualitative` | no | verificar seqüència de dalt a baix / fora a dins; detectar salts d'ordre no justificats |
| 3 Adjectius — Varietat i precisió | `binary` + `qualitative` | no | binary: absència d'adjectius subjectius genèrics (llista negra: bonic, interessant, especial, increïble); qualitative: LLM-jutge sobre adequació al camp lèxic |
| 4 Comparacions — Accessibilitat i precisió | `qualitative` | no | LLM-jutge: la comparació és concreta i quotidiana per al nivell |
| 5 Separació física/funcional — Distinció | `structural` + `qualitative` | no | detectar barreja descripció física/emocional al mateix paràgraf; LLM-jutge per a A2+ |
| 6.1 Criteris — Llargada | `countable` | no | comptar frases o paràgrafs; verificar llindar per nivell |
| 6.2 Criteris — Adjectius subjectius | `binary` | no | regex/llista negra: detectar "bonic", "interessant", "especial", "increïble", "meravellós" sense qualificació |
| 6.3 Criteris — Fidelitat al text font | `cross_source` | **sí** (si adaptació) | comparar característiques principals originals vs adaptades; verificació per nivell |
| 7 Autoavaluació metacognitiva | `metacognitive` | no | derivar a vista d'autoavaluació alumne + registre docent |

**Notes:**
- Adjectius subjectius (Pas 3 i 6.2) són parcialment automatitzables per llista negra (binary), però casos ambigus requereixen LLM-jutge (ex. "gran" pot ser concret o valoratiu).
- Ordre espacial (Pas 2) és verificable estructuralment però depèn del tipus d'objecte: "de dalt a baix" per a persones/plantes, "de fora a dins" per a estructures, "de general a concret" per a paisatges.
- A pre-A1 logogràfic, els Passos 1-5 son orals i mediats per l'adult; la validació automàtica no aplica — derivar a registre docent.

## Heurístiques docent

**H1 — "De dalt a baix" com a bastida universal.**
Proposo a l'alumne que imagini una càmera que comença dalt del tot de l'objecte i baixa fins a baix. El que la càmera "veu" en ordre és la descripció. Funciona per a animals, persones, monuments i paisatges. A pre-A1/A1, el docent fa el moviment amb el dit sobre la imatge i l'alumne nomena el que assenyala.

**H2 — Comparació concreta com a definició a A1-A2.**
Quan l'alumne no sap un adjectiu precís, proposo: "És del color de ___?" / "És de la mida d'un ___?" La comparació amb un referent familiar substitueix l'adjectiu tècnic i és pedagògicament més rica: activa el coneixement previ i construeix el pont cap al vocabulari específic.

**H3 — Separar en dues columnes: "com és" / "per a què serveix".**
Abans d'escriure, l'alumne emplena dues columnes. La primera és la descripció física (colors, mides, parts); la segona, la funció o l'impacte (per a què serveix, com afecta). La separació visual prèvia evita la barreja al text. Especialment útil a B1+ quan l'alumne comença a integrar funció i descripció física al mateix paràgraf.

**H4 — La llista negra d'adjectius.**
Proposo als alumnes una llista d'adjectius a evitar: "bonic", "interessant", "especial", "increïble". Per a cada adjectiu de la llista, la pregunta és: "Pots posar una foto d'aquest adjectiu?" Si no, cal substituir-lo per un adjectiu que sí que s'hi pugui representar. Funciona des de A2.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Descripció
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
cap
```

**Bullets / moments interns** (si aplica — NO son H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
[IMG: clau_imatge|text_alternatiu]
[PICTO: terme_arasaac|terme_visible]
```

**Headers explicitament PROHIBITS:**
```
## Descripció física
## Descripció funcional
## Parts
## Característiques
```

**Regla d'integritat estructural.** El text adaptat es publica sota el H2 literal `## Descripció` seguit del cos descriptiu en prosa o llista (segons MECR). No s'usen H3 dins de la descripció. A pre-A1 logogràfic, la sortida és una llista oral mediada (no prosa). Sense aquest H2 literal, el frontend no detecta el bloc de lectura.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): HCL Descriure, gradació enumeratiu→descriptiu, multimodalitat pre-A1.
- Halliday, M.A.K. (1994): *An Introduction to Functional Grammar* — la descripció com a funció ideativa de la llengua; base de la distinció descripció física / funcional / emocional.
- Decret 175/2022 (currículum Catalunya): competència en comunicació lingüística (dimensió literària i cultural) i competència en consciència i expressions culturals.
