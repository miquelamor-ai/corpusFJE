---
tipus: derivat
font_canonic: M3_instrument-escriure-divulgatiu.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-05-26'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 186b30cd25ef1119
---

# Escriure/adaptar un text divulgatiu — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un text divulgatiu per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Claredat i captació**: Títol clar i directe. Diu el tema sense metàfores.
- **Motivació i context**: 1 frase que anuncia el tema.
- **Causa-efecte i coherència**: 2-3 paràgrafs molt curts. Un fet explicat com a procés (no llista de fets).
- **Accessibilitat i context**: Xifres molt simples i arrodonides: "uns quants milers".
- **Credibilitat i font**: Sense cites (massa complex per a A1).
- **Accessibilitat i connexió**: 1 exemple per paràgraf, pres del context immediat de l'alumne.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Claredat i captació**: Títol informatiu i lleugerament captador. Sense metàfores obscures.
- **Motivació i context**: 2 frases: ganxo inicial (pregunta o dada) + anunci del tema.
- **Causa-efecte i coherència**: 3-4 paràgrafs narrativitzats. No llista de fets. Exemple per paràgraf.
- **Accessibilitat i context**: Xifres arrodonides i contextualitzades: "gairebé dos milions".
- **Credibilitat i font**: 1 cita màxim, atribució simple: "diu la científica X".
- **Accessibilitat i connexió**: 1 exemple concret i quotidià per paràgraf. Accessible per a l'alumne.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Claredat i captació**: Títol captador (pregunta o xifra sorprenent). Clar i directe.
- **Motivació i context**: Entradeta clara que crea expectativa sense revelar tot el contingut.
- **Causa-efecte i coherència**: 4-5 paràgrafs. El contingut s'explica com una historia (causa → efecte → implicació).
- **Accessibilitat i context**: Xifres arrodonides amb comparació: "més de dos milions, una xifra equivalent a...".
- **Credibilitat i font**: 1-2 cites breus. Atribució clara: "com explica la doctora X, investigadora de...".
- **Accessibilitat i connexió**: Exemples concrets i variats. Connectats al text, no digressius.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Claredat i captació**: Títol captador i precís. Pot tenir un subratllat temàtic.
- **Motivació i context**: Entradeta elaborada que contextualitza el fenomen i capta l'atenció.
- **Causa-efecte i coherència**: Narrativització elaborada. Cada paràgraf avança la comprensió del fenomen.
- **Accessibilitat i context**: Xifres precises amb font i comparació contextualitzada.
- **Credibilitat i font**: 2-3 cites ben atribuïdes. Contrast de perspectives si escau.
- **Accessibilitat i connexió**: Exemples concrets amb connexió explícita amb el concepte que il·lustren.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Claredat i captació**: Títol complex i suggeridor. Pot ser provocatiu però no obscur.
- **Motivació i context**: Entradeta sofisticada que situa el tema en un context ampli i crea intriga.
- **Causa-efecte i coherència**: Text narrativitzat complet. Pot incloure controvèrsies científiques presentades de forma accessible.
- **Accessibilitat i context**: Xifres amb anàlisi crítica de la seva significació estadística.
- **Credibilitat i font**: Múltiples fonts ben atribuïdes. Pot incloure controvèrsia científica sobre el fenomen.
- **Accessibilitat i connexió**: Exemples variats, alguns trets de contexts no quotidians.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


