---
tipus: derivat
font_canonic: M3_genere-escriure-informe.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 44b06c58a2a4ac8c
---

# Escriure/adaptar un informe — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un informe per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Orientació i síntesi**: 1-2 frases que diuen de qué tracta l'informe.
- **Format i objectivitat**: 3-5 dades en frases simples o llista simple (dada / valor). Nombre + unitat. Taula de 2 columnes admissible com a bastida visual.
- **Rigor epistèmic**: Dades primer ("hem vist que X"). Conclusions separades ("per tant, Y").
- **Coherència estilística**: Sense frases personals ("jo crec que..."). Impersonal simple.
- **Rigor metodològic**: Sense hipòtesi (massa complex per a A1). Una descripció mínima del procediment.
- **Profunditat argumentativa**: 1 conclusió simple derivada de les dades: "Hem après que..."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Orientació i síntesi**: Introducció de 2-3 frases: qué s'ha estudiat i per qué.
- **Format i objectivitat**: Dades organitzades en llista o taula simple. Unitats explícites.
- **Rigor epistèmic**: Dades i conclusions en blocs separats. Connector explícit: "per tant", "com a conclusió".
- **Coherència estilística**: Veu impersonal consistent: "s'observa que", "els resultats indiquen que".
- **Rigor metodològic**: Pot incloure una pregunta inicial que l'informe respon.
- **Profunditat argumentativa**: 1-2 conclusions derivades de les dades. Connector "per tant".

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Orientació i síntesi**: Resum executiu: 1 paràgraf que indica l'objectiu i la conclusió principal. No detalla les dades (per evitar duplicació amb el cos).
- **Format i objectivitat**: Dades organitzades per categories. Pot incloure comparació entre valors.
- **Rigor epistèmic**: Separació neta entre resultats i conclusions en seccions diferenciades. Sense barreja.
- **Coherència estilística**: Vocabulari objectiu i tècnic. Sense adjectius subjectius. Impersonal (es + verb) prioritari; passiva opcional.
- **Rigor metodològic**: Hipòtesi "Si..., llavors..." explícita. Metodologia en 2-3 frases.
- **Profunditat argumentativa**: 2-3 conclusions argumentades. Pot incloure 1 recomanació derivada de les conclusions.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Orientació i síntesi**: Resum executiu amb les conclusions principals davant dels resultats.
- **Format i objectivitat**: Dades en taules o gràfics simples. Descripció objectiva de les dades (sense conclusió).
- **Rigor epistèmic**: Dades comentades objectivament i conclusions argumentades per separat amb connector explícit.
- **Coherència estilística**: Objectivitat rigurosa. Pot incloure citació de fonts per a afirmacions.
- **Rigor metodològic**: Hipòtesi i metodologia ben descrites. Variables identificades (independent/dependent).
- **Profunditat argumentativa**: Conclusions argumentades + recomanacions basades en les dades. Connexió explícita dades→conclusions.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Orientació i síntesi**: Resum executiu professional que permet comprendre l'informe sense llegir el cos complet.
- **Format i objectivitat**: Dades en formats variats (taules, gràfics, diagrames). Anàlisi estadística si escau.
- **Rigor epistèmic**: Separació rigorosa. Les conclusions deriven explícitament i raonada de les dades.
- **Coherència estilística**: Objectivitat acadèmica amb reconeixement de limitacions i incerteses del procés.
- **Rigor metodològic**: Hipòtesi, variables, limitacions metodològiques i fonts en la metodologia.
- **Profunditat argumentativa**: Conclusions amb discussió de les limitacions, propostes de recerca futures i reconeixement d'incerteses.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


