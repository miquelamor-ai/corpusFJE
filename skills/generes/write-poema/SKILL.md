---
name: write-poema
description: 'Use when adapting or generating a poema for students. Activates when
  genre_discursiu == "poema". Preserves strophic structure, concrete metaphors, and
  rhythm. Does not convert to prose. Output: poema in markdown with title, stanzas,
  and verses.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: poema
tipologia: Narrativa / Expressiva
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
  equals: poema
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-poema.md
font_version: 4.0.0-canonic
generat_at: '2026-06-11'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 5951b3be11b80fa3
---

# Escriure/adaptar un poema — skill operativa per a LLM

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

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Estructura estrofica**
- Forma i regularitat: Recitacio oral; adult escriu si cal. L'alumne reconeix la repeticio de sons i versos.

**2. Vers com a unitat**
- Significat i ritme: No s'aplica (oral; el ritme és el de la canço o el rodoli).

**3. Metafores i imatges**
- Accessibilitat estetica: Reconeixement oral: "el sol és com una taronja". L'adult proposa la imatge.

**4. Vocabulari**
- Accessibilitat lexica: Vocabulari molt quotidia. Paraules que l'alumne ja usa (objectes, animals, colors).

**5. Ritme (rima/cadencia)**
- Musicalitat: Rima final simple i molt repetitiva. L'adult guia la rima (aaaa o aabb).

**6. Veu poetica (jo liric)**
- Perspectiva i autoria: L'alumne expressa oralment com se sent davant d'una cosa. L'adult escriu.

### A1 — Inicial


**1. Estructura estrofica**
- Forma i regularitat: 1-2 estrofes de 2-3 versos. Estructura visible i regular. Separacio visual clara.

**2. Vers com a unitat**
- Significat i ritme: Cada vers = 1 idea o imatge. Sense partir una idea a la meitat del vers.

**3. Metafores i imatges**
- Accessibilitat estetica: 1 comparacio concreta per estrofa: "com un...", "sembla un...". Imatge visual.

**4. Vocabulari**
- Accessibilitat lexica: Vocabulari quotidia. Cap sinonim rebuscat. 1 paraula nova com a maxim per estrofa.

**5. Ritme (rima/cadencia)**
- Musicalitat: Rima consonant senzilla al final del vers (parells o alternada).

**6. Veu poetica (jo liric)**
- Perspectiva i autoria: "Jo" visible i consistent. El poema parla des d'una perspectiva clara.

**7. Autoavaluacio**
- Metacognicao: "He escrit 2 estrofes. He posat una comparacio (com un...)."

### A2 — Funcional


**1. Estructura estrofica**
- Forma i regularitat: 2-3 estrofes de 3-4 versos. Separacio visual entre estrofes. Cada estrofa = 1 idea.

**2. Vers com a unitat**
- Significat i ritme: Cada vers és independent pero contribueix a la imatge global.

**3. Metafores i imatges**
- Accessibilitat estetica: 1 metafora o comparacio per estrofa. Concreta i visual. Ancoratge sensorial.

**4. Vocabulari**
- Accessibilitat lexica: Vocabulari accessible. 1-2 paraules noves amb context que ajudi a entendre-les.

**5. Ritme (rima/cadencia)**
- Musicalitat: Rima consonant o assonant. Pot ser alternada. Ritme regular perceptible.

**6. Veu poetica (jo liric)**
- Perspectiva i autoria: Veu del jo liric consistent durant tot el poema. No canviar de perspectiva.

**7. Autoavaluacio**
- Metacognicao: "Cada estrofa te la seva idea. He mantingut la rima fins al final."

### B1 — Estratègic


**1. Estructura estrofica**
- Forma i regularitat: 3-4 estrofes. Estructura conscient. Pot variar el nombre de versos per efecte intencional.

**2. Vers com a unitat**
- Significat i ritme: Encavalcament conscient si s'usa: la idea continua al vers seguent amb intencio.

**3. Metafores i imatges**
- Accessibilitat estetica: Metafora que connecta un concepte nou amb l'experiencia de l'alumne (ZDP).

**4. Vocabulari**
- Accessibilitat lexica: Vocabulari adequat al tema. Les paraules noves hi son perque aporten precisio poetica.

**5. Ritme (rima/cadencia)**
- Musicalitat: Ritme conscient. Pot renunciar a la rima si la cadencia es manté.

**6. Veu poetica (jo liric)**
- Perspectiva i autoria: Distincio entre jo liric i autor. Pot explorar una veu diferent de la propia.

**7. Autoavaluacio**
- Metacognicao: "La meva metafora connecta el tema amb alguna cosa que conec. El ritme es manté."

### B2 — Acadèmic


**1. Estructura estrofica**
- Forma i regularitat: Estructura variada amb intencionalitat. Pot incloure estrofes de mida diferent.

**2. Vers com a unitat**
- Significat i ritme: Control del vers com a unitat de sentit i de ritme simultaneament.

**3. Metafores i imatges**
- Accessibilitat estetica: 2-3 imatges elaborades. Coherencia tematica entre elles.

**4. Vocabulari**
- Accessibilitat lexica: Vocabulari ric i variat. Tria conscient de paraules per la seva musicalitat i densitat semantica.

**5. Ritme (rima/cadencia)**
- Musicalitat: Varietat ritmica. Pot combinar versos amb rima i versos blancs.

**6. Veu poetica (jo liric)**
- Perspectiva i autoria: Veu poetica personal i reconeixible. El lector nota qui parla.

**7. Autoavaluacio**
- Metacognicao: "He triat les paraules per la seva sonoritat. La veu del poema és consistent."

### C1+ — Crític


**1. Estructura estrofica**
- Forma i regularitat: Estructura lliure o formal amb plena consciencia del model triat i el seu efecte.

**2. Vers com a unitat**
- Significat i ritme: Vers com a instrument precis de significat, pausa i musicalitat.

**3. Metafores i imatges**
- Accessibilitat estetica: Imatges originals. Pot explorar metafora mixta o sinestesia.

**4. Vocabulari**
- Accessibilitat lexica: Vocabulari precis, ric i personal. Pot incloure neologismes justificats.

**5. Ritme (rima/cadencia)**
- Musicalitat: Ritme com a eina expressiva. Alteracio conscient del ritme per crear efecte.

**6. Veu poetica (jo liric)**
- Perspectiva i autoria: Veu poetica plenament elaborada amb distancia critica o ironia si escau.

**7. Autoavaluacio**
- Metacognicao: "El meu poema te una veu propia. Les imatges son originals i el ritme és intencional."

