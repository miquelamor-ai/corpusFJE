---
tipus: derivat
font_canonic: M3_genere-escriure-diari.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-20'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: f11a8f14a534561d
---

# Escriure/adaptar una entrada de diari — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una entrada de diari per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Format i precisió**: Data en format simple: "Dilluns" / "12/05".
- **Seqüència i rellevància**: 1-2 frases de fets en passat simple. Ordre cronològic estricte.
- **Precisió i ancoratge**: 1 emoció nomenada: "Estava content." / "Tenia por."
- **Profunditat i orientació**: 1 frase de reflexió orientada a l'aprenentatge: "He après que..."
- **Consistència i naturalitat**: Primera persona consistent: "he", "em", "vaig".
- **Separació dels blocs**: Tres seccions clarament separades, 1 frase per bloc. Cap barreja fets/emocions.
- **Variant acadèmica (B1+)**: No s'aplica.
- **Fidelitat al text font**: Fidelitat als fets principals i a la veu en primera persona.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Format i precisió**: Data completa: "Dilluns, 12 de maig de 2026".
- **Seqüència i rellevància**: 3-4 frases de fets ordenats cronològicament. Connectors simples.
- **Precisió i ancoratge**: 2 emocions amb matís lleu: "Estava una mica nerviós però content."
- **Profunditat i orientació**: Reflexió de 2 frases amb connector causal: "Per això crec que..."
- **Consistència i naturalitat**: Primera persona en tots els verbs principals. Cap canvi a tercera persona.
- **Separació dels blocs**: Tres blocs diferenciats per paràgraf o línia en blanc.
- **Variant acadèmica (B1+)**: No s'aplica.
- **Fidelitat al text font**: Fidelitat als fets, a les emocions i a la reflexió essencial.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Format i precisió**: Data completa + context breu si escau ("Primer dia de campaments").
- **Seqüència i rellevància**: Fets narrats amb causa explícita. Connectors temporals variats. Selecció dels moments clau.
- **Precisió i ancoratge**: 2-3 emocions variades i situades en el moment: "Quan vaig veure X, em vaig sentir Y."
- **Profunditat i orientació**: Conclusió clara de 2-3 frases. Diari acadèmic (B1+): "Els resultats mostren que..."
- **Consistència i naturalitat**: Primera persona consistent i variada. Veu pròpia recognoscible.
- **Separació dels blocs**: Tres paràgrafs clarament diferenciats amb transicions naturals entre blocs.
- **Variant acadèmica (B1+)**: Quan el context és acadèmic (diari de laboratori, projecte): bloc fets → "Observació"; bloc reflexió → "Conclusions" ("Els resultats mostren que..."). El to és acadèmic, no memorialístic.
- **Fidelitat al text font**: Fidelitat als fets, a les emocions, a la reflexió i al to personal.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Format i precisió**: Data completa integrada naturalment a l'entrada.
- **Seqüència i rellevància**: Fets en relació amb el context. Selecció conscient dels fets més rellevants per a la reflexió.
- **Precisió i ancoratge**: Emocions analitzades: no només nomenades, sinó explicades en relació als fets.
- **Profunditat i orientació**: Reflexió que connecta l'experiència amb coneixements previs o futurs.
- **Consistència i naturalitat**: Primera persona natural, no forçada. Veu personal diferenciada.
- **Separació dels blocs**: Blocs integrats amb transicions elaborades que mantenen la distinció fets/emocions/reflexió.
- **Variant acadèmica (B1+)**: Tots tres blocs amb vocabulari acadèmic. Fets → Observació o resultats. Emocions → Valoració del procés. Reflexió → Conclusions.
- **Fidelitat al text font**: Fidelitat a la complexitat emocional i reflexiva del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Format i precisió**: Data completa. Pot incloure el context situacional si és rellevant per a la comprensió.
- **Seqüència i rellevància**: Fets narrats amb perspectiva sobre la seva significació. Pot incloure contrast entre expectativa i realitat.
- **Precisió i ancoratge**: Emocions complexes o contradictòries amb reflexió sobre el seu origen i significat.
- **Profunditat i orientació**: Reflexió metacognitiva: "com he après" i "qué m'ha sorprès", no només "qué he après".
- **Consistència i naturalitat**: Primera persona reflexiva: "m'he adonat que", "he reconsiderat", "em pregunto si".
- **Separació dels blocs**: Blocs fluïts però clarament discernibles per al lector. La integració no amaga la distinció.
- **Variant acadèmica (B1+)**: Reflexió crítica sobre el procés d'aprenentatge, incloent limitacions i reptes.
- **Fidelitat al text font**: Fidelitat a la complexitat, als matisos i a les contradiccions si les hi ha.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


