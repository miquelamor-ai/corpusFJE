---
modul: M3
titol: "Escriure/adaptar un poema"
tipus: genere-discursiu
categoria_principal: generes
categories_secundaries: []
descripcio: "Instrument per adaptar o generar un poema (gènere líric): preservacio de l'estructura estrofica i la divisio en versos, metafores concretes i visuals, simplificacio de vocabulari mantenint el ritme i la veu poetica. HCL Descriure (expressiva). Pre-A1 SÍ (oral i ludic, mediat per adult). Rubrica gradada 7 passos × 6 nivells MECR (pre-A1→C1)."
mecr_range: [pre-A1, A1, A2, B1, B2, C1]
agent_roles: [adapter, generator]
genre_key: poema
macro_tipologia: poetica
label_ca: "Poema"
translanguaging: false
multimodal: false
moduls_relacionats: [M3]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: write-poema@corpusFJE/skills/generes/write-poema
review_status: pilot-fusio-8
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, variabilitat-cardinal-passos-D3]
  aplicades_post_review: [b6-poema-pas2-qualitative-afegit]
  comentari_key: "pas2-vers-structural+qualitative-clarificat; translanguaging-false-correcte-tolc-estrategia-no-l1-al-text; multimodal-false-correcte-poema-es-textual"
---

# Escriure/adaptar un poema

## Descripció

El poema és un text literari que usa el vers com a unitat ritmica i la imatge com a vehicle de significat. El seu tret definitori és la **forma com a significat**: l'estructura estrofica, el ritme i la metafora no son ornaments — son el contingut. L'adaptacio simplifica vocabulari i metafores, pero mai l'estructura. Si la forma es trenca, el text deixa de ser un poema.

**Tipologia MALL**: Expressiva/Retorica.
**HCL principal**: Descriure (expressiva, evocadora) — seleccionar imatges i sensacions i condensar-les en la forma del vers.
**HCL secundaries**: Narrar (poema narratiu) · Interpretar/Valorar (posicionament personal sobre el poema, B1+).
**Nota MALL**: la poesia combina simultaneament les dimensions oral i escrita. Memoritzar un rodoli es aprendre el ritme de la llengua nova. La lectura en veu alta activa la musicalitat i fa accessibles metafores que semblen "difícils" a la lectura silenciosa.
**Pre-A1 SÍ (D6)**: rodolins, cançons i endevinalles orals. La preferència, la sensació i la imatge concreta son accessibles sense inferencia simbolica: "el sol és com una taronja" pot mostrar-se amb gest i imatge. El docent recita o canta, l'alumne repeteix, imita i completa. No requereix simbolisme de segon nivell ni abstraccio temporal.

**Connexions MALL transversals:**
- *Rima com a bastida fonologica*: per a l'alumne nouvingut, la rima és una bastida de memoria i de risc lingüístic. El motlle fonic redueix la incertesa lexica i permet produir.
- *Metafora concreta com a pont cognitiu (ZDP)*: substituir "l'astre flamiger" per "el sol vermell com una brasa" no és empobriment literari — és accessibilitat sense renunciar al genere. La metafora concreta connecta el text font amb l'experiencia sensorial de l'alumne.
- *Pre-A1 oral i ludic*: el poema és el genere de la transmissio oral per excel·lencia. A pre-A1, rodolins i cançons son la bastida fonetica i prosodica de la llengua nova. Cantar un poema és aprendre-la des de dins.

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **poema adaptat per a la LECTURA** de l'alumne. **No descriu la produccio autonoma** — la produccio és tasca d'un derivat propi. Principi pedagogic MALL: l'alumne llegeix models al maxim del seu abast.
**Sub-granularitat dins de pre-A1**: es treballa amb `fase_lectora: logografica` (oral i pictografic, mediat per adult) i `fase_lectora: alfabetica_emergent` (oral + primer text escrit); no s'exclou el nivell logografic perque el poema oral no requereix llegir.

## Principi general

**Regla de selecció simple.** Genera o adapta un text en forma de poema: una unitat lírica organitzada en estrofes i versos (un vers per línia), amb almenys una imatge o metàfora concreta i un ritme perceptible (rima o cadència) adequat al nivell MECR objectiu. Modula vocabulari, metàfores i ritme segons la taula de modulació, però MAI eliminis l'estructura estròfica ni els salts de línia: si la forma es trenca, el text deixa de ser un poema.

**Límits del LLM (no judici qualitatiu complex).** El LLM no ha d'avaluar el valor estètic ni l'originalitat literària del poema, ni decidir quina metàfora del text font és 'massa abstracta' per a un alumne concret, ni jutjar la qualitat de la veu poètica resultant. La decisió final sobre acceptabilitat poètica i adequació al grup la pren qui ensenya; el LLM només garanteix la forma (estrofes, versos per línia, imatge concreta, ritme perceptible) i l'adequació lèxica al MECR.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### default

**Inclou si:**
- estructura_estrofica_visible
- un_vers_per_linia
- almenys_una_imatge_concreta_per_estrofa
- ritme_perceptible_segons_MECR

**Exclou explicitament:**
- text_renderitzat_com_a_prosa
- versos_partits_o_units_sense_intencio

**Raonament pedagògic.** El default aplica la cel·la MECR de la taula Modulació mantenint la forma poètica com a contingut: si es trenca l'estructura, el text deixa de pertànyer al gènere.

### preA1

**Inclou si:**
- format_oral_rodoli_o_canço
- 2_a_4_versos
- rima_aaaa_o_aabb
- 1_imatge_concreta
- vocabulari_quotidia
- mediacio_adulta_per_l_escriptura

**Exclou explicitament:**
- escriptura_autonoma_alumne
- metafores_de_segon_nivell

**Raonament pedagògic.** A pre-A1 la poesia és oral i lúdica (decisió D6); rodolins i cançons són bastida fonètica i prosòdica de la llengua nova (MALL, eix oral-escrit).

### A1_A2

**Inclou si:**
- 1_a_3_estrofes_de_2_a_4_versos
- rima_consonant_senzilla
- una_comparacio_o_metafora_concreta_per_estrofa
- vocabulari_quotidia_amb_max_1_o_2_paraules_noves_contextualitzades

**Exclou explicitament:**
- metafores_abstractes_o_simbolisme_de_segon_nivell
- vocabulari_rebuscat

**Raonament pedagògic.** A A1-A2 la rima funciona com a bastida de memòria i de risc lingüístic; la metàfora concreta connecta el text font amb l'experiència sensorial de l'alumne (ZDP).

### B1

**Inclou si:**
- 3_a_4_estrofes
- estructura_conscient
- metafora_que_connecta_concepte_nou_amb_experiencia_de_l_alumne
- ritme_que_pot_prescindir_de_rima_si_la_cadencia_es_mante

**Exclou explicitament:**
- rima_forçada_que_distorsiona_significat

**Raonament pedagògic.** A B1 l'alumne ja pot sostenir intenció estructural; la metàfora opera com a pont cognitiu dins la ZDP de Vygotsky.

### B2_C1

**Inclou si:**
- estructura_variada_amb_intencionalitat
- 2_a_3_imatges_elaborades_coherents
- vocabulari_ric_i_precis
- veu_poetica_personal_i_reconeixible
- a_C1_estructura_lliure_i_recursos_com_sinestesia_o_metafora_mixta

**Exclou explicitament:**
- empobriment_lexic_artificial

**Raonament pedagògic.** A B2-C1 es manté sostre alt: l'alumne treballa la forma com a eina expressiva conscient (funció poètica de Jakobson).

### nouvingut_L1

**Inclou si:**
- estrategia_canço_pont_L1
- bastida_oral_en_L1
- rima_final_regular_per_ancorar_memoria
- imatges_sensorials_i_universals

**Exclou explicitament:**
- L1_al_text_final_del_poema (translanguaging: false al frontmatter)

**Raonament pedagògic.** Vegeu cas especial 'nouvingut_L1_canço_pont': la musicalitat de la L1 transfereix (TOLC, Cummins); cantar el poema en la nova llengua activa connexió identitària i memòria afectiva. El poema escrit final queda monolingüe en català.

## Detecció

**Senyals docent** (quan adaptar a poema):
- El text font és un poema (tradicio lirica catalana, castellana, llatinoamericana, universal).
- La unitat de llengua i literatura treballa la dimensio lirica o la competencia emocional.
- L'alumne ha de produir un poema com a tasca d'expressio creativa.
- El docent vol introduir un text poetc a un grup amb nivells mixtos (multinivell).

**Senyals alumne** (que indica que necessita bastida):
- Llegeix el poema pero el percep com a text incoherent (no entén la metafora ni el ritme).
- L'escriu pero el converteix en prosa (elimina els salts de linia).
- Usa vocabulari molt quotidia sense cap recurs estetic.
- Rima forçada que distorsiona el significat ("feia fred i per tant menjed").

**Context favorable**:
- Llengua i literatura (analisi i produccio poetica).
- Musica (cançons com a poemes, musicalitat de la llengua).
- Educacio artistica (poesia visual, caldogrammes).
- Tutoria (poesia com a expressio emocional i vincle identitari).

**Anti-senyals** (quan NO adaptar a poema):
- El text font és narratiu en prosa → conte o cronica.
- El text expressa una postura raonada → assaig o opinio.
- El text vol emocionar pero en prosa → diari personal.
- El text descriu de manera sistematica i objectiva → descripcio o informe.

## Modulació per nivell

| Pas | Dimensió | Pre-A1 Emergent | A1 Inicial | A2 Funcional | B1 Estratègic | B2 Acadèmic | C1 Crític |
|---|---|---|---|---|---|---|---|
| **1. Estructura estrofica** | Forma i regularitat | Recitacio oral; adult escriu si cal. L'alumne reconeix la repeticio de sons i versos. | 1-2 estrofes de 2-3 versos. Estructura visible i regular. Separacio visual clara. | 2-3 estrofes de 3-4 versos. Separacio visual entre estrofes. Cada estrofa = 1 idea. | 3-4 estrofes. Estructura conscient. Pot variar el nombre de versos per efecte intencional. | Estructura variada amb intencionalitat. Pot incloure estrofes de mida diferent. | Estructura lliure o formal amb plena consciencia del model triat i el seu efecte. |
| **2. Vers com a unitat** | Significat i ritme | No s'aplica (oral; el ritme és el de la canço o el rodoli). | Cada vers = 1 idea o imatge. Sense partir una idea a la meitat del vers. | Cada vers és independent pero contribueix a la imatge global. | Encavalcament conscient si s'usa: la idea continua al vers seguent amb intencio. | Control del vers com a unitat de sentit i de ritme simultaneament. | Vers com a instrument precis de significat, pausa i musicalitat. |
| **3. Metafores i imatges** | Accessibilitat estetica | Reconeixement oral: "el sol és com una taronja". L'adult proposa la imatge. | 1 comparacio concreta per estrofa: "com un...", "sembla un...". Imatge visual. | 1 metafora o comparacio per estrofa. Concreta i visual. Ancoratge sensorial. | Metafora que connecta un concepte nou amb l'experiencia de l'alumne (ZDP). | 2-3 imatges elaborades. Coherencia tematica entre elles. | Imatges originals. Pot explorar metafora mixta o sinestesia. |
| **4. Vocabulari** | Accessibilitat lexica | Vocabulari molt quotidia. Paraules que l'alumne ja usa (objectes, animals, colors). | Vocabulari quotidia. Cap sinonim rebuscat. 1 paraula nova com a maxim per estrofa. | Vocabulari accessible. 1-2 paraules noves amb context que ajudi a entendre-les. | Vocabulari adequat al tema. Les paraules noves hi son perque aporten precisio poetica. | Vocabulari ric i variat. Tria conscient de paraules per la seva musicalitat i densitat semantica. | Vocabulari precis, ric i personal. Pot incloure neologismes justificats. |
| **5. Ritme (rima/cadencia)** | Musicalitat | Rima final simple i molt repetitiva. L'adult guia la rima (aaaa o aabb). | Rima consonant senzilla al final del vers (parells o alternada). | Rima consonant o assonant. Pot ser alternada. Ritme regular perceptible. | Ritme conscient. Pot renunciar a la rima si la cadencia es manté. | Varietat ritmica. Pot combinar versos amb rima i versos blancs. | Ritme com a eina expressiva. Alteracio conscient del ritme per crear efecte. |
| **6. Veu poetica (jo liric)** | Perspectiva i autoria | L'alumne expressa oralment com se sent davant d'una cosa. L'adult escriu. | "Jo" visible i consistent. El poema parla des d'una perspectiva clara. | Veu del jo liric consistent durant tot el poema. No canviar de perspectiva. | Distincio entre jo liric i autor. Pot explorar una veu diferent de la propia. | Veu poetica personal i reconeixible. El lector nota qui parla. | Veu poetica plenament elaborada amb distancia critica o ironia si escau. |
| **7. Autoavaluacio** | Metacognicao | — | "He escrit 2 estrofes. He posat una comparacio (com un...)." | "Cada estrofa te la seva idea. He mantingut la rima fins al final." | "La meva metafora connecta el tema amb alguna cosa que conec. El ritme es manté." | "He triat les paraules per la seva sonoritat. La veu del poema és consistent." | "El meu poema te una veu propia. Les imatges son originals i el ritme és intencional." |

## Casos especials

### preA1_oral_mediat

**Trigger:** mecr_in: [pre-A1] AND fase_lectora_in: [logografica, alfabetica_emergent]

**Modulació:**
- format_sortida: rodolí o cançó curta de 2-4 versos amb rima molt repetitiva (aaaa o aabb)
- densitat_imatges: 1 imatge concreta i visible (sol, lluna, gat)
- vocabulari: només paraules quotidianes que l'alumne ja usa
- no_escriptura_autonoma: true (l'adult escriu; l'alumne recita, repeteix o completa)
- pas_7_autoavaluacio: omès (no aplica)

**Raonament pedagògic.** A pre-A1 la poesia és oral i lúdica; rodolins i cançons són bastida fonètica i prosòdica de la llengua nova (MALL, eix oral-escrit). La producció escrita autònoma està fora de la ZDP; la mediació adulta i la repetició cantada són el motor d'aprenentatge.

### nouvingut_L1_canço_pont

**Trigger:** nouvingut_L1: true AND mecr_in: [pre-A1, A1, A2]

**Modulació:**
- estrategia_recomanada: partir d'una cançó o rodolí que l'alumne coneix en L1 i buscar-ne un equivalent o adaptació en català
- translanguaging_oral: sí (ús de la L1 oral com a bastida fonètica i emocional, sense afegir L1 al text del poema final)
- densitat_rima: alta (rima final regular per ancorar memòria)
- imatges: sensorials i universals (foc, aigua, mare, casa)

**Raonament pedagògic.** La musicalitat de la L1 transfereix (TOLC, Cummins); cantar el poema en la nova llengua activa connexió identitària i memòria afectiva. El poema escrit no porta L1 (translanguaging: false al frontmatter) però el procés oral sí l'aprofita.

### DUA_acces_perfil_visual_auditiu

**Trigger:** dua_equals: Acces AND (perfil_in: [TDAH, dislexia] OR força_auditiva: true)

**Modulació:**
- lectura_veu_alta_obligatoria: true (presentar el poema sonor abans del visual)
- rima: consonant i regular (no rima blanca ni encavalcament)
- longitud_max_vers: 6-8 síl·labes
- metafores: només concretes i sensorials (evitar simbolisme de segon nivell)
- suport_visual_opcional: il·lustració o pictograma per estrofa que ancori la imatge clau

**Raonament pedagògic.** El ritme regular i la rima funcionen com a bastida atencional i mnemotècnica; la lectura en veu alta activa el canal auditiu i fa accessibles metàfores que semblen difícils en lectura silenciosa (H3 del propi instrument).

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `countable` — llindar quantitatiu verificable mecanicament.
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici huma o LLM-jutge.
- `structural` — requereix analisi sintatica o discursiva.
- `metacognitive` — descriptor de proces en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Estructura estrofica | `binary` + `qualitative` | no | binary: hi ha mes d'una estrofa separada visualment; qualitative: LLM-jutge sobre si el nombre d'estrofes i versos és adequat al nivell |
| 2 Vers com a unitat | `structural` + `qualitative` | no | structural: detectar si hi ha salts de linia per vers (regex: absència de salts de linia dins d'una estrofa = error); qualitative: LLM-jutge sobre si cada vers respecta la unitat de sentit o parteix una idea de manera injustificada |
| 3 Metafores i imatges | `qualitative` | **si** (B1+) | LLM-jutge sobre si la metafora és concreta i accessible; si s'hi pot anclar visualment; cross_source B1+: verificar si la metafora adaptada manté l'equivalent semantic de l'original |
| 4 Vocabulari | `countable` + `qualitative` | no | comptar paraules fora del vocabulari de frequencia MECR corresponent; qualitative: LLM-jutge sobre si les paraules noves aporten valor o son obstacles |
| 5 Ritme | `structural` + `qualitative` | no | detectar si hi ha rima (consonant/assonant); analisi sil·labica si cal; qualitative: LLM-jutge sobre si el ritme és perceptible o forçat |
| 6 Veu poetica | `binary` + `qualitative` | no | binary: us consistent de la primera persona; qualitative: LLM-jutge sobre si la veu del jo liric és consistent i reconeixible |
| 7 Autoavaluacio | `metacognitive` | no | derivar a vista d'autoavaluacio alumne + registre docent |

**Notes:**
- El poema és l'instrument on `requires_source_text` és menys crític: la forma és el criteri principal, no la fidelitat informativa al font. Cross_source s'aplica a B1+ per verificar la coherencia de la metafora adaptada respecte a l'original.
- Vers com a unitat (Pas 2): el salt de linia és el marcador formal mes important i el mes facil de verificar automaticament. Un poema sense salts de linia no és un poema.
- Pre-A1: el descriptor de Pas 7 (autoavaluacio) no aplica perque la produccio és oral. El registre es fa pel docent.

## Regles transversals

- **Forma sobre MECR**: la forma del gènere guanya sobre el nivell MECR. Si hi ha conflicte entre simplificar al MECR i preservar l'estructura formal del gènere (versos, torns, passos numerats, camps), guanya la forma. Es pot simplificar el VOCABULARI, però cal seguir l'estructura canònica que defineix la skill del gènere. Millor un text mínimament adaptat però formalment íntegre que un text aplanat que destrueixi el gènere.

## Heurístiques docent

**H1 — La imatge concreta com a entrada.**
Proposo que l'alumne pensi en una cosa que pot tocar o veure. Despres li demano: "Com és, sense dir-ne el nom?" La resposta és la metafora del poema. Funciona des de pre-A1 (oral) fins a C1.

**H2 — El poema com a columna.**
Escriure el poema verticalment, un vers per linia. Si una idea no cap en una linia, té massa contingut per a un sol vers. Funciona com a test visual de la forma: si el text s'assembla a un paragraf, no és un poema.

**H3 — Llegir en veu alta com a primer pas.**
Proposo que l'alumne llegeixi el poema en veu alta abans de fer res mes. La lectura en veu alta activa el ritme i la musicalitat. Moltes metafores "difícils" resulten comprensibles quan se senten. Especialment util per a alumnat amb TDAH o mes força auditiva que visual.

**H4 — "Que veus?" per a les metafores.**
Quan una metafora resulta abstracta, demano: "Que veus quan llegeixes 'l'astre flamiger'?" L'alumne descriu el que imagina, i d'alla surt la versio concreta. La pregunta "que veus?" transforma la metafora abstracta en imatge visual sense que el docent hagi de donar la resposta.

**H5 — Cançó equivalent a pre-A1/A1.**
A pre-A1 i A1, proposo partir d'una canço que l'alumne coneix en la seva L1 i trobar-ne una equivalent en catala. La musicalitat de la L1 transfereix (TOLC). Cantar el poema en la nova llengua és una bastida fonetica i emocional que facilita la memoritzacio i la connexio afectiva amb la llengua.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Poema
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
cap (el poema és una unitat lírica única; no es divideix en H3 dins de ## Poema)
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
[ESTROFA]   <!-- opcional: separador explícit d'estrofa quan la línia en blanc no es renderitza prou clarament -->
```

**Headers explícitament PROHIBITS:**
```
## Estrofes
## Versos
## Rima
```

**Regla d'integritat estructural.** Sense el header literal `## Poema` i sense salts de línia explícits entre versos (un vers per línia) i entre estrofes (línia en blanc), el parser del frontend no detecta la unitat poètica i renderitza el text com a prosa, perdent la forma que és el contingut del gènere.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengues i Literacitat): HCL Descriure expressiva, dimensio literaria, eix oral-escrit.
- Jakobson, R. (1960): funcio poetica del llenguatge — el poema com a focus en la forma del missatge.
- Vygotsky, L.S. (1978): *Mind in Society* — joc simbolic i metafora com a eina cognitiva; ZDP aplicat a la creacio poetica.
- Cummins, J. (2001): *Negotiating Identities* — la poesia en L1 com a pont identitari i cognitiu; transferencia TOLC.
- Decret 175/2022 (curriculum Catalunya): competencia en comunicacio lingüística, dimensio literaria i expressio creativa.
