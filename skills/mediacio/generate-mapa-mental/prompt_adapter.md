---
tipus: derivat
font_canonic: M3_instrument-generar-mapa-mental.md
font_version: 1.1.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-25'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 326a7b69817dc91d
---

# Generar mapa mental — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar mapa mental per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Nucli radial**: Tema o objecte familiar, 1 paraula + pictograma/emoji.
- **Nombre de branques**: 2 branques associatives.
- **Nivells d'expansió**: 1 nivell: arrel i branques directes, sense sub-idees.
- **Densitat i obertura**: Cap pregunta abstracta: només paraula clau + imatge.
- **Associacions interdisciplinàries**: Cap connexió interdisciplinària (massa abstracta a aquest nivell).
- **Estructura markdown radial**: `## Mapa mental` + llista amb central com a única arrel en negreta (`- **CENTRAL**`) i branques sagnades 2 espais. Pictogrames/emoji inline a arrel i branques. Cap fletxa Unicode ni ASCII-art.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Nucli radial**: 1 paraula clau del tema. En negreta.
- **Nombre de branques**: 2-3 branques associatives.
- **Nivells d'expansió**: 1 nivell: arrel i branques directes.
- **Densitat i obertura**: Cap pregunta abstracta: paraules clau soles.
- **Associacions interdisciplinàries**: Cap connexió interdisciplinària.
- **Estructura markdown radial**: `## Mapa mental` + central arrel en negreta, branques sagnades 2 espais. Pictogrames recomanats. Cap ASCII-art.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Nucli radial**: Frase nominal curta (1-3 paraules) del tema. En negreta.
- **Nombre de branques**: 3-4 branques associatives.
- **Nivells d'expansió**: 1-2 nivells: branca i, opcionalment, una sub-idea.
- **Densitat i obertura**: Una idea curta per branca; encara sense preguntes generadores explícites.
- **Associacions interdisciplinàries**: 1 connexió concreta amb la vida quotidiana.
- **Estructura markdown radial**: `## Mapa mental` + central arrel en negreta, branques sagnades, fins a 2 nivells. Cap ASCII-art.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Nucli radial**: Tema o concepte que es vol explorar. En negreta.
- **Nombre de branques**: 4-5 branques associatives.
- **Nivells d'expansió**: 2 nivells: branca i sub-idees.
- **Densitat i obertura**: 1-2 preguntes generadores ("per què...?", "què passaria si...?").
- **Associacions interdisciplinàries**: 1 connexió explícita amb una altra matèria.
- **Estructura markdown radial**: `## Mapa mental` + central arrel en negreta, branques i sub-idees sagnades (2 nivells). Cap ASCII-art.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Nucli radial**: Concepte nuclear, pot ser abstracte. En negreta.
- **Nombre de branques**: 5-7 branques associatives.
- **Nivells d'expansió**: 2-3 nivells: branca, sub-idees i matís.
- **Densitat i obertura**: Preguntes obertes a diverses branques que conviden a explorar.
- **Associacions interdisciplinàries**: 1-2 connexions interdisciplinàries.
- **Estructura markdown radial**: `## Mapa mental` + central arrel en negreta, fins a 3 nivells de sagnia. Cap ASCII-art.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Nucli radial**: Concepte complex o tensió que es vol obrir. En negreta.
- **Nombre de branques**: 5-8 branques associatives.
- **Nivells d'expansió**: 3 nivells: expansió completa amb tensions.
- **Densitat i obertura**: Preguntes provocadores que obren tensions o contradiccions.
- **Associacions interdisciplinàries**: Connexions interdisciplinàries + connexió amb fonts o debats externs.
- **Estructura markdown radial**: `## Mapa mental` + central arrel en negreta, fins a 3 nivells de sagnia amb tensions. Cap ASCII-art.

