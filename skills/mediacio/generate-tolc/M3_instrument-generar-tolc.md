---
modul: M3
titol: "Generar TOLC / transllenguatge"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: []
descripcio: "Instrument per generar el bloc TOLC/transllenguatge: pont L1->catala. Activacio condicional: UNICAMENTE si perfil nouvingut actiu amb L1 coneguda; si L1 desconeguda, no generar. 5 blocs: Activacio (pregunta comparativa), Acarament (taula bilingue L1<->catala amb alfabet original), Observacio estructural (semblances primer), Consigna de transferencia (dictat pre-A1/A1 -> mediacio complexa C1), Caracter voluntari (sempre, mai exposar l'alumne). TOLC (Cummins) + PBCS. Rubrica gradada 5 passos x 6 nivells MECR (pre-A1->C1)."
mecr_range: [pre_A1, A1, A2, B1, B2, C1]
agent_roles: [generator]
complement_key: tolc
translanguaging: true
multimodal: false
moduls_relacionats: [M2, M3]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: generate-tolc@corpusFJE/skills/mediacio/generate-tolc
review_status: pilot-fusio-8
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, variabilitat-cardinal-passos-D3, modulacio-per-perfil-D1]
  aplicades_post_review: [b10-tolc-c2-pas2-qualitative-alfabet, b10-tolc-c3-pas4-requires-source-text-si, b10-tolc-c4-pas5-qualitative-llm-jutge]
  comentari_key: "C1-multimodal-false-rebutjat-pictograma-recurs-docent; C5-b1-resum-l1-rebutjat-o-manté-objectiu-tolc"
---

# Generar TOLC / transllenguatge

## Descripció

El TOLC (Translation for Other Learning Contexts, Cummins) usa la **L1 de l'alumne com a pont cognitiu** cap al català. El complement genera un bloc estructurat en 5 parts: activació (pregunta comparativa), acarament (taula bilingüe L1↔català amb alfabet original), observació estructural (semblances primer, diferències com a curiositat), consigna de transferència (pont de producció), i clàusula de voluntarietat (mai exposar l'alumne). Complementat amb el **PBCS** (Pedagogically-Based Code Switching, alternança estratègica de codis), fa visible la diferència entre sistemes lingüístics.

**Tipologia MALL**: Mediació (transllenguatge actiu).
**HCL principals**: Comparar · Transferir · Reflexionar metalingüísticament.
**Principi rector — L1 com a recurs, no obstacle**: el TOLC materialitza el principi del MALL que totes les llengues de l'alumne son recursos cognitius. La L1 no és un problema a superar sinó un pont per construir. La Hipòtesi d'Interdependència de Cummins (2008) demostra que les competències de L1 transfereixen a L2 quan el pont es fa explícit.

**Activació condicional crítica**: el complement es genera ÚNICAMENT si:
1. El perfil de l'alumne té `nouvingut: true` actiu.
2. La L1 de l'alumne és **coneguda** (declarada al perfil).
Si la L1 no és declarada → es retorna advertència i no es genera el complement. Si el docent activa TOLC sense perfil nouvingut → el complement salta silenciosament.

**Alfabet original de la L1**: escriure les paraules en àrab, xinès, urdú, ciríl·lic, armeni o qualsevol altre alfabet en la seva forma original (no transliterada) és un acte de **reconeixement de la llengua de l'alumne**. La transliteració pot ser útil però no substitueix l'alfabet original.

**Principi de voluntarietat absoluta**: totes les consignes inclouen la clàusula "si vols, si pots" o equivalent. Mai exigir la L1 públicament. La taula bilingüe és personal. La consigna no exposa: "Si coneixes la paraula en una altra llengua, comparteix-ho si vols."

**PBCS — Alternança estratègica de codis**: el PBCS (diferent del transllenguatge espontani) fa visible la diferència entre sistemes lingüístics de manera controlada. L'alumne aprèn que les llengues no son traduccions literals les unes de les altres: l'ordre SVO, la posició de l'adjectiu, les construccions causals variam entre L1 i català. Aquesta consciència metalingüística accelera l'adquisició del català.

**Connexions MALL transversals:**
- *Semblances primer (principi pedagògic)*: l'observació estructural comença SEMPRE per les semblances entre L1 i català. "En la teva llengua i en català, les dues funcionen igual en aquest punt" és el millor punt de partida. Les diferències son interessants, no problemàtiques.
- *Taula bilingüe com a vocabulari actiu*: la taula no és per llegir — és per usar mentre es llegeix el text. L'alumne veu un terme difícil → consulta la taula → activa la xarxa semàntica en L1 → transfereix al català. Aquest procediment automatitza la transferència.
- *Consigna de transferència com a producció mediada*: a nivells inicials (dictat a l'adult, pre-A1/A1), la consigna de transferència és una forma de producció mediada. A nivells avançats (mediació complexa, B2-C1), és producció plena de mediació lingüística.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **bloc TOLC que es genera per a l'alumne nouvingut** (MEDIACIÓ PLURILINGÜE). **No descriu l'avaluació del docent ni la competència en L1**: el docent observa si l'alumne usa la taula durant la lectura i si la consigna de transferència li permet avançar.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → activació oral + assenyalar; `fase_lectora: alfabetica_emergent` → 1-2 paraules escrites en català.

## Principi general

**Regla de selecció simple.** Genera SEMPRE i NOMÉS els 5 blocs canònics del TOLC en aquest ordre (1. Activació, 2. Acarament L1↔català, 3. Observació estructural, 4. Consigna de transferència, 5. Clàusula de voluntarietat), modulats segons MECR i fase lectora. ACTIVACIÓ CONDICIONAL: el complement es genera ÚNICAMENT si el perfil té `nouvingut: true` i la L1 és declarada; si la L1 és desconeguda → retorna advertència i no generis res; si nouvingut no actiu → salta silenciosament.

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix si l'alumne 'sap prou L1' per fer transferència, ni si la L1 declarada està prou desenvolupada, ni si l'alumne 'estarà còmode' exposant la seva L1 públicament. Tampoc inventa contingut en L1 si no està segur de la grafia o l'alfabet correcte: si dubta de la forma escrita en àrab/hanzi/devanagari/ciríl·lic, ho marca explícitament al log i no fabrica. La decisió sobre acceptar/modificar la taula bilingüe i el grau d'integració de la L1 a l'aula la pren el docent.

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### nouvingut_L1_coneguda

**Inclou si:**
- nouvingut: true
- L1_declarada: true

**Exclou explicitament:**
- cap exclusió (genera els 5 blocs complets segons MECR i fase lectora)

**Raonament pedagògic.** Amb L1 coneguda es pot construir el pont cognitiu real (Hipòtesi d'Interdependència, Cummins 2008). Alfabet original obligatori a la columna L1 com a acte de reconeixement lingüístic; voluntarietat explícita a tots els blocs.

### nouvingut_L1_desconeguda

**Inclou si:**
- cap criteri (no genera output)

**Exclou explicitament:**
- generació_complement

**Raonament pedagògic.** Sense L1 declarada no es pot construir cap pont; fabricar L1 o assumir-la és un risc ètic que invisibilitza la llengua real de l'alumne. Es retorna advertència al docent: «L1 no declarada — pregunta a alumne/família abans d'activar TOLC.» Log motiu: L1_unknown.

### nouvingut_no_actiu

**Inclou si:**
- cap criteri (no genera output)

**Exclou explicitament:**
- generació_complement

**Raonament pedagògic.** TOLC està dissenyat per a perfils nouvinguts amb L1 viva; aplicar-lo a alumnat plenament catalanoparlant no té sentit pedagògic. Es salta silenciosament (sense advertència visible) perquè el docent pot estar provant l'eina.

### AACC_nouvingut

**Inclou si:**
- nouvingut: true
- AACC: true
- densitat_metalingüística_augmentada (a partir d'A2)

**Exclou explicitament:**
- trencament_voluntarietat

**Raonament pedagògic.** Manté els 5 blocs però augmenta la densitat metalingüística: l'observació estructural (pas 3) pot incloure 2 contrastos en comptes d'1, i la consigna de transferència pot proposar mediació més complexa al sostre del MECR. Sostre alt sense techo artificial, però mai trencar la voluntarietat (H3 ATNE).

### DUA_acces_nouvingut

**Inclou si:**
- nouvingut: true
- DUA_dimensio: acces
- suport_visual_reforçat (a pre-A1/A1)

**Exclou explicitament:**
- exposició_pública_obligada

**Raonament pedagògic.** Manté els 5 blocs amb reforç visual (pictogrames a la taula bilingüe, gest). La voluntarietat es verbalitza explícitament; si el perfil té vergonya/inhibició documentada, la consigna de transferència s'orienta a producció privada (no comparteix públicament). Principi DUA d'Accés: cap barrera a l'expressió.

## Detecció

**Senyals docent** (quan activar el complement):
- Ha activat "TOLC" al Pas 2 i el perfil té `nouvingut: true` amb L1 coneguda.
- Vol usar la L1 com a recurs d'aprenentatge explícit.
- Treballa en un context plurilingüe on la diversitat lingüística és visible i valorada.

**Senyals alumne** (que indica que necessita el suport):
- Tradueix mot a mot des de L1 → errors de transferència directa (interferències).
- Al contrari: inhibició completa de la L1 per vergonya o normes de l'aula.
- Comprèn el concepte en L1 però no el pot articular en català.

**Context favorable**:
- Unitat TILC on el contingut disciplinar té terminologia específica que pot ancorarse a L1.
- Alumne nouvingut recent (< 2 anys a Catalunya) amb L1 desenvolupada.
- Aula culturalment diversa on el plurilingüisme és un valor pedagogic explícit.

**Anti-senyals** (quan NO activar):
- Perfil nouvingut no actiu → el complement no es genera.
- L1 desconeguda → es retorna advertència, no es genera.
- Objectiu és glossari de català monolingüe → `glossari`.
- Objectiu és bastides de lectura generals → `bastides_lectura`.

## Modulació per nivell

| Pas | Dimensió | Pre-A1 Emergent | A1 Inicial | A2 Funcional | B1 Estratègic | B2 Acadèmic | C1 Crític |
|---|---|---|---|---|---|---|---|
| **1. Activació** | Tipus de pregunta comparativa | Oral: "Com es diu X en la teva llengua?" — cap escriptura. El docent recull la resposta. | Pregunta oral + pictograma: "Com es diu [paraula clau] en la teva llengua?" Resposta optional escrita. | Activació escrita: "Com es diu «[concepte clau]» en la teva llengua?" | Activació comparativa: "«[concepte]» en [L1] s'expressa com ___. En català usem ___. Qué observes?" | Activació metalingüística: contrast de construccions gramaticals entre L1 i català. | Activació crítica: contrast entre sistemes lingüístics i convencions culturals del gènere discursiu. |
| **2. Acarament (taula bilingüe)** | Forma de l'acarament | Cap escriptura. Assenyalar o dibuixar el concepte. | Taula 2 columnes: 3-5 parells paraula L1 (alfabet original) / paraula català. | Taula 2 columnes: 3-5 parells + 1 observació de semblança/diferència estructural senzilla. | Contrast de connectors i construccions causals L1↔català. Taula o paràgraf breu. | Contrast de l'organització del gènere entre L1 i català. Com s'estructura el text en cada llengua. | Contrast d'intenció comunicativa i convencions retòriques entre L1 i català. Biaix cultural del gènere. |
| **3. Observació estructural** | Semblances primer | Cap observació: activitat oral i manipulativa. | Cap observació a A1: massa càrrega metalingüística. | 1 frase positiva: semblances primer, diferències com a curiositat. Mai observació negativa. | Observació sobre construcció causal o estructural (ordre SVO, posició adjectiu, connectors). | Observació sobre l'organització del gènere entre les dues llengues. Gèneres similars i divergents. | Observació crítica sobre com les dues llengues codifiquen el coneixement de forma diferent. Convencions retòriques. |
| **4. Consigna de transferència** | Pont de producció | Oral mediat: "Dibuixa o assenyala mentre ho dius." Dictat a l'adult si l'alumne vol escriure. | Dictat a l'adult o assenyalar. "Pots dir-ho en veu alta si vols." | Frase curta: escriu en català una idea del text usant un connector de la taula (si vols, primer en L1). | Paràgraf breu: resumir en L1 una part del text, o traduir una conclusió al català usant els connectors apressos. | Mediació complexa: mediar un text complet entre L1 i català. Comparar l'organització de les idees. | Contrast escrit: analitza com el gènere treballat es construiria diferent en L1 i en català. |
| **5. Caràcter voluntari** | Protecció de l'alumne | Sempre voluntari. "Si vols, si pots." Cap exposició pública. | Sempre voluntari. La consigna no exposa l'alumne. La taula és personal. | Voluntari. Mai exigir L1 públicament. "Comparteix-ho si vols" sempre present. | Voluntari. Mediació accessible sense revelar la L1 si l'alumne no vol. | Voluntari. L'alumne pot triar fer la mediació en L1 o directament en català. | Voluntari. L'alumne decideix el grau d'integració de la seva L1 en l'anàlisi crítica. |

## Casos especials

### nouvingut_L1_alfabet_no_llati

**Trigger:** nouvingut: true AND L1_script_in: [arab, han, ciril-lic, devanagari, hebreu, armeni, grec, georgia, thai]

**Modulació:**
- alfabet_original_obligatori: true
- transliteracio: opcional_addicional (mai substitueix l'original)
- columna_taula_ordre: [L1_alfabet_original, catala, transliteracio?]
- observacio_estructural_inclou: direccionalitat_escriptura (àrab/hebreu dreta-esquerra)

**Raonament pedagògic.** L'alfabet original és un acte de reconeixement de la llengua de l'alumne (H2 de l'skill). La transliteració sense l'original invisibilitza la L1: un alumne arabòfon que veu només "biologia" no veu la seva llengua a l'aula; en canvi, "بيولوجيا" al costat de "biologia" materialitza el principi del MALL (L1 com a recurs, no obstacle).

### L1_desconeguda

**Trigger:** nouvingut: true AND (L1: null OR L1: 'desconeguda')

**Modulació:**
- generar_complement: false
- retornar_advertencia: "TOLC requereix L1 declarada. Pregunta a l'alumne o família abans d'activar."
- log_motiu: L1_unknown

**Raonament pedagògic.** Sense L1 declarada no es pot construir cap pont cognitiu; fabricar L1 o assumir-la és un risc ètic que invisibilitza la llengua real de l'alumne. La decisió correcta és preguntar a l'alumne o família, no inventar.

### nouvingut_no_actiu

**Trigger:** nouvingut: false (independentment de si el docent ha activat TOLC al Pas 2)

**Modulació:**
- generar_complement: false
- saltar_silenciosament: true (sense advertència visible)

**Raonament pedagògic.** TOLC està dissenyat per a perfils nouvinguts amb L1 viva; aplicar-lo a alumnat plenament catalanoparlant no té sentit pedagògic. La salta silenciosa permet que el docent provi l'eina sense generar soroll.

### fase_lectora_logografica

**Trigger:** mecr_in: [pre_A1] AND fase_lectora: logografica

**Modulació:**
- acarament_taula: cap_taula_escrita
- substituir_per: assenyalar_o_dibuixar
- consigna_transferencia: oral_mediada (no_escriptura_autonoma)
- pas_2_descriptor: binary_no_aplica

**Raonament pedagògic.** A fase logogràfica l'alumne encara no descodifica grafies; demanar la lectura d'una taula bilingüe és incoherent amb la fase lectora real. La mediació es fa oral i manipulativa, preservant el principi TOLC sense forçar CALP en context BICS (Kuhn 1991, Cummins).

### fase_lectora_alfabetica_emergent

**Trigger:** mecr_in: [pre_A1] AND fase_lectora: alfabetica_emergent

**Modulació:**
- acarament_taula: 1-2_parells_maxim (no 3-5)
- escriptura_autonoma_catala: 1-2_paraules_clau
- consigna_transferencia: dictat_a_l_adult (amb opció minoritària d'escriptura voluntària)

**Raonament pedagògic.** L'alumne comença a descodificar però la càrrega cognitiva d'una taula 3-5 + alfabet original + català és excessiva. Reduir el nombre de parells permet activar el pont L1↔català sense saturar la memòria de treball; el dictat a l'adult preserva la mediació quan l'escriptura autònoma encara és costosa.

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici huma o LLM-jutge.
- `countable` — llindar quantitatiu verificable mecanicament.
- `structural` — requereix analisi sintatica o discursiva.
- `metacognitive` — descriptor de proces en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Activació | `binary` + `qualitative` | **si** | binary: presencia de pregunta comparativa L1↔català; qualitative: LLM-jutge sobre si la pregunta és específica del concepte del text font (positiu) o genèrica (negatiu); cross_source: verificar que el concepte de l'activació és del text font |
| 2 Acarament (taula bilingüe) | `binary` + `countable` + `qualitative` | no | binary: presencia de taula bilingüe a A1+ (cap taula a pre-A1); qualitative: LLM-jutge alfabet original de la L1 usat (no transliterat) — verificar coherència alfabètica amb la L1 declarada (àrab → arabic script; xinès → hanzi; ciríl·lic → ciríl·lic); countable: 3-5 parells a la taula (ni massa ni poc) |
| 3 Observació estructural | `binary` + `qualitative` | no | binary: absencia d'observació negativa ("en la teva llengua no hi ha X") — error pedagògic; qualitative: LLM-jutge sobre si l'observació comença per semblances (positiu) o per diferències (negatiu) |
| 4 Consigna de transferència | `qualitative` | **si** | qualitative: LLM-jutge sobre si la consigna de transferència és assolible al MECR declarat (dictat pre-A1/A1; frase A2; mediació B2+); binary: pre-A1 = cap escriptura autònoma; cross_source: verificar que la consigna de transferència referencia contingut o connector del text font (no una tasca genèrica) |
| 5 Caràcter voluntari | `binary` + `qualitative` | no | binary: presencia de clàusula de voluntarietat ("si vols", "si pots", "comparteix-ho si vols" o equivalent) en totes les consignes; detecció inicial per regex + LLM-jutge de seguiment (to realment no impositiu); absencia = error crític; qualitative: LLM-jutge sobre si el to de la consigna és genuïnament voluntari (positiu) o voluntari de paraula però impositiu de forma ("Ara escriu en la teva llengua" sense "si vols" = negatiu) |

**Notes:**
- Activació condicional: si el perfil no té `nouvingut: true` o L1 desconeguda → el complement es salta. Documentar al log.
- Alfabet original: la transliteració és acceptable ADICIONALMENT però no substitueix l'alfabet original. Detectar per LLM-jutge si l'alfabet és coherent amb la L1 declarada.
- Observació negativa: "en la teva llengua no hi ha..." és un error pedagògic que invalidiza la L1. Detectar per regex + LLM-jutge.
- Màxim 5 parells a la taula: si n'hi ha 6 o més, l'alumne es perd. Detectar per countable.

## Heurístiques docent

**H1 — La semblança com a entrada.**
Sempre comenzar per allò que les dues llengues comparteixen. Les diferències son interessants, no problemàtiques. "En la teva llengua i en català les dues funcionen igual en aquest punt" és el millor punt de partida. Si les diferències arriben primer, l'alumne pot sentir la seva L1 com a "defectuosa" — l'efecte contrari del que busquem.

**H2 — Alfabet original com a dignitat lingüística.**
Escriure la paraula en àrab, xinès o ciríl·lic en l'alfabet original (no transliterat) és un acte de reconeixement de la llengua de l'alumne. Un alumne arabòfon que veu "بيولوجيا" al costat de "biologia" veu que la seva llengua té presència real a l'aula. La transliteració "biologia" sense l'original és invisible.

**H3 — La clàusula de voluntarietat és sempre present.**
Quan proposo l'activitat de TOLC, diuen sempre la clàusula de voluntarietat EXPLÍCITAMENT en veu alta, no només al full: "Si vols i si pots, comparteix com es diu en la teva llengua. Si prefereixes no dir-ho, perfectament." Aquesta verbalització normalitza la voluntarietat i garanteix un espai segur.

**H4 — TOLC com a eina, no com a examen de L1.**
El TOLC no avalua la L1 de l'alumne. L'alumne que no sap escriure en L1 (o que ha perdut la L1 per pressió d'assimilació) no és el subjecte d'aquesta activitat. Si l'alumne no pot o no vol participar, l'activitat és transparent per a ell. Mai imputar un rendiment a la L1.

**H5 — La taula bilingüe durant la lectura, no al final.**
La taula bilingüe té màxim valor si l'alumne la consulta DURANT la lectura, quan troba un terme difícil. No és una activitat que es fa al final. El flux correcte: lectura del text → trobar terme difícil → consultar taula → activar xarxa semàntica en L1 → continuar la lectura. Assegurar que la taula és accessible (no plegada, no al fons de la carpeta) durant la sessió de lectura.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## TOLC / Transllenguatge
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
### 1. Activació
### 2. Acarament L1 ↔ català
### 3. Observació estructural
### 4. Consigna de transferència
### 5. Caràcter voluntari
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
[L1: <codi_iso>]
[ALFABET_ORIGINAL: <script>]
```

**Headers explícitament PROHIBITS:**
```
## TOLC
## Transllenguatge
## Taula bilingüe
```

**Regla d'integritat estructural.** Sense `## TOLC / Transllenguatge` i els 5 H3 numerats en ordre estricte, el parser de pas3.html no detecta el bloc i la rúbrica 5×6 no s'ancora al text. Si falta el H3 `### 5. Caràcter voluntari` o la clàusula «si vols, si pots» equivalent, el guardrail ètic salta i el bloc es rebutja: la voluntarietat absoluta és condició no negociable de l'skill.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengues i Literacitat): transllenguatge, TOLC, PBCS, L1 com a recurs cognitiu.
- Cummins, J. (2008): "Teaching for transfer: Challenging the two solitudes assumption in bilingual education" — Hipòtesi d'Interdependència (les competencies de L1 transfereixen a L2).
- García, O. & Wei, L. (2014): *Translanguaging: Language, Bilingualism and Education* — repertori lingüístic com a recurs pedagògic.
- Decret 175/2022 (curriculum Catalunya): plurilingüisme, competencia en comunicacio lingüística i dimensio intercultural.
