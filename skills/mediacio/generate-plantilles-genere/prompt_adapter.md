---
tipus: derivat
font_canonic: M3_instrument-generar-plantilles-genere.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-25'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 3a6b8955a948edb9
---

# Generar plantilles de gènere — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar plantilles de gènere per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Format i densitat del text donat**: Visual: 3-4 requadres amb icones. Cap text autònom. L'adult llegeix les instruccions.
- **Concretesa del contingut del forat**: Requadre de dibuix o icona per completar. Cap text a omplir autònomament.
- **Ancoratge al contingut llegit**: Forats completables amb imatges o paraules que apareixen al text. L'adult mostra on és la resposta.
- **Proporció text donat / forats**: Maxima densitat visual: tota la plantilla és un esquema. Cap text en prosa.
- **Metacognició**: "He dibuixat (o enganxat) el que passa al text." (oral, mediat per adult)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Format i densitat del text donat**: Text quasi complet: 70-80% donat, 20-30% forats. 1-2 paraules per forat.
- **Concretesa del contingut del forat**: Forats de 1-2 paraules: nom concret, verb d'acció, un adjectiu. Completables amb paraules del text adaptat.
- **Ancoratge al contingut llegit**: Forats completables amb paraules o noms extrets directament del text adaptat.
- **Proporció text donat / forats**: Alta densitat forats: 1 forat cada 2-3 paraules. El text donat guia i contextualitza.
- **Metacognició**: "He completat les paraules que faltaven amb informació del text."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Format i densitat del text donat**: Text parcialment donat: 50-60% donat, 40-50% forats. Frases curtes per completar.
- **Concretesa del contingut del forat**: Forats d'1 frase: "Els protagonistes son ___" · "El conflicte és ___". Completables amb reformulació del text.
- **Ancoratge al contingut llegit**: Forats que requereixen selecció i reformulació d'informació del text.
- **Proporció text donat / forats**: Densitat moderada: 1 forat per frase o cada 2 frases. Text donat aporta estructura.
- **Metacognició**: "He completat les seccions amb informació del text que he llegit."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Format i densitat del text donat**: Text marc: 30-40% donat (connectors, estructura, termes disciplinars clau).
- **Concretesa del contingut del forat**: Forats de 2-3 frases construïdes per l'alumne amb les seves paraules a partir del text.
- **Ancoratge al contingut llegit**: Forats que requereixen inferència o selecció crítica d'informació del text.
- **Proporció text donat / forats**: Densitat baixa: 1 forat per paràgraf. L'alumne aporta la major part del contingut.
- **Metacognició**: "He completat la plantilla amb informació pròpia sobre el contingut. He verificat que els forats son coherents amb el gènere."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Format i densitat del text donat**: Plantilla minimalista: encapçalaments + 1 frase d'exemple per secció com a model de referència.
- **Concretesa del contingut del forat**: Forats que demanen elaboració argumentada (1 paràgraf) que va més enllà del text (connexió, anàlisi).
- **Ancoratge al contingut llegit**: Forats que requereixen elaboració que va més enllà del text (connexió amb altres fonts).
- **Proporció text donat / forats**: Densitat mínima: 1 forat per secció. Quasi tot és producció pròpia.
- **Metacognició**: "He usat la plantilla com a model de referència i he escrit el text amb les meves pròpies paraules."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Format i densitat del text donat**: Criteris de gènere i estil. Pràcticament sense text donat: el primer mot de cada secció com a únic ancoratge.
- **Concretesa del contingut del forat**: Forats de producció lliure coherent amb el gènere, inspirada però no limitada pel text.
- **Ancoratge al contingut llegit**: Forats de producció pròpia de l'alumne, inspirada però autònoma.
- **Proporció text donat / forats**: Forat de producció completa per secció. La plantilla és una rúbrica de gènere.
- **Metacognició**: "He usat els criteris de gènere per autoregular la meva producció sense suport directe."

