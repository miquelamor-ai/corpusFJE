---
tipus: derivat
font_canonic: M3_instrument-generar-pictogrames.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-05-26'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 7f6a3c598055a62b
---

# Generar pictogrames — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar pictogrames per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Emoji vs ARASAAC**: ARASAAC si TEA/CAA; emoji si nouvingut BICS. Sempre inline com a anticipacio.
- **Inline vs glossari**: Inline DAVANT de la paraula: l'alumne veu el pictograma PRIMER, llavors llegeix la paraula.
- **Nombre per text**: 8-10 pictogrames maxim per text (maxim 1-2 per frase inline). Alta densitat justificada.
- **Concret vs disciplinar**: Conceptes molt concrets i universals (mode emoji) o conceptes escolars basics (mode ARASAAC).
- **Pre-lectura visual**: Obligatori: vocabulari visual ABANS del text. Docent presenta els pictogrames oralment. Format: `### Vocabulari del text (mira primer!)` + llista pictograma·paraula.
- **Coherencia i qualitat**: Mateix pictograma per al mateix concepte en tot el document. Cap pictograma decoratiu. Cap emoji de flags o gestos ambigus.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Emoji vs ARASAAC**: ARASAAC si TEA o text disciplinar; emoji si vocabulari quotidia. Inline discret.
- **Inline vs glossari**: Inline discret davant o al costat del terme clau. 1 pictograma per paraula nova.
- **Nombre per text**: 4-6 pictogrames. 1 per paraula nova o concepte clau.
- **Concret vs disciplinar**: Conceptes concrets: objectes, essers vius, accions fisiques observables.
- **Pre-lectura visual**: Recomanat: presentar el vocabulari visual abans de llegir.
- **Coherencia i qualitat**: Idem. Coherencia entre seccions.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Emoji vs ARASAAC**: ARASAAC per termes disciplinars (TEA o nouvingut+CALP); emoji si BICS. Al glossari visual, mai inline.
- **Inline vs glossari**: Glossari visual al peu (mai inline). Llista de termes + pictograma + definicio breu.
- **Nombre per text**: 3-5 al glossari visual. 1 per terme disciplinar.
- **Concret vs disciplinar**: Termes disciplinars: "volca", "cel·lula", "parlament" (si te representacio visual).
- **Pre-lectura visual**: No cal. El glossari visual al peu és consultat durant la lectura.
- **Coherencia i qualitat**: Idem. El glossari visual no substitueix el glossari textual.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Emoji vs ARASAAC**: ARASAAC per termes disciplinars especifics de la materia. Al glossari visual.
- **Inline vs glossari**: Glossari visual al peu. Reservat per a termes disciplinars no familiars.
- **Nombre per text**: 2-4 al glossari visual. Termes disciplinars de la materia.
- **Concret vs disciplinar**: Termes disciplinars especifics de la materia sense equivalent quotidia.
- **Pre-lectura visual**: No cal.
- **Coherencia i qualitat**: Idem. Si un terme no te representacio visual clara, millor no posar-ne.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Emoji vs ARASAAC**: ARASAAC o emoji per termes molt tecnics sense equivalent quotidià. Glossari visual.
- **Inline vs glossari**: Glossari visual al peu. Maxim 3-4 termes realment necessaris.
- **Nombre per text**: 1-3 al glossari visual. Termes molt especialitzats.
- **Concret vs disciplinar**: Termes tecnics que beneficien d'ancoratge visual.
- **Pre-lectura visual**: No cal.
- **Coherencia i qualitat**: Idem. Densitat minima: nomes els termes que realment aporten.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Emoji vs ARASAAC**: Rarament. Nomes si hi ha termes molt especialitzats sense representacio coneguda.
- **Inline vs glossari**: Glossari visual minimal o absent.
- **Nombre per text**: 0-2. Rarament necessari.
- **Concret vs disciplinar**: Termes molt especialitzats sense representacio quotidiana accessible.
- **Pre-lectura visual**: No cal.
- **Coherencia i qualitat**: Idem.

