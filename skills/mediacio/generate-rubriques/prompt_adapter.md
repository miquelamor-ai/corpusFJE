---
tipus: derivat
font_canonic: M3_instrument-generar-rubriques.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-01'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 6923f54163438e53
---

# Generar rúbriques d'autoavaluació — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar rúbriques d'autoavaluació per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Estructura de l'instrument**: Checklist d'icones: ✅ / ❌ per a cada ítem. Sense escala. Molt visual. Adult media la revisió oral.
- **Amplitud d'avaluació**: 2-3 criteris molt concrets i visuals. Accionables a pre-A1 (He dibuixat / He assenyalat).
- **Concretesa del descriptor**: Acció visible: "He dibuixat els 3 moments." / "He assenyalat el personatge." Mai "He fet bé".
- **Perspectiva alumne-facing**: "He fet ___ / He posat ___." Molt concret i físic.
- **Naturalesa de l'excel·lència**: Cap descriptor AE: checklist binari.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Estructura de l'instrument**: Taula simplificada: 2-3 criteris × 3 nivells (Encara no / Sí / Sí, i alguna cosa més). Sense vocabulari FJE.
- **Amplitud d'avaluació**: 2-3 criteris accionables. Corresponen a les tasques concretes demandades.
- **Concretesa del descriptor**: Observable: "He escrit 3 passos numerats." Sense adjectius valoratius.
- **Perspectiva alumne-facing**: "He escrit ___ / He usat ___." Primera persona consistent en tota la rúbrica.
- **Naturalesa de l'excel·lència**: Descriptor AE = precisió o originalitat dins del límit: "He triat una paraula que no estava a la bastida però que explica exactament el que volia dir." No "he afegit coses" ni "ho he fet molt bé".

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Estructura de l'instrument**: Taula: 3-4 criteris × escala FJE completa (NA/AS/AN/AE). Primera escala gradada.
- **Amplitud d'avaluació**: 3-4 criteris del gènere o la tasca concreta.
- **Concretesa del descriptor**: Observable amb indicadors: "He escrit la idea principal a la 1a frase, sense 'Aquest text parla de…'."
- **Perspectiva alumne-facing**: "He escrit / He usat / He inclòs ___." Primera persona en tot el document.
- **Naturalesa de l'excel·lència**: Descriptor AE = qualitat que transforma: una imatge pròpia, un connector inesperat, un exemple original no donat a la bastida.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Estructura de l'instrument**: Taula: 4-5 criteris × escala FJE. Descriptor breu per a cada criteri i nivell.
- **Amplitud d'avaluació**: 4-5 criteris que cobreixen les HCL clau de la tasca (Argumentar, Descriure, Narrar...).
- **Concretesa del descriptor**: Apunta a la qualitat: "Cada argument inclou una evidència del text o una raó concreta."
- **Perspectiva alumne-facing**: "He argumentat / He justificat / He demostrat ___." HCL en primera persona.
- **Naturalesa de l'excel·lència**: Descriptor AE = habilitat que anticipa el nivell següent: un argument no donat per la bastida, una connexió pròpia entre dues idees del text.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Estructura de l'instrument**: Taula: 5-6 criteris × escala FJE + descriptor observatble per a cada criteri i nivell.
- **Amplitud d'avaluació**: 5-6 criteris que inclouen dimensió formal (llengua) i dimensió de contingut (idees).
- **Concretesa del descriptor**: Apunta a la relació: "He connectat les idees de seccions diferents usant connectors precisos."
- **Perspectiva alumne-facing**: "He analitzat / He contrastat / He elaborat ___." HCL acadèmiques en 1a persona.
- **Naturalesa de l'excel·lència**: Descriptor AE = evidència de pensament crític: detectar un biaix, contrastar fonts, plantejar una objecció fonamentada.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Estructura de l'instrument**: Taula: 5-6 criteris × escala FJE + reflexió metacognitiva final (1-2 frases lliures).
- **Amplitud d'avaluació**: 5-6 criteris amb criteri de reflexió metacognitiva ("He revisat el text i he millorat ___").
- **Concretesa del descriptor**: Metacognitiu: "He detectat i corregit al menys un error de coherència o un terme imprecís."
- **Perspectiva alumne-facing**: "He reflexionat / He avaluat / He detectat ___." Metacognició en 1a persona.
- **Naturalesa de l'excel·lència**: Descriptor AE = reflexió que demostra metacognició genuïna i transferència a altres contexts o tasques.

