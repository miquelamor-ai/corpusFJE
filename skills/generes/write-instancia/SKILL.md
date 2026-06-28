---
name: write-instancia
description: 'Instrument per adaptar o generar una instància: document formal dirigit
  a una administració pública o institució per exposar fets i motius (bloc EXPOSA)
  i sol·licitar una acció concreta (bloc SOL·LICITA). HCL principal Argumentar + Justificar;
  HCL secundàries Explicar + Descriure. Invariant de gènere: estructura bipartida
  EXPOSA/SOL·LICITA, destinatari en majúscules, identificació completa del sol·licitant
  i tractament de vostè. Rúbrica gradada 8 passos × 3 nivells MECR (B1→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 1.1.0
tools_required: []
agent_role: adapter
genre_key: instancia
triggers:
- path: params.genere_discursiu
  equals: instancia
macro_tipologia: argumentativa
label_ca: Instància
mecr_range:
- B1
- B2
- C1
translanguaging: false
multimodal: false
moduls_relacionats:
- M3
- M9
font_canonic: M3_genere-escriure-instancia.md
font_version: 1.1.0
generat_at: '2026-06-28'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 8e2c49a289a2610f
---

# Escriure/adaptar una instància — skill operativa per a LLM

La instància és el **document formal per excel·lència de l'esfera administrativa i cívica**: un escrit dirigit a una administració pública o institució en què el sol·licitant **exposa uns fets i motius** (bloc EXPOSA) i **demana una acció concreta** (bloc SOL·LICITA). El MALL la identifica com a text legal/administratiu amb "convencions de carta formal molt marcades". A diferència de la carta personal o professional, la instància té un **destinatari necessàriament institucional** (alcalde/essa, rector/a, director/a de departament, cap de servei) i activa un marc legal i de drets que l'empara.

**Tipologia MALL (macro)**: Argumentativa + Instructiva. El gènere pertany a la macro-tipologia **Argumentativa** (exposa motius per convèncer l'administració) amb una dimensió **Instructiva** essencial (sol·licita una acció concreta i delimitable). Les dues tipologies coexisteixen en l'estructura bipartida del document: EXPOSA és el bloc argumentatiu; SOL·LICITA és el bloc instructiu.
**HCL principal**: Argumentar + Justificar — fonamentar la sol·licitud amb drets, fets i normes de manera que l'administració tingui motius suficients per atorgar-la.
**HCL secundàries**: Explicar (exposa la situació de manera ordenada i intel·ligible) i Descriure (les dades d'identificació del sol·licitant).
**Rang MECR**: B1–C1. La instància exigeix un mínim B1 per la complexitat formal i argumentativa: implica dominar fórmules fixes, estructurar un raonament i usar un registre formal consistentment. A pre-A1/A1/A2 no es treballa com a producció pròpia, però es pot llegir com a model amb bastida guiada.

**Connexions MALL transversals:**
- *Gènere de l'esfera pública i dels drets*: la instància és l'instrument primari de l'exercici de drets davant les administracions. Aprendre a escriure-la és aprendre a participar en la vida cívica.
- *Argumentació institucional*: a diferència de l'assaig (on l'argument és acadèmic) o de l'opinió (on és personal), la instància argumenta dins d'un marc legal i reglamentari. Els motius no son opinions: son fets verificables i, si escau, drets reconeguts per norma.
- *Fórmules fixades com a bastida*: les fórmules convencionals de la instància ("EXPOSA:", "Per tot l'anterior, SOL·LICITA:") no son restriccions arbitràries — son la bastida que permet a l'administrador identificar i processar la petició d'un sol·licitant. Aprendre-les és aprendre el codi del gènere.
- *Competència lingüística cívica*: la instància connecta directament amb la competència en comunicació lingüística del Decret 175/2022 i amb els objectius de formació per a la ciutadania activa. En contextos FP, sol ser la primera interacció real amb l'administració acadèmica.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **instància adaptada per a la LECTURA** de l'alumne (el model que llegeix/analitza) i la **generació guiada** amb bastida. A B1, el model fa servir fórmules fixades i estructura simplificada; l'alumne la pot llegir i imitar. A C1, la producció autònoma és l'objectiu final. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast cognitiu, amb la forma lingüística ajustada al seu nivell.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Encapçalament i identificació**
- Completesa i format: Nom complet + DNI/NIE + adreça en un bloc compacte. Format convencional simplificat: "Jo, [NOM], amb DNI/NIE [X], domiciliat/ada a [ADREÇA]".

**2. Destinatari**
- Formalitat del càrrec: Càrrec en majúscules al final del document: "AL/A LA [CÀRREC] DE [INSTITUCIÓ]". Càrrecs habituals del context educatiu o local.

**3. Bloc EXPOSA**
- Densitat i estructura argumentativa: 1 motiu clar exposat en 1-2 frases simples. Connector introductori: "Que". Fets verificables, no opinions.

**4. Referència normativa**
- Presència i precisió: Absent o molt breu si és evident ("d'acord amb la normativa vigent"). No és obligatòria a B1 però no penalitza si és simple.

**5. Bloc SOL·LICITA**
- Concreció i fórmula: Petició única, concreta i delimitable, precedida de "SOL·LICITA:" o "Per tot l'anterior, SOL·LICITA:". 1-2 frases màxim. Infinitiu o que + subjuntiu.

**6. Fórmula de comiat**
- Formalitat: Fórmula simple: "Cosa que espero em serà concedida."

**7. Data i signatura**
- Completesa: Lloc + data (dia, mes en lletres, any). Signatura (representada com a línia per a l'alumne).

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He separat clarament el que exposo del que demano?" "He escrit el nom, el DNI i l'adreça?"

### A1 — Inicial


**1. Encapçalament i identificació**
- Completesa i format: Bloc d'identificació complet amb totes les dades reglamentàries. Format administratiu rigorós.

**2. Destinatari**
- Formalitat del càrrec: Càrrec institucional precís. Si el destinatari immediat no és el màxim òrgan, s'adreça a qui té competència sobre la petició.

**3. Bloc EXPOSA**
- Densitat i estructura argumentativa: 2-3 motius exposats en paràgrafs numerats o en seqüència causal. Motius jerarquitzats: del més rellevant al més secundari. Connectors argumentatius ("en primer lloc", "a més a més", "per últim").

**4. Referència normativa**
- Presència i precisió: Referència normativa present i identificada: article + llei o decret + any. Breu però precisa ("a l'empara de l'article 14 de la Llei X/YYYY").

**5. Bloc SOL·LICITA**
- Concreció i fórmula: Petició principal + 1-2 peticions secundàries si escau (en ordre de preferència). Estructura clara: "1. Que se m'atorgui...; 2. Que se m'informi de...".

**6. Fórmula de comiat**
- Formalitat: Fórmula estàndard: "En espera de la vostra resolució favorable, us saludo atentament."

**7. Data i signatura**
- Completesa: Idem, amb format administratiu complet. Pot afegir "Signat:" abans de la signatura.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Els motius que exposo justifiquen la petició que faig? Segueixen un ordre lògic?"

### A2 — Funcional


**1. Encapçalament i identificació**
- Completesa i format: Bloc d'identificació complet. Si escau, títol professional o condició que reforça la legitimitat de la petició (qualitat de llicenciat/ada, de veí/na empadronat/da, de tutor/a legal).

**2. Destinatari**
- Formalitat del càrrec: Càrrec amb fórmula de tractament completa si el protocol ho exigeix ("Il·lm./Il·lma. Sr./Sra."). Coneixement del circuit administratiu: a qui s'adreça i per quins canals.

**3. Bloc EXPOSA**
- Densitat i estructura argumentativa: 3 o més motius elaborats, amb jerarquització lògica i anticipació d'objeccions. Pot incitar a la concepció de la legitimitat de la petició i la competència de l'organisme. Argumentació densa i cohesionada.

**4. Referència normativa**
- Presència i precisió: Citació legal precisa amb identificació de la norma, l'article i el seu contingut rellevant. Pot comparar normes o citar jurisprudència si escau. El LLM no valida si la norma és vigent; el docent revisa.

**5. Bloc SOL·LICITA**
- Concreció i fórmula: Petició principal amb condicions o terminis si el context ho requereix. Referència al procediment administratiu esperat (resolució, notificació, termini legal).

**6. Fórmula de comiat**
- Formalitat: Fórmula completa adaptada al context institucional. Pot incloure referència al procediment de notificació preferit.

**7. Data i signatura**
- Completesa: Idem. Si hi ha documentació adjunta (còpia del DNI, titulació, comprovant), s'anuncia amb "Adjunto la documentació següent:" al peu.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva argumentació és coherent i la petició és precisa i delimitable? He citat la norma correctament? He anticipat possibles objeccions?"

### B1 — Estratègic


### B2 — Acadèmic


### C1+ — Crític


