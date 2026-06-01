---
tipus: derivat
font_canonic: M3_instrument-generar-bastides-lectura.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-01'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 7d25631d63b18a68
---

# Generar bastides de lectura — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar bastides de lectura per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Activació de previs**: L'adult activa amb una imatge: "Què veus aquí?". L'alumne assenyala o anomena.
- **Propòsit de lectura**: Propòsit oral de l'adult: "Anem a saber què passa amb [X]".
- **Modalitat lectora**: L'adult llegeix en veu alta. L'alumne assenyala, dramatitza o dibuixa el que entén. **Zero lectura autònoma.**
- **Plànol literal — Resum**: Dibuixar el que ha après. Dictat oral a l'adult. Ordenació d'imatges.
- **Autoregulació (metacognició)**: "He fet el que m'ha dit el mestre." (registre oral/gestual de l'adult).
- **Volum màxim per moment**: 1-2 accions gestuals/orals per moment.
- **No duplicar `preguntes_comprensio`**: Les bastides donen el procediment; les preguntes detallades són del complement `preguntes_comprensio`.
- **Especificitat del propòsit**: Propòsit referit a una imatge o paraula concreta del text.
- **Format obligatori**: Secció `## Bastides` amb sub-H3 `### Bastides de lectura` i bullets per moment (`- **Abans:**`, `- **Durant:**`, `- **Després:**`).
- **Reflexió en primera persona**: *(via adult)* "He assenyalat el que m'ha demanat el mestre."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Activació de previs**: 1 pregunta d'activació de previs en frase simple ("Què saps de [tema]?").
- **Propòsit de lectura**: Propòsit explícit i concret: "Llegeix per saber [una cosa concreta]".
- **Hipòtesi prèvia**: Predicció pel títol: "De què creus que parlarà?". 1 paraula o frase mínima.
- **Modalitat lectora**: Lectura mediada per l'adult; l'alumne segueix amb el dit. Subratlla 1 mot clau per paràgraf.
- **Plànol literal — Resum**: **Frase-buit** literal d'un sol buit: "El text parla de ___".
- **Autoregulació (metacognició)**: "He llegit el text amb el mestre i he marcat la paraula difícil."
- **Volum màxim per moment**: Màxim 3 ítems per moment.
- **No duplicar `preguntes_comprensio`**: Idem.
- **Especificitat del propòsit**: Propòsit específic del text actual, no genèric.
- **Format obligatori**: Idem.
- **Reflexió en primera persona**: "He marcat una paraula important. He completat la frase-buit del resum."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Activació de previs**: 2 preguntes d'activació + ancoratge a una experiència concreta.
- **Propòsit de lectura**: + propòsit operatiu amb verb d'acció: "Llegeix per identificar [X]".
- **Hipòtesi prèvia**: Predicció breu escrita: "Crec que el text dirà…".
- **Modalitat lectora**: Lectura autònoma possible. Marca ✓ (entès) / ? (dubte) / ! (important) al marge.
- **Plànol literal — Resum**: Resum breu de 2-3 frases sobre què tracta el text.
- **Plànol inferencial**: 1 pregunta inferencial guiada: "Per què creus que…?".
- **Autoregulació (metacognició)**: "He llegit i he marcat ✓/? / !. He fet el resum."
- **Volum màxim per moment**: Màxim 3 ítems per moment.
- **No duplicar `preguntes_comprensio`**: Idem.
- **Especificitat del propòsit**: Idem.
- **Format obligatori**: Idem.
- **Reflexió en primera persona**: "He marcat ✓/? /! mentre llegia. He escrit de què tracta el text."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Activació de previs**: Activació + predicció pel títol o imatge inicial.
- **Propòsit de lectura**: + propòsit jeràrquic: "Llegeix per distingir el fet principal del context".
- **Hipòtesi prèvia**: Hipòtesi pròpia formulada per escrit: "Hipòtesi: ___. Per què: ___".
- **Modalitat lectora**: Lectura autònoma. Notes marginals breus (1-3 paraules per marca).
- **Hipòtesi en curs**: **Pausa obligatòria** marcada al text (símbol ⏸ o instrucció "Atura't aquí") on l'alumne escriu hipòtesi en curs: "Fins aquí, crec que el text dirà que…".
- **Plànol literal — Resum**: Resum estructurat de 3-4 frases (idea principal + 2 secundàries).
- **Plànol inferencial**: Inferència explícita: "Quin era l'objectiu de l'autor?" + "Què queda implícit?".
- **Plànol crític / Valoració**: Valoració simple: "Estàs d'acord amb el que diu el text? Per què?".
- **Autoregulació (metacognició)**: "He revisat si la meva hipòtesi inicial era correcta o no."
- **Volum màxim per moment**: Màxim 3 ítems per moment.
- **No duplicar `preguntes_comprensio`**: Idem.
- **Especificitat del propòsit**: Idem.
- **Format obligatori**: Idem.
- **Reflexió en primera persona**: "He fet una hipòtesi abans de llegir. He comprovat si era correcta."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Activació de previs**: + identificació del gènere i de l'autor/font.
- **Propòsit de lectura**: + propòsit avaluatiu: "Llegeix per avaluar la fiabilitat de les dades".
- **Hipòtesi prèvia**: + identificació del posicionament inicial probable de l'autor.
- **Modalitat lectora**: + identificació explícita del posicionament de l'autor al marge.
- **Hipòtesi en curs**: + a la mateixa pausa, **revisió explícita** de la hipòtesi inicial: "La meva hipòtesi era X, ara crec Y, per què…".
- **Plànol literal — Resum**: Resum amb jerarquització explícita (titular + cos).
- **Plànol inferencial**: + detecció de pressuposicions i seleccions narratives no explícites.
- **Plànol crític / Valoració**: Avaluació de fiabilitat: "Fins a quin punt és objectiu l'autor? Quines proves dóna?".
- **Autoregulació (metacognició)**: "He pensat si l'autor és imparcial. He comprovat si dóna proves de les seves afirmacions."
- **Volum màxim per moment**: Màxim 3 ítems per moment.
- **No duplicar `preguntes_comprensio`**: Idem.
- **Especificitat del propòsit**: Idem.
- **Format obligatori**: Idem.
- **Reflexió en primera persona**: "He identificat la postura de l'autor. He avaluat si les dades eren fiables."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Activació de previs**: + l'alumne formula les seves pròpies preguntes de lectura abans de llegir.
- **Propòsit de lectura**: + propòsit metacognitiu: l'alumne formula el seu propi propòsit i justifica per què.
- **Hipòtesi prèvia**: + plantejament d'hipòtesis contrastades.
- **Modalitat lectora**: + contrast actiu amb coneixements previs anotat: "Aquí diu X però jo sabia Y".
- **Hipòtesi en curs**: + a la mateixa pausa, **reformulació metacognitiva**: "Si la meva hipòtesi falla, què revela el text que jo no sabia?".
- **Plànol literal — Resum**: Resum sintètic + comparació amb hipòtesi inicial.
- **Plànol inferencial**: + anàlisi de l'enquadrament: "Què queda fora del marc del text? Per què?".
- **Plànol crític / Valoració**: Contrast crític: "Quines altres fonts caldrien per validar aquesta informació?".
- **Autoregulació (metacognició)**: "He entès tot el que calia? Quines preguntes m'han quedat obertes? Quin pas faria a continuació?"
- **Volum màxim per moment**: Màxim 3 ítems per moment.
- **No duplicar `preguntes_comprensio`**: Idem.
- **Especificitat del propòsit**: Idem.
- **Format obligatori**: Idem.
- **Reflexió en primera persona**: "He formulat les meves pròpies preguntes abans de llegir i he comprovat si el text les responia."

