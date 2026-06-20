---
tipus: derivat
font_canonic: M3_genere-escriure-poema.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-20'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: c3b70a46bc3928c1
---

# Escriure/adaptar un poema — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un poema per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Forma i regularitat**: Recitacio oral; adult escriu si cal. L'alumne reconeix la repeticio de sons i versos.
- **Significat i ritme**: No s'aplica (oral; el ritme és el de la canço o el rodoli).
- **Accessibilitat estetica**: Reconeixement oral: "el sol és com una taronja". L'adult proposa la imatge.
- **Accessibilitat lexica**: Vocabulari molt quotidia. Paraules que l'alumne ja usa (objectes, animals, colors).
- **Musicalitat**: Rima final simple i molt repetitiva. L'adult guia la rima (aaaa o aabb).
- **Perspectiva i autoria**: L'alumne expressa oralment com se sent davant d'una cosa. L'adult escriu.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Forma i regularitat**: 1-2 estrofes de 2-3 versos. Estructura visible i regular. Separacio visual clara.
- **Significat i ritme**: Cada vers = 1 idea o imatge. Sense partir una idea a la meitat del vers.
- **Accessibilitat estetica**: 1 comparacio concreta per estrofa: "com un...", "sembla un...". Imatge visual.
- **Accessibilitat lexica**: Vocabulari quotidia. Cap sinonim rebuscat. 1 paraula nova com a maxim per estrofa.
- **Musicalitat**: Rima consonant senzilla al final del vers (parells o alternada).
- **Perspectiva i autoria**: "Jo" visible i consistent. El poema parla des d'una perspectiva clara.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Forma i regularitat**: 2-3 estrofes de 3-4 versos. Separacio visual entre estrofes. Cada estrofa = 1 idea.
- **Significat i ritme**: Cada vers és independent pero contribueix a la imatge global.
- **Accessibilitat estetica**: 1 metafora o comparacio per estrofa. Concreta i visual. Ancoratge sensorial.
- **Accessibilitat lexica**: Vocabulari accessible. 1-2 paraules noves amb context que ajudi a entendre-les.
- **Musicalitat**: Rima consonant o assonant. Pot ser alternada. Ritme regular perceptible.
- **Perspectiva i autoria**: Veu del jo liric consistent durant tot el poema. No canviar de perspectiva.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Forma i regularitat**: 3-4 estrofes. Estructura conscient. Pot variar el nombre de versos per efecte intencional.
- **Significat i ritme**: Encavalcament conscient si s'usa: la idea continua al vers seguent amb intencio.
- **Accessibilitat estetica**: Metafora que connecta un concepte nou amb l'experiencia de l'alumne (ZDP).
- **Accessibilitat lexica**: Vocabulari adequat al tema. Les paraules noves hi son perque aporten precisio poetica.
- **Musicalitat**: Ritme conscient. Pot renunciar a la rima si la cadencia es manté.
- **Perspectiva i autoria**: Distincio entre jo liric i autor. Pot explorar una veu diferent de la propia.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Forma i regularitat**: Estructura variada amb intencionalitat. Pot incloure estrofes de mida diferent.
- **Significat i ritme**: Control del vers com a unitat de sentit i de ritme simultaneament.
- **Accessibilitat estetica**: 2-3 imatges elaborades. Coherencia tematica entre elles.
- **Accessibilitat lexica**: Vocabulari ric i variat. Tria conscient de paraules per la seva musicalitat i densitat semantica.
- **Musicalitat**: Varietat ritmica. Pot combinar versos amb rima i versos blancs.
- **Perspectiva i autoria**: Veu poetica personal i reconeixible. El lector nota qui parla.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Forma i regularitat**: Estructura lliure o formal amb plena consciencia del model triat i el seu efecte.
- **Significat i ritme**: Vers com a instrument precis de significat, pausa i musicalitat.
- **Accessibilitat estetica**: Imatges originals. Pot explorar metafora mixta o sinestesia.
- **Accessibilitat lexica**: Vocabulari precis, ric i personal. Pot incloure neologismes justificats.
- **Musicalitat**: Ritme com a eina expressiva. Alteracio conscient del ritme per crear efecte.
- **Perspectiva i autoria**: Veu poetica plenament elaborada amb distancia critica o ironia si escau.

