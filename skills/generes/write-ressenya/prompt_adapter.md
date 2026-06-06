---
tipus: derivat
font_canonic: M3_genere-escriure-ressenya.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-06'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 3c7588ce98d083b7
---

# Escriure/adaptar una ressenya — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una ressenya per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Completitud i context**: Títol + autor/director. 1 frase.
- **Objectivitat i seqüència**: 2-3 frases: de qué va l'obra. SENSE valorar. SEMPRE PRIMER.
- **Metacognició i precisió**: Senyals lingüístics visibles: "crec que", "m'ha agradat". Separació mínima visible.
- **Suport i credibilitat**: 1 argument senzill: "m'ha agradat perquè…" + 1 fet de l'obra.
- **Perspectivisme**: "La recomano / No la recomano." 1 frase.
- **Control de la informació**: No revelar el final.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Completitud i context**: Títol + autor/director + gènere + any. 1-2 frases.
- **Objectivitat i seqüència**: 3-4 frases descriptives del contingut. Sense cap judici. SEMPRE PRIMER.
- **Metacognició i precisió**: Separació clara: bloc descriptiu → bloc valoratiu. Sense barrejar dins d'una frase.
- **Suport i credibilitat**: 2 arguments concrets amb 1 fet de l'obra cadascun.
- **Perspectivisme**: "La recomano a qui li agradi…" + 1 condició concreta.
- **Control de la informació**: No revelar girs principals de la trama si l'obra és narrativa.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Completitud i context**: Identificació completa + context breu (de qué va, per a qui és).
- **Objectivitat i seqüència**: Descripció del contingut, estructura i elements principals. Sense valoració.
- **Metacognició i precisió**: Separació neta amb connectors de transició: "Pel que fa a la meva valoració…", "En la meva opinió…".
- **Suport i credibilitat**: 3 arguments ben diferenciats (contingut, forma, impacte). Cada un amb evidència de l'obra.
- **Perspectivisme**: Recomanació per a un públic específic amb justificació.
- **Control de la informació**: No revelar elements sorpresa. Indicar "sense revelar el final" si cal.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Completitud i context**: Identificació amb context cultural o biogràfic rellevant de l'autor.
- **Objectivitat i seqüència**: Descripció completa amb elements formals (estructura, personatges, estil) si és rellevant.
- **Metacognició i precisió**: Distinció precisa entre el que és objectiu (fet de l'obra) i el que és subjectiu (judici argumentat).
- **Suport i credibilitat**: Arguments elaborats amb exemples concrets i específics de l'obra.
- **Perspectivisme**: Recomanació matisada: per a qui sí, per a qui potser no.
- **Control de la informació**: Control conscient de la informació revelada. El lector pot decidir si vol llegir-la.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Completitud i context**: Identificació amb context ampli: tradició, gènere, recepció crítica inicial.
- **Objectivitat i seqüència**: Descripció precisa que permet al lector entendre l'obra sense haver-la llegit o vista.
- **Metacognició i precisió**: Distinció sofisticada entre descripció, interpretació i valoració com a tres capes explícites.
- **Suport i credibilitat**: Arguments rigorosos amb cites o referències específiques a l'obra.
- **Perspectivisme**: Recomanació crítica que pot contenir reserves o condicions.
- **Control de la informació**: Gestió precisa: descriure sense revelar, incitar sense enganyar.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


