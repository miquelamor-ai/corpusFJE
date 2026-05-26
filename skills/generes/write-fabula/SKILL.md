---
name: write-fabula
description: 'Use when adapting or generating a fàbula for students. Activates when
  genre_discursiu == "fabula". Applies explicit moral, archetypal characters, and
  maintained character traits. Output: fàbula in markdown with situation, action,
  denouement, and explicit moral.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: fabula
tipologia: Narrativa
mecr_range:
- A1
- A2
- B1
- B2
- C1
agent_role: adapter
tools_required: []
triggers:
- path: params.genere_discursiu
  equals: fabula
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-fabula.md
font_version: 4.0.0-canonic
generat_at: '2026-05-26'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 73ccb627464a57f2
---

# Escriure/adaptar una fàbula — skill operativa per a LLM

La fàbula és una narració breu amb personatges arquetípics (animals o éssers personificats) que il·lustren un conflicte moral i el resolen amb una lliçó explícita: la **moral**. El seu tret definitori és la doble estructura: la narració superficial (la historia dels personatges) i la lliçó profunda (la moral, que s'extreu explícitament al final). A diferència del conte, la fàbula té una funció prescriptiva: ensenya com s'ha d'actuar.

**Tipologia MALL**: Narrativa (imaginar — il·lustrar un principi moral via ficció).
**HCL principal**: Narrar — seqüenciar una acció amb personatges arquetípics que il·lustren una tensió moral.
**HCL secundàries**: Interpretar/Valorar — la moral és HCL explícita des de A2 · Argumentar — justificar la moral amb el text, B2+.
**No s'adapta a pre-A1**: la fàbula requereix comprendre dos plans simultanis — la narració superficial i la lliçó moral — i entendre que els personatges *representen* arquetips humans, no que *són* animals. Aquesta abstracció de segon nivell (símbol + inferència) no és accessible a la fase logogràfica/emergent, on el significat es construeix per via visual i concreta. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Arquetip com a bastida transcultural*: els personatges arquetípics (el ràpid i descuidat, el llest i orgullós, l'humil i treballador) son esquemes cognitius universals. L'alumne nouvingut els reconeix fins i tot sense conèixer la tradició literària local perquè els arquetips son transculturals. No cal translanguaging: l'analogia s'activa per les accions del personatge, no per la traducció.
- *Moral com a transició Narrar → Valorar*: escriure la moral és el pas de contar el que ha passat a dir el que significa. Aquesta transició és el nucli de la competència MALL de valoració i el primer pont cap a l'argumentació (B2+).
- *Eix oral/escrit*: la fàbula es presta a la lectura dramatitzada (A1-A2) per activar la percepció dels arquetips abans de la lectura autònoma.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **fàbula adaptada per a la LECTURA** de l'alumne (el que el docent presenta perquè l'alumne llegeixi). **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast i en produeix els seus textos; l'adaptació és tasca del docent.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logografic perquè la fàbula requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Personatges arquetípics**
- Nombre i definició: 2 personatges amb un tret únic cadascun (ràpid/lent, llest/ingenu). Noms genèrics ("La llebre", "La tortuga").

**2. Caràcter mantingut**
- Consistència: El personatge ràpid és ràpid de principi a fi. Cap canvi de caràcter.

**3. Situació i fet desencadenant**
- Context i tensió: Situació en 1-2 frases. Incident simple que posa la narració en moviment.

**4. Acció i desenllaç**
- Causalitat i coherència: Acció en 1-2 frases. Desenllaç clar i directe. Conseqüència evident del tret del personatge.

**5. Moral explícita**
- Format i universalitat: 1 frase curta. Sempre precedida de "Moral:". Universal: aplicable fora de la historia.

**6. Criteris transversals**
- Llargada: 6-8 frases totals. Moral d'1 frase.
- Llengua i registre: Sense fórmules arcaiques ("En un llunyà temps..."). Llengua actual. Passat simple.
- Fidelitat al text font: Fidelitat a la moral original i als arquetips. L'acció pot simplificar-se.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit 2 personatges amb un tret diferent cadascun. He escrit la moral al final i comença amb 'Moral:'."

### A1 — Inicial


**1. Personatges arquetípics**
- Nombre i definició: 2 personatges arquetípics ben definits des del primer paràgraf. Tret únic explícit al text.

**2. Caràcter mantingut**
- Consistència: Caràcter consistent en tots els actes del personatge.

**3. Situació i fet desencadenant**
- Context i tensió: Situació + fet desencadenant diferenciats en paràgrafs o frases separades. El fet crea una tensió senzilla.

**4. Acció i desenllaç**
- Causalitat i coherència: Acció narrada amb connectors temporals simples. Desenllaç coherent amb el caràcter.

**5. Moral explícita**
- Format i universalitat: 1-2 frases. Precedida de "Moral:". Aplicable a situacions reals que l'alumne pot reconèixer.

**6. Criteris transversals**
- Llargada: 8-12 frases. Moral d'1-2 frases.
- Llengua i registre: Idem. Sense temps verbals arcaics.
- Fidelitat al text font: Fidelitat a la moral i als personatges arquetípics.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La historia dels meus personatges mostra per qué la moral és certa. He revisat que la moral sigui una lliçó aplicable fora de la historia."

### A2 — Funcional


**1. Personatges arquetípics**
- Nombre i definició: 2-3 personatges amb tret únic consistent durant tota la fàbula. El tret s'anuncia al principi.

**2. Caràcter mantingut**
- Consistència: Caràcter mantingut fins al desenllaç. El desenllaç deriva directament del caràcter.

**3. Situació i fet desencadenant**
- Context i tensió: Situació amb context del tret dels personatges + fet que posa el tret a prova.

**4. Acció i desenllaç**
- Causalitat i coherència: Acció amb causa-efecte explícit. Desenllaç que deriva directament i de forma inequívoca del caràcter.

**5. Moral explícita**
- Format i universalitat: 2 frases. Explícita, universal i ben argumentada. El lector no ha d'inferir-la.

**6. Criteris transversals**
- Llargada: 3-4 paràgrafs + moral.
- Llengua i registre: Idem. Registre literari simple admissible sense arcaisme.
- Fidelitat al text font: Fidelitat a la moral, als arquetips i a la tensió moral del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El caràcter del personatge no canvia durant la historia. La moral explica una lliçó aplicable a la vida."

### B1 — Estratègic


**1. Personatges arquetípics**
- Nombre i definició: 3-4 personatges amb trets complementaris o oposats. Les relacions entre trets generen el conflicte.

**2. Caràcter mantingut**
- Consistència: Caràcter consistent. Pot incloure un moment d'auto-engany del personatge (mantenir el tret fins a les últimes conseqüències).

**3. Situació i fet desencadenant**
- Context i tensió: Situació ben construïda que prepara el conflicte moral. Context suficient per comprendre els trets.

**4. Acció i desenllaç**
- Causalitat i coherència: Acció amb tensió creixent. Desenllaç que justifica plenament la moral, no pot ser d'una altra manera.

**5. Moral explícita**
- Format i universalitat: Explícita. Connecta la historia amb un principi general aplicable fora del context concret.

**6. Criteris transversals**
- Llargada: 3-4 paràgrafs ben diferenciats + moral (2 frases).
- Llengua i registre: Idem. Recursos expressius admissibles si no son arcaics.
- Fidelitat al text font: Fidelitat a la moral, als arquetips i al to del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La historia té tensió i el desenllaç és una conseqüència lògica del caràcter dels personatges. He revisat que la moral no sigui massa específica."

### B2 — Acadèmic


**1. Personatges arquetípics**
- Nombre i definició: Personatges amb complexitat arquetípica. El tret pot tenir matisos sense trencar l'arquetip ni la moral.

**2. Caràcter mantingut**
- Consistència: Arquetip consistent però amb matisos que enriqueixen la moral sense contradir-la.

**3. Situació i fet desencadenant**
- Context i tensió: Situació elaborada que posa en tensió valors o concepcions del món. El conflicte moral és evident des del principi.

**4. Acció i desenllaç**
- Causalitat i coherència: Acció elaborada. Desenllaç que pot tenir ironia lleugera si la moral ho suporta i s'explicita.

**5. Moral explícita**
- Format i universalitat: Explícita però no simplista. Pot plantejar una tensió entre valors o un dilema, però mai implícita.

**6. Criteris transversals**
- Llargada: Fàbula completa amb riquesa descriptiva + moral elaborada (fins a 3 frases).
- Llengua i registre: Sense arcaismes que dificultin la comprensió. Usos estilístics conscients (pastitx literari) admissibles si no comprometen la claredat.
- Fidelitat al text font: Fidelitat a la moral, als arquetips, al to i a la intenció del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva fàbula planteja una complexitat moral i la moral no és simplista, però és explícita. He revisat que l'arquetip sigui consistent tot i tenir matisos."

### C1+ — Crític


