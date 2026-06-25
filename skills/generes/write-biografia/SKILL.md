---
name: write-biografia
description: 'Use when adapting or generating a biografia for students. Activates
  when genre_discursiu == "biografia". Applies strict chronological order, 3-5 key
  facts, complete dates, and separation of facts and legacy. Output: biografia in
  markdown from birth to death/legacy.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: biografia
tipologia: Narrativa
mecr_range:
- A1
- A2
- B1
- B2
- C1
agent_role: adapter
tools_required: []
triggers:
- path: params.genere_discursiu
  equals: biografia
moduls_relacionats:
- M3
macro_tipologia: narrativa
label_ca: Biografia
font_canonic: M3_genere-escriure-biografia.md
font_version: 4.0.0-canonic
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: bc3e5957c80751e0
---

# Escriure/adaptar una biografia — skill operativa per a LLM

La biografia és una narració cronològica de la vida d'una persona real, centrada en els fets més rellevants per entendre el seu llegat. El seu tret definitori és l'**ordre cronològic estricte** i la **separació neta entre fets i llegat**: primer es narra el que va fer, i al final s'explica per què importa.

**Tipologia MALL**: Narrativa (narrar fets reals en el temps).
**HCL principal**: Narrar — seqüenciar fets biogràfics reals en ordre cronològic.
**HCL secundàries**: Descriure context i entorn (A2+) · Explicar causes del llegat i connexió amb el present (B1+) · Argumentar des d'una perspectiva historiogràfica (C1+).
**No s'adapta a pre-A1**: la biografia requereix el temps com a categoria abstracta (cronologia, context historicogeogràfic, llegat diferit — "per què importa avui"). Cap d'aquests conceptes es pot construir per via visual i concreta sense base lingüística mínima. A diferència del conte, no hi ha mediació adulta que substitueixi la comprensió temporal abstracta. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Narrar en el temps*: la biografia és el gènere canònic per treballar la cronologia. Els connectors temporals (primer, llavors, l'any..., quan tenia... anys, finalment) són el vocabulari estructural del gènere i la bastida principal de la comprensió.
- *Context com a ancoratge*: sense "a Alemanya, fa 150 anys", l'alumne no pot situar la figura ni construir significat. El context breu però present és imprescindible per a la comprensió, especialment per a alumnat nouvingut.
- *Llegat com a transició HCL Narrar → Explicar*: a B1+, el llegat no és una descripció ("és famosa per...") sinó una explicació ("la seva contribució és important perquè..."). Marca el pas de contar fets a explicar causes i conseqüències.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **biografia adaptada per a la LECTURA** de l'alumne (el que el docent presenta perquè l'alumne llegeixi). **No descriu la producció autònoma de l'alumne** — la producció biogràfica de l'alumne s'avalua amb un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast i en produeix els seus textos.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logografic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Ordre cronològic**
- Seqüència i coherència: Fets ordenats en el temps, del més antic al més recent. Sense flashbacks.

**2. Dates**
- Format i precisió: Dates relatives: "fa molts anys", "quan era jove", "l'any passat dels seus besavis".

**3. Context (lloc i època)**
- Situació espai-temps: Context d'1 frase: "a Alemanya, fa molt de temps".

**4. Selecció de fets principals**
- Nombre i rellevància: 2-3 fets simples, un per frase. Ordenats cronològicament.

**5. Connectors temporals**
- Varietat i precisió: "Primer", "després", "al final".

**6. Llegat**
- Extensió i profunditat: 1 frase: "Per això, aquesta persona és important."

**7. Criteris transversals**
- Especulació: Cap especulació sobre motivacions íntimes ("potser pensava que...", "probablement sentia..."). Només fets verificables.
- Numeració: Sense números romans per a segles. Usar "al segle XX" o "fa cent anys".
- Fidelitat al text font: Fidelitat als fets nuclears: qui és la persona, quins fets principals, quin llegat.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit qui és la persona, 2 coses que va fer i per qué és important."

### A1 — Inicial


**1. Ordre cronològic**
- Seqüència i coherència: Fets ordenats cronològicament amb connectors temporals simples.

**2. Dates**
- Format i precisió: Dates completes o any exacte: "el 1879", "el 15 de març de 1879".

**3. Context (lloc i època)**
- Situació espai-temps: Context de 2 frases: país, època, context familiar breu.

**4. Selecció de fets principals**
- Nombre i rellevància: 3 fets principals, un per paràgraf o dues frases cadascun.

**5. Connectors temporals**
- Varietat i precisió: "L'any...", "quan tenia... anys", "més tard".

**6. Llegat**
- Extensió i profunditat: 1-2 frases amb connector: "per això, avui... és recordada per..."

**7. Criteris transversals**
- Especulació: Idem.
- Numeració: Idem. Dates en xifres aràbigues.
- Fidelitat al text font: Fidelitat als fets i al llegat essencial.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He explicat la seva vida en ordre cronològic i he inclòs dates."

### A2 — Funcional


**1. Ordre cronològic**
- Seqüència i coherència: Cronologia estricta respectada al llarg de tot el text.

**2. Dates**
- Format i precisió: Dates completes: "el 15 de març de 1879". Context temporal breu integrat.

**3. Context (lloc i època)**
- Situació espai-temps: Context breu però present: lloc + any + 1 frase sobre el context social.

**4. Selecció de fets principals**
- Nombre i rellevància: 3-4 fets seleccionats per rellevància per al llegat. Jerarquització implícita.

**5. Connectors temporals**
- Varietat i precisió: "En aquell moment", "com a conseqüència", "a partir d'aleshores".

**6. Llegat**
- Extensió i profunditat: 2-3 frases. Distinció clara entre fets i llegat. Connector explicatiu ("la seva contribució és important perquè...").

**7. Criteris transversals**
- Especulació: Idem. Les motivacions s'expliciten per fonts (cites documentades), no per inferència.
- Numeració: Idem.
- Fidelitat al text font: Fidelitat als fets, al llegat i al to factual del text original.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He inclòs 3-4 fets principals amb context. He separat els fets del llegat."

### B1 — Estratègic


**1. Ordre cronològic**
- Seqüència i coherència: Cronologia precisa amb relació causa-efecte entre fets.

**2. Dates**
- Format i precisió: Dates completes amb context historicogeogràfic integrat als paràgrafs.

**3. Context (lloc i època)**
- Situació espai-temps: Context historicogeogràfic integrat als paràgrafs de fets.

**4. Selecció de fets principals**
- Nombre i rellevància: 4-5 fets amb context causal. Selecció justificada implícitament per la seva relació amb el llegat.

**5. Connectors temporals**
- Varietat i precisió: Connectors causals i temporals variats i precisos.

**6. Llegat**
- Extensió i profunditat: Llegat argumentat (3-4 frases). Connexió explícita entre el context de la figura i el context actual.

**7. Criteris transversals**
- Especulació: Idem.
- Numeració: Idem.
- Fidelitat al text font: Fidelitat als fets, al llegat, al context historiogràfic i al to.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He argumentat el llegat amb referència al context actual. He revisat que tots els fets estiguin ordenats cronològicament."

### B2 — Acadèmic


**1. Ordre cronològic**
- Seqüència i coherència: Cronologia completa. Pot incloure una retrospectiva crítica del llegat al final.

**2. Dates**
- Format i precisió: Dates amb referència al context historiogràfic quan és rellevant per al llegat.

**3. Context (lloc i època)**
- Situació espai-temps: Context historiogràfic crític: la figura en relació amb el seu temps i amb el nostre.

**4. Selecció de fets principals**
- Nombre i rellevància: 5 fets amb perspectiva historiogràfica. Pot incloure reflexió sobre la selecció mateixa (quins fets es recorden i per qué).

**5. Connectors temporals**
- Varietat i precisió: Connectors elaborats amb matís cronològic o causal complex.

**6. Llegat**
- Extensió i profunditat: Llegat crític (4-5 frases): pot incloure controvèrsies, revisions historiogràfiques o perspectives múltiples.

**7. Criteris transversals**
- Especulació: La inferència historiogràfica és admissible si s'explicita ("Segons els historiadors...", "Els indicis suggereixen que..."). L'especulació íntima sense evidència segueix prohibida.
- Numeració: Números romans admissibles si el text font els conté i el context historiogràfic ho requereix.
- Fidelitat al text font: Fidelitat a la complexitat crítica del text original, incloent matisos i controvèrsies.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He presentat la figura amb perspectiva crítica i he contextualitzat el llegat en el debat historiogràfic. He revisat que no hi hagi especulació sense evidència."

### C1+ — Crític


