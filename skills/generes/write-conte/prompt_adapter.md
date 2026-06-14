---
tipus: derivat
font_canonic: M3_genere-escriure-conte.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-14'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 1cb2bd96aedf78f7
---

# Escriure/adaptar un conte — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un conte per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Personatges i context**: Adult narra. L'alumne assenyala el personatge principal a la imatge.
- **Obstacle i causa**: Adult explica el problema. L'alumne escolta i assenyala la imatge del conflicte.
- **Ordre i causalitat**: 2-3 imatges amb una frase oral per imatge. L'adult transcriu si l'alumne dicta.
- **Punt de màxima tensió**: L'adult assenyala el moment de tensió. L'alumne el reconeix ("aquí és on tot va malament").
- **Coherència i tancament**: L'adult llegeix la resolució. L'alumne identifica si ha anat bé o malament.
- **Varietat i situació**: Cap escriptura d'emocions. L'adult pot preguntar oralment "Com es sent?"
- **Reflexió sobre el procés**: "He vist les imatges i he dit el que passa a cada una." (oral, mediat per l'adult)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Personatges i context**: 1 personatge + 1 lloc en 1-2 frases. Sense descripció de trets.
- **Obstacle i causa**: 1 problema en 1 frase. "El lleó té gana però no hi ha menjar."
- **Ordre i causalitat**: 2-3 frases de fets en ordre cronològic. Sense connectors causals obligatoris.
- **Punt de màxima tensió**: 1 frase sobre el moment decisiu. Visual i inequívoc.
- **Coherència i tancament**: 1 frase de resolució. Positiva o negativa, clara i inequívoca.
- **Varietat i situació**: 1 emoció nomenada en un moment clau. Vocabulari bàsic ("content", "trist", "tenia por").
- **Reflexió sobre el procés**: "He escrit qui és el personatge, on és i què li passa. He escrit el final."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Personatges i context**: 1-2 personatges amb un tret cadascun. Lloc en 1 frase de context.
- **Obstacle i causa**: Conflicte clar: el personatge vol X però hi ha un obstacle. Causa no obligatòria.
- **Ordre i causalitat**: 3-4 frases ordenades amb connectors temporals simples ("primer", "després", "llavors").
- **Punt de màxima tensió**: El moment de màxima tensió es pot identificar clarament al text.
- **Coherència i tancament**: Resolució en 1-2 frases. Coherent amb el conflicte plantejat.
- **Varietat i situació**: 1-2 emocions nomenades situades en moments clau del conte.
- **Reflexió sobre el procés**: "El meu conte té un problema i un final. He nomenat com se sent el personatge."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Personatges i context**: 1-2 personatges amb tret i desig inicial clars. Lloc amb ambient breu.
- **Obstacle i causa**: Conflicte amb causa explícita. L'obstacle és comprensible per al lector.
- **Ordre i causalitat**: 3-4 esdeveniments amb connectors variats (temporals + causals). Causa i efecte explícits.
- **Punt de màxima tensió**: Clímax marcat amb connector de contrast ("però", "de sobte"). Tensió nomenada.
- **Coherència i tancament**: Resolució que connecta causalment amb el conflicte (com s'ha resolt).
- **Varietat i situació**: 2-3 emocions variades situades en el moment de l'acció. Connexió causa-emoció explícita.
- **Reflexió sobre el procés**: "He escrit els 5 moments del conte en ordre. He explicat per què el personatge fa el que fa."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Personatges i context**: Personatges amb motivació explícita. Context temporal i espacial integrat al relat.
- **Obstacle i causa**: Conflicte amb dimensió emocional. La causa s'explicita i impacta el personatge.
- **Ordre i causalitat**: Seqüència de 4-5 actes amb causa-efecte i tensió creixent cap al clímax.
- **Punt de màxima tensió**: Clímax amb emoció nomenada del personatge + acció decisiva. Tensió crescuda gradualment.
- **Coherència i tancament**: Resolució amb reflex emocional del personatge. Final tancat amb matís moderat.
- **Varietat i situació**: Emocions integrades al text sense aparèixer llistades. Matisades i variades.
- **Reflexió sobre el procés**: "El meu conte té tensió creixent i resolució coherent. Les emocions estan integrades al text, no llistades."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Personatges i context**: Personatges complexos amb motivació i tensió interna. Context ric i funcional per a la trama.
- **Obstacle i causa**: Conflicte complex: pot incloure tensions morals, dilemes o contradicció interna del personatge.
- **Ordre i causalitat**: Seqüència causal elaborada. Cada acte prepara el clímax. Pot incloure paral·lelisme o recursivitat.
- **Punt de màxima tensió**: Clímax amb decisió moral, reversió o canvi de perspectiva. Pot incloure ironia si el context ho justifica.
- **Coherència i tancament**: Resolució oberta, irònica o ambigua si el context literari ho requereix. Ha de ser significativa.
- **Varietat i situació**: Emocions complexes o contradictòries. Descripció interior del personatge possible.
- **Reflexió sobre el procés**: "El meu conte té personatges complexos, clímax ben construït i resolució significativa. He revisat que la veu narrativa sigui consistent."

