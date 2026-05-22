---
name: generate-mapa-mental
description: >
  Use when the teacher has activated the "mapa_mental" complement. Generates
  a radial mind map (Buzan-style): central concept surrounded by primary
  branches with associative ideas, generating questions, and
  interdisciplinary connections. DIFFERENT from `generate-mapa-conceptual`:
  mind map prioritises divergent thinking and free association; concept map
  prioritises hierarchical structure and labelled relationships.
  Output is markdown that can be copy-pasted into Canva, MindMeister, XMind.
author: FJE — Fundació Jesuïtes Educació
version: 1.0.0-proto
complement_key: mapa_mental
agent_role: complements
tools_required: []
triggers:
  - path: params.complements.mapa_mental
    equals: true
---

# Generar mapa mental

## Quan activar aquesta skill

Activar quan el docent ha marcat el complement **"Mapa mental"** al Pas 2.
És especialment útil per a:
- **Altes capacitats** (AC): brainstorming, generació d'idees, connexions
  interdisciplinars.
- **Recapitulació o introducció** d'un tema (no per a estructurar contingut
  jeràrquic — això és la feina del mapa conceptual).
- **Estimular pensament divergent**: associacions lliures, preguntes
  generadores.

## Distinció fonamental amb el mapa conceptual

| Dimensió | Mapa conceptual | Mapa mental |
|---|---|---|
| **Estructura** | Jeràrquica (general → específic) | Radial (centre → expansió 360°) |
| **Relacions** | Etiquetades (proposicions: "X causa Y") | No etiquetades (associació lliure) |
| **Funció cognitiva** | Organitzar i comprendre estructura | Generar idees i connexions creatives |
| **Output** | Llista jeràrquica amb sagnies progressives | Branques radials + preguntes generadores |
| **Quan triar** | Comprensió d'un tema acabat | Exploració d'un tema obert |

## Format de sortida (markdown)

A diferència del mapa conceptual (sagnia jeràrquica), el mapa mental és
una estructura **radial** que es representa com a llista amb el concepte
central destacat i branques amb associacions:

```markdown
## Mapa mental

**[CONCEPTE CENTRAL]**

🌿 Branca 1: [associació primària]
   → [idea associada]
   → [pregunta generadora?]
   → [connexió amb altra matèria]

🌿 Branca 2: [associació primària]
   → [idea associada]
   → [exemple concret de la vida quotidiana]
   → [pregunta provocadora?]

🌿 Branca 3: [associació primària]
   → [...]

🔗 Connexions transversals:
- [Branca X] ↔ [Branca Y]: [com es relacionen]
```

**No** usar caràcters ASCII-art (`│ ├ └ ─`). El docent ho copia a Canva o
MindMeister i la sintaxi ASCII no es renderitza bé.

## Graduació per nivell MECR

| Nivell | Nombre branques | Profunditat | Llenguatge | Característica clau |
|---|---|---|---|---|
| **Pre-A1 / A1** | 2-3 branques | 1 nivell | Paraules clau soles | Imatges/emojis + paraula. Cap pregunta abstracta. |
| **A2** | 3-4 branques | 1-2 nivells | Frases molt curtes | Una idea per branca + 1 connexió concreta |
| **B1** | 4-5 branques | 2 nivells | Frases gradades B1 | Afegir 1-2 preguntes generadores |
| **B2** | 5-7 branques | 2-3 nivells | Lèxic d'especialitat permès | Preguntes obertes + 1-2 connexions interdisciplinàries |
| **C1+** | 5-8 branques | 3 nivells | Llenguatge metacognitiu | Preguntes provocadores + tensions/contradiccions + connexió amb fonts externes |

## Quan NO és apropiat

- **Mapa conceptual ja seleccionat**: redundància. El docent ha de triar un
  dels dos, no els dos junts. Si ambdós actius: prioritzar mapa conceptual
  per a tasques d'estudi tradicional.
- **Pre-A1 amb alumne sense alfabetització L1**: el patró radial pot
  confondre. Substituir per dibuix amb pictogrames lineals.
- **Textos molt curts (< 50 paraules)**: no hi ha prou matèria per
  generar branques significatives.

## Exemple per a B1 — Tema: la fotosíntesi

```markdown
## Mapa mental

**FOTOSÍNTESI**

🌿 Què és?
   → Transformació de llum en aliment
   → Només les plantes ho fan?
   → 🔗 Connexió amb la cuina: per què cuinem els aliments?

🌿 Quins ingredients?
   → Aigua + diòxid de carboni + llum solar
   → Què aporta cadascun?
   → 🔗 Connexió amb Química 1r ESO (matèria/energia)

🌿 On passa?
   → A les fulles (cloroplasts)
   → Per què les fulles són verdes?

🌿 Quin resultat dona?
   → Sucres (glucosa) + oxigen
   → Per què respirem millor on hi ha boscos?
   → 🔗 Connexió amb Geografia (canvi climàtic, pulmó verd)

🔗 Connexions transversals:
- "Què passa?" ↔ "Quin resultat?" : la transformació explica el resultat
- "Quins ingredients?" ↔ "Per què respirem millor?" : entrada CO₂ ↔ sortida O₂
```

## Notes pedagògiques (MALL)

- **No és un esquema d'estudi**: és una eina de **divergència**, d'obertura
  cognitiva. Si el docent vol que l'alumne estructuri un tema per estudiar-lo,
  usar mapa conceptual.
- **Les preguntes generadores** són clau: una branca sense pregunta és una
  llista, no un mapa mental.
- **Les connexions transversals** són el valor afegit més gran. Si el
  resultat no inclou cap, el mapa s'ha quedat curt.
- **Color/imatges al Canva**: el docent acaba la peça visual. ATNE proveeix
  l'estructura semàntica.

## Referències

- Buzan, T. (1974). *Use Your Head*. BBC Books. (mapa mental original)
- Novak, J. & Gowin, B. (1984). *Learning How to Learn*. (mapa conceptual,
  contrast amb mapa mental)
- MALL FJE — divergència vs. organització estructural (M2 instruments-mediacio)
