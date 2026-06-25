---
name: generate-pictogrames
description: 'Use when the teacher has activated the "pictogrames" complement. Inserts
  ARASAAC pictogram markers [PICTO: terme] in the adapted text (NOT Unicode emojis).
  The backend resolves each marker to a real ARASAAC pictogram image (CC BY-NC-SA
  4.0, Sergio Palao / CATEDU). At Emergent/pre-A1: inline beside each key noun and
  verb (1-2 per sentence) + lateral paratext for anticipation. At A1: 1 marker per
  sentence or technical term. At A2+: visual glossary only (markers in a side list,
  NOT inline in running text). Modulated strictly by MECR level.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: pictogrames
agent_role: adapter
tools_required: []
triggers:
- path: params.complements.pictogrames
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-pictogrames.md
font_version: 4.0.0-canonic
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: d75324856acbdc7b
---

# Generar pictogrames — skill operativa per a LLM

El complement de pictogrames afegeix suport visual al text adaptat per facilitar la descodificació i l'ancoratge conceptual. Opera en dos modes segons el perfil de l'alumne: **emoji Unicode** per a BICS general i **ARASAAC** per a TEA, CAA i vocabulari disciplinar de nouvinguts. La posicio canvia radicalment per nivell: a pre-A1/A1 el pictograma va **inline** com a anticipacio; a A2+ va al **glossari visual al peu**, mai inline.

**Tipologia MALL**: Mediacio (suport augmentatiu i alternatiu de comunicacio, AAC).
**HCL associada**: cap HCL productiva — el complement suporta la descodificacio lectora sense activar producció escrita autònoma.
**Principi rector**: el pictograma és una bastida de descodificacio a pre-A1/A1, i un glossari visual de referencia a A2+. La mateixa forma serveix funcions completament diferentes.

**Dos modes — quan usar cadascun:**

| Mode | Format | Quan activar |
|---|---|---|
| **Emoji Unicode** | ☀️ 💧 🌱 (inline o glossari) | BICS general: conceptes quotidians, nouvingut A1+ sense vocabulari disciplinar, alumnat general |
| **ARASAAC** | `[PICTO: ecosistema\|ecosistema]` | TEA (sempre), CAA, nouvingut + text disciplinar (CALP), pre-A1 amb vocabulari escolar |

**Per que ARASAAC és superior per a TEA i nouvingut+disciplinar:**
- **TEA**: ARASAAC és l'estandard CAA internacional; els pictogrames son coherents, accessibles i reconeguts pels professionals de suport.
- **Nouvingut + disciplinar**: els emojis no cobreixen "ecosistema", "parlament", "evaporacio" o "fraccio". ARASAAC te ~30.000 pictogrames escolars. El terme castellà en el marcador (`[PICTO: ecosistema|ecosistema]`) actua com a pont TOLC per a nouvinguts hispanofons.
- **General**: emoji suficient per a conceptes que ja tenen representacio visual clara i universal.

**Format dels marcadors ARASAAC:**
```
[PICTO: terme_catala|terme_castella]
```
- El terme catala apareix com a etiqueta visible per a l'alumne.
- El terme castella va a la cerca ARASAAC (cobertura molt superior).
- Compatible amb format antic sense `|` (s'usa el terme únic per a la cerca).
- Format emoji: emoji directament inline o al glossari.

**Connexions MALL transversals:**
- *Descodificacio visual com a competencia lectora emergent*: a pre-A1, el pictograma és el text per a lectors logografics o amb alfabet diferent. El pictograma i la paraula van junts perque l'alumne associa forma visual amb so i significat.
- *Paratext d'anticipacio com a activacio de coneixement previ*: mostrar el vocabulari visual ABANS de llegir activa els coneixements previs i redueix la carrega cognitiva. Principi "context before text".
- *Glossari visual A2+ com a referencia, no bastida*: a A2+, l'alumne ja pot llegir en flux continu. El glossari al peu és un recurs de consulta, com un diccionari visual. Mantenir-lo inline a A2+ introduiria soroll visual.
- *TOLC via castella (ARASAAC)*: el terme castella al marcador `[PICTO: cat|cast]` actua com a pont interlinguistic per a nouvinguts hispanofons. La imatge ARASAAC ancora el concepte catala via una llengua parcialment accessible.

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **complement de pictogrames generat per al text adaptat**. **No descriu la produccio autonoma de l'alumne**: el complement es genera i el docent/alumne l'usa per llegir. El registre d'us és del docent (observacio de si l'alumne usa el suport visual).

**Modulacio per perfil (Decisio 1 Fase B):**
- **TEA**: mode ARASAAC sempre, densitat alta (pre-A1/A1), paratext d'anticipacio obligatori.
- **Nouvingut pre-A1/A1 + text BICS**: mode emoji, inline, vocabulari quotidia.
- **Nouvingut + text disciplinar (CALP)**: mode ARASAAC, terme castella al marcador.
- **General (sense condicio especifica)**: emoji si cal, glossari visual al peu (A2+).
- **AACC**: cap pictograma o glossari minimal — el suport visual pot distreure si l'alumne ja te fluencia lectora alta.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Mode pictograma**
- Emoji vs ARASAAC: ARASAAC si TEA/CAA; emoji si nouvingut BICS. Sempre inline com a anticipacio.

**2. Posicio al text**
- Inline vs glossari: Inline DAVANT de la paraula: l'alumne veu el pictograma PRIMER, llavors llegeix la paraula.

**3. Densitat**
- Nombre per text: 8-10 pictogrames maxim per text (maxim 1-2 per frase inline). Alta densitat justificada.

**4. Especificitat del concepte**
- Concret vs disciplinar: Conceptes molt concrets i universals (mode emoji) o conceptes escolars basics (mode ARASAAC).

**5. Paratext d'anticipacio**
- Pre-lectura visual: Obligatori: vocabulari visual ABANS del text. Docent presenta els pictogrames oralment. Format: `### Vocabulari del text (mira primer!)` + llista pictograma·paraula.

**6. Criteris transversals**
- Coherencia i qualitat: Mateix pictograma per al mateix concepte en tot el document. Cap pictograma decoratiu. Cap emoji de flags o gestos ambigus.

**7. Autoavaluacio mediada**
- Metacognicao: Docent observa: "L'alumne ha vist els pictogrames i ha dit el nom de cada concepte." (oral, mediat)

### A1 — Inicial


**1. Mode pictograma**
- Emoji vs ARASAAC: ARASAAC si TEA o text disciplinar; emoji si vocabulari quotidia. Inline discret.

**2. Posicio al text**
- Inline vs glossari: Inline discret davant o al costat del terme clau. 1 pictograma per paraula nova.

**3. Densitat**
- Nombre per text: 4-6 pictogrames. 1 per paraula nova o concepte clau.

**4. Especificitat del concepte**
- Concret vs disciplinar: Conceptes concrets: objectes, essers vius, accions fisiques observables.

**5. Paratext d'anticipacio**
- Pre-lectura visual: Recomanat: presentar el vocabulari visual abans de llegir.

**6. Criteris transversals**
- Coherencia i qualitat: Idem. Coherencia entre seccions.

**7. Autoavaluacio mediada**
- Metacognicao: "He usat els pictogrames per entendre les paraules difícils."

### A2 — Funcional


**1. Mode pictograma**
- Emoji vs ARASAAC: ARASAAC per termes disciplinars (TEA o nouvingut+CALP); emoji si BICS. Al glossari visual, mai inline.

**2. Posicio al text**
- Inline vs glossari: Glossari visual al peu (mai inline). Llista de termes + pictograma + definicio breu.

**3. Densitat**
- Nombre per text: 3-5 al glossari visual. 1 per terme disciplinar.

**4. Especificitat del concepte**
- Concret vs disciplinar: Termes disciplinars: "volca", "cel·lula", "parlament" (si te representacio visual).

**5. Paratext d'anticipacio**
- Pre-lectura visual: No cal. El glossari visual al peu és consultat durant la lectura.

**6. Criteris transversals**
- Coherencia i qualitat: Idem. El glossari visual no substitueix el glossari textual.

**7. Autoavaluacio mediada**
- Metacognicao: "He usat el glossari visual al peu per recordar el significat dels termes."

### B1 — Estratègic


**1. Mode pictograma**
- Emoji vs ARASAAC: ARASAAC per termes disciplinars especifics de la materia. Al glossari visual.

**2. Posicio al text**
- Inline vs glossari: Glossari visual al peu. Reservat per a termes disciplinars no familiars.

**3. Densitat**
- Nombre per text: 2-4 al glossari visual. Termes disciplinars de la materia.

**4. Especificitat del concepte**
- Concret vs disciplinar: Termes disciplinars especifics de la materia sense equivalent quotidia.

**5. Paratext d'anticipacio**
- Pre-lectura visual: No cal.

**6. Criteris transversals**
- Coherencia i qualitat: Idem. Si un terme no te representacio visual clara, millor no posar-ne.

**7. Autoavaluacio mediada**
- Metacognicao: "He identificat quins termes necessitaven un pictograma de referencia."

### B2 — Acadèmic


**1. Mode pictograma**
- Emoji vs ARASAAC: ARASAAC o emoji per termes molt tecnics sense equivalent quotidià. Glossari visual.

**2. Posicio al text**
- Inline vs glossari: Glossari visual al peu. Maxim 3-4 termes realment necessaris.

**3. Densitat**
- Nombre per text: 1-3 al glossari visual. Termes molt especialitzats.

**4. Especificitat del concepte**
- Concret vs disciplinar: Termes tecnics que beneficien d'ancoratge visual.

**5. Paratext d'anticipacio**
- Pre-lectura visual: No cal.

**6. Criteris transversals**
- Coherencia i qualitat: Idem. Densitat minima: nomes els termes que realment aporten.

**7. Autoavaluacio mediada**
- Metacognicao: Idem.

### C1+ — Crític


**1. Mode pictograma**
- Emoji vs ARASAAC: Rarament. Nomes si hi ha termes molt especialitzats sense representacio coneguda.

**2. Posicio al text**
- Inline vs glossari: Glossari visual minimal o absent.

**3. Densitat**
- Nombre per text: 0-2. Rarament necessari.

**4. Especificitat del concepte**
- Concret vs disciplinar: Termes molt especialitzats sense representacio quotidiana accessible.

**5. Paratext d'anticipacio**
- Pre-lectura visual: No cal.

**6. Criteris transversals**
- Coherencia i qualitat: Idem.

