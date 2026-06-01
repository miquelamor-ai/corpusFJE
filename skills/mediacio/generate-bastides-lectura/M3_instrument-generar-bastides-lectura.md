---
modul: M3
titol: "Generar bastides de lectura"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: []
descripcio: "Instrument de mediació cognitiva que guia l'alumne als 3 moments del procés lector (Abans/Durant/Després) i als 3 plànols de comprensió (literal/inferencial/crític). Pre-A1 sempre gestual/oral. Rúbrica gradada 3 passos × 6 nivells MECR amb dimensions internes."
mecr_range: [pre-A1, A1, A2, B1, B2, C1]
agent_roles: [generator]
complement_key: bastides
translanguaging: false
multimodal: true
moduls_relacionats: [M2, M3]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: generate-bastides-lectura@corpusFJE/skills/mediacio/generate-bastides-lectura
review_status: pilot-fusio-4
version: 4.0.0-canonic
generat_at: 2026-05-25
actualitzat_at: 2026-05-25
notebooklm_review:
  data: 2026-05-25
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-noticia-glossari-opinio, fidelitat-gradada-C2, aclariment-us-lectura-vs-produccio-C1, metadades-cella, cas-especial-V2-compartit-V3-dedicat]
  aplicades_post_review: [C1-terminologia-frase-buit-A1-resum-i-autoavaluacio, C2-pausa-obligatoria-explicita-hipotesi-en-curs-B1plus]
  comentari_key: "Pilot 4 aporta la lògica de control intra-pipeline (descriptor cross_source dependent del pipeline) i consolida el model 3 moments × 3 plànols com a estàndard de mediació cognitiva ATNE. Quart pilot Fase A validat amb la mateixa estructura canònica."
  decisio_arquitectonica_mineriarag_20260525: "RESOLTA. Opció híbrida: (1) Prevenció per disseny — bastides llegeix l'output de preguntes_comprensio al moment de generació i produeix preguntes ortogonals (vygotskià). (2) Fallback dedup silenciós amb traça — si arriba duplicitat, ATNE dedupea amb regla de prioritat (preguntes_comprensio guanya, bastides es replanteja) + log a metadades. (3) NO warning runtime al docent (soroll sense valor accionable). Patró cross_source intra-pipeline confirmat com a patró canònic a corpus-spec v2.7 (mineriaRAG). Patró d'absència de fidelitat per a instruments d'orientació també confirmat al spec."
---

# Generar bastides de lectura

## Descripció

Les bastides de lectura són **suports temporals i retirables** que guien l'alumne als tres moments del procés lector (**Abans / Durant / Després**) i als tres plànols de comprensió (**literal / inferencial / crític**). El complement `bastides` les activa sempre que el docent vol estructurar el procés lector de l'alumne. La seva funció no és substituir el treball de comprensió detallat (això és tasca del complement `preguntes_comprensio`), sinó aportar el **procediment** (com llegir).

**Tipologia MALL**: Mediació cognitiva (bastida de lectura).
**HCL principal**: Mediar — orientar el procés lector amb suports retirables.
**HCL secundàries**: Predir (Abans, A1+) · Inferir (Durant/Després, A2+) · Valorar críticament (Després, B1+).
**Principi rector**: *"Menys és més"* — màxim 3 ítems per moment. Una bastida ben triada aporta més que deu ítems genèrics.

**Connexions MALL transversals:**
- *3 moments × 3 plànols*: el model MALL canònic estructura tant la seqüència temporal (avant/durant/après) com la profunditat cognitiva (literal/inferencial/crític). Aquest instrument els implementa explícitament.
- *Multimodalitat*: a pre-A1 totes les bastides són **físiques i gestuals** (assenyalar, dramatitzar, dibuixar). A A1, suport visual encara recomanat.
- *Bastida retirable (Vygotsky)*: la bastida té vocació d'extingir-se. El docent la introdueix les primeres 2-3 sessions i progressivament elimina els ítems que l'alumne ja fa sol. Una bastida que no es retira es converteix en dependència.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **bastides que ATNE o el docent presenten a l'alumne perquè llegeixi un text adaptat** (LECTURA). **No descriu la producció autònoma de l'alumne** — això és tasca del derivat propi (rúbrica d'avaluació formativa) i, si la tasca implica escriure, del pilot complementari `bastides-produccio`.
**Sub-granularitat dins de pre-A1 i A1**: es treballa amb la variable independent `fase_lectora` del frontmatter (logografica · alfabetica_emergent · alfabetica_fluida), no amb columnes addicionals.

## Principi general

**Regla de selecció simple.** Genera bastides organitzades en 3 moments del procés lector (Abans / Durant / Després), amb un màxim de 3 ítems per moment, modulades pel nivell MECR de l'alumne i, dins de pre-A1 / A1, per la variable `fase_lectora`. A pre-A1 totes les bastides són sempre gestuals/orals (zero lectura autònoma).

**Límits del LLM (no judici qualitatiu complex).** El LLM no ha de decidir si l'alumne ha internalitzat o no el procediment lector (això pertoca al docent: H1 'bastida que es retira'), ni ha de generar preguntes detallades de comprensió del text (això és tasca del complement `preguntes_comprensio`). El LLM produeix el procediment (com llegir), no la comprensió punt a punt; la valoració de l'oportunitat i la retirada progressiva la decideix qui ensenya.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### pre-A1

**Inclou si:**
- Bastides 100% gestuals/orals/visuals; l'adult llegeix en veu alta i l'alumne assenyala, dramatitza, dibuixa o ordena imatges. 1-2 accions per moment. No s'activen els plànols inferencial ni crític ni la hipòtesi en curs.

**Raonament pedagògic.** A fase logogràfica/emergent, la lectura autònoma encara no és viable; la bastida es realitza per via gestual-oral-visual perquè la imatge ancora el significat abans del codi escrit (MALL multimodal).

### A1

**Inclou si:**
- Bastides mínimes amb suport visual recomanat; 1 pregunta d'activació, predicció pel títol, frase-buit d'un sol forat al Moment Després. No inferència ni valoració crítica encara.

**Raonament pedagògic.** A A1 l'alumne comença a llegir amb mediació; la bastida ha de ser mínima per no saturar el processament i preservar la construcció inicial de sentit.

### A2

**Inclou si:**
- Lectura autònoma possible amb marcatge ✓/?/! al marge; 2 preguntes d'activació + ancoratge experiencial; s'obre el plànol inferencial guiat (1 pregunta).

**Raonament pedagògic.** A A2 emergeix la lectura autònoma funcional; la bastida desplaça el focus cap a la metacognició lectora bàsica (marcatge) i obre el plànol inferencial guiat.

### B1

**Inclou si:**
- Bastides estratègiques amb hipòtesi escrita pròpia (Abans), pausa obligatòria ⏸ amb hipòtesi en curs (Durant) i obertura del plànol crític (Després).

**Raonament pedagògic.** A B1 l'alumne pot anticipar i revisar hipòtesis; la pausa obligatòria activa la monitorització lectora i obre el plànol crític inicial (Vygotsky, ZDP).

### B2

**Inclou si:**
- Bastides acadèmiques amb identificació de gènere/autor, posicionament al marge, revisió explícita de la hipòtesi inicial i avaluació de fiabilitat de fonts.

**Raonament pedagògic.** A B2 la lectura esdevé acadèmica; la bastida ha d'orientar la identificació del posicionament autoral i l'avaluació de fonts (literacitat crítica).

### C1

**Inclou si:**
- Bastides crítiques amb propòsit metacognitiu autogenerat per l'alumne, reformulació metacognitiva de la hipòtesi i contrast amb altres fonts.

**Raonament pedagògic.** A C1 l'alumne és lector autònom expert; la bastida s'orienta a la metacognició plena i al contrast intertextual, preparant la retirada total.

### transversal_fase_lectora_pre-A1_A1

**Inclou si:**
- Dins de pre-A1 i A1, la sub-granularitat es resol amb la variable `fase_lectora` del frontmatter (logografica / alfabetica_emergent / alfabetica_fluida), NO amb columnes addicionals.

**Raonament pedagògic.** El frontmatter modula sub-granularment dins els nivells inicials per evitar inflar la rúbrica amb columnes redundants; la fase lectora és variable independent.

## Detecció

**Senyals docent** (quan activar bastides de lectura):
- L'alumnat llegeix passivament sense estratègia: descodifica les paraules però no construeix sentit.
- La unitat és TILC i el contingut disciplinar és nou per a l'alumnat (text dens >200 paraules).
- Grup amb diversitat de nivells on cal una bastida universal que cada alumne usa al seu ritme.
- Primer cicle de treball d'un gènere nou (la bastida es retira progressivament al llarg de la SD).
- L'alumnat nouvingut A1-B1 no té el procediment lector internalitzat en català.

**Senyals alumne** (que indica que necessita bastides):
- Comença a llegir sense propòsit i s'atura al mig sense saber on tornar.
- A la pregunta "De què has llegit?", respon "No sé" o "Parla de coses".
- Llegeix tot de seguida sense aturar-se ni marcar res; resum posterior pobre.
- No fa prediccions; no distingeix idea principal de detall.
- Nouvingut pre-A1 / A1: descodifica mecànicament però no construeix sentit; s'atura i mira l'adult.

**Context favorable**:
- Unitat TILC amb text dens (>200 paraules) on la comprensió és prerequisit per a l'activitat.
- Alumnat nouvingut A1-B1: necessita el GPS del procés lector perquè no el té internalitzat en català.
- Aula heterogènia: la bastida actua com a base comuna que cada alumne usa al seu nivell.

**Anti-senyals** (quan NO activar):
- Text molt curt amb comprensió immediata → discussió oral directa.
- L'alumne ja ha internalitzat el procediment lector → retirar les bastides.
- Temps molt limitat → millor una o dues preguntes potents (`preguntes_comprensio`).
- Cal treballar la PRODUCCIÓ escrita d'una tasca → activar `bastides-produccio`, no aquest instrument.

## Modulació per nivell

| Pas | Dimensió | Pre-A1<br>Emergent | A1<br>Inicial | A2<br>Funcional | B1<br>Estratègic | B2<br>Acadèmic | C1+<br>Crític |
|---|---|---|---|---|---|---|---|
| **1. Moment Abans** | Activació de previs | L'adult activa amb una imatge: "Què veus aquí?". L'alumne assenyala o anomena. | 1 pregunta d'activació de previs en frase simple ("Què saps de [tema]?"). | 2 preguntes d'activació + ancoratge a una experiència concreta. | Activació + predicció pel títol o imatge inicial. | + identificació del gènere i de l'autor/font. | + l'alumne formula les seves pròpies preguntes de lectura abans de llegir. |
|  | Propòsit de lectura | Propòsit oral de l'adult: "Anem a saber què passa amb [X]". | Propòsit explícit i concret: "Llegeix per saber [una cosa concreta]". | + propòsit operatiu amb verb d'acció: "Llegeix per identificar [X]". | + propòsit jeràrquic: "Llegeix per distingir el fet principal del context". | + propòsit avaluatiu: "Llegeix per avaluar la fiabilitat de les dades". | + propòsit metacognitiu: l'alumne formula el seu propi propòsit i justifica per què. |
|  | Hipòtesi prèvia | No aplicable (predicció oral guiada). | Predicció pel títol: "De què creus que parlarà?". 1 paraula o frase mínima. | Predicció breu escrita: "Crec que el text dirà…". | Hipòtesi pròpia formulada per escrit: "Hipòtesi: ___. Per què: ___". | + identificació del posicionament inicial probable de l'autor. | + plantejament d'hipòtesis contrastades. |
| **2. Moment Durant** | Modalitat lectora | L'adult llegeix en veu alta. L'alumne assenyala, dramatitza o dibuixa el que entén. **Zero lectura autònoma.** | Lectura mediada per l'adult; l'alumne segueix amb el dit. Subratlla 1 mot clau per paràgraf. | Lectura autònoma possible. Marca ✓ (entès) / ? (dubte) / ! (important) al marge. | Lectura autònoma. Notes marginals breus (1-3 paraules per marca). | + identificació explícita del posicionament de l'autor al marge. | + contrast actiu amb coneixements previs anotat: "Aquí diu X però jo sabia Y". |
|  | Hipòtesi en curs | No aplicable. | No aplicable. | No aplicable. | **Pausa obligatòria** marcada al text (símbol ⏸ o instrucció "Atura't aquí") on l'alumne escriu hipòtesi en curs: "Fins aquí, crec que el text dirà que…". | + a la mateixa pausa, **revisió explícita** de la hipòtesi inicial: "La meva hipòtesi era X, ara crec Y, per què…". | + a la mateixa pausa, **reformulació metacognitiva**: "Si la meva hipòtesi falla, què revela el text que jo no sabia?". |
| **3. Moment Després** | Plànol literal — Resum | Dibuixar el que ha après. Dictat oral a l'adult. Ordenació d'imatges. | **Frase-buit** literal d'un sol buit: "El text parla de ___". | Resum breu de 2-3 frases sobre què tracta el text. | Resum estructurat de 3-4 frases (idea principal + 2 secundàries). | Resum amb jerarquització explícita (titular + cos). | Resum sintètic + comparació amb hipòtesi inicial. |
|  | Plànol inferencial | No aplicable. | No aplicable. | 1 pregunta inferencial guiada: "Per què creus que…?". | Inferència explícita: "Quin era l'objectiu de l'autor?" + "Què queda implícit?". | + detecció de pressuposicions i seleccions narratives no explícites. | + anàlisi de l'enquadrament: "Què queda fora del marc del text? Per què?". |
|  | Plànol crític / Valoració | No aplicable. | No aplicable. | No aplicable. | Valoració simple: "Estàs d'acord amb el que diu el text? Per què?". | Avaluació de fiabilitat: "Fins a quin punt és objectiu l'autor? Quines proves dóna?". | Contrast crític: "Quines altres fonts caldrien per validar aquesta informació?". |
|  | Autoregulació (metacognició) | "He fet el que m'ha dit el mestre." (registre oral/gestual de l'adult). | "He llegit el text amb el mestre i he marcat la paraula difícil." | "He llegit i he marcat ✓/? / !. He fet el resum." | "He revisat si la meva hipòtesi inicial era correcta o no." | "He pensat si l'autor és imparcial. He comprovat si dóna proves de les seves afirmacions." | "He entès tot el que calia? Quines preguntes m'han quedat obertes? Quin pas faria a continuació?" |
| **4. Criteris transversals** | Volum màxim per moment | 1-2 accions gestuals/orals per moment. | Màxim 3 ítems per moment. | Màxim 3 ítems per moment. | Màxim 3 ítems per moment. | Màxim 3 ítems per moment. | Màxim 3 ítems per moment. |
|  | No duplicar `preguntes_comprensio` | Les bastides donen el procediment; les preguntes detallades són del complement `preguntes_comprensio`. | Idem. | Idem. | Idem. | Idem. | Idem. |
|  | Especificitat del propòsit | Propòsit referit a una imatge o paraula concreta del text. | Propòsit específic del text actual, no genèric. | Idem. | Idem. | Idem. | Idem. |
|  | Format obligatori | Secció `## Suports de lectura` + 3 subseccions (Abans/Durant/Després). | Idem. | Idem. | Idem. | Idem. | Idem. |
| **5. Autoavaluació (per l'alumne)** | Reflexió en primera persona | *(via adult)* "He assenyalat el que m'ha demanat el mestre." | "He marcat una paraula important. He completat la frase-buit del resum." | "He marcat ✓/? /! mentre llegia. He escrit de què tracta el text." | "He fet una hipòtesi abans de llegir. He comprovat si era correcta." | "He identificat la postura de l'autor. He avaluat si les dades eren fiables." | "He formulat les meves pròpies preguntes abans de llegir i he comprovat si el text les responia." |

## Casos especials

### fase_lectora_logografica

**Trigger:** mecr_in: [pre-A1] AND fase_lectora: logografica

**Modulació:**
- modalitat_lectora: 'adult llegeix en veu alta'
- lectura_autonoma_alumne: false
- format_bastides: gestual_oral_visual (assenyalar, dramatitzar, dibuixar, ordenar imatges)
- items_per_moment: 1-2 accions
- hipotesi_en_curs: no_aplicable
- planols_inferencial_i_critic: no_aplicables

**Raonament pedagògic.** A fase logogràfica l'alumne reconeix la imatge com a text però encara no descodifica grafies; forçar lectura autònoma o plànols inferencial/crític sobrepassa la ZDP (Vygotsky). La bastida es realitza per via gestual i oral, ancorada a la imatge (MALL multimodal).

### hipotesi_en_curs_B1plus

**Trigger:** mecr_in: [B1, B2, C1]

**Modulació:**
- pausa_obligatoria: true (marca explícita ⏸ o instrucció 'Atura't aquí' inserida al text adaptat)
- bastida_hipotesi_en_curs: obligatòria al Moment Durant
- a B2/C1: revisió/reformulació metacognitiva de la hipòtesi inicial a la mateixa pausa

**Raonament pedagògic.** A B1+ l'alumne ja pot monitoritzar la pròpia comprensió; la pausa obligatòria amb hipòtesi en curs activa la metacognició lectora (Palincsar & Brown 1984, lectura recíproca) i prevé la lectura passiva.

### no_duplicar_preguntes_comprensio

**Trigger:** pipeline_actius_inclou: preguntes_comprensio

**Modulació:**
- cross_source: llegir l'output de `preguntes_comprensio` abans de generar
- bastides_ortogonals: true (procediment, no preguntes de contingut)
- si_duplicitat: ATNE dedupea (preguntes_comprensio guanya, bastides es replanteja) i registra traça a metadades
- sense_warning_runtime: true

**Raonament pedagògic.** Bastides i preguntes_comprensio són ortogonals: la bastida dona el procediment (com llegir), les preguntes treballen la comprensió punt a punt. Duplicar saturaria l'alumne i diluiria la funció orientadora de la bastida.

### frase_buit_A1

**Trigger:** mecr_in: [A1]

**Modulació:**
- resum_literal: una sola frase-buit amb un únic forat ('El text parla de ___')
- cap inferència ni valoració crítica al Moment Després

**Raonament pedagògic.** A A1, el resum amb un sol buit funciona com a test diagnòstic ràpid (H5) i evita la sobrecàrrega cognitiva pròpia d'una construcció lliure; la inferència i la valoració crítica s'introdueixen a A2/B1.

## Metadades de cel·la (per a `build_skills.py`)

Cada dimensió té un **tipus de descriptor** que condiciona com s'ha de transformar al derivat avaluatiu i al derivat-prompt.

**Tipus de descriptor:**
- `countable` — té un llindar quantitatiu verificable mecànicament.
- `binary` — només admet "compleix / no compleix".
- `enumerable` — verificable contra una llista.
- `qualitative` — requereix judici humà o LLM-jutge.
- `structural` — requereix anàlisi sintàctica/discursiva.
- `cross_source` — requereix accés a un altre output del pipeline (text adaptat, output d'altres complements) per comparar.
- `metacognitive` — descriptor de procés en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1.1 Abans — Activació de previs | `qualitative` | parcial (text adaptat) | LLM-jutge: la pregunta connecta amb experiència o coneixement plausible per al nivell? |
| 1.2 Abans — Propòsit de lectura | `qualitative` + `structural` | sí (text adaptat) | LLM-jutge: propòsit específic del text actual vs propòsit genèric ("llegeix el text") |
| 1.3 Abans — Hipòtesi prèvia | `binary` (existència) + `qualitative` (qualitat) | no | detectar presència de bastida d'hipòtesi a A1+ amb forma adequada al nivell |
| 2.1 Durant — Modalitat lectora | `structural` + `binary` | no | detectar instrucció de marcatge (✓/?/!, subratllat, notes) i la seva adequació al nivell |
| 2.2 Durant — Hipòtesi en curs | `binary` (existència) + `structural` | no | a B1+: detectar **marca de pausa explícita** al text (símbol ⏸ o instrucció "Atura't aquí") + bastida metacognitiva de revisió d'hipòtesi en curs |
| 3.1 Després — Resum literal | `countable` + `structural` | no | comptar buits/frases del resum; verificar adequació al nivell (1 buit a A1, 3-4 frases a B1) |
| 3.2 Després — Inferència | `qualitative` | no | LLM-jutge: la pregunta demana inferència no literal i és respondible amb el text |
| 3.3 Després — Valoració crítica | `qualitative` | no | LLM-jutge: la bastida obre un espai de judici argumentat (B1+) o d'avaluació de fonts (B2+) |
| 3.4 Després — Autoregulació | `metacognitive` | no | derivat doble: autoavaluació alumne + registre docent |
| 4.1 Volum màxim per moment | `countable` | no | comptar ítems per cada subsecció (Abans/Durant/Després); llindar ≤3 |
| 4.2 No duplicar `preguntes_comprensio` | `cross_source` | **sí (output de preguntes_comprensio si actiu)** | comparar semànticament: cap pregunta de bastides ha de coincidir amb cap pregunta del complement |
| 4.3 Especificitat del propòsit | `qualitative` + `cross_source` | sí (text adaptat) | LLM-jutge: el propòsit referencia contingut concret del text actual |
| 4.4 Format obligatori | `structural` + `binary` | no | parser markdown: `## Suports de lectura` + 3 subseccions Abans/Durant/Després |
| 5 Autoavaluació metacognitiva | `metacognitive` | no | derivat doble: autoavaluació alumne + registre docent de la qualitat |

**Notes:**
- 4.2 No duplicar `preguntes_comprensio` és un descriptor `cross_source` **dependent del pipeline**: només s'avalua quan els dos complements estan actius simultàniament. Si només `bastides` està actiu, no aplica.
- 4.1 Volum màxim per moment és `countable` verificable amb regex/markdown parser; cost zero.
- 3.4 i 5 són `metacognitive` — comparteixen el patró de **doble sortida** (autoavaluació alumne + registre docent) ja establert a notícia/glossari/opinió.
- A diferència de gèneres com notícia, **no hi ha descriptor de fidelitat al text font** (5.5 al glossari, 7.4 a notícia): les bastides no reformulen el text font, l'orienten. La validació cross_source és contra altres outputs del pipeline (preguntes_comprensio, text adaptat) i no contra el text original.

## Heurístiques docent

**H1 — La bastida que es retira**
Les bastides no són permanents. Introdueixo les bastides de lectura les primeres 2-3 sessions i progressivament elimino els ítems que l'alumne ja fa sol. Una bastida que no es retira deixa de ser bastida i es converteix en dependència. Quan veig que l'alumne fa la predicció del títol sense que jo l'hi demani, és el senyal: aquesta bastida ja no cal.

**H2 — El propòsit de lectura és la clau**
"Llegeix per saber X" ha de ser específic i concret. Si el propòsit és genèric ("llegeix el text"), la bastida perd la seva funció orientadora. Quan formulo el propòsit, em pregunto: "Si l'alumne només llegís per respondre aquesta pregunta, hauria llegit el text amb sentit?". Si la resposta és sí, el propòsit és bo.

**H3 — "Subratlla el que no entens" abans de marcar el que entens**
A A2-B1, dono primer la instrucció inversa: "Marca amb ? les paraules o frases que no entens." Quan l'alumne ho ha fet, li dic: "El que queda sense marcar, ho has entès. Ara subratllem les idees importants d'allò que has entès." Evita la paràlisi davant un text parcialment opac i transforma la lectura passiva en una activitat metacognitiva des de l'inici.

**H4 — La bastida mínima viable**
Quan tinc poc temps, trio la bastida mínima: propòsit de lectura ("Llegeix per saber [X concret]") + un buit al final per al resum. Dos ítems ben triats activen la comprensió activa millor que 10 ítems mal triats. La temptació de posar "una mica de tot" sempre acaba en saturació cognitiva.

**H5 — El Moment Després revela la comprensió**
Si l'alumne no pot completar la frase marc del Moment Després, no ha entès el text. La bastida revela el problema **abans** de la pregunta de comprensió: el frase-buit "El text parla de ___" és un test diagnòstic ràpid. Quan veig que el buit es queda en blanc o amb una resposta tangencial, sé que cal tornar a llegir mediant.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Suports de lectura
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
### Abans
### Durant
### Després
```

**Marcadors inline obligatoris:**
```
⏸
✓
?
!
```

**Regla d'integritat estructural.** Sense el header literal `## Suports de lectura` i les 3 subseccions `### Abans`, `### Durant`, `### Després` en aquest ordre, el parser d'ATNE no detecta l'estructura i les bastides queden orfes al frontend, impossibilitant la verificació estructural (4.4) i el comptatge d'ítems per moment (4.1 ≤3).

## Fonts principals

- MALL (Model d'Aprenentatge de Llengües i Literacitat): 3 moments × 3 plànols, estratègies lectives, principi "menys és més".
- Vygotsky (1978): zona de desenvolupament proper — el scaffolding com a suport temporal entre el que l'alumne sap fer sol i el que pot fer amb ajuda.
- Wood, Bruner & Ross (1976): concepte de *scaffolding* en educació — bastides retirables.
- Palincsar & Brown (1984): lectura recíproca — les 4 estratègies (predicció, aclariment, interrogació, resum) que estructuren els tres moments.
- Gibbons (2002): *Scaffolding language, scaffolding learning* — bastides específiques per a alumnat EAL/L2.
- Decret 175/2022 (currículum Catalunya): competència lectora, comprensió crítica i plurilingüisme.
