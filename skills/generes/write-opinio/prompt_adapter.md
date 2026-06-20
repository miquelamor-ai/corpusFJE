---
tipus: derivat
font_canonic: M3_genere-escriure-opinio.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-20'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 554fa0285a4be904
---

# Escriure/adaptar un article d'opinió — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un article d'opinió per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Formulació**: Una sola oració que comença amb "Crec que…". Sense preàmbul.
- **Posició al text**: Primera frase del text.
- **Nombre**: Màxim 2 arguments.
- **Tipus d'evidència**: Exemple de la vida quotidiana de l'alumne.
- **Nombre per argument**: 1 evidència per argument.
- **Inventari per nivell**: "perquè", "i", "però".
- **Varietat funcional**: N/A — només un tipus disponible.
- **Inclusió**: No requerit.
- **Format i funció**: Una frase: "Per això, crec que…". Reprèn la tesi.
- **Reflexió sobre el procés**: "He pensat què crec abans d'escriure, i he buscat 2 raons que m'ajudin a explicar-ho."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Formulació**: Clara i directa, en primera persona. Una oració.
- **Posició al text**: Al primer paràgraf.
- **Nombre**: 2-3 arguments.
- **Tipus d'evidència**: Exemple concret o dada simple.
- **Nombre per argument**: 1 evidència per argument.
- **Inventari per nivell**: "perquè", "per tant", "però", "a més".
- **Varietat funcional**: N/A — repertori limitat.
- **Inclusió**: No requerit.
- **Format i funció**: 1-2 frases. Reprèn la tesi. No introdueix arguments nous.
- **Reflexió sobre el procés**: "He comprovat que la meva tesi s'entén de seguida i que tinc un exemple per a cada raó."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Formulació**: Clara i directa. Pot ser de 2 oracions. Primera persona o impersonal.
- **Posició al text**: Al primer paràgraf.
- **Nombre**: 3 arguments.
- **Tipus d'evidència**: Dada, exemple concret o cita breu.
- **Nombre per argument**: 1 evidència per argument.
- **Inventari per nivell**: "en primer lloc", "a més", "per tant", "en conclusió".
- **Varietat funcional**: Es recomana variar: causa (perquè) + addició (a més) + conclusió (per tant).
- **Inclusió**: Opcional ("Algú pot pensar que… però…").
- **Refutació**: Suggerida si s'inclou contraargument.
- **Format i funció**: 2-3 frases. Reprèn i reforça la tesi. Pot incloure una crida a l'acció.
- **Reflexió sobre el procés**: "He revisat si els meus arguments es relacionen entre ells i si la conclusió tanca el que vaig anunciar a la tesi."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Formulació**: Pot ser impersonal ("Cal considerar que…"). Elaborada però sense preàmbul.
- **Posició al text**: Al primer paràgraf.
- **Nombre**: 3-4 arguments amb estructura interna.
- **Tipus d'evidència**: Dada estadística, cita d'expert o exemple complex.
- **Nombre per argument**: 1-2 evidències per argument.
- **Inventari per nivell**: "d'altra banda", "per contra", "en conseqüència", "en resum". **"Tanmateix" i "no obstant això" només a partir de B2**.
- **Varietat funcional**: **Obligatori**: cada argument introduït amb un tipus diferent (causa / contrast / addició / conclusió). No repetir el mateix tipus.
- **Inclusió**: Obligatori: contraargument en paràgraf separat.
- **Refutació**: Refutació concreta amb evidència pròpia.
- **Format i funció**: 3-4 frases. Argumentada. Pot reformular la tesi amb matís.
- **Reflexió sobre el procés**: "He pensat què diria algú que no opina com jo, i he intentat respondre-li al text. Així he vist on era forta o feble la meva postura."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Formulació**: Complexa. Pot matisar la pròpia postura o ser paradoxal. Sense preàmbul.
- **Posició al text**: Al primer paràgraf.
- **Nombre**: 3-5 arguments amb jerarquització explícita.
- **Tipus d'evidència**: Evidències múltiples i variades; pot incloure contrastos entre fonts.
- **Nombre per argument**: Múltiples, segons la complexitat de l'argument.
- **Inventari per nivell**: Connectors d'especialitat acadèmica propis de la disciplina. Variació rica i precisa.
- **Varietat funcional**: Cada relació lògica marcada amb el connector funcional adequat (causal, concessiu, consecutiu, contrastiu, additiu). Sense repetició de tipus.
- **Inclusió**: Obligatori: contraargument elaborat amb matís.
- **Refutació**: Refutació fonamentada, integra el contraargument al raonament.
- **Format i funció**: Reformulació complexa de la tesi amb integració de les tensions identificades.
- **Reflexió sobre el procés**: "He reflexionat sobre els límits de la meva pròpia postura: quines suposicions estic fent? Quines evidències em manquen?"

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


