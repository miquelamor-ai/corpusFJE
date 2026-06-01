---
tipus: derivat
font_canonic: M3_instrument-generar-activitats-aprofundiment.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-01'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: ef0bfd256305893c
---

# Generar activitats d'aprofundiment — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar activitats d'aprofundiment per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Quantitat i varietat**: 1-2 activitats físiques o manipulatives. Una sola consigna visual.
- **Profunditat de pensament**: Manipulatiu: ordenar, tocar, moure, dramatitzar, dibuixar. No requereix abstracció lingüística.
- **Producte esperat explícit**: Indicació física i visual: "Ordena les imatges de [X] a [Y]." Producte: dibuix, ordenació, dramatització. Cap escriptura autònoma.
- **Ús de L1 com a recurs**: No generar.
- **Metacognició**: "He ordenat les imatges / he dibuixat." (oral, mediat per adult)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Quantitat i varietat**: 2 activitats concretes i visuals. Evitar debats abstractes.
- **Profunditat de pensament**: Concret i visual. Màxim ancoratge en objectes o experiències familiars. Comparació simple.
- **Producte esperat explícit**: Consigna molt concreta. Producte clar i assolible: 1 dibuix, 1 frase, 1 llista de 3 ítems.
- **Ús de L1 com a recurs**: No generar.
- **Metacognició**: "He fet l'activitat. He escrit [producte]."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Quantitat i varietat**: 2-3 activitats. Combinació de connexió i "i si...?".
- **Profunditat de pensament**: Comparable i imaginatiu. "Com és X aquí vs. allà?" · "Qué passaria si...?".
- **Producte esperat explícit**: Consigna accionable. Producte concret i delimitat: 1 fitxa, 1 mapa, 1 comparació de 3 elements.
- **Ús de L1 com a recurs**: Opcional: "Com es diu [terme clau] en altres llengues de l'aula? Comparteix-ho si vols." Cap exposició.
- **Metacognició**: "He pensat més enllà del text. He fet la connexió o el 'i si...?'."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Quantitat i varietat**: 2-3 activitats. Combinació de debat, connexió interdisciplinar i recerca guiada.
- **Profunditat de pensament**: Argumentatiu. Pren posicions i les justifica. Discrimina evidència de creença o opinió.
- **Producte esperat explícit**: Consigna accionable amb producte i temps estimat (15-30 min): 1 argument escrit, 1 recerca a 2 fonts.
- **Ús de L1 com a recurs**: Opcional: comparació d'expressions o conceptes entre L1s dels alumnes si el text ho permet.
- **Metacognició**: "He argumentat la meva postura i he usat evidència del text o d'una altra font."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Quantitat i varietat**: 2-3 activitats. Connexió entre matèries, contrast de fonts, intertextualitat.
- **Profunditat de pensament**: Analític. Contrastiu. Cerca relacions no evidents entre idees o camps disciplinars.
- **Producte esperat explícit**: Consigna amb producte complex: argumentació de 2-3 paràgrafs, recerca comparada, informe breu.
- **Ús de L1 com a recurs**: Opcional: contrast d'equivalents culturals o termes tècnics entre les llengues que coneixes.
- **Metacognició**: "He analitzat les relacions entre matèries i he contrastat informació de fonts diverses."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Quantitat i varietat**: 2-3 activitats. Reflexió crítica, hipòtesis contrafactuals, fonts contradictòries.
- **Profunditat de pensament**: Crític. Metacognitiu. Detecta biaixos, dilemes ètics, limitacions del coneixement i de les fonts.
- **Producte esperat explícit**: Consigna oberta amb criteris de qualitat del producte. L'alumne decideix el format i justifica la tria.
- **Ús de L1 com a recurs**: Opcional: contrast metalingüístic i discursiu entre sistemes lingüístics i culturals.
- **Metacognició**: "He detectat biaixos i limitacions del text. He qüestionat les afirmacions de l'autor amb arguments propis. He justificat la tria del format del meu producte segons l'objectiu de l'activitat."

