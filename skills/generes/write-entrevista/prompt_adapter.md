---
tipus: derivat
font_canonic: M3_genere-escriure-entrevista.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-05-31'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 238a6c7a4f9007f6
---

# Escriure/adaptar una entrevista — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una entrevista per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Context i rellevància**: 1 frase: qui és i per qué.
- **Consistència gràfica**: **P:** i **R:** en negreta. Consistent en tot el text.
- **Precisió i focus**: Preguntes de 1-2 paraules clau o 1 frase simple ("Qué fas?", "On vius?").
- **Veu i autenticitat**: Respostes de 1-2 frases en primera persona.
- **Extensió i cobertura**: 3-4 parells P/R.
- **Termes tècnics de l'entrevistat**: Sense termes tècnics (o amb explicació immediata entre parèntesi).
- **No linearitzar**: Cap frase de transició narrativa entre P/R ("l'entrevistat va contestar que..."). Format P/R pur.
- **Fidelitat al text font**: Fidelitat a les idees principals de l'entrevistat i al format P/R.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Context i rellevància**: 2 frases: qui és i per qué és rellevant entrevistar-lo.
- **Consistència gràfica**: **P:** i **R:** en negreta. Format perfectament consistent.
- **Precisió i focus**: Preguntes directes d'una sola idea. Sense preguntes dobles ni retòriques.
- **Veu i autenticitat**: Respostes de 2-3 frases. Primera persona consistent. Cap transformació a 3a persona.
- **Extensió i cobertura**: 4-5 parells P/R.
- **Termes tècnics de l'entrevistat**: 1 terme tècnic màxim, explicat entre parèntesi o al costat.
- **No linearitzar**: Idem.
- **Fidelitat al text font**: Fidelitat a les idees, al registre bàsic i al format.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Context i rellevància**: 3-4 frases de context professional o personal que justifiquen l'entrevista.
- **Consistència gràfica**: **P:** i **R:** en negreta. Cap ambigüitat sobre qui parla en cap moment.
- **Precisió i focus**: Preguntes d'una idea que exploren un aspecte concret. Sense preguntes retòriques.
- **Veu i autenticitat**: Respostes de 3-4 frases amb matís. Veu de l'entrevistat preservada i recognoscible.
- **Extensió i cobertura**: 5-6 parells P/R.
- **Termes tècnics de l'entrevistat**: Termes tècnics explicats entre claudàtors [terme: significat] o en nota al final.
- **No linearitzar**: Idem.
- **Fidelitat al text font**: Fidelitat a les idees, al registre, a la veu de l'entrevistat i al format.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Context i rellevància**: Presentació completa amb context social o professional.
- **Consistència gràfica**: **P:** i **R:** en negreta. La veu de l'entrevistat és lingüísticament diferenciable de la del periodista.
- **Precisió i focus**: Preguntes que conviden a defensar posicions o explicar processos complexos.
- **Veu i autenticitat**: Respostes que mostren el punt de vista de l'entrevistat amb arguments i evidències.
- **Extensió i cobertura**: 6-7 parells P/R. Pot incloure 1 pregunta de seguiment.
- **Termes tècnics de l'entrevistat**: Termes tècnics explicats naturalment dins del text.
- **No linearitzar**: Idem.
- **Fidelitat al text font**: Fidelitat a la complexitat de les idees i al to de l'entrevistat.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Context i rellevància**: Presentació que situa l'entrevistat en el seu camp i dona el marc de l'entrevista.
- **Consistència gràfica**: **P:** i **R:** en negreta. La diferència de registre i veu entre entrevistador i entrevistat és evident.
- **Precisió i focus**: Preguntes que qüestionen, matisen o aprofundeixen. Pot incloure preguntes de seguiment.
- **Veu i autenticitat**: Respostes que mostren la complexitat de la postura. Pot incloure matisos i contradiccions.
- **Extensió i cobertura**: 7-10 parells P/R. Moments de tensió dialèctica quan el tema ho permet. La profunditat de cada rèplica és més rellevant que el nombre total.
- **Termes tècnics de l'entrevistat**: Termes tècnics integrats; glossari al final si hi ha molts.
- **No linearitzar**: Idem. Pot incloure una nota editorial breu entre claudàtors [nota de la redacció] si és rellevant.
- **Fidelitat al text font**: Fidelitat a la complexitat, al to, als matisos i als moments de tensió del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


