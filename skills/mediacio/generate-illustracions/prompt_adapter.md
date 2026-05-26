---
tipus: derivat
font_canonic: M3_instrument-generar-illustracions.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-05-26'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 71cc77fc49dd1667
---

# Generar il·lustracions — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar il·lustracions per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Densitat**: Maxim 4-5. Una per idea principal. Alta densitat justificada (text ≈ imatge).
- **Anticipacio vs ancoratge**: Imatge DAVANT de la paraula/frase que il·lustra. L'alumne veu la imatge PRIMER. Anticipacio visual.
- **Concretesa del concepte**: Concepte molt concret i universal: "gat", "arbre", "pluja". 1-2 paraules.
- **Registre visual**: Pictograma o il·lustració clara i simple. Sense elements distractors.
- **Metacognicao**: "He vist la imatge i he dit el que era." (oral, mediat per adult)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Densitat**: 3-4 il·lustracions. Una per paragraf o per concepte clau.
- **Anticipacio vs ancoratge**: Imatge immediatament DAVANT o AL COSTAT del concepte clau.
- **Concretesa del concepte**: Concepte concret: "cel·lula animal", "volca en erupcio". 1-3 paraules.
- **Registre visual**: Il·lustracò o foto realista. Molt clara, sense text a la imatge.
- **Metacognicao**: "He mirat la imatge i m'ha ajudat a entendre la paraula difícil."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Densitat**: 2-3 il·lustracions. Als punts de maxim ancoratge conceptual.
- **Anticipacio vs ancoratge**: Imatge al costat del concepte que ancora, dins del paragraf.
- **Concretesa del concepte**: Concepte concret + context: "fotosintesi a fulla verda". 2-4 paraules.
- **Registre visual**: Foto realista o il·lustracó educativa. Pot tenir etiquetes simples.
- **Metacognicao**: "La imatge m'ha ajudat a entendre el proces o el concepte."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Densitat**: 1-2 il·lustracions als conceptes abstractes o processos clau.
- **Anticipacio vs ancoratge**: Imatge al concepte abstracte o al proces que beneficia d'ancoratge visual.
- **Concretesa del concepte**: Concepte especific del contingut: "cadena trofica marina", "cambra del parlament".
- **Registre visual**: Diagrama o foto cientifica/geografica. Etiquetes disciplinars.
- **Metacognicao**: "He identificat quins conceptes necessitaven imatge i quins no."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Densitat**: 1-2 il·lustracions molt selectives (diagrama, proces, dada visual clau).
- **Anticipacio vs ancoratge**: Imatge estrategica: diagrama d'un proces, taula de dades, mapa conceptual visual.
- **Concretesa del concepte**: Concepte disciplinar: "diagrama de l'aparell respiratori", "mapa de la Revolucio Francesa".
- **Registre visual**: Diagrama, mapa, grafic. Llegenda si cal.
- **Metacognicao**: "He usat les il·lustracions com a suport visual per a conceptes que no s'expliquen facilment amb paraules."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Densitat**: 0-1 il·lustració. Reservada per a diagrames o infografies que condensin dades.
- **Anticipacio vs ancoratge**: Imatge de suport a l'argument: infografia, grafic, mapa.
- **Concretesa del concepte**: Concepte complex: "infografia comparativa de sistemes politics", "grafic evolucio PIB".
- **Registre visual**: Infografia, grafic estadistic, mapa tematic.
- **Metacognicao**: — (N/A: a C1 rarament es genera il·lustracó; si es genera, l'autoavaluacio és igual que B2)

