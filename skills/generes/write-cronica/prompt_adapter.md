---
tipus: derivat
font_canonic: M3_genere-escriure-cronica.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-21'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 7695fb453ef6f0c0
---

# Escriure/adaptar una crònica — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una crònica per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Seqüència i precisió**: "Primer", "després", "al final". 3-4 moments.
- **Visibilitat i consistència**: Primera persona plural ("vam veure", "vam anar"). Consistent.
- **Organització i progressió**: 3-4 moments en ordre cronològic estricte. 1-2 frases per moment.
- **Concreció i atmosfera**: 1 descripció sensorial per moment: qué es veu o s'escolta.
- **Rigor i reflexió**: Sense valoració final (no requerida a A1).
- **Connectors**: Almenys 2 connectors temporals diferents al llarg del text. Cap repetició sistemàtica del mateix connector.
- **Especulació sobre tercers**: Cap especulació sobre el que altres persones pensaven o sentien. Només el que el cronista ha observat directament.
- **Fidelitat al text font**: Fidelitat als fets principals i a la perspectiva testimonial bàsica.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Seqüència i precisió**: "A les X", "de sobte", "llavors". 4-5 moments.
- **Visibilitat i consistència**: Primera persona (singular o plural) visible i consistent en tot el text.
- **Organització i progressió**: 4-5 moments ordenats. 2-3 frases per moment. Connexió simple entre moments.
- **Concreció i atmosfera**: Descripció sensorial i emocional breu per moment.
- **Rigor i reflexió**: Valoració d'una frase al final, clarament separada dels fets.
- **Connectors**: Varietat mínima de 3 connectors temporals de tipus diferent. Cap connector repetit en moments consecutius.
- **Especulació sobre tercers**: Idem.
- **Fidelitat al text font**: Fidelitat als fets, a la perspectiva i a la valoració essencial.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Seqüència i precisió**: Marcadors temporals precisos (hores concretes o expressions precises: "just quan", "a mesura que").
- **Visibilitat i consistència**: Perspectiva del cronista consistent. Selecció d'allò que el cronista ha viscut directament.
- **Organització i progressió**: 4-5 moments amb connexió causal. La seqüència mostra progressió i evolució de l'event.
- **Concreció i atmosfera**: Descripcions sensorials integrades a la narració (no en llista separada).
- **Rigor i reflexió**: Valoració de 2-3 frases al final, en paràgraf separat. No barrejada amb els fets.
- **Connectors**: Combinació de connectors temporals i 1-2 causals. La varietat reflecteix la progressió i causalitat de l'event.
- **Especulació sobre tercers**: Idem. Les emocions d'altri s'infereixen de comportaments observats, no s'afirmen.
- **Fidelitat al text font**: Fidelitat als fets, a la perspectiva, a la valoració i al to testimonial.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Seqüència i precisió**: Temporalitat precisa integrada naturalment a la narració.
- **Visibilitat i consistència**: Perspectiva del cronista amb veu pròpia clarament diferenciada dels fets.
- **Organització i progressió**: 5-6 moments amb detall creixent i tensió narrativa.
- **Concreció i atmosfera**: Descripcions riques: visuals, auditives, olfactives o tàctils. Integrades al text.
- **Rigor i reflexió**: Valoració argumentada que connecta l'experiència amb un context més ampli.
- **Connectors**: Connectors temporals i causals variats i integrats naturalment al text. Cap patró de repetició visible.
- **Especulació sobre tercers**: Idem. Pot incloure cites textuals d'altres participants.
- **Fidelitat al text font**: Fidelitat als fets, a la perspectiva, a la valoració i al context.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Seqüència i precisió**: Temporalitat elaborada que reflecteix el ritme de l'experiència viscuda.
- **Visibilitat i consistència**: Perspectiva crítica: el cronista interpreta l'event, no només el narra.
- **Organització i progressió**: 5-6 moments amb variació de ritme narratiu (acceleració i aturada).
- **Concreció i atmosfera**: Descripcions elaborades que creen atmosfera i situen el lector en l'experiència.
- **Rigor i reflexió**: Valoració crítica que analitza l'impacte o el significat de l'event.
- **Connectors**: Connectors sofisticats que reflecteixen el ritme i la intensitat de l'experiència. Pot incloure adversatius o concessius.
- **Especulació sobre tercers**: Idem. La perspectiva dels altres s'atribueix amb marcadors ("semblava que", "ens va dir que").
- **Fidelitat al text font**: Fidelitat a la complexitat experiencial del text original, incloent matisos i contradiccions.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


