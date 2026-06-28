---
tipus: derivat
font_canonic: M3_genere-escriure-dialeg.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 18c26096b6c9d33a
---

# Escriure/adaptar un diàleg — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un diàleg per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Presentació**: 2 personatges llistats amb nom. Sense descripcio.
- **Claredat formal**: Torns atribuïts per nom en negreta: **Marc:** / **Sofia:**. Mai amb inicials o lletres (A:, B:).
- **Subtext i accio**: Acotacio molt simple: "En Marc entra." / "La Sofia somriu." Present, 3a persona. 1 accio.
- **Tensio dramatica**: Tensio simple en 1 torn: "Vull X. — No pots."
- **Extensio**: 6-8 torns totals. 1-2 frases per torn.
- **Format i fidelitat**: Llista de personatges present al principi. Cap torn amb inicials. Cap acotacio amb ironia. Manté personatges i conflicte principals del text font.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Presentació**: 2 personatges amb 1 linia de descripcio cadascun.
- **Claredat formal**: Torns atribuïts per nom en negreta. Format consistent al llarg del dialeg.
- **Subtext i accio**: 1 accio per acotacio, sense subordinades. Present, 3a persona. Subtext explícit senzill.
- **Tensio dramatica**: Conflicte simple i resolucio clara en 6-8 torns.
- **Extensio**: 8-10 torns. Frases fins a 10 paraules per torn.
- **Format i fidelitat**: Idem. Subtext explícit a les acotacions. La resolucio del conflicte és clara. Manté l'ordre i la resolucio del text font.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Presentació**: 2-3 personatges amb descripcio i relacio entre ells.
- **Claredat formal**: Torns atribuïts per nom. L'atribucio mai és ambigua (cap torn "flotant").
- **Subtext i accio**: Acotacio amb subtext emocional explícit: "[La Sofia fa un pas enrere, preocupada.]"
- **Tensio dramatica**: Conflicte amb 2 punts de vista diferenciats. Inclou 1 moment d'argumentacio.
- **Extensio**: 10-12 torns. Frases de fins a 15 paraules per torn.
- **Format i fidelitat**: Idem. Les acotacions no confonen accio amb judici. Manté els punts de vista dels personatges del text font.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Presentació**: 3-4 personatges amb tret diferenciador i funcio en el conflicte.
- **Claredat formal**: Torns atribuïts amb nom + acotacio breu si la veu pot confondre's.
- **Subtext i accio**: Acotacions que revelen intencions no dites. 1 accio per acotacio.
- **Tensio dramatica**: Conflicte complex amb postures elaborades per cada personatge.
- **Extensio**: 12-15 torns. Frases elaborades.
- **Format i fidelitat**: Idem. Manté matisos i complexitat del conflicte original. L'acotacio pot contradir o matisar el torn si escau.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Presentació**: 3-4 personatges amb motivacio i postura explícites.
- **Claredat formal**: Torns atribuïts per nom. La veu de cada personatge és diferenciada lingüísticament.
- **Subtext i accio**: Acotacions detallades amb subtext complex. Sense ironia ni judicis sobre el personatge.
- **Tensio dramatica**: Conflicte de valors o de visions del mon. Resolucio no necessariament clara.
- **Extensio**: 12-15+ torns. Llargada variable segons el ritme dramatic.
- **Format i fidelitat**: Idem. Manté intencio retorica i matisos del text font. Sense monolegs interns llargs.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


