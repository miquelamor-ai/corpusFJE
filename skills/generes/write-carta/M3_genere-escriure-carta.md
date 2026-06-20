---
modul: M3
titol: "Escriure/adaptar una carta"
tipus: genere-discursiu
categoria_principal: generes
categories_secundaries: []
descripcio: "Instrument per adaptar o generar una carta formal o informal: estructura de 7 parts (encapçalament-salutació-motiu-cos-petició-comiat-signatura), motiu al primer paràgraf, una sola petició i registre ajustat al destinatari. HCL Justificar (formal, B1+) + Narrar+Descriure (informal, A1-A2). Translanguaging admès a A1-A2 (carta informal, expressions L1 entre claudàtors). No s'adapta a pre-A1. Rúbrica gradada 7 passos × 5 nivells MECR (A1→C1)."
mecr_range: [A1, A2, B1, B2, C1]
agent_roles: [adapter, generator]
genre_key: carta
macro_tipologia: conversacional
label_ca: "Carta"
translanguaging: true
multimodal: false
moduls_relacionats: [M3]
variables_configurables:
  fase_lectora: [alfabetica_emergent, alfabetica_fluida]
skill_meta: write-carta@corpusFJE/skills/generes/write-carta
review_status: pilot-fusio-5
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, fidelitat-gradada-C2, variabilitat-cardinal-passos-D3]
  aplicades_post_review: [pas3-afegir-qualitative]
  comentari_key: "La carta és el gènere de comunicació formal per excel·lència: el motiu al primer paràgraf i la petició única son les competències comunicatives acadèmiques més transferibles."
---

# Escriure/adaptar una carta

## Descripció

La carta és un text comunicatiu adreçat a un **destinatari específic** amb estructura convencional de 7 parts. El seu tret definitori és la doble exigència: el **motiu al primer paràgraf** (sense preàmbuls) i la **única petició per carta** (una demanda, una acció esperada del destinatari). El registre —formal o informal— és determinat exclusivament per la relació entre remitent i destinatari i ha de ser consistent en tot el text.

**Tipologia MALL**: Argumentativa/Comunicativa (carta formal) · Expressiva/Narrativa (carta informal).
**HCL principal**: Justificar — carta formal B1+: argumentar la petició amb raons ordenades · Narrar+Descriure — carta informal A1-A2: explicar la situació i demanar de forma directa.
**HCL secundàries**: Argumentar (anticipació d'objeccions, B2+) · Persuadir retòricament (C1).
**No s'adapta a pre-A1**: la carta requereix la comprensió del **destinatari com a constructor de registre** — saber que "Hola" vs "Benvolgut" depèn de la relació social és una abstracció sociolingüística que requereix comprensió del context comunicatiu com a variació conscient. (Decisió 6 canònica Fase B.)
**Translanguaging (A1-A2)**: la carta personal (informal) a A1-A2 pot incloure expressions en L1 entre claudàtors si l'alumne no troba el mot en llengua de destinació. El docent valora el contingut separat de la forma. No s'aplica a la carta formal.

**Connexions MALL transversals:**
- *Registre com a competència sociolingüística*: saber quan usar "tu" o "vostè", "Hola" o "Benvolgut", és una competència de relació social visible i avaluable. La carta és el gènere on la variació de registre és més explícita i on l'error de registre té conseqüències comunicatives reals.
- *El motiu al primer paràgraf com a claredat comunicativa*: comunicar el propòsit de manera directa és una competència professional i acadèmica transferible a correus electrònics, instàncies i sol·licituds. La carta ensenya a evitar les introduccions que retarden el missatge.
- *Una sola petició com a focus comunicatiu*: la regla "una carta = una petició" és una heurística de comunicació formal exportable a totes les situacions professionals. L'alumne que aprèn a no acumular demandes aprèn a pensar comunicativament amb focus: saber quin és el "desig principal" és una competència de síntesi i priorització.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **carta adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Principi general

**Regla de selecció simple.** Adapta o genera una carta amb estructura de 7 parts (encapçalament, salutació, motiu, cos, petició, comiat, signatura), posant el motiu al primer paràgraf, formulant una sola petició i mantenint un registre (formal o informal) consistent i ajustat al destinatari. Inclou la rúbrica gradada A1→C1 per als 7 passos.

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix la relació social entre remitent i destinatari ni si la petició és pedagògicament adequada: aplica el registre i el motiu que el text font o el docent indiquen. Tampoc valora autònomament la pertinença d'expressions en L1 (translanguaging A1-A2 carta informal): les preserva entre claudàtors si apareixen. La decisió final sobre adequació sociolingüística la pren el docent.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### nouvingut_L1_carta_informal

**Inclou si:**
- Activar translanguaging amb marcador [L1: ...] per al cos i la petició
- Mantenir salutació i comiat sempre en llengua de destinació com a ancoratge formal

**Exclou explícitament:**
- L1 a salutació o comiat (han de mantenir-se en llengua de destinació)

**Raonament pedagògic.** Per al nouvingut amb L1 declarada en carta informal A1-A2, el translanguaging admet expressions en L1 quan l'alumne no troba el mot en llengua de destinació: el contingut comunicatiu es valora separat de la forma (MALL, Cummins translanguaging). Salutació i comiat es mantenen en llengua meta com a ancoratge formal del gènere.

### registre_formal_B1_plus

**Inclou si:**
- Tractament 'vostè' consistent
- Comiat protocol·lari ('Atentament', 'Salutacions cordials')

**Exclou explícitament:**
- Expressions col·loquials
- Translanguaging (marcadors [L1: ...])

**Raonament pedagògic.** A B1+ la carta formal exigeix competència sociolingüística plena: el registre formal és inequívoc i no admet barreja amb col·loquialismes ni amb L1, perquè el destinatari institucional avalua adequació al protocol (Hymes, competència comunicativa).

### registre_informal

**Inclou si:**
- Tractament 'tu' consistent
- Salutació i comiat afectius adequats a la relació

**Exclou explícitament:**
- Fórmules arcaiques encara que el text font les contingui (s'actualitzen)

**Raonament pedagògic.** El registre informal exigeix coherència de tractament i fórmules contemporànies; les fórmules arcaiques del text font s'actualitzen perquè la carta serveix la comunicació real, no la reproducció històrica.

## Detecció

**Senyals docent** (quan adaptar a carta):
- El text font és una carta (formal o informal) que cal simplificar o adaptar al nivell.
- La unitat treballa la comunicació escrita amb propòsit real: demanar, queixar-se, agrair, presentar-se, informar.
- L'alumne ha de llegir per comprendre com s'adapta la forma al destinatari i al registre.
- El context TILC requereix que l'alumne aprengui a comunicar-se formalment (sol·licitud, reclamació, carta de presentació).

**Senyals alumne** (que indica que necessita bastida):
- Posa el motiu al final de la carta en lloc del principi.
- No distingeix el registre: tuteja una institució o usa fórmules massa formals amb un amic.
- Fa múltiples peticions en una mateixa carta.
- No sap com cloure la carta: repeteix la petició o acaba bruscament sense comiat.
- Usa fórmules arcaiques ("En prego acceptació de les més distingides salutacions") o barreja d'èpoques.

**Context favorable**:
- Llengua i Literatura: carta literària, carta a un autor, carta d'un personatge a un altre.
- Ciències Socials: carta a un personatge històric, carta a una institució.
- Educació per a la Ciutadania: sol·licitud formal, queixa a l'ajuntament, carta de reclamació.
- Orientació i Emprenedoria: carta de presentació, carta de motivació.
- Alumnat nouvingut A1-A2: la carta informal a un amic o familiar és un dels primers usos comunicatius autèntics en llengua nova; el translanguaging permet expressar el contingut mentre s'aprèn la forma.

**Anti-senyals** (quan NO adaptar a carta):
- El text és adreçat a un lector general, no a un destinatari específic → article d'opinió o assaig.
- El text és íntim i no vol comunicar a un destinatari extern → diari.
- El text debat posicions oposades sense destinatari concret → assaig argumentatiu.
- Pre-A1: la comprensió del destinatari com a constructor de registre no és accessible sense base lingüística.

## Modulació per nivell

| Pas | Dimensió | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1<br>Crític |
|---|---|---|---|---|---|---|
| **1. Encapçalament** | Format i completitud | Lloc i data en format simple: "Barcelona, 12 de maig". | Lloc, data i nom del destinatari complets. | Encapçalament complet: lloc, data, nom i adreça del destinatari (carta formal). | Encapçalament complet i ben formatat. Referència o assumpte si escau. | Encapçalament professional complet. Pot incloure referència, assumpte i número d'expedient. |
| **2. Salutació** | Registre i adequació | "Hola [nom]," (informal) / "Estimat/da [nom]:" (formal molt simple). | Salutació ajustada al registre: informal (amic/família) / formal (autoritat/desconegut). | Salutació formal precisa: "Benvolgut/da senyor/a [cognom]:" sense errors de tractament. | Salutació formal amb tractament correcte i consistent amb el to de la carta. | Salutació formal o protocol·lària si el context ho exigeix. Tractament perfectament ajustat. |
| **3. Motiu al primer paràgraf** | Claredat i posició | 1 frase que diu per qué s'escriu: "T'escric per..." Sense preàmbuls. | Motiu explícit al primer paràgraf. Directe i clar. Cap introducció sobre el benestar del destinatari. | Motiu presentat amb connector introductori: "Em dirigeixo a vostè per informar-lo/la que..." | Motiu presentat amb context breu i connector formal. El lector sap per qué s'escriu a la primera frase. | Motiu presentat amb precisió i context necessari per al destinatari. Pot incloure referència a una comunicació prèvia. |
| **4. Una sola petició** | Focus i concreció | 1 petició molt simple: "Et demano que..." Sense acumulació de demandes. | 1 petició clara i directa. Sense preguntes múltiples ni demandes encadenades. | Petició formulada amb justificació breu: "Li demano que... ja que..." | Petició argumentada: context + raó + demanda concreta. Anticipació possible: "Sóc conscient que..." | Petició amb argumentació elaborada i recursos de persuasió (empatia, reciprocitat). |
| **5. Registre** | Consistència i adequació | Informal (amic/família) o formal molt simple (desconegut). Consistent en tot el text. | Distinció clara entre formal i informal. Registre consistent. Cap barreja. | Registre formal o informal consistent. Vostè vs. tu ajustat al destinatari en tot el text. | Registre formal sofisticat. Cap expressió col·loquial a la carta formal. | Registre adaptat amb matisos de cortesia i protocol. El to és inequívocament professional o personal. |
| **6. Criteris transversals** | Comiat i signatura | "Fins aviat, [nom]." (informal) / "Salutacions, [nom]." (formal). Consistent amb la salutació. | Comiat ajustat al registre. Nom complet a la carta formal. | Comiat formal: "Atentament," / informal: "Una salutació,". Signatura completa (nom i cognoms). | Comiat protocol·lari adequat al registre i al to de la carta. | Comiat i signatura professionals. Pot incloure càrrec, institució o funció del remitent. |
|  | Fórmules arcaiques | Cap fórmula arcaica. Si apareix al text font, s'actualitza. | Idem. Cap fórmula arcaica ni expressió obsoleta. | Idem. Fórmules de cortesia contemporànies. | Idem. Pot usar fórmules formals però no antiquades. | Idem. Registre professional actual, sense arcaismes. |
|  | Fidelitat al text font | Fidelitat al motiu principal i al registre bàsic. | Fidelitat al motiu, al registre i a la petició essencial. | Fidelitat al motiu, al registre, a la petició i a l'estructura de 7 parts. | Fidelitat a la complexitat argumentativa i al to del remitent. | Fidelitat a la complexitat, al to i als recursos retòrics del text original. |
| **7. Autoavaluació metacognitiva** | Reflexió sobre el procés | "He escrit a qui va la carta i per qué. He fet una sola petició. He signat." | "He posat salutació i comiat adequats al destinatari. He dit el motiu al principi." | "He usat el registre correcte (formal/informal). He fet una sola petició amb justificació." | "La meva carta té context, petició argumentada i registre consistent de principi a fi." | "La meva carta és professional, ben estructurada i usa recursos de persuasió adequats al destinatari." |

## Casos especials

### translanguaging_A1_A2_informal

**Trigger:** mecr_in: [A1, A2] AND registre: informal AND nouvingut_L1: true

**Modulació:**
- admet_expressions_L1_entre_claudators: true
- marcador_inline: [L1: ...]
- valoracio_LLM_jutge: contingut_comunicatiu_separat_de_forma
- aplicar_a_carta_formal: false
- aplicar_a_B1_plus: false

**Raonament pedagògic.** Per al nouvingut amb L1 a carta informal A1-A2, el principi MALL de translanguaging permet expressar el contingut comunicatiu mentre s'aprèn la forma; les expressions L1 entre claudàtors no penalitzen la valoració. A carta formal o B1+, el registre esdevé competència sociolingüística plena i el translanguaging deixa de ser admissible.

### no_aplicable_preA1

**Trigger:** mecr_equals: pre-A1

**Modulació:**
- no_generar: true
- output_reemplacat_per: missatge_explicatiu
- missatge: "la carta requereix la comprensió del destinatari com a constructor de registre, una abstracció sociolingüística no accessible a pre-A1"
- derivar_a: generes_mes_basics (rètol, missatge curt)

**Raonament pedagògic.** Saber que "Hola" vs "Benvolgut" depèn de la relació social és una variació conscient del context comunicatiu (Hymes, competència comunicativa) que requereix una base lingüística mínima absent a pre-A1. Forçar la carta en aquest nivell genera reproducció mecànica sense competència real (Decisió 6 canònica Fase B).

### fase_lectora_alfabetica_emergent

**Trigger:** mecr_equals: A1 AND fase_lectora: alfabetica_emergent

**Modulació:**
- max_paraules_per_frase: 8-10
- estructura_7_parts_marcada_visualment: true (amb separadors)
- salutacio_comiat_tancats: escollir_entre_3_opcions_memoritzables_per_registre
- formula_peticio_fixa: "T'escric per..." + "Et demano que..."

**Raonament pedagògic.** A A1 amb fase lectora alfabètica emergent, l'alumne disposa de recursos descodificadors limitats: frases curtes, opcions tancades memoritzables i fórmules fixes redueixen la càrrega cognitiva i permeten focalitzar en l'estructura del gènere (H5 Heurística docent — tres comiats memoritzats resolen el 90% dels errors de tancament).

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
| 1 Encapçalament — Format | `structural` + `binary` | no | binary: encapçalament present; verificar completitud per nivell (lloc+data A1, + destinatari A2+, + adreça B1+); detectar absència d'encapçalament |
| 2 Salutació — Registre | `binary` + `qualitative` | no | binary: salutació present; qualitative: LLM-jutge sobre adequació del registre al destinatari (formal/informal) |
| 3 Motiu al primer paràgraf — Posició | `structural` + `binary` + `qualitative` | no | structural: detectar si el motiu apareix al primer paràgraf o al final; binary: motiu explícit present; qualitative: LLM-jutge sobre si la primera frase expressa realment el motiu o és una cortesia introductòria ("Espero que et trobis bé...") |
| 4 Una sola petició — Focus | `countable` + `binary` | no | comptar peticions (frases amb verbs de demanda: "demano", "sol·licito", "voldria que", "t'agradaria que"); binary: 1 sola petició compleix, 2+ no compleix |
| 5 Registre — Consistència | `binary` + `qualitative` | no | binary: registre consistent (detectar barreja tu/vostè, formal/col·loquial); qualitative: LLM-jutge sobre adequació del registre al destinatari |
| 6.1 Criteris — Comiat | `binary` + `qualitative` | no | binary: comiat present; qualitative: adequació del comiat al registre de la salutació |
| 6.2 Criteris — Signatura | `binary` | no | binary: signatura present; verificar nom complet a B1+ carta formal |
| 6.3 Criteris — Fórmules arcaiques | `binary` | no | regex: detectar fórmules arcaiques ("en prego acceptació", "distingides salutacions", "en espera de les vostres notícies", "molt atentament li saluda"); binary: absent compleix, present no compleix |
| 6.4 Criteris — Fidelitat al text font | `cross_source` + `qualitative` | **sí** (si adaptació) | comparar motiu, petició, registre i estructura original vs adaptats; LLM-jutge sobre preservació del to del remitent |
| 7 Autoavaluació metacognitiva | `metacognitive` | no | derivar a vista d'autoavaluació alumne + registre docent |

**Notes:**
- Motiu al primer paràgraf (Pas 3): és el descriptor de posició més crític de la carta i és detectable estructuralment. El motiu tardà és el principal error dels alumnes i requereix anàlisi de posició (primer paràgraf vs. últim) més que d'existència.
- Una sola petició (Pas 4): detectable per comptatge de verbs de demanda. Cas especial: una petició principal amb subcondicions ("demano que... i que...") és acceptable si el focus és un sol objectiu.
- Fórmules arcaiques (Pas 6.3): altament automatitzable per regex. La llista de fórmules obsoletes és finita i identificable.
- Translanguaging (A1-A2, carta informal): expressions en L1 entre claudàtors no es penalitzen al validador; el LLM-jutge valora el contingut comunicatiu independent de la llengua de les expressions.

## Heurístiques docent

**H1 — El destinatari primer.**
Antes d'escriure, proposo dues preguntes: "A qui escrius? Com el coneixes? Li dius 'tu' o 'vostè'?" Trenta segons. Si l'alumne no pot respondre, el registre de tota la carta serà incoherent. El destinatari és la clau de tot: determina salutació, comiat i to del cos.

**H2 — El motiu en una frase.**
Demano que l'alumne em digui en veu alta, en una frase, per qué escriu la carta. Si no pot, la carta no té motiu clar. La prova inversa: llegeixo el primer paràgraf i em pregunto "Sé per qué escriu?" Si no, el motiu no és prou explícit. A A1-A2, proposo completar la frase: "T'escric per..."

**H3 — La prova d'una sola petició.**
Llegeixo la carta de l'alumne i subratllo cada vegada que demana alguna cosa. Si n'hi ha més d'una, treballem quin és el "desig principal" i com integrar els altres de forma secundària o en una altra carta. La carta és un gènere de focus: una demanda, una acció esperada del destinatari.

**H4 — Registre: la salutació com a termòmetre.**
La salutació em diu tot. "Hola Pau" → informal. "Benvolgut senyor García" → formal. "Estimada Marta" → afectiu/familiar. Si la salutació no coincideix amb el to del cos, hi ha problema de registre. Corrijo sempre per la salutació primer: quan la salutació és coherent, la resta del text tendeix a alinear-s'hi.

**H5 — El comiat coherent.**
A A1-A2, els alumnes saben com acabar una conversa oral però no una carta. Proposo aprendre 3 comiats per registre: formal ("Atentament" / "Salutacions cordials"), semiformal ("Gràcies per la vostra atenció"), informal ("Fins aviat!" / "Una abraçada"). Tres comiats memoritzats resolen el 90% dels errors de tancament.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Carta adaptada
## Rúbrica de la carta
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
### 1. Encapçalament
### 2. Salutació
### 3. Motiu al primer paràgraf
### 4. Una sola petició
### 5. Registre
### 6. Criteris transversals (comiat, signatura, fórmules, fidelitat)
### 7. Autoavaluació metacognitiva
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
[L1: expressió_original]   <!-- només a A1-A2 carta informal amb nouvingut L1 -->
```

**Headers explícitament PROHIBITS:**
```
## Carta
## Rúbrica
```

**Regla d'integritat estructural.** Sense el header literal `## Carta adaptada` i la rúbrica gradada amb els 7 passos com a H3, el parser de pas3.html no pot ancorar els descriptors i la vista d'autoavaluació queda òrfena. El marcador [L1: ...] només s'usa a A1-A2 carta informal.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): HCL Justificar + Argumentar, adequació de registre al destinatari, gènere comunicatiu formal i informal.
- Hymes, D. (1972): "On Communicative Competence" — la competència comunicativa com a adequació al context social; el destinatari com a variable sociolingüística definitòria del registre.
- Briz, A. (1998): *El español coloquial en la conversación* — l'eix formal/informal en la comunicació escrita; variació de registre com a competència social (marc transferible al català).
- Decret 175/2022 (currículum Catalunya): competència en comunicació lingüística, gèneres discursius formals i informals.
