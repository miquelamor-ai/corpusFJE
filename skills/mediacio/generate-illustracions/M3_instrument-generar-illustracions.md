---
modul: M3
titol: "Generar il·lustracions"
tipus: instrument
categoria_principal: mediacio
categories_secundaries: []
descripcio: "Instrument per inserir marcadors d'il·lustracions IA al text adaptat. Format: [IMATGE: concepte curt en catala]. Backend: Wikimedia (llicencia lliure) → FLUX (generativa) → skip. 7 presets d'estil. Pre-A1/A1 davant del concepte com a anticipacio; A2+ al costat o dins del paragraf. Principi 'menys és mes': maxim 3-4 per document. Rubrica gradada 5 passos × 6 nivells MECR (pre-A1→C1)."
mecr_range: [pre_A1, A1, A2, B1, B2, C1]
agent_roles: [generator]
complement_key: illustracions
translanguaging: false
multimodal: true
moduls_relacionats: [M2, M3]
variables_configurables:
  fase_lectora: [logografica, alfabetica_emergent, alfabetica_fluida]
skill_meta: generate-illustracions@corpusFJE/skills/mediacio/generate-illustracions
review_status: pilot-fusio-8
version: 4.0.0-canonic
generat_at: 2026-05-26
actualitzat_at: 2026-05-26
notebooklm_review:
  data: 2026-05-26
  veredicte: si-amb-correccions-menors
  aplicades_des_d_inici: [patro-canonic-pilots-fase-a, aclariment-us-lectura-vs-produccio-C1, variabilitat-cardinal-passos-D3, modulacio-per-perfil-D1]
  aplicades_post_review: [b7-illustr-pas3-requires-source, b7-illustr-pas5-c1-na, b7-illustr-antisenyal-polisemics]
  comentari_key: "pas3-requires-source-text-si-especificitat-vs-font; pas5-c1-marcat-na; anti-senyals-conceptes-polisemics-afegit"
---

# Generar il·lustracions

## Descripció

El complement d'il·lustracions insereix marcadors `[IMATGE: concepte curt en catala]` al text adaptat perquè es resolguin en imatges. Es proven tres vies en ordre: Wikimedia Commons (imatges reals amb llicencia lliure), FLUX.1-schnell (generació IA), skip (si el concepte no és visualitzable). La il·lustració no decora — ancla conceptes que son difícils de descriure verbalment.

**Tipologia MALL**: Mediacio (suport multimodal cognitiu).
**HCL associada**: cap HCL productiva — el complement suporta l'acces i l'ancoratge conceptual del text.
**Principi rector**: menys és mes. Cada il·lustració afegeix carrega cognitiva de processament visual. A B2-C1, una il·lustració sense valor informatiu addicional distreu en lloc d'ancorar.
**Feature BETA**: qualitat no garantida; demora de 1-3 minuts per imatge; el docent sempre pot substituir o regenerar.

**Format del marcador:**
```
[IMATGE: concepte curt en catala]
```
- Delimitadors obligatoris: `[IMATGE:` a l'inici, `]` al final.
- Idioma: catala. Es tradueix si cal.
- En linia propia, DAVANT del paragraf on s'introdueix el concepte (pre-A1/A1) o al costat (A2+).
- Longitud: 3-8 paraules. Concepte nuclear, no descripcio d'escena.
- Mai dins de llistes, taules, bastides, glossaris, pictogrames o altres complements.
- Mai incloure estil, paleta, viewpoint o enquadrament (s'afegeix automaticament).

**Els 7 presets d'estil** (el docent tria al Pas 2; si no, s'aplica el default per MECR + assignatura):

| Preset | Per a qui / quan |
|---|---|
| Aquarel·la storybook | Primaria, LF, nouvinguts, literatura, A1-A2 |
| Vectorial editorial pla | ESO+, humanitats, conceptes abstractes, B1+ |
| Isometric infografic | STEM, processos, sistemes, diagrames, A2+ |
| Icona minimalista | DUA Acces, vocabulari abstracte, glossari visual |
| Claymation plastilina | Primaria STEM ludic, infantil, A1-B1 |
| Escala de grisos (carbonet) | Historia, filosofia, impressio B/N, baixa visio |
| Fotografia documental | Natura, arquitectura, geografia, ciencia actual |

**Diferencia clau amb pictogrames:**
- **Pictogrames**: sistema AAC (emojis o ARASAAC), vocabulari, referencia lexica, TEA/CAA.
- **Il·lustracions**: ancoratge conceptual de processos, sistemes, llocs, escenes; no és AAC.

**Connexions MALL transversals:**
- *Imatge com a bastida d'acces (pre-A1/A1)*: l'alumne nouvingut que no coneix "fotosintesi" pot aprendre el concepte si veu la imatge PRIMER. La sequencia imatge → paraula és la logica de l'aprenentatge, no la del text.
- *Imatge com a ampliacio cognitiva (B1+)*: als nivells alts, la il·lustració no simplifica — complexifica. Un diagrama pot donar en un cop d'ull la informacio que requereix 3 paragraf de text. L'ampliacio és el valor afegit, no la simplificacio.
- *Preset com a coherencia de registre*: triar el preset adequat al context (aquarel·la per a primaria, vectorial per a ESO) és una decisio pedagogica sobre el registre visual. Un poema il·lustrat amb infografic isometric envia un missatge contradictori.

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **complement d'il·lustracions generat per al text adaptat**. **No descriu la produccio autonoma de l'alumne**: els marcadors s'insereixen al text adaptat i les imatges es generen automàticament. El registre d'us és del docent (observacio de si l'alumne usa el suport visual durant la lectura).

## Principi general

**Regla de selecció simple.** Insereix marcadors `[IMATGE: concepte curt en català]` només davant o al costat de conceptes visualitzables que ancoren idees clau del text (processos, sistemes, llocs, escenes, objectes concrets). Aplica el principi 'menys és més': respecta el sostre per nivell MECR (pre-A1: ≤5; A1: ≤4; A2: ≤3; B1-B2: ≤2; C1: ≤1) i no marquis conceptes abstractes purs, microscòpics sense escala macro, ni polisèmics sense desambiguació al marcador.

**Límits del LLM (no judici qualitatiu complex).** El LLM no decideix si una il·lustració concreta ajudarà aquest alumne real ni jutja la qualitat estètica del resultat visual; tampoc tria el preset d'estil definitiu. Identifica candidats segons visualitzabilitat i centralitat al text font, i delega al docent al Pas 3 la decisió final (esborrar, regenerar, substituir, canviar preset).

_Excepcions: no n'hi ha._

## Regla de selecció per perfil

### alumne_DUA_acces

**Inclou si:**
- conceptes_visualitzables_centrals_al_text
- conceptes_que_requereixen_ancoratge_visual_per_descodificacio
- marcador_en_linia_propia_DAVANT_del_concepte (fins i tot a A2+)

**Exclou explicitament:**
- conceptes_abstractes_sense_referent_visual
- conceptes_polisemics_sense_desambiguacio

**Raonament pedagògic.** Activa preset 'Icona minimalista' o 'Aquarel·la storybook' segons fase lectora i manté densitat al sostre màxim del nivell. Per a baixa visió, preset 'Escala de grisos (carbonet)' amb contrast alt. La imatge davant del concepte garanteix accés alternatiu al significat (Mayer, principi de contigüitat).

### alumne_AACC_o_capacitat_alta

**Inclou si:**
- conceptes_que_aporten_complexitat_addicional
- diagrames_densos_en_informacio
- infografies_que_condensin_dades

**Exclou explicitament:**
- il·lustracions_decoratives
- conceptes_obvis_o_ja_dominats

**Raonament pedagògic.** Densitat al límit inferior del rang del nivell (B1: 1; B2-C1: 0-1) i preset 'Isomètric infogràfic' o 'Vectorial editorial' per privilegiar diagrames densos sobre il·lustracions decoratives. El sostre alt es manté: la il·lustració aporta valor informatiu addicional, no simplifica.

### alumne_nouvingut_amb_L1

**Inclou si:**
- conceptes_universals_i_concrets_traduibles_culturalment
- marcador_SEMPRE_en_linia_propia_DAVANT_del_paragraf

**Exclou explicitament:**
- referents_culturalment_marcats_sense_context_addicional

**Raonament pedagògic.** Densitat al límit superior del rang (pre-A1: 5; A1: 4; A2: 3) i preset 'Aquarel·la storybook' o 'Fotografia documental' per a màxima recognoscibilitat. La seqüència imatge → paraula és la lògica de l'aprenentatge inicial (MALL, Lectura Fàcil); el nouvingut accedeix al concepte abans de descodificar el mot.

## Detecció

**Senyals docent** (quan activar el complement):
- Ha activat "Il·lustracions" al Pas 2.
- El text adaptat conte conceptes visuals que l'alumne pot no conèixer o que son difícils de representar verbalment.
- La materia és visual per naturalesa (ciencies naturals, historia, geografia, educacio artistica).

**Senyals alumne** (que indica que necessita el suport):
- Llegeix paraules sense imatge mental del concepte (mai ha vist un volca, una balena, una fabrica del s. XIX).
- El vocabulari esta desconnectat del significat referencial.

**Context favorable**:
- Ciencies naturals (ecosistemes, organs, processos biologics).
- Historia (monuments, escenes historiques, artefactes culturals).
- Politiques STEM: diagrames, infografies, mapes de conceptes visuals.
- Educacio artistica (tecniques visuals, estils, artistes).

**Anti-senyals** (quan NO activar):
- El text és abstracte i purament verbal (matematiques de calcul, filosofia) → cap il·lustració.
- El concepte és tècnic-microscopic (cel·lula, atom, enzim) → formular a escala macro o ometre.
- El concepte no te representacio visual clara → no posar el marcador.
- El concepte és polisemic sense context suficient al marcador → especificar el context al marcador (ex.: "banc" → `[IMATGE: banc de peixos]` o `[IMATGE: banc de fusta al parc]`; mai `[IMATGE: banc]`).
- Suport lexic sistematic → complement `pictogrames`.
- Esquema visual del contingut → complement `mapa-conceptual`.

## Modulació per nivell

| Pas | Dimensió | Pre-A1 Emergent | A1 Inicial | A2 Funcional | B1 Estratègic | B2 Acadèmic | C1 Crític |
|---|---|---|---|---|---|---|---|
| **1. Nombre d'il·lustracions** | Densitat | Maxim 4-5. Una per idea principal. Alta densitat justificada (text ≈ imatge). | 3-4 il·lustracions. Una per paragraf o per concepte clau. | 2-3 il·lustracions. Als punts de maxim ancoratge conceptual. | 1-2 il·lustracions als conceptes abstractes o processos clau. | 1-2 il·lustracions molt selectives (diagrama, proces, dada visual clau). | 0-1 il·lustració. Reservada per a diagrames o infografies que condensin dades. |
| **2. Posicio al text** | Anticipacio vs ancoratge | Imatge DAVANT de la paraula/frase que il·lustra. L'alumne veu la imatge PRIMER. Anticipacio visual. | Imatge immediatament DAVANT o AL COSTAT del concepte clau. | Imatge al costat del concepte que ancora, dins del paragraf. | Imatge al concepte abstracte o al proces que beneficia d'ancoratge visual. | Imatge estrategica: diagrama d'un proces, taula de dades, mapa conceptual visual. | Imatge de suport a l'argument: infografia, grafic, mapa. |
| **3. Especificitat del marcador** | Concretesa del concepte | Concepte molt concret i universal: "gat", "arbre", "pluja". 1-2 paraules. | Concepte concret: "cel·lula animal", "volca en erupcio". 1-3 paraules. | Concepte concret + context: "fotosintesi a fulla verda". 2-4 paraules. | Concepte especific del contingut: "cadena trofica marina", "cambra del parlament". | Concepte disciplinar: "diagrama de l'aparell respiratori", "mapa de la Revolucio Francesa". | Concepte complex: "infografia comparativa de sistemes politics", "grafic evolucio PIB". |
| **4. Preset d'estil** | Registre visual | Pictograma o il·lustració clara i simple. Sense elements distractors. | Il·lustracò o foto realista. Molt clara, sense text a la imatge. | Foto realista o il·lustracó educativa. Pot tenir etiquetes simples. | Diagrama o foto cientifica/geografica. Etiquetes disciplinars. | Diagrama, mapa, grafic. Llegenda si cal. | Infografia, grafic estadistic, mapa tematic. |
| **5. Autoavaluacio mediada** | Metacognicao | "He vist la imatge i he dit el que era." (oral, mediat per adult) | "He mirat la imatge i m'ha ajudat a entendre la paraula difícil." | "La imatge m'ha ajudat a entendre el proces o el concepte." | "He identificat quins conceptes necessitaven imatge i quins no." | "He usat les il·lustracions com a suport visual per a conceptes que no s'expliquen facilment amb paraules." | — (N/A: a C1 rarament es genera il·lustracó; si es genera, l'autoavaluacio és igual que B2) |

## Casos especials

### pre_A1_A1_anticipacio_visual

**Trigger:** mecr_in: [pre-A1, A1] OR fase_lectora_in: [logografica, alfabetica_emergent]

**Modulació:**
- posicio: marcador en línia pròpia DAVANT del paràgraf (no al costat ni darrere)
- densitat: fins a 4-5 marcadors a pre-A1 i 3-4 a A1
- especificitat: concepte molt concret i universal (1-3 paraules: 'gat', 'volcà en erupció')
- preset: aquarel·la storybook o claymation per defecte

**Raonament pedagògic.** La seqüència imatge → paraula és la lògica de l'aprenentatge inicial (MALL, Lectura Fàcil); l'alumne nouvingut o emergent ha de poder accedir al concepte abans de descodificar el mot.

### concepte_polisemic

**Trigger:** el concepte té múltiples referents visuals sense context suficient (p.e. 'banc', 'pla', 'cua', 'arc')

**Modulació:**
- marcador: SEMPRE desambiguar al propi marcador (`[IMATGE: banc de peixos]` o `[IMATGE: banc de fusta al parc]`, mai `[IMATGE: banc]`)
- si_no_desambiguable_en_3_8_paraules: ometre el marcador

**Raonament pedagògic.** El resolver Wikimedia/FLUX no té context del paràgraf; un marcador ambigu retorna una imatge irrellevant que distorsiona el significat (Mayer, principi de coherència).

### concepte_microscopic_o_abstracte

**Trigger:** concepte sense referent visual macro clar (cèl·lula, àtom, enzim, justícia, infinit, democràcia abstracta)

**Modulació:**
- default: ometre el marcador
- alternativa: reformular a escala macro o visualitzable ('cèl·lula' → `[IMATGE: cèl·lula animal vista al microscopi]`; 'democràcia' → `[IMATGE: cambra del parlament]`)

**Raonament pedagògic.** Una il·lustració genèrica d'un concepte abstracte no ancora — distreu (Mayer, principi de redundància); millor cap imatge que una imatge buida de significat.

### B2_C1_menys_es_mes

**Trigger:** mecr_in: [B2, C1]

**Modulació:**
- densitat: 1-2 marcadors a B2, 0-1 a C1
- especificitat: només per a diagrames, infografies, mapes temàtics o gràfics que condensin dades difícils de verbalitzar
- preset: vectorial editorial, isomètric infogràfic o fotografia documental
- posicio: dins del paràgraf com a suport a l'argument, mai en línia pròpia aïllada

**Raonament pedagògic.** Als nivells alts la il·lustració no simplifica — ha d'aportar valor informatiu que el text no dóna en un cop d'ull (Mayer, principi de contigüitat); si el concepte es pot explicar en dues frases sense pèrdua, no marquis.

### materia_no_visual

**Trigger:** materia_in: [matematiques_calcul, filosofia_abstracta, llengua_gramatica] AND text purament verbal sense conceptes referencials

**Modulació:**
- default: 0 marcadors
- si_complement_activat_pel_docent: màxim 1 marcador i només si hi ha un concepte concret puntual

**Raonament pedagògic.** La càrrega visual gratuïta competeix amb el processament verbal que és precisament el focus d'aquestes matèries (principi de coherència de Mayer).

## Metadades de cel·la (per a `build_skills.py`)

**Tipus de descriptor:**
- `binary` — "compleix / no compleix".
- `qualitative` — requereix judici huma o LLM-jutge.
- `countable` — llindar quantitatiu verificable mecanicament.
- `structural` — requereix analisi sintatica o discursiva.
- `metacognitive` — descriptor de proces en primera persona.

| Pas / Dimensió | Tipus | requires_source_text | validation_hint |
|---|---|---|---|
| 1 Nombre d'il·lustracions | `countable` | no | comptar marcadors `[IMATGE:]` al text; verificar que esta dins del rang per nivell (pre-A1: ≤5; A1: ≤4; A2: ≤3; B1: ≤2; B2: ≤2; C1: ≤1) |
| 2 Posicio al text | `structural` | no | pre-A1/A1: verificar que el marcador precedeix el paragraf (linia propia DAVANT); A2+: verificar que no hi ha marcadors en linia propia aillats (han d'anar dins del context del paragraf) |
| 3 Especificitat del marcador | `qualitative` | **si** | LLM-jutge sobre si el concepte del marcador és concret i visualitzable (positiu) o vague i abstracte (negatiu); detectar marcadors massa genèrics ("[IMATGE: ciencies]"); cross_source: verificar que el concepte del marcador esta present i és central al text font |
| 4 Preset d'estil | `binary` | no | binary: el preset seleccionat és coherent amb el MECR i la materia (aquarel·la per primaria, vectorial per ESO+); si no s'especifica, s'aplica el default adequat |
| 5 Autoavaluacio mediada | `metacognitive` | no | pre-A1: registre docent d'observacio; A1+: derivar a vista d'autoavaluacio alumne |

**Notes:**
- Format del marcador: `[IMATGE: concepte curt]`. L'absencia del delimitador de tancament `]` o un marcador dins d'una llista/taula son errors detectables per regex.
- Conceptes micro/abstractes: detectables per LLM-jutge. Si el marcador conté "cel·lula", "atom", "molecula", "justicia", "infinit" → alertar el docent per si vol ometre o reformular.
- Diferencia `[IMATGE:]` vs `[PICTO:]`: es processen separadament. Mai barrejar els dos sistemes en el mateix fragment per al mateix concepte.
- Pre-A1: si el text no te conceptes visualitzables, millor usar `pictogrames` que il·lustracions (mes ràpid i sense demora de generacio).

## Heurístiques docent

**H1 — "Pots imaginar-ho?" (seleccio del concepte).**
Per a cada concepte del text, pregunto: "Pots imaginar una imatge clara d'aquest concepte?" Si la resposta és si facilment (gat, arbre, volca), potser no cal il·lustrar — l'alumne ja te la imatge mental. Si la resposta és no (fotosintesi, revolucio industrial, democracia), la il·lustració pot ajudar. Si no hi ha cap imatge possible clara, no posar el marcador.

**H2 — Pre-A1: imatge DAVANT, sempre.**
L'ordre natural del text posa la imatge al costat o darrere del concepte. Per a pre-A1, cal invertir-ho: la imatge anticipa la paraula. L'alumne veu la imatge → el docent diu la paraula → l'alumne llegeix la paraula al text. Aquesta inversio és pedagogica, no estetica.

**H3 — El preset com a decisio pedagogica explicita.**
Quan el docent tria el preset, ho fa com a decisio conscious. Explicar a la classe per que s'ha triat aquarel·la per a un conte i vectorial per a un article de ciencies és una llico de multimodalitat i de registre visual: cada context te el seu codi visual.

**H4 — Menys és mes (A2+).**
Cada il·lustró afegeix carrega cognitiva. A B2-C1, una il·lustració sense valor informatiu addicional distreu en lloc d'ancorar. Proposo la regla: si puc explicar el concepte en dues frases sense la imatge i l'alumne ho entendra igualment, no posar el marcador.

**H5 — Il·lustracio vs pictograma: la pregunta de la funcio.**
Quan dubto entre usar pictograma o il·lustració, em pregunto: "Necessite suport lexic (aprendre la paraula) o suport conceptual (entendre el concepte)?" Suport lexic → pictograma. Suport conceptual (proces, sistema, lloc, escena) → il·lustracó.

## Format de sortida

**Header H2 obligatori (literal exacte):**
```
## Il·lustracions
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
[IMATGE: concepte curt en català]
```

**Headers explicitament PROHIBITS:**
```
cap header addicional dins del bloc d'il·lustracions
```

**Regla d'integritat estructural.** Marcadors en línia pròpia DAVANT del paràgraf (pre-A1/A1) o al costat / dins del paràgraf (A2+); mai dins de llistes, taules, bastides ni altres complements. Sense els delimitadors literals `[IMATGE:` i `]` el resolver no detecta el marcador i el complement queda inert (no es generen imatges).

## Fonts principals

- MALL (Model d'Aprenentatge de Llengues i Literacitat): multimodalitat, principi "imatge a l'esquerra", ancoratge visual ZDP.
- Mayer, R.E. (2009): *Multimedia Learning* — principi de contigüitat imatge-text; principi de redundancia; principi de coherencia (eliminar elements visuals sense valor informatiu).
- Regles de Lectura Fàcil: imatge davant del text, un element visual per concepte clau.
- Decret 175/2022 (curriculum Catalunya): competencia digital i multimodalitat com a dimensio de la comunicacio lingüística.
