---
tipus: derivat
font_canonic: M3_instrument-generar-bastides-produccio.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-11'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: d13f7b2efbec5e22
---

# Generar bastides de producció — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar bastides de producció per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **GPS disciplinar**: 2-3 passos molt concrets amb terminologia disciplinar de la matèria. Cada pas = 1 frase imperativa breu.
- **Connectors + iniciadors HCL**: 1 iniciador per HCL principal del gènere. Connectors: *i, però, perquè*. Llista curta (max 5 ítems).
- **Checklist d'autoavaluació**: Cap pauta a A1: la bastida és el Bloc A i B.
- **Metacognició**: "He seguit els passos de la bastida per escriure el meu text."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **GPS disciplinar**: 3-4 passos + terminologia disciplinar específica. Cada pas indica QUÈ fer i AMB QUÈ.
- **Connectors + iniciadors HCL**: 2-3 iniciadors per HCL. Connectors: + *primer, llavors, per tant*. Connectors de causa-efecte.
- **Checklist d'autoavaluació**: 2-3 ítems simples vinculats al gènere i la tasca concreta. Com a mínim un ítem sobre el destinatari o el propòsit (ex.: "A qui escric? He posat el nom del personatge?").
- **Metacognició**: "He usat la bastida per estructurar el meu text. He completat el checklist."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **GPS disciplinar**: Raonament disciplinar explícit: hipòtesi, evidència, causa, efecte. Vocabulari CALP del camp.
- **Connectors + iniciadors HCL**: Iniciadors inferencials i causals. Connectors: + *ja que, en canvi, tot i que*. Iniciadors de contrast.
- **Checklist d'autoavaluació**: 4-5 ítems específics del gènere. Vinculats als criteris d'avaluació si estan disponibles.
- **Metacognició**: "He seguit la base d'orientació i he usat els iniciadors per construir el meu argument."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **GPS disciplinar**: Superestructura completa del gènere amb lèxic CALP i indicadors de qualitat per secció.
- **Connectors + iniciadors HCL**: Iniciadors CALP argumentals. Connectors: + *no obstant, atès que, en conseqüència* (NOMES a B2+).
- **Checklist d'autoavaluació**: Criteris d'avaluació específics amb indicadors observables. Inclou criteris de rigor disciplinar.
- **Metacognició**: "He usat la pauta d'interrogació per revisar que el meu text compleix els criteris del gènere."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **GPS disciplinar**: Contrast de fonts, biaix autorial, intertextualitat. El GPS inclou indicadors de rigor crític.
- **Connectors + iniciadors HCL**: Iniciadors dialèctics i retòrics. Connectors de concessió i contrast complexos.
- **Checklist d'autoavaluació**: Reflexió metacognitiva sobre fiabilitat de les fonts, biaix i coherència interna de l'argument.
- **Metacognició**: "He comprovat que les meves fonts son fiables i que el meu argument és coherent i honest."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


