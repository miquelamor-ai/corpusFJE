---
modul: M3
titol: "Generar preguntes de comprensió"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: []
descripcio: "Instrument per generar preguntes de comprensió lectora seguint el model MALL 3 moments × 3 plànols cognitius (literal/inferencial/crític). Inclou pas d'acarament de llengues L1↔L2 per a nouvinguts. Pre-A1 sense escriptura autonoma: consignes d'accio. Maxim 10 preguntes totals. Rúbrica gradada 5 passos × 6 nivells MECR (pre-A1→C1)."
mecr_range: [pre_A1, A1, A2, B1, B2, C1]
agent_roles: [generator]
complement_key: preguntes_comprensio
translanguaging: true
multimodal: true
moduls_relacionats: [M2, M3]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: generate-preguntes-comprensio@corpusFJE/skills/mediacio/generate-preguntes-comprensio
review_status: pilot-fusio-8
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, variabilitat-cardinal-passos-D3, modulacio-per-perfil-D1]
  aplicades_post_review: [b9-preg-c1-cross-source-no-duplicar-bastides, b9-preg-c2-llindars-per-nivell-pas4, b9-preg-c3-inferencial-a1-reformulat]
  comentari_key: "C1-metadades-fila-cross-source-bastides-lectura-afegida; C2-llindars-preA1-6-A1-8-A2C1-10; C3-inferencial-A1-mot-clau-evidencia"
---

# Generar preguntes de comprensió

## Descripció

Les preguntes de comprensió lectora segueixen el **model MALL de 3 moments × 3 plànols cognitius**: les preguntes acompanyen l'alumne **Abans / Durant / Després** de la lectura, i treballen progressivament els plànols **literal → inferencial → crític**. El complement no és un examen final: és un **guió actiu de lectura** que estructura el procés de construcció de sentit.

**Tipologia MALL**: Mediació cognitiva (guia del procés lector).
**HCL principals**: Comprendre (literal, A1+) · Inferir (inferencial, A2+) · Valorar críticament (crític, B1+).
**HCL secundàries**: Predir (Abans de llegir, A1+) · Monitorar (Durant, A2+) · Crear/Imaginar (crític creatiu, pre-A1+).
**Principi rector**: *"Menys és més"* (MALL) — màxim 10 preguntes totals. 6-8 és l'òptim. Una pregunta inferencial ben construïda genera més aprenentatge que cinc de literals.

**Translanguaging — Pas d'acarament L1↔L2**: el complement inclou explícitament, per a alumnat nouvingut (A1-C1), una pregunta d'acarament de llengues que invita a activar la L1 com a recurs cognitiu. És la implementació directa del TOLC (Transfer of Literacy and Cognition, Cummins).

**Interacció intra-pipeline amb `bastides-lectura`**: si tots dos complements son actius simultàniament, les preguntes han de ser **ortogonals** a les bastides. `preguntes_comprensio` **guanya** amb prioritat de dedup: si un ítem és equivalent a un de les bastides, es replanteja la pregunta o s'elimina. La bastida dona el procediment (com llegir); la pregunta, el contingut (qué entendre). Patró cross_source intra-pipeline confirmat al corpus-spec v2.7 (mineraIRAG).

**Pre-A1 SÍ (D6)**: les "preguntes" a pre-A1 son consignes d'acció (assenyalar, dibuixar, dramatitzar, dictat a l'adult). Els 3 plànols cognitius son accessibles des d'infantil: el plànol crític s'introdueix oralment ("Qué hauries fet tu?"). Cap escriptura autònoma.

**Connexions MALL transversals:**
- *3 moments × 3 plànols*: el model MALL canònic estructura tant la seqüència temporal (avant/durant/après) com la profunditat cognitiva (literal/inferencial/crític). Les preguntes implementen explícitament aquesta bidimensionalitat.
- *Propòsit de lectura*: l'activació prèvia ("Llegeix per saber [X concret]") és el factor amb major impacte demostrat en la comprensió lectora. Sense propòsit, l'alumne llegeix sense construir sentit.
- *Acarament L1↔L2 (TOLC)*: la pregunta "Com es diu X en la teva llengua?" no és decorativa. Activa la xarxa semàntica en L1, que dona suport cognitiu a la comprensió en L2. Per a nouvinguts, l'acarament és la bastida conceptual més efectiva.
- *Multimodalitat*: a pre-A1 i A1, les consignes d'acció i les imatges substitueixen el text escrit. El repte cognitiu (inferir, valorar) no requereix producció escrita.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **preguntes que es generen per guiar la comprensió del text adaptat** (LECTURA ACTIVA). **No descriu l'avaluació del docent ni la producció autònoma de l'alumne**. El complement no és un examen: l'alumne usa les preguntes per llegir millor, no per ser avaluat.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → consignes d'assenyalar/dibuixar, mediació oral total. `fase_lectora: alfabetica_emergent` → consigna escrita simple, 1-2 paraules de resposta.

## Principi general

**Regla de selecció simple.** Genera entre 4 i 10 preguntes (o consignes d'acció a pre-A1) distribuïdes en els 3 moments MALL (Abans / Durant / Després) i, al moment "Després", cobrint els 3 plànols cognitius (literal, inferencial, crític). Inclou sempre un propòsit de lectura concret i específic del text font; si el perfil és nouvingut, inclou explícitament 1 pregunta d'acarament L1↔L2. Respecta el sostre per MECR: pre-A1 màxim 6, A1 màxim 8, A2-C1 màxim 10.

**Límits del LLM (no judici qualitatiu complex).** El LLM no ha de decidir si una pregunta inferencial concreta "genera més aprenentatge" que una altra, ni avaluar la maduresa cognitiva real de l'alumne, ni qualificar la qualitat literària del text font. Genera l'estructura de 3 moments × 3 plànols seguint la modulació per MECR i delega a qui ensenya la valoració pedagògica final (esborrar, reformular o substituir preguntes via la vàlvula humana al Pas 3).

_Excepcions: a pre-A1 les "preguntes" són consignes d'acció (assenyalar, dibuixar, dramatitzar, dictat a l'adult) i el plànol crític s'introdueix oralment ("Què hauries fet tu?"), sense escriptura autònoma._

## Regla de selecció per perfil

### alumne_general

**Inclou si:**
- preguntes_per_moment_MALL (Abans, Durant, Després)
- 3_planols_cognitius_al_moment_despres (literal, inferencial, crític)
- proposit_lectura_concret_i_especific
- sostre_max_segons_MECR (pre-A1: 6, A1: 8, A2-C1: 10)

**Exclou explícitament:**
- etiquetes_visibles_planol ([Literal]/[Inferencial]/[Crític])
- numeracio_1_2_3
- preguntes_copia_i_enganxa (resposta literalment copiable del text)

**Raonament pedagògic.** El model MALL canònic (3 moments × 3 plànols) estructura tant la seqüència temporal com la profunditat cognitiva. La invisibilitat de les etiquetes preserva la lectura activa: l'alumne no ha de saber el "tipus" de pregunta per respondre-la.

### alumne_nouvingut_amb_L1

**Inclou si:**
- preguntes_per_moment_MALL
- 3_planols_cognitius_al_moment_despres
- proposit_lectura_concret
- pregunta_acarament_L1_L2_obligatoria (com a mínim 1)

**Exclou explícitament:**
- formulacio_exposadora_de_la_L1 ("digues-ho en la teva llengua" sense alternativa)

**Raonament pedagògic.** TOLC (Cummins): la xarxa semàntica en L1 és la bastida conceptual més efectiva per a la comprensió en L2. Sense acarament, l'alumnat nouvingut llegeix sense ancoratge cognitiu. La formulació canònica és no-exposadora: "Si coneixes la paraula en una altra llengua, comparteix-ho si vols."

### alumne_AACC_o_capacitat_alta

**Inclou si:**
- planol_critic_i_inferencial_prioritzat
- preguntes_d_intencionalitat_autorial_i_intertextualitat (a B2-C1)

**Exclou explícitament:**
- saturacio_de_planol_literal (no superar 30% del total)

**Raonament pedagògic.** Per a AACC, mantenir sostre alt: el sostre de 10 preguntes es manté, però la composició es desplaça cap a inferencial i crític (sostre alt sense techo artificial). La decisió fina la pren qui ensenya via la vàlvula humana al Pas 3.

## Detecció

**Senyals docent** (quan activar el complement):
- Ha activat "Preguntes de comprensió" al Pas 2.
- El text adaptat és complex per al nivell de l'alumnat i cal guiar el processament actiu.
- L'alumnat llegeix passivament: llegeix les paraules però no construeix sentit.
- Cal demostrar comprensió per a una activitat posterior (debat, producció escrita, avaluació).
- La unitat és TILC on la comprensió del text és prerequisit per a l'aprenentatge del contingut.

**Senyals alumne** (que indica que necessita les preguntes):
- Llegeix el text sencer i quan li preguntes "De qué tracta?" respon "No sé" — lectura sense propòsit.
- Respon preguntes literals (copiables) però es queda en blanc davant "Per qué creus que...?" — *efecte mirall literal* (MALL).
- No pot predir de qué tractarà el text a partir del títol o les imatges.
- S'atura durant la lectura i no sap com continuar davant una frase difícil.

**Context favorable**:
- Text TILC on la comprensió és prerequisit per a l'activitat posterior (ciències, socials, tecnologia).
- Text literari on cal treballar la resposta estètica i afectiva.
- Grup amb 30%+ de comprensió lectora baixa (PIRLS Catalunya: 30.4% sota llindar mínim, 2021).

**Anti-senyals** (quan NO activar):
- Text molt curt (< 80 paraules) i comprensió immediata → discussió oral col·lectiva.
- El docent ja ha preparat les seves pròpies preguntes específiques.
- Temps de sessió molt limitat → 2-3 preguntes orals del docent basten.
- Preguntes de producció escrita creativa → `activitats-aprofundiment`.

## Modulació per nivell

| Pas | Dimensió | Pre-A1 Emergent | A1 Inicial | A2 Funcional | B1 Estratègic | B2 Acadèmic | C1 Crític |
|---|---|---|---|---|---|---|---|
| **1. Moment "Abans de llegir"** | Activació + propòsit | Adult estableix el propòsit en veu alta. Consigna de predicció visual: "Assenyala la imatge que creus que explica de qué va el text." | Activació: "Escriu 1 paraula sobre el que saps de [tema]." Propòsit: "Llegeix per saber [X concret]." | Activació: "Escriu 2-3 coses que saps sobre [tema]." Propòsit: "Llegeix per trobar [2 informacions concretes]." | Activació + 2 preguntes pròpies: "Qué saps? Qué et preguntes?" Propòsit: "Llegeix per entendre com [causa-efecte o seqüència]." | Activació del marc teòric o experiència prèvia. Propòsit d'avaluació: "Llegeix per avaluar si [afirmació] és vàlida." | Propòsit d'anàlisi autorial: "Llegeix per analitzar com l'autor construeix la seva postura i quines proves aporta." |
| **2. Moment "Durant la lectura"** | Aturada estratègica | Adult atura i pregunta: "Mostra'm on és [element del text]." Assenyalar o apuntar. | "Para a [punt]. Hi ha alguna paraula que no entens? Marca-la amb ?." | "Para a [punt]. Escriu en 1 frase el que ha passat fins ara." | "Para a [punt]. Quina hipòtesi tens sobre el que passarà o dirà a continuació?" | "Para a [punt]. Quina idea principal s'ha presentat fins ara? Com s'estructura argumentalment?" | "Para a [punt]. Quina és la postura de l'autor fins aquí? Quines proves ha aportat? N'hi ha d'absents?" |
| **3. Moment "Després de llegir"** | 3 plànols cognitius | Literal: "Assenyala la imatge de [element del text]" o "Dibuixa [element]." Inferencial: "Per qué creus que...?" (oral, mediat). Crític: "Qué hauries fet tu?" (oral). | Literal: V/F senzill o omple buit amb llista tancada. Inferencial: inferència mínima connectada a evidència visual o mot clau del text ("Per qué creus que [element]? Mira [part del text]"). Crític: oral o dibuix ("T'ha agradat? Dibuixa com t'has sentit"). | Literal: ordenar seqüències, relacionar amb fletxes. Inferencial: causa literal al text ("Per qué...? Busca-ho al text"). Crític: "Qué hauria passat si [canvi]?" Resposta breu. | Literal: 1-2 frases, resposta explícita al text. Inferencial: deducció relacional ("Quin efecte té [causa]? Argumenta-ho"). Crític: postura justificada (literari: sentiments; informatiu: fiabilitat de les dades). | Literal: resum de 3-5 frases amb jerarquització. Inferencial: justificació + referència al text. Crític: argumentació oberta + avaluació de la fiabilitat. | Literal: síntesi estructurada jerarquitzada. Inferencial: relacions implícites complexes, ironia, subtext. Crític: judici sobre intencionalitat, contrast amb fonts alternatives. |
| **4. Criteris transversals** | Format + modalitat + acarament | Consignes d'acció (mai V/F). Cap numeració: usar `-`. Cap etiqueta visible [Literal]. Màxim 6 consignes. | Mai V/F de frase complexa. Mai "copia i enganxa" (resposta copiable sense processament). Frases pregunta: màxim 10 paraules. Màxim 8 preguntes totals. LITERARI: "Qui és el personatge? Com se sent?" INFORMATIU: "Quina és la informació més important?" | Frases pregunta: màxim 12 paraules. Màxim 10 preguntes. LITERARI: pregunta afectiva. INFORMATIU: pregunta de precisió. Acarament L1 (si nouvingut): "Com es diu [terme clau] en la teva llengua?" | Frases pregunta: màxim 15 paraules. Màxim 10 preguntes. LITERARI: símbols i metàfores simples. INFORMATIU: jerarquitzar amb connectors. Acarament L1 (si nouvingut): "El text s'escriuria igual en la teva llengua?" | Màxim 10 preguntes. LITERARI: veu narrativa i intenció estètica. INFORMATIU: fiabilitat de les dades. Acarament L1 (si nouvingut): contrast d'argumentació entre català i L1. | Màxim 10 preguntes (prioritzar qualitat). LITERARI: intertextualitat i intencionalitat. INFORMATIU: contrast de fonts i biaix. Acarament L1 (si nouvingut): contrast metalingüístic i discursiu. |
| **5. Autoavaluació mediada** | Metacognició | "He assenyalat les imatges que m'ha demanat el mestre." (oral, mediat per adult) | "He respost si és vertader o fals. He omplert els buits." | "He ordenat les idees. He trobat la idea principal." | "He deduït informació que no estava explícita al text. He fet una hipòtesi durant la lectura." | "He argumentat les meves respostes amb referències al text. He avaluat si les dades eren fiables." | "He analitzat la intencionalitat de l'autor i he qüestionat les seves afirmacions. He contrastat amb el que ja sabia." |

## Casos especials

### pre_A1_fase_logografica

**Trigger:** mecr_in: [pre-A1] AND fase_lectora_in: [logografica]

**Modulació:**
- sostre_max_preguntes: 6
- format: consignes_accio_oral (assenyalar, dibuixar, dramatitzar, dictat a l'adult)
- escriptura_autonoma: false
- planol_critic: oral_mediat ("Què hauries fet tu?")
- prohibit: V/F, omplir buits, numeració

**Raonament pedagògic.** A la fase logogràfica l'alumne encara no descodifica autònomament; les "preguntes" han de ser accions observables mediades per l'adult. Els 3 plànols cognitius són accessibles oralment des d'infantil (MALL); el repte cognitiu no requereix producció escrita.

### pre_A1_fase_alfabetica_emergent

**Trigger:** mecr_in: [pre-A1] AND fase_lectora_in: [alfabetica_emergent]

**Modulació:**
- sostre_max_preguntes: 6
- format: consigna_escrita_simple_resposta_1_2_paraules
- escriptura_autonoma: minima
- prohibit: V/F de frase complexa, copia-i-enganxa

**Raonament pedagògic.** L'alumne comença a descodificar però la càrrega cognitiva de l'escriptura encara saturaria el processament del text; mantenim la resposta breu per protegir la comprensió.

### nouvingut_L1_acarament_obligatori

**Trigger:** nouvingut_L1: true AND mecr_in: [A1, A2, B1, B2, C1]

**Modulació:**
- acarament_L1_obligatori: true
- marcador_inline: [ACARAMENT_L1]
- formulacio_no_exposadora: "Si coneixes la paraula en una altra llengua, comparteix-ho si vols"
- progressio: A1-A2 traducció de terme clau; B1 contrast d'escriptura/estructura; B2 contrast d'argumentació; C1 contrast metalingüístic i discursiu

**Raonament pedagògic.** TOLC (Cummins): la xarxa semàntica en L1 és la bastida conceptual més efectiva per a la comprensió en L2; sense acarament, l'alumnat nouvingut llegeix sense ancoratge cognitiu. La formulació no-exposadora respecta l'agència de l'alumne.

### coexistencia_amb_bastides_lectura

**Trigger:** complement_actiu: bastides-lectura == true

**Modulació:**
- dedup_cross_source: true
- prioritat: preguntes_comprensio guanya
- accio_si_solapament: replanteja o elimina la pregunta duplicada
- separacio_funcional: bastida = procediment (com llegir), pregunta = contingut (què entendre)

**Raonament pedagògic.** Si els dos complements repeteixen el mateix ítem, l'alumne percep redundància i baixa l'engagement; la bastida ja resol el "com", les preguntes han de centrar-se en el "què" i el "per què". Patró cross_source intra-pipeline confirmat al corpus-spec v2.7.

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici huma o LLM-jutge.
- `countable` — llindar quantitatiu verificable mecanicament.
- `structural` — requereix analisi sintatica o discursiva.
- `metacognitive` — descriptor de proces en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Moment "Abans de llegir" | `binary` + `qualitative` | **si** | binary: presencia de pregunta d'activació + propòsit de lectura explícit; qualitative: LLM-jutge sobre si el propòsit és concret i específic del text font (positiu) o genèric "llegeix el text" (negatiu); cross_source |
| 2 Moment "Durant la lectura" | `binary` | no | binary: presencia d'almenys una aturada estratègica; detectar si la pregunta Durant és una repetició del Literals final (error) |
| 3 Moment "Després de llegir" | `structural` + `qualitative` | **si** | structural: presencia dels 3 plànols (literal+inferencial+crític) detectables per tipus de pregunta; qualitative: LLM-jutge sobre si les preguntes inferencials i crítiques son realment no-copiables del text (cross_source) |
| 4 Criteris transversals | `countable` + `binary` | no | countable: total de preguntes — pre-A1: ≤6 (consignes d'acció); A1: ≤8; A2-C1: ≤10; binary: absencia de etiquetes [Literal]/[Inferencial]; absencia de numeració; presencia d'acarament L1 si perfil nouvingut actiu |
| 4b No duplicar bastides-lectura | `cross_source` | **si** (output bastides-lectura si actiu) | comparar semànticament: cap pregunta de comprensió ha de coincidir amb un ítem de bastides-lectura; preguntes_comprensio guanya en cas de conflict — replanteja o elimina la pregunta duplicada |
| 5 Autoavaluació mediada | `metacognitive` | no | pre-A1: registre docent d'observació oral; A1+: derivar a vista d'autoavaluació de l'alumne |

**Notes:**
- Preguntes "copia i enganxa": detectar per LLM-jutge si la resposta pot copiar-se literalment del text sense processament. Error crític.
- Interacció intra-pipeline: si `bastides-lectura` i `preguntes_comprensio` son actius, verificar ortogonalitat (no duplicació). `preguntes_comprensio` guanya en cas de conflict.
- Acarament L1: detectar presencia de pregunta d'acarament si el perfil té `nouvingut: true`. Si absent = gap pedagògic (qualitative).
- Plànol crític a pre-A1: les consignes orals "Qué hauries fet tu?" son vàlides — no requereixen escriptura.

## Heurístiques docent

**H1 — La resposta "no sé" com a senyal d'alarma.**
Quan pregunto "De qué tracta el text?" i l'alumne respon "No sé", ha llegit sense propòsit. El Moment "Abans de llegir" és el més important: li dono un propòsit explícit ("Llegeix per saber [X concret]") i li pregunto el que ja sap del tema. Amb un propòsit, la comprensió millora notablement fins i tot sense canviar el text.

**H2 — Detectar el mirall literal.**
L'alumne respon correctament totes les preguntes literals però es queda en blanc davant "Per qué creus que...?" Introdueixo gradualment l'inferencial: primer amb inferències mínimes ("La resposta no és al text però sí al context"), progressivament amb major distància inferencial. El mirall literal s'identifica quan totes les respostes son frases del text lleugerament reformulades.

**H3 — El coneixement previ com a palanca.**
Per a textos sobre temes allunyats de l'experiència de l'alumne (ecosistemes de l'Àrtic, Revolució Industrial), el Moment "Abans de llegir" és crític. Sense ancoratge previ, les preguntes posteriors seran molt difícils. Dedico 5 minuts a activar coneixement previ (imatge, vídeo curt, 2 frases del docent) abans de distribuir el text.

**H4 — Text literari vs. informatiu: canvi de to.**
La primera pregunta après d'un text literari és sempre afectiva: "Com t'has sentit llegint-lo?" Per a un text informatiu, la primera és de precisió: "Quin és el fet o dada més important?" Aquesta distinció inicial marca el to de tota la sessió i evita que l'alumnat apliqui la mateixa estratègia a gèneres molt diferents.

**H5 — L'acarament L1↔L2 no és opcional per a nouvinguts.**
Quan treballo amb alumnat nouvingut, la pregunta d'acarament de llengues no és un extra: és la bastida conceptual més efectiva. "Com es diu [terme clau] en la teva llengua?" activa la xarxa semàntica en L1 i transfereix la comprensió cap al català. La consigna no exposa: "Si coneixes la paraula en una altra llengua, comparteix-ho si vols."

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Preguntes de comprensió
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
### Abans de llegir
### Durant la lectura
### Després de llegir
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
Dins de "### Després de llegir" els 3 plànols cognitius (literal, inferencial, crític) s'integren com a preguntes successives SENSE etiquetes visibles ni numeració.
```

**Marcadors inline obligatoris** (si aplica):
```
[ACARAMENT_L1]   <!-- només si nouvingut_L1: true, marca la pregunta d'acarament L1↔L2 -->
```

**Headers explícitament PROHIBITS:**
```
### Literal
### Inferencial
### Crític
### 1. Abans
### 2. Durant
### 3. Després
```

**Regla d'integritat estructural.** Sense els 3 H3 literals dins de `## Preguntes de comprensió`, el parser de pas3.html no segmenta els moments MALL. Etiquetes visibles `[Literal]`/`[Inferencial]`/`[Crític]` i numeració `1.`/`2.`/`3.` estan prohibides: trenquen la lectura activa (l'alumne no ha de saber el "tipus" de pregunta per respondre-la).

## Fonts principals

- MALL (Model d'Aprenentatge de Llengues i Literacitat): 3 moments × 3 plànols, propòsit de lectura, "menys és mes".
- Cummins, J. (2000): *Language, Power and Pedagogy* — CALP, BICS, TOLC (Transfer of Literacy and Cognition).
- Solé, I. (1992): *Estrategias de lectura* — estratègies de comprensió lectora; moments de lectura.
- PIRLS (2021): dades de comprensió lectora Catalunya (30.4% sota llindar mínim) — context del complement.
- Decret 175/2022 (curriculum Catalunya): competencia lectora i plurilingüisme.
