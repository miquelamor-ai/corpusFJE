---
modul: M3
titol: "Escriure/adaptar una entrevista"
tipus: genere-discursiu
categoria_principal: generes
categories_secundaries: []
descripcio: "Instrument per adaptar o generar una entrevista: gènere dialogat d'informació amb format pregunta/resposta invariant, presentació de l'entrevistat, i primera persona a les respostes. HCL Descriure (qui és l'entrevistat i quines idees defensa) + Argumentar (B1+). No s'adapta a pre-A1. Rúbrica gradada 7 passos × 5 nivells MECR (A1→C1)."
mecr_range: [A1, A2, B1, B2, C1]
agent_roles: [adapter, generator]
genre_key: entrevista
translanguaging: false
multimodal: false
moduls_relacionats: [M3]
variables_configurables:
  fase_lectora: [alfabetica_emergent, alfabetica_fluida]
skill_meta: write-entrevista@corpusFJE/skills/generes/write-entrevista
review_status: pilot-fusio-5
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, fidelitat-gradada-C2, variabilitat-cardinal-passos-D3]
  aplicades_post_review: [hcl-narrar-eliminat-principal, c1-parells-llindar-profunditat, pas3-falsos-positius-i-enum]
  comentari_key: "L'entrevista és el gènere dialogat d'informació per excel·lència; la distinció amb el gènere narratiu és clau per a la correcta assignació d'HCL."
---

# Escriure/adaptar una entrevista

## Descripció

L'entrevista és un gènere dialogat d'informació: una persona (entrevistador) pregunta i una altra (entrevistat) respon. El seu tret definitori és el **format P/R invariant**: la seqüència pregunta-resposta s'ha de mantenir sempre com a parells atribuïts i mai no es pot convertir en prosa narrativa. L'etiqueta visible (**P:** / **R:**) és el marcador gràfic del gènere.

**Tipologia MALL**: Dialogada/Informativa.
**HCL principal**: Descriure — qui és l'entrevistat i quines idees defensa.
**HCL secundàries**: Argumentar — quan l'entrevistat defensa una postura (B1+).
**No s'adapta a pre-A1**: l'entrevista requereix la comprensió de la **seqüència P/R com a relació dialogada**: entendre que "P:" i "R:" son torns de paraula atribuïts a persones different, i que una pregunta espera una resposta de la mateixa persona. Aquesta abstracció de relació dialogada i lectura d'etiquetes semàntiques no és accessible sense base lecto-escriptora mínima. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Format P/R com a seqüència conversacional*: l'entrevista és la representació escrita de la conversa pregunta-resposta, la seqüència d'adjacència més bàsica de la interacció. Treballar-la entrena la comprensió del torn de paraula i la relació entre interlocutors, que és la base de tota literacitat dialògica.
- *La pregunta com a eina cognitiva*: formular preguntes precises d'una sola idea és una competència de pensament crític. Diferenciar preguntes obertes, tancades, múltiples i retòriques és un aprenentatge metalingüístic transferible a totes les matèries.
- *HCL Argumentar en context accessible*: quan l'entrevistat defensa una postura, l'alumne veu la HCL Argumentar en acció dins d'un format accessible. L'entrevista és el pont entre la descripció (qui és) i l'assaig (per què ho defensa).

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu l'**entrevista adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Principi general

**Regla de selecció simple.** Genera o adapta el text com a entrevista en format pregunta/resposta invariant, amb les etiquetes literals **P:** i **R:** en negreta, presentació inicial de l'entrevistat i respostes sempre en primera persona; nombre de parells P/R segons llindar de nivell MECR (3-4 a A1, fins a 7-10 a C1).

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix si l'entrevistat triat és pedagògicament rellevant, si la postura defensada és adequada a l'aula, ni si la fidelitat a la veu original és prou autèntica; aquestes valoracions les fa el docent. El LLM tampoc no avalua nivell MECR de l'alumne ni assigna fase lectora: rep el nivell i la fase com a paràmetres d'entrada.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### fase_lectora_alfabetica_emergent

**Inclou si:**
- A1 amb llindar inferior: 3 parells P/R
- presentació d'1 frase
- preguntes de 1-2 paraules clau o frase simple
- respostes de 1-2 frases en 1a persona

**Exclou explícitament:**
- termes tècnics sense explicació immediata

**Raonament pedagògic.** A fase emergent, la lectura encara consumeix recursos cognitius elevats; reduir el nombre de parells i la càrrega lèxica preserva l'accés al gènere sense saturar la descodificació (MALL: lectura assequible com a porta d'entrada al format dialogat).

### fase_lectora_alfabetica_fluida

**Inclou si:**
- A1 amb llindar superior: 4 parells P/R
- presentació fins a 2 frases
- possible 1 terme tècnic amb explicació entre parèntesi

**Exclou explícitament:**
- termes tècnics sense explicació immediata a A1

**Raonament pedagògic.** Amb descodificació fluida, l'alumne pot sostenir un parell P/R addicional i una presentació més rica; la resta de la taula Modulació s'aplica directament per nivell MECR.

### agent_role_adapter

**Inclou si:**
- treball sobre text font
- preservació de les idees principals
- preservació del format P/R i veu original de l'entrevistat
- activació del descriptor cross_source (Pas 6.3 Fidelitat)

**Exclou explícitament:**
- invenció d'idees no presents al text font

**Raonament pedagògic.** En mode adaptador la veu de l'entrevistat és patrimoni del text font; la fidelitat és el criteri de qualitat (decisió canònica Fase B: adaptació no és reescriptura).

### agent_role_generator

**Inclou si:**
- creació d'entrevista ex novo a partir d'un perfil d'entrevistat proposat pel docent
- coherència interna del personatge com a substitut de la fidelitat

**Exclou explícitament:**
- activació de cross_source (no hi ha text font)

**Raonament pedagògic.** En mode generador la fidelitat externa no aplica; la qualitat es valida per consistència interna del personatge i adequació al perfil declarat pel docent.

## Detecció

**Senyals docent** (quan adaptar a entrevista):
- El text font és una entrevista publicada a una revista, diari o plataforma digital.
- La unitat vol apropar una figura (científica, artística, esportiva, històrica) a l'alumnat a través de les seves paraules.
- L'activitat preveu que l'alumne produeixi una entrevista com a tasca (entrevistar un company, un familiar, un expert local).
- L'objectiu inclou treballar la formulació de preguntes com a competència cognitiva.

**Senyals alumne** (que indica que necessita bastida):
- Converteix les respostes en tercera persona ("va dir que estava content" en lloc de "Estic content").
- Barreja preguntes i respostes sense etiquetar.
- Fa preguntes múltiples en una sola intervenció ("Com et dius i qué fas i d'on ets?").
- Perd la veu de l'entrevistat al transformar-la.
- Linealitza: converteix l'entrevista en prosa narrativa.

**Context favorable**:
- Llengua i Literatura: entrevistes a autors o personatges literaris.
- Ciències Socials: personatges històrics o contemporanis.
- Ciències: científics, investigadors o divulgadors.
- Arts: artistes, músics o esportistes.
- Alumnat nouvingut A1-A2: l'entrevista és el gènere que permet escoltar la veu d'algú en primera persona sense la complexitat de la narració literària.

**Anti-senyals** (quan NO adaptar a entrevista):
- El text informatiu sobre una persona no té format dialogat → biografia o entrada enciclopèdica.
- El text és un debat entre dues persones amb postures oposades → cartes conversacionals o assaig.
- Pre-A1: la comprensió de torns atribuïts i etiquetes semàntiques no és accessible sense base lingüística.

## Modulació per nivell

| Pas | Dimensió | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1<br>Crític |
|---|---|---|---|---|---|---|
| **1. Presentació de l'entrevistat** | Context i rellevància | 1 frase: qui és i per qué. | 2 frases: qui és i per qué és rellevant entrevistar-lo. | 3-4 frases de context professional o personal que justifiquen l'entrevista. | Presentació completa amb context social o professional. | Presentació que situa l'entrevistat en el seu camp i dona el marc de l'entrevista. |
| **2. Format P/R (etiquetes)** | Consistència gràfica | **P:** i **R:** en negreta. Consistent en tot el text. | **P:** i **R:** en negreta. Format perfectament consistent. | **P:** i **R:** en negreta. Cap ambigüitat sobre qui parla en cap moment. | **P:** i **R:** en negreta. La veu de l'entrevistat és lingüísticament diferenciable de la del periodista. | **P:** i **R:** en negreta. La diferència de registre i veu entre entrevistador i entrevistat és evident. |
| **3. Preguntes directes (1 sola idea)** | Precisió i focus | Preguntes de 1-2 paraules clau o 1 frase simple ("Qué fas?", "On vius?"). | Preguntes directes d'una sola idea. Sense preguntes dobles ni retòriques. | Preguntes d'una idea que exploren un aspecte concret. Sense preguntes retòriques. | Preguntes que conviden a defensar posicions o explicar processos complexos. | Preguntes que qüestionen, matisen o aprofundeixen. Pot incloure preguntes de seguiment. |
| **4. Respostes en 1a persona** | Veu i autenticitat | Respostes de 1-2 frases en primera persona. | Respostes de 2-3 frases. Primera persona consistent. Cap transformació a 3a persona. | Respostes de 3-4 frases amb matís. Veu de l'entrevistat preservada i recognoscible. | Respostes que mostren el punt de vista de l'entrevistat amb arguments i evidències. | Respostes que mostren la complexitat de la postura. Pot incloure matisos i contradiccions. |
| **5. Nombre de parells P/R** | Extensió i cobertura | 3-4 parells P/R. | 4-5 parells P/R. | 5-6 parells P/R. | 6-7 parells P/R. Pot incloure 1 pregunta de seguiment. | 7-10 parells P/R. Moments de tensió dialèctica quan el tema ho permet. La profunditat de cada rèplica és més rellevant que el nombre total. |
| **6. Criteris transversals** | Termes tècnics de l'entrevistat | Sense termes tècnics (o amb explicació immediata entre parèntesi). | 1 terme tècnic màxim, explicat entre parèntesi o al costat. | Termes tècnics explicats entre claudàtors [terme: significat] o en nota al final. | Termes tècnics explicats naturalment dins del text. | Termes tècnics integrats; glossari al final si hi ha molts. |
|  | No linearitzar | Cap frase de transició narrativa entre P/R ("l'entrevistat va contestar que..."). Format P/R pur. | Idem. | Idem. | Idem. | Idem. Pot incloure una nota editorial breu entre claudàtors [nota de la redacció] si és rellevant. |
|  | Fidelitat al text font | Fidelitat a les idees principals de l'entrevistat i al format P/R. | Fidelitat a les idees, al registre bàsic i al format. | Fidelitat a les idees, al registre, a la veu de l'entrevistat i al format. | Fidelitat a la complexitat de les idees i al to de l'entrevistat. | Fidelitat a la complexitat, al to, als matisos i als moments de tensió del text original. |
| **7. Autoavaluació metacognitiva** | Reflexió sobre el procés | "He escrit qui és l'entrevistat. He escrit 3-4 preguntes i respostes marcades amb P i R." | "Cada pregunta té una sola idea. Les respostes son en primera persona." | "Les meves preguntes exploren aspectes interessants. He explicat els termes difícils." | "L'entrevistat defensa una postura clara. He fet preguntes de seguiment." | "L'entrevista mostra la complexitat de les idees de l'entrevistat. He revisat que no hi hagi linearització." |

## Casos especials

### no_aplica_preA1

**Trigger:** mecr_in: [pre-A1] OR fase_lectora_in: [logografica]

**Modulació:**
- skill_no_executat: true
- missatge_docent: "L'entrevista requereix base lecto-escriptora mínima (comprensió de torns atribuïts P:/R: i etiquetes semàntiques). Per a pre-A1 / fase logogràfica, usar un altre gènere (p.e. descripció amb pictogrames). Decisió canònica Fase B."

**Raonament pedagògic.** La comprensió de torns atribuïts i etiquetes semàntiques requereix base lecto-escriptora; sense ella, el format P/R es perd com a marcador del gènere i l'instrument deixa de ser pedagògicament viable. Decisió canònica Fase B documentada al frontmatter.

### argumentar_activat_B1_plus

**Trigger:** mecr_in: [B1, B2, C1] AND entrevistat_defensa_postura: true

**Modulació:**
- hcl_secundaria_argumentar: activa a les respostes
- B1: l'entrevistat justifica la postura amb 1-2 raons
- B2: arguments i evidències
- C1: matisos i contradiccions assumides
- B2-C1: incloure 1 pregunta de seguiment que aprofundeixi la postura

**Raonament pedagògic.** Quan l'entrevistat defensa una postura, l'entrevista esdevé pont entre Descriure i Argumentar (MALL). Activar Argumentar a partir de B1 permet treballar la HCL secundària en un format dialogat accessible, sense exigir l'estructura formal de l'assaig.

### DUA_acces

**Trigger:** dua_equals: Acces

**Modulació:**
- nombre_parells_PR: llindar inferior del nivell (p.e. 3 a A1 en lloc de 4)
- presentacio_max_frases: 1
- termes_tecnics: zero o explicació immediata entre parèntesi
- respostes_max_frases: 1-2

**Raonament pedagògic.** El principi DUA d'Accés demana reduir la càrrega cognitiva no essencial al gènere. Mantenir el format P/R com a marcador identificatiu i alleugerir la resta (nombre de parells, presentació, lèxic) preserva l'essència de l'entrevista sense crear barrera d'entrada.

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
| 1 Presentació — Context i rellevància | `qualitative` + `countable` | no | comptar frases de presentació; LLM-jutge sobre suficiència del context per al nivell |
| 2 Format P/R — Consistència gràfica | `binary` | no | regex: presència de "**P:**" i "**R:**" (o "P:" / "R:") de manera consistent; detectar parells sense etiqueta |
| 3 Preguntes directes — Precisió | `binary` + `qualitative` | no | binary: detectar preguntes dobles (connector "i" entre dos verbs o clàusules interrogatives, no en enumeracions nominals — "Qué fas i on treballes?" sí és doble; "Qué en penses del grup i del seu estil?" no ho és); qualitative: LLM-jutge sobre focus i no-retòriques |
| 4 Respostes 1a persona — Veu | `binary` + `qualitative` | no | binary: detectar transformació a 3a persona ("va dir que..."); qualitative: LLM-jutge sobre autenticitat de veu |
| 5 Nombre de parells P/R — Extensió | `countable` | no | comptar parells P/R; verificar llindar per nivell |
| 6.1 Criteris — Termes tècnics | `binary` + `qualitative` | no | binary: presència de termes sense explicació a A1-A2; qualitative: adequació de l'explicació per a cada terme |
| 6.2 Criteris — No linearitzar | `binary` | no | detectar frases narratives de transició entre P/R ("va respondre que", "l'entrevistat va explicar que"); regex sobre patrons de discurs indirecte |
| 6.3 Criteris — Fidelitat al text font | `cross_source` + `qualitative` | **sí** (si adaptació) | comparar idees principals de l'entrevistat, format P/R i veu original vs adaptats |
| 7 Autoavaluació metacognitiva | `metacognitive` | no | derivar a vista d'autoavaluació alumne + registre docent |

**Notes:**
- Format P/R (Pas 2) és el descriptor més automatitzable del corpus d'entrevista: binary pur per regex sobre la presència consistent de "P:" i "R:".
- No linearitzar (Pas 6.2): detectable per patrons de discurs indirecte ("va dir que", "va respondre que", "l'entrevistat va explicar que") que indiquen que les respostes s'han convertit en narració.
- Preguntes dobles (Pas 3): detectables per la presència de connectors coordinants ("i", "o") dins d'una mateixa pregunta seguida de signe d'interrogació.

## Heurístiques docent

**H1 — Preparar les preguntes primer.**
Proposo que l'alumne prepari les preguntes en un full separat ABANS de fer (o escriure) l'entrevista. Les preguntes han de cobrir: qui és, qué fa, per qué ho fa, qué ha après, qué recomanaria. Amb 5 preguntes cobertes, l'entrevista té estructura. Evita el bloqueig de "no sé qué preguntar".

**H2 — El test de la pregunta única.**
Quan l'alumne escriu una pregunta doble, la llegeixo en veu alta i li pregunto: "Quantes preguntes has fet?" Si n'hi ha més d'una, cal dividir. Funciona com a autocorrecció immediata des de A2. La versió escrita: cada pregunta ha de tenir un sol signe d'interrogació i no ha de contenir la conjunció "i" en posició interrogativa.

**H3 — "Parla en nom teu, no en nom d'altri".**
Quan l'alumne converteix les respostes en tercera persona ("Va dir que estava content"), li demano: "Ara fes que l'entrevistat parli directament a mi." La transformació de 3a a 1a persona és un exercici de perspectiva i de preservació de la veu. Funciona com a bastida per a la comprensió del discurs directe.

**H4 — L'entrevista oral com a bastida (A1-A2).**
Per a les primeres entrevistes, proposo una entrevista real en parelles a l'aula: un fa de periodista, l'altre d'entrevistat. Primer oral, després escriure els torns. El format P/R neix de manera natural de l'experiència viscuda i es trasllada a l'escriptura amb menys resistència.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Entrevista
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
cap (no s'usen H3; el cos és una presentació en prosa seguida de parells P/R consecutius)
```

**Bullets / moments interns** (si aplica — NO son H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
**P:**
**R:**
```

**Headers explícitament PROHIBITS:**
```
## Preguntes
## Respostes
## Presentació
### Pregunta 1
### Resposta 1
```

**Regla d'integritat estructural.** Tot el cos sota un únic H2 `## Entrevista`. Presentació en prosa inicial sense subheader. Parells P/R consecutius amb `**P:**`/`**R:**` literals a inici de línia. Sense H3 ni transicions narratives. Sense aquests marcadors, el parser de pas3.html no detecta el gènere i el descriptor binari del Pas 2 (regex sobre `**P:**`/`**R:**`) falla.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): HCL Descriure + Narrar + Argumentar, gènere dialogat d'informació.
- Sacks, H., Schegloff, E. i Jefferson, G. (1974): "A Simplest Systematics for the Organization of Turn-Taking for Conversation" — seqüències d'adjacència i torns de paraula; base teòrica del format P/R.
- Decret 175/2022 (currículum Catalunya): competència en comunicació oral i escrita, gèneres discursius dialogats.
