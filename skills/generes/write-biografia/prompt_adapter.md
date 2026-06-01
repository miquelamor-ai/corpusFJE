---
tipus: derivat
font_canonic: M3_genere-escriure-biografia.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-01'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 15d0dad0b6e1da5e
---

# Escriure/adaptar una biografia — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una biografia per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Seqüència i coherència**: Fets ordenats en el temps, del més antic al més recent. Sense flashbacks.
- **Format i precisió**: Dates relatives: "fa molts anys", "quan era jove", "l'any passat dels seus besavis".
- **Situació espai-temps**: Context d'1 frase: "a Alemanya, fa molt de temps".
- **Nombre i rellevància**: 2-3 fets simples, un per frase. Ordenats cronològicament.
- **Varietat i precisió**: "Primer", "després", "al final".
- **Extensió i profunditat**: 1 frase: "Per això, aquesta persona és important."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Seqüència i coherència**: Fets ordenats cronològicament amb connectors temporals simples.
- **Format i precisió**: Dates completes o any exacte: "el 1879", "el 15 de març de 1879".
- **Situació espai-temps**: Context de 2 frases: país, època, context familiar breu.
- **Nombre i rellevància**: 3 fets principals, un per paràgraf o dues frases cadascun.
- **Varietat i precisió**: "L'any...", "quan tenia... anys", "més tard".
- **Extensió i profunditat**: 1-2 frases amb connector: "per això, avui... és recordada per..."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Seqüència i coherència**: Cronologia estricta respectada al llarg de tot el text.
- **Format i precisió**: Dates completes: "el 15 de març de 1879". Context temporal breu integrat.
- **Situació espai-temps**: Context breu però present: lloc + any + 1 frase sobre el context social.
- **Nombre i rellevància**: 3-4 fets seleccionats per rellevància per al llegat. Jerarquització implícita.
- **Varietat i precisió**: "En aquell moment", "com a conseqüència", "a partir d'aleshores".
- **Extensió i profunditat**: 2-3 frases. Distinció clara entre fets i llegat. Connector explicatiu ("la seva contribució és important perquè...").

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Seqüència i coherència**: Cronologia precisa amb relació causa-efecte entre fets.
- **Format i precisió**: Dates completes amb context historicogeogràfic integrat als paràgrafs.
- **Situació espai-temps**: Context historicogeogràfic integrat als paràgrafs de fets.
- **Nombre i rellevància**: 4-5 fets amb context causal. Selecció justificada implícitament per la seva relació amb el llegat.
- **Varietat i precisió**: Connectors causals i temporals variats i precisos.
- **Extensió i profunditat**: Llegat argumentat (3-4 frases). Connexió explícita entre el context de la figura i el context actual.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Seqüència i coherència**: Cronologia completa. Pot incloure una retrospectiva crítica del llegat al final.
- **Format i precisió**: Dates amb referència al context historiogràfic quan és rellevant per al llegat.
- **Situació espai-temps**: Context historiogràfic crític: la figura en relació amb el seu temps i amb el nostre.
- **Nombre i rellevància**: 5 fets amb perspectiva historiogràfica. Pot incloure reflexió sobre la selecció mateixa (quins fets es recorden i per qué).
- **Varietat i precisió**: Connectors elaborats amb matís cronològic o causal complex.
- **Extensió i profunditat**: Llegat crític (4-5 frases): pot incloure controvèrsies, revisions historiogràfiques o perspectives múltiples.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


