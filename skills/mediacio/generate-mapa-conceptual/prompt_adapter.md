---
tipus: derivat
font_canonic: M3_instrument-generar-mapa-conceptual.md
font_version: 4.2.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-20'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: d6eaedbfe6bfbf82
---

# Generar mapa conceptual — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar mapa conceptual per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Funció cognitiva**: Esquema visual: 2-3 nodes. Imatge → paraula o seqüència temporal (antes/durant/après).
- **Nucli del mapa**: Nom d'un personatge o objecte familiar del text. 1-2 paraules.
- **Relació de branca (graduada MECR)**: 1-2 elements: parts o qualitats d'un tot. Noms simples i concrets (cap, pit, cua).
- **Detalls de les branques**: Cap sub-element: l'esquema és pla (massa nivells per a pre-A1).
- **Estructura markdown**: `## Esquema visual` + llista plana sense sangria. 2-3 ítems màxim.
- **Nombre recomanat**: 0 enllaços creuats. L'esquema visual és pla, sense relacions transversals.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Funció cognitiva**: Esquema visual: 3-4 nodes. Parts d'un tot o qualitats simples d'un element concret.
- **Nucli del mapa**: 1 terme nuclear concret del text adaptat. En negreta.
- **Relació de branca (graduada MECR)**: 2-3 branques concretes. Noms simples. Pot ser seqüència temporal (1r, 2n, 3r).
- **Detalls de les branques**: Cap sub-element: l'esquema és pla (màxim 1 nivell).
- **Estructura markdown**: `## Esquema visual` + llista amb sangria màxima 1 nivell. Cap ASCII-art.
- **Nombre recomanat**: 0 enllaços creuats. L'esquema visual és pla.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Funció cognitiva**: Mapa conceptual: 2 nivells jeràrquics. Primera introducció guiada de branques etiquetades.
- **Nucli del mapa**: 1 terme nuclear precís del text adaptat. En negreta. Correspon a la idea central del text.
- **Relació de branca (graduada MECR)**: 3-4 branques amb **nom de categoria** (Causes / Tipus / Efectes / Processos). Bastida classificatòria. Mai genèrics.
- **Detalls de les branques**: 2-3 sub-elements per branca. Termes curts, no frases llargues. Del text adaptat.
- **Estructura markdown**: `## Mapa conceptual` + 2 nivells de sangria. Branques en negreta. Cap ASCII-art.
- **Nombre recomanat**: 0 enllaços creuats. Primer mapa jeràrquic: el focus és nomenar categories, encara no creuar branques.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Funció cognitiva**: Mapa conceptual: 3 nivells. Concepte → categories disciplinars → detalls inferts del text.
- **Nucli del mapa**: 1 terme que organitza tot el coneixement del text. Terme disciplinar.
- **Relació de branca (graduada MECR)**: 3-5 branques amb **verb d'enllaç de relació bàsica**: causa/conseqüència (provoca, és provocat per) o part/tot (es divideix en, forma part de). Proposició Novak llegible. **Sense connectors de matís/concessió/contrast.** Mai genèrics.
- **Detalls de les branques**: 3-4 sub-elements per branca. Inferts del text, no copiats literalment.
- **Estructura markdown**: `## Mapa conceptual` + 3 nivells de sangria. Branques en negreta. Cap ASCII-art.
- **Nombre recomanat**: 0-1 enllaços creuats. Opcional, només si hi ha una relació transversal evident entre dues branques.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Funció cognitiva**: Mapa conceptual: 4 nivells màxim. Superestructura del gènere amb lèxic CALP.
- **Nucli del mapa**: 1 terme nuclear CALP. Pot ser un procés, un fenomen o un concepte abstracte.
- **Relació de branca (graduada MECR)**: 4-6 branques amb **verb d'enllaç CALP**; s'hi afegeixen matís/concessió/condició (en canvi, a diferència de, depèn de, determina, condiciona). Reflecteixen l'estructura del gènere.
- **Detalls de les branques**: Sub-elements amb matisos. Pot incloure relacions transversals entre branques.
- **Estructura markdown**: `## Mapa conceptual` + 4 nivells màxim. Branques CALP en negreta. Cap ASCII-art.
- **Nombre recomanat**: 1-2 enllaços creuats. S'introdueixen explícitament per mostrar relacions entre branques diferents.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Funció cognitiva**: Mapa de contrast: 2 columnes o branques en contraposició. Comparació de fonts o ideologies.
- **Nucli del mapa**: 2 termes en contrast o 1 concepte complex amb múltiples dimensions o perspectives.
- **Relació de branca (graduada MECR)**: 2 columnes de contrast o 4-6 branques amb verb/connector de tensió explícita (contrasta amb, s'oposa a, tanmateix, mentre que).
- **Detalls de les branques**: Sub-elements de contrast, evidències o cites de fonts. Pot incloure tensions entre branques.
- **Estructura markdown**: `## Mapa de contrast` + 2 columnes (taula markdown) o mapa amb branques de contrast.
- **Nombre recomanat**: 2-3 enllaços creuats. Pocs però d'alt valor: mostren integració i tensions entre branques (Novak: el tret de pensament creatiu).

