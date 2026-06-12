---
tipus: derivat
font_canonic: M3_instrument-generar-cartes-conversacionals.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-12'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: de9f447faf0ce158
---

# Generar cartes conversacionals — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar cartes conversacionals per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Nombre i complexitat**: NO generar.
- **Repertori lingüístic**: NO generar.
- **Registre i objectiu**: NO generar.
- **Connexió amb el text**: NO generar.
- **Metareflexió del grup**: NO generar.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Nombre i complexitat**: 2 rols: Proposador/a + Objector/a. Format simplificat per parelles.
- **Repertori lingüístic**: 2 iniciadors per rol. Frases curtes i segures (Jo penso que ___ / Jo crec que no ___).
- **Registre i objectiu**: Exploratòria: posicions obertes, errors tolerats, raonament visible. "I si...?" "Potser...".
- **Connexió amb el text**: Iniciadors genèrics ("Jo penso que ___"). Curts i segurs. Fàcils de dir.
- **Metareflexió del grup**: "Hem dit ___. Algú vol afegir alguna cosa?" (Element obert simple).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Nombre i complexitat**: 3-4 rols: Proposador + Objector + Mediador + Sintetitzador.
- **Repertori lingüístic**: 3 iniciadors per rol. Frases completes adaptades a la HCL del rol (Argumentar, Contrargumentar, Mediar).
- **Registre i objectiu**: Exploratòria o disputativa: comença explorant, pot formalitzar-se si el grup avança.
- **Connexió amb el text**: Iniciadors específics de la pregunta de debat del text. Causals i justificatius ("El text diu que... i per això crec que...").
- **Metareflexió del grup**: "La conclusió del grup és ___. El que no hem resolt és ___." (Tancament + obertura).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Nombre i complexitat**: 4 rols complets amb registre formal i terminologia de debat.
- **Repertori lingüístic**: 3 iniciadors amb vocabulari CALP i connectors argumentals (Malgrat que..., Tenint en compte que...).
- **Registre i objectiu**: Disputativa: posicions definides, argumentació formal, citació d'evidències del text.
- **Connexió amb el text**: Iniciadors que inclouen citació del text ("Segons el text...", "D'acord amb..."). Registre formal.
- **Metareflexió del grup**: "El que no hem resolt és ___. Per resoldre-ho caldria saber ___." (Apertura epistemica).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Nombre i complexitat**: 4 rols + capa metacognitiva al Sintetitzador (detecció de biaixos i punts cecs).
- **Repertori lingüístic**: 3 iniciadors dialèctics o retòrics que qüestionen la postura contrària (Si fos cert que X, llavors...).
- **Registre i objectiu**: Disputativa amb metacognició: detecció de biaixos, qüestionament de la fiabilitat de les fonts.
- **Connexió amb el text**: Iniciadors que qüestionen, matisen i detecten biaixos ("Però si pensem que X, el text podria estar ignorant...").
- **Metareflexió del grup**: "El que queda obert és ___. Per respondre-ho, caldria contrastar amb ___ i revisar si els nostres arguments son fiables."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


