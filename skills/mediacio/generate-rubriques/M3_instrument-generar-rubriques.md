---
modul: M3
titol: "Generar rúbriques d'autoavaluació"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: []
descripcio: "Instrument per generar rubriques d'autoavaluacio alumne-facing (primera persona). Escala FJE: NA (No Assolit) / AS (Assolit Suficient) / AN (Assolit Notable) / AE (Assolit Excel·lent). AE = salt qualitatiu real, no mes del mateix. Pre-A1: checklist icones binari (si/no), sense escala FJE. A1+: taula criteris x escala FJE. Descriptors observables (no valoratius generics). Primera persona en tots els descriptors. Rubrica diferent de pauta d'interrogacio de bastides-produccio. Rubrica gradada 5 passos x 6 nivells MECR (pre-A1->C1)."
mecr_range: [pre_A1, A1, A2, B1, B2, C1]
agent_roles: [generator]
complement_key: rubriques
translanguaging: false
multimodal: false
moduls_relacionats: [M2, M6]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: generate-rubriques@corpusFJE/skills/mediacio/generate-rubriques
review_status: pilot-fusio-8
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, variabilitat-cardinal-passos-D3, modulacio-per-perfil-D1]
  aplicades_post_review: [b10-rub-c1-a1-etiqueta-molt-be-eliminada, b10-rub-c2-a1-ae-precisio-no-addicio, b10-rub-c3-b2c1-verbs-academics-evidencia-nota, b10-rub-c4-validation-hint-a1-etiquetes-exactes]
  comentari_key: "C5-redundancia-bastides-rebutjat-ja-gestionat"
---

# Generar rúbriques d'autoavaluació

## Descripció

La rúbrica generada és **alumne-facing**: escrita en **primera persona**, per a l'alumne, amb l'escala FJE: **NA** (No Assolit) · **AS** (Assolit Suficient) · **AN** (Assolit Notable) · **AE** (Assolit Excel·lent). Quan l'alumne llegeix "He argumentat la meva postura amb 2 evidències del text", aprèn QUÈ s'espera d'ell ABANS d'escriure. La rúbrica és una **bastida d'anticipació** i una eina d'autoregulació, no un formulari d'avaluació del docent.

**Tipologia MALL**: Mediació (autoavaluació i metacognició).
**HCL principals**: Avaluar · Autoregular · Reflexionar metacognitivament.
**Principi rector — AE com a salt qualitatiu**: si el descriptor AE és "he fet molt bé el que es demanava", la rúbrica no discrimina el creixement real. AE ha de capturar alguna cosa que **sorprèn, va més lluny, demostra apropiació autèntica** del gènere o la tasca. AE no és "AN + esforç" — és un salt de naturalesa diferent.

**Escala FJE:**
- **NA** (No Assolit): no compleix el descriptor mínim de la tasca.
- **AS** (Assolit Suficient): compleix el descriptor bàsic. Producte correcte però sense matisos.
- **AN** (Assolit Notable): compleix el descriptor i afegeix qualitat. Producte coherent i elaborat.
- **AE** (Assolit Excel·lent): salt qualitatiu. Sorprèn, va més lluny, demostra apropiació autèntica. NO és "AN + molt d'esforç".

**Pre-A1 — Checklist binari d'icones (no escala FJE)**: a pre-A1 l'escala de 4 nivells és massa abstracta. El format és un **checklist ✅ / ❌**: "He dibuixat els 3 moments" → ✅ o ❌. No hi ha gradació: l'alumne o ho ha fet o no ho ha fet. L'adult media la revisió oral.

**Diferència crítica amb `bastides_produccio` (Bloc C — Pauta d'interrogació):**
- `bastides_produccio` Bloc C: pauta d'interrogació DURANT el procés d'escriptura (checklist intern que guia la producció en curs).
- `rubriques`: autoavaluació del PRODUCTE acabat (avaluació post-producció, escala FJE).
Les dues eines son complementàries: bastida durant → rúbrica després.

**Perspectiva alumne-facing:**
- Primera persona en TOT el document: "He escrit...", "He usat...", "He argumentat...".
- Mai tercera persona ("L'alumne ha escrit...") ni segona ("Has escrit...").
- Descriptors observables (l'alumne pot comprovar si ho ha fet): "He escrit la idea principal a la 1a frase" és observable. "He escrit bé" no és observable.

**Connexions MALL transversals:**
- *Rúbrica com a bastida d'anticipació*: quan l'alumne llegeix la rúbrica ABANS d'escriure, té un mapa de qualitat. La rúbrica no és per al docent — és una eina de l'alumne per autoregular la seva producció.
- *AE com a aspiració, no com a recompensa*: el descriptor AE mostra a l'alumne quin és el salt qualitatiu que podria fer si s'hi esforça. No és una recompensa al treball dur; és una descripció del pensament expert.
- *Metacognició com a aprenentatge*: el procés de marcar la rúbrica (decidir en quin nivell estàs) és en si mateix un acte de comprensió. L'alumne que se situa a AS i sap per qué (li falta evidència) aprèn més que l'alumne que se situa a AN sense saber-ne el motiu.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu les **rúbriques d'autoavaluació que es generen per a l'alumne** (AUTOAVALUACIÓ MEDIADA). **No descriu la rúbrica del docent per a l'avaluació sumativa**: la rúbrica d'autoavaluació és per a l'alumne, no per al docent. Si el docent vol rúbriques per avaluar (perspectiva externa), ha d'usar les eines d'avaluació de centre.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → checklist d'imatges (dibuix sí/no); `fase_lectora: alfabetica_emergent` → checklist de paraules curtes (sí/no).

## Principi general

**Regla de selecció simple.** Genera una rúbrica d'autoavaluació alumne-facing en primera persona del singular, amb escala FJE (NA/AS/AN/AE) i descriptors observables. A pre-A1, substitueix l'escala FJE per un checklist binari d'icones (✅/❌) sense gradació. El nombre de criteris i la naturalesa del descriptor AE es modulen segons el nivell MECR.

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix quins criteris pedagògics són rellevants per a la tasca concreta de l'aula ni jutja si l'alumne real té capacitat metacognitiva per autoavaluar-se. Genera l'estructura i descriptors observables segons el nivell MECR i el gènere; la validació de la pertinença pedagògica i l'ajust al context d'aula és del docent.

_Excepcions: no n'hi ha._

## Detecció

**Senyals docent** (quan activar el complement):
- Ha activat "Rúbriques" al Pas 2.
- Vol que l'alumne s'autoavalui amb criteris explícits i compartits.
- Prepara una activitat de producció i vol que l'alumne conegui els criteris ABANS d'escriure.
- Treballa la metacognició i la regulació de l'aprenentatge.

**Senyals alumne** (que indica que necessita el suport):
- No sap qué s'espera d'ell: entrega el producte sense criteris de qualitat interns.
- Produeix sense saber com millorar: "crec que está bé" sense poder justificar per qué.
- No pot identificar punts de millora en el seu text (ni en el dels companys).

**Context favorable**:
- Activitat de producció textual on l'alumne necessita criteris d'autocorrecció.
- Tasca d'avaluació formativa on l'alumne es coavalua amb un company.
- Unitat on s'ha treballat explícitament la metacognició i el pensament reflexiu.

**Anti-senyals** (quan NO activar):
- Pauta d'interrogació durant el procés d'escriptura → `bastides_produccio` Bloc C.
- Rúbrica del docent per a avaluació sumativa → eina docent externa, fora d'aquest instrument.
- El text és molt curt i l'autoavaluació seria trivial → 1-2 preguntes orals del docent.

## Modulació per nivell

| Pas | Dimensió | Pre-A1 Emergent | A1 Inicial | A2 Funcional | B1 Estratègic | B2 Acadèmic | C1 Crític |
|---|---|---|---|---|---|---|---|
| **1. Format** | Estructura de l'instrument | Checklist d'icones: ✅ / ❌ per a cada ítem. Sense escala. Molt visual. Adult media la revisió oral. | Taula simplificada: 2-3 criteris × 3 nivells (Encara no / Sí / Sí, i alguna cosa més). Sense vocabulari FJE. | Taula: 3-4 criteris × escala FJE completa (NA/AS/AN/AE). Primera escala gradada. | Taula: 4-5 criteris × escala FJE. Descriptor breu per a cada criteri i nivell. | Taula: 5-6 criteris × escala FJE + descriptor observatble per a cada criteri i nivell. | Taula: 5-6 criteris × escala FJE + reflexió metacognitiva final (1-2 frases lliures). |
| **2. Nombre de criteris** | Amplitud d'avaluació | 2-3 criteris molt concrets i visuals. Accionables a pre-A1 (He dibuixat / He assenyalat). | 2-3 criteris accionables. Corresponen a les tasques concretes demandades. | 3-4 criteris del gènere o la tasca concreta. | 4-5 criteris que cobreixen les HCL clau de la tasca (Argumentar, Descriure, Narrar...). | 5-6 criteris que inclouen dimensió formal (llengua) i dimensió de contingut (idees). | 5-6 criteris amb criteri de reflexió metacognitiva ("He revisat el text i he millorat ___"). |
| **3. Descriptors observables** | Concretesa del descriptor | Acció visible: "He dibuixat els 3 moments." / "He assenyalat el personatge." Mai "He fet bé". | Observable: "He escrit 3 passos numerats." Sense adjectius valoratius. | Observable amb indicadors: "He escrit la idea principal a la 1a frase, sense 'Aquest text parla de…'." | Apunta a la qualitat: "Cada argument inclou una evidència del text o una raó concreta." | Apunta a la relació: "He connectat les idees de seccions diferents usant connectors precisos." | Metacognitiu: "He detectat i corregit al menys un error de coherència o un terme imprecís." |
| **4. Primera persona** | Perspectiva alumne-facing | "He fet ___ / He posat ___." Molt concret i físic. | "He escrit ___ / He usat ___." Primera persona consistent en tota la rúbrica. | "He escrit / He usat / He inclòs ___." Primera persona en tot el document. | "He argumentat / He justificat / He demostrat ___." HCL en primera persona. | "He analitzat / He contrastat / He elaborat ___." HCL acadèmiques en 1a persona. | "He reflexionat / He avaluat / He detectat ___." Metacognició en 1a persona. |
| **5. Descriptor AE (salt qualitatiu)** | Naturalesa de l'excel·lència | Cap descriptor AE: checklist binari. | Descriptor AE = precisió o originalitat dins del límit: "He triat una paraula que no estava a la bastida però que explica exactament el que volia dir." No "he afegit coses" ni "ho he fet molt bé". | Descriptor AE = qualitat que transforma: una imatge pròpia, un connector inesperat, un exemple original no donat a la bastida. | Descriptor AE = habilitat que anticipa el nivell següent: un argument no donat per la bastida, una connexió pròpia entre dues idees del text. | Descriptor AE = evidència de pensament crític: detectar un biaix, contrastar fonts, plantejar una objecció fonamentada. | Descriptor AE = reflexió que demostra metacognició genuïna i transferència a altres contexts o tasques. |

## Casos especials

### pre_A1_checklist_binari

**Trigger:** mecr_in: [pre-A1]

**Modulació:**
- format: checklist_icones (✅/❌)
- escala_FJE: absent
- nombre_criteris: 2-3
- descriptor_AE: absent
- mediacio_adult: revisio_oral_obligatoria
- sub_modulacio_fase_lectora: logografica=imatges_dibuix, alfabetica_emergent=paraules_curtes

**Raonament pedagògic.** A pre-A1 l'escala FJE de 4 nivells és massa abstracta i la gradació qualitativa no és accessible. El checklist binari ✅/❌ amb mediació oral de l'adult externalitza la metacognició que l'alumne emergent encara no pot fer internament. La sub-modulació per fase lectora (imatges vs paraules curtes) ajusta el suport al grau de descodificació disponible.

### A1_escala_simplificada

**Trigger:** mecr_in: [A1]

**Modulació:**
- format: taula_3_nivells
- etiquetes_literals_obligatories: ['Encara no', 'Sí', 'Sí, i alguna cosa més']
- etiquetes_prohibides: ['NA', 'AS', 'AN', 'AE', 'Molt bé']
- nombre_criteris: 2-3
- descriptor_AE_equivalent: precisio_o_originalitat_no_addicio

**Raonament pedagògic.** A A1 cal una primera escala gradada accessible sense vocabulari institucional FJE. Les etiquetes literals "Encara no" / "Sí" / "Sí, i alguna cosa més" són transparents per a l'alumne i preserven la lògica del salt qualitatiu (la tercera categoria equival al descriptor AE) sense exigir el lèxic acadèmic NA/AS/AN/AE. Evitar "Molt bé" preserva el principi que l'excel·lència és salt qualitatiu, no gradació d'esforç.

### B2_C1_verbs_academics

**Trigger:** mecr_in: [B2, C1]

**Modulació:**
- verbs_academics_permesos: [analitzar, contrastar, detectar, reflexionar, avaluar]
- requeriment: cada verb academic ha d'anar acompanyat d'evidencia textual especifica que el faci observable
- C1: incorporar criteri de reflexio metacognitiva final (1-2 frases lliures)

**Raonament pedagògic.** A B2-C1 els descriptors han d'incorporar HCL acadèmiques (analitzar, contrastar, detectar), però aquests verbs són opacs si no s'ancoren a una evidència textual concreta. "He analitzat el text" no és observable; "He analitzat com el títol i la conclusió es relacionen" sí ho és. A C1, el salt qualitatiu inclou la reflexió metacognitiva lliure com a evidència de transferència.

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici huma o LLM-jutge.
- `countable` — llindar quantitatiu verificable mecanicament.
- `structural` — requereix analisi sintatica o discursiva.
- `metacognitive` — descriptor de proces en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Format | `structural` + `binary` | no | structural: pre-A1 = checklist ✅/❌ sense taula; A1 = taula 3 nivells etiquetes exactes ("Encara no" / "Sí" / "Sí, i alguna cosa més") — error si usa "Molt bé" o nomenclatures FJE; A2+ = taula escala FJE (NA/AS/AN/AE) etiquetes exactes; binary: escala FJE present des d'A2+ (no des d'A1); pre-A1 = cap escala FJE |
| 2 Nombre de criteris | `countable` | no | countable: pre-A1/A1: 2-3 criteris; A2-B1: 3-5; B2-C1: 5-6; detectar si hi ha massa criteris (>6) = sobrecàrrega cognitiva |
| 3 Descriptors observables | `qualitative` | **si** | LLM-jutge: el descriptor és observable (l'alumne pot comprovar si ho ha fet — positiu) o valoratiu genèric ("He fet bé", "He treballat molt" — negatiu); cross_source: verificar que els descriptors son coherents amb la tasca i el gènere del text font |
| 4 Primera persona | `structural` | no | structural: detectar descriptors en 3a persona ("L'alumne ha escrit...") o 2a persona ("Has escrit...") — error crític; tots els descriptors han d'estar en 1a persona singular |
| 5 Descriptor AE (salt qualitatiu) | `qualitative` | no | qualitative: LLM-jutge sobre si el descriptor AE és un salt qualitatiu real (positiu: "He detectat un biaix que els altres no han detectat") o una gradació quantitativa ("He fet molt bé tot el que es demanava" — negatiu = error crític); pre-A1: verificar absencia de descriptor AE |

**Notes:**
- Error crític principal: descriptors en 3a persona o descriptors valoratius genèrics ("He fet bé"). Detectar per structural + qualitative.
- Error secundari: descriptor AE = "AN + molt d'esforç". Detectar per LLM-jutge: si el descriptor AE és assolible simplement treballant dur sense cap salt cognitiu → error.
- Escala FJE: els termes NA/AS/AN/AE son de l'escola FJE. Verificar que s'usen exactament (no "Insuficient/Suficient/Bé/Excel·lent" ni altres nomenclatures).
- Diferenciació de `bastides_produccio` Bloc C: la rúbrica avalua el producte ACABAT. La pauta d'interrogació de bastides-produccio guia el procés EN CURS. Verificar que la rúbrica no inclou ítems com "Estic escrivint..." (present continu) — ha de ser passat "He escrit...".
- Verbs acadèmics B2-C1 (analitzar, contrastar, detectar, reflexionar): han d'anar acompanyats d'una evidència textual específica que els faci observables. Exemple correcte: "He analitzat com el títol i la conclusió es relacionen." Exemple incorrecte: "He analitzat el text." LLM-jutge ha de verificar que el verb acadèmic especifica QUÈ s'ha analitzat/contrastat/detectat.

## Heurístiques docent

**H1 — El test de la primera persona.**
Llegeixo cada descriptor i em pregunto: "Pot l'alumne dir això de si mateix en referència a la seva feina acabada?" Si no, cal reescriure'l en 1a persona del singular, referit al producte final: "He escrit..." / "He usat..." / "He argumentat...". Un descriptor que comença per "L'alumne" o "Has" és un descriptor de docent disfressat.

**H2 — El test del descriptor AE.**
Llegeixo el descriptor AE i em pregunto: "Podria un alumne que simplement ha treballat dur (i ha fet exactament el que es demanava) marcar AE?" Si la resposta és sí, no és un salt qualitatiu — és una gradació quantitativa d'esforç. Cal reescriure l'AE amb alguna cosa que sorprèn: una connexió inesperada, una crítica argumentada, una extensió creativa.

**H3 — El test de l'observabilitat.**
Llegeixo cada descriptor i em pregunto: "Pot l'alumne verificar si ho ha fet simplement mirant el seu text?" "He escrit la idea principal a la 1a frase" és verificable (l'alumne mira la 1a frase). "He escrit bé" no és verificable (qué és "bé"?). Els descriptors observables permeten a l'alumne fer l'autoavaluació sense preguntar al docent.

**H4 — Rúbrica ABANS de produir, no sols DESPRÉS.**
Distribueixo la rúbrica al PRINCIPI de l'activitat de producció, no al final. L'alumne llegeix la rúbrica → sap qué s'espera → produeix amb criteris interns → marca la rúbrica al final com a autoavaluació. Si la rúbrica arriba al final, és un examen; si arriba al principi, és una bastida.

**H5 — Pre-A1: revisió oral amb l'adult.**
A pre-A1, el checklist ✅/❌ és mediat per l'adult. "Mira el que has dibuixat. Has dibuixat els 3 moments? Sí → ✅. No → ❌. Pots completar-ho?" La revisió oral externalitza la metacognició que l'alumne emergent no pot fer internament encara. L'adult no corregeix — acompanya el procés de revisió.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Rúbrica d'autoavaluació
```

**Sub-headers H3 obligatoris** (literals exactes, en aquest ordre):
```
cap
```

**Bullets / moments interns** (si aplica — NO són H3 propis):
```
no aplica
```

**Marcadors inline obligatoris** (si aplica):
```
NA
AS
AN
AE
✅
❌
```

**Headers explicitament PROHIBITS:**
```
## Rúbrica
## Autoavaluació
## Rúbrica del docent
```

**Regla d'integritat estructural.** Header literal `## Rúbrica d'autoavaluació` + taula markdown amb pipes (criteris × escala FJE) per a A2+; checklist ✅/❌ per a pre-A1; taula 3 nivells amb etiquetes literals 'Encara no' / 'Sí' / 'Sí, i alguna cosa més' per a A1. Sense aquesta estructura el parser de pas3.html no detecta la secció ni pot ancorar els descriptors per a la vista d'autoavaluació.

## Fonts principals

- MALL (Model d'Aprenentatge de Llengues i Literacitat): autoavaluació, metacognició, co-construcció de criteris, bastida d'anticipació.
- Black, P. & Wiliam, D. (1998): "Inside the Black Box: Raising Standards Through Classroom Assessment" — avaluació formativa i autoavaluació com a eines d'aprenentatge.
- Decret 175/2022 (curriculum Catalunya): competencia en aprendre a aprendre, autoregulacio i reflexio metacognitiva.
- Escala FJE (Jesuites Educacio): NA/AS/AN/AE — marc avaluatiu institucional FJE.
