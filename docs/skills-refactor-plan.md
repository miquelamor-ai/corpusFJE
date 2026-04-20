# Pla de refactor: corpusFJE com a biblioteca d'Agent Skills

**Data**: 2026-04-20
**Autor**: Miquel Amor + Claude (anàlisi)
**Estat**: Proposta (Fase E del pla de sincronització)
**Prerequisits**: Fase D completa (ATNE llegeix de corpusFJE)

---

## 1. Resum executiu

Proposem refactoritzar el contingut operatiu del corpusFJE per complir l'**estàndard obert Agent Skills** ([agentskills.io](https://agentskills.io)), adoptat per Claude Code, OpenAI Codex i altres plataformes. Això convertiria corpusFJE d'una biblioteca de documents markdown a una **biblioteca de capacitats executables** que qualsevol agent LLM pugui activar sota demanda.

**Benefici clau**: reduir tokens al prompt, compartir la mateixa biblioteca entre els 5 assistents FJE planificats, i guanyar interoperabilitat amb qualsevol stack d'IA futur.

**Cost estimat**: mitjà. No requereix regenerar contingut; bàsicament reestructurar fitxers i actualitzar `corpus_reader.py` d'ATNE.

---

## 2. Context: què són les Agent Skills

### Definició
Un **Agent Skill** és un directori amb un `SKILL.md` al seu interior que conté:

- **Frontmatter YAML** amb dos camps obligatoris:
  - `name`: identificador únic de la skill
  - `description`: condició de disparador — explica a l'agent *quan* usar aquesta skill
- **Cos markdown**: instruccions, passos, exemples que l'agent necessita per executar la tasca
- **Carpetes opcionals**:
  - `scripts/`: executables (Python, JS, bash) que l'agent pot invocar
  - `references/`: documentació addicional carregada sota demanda
  - `assets/`: recursos estàtics (templates, dades, imatges)

### Progressive disclosure (càrrega en tres nivells)
Per evitar saturar el context window quan hi ha centenars de skills disponibles:

| Nivell | Quan es carrega | Què es carrega |
|---|---|---|
| **Tier 1** | A l'startup de l'agent | Només `name` + `description` de cada skill (pocs tokens, una mena de "taula de contingut") |
| **Tier 2** | Quan una petició de l'usuari encaixa amb la `description` | El cos sencer del `SKILL.md` d'aquella skill |
| **Tier 3** | Quan l'execució de la skill necessita recursos específics | Scripts, references, o assets concrets |

### Tipus de coneixement que aporta
Segons la classificació cognitiva (Anderson, Squire):

| Tipus de memòria | Exemple humà | Equivalent en agents |
|---|---|---|
| Semàntica (fets) | "Roma és la capital d'Itàlia" | RAG, knowledge bases |
| Episòdica (experiències) | "Vaig anar a Roma l'estiu passat" | Logs conversacionals, historial |
| **Procedimental (habilitats)** | **"Com conduir una moto a Roma"** | **Agent Skills** |

Les skills omplen un buit que **ni RAG, ni MCP, ni fine-tuning** cobreixen: el coneixement procedimental — *com* fer les coses, en quin ordre, amb quin criteri.

### Comparació amb altres mecanismes

| Mecanisme | Què aporta | Què NO aporta |
|---|---|---|
| **MCP (Model Context Protocol)** | Accés a eines/APIs externes | No diu quan usar-les ni com interpretar el resultat |
| **RAG** | Coneixement factual sota demanda | No ensenya a fer res |
| **Fine-tuning** | Coneixement permanent al model | Car, s'ha de repetir amb cada nova versió del model |
| **Agent Skills** | Procediments, heurístiques, workflows | No substitueix les anteriors — es combina amb elles |

Sovint una skill **usa** MCP (per invocar eines), RAG (per consultar fets) i té scripts deterministes — la skill aporta el *judici* sobre quan i com.

---

## 3. Per què encaixa amb corpusFJE

El corpusFJE actual ja té moltes característiques d'una biblioteca de skills. La sincronització de la Fase C (2026-04-20) ha reforçat aquesta estructura amb la secció 6 "INSTRUCCIONS PER A L'LLM" a cada perfil.

### Correspondència estructural

| Component d'una Skill | Equivalent actual al corpusFJE | Estat |
|---|---|---|
| `name` | `titol` al frontmatter + nom de fitxer | ✓ Ja hi és |
| `description` (quan activar) | `descripcio` al frontmatter + "Barrera nuclear" de secció 6 | ⚠ Cal adaptar format |
| Cos markdown | Secció 6 (INSTRUCCIONS PER A L'LLM) + Mapa barrera→instruccions | ✓ Ja hi és, només cal extreure-ho |
| `references/` | Seccions 1-4 (CONTINGUT, CONNEXIONS, DETECCIÓ, HEURÍSTIQUES) + 5 (FONTS) | ✓ Es pot migrar sense edició |
| `assets/` | Exemples ABANS→DESPRÉS, glossaris bilingües | ✓ Ja hi són, només cal separar |
| `scripts/` | (Sense equivalent actual) | ✗ Nou; opcional |

### Què ja funciona com un proto-skill system

- **`corpus_reader.py` d'ATNE**: ja fa una mena de "skill loading" manual extraient blocs per clau (secció `## <key>`). És progressive disclosure manual.
- **Frontmatter amb variables_configurables**: equivalents funcionals a paràmetres d'entrada d'una skill.
- **Mapa barrera→instruccions (H-04, A-01, etc.)**: un registre taxonòmic d'instruccions atomicitzades — es podria evolucionar a sub-skills compostables.

### Què falta per ser compliant amb agentskills.io

1. Format frontmatter estandarditzat (`name`, `description` com a camps obligatoris i primers).
2. Estructura de directori (una carpeta per skill, amb `SKILL.md` al seu interior).
3. Separació entre procediment (cos skill) i coneixement de suport (references).
4. Registre central de skills disponibles (index o manifest).

---

## 4. Proposta d'arquitectura per al corpusFJE refactoritzat

### Opció A — Full refactor (skills puros)

```
corpusFJE/
├── skills/
│   ├── adapt-for-tdah/
│   │   ├── SKILL.md                     # name, description, body (secció 6 actual)
│   │   ├── references/
│   │   │   └── perfil-complet.md        # seccions 1-4 (contingut conceptual)
│   │   │   └── fonts.md                  # secció 5 (bibliografia)
│   │   └── assets/
│   │       └── exemple-abans-despres-A2.md
│   ├── adapt-for-tea/
│   │   └── ...
│   ├── adapt-for-nouvingut/
│   │   └── ...
│   └── ... (una carpeta per perfil, ~16 perfils M1 + DUA, LF, gèneres, etc.)
├── framework/
│   ├── marc-general-ia.md               # marc transversal (ja existeix)
│   └── lectura-facil-comunicacio-clara.md  # no és un perfil; és metodologia comuna
└── docs/
    └── ...
```

**Avantatges**:
- 100% compliant amb agentskills.io
- Progressive disclosure natiu
- Interoperabilitat amb Claude Code, OpenAI Codex, etc.

**Inconvenients**:
- Ruptura amb l'estructura actual (arxius plans a l'arrel)
- ATNE necessita refactor gran de `corpus_reader.py`
- Docents i responsables pedagògics poden perdre la vista unificada (1 fitxer = 1 perfil)

### Opció B — Refactor híbrid (compatible i mínim risc)

Mantenir els md actuals a l'arrel + afegir una capa de skills que referencia als md existents:

```
corpusFJE/
├── M1_alumnat-TEA.md                    # (intacte, com està ara)
├── M1_TDAH.md                           # (intacte)
├── ...
├── skills/                              # NOVA capa
│   ├── index.json                       # registre central: [{name, description, source_md, source_section}]
│   ├── adapt-for-tdah/
│   │   └── SKILL.md                     # extret de M1_TDAH.md línies X-Y (secció 6)
│   └── ...
└── docs/
```

El `SKILL.md` inclou al seu body un `@include` o referència al md original. El sistema de build regenera els `SKILL.md` automàticament quan canvien els md font.

**Avantatges**:
- Els md actuals no es toquen (compatibilitat total amb ús humà)
- La capa skills es regenera automàticament
- ATNE pot llegir de qualsevol de les dues capes

**Inconvenients**:
- Duplicació de contingut (gestionable amb build scripts)
- Dues fonts de veritat tècniques — hi ha el risc que divergeixin si el build script falla

### Opció C — Refactor lleuger (sense skills físics, només compliance del format)

Afegir als md actuals la dimensió "skill-ready" sense reestructurar:

```
corpusFJE/M1_TDAH.md:
---
modul: M1
titol: "Alumnat amb TDAH"
# --- NOUS CAMPS PER COMPATIBILITAT SKILLS ---
skill_name: adapt-for-tdah
skill_description: "Use when adapting text for a student with TDAH (baixa atenció sostinguda, memòria de treball limitada, cal micro-blocs i indicadors de progrés)"
skill_body_section: "## 6. INSTRUCCIONS D'ADAPTACIÓ TEXTUAL PER A L'LLM"
# ---
...
```

Un script extractor `build_skills.py` al repo genera la biblioteca `/skills/` automàticament a partir d'aquests metadades.

**Avantatges**:
- Canvi mínim als md existents
- Progressive disclosure es pot implementar a `corpus_reader.py` sense canvis estructurals
- Fàcil revertir si no convenç

**Inconvenients**:
- No és 100% compliant amb agentskills.io de manera natural
- Requereix eina d'extracció

### Recomanació

**Opció C com a primer pas, amb migració gradual a Opció B**. Raonament:
- Minimitza risc immediat
- Permet aprendre abans de comprometre's a l'arquitectura final
- L'extracció automàtica ens dóna la biblioteca skills sense perdre els md actuals
- Un cop els altres assistents FJE comencin a consumir la biblioteca, podem avaluar si cal passar a Opció B (capa física) o A (full refactor).

---

## 5. Exemple concret: M1_TDAH com a skill

### Abans (format actual)

Fitxer únic `M1_TDAH.md` amb 6 seccions: 1-CONTINGUT, 2-CONNEXIONS, 3-DETECCIÓ, 4-HEURÍSTIQUES, 6-INSTRUCCIONS PER A L'LLM, 5-FONTS. Total ~240 línies. Cada vegada que ATNE adapta un text per a un alumne amb TDAH, injecta tot o bona part del md al prompt.

### Després (Opció A, full skill)

**`corpusFJE/skills/adapt-for-tdah/SKILL.md`**:
```markdown
---
name: adapt-for-tdah
description: Use when adapting educational text for a student with TDAH. Activates when the student profile includes "TDAH" or "atenció sostinguda baixa" or "memòria de treball limitada". Input requirements: original text, MECR level, DUA level. Output: text adapted with micro-blocks, progress indicators, and visual signaling.
author: FJE — Fundació Jesuïtes Educació
version: 1.0.0
---

# Adapt text for TDAH profile

## When to use this skill
Activate this skill when the user requests text adaptation for a student whose profile includes TDAH (Trastorn per Dèficit d'Atenció i Hiperactivitat). Signals: baixa atenció sostinguda, memòria de treball limitada, necessitat de variació i retroalimentació constant.

## Core barrier
Atenció sostinguda limitada. La memòria de treball compromesa dificulta retenir informació entre frases llargues o paràgrafs densos.

## Adaptation rules

```
PERFIL: TDAH
- Micro-blocs de 3-5 frases amb objectiu explícit per bloc
- Senyalització visual intensa: negretes, requadres, icones
- Variació: alternar lectura, esquema, pregunta
- Indicadors de progrés: [Secció X de Y]
```

## Priority map

| Priority | Instructions activated | Rationale |
|---|---|---|
| 1 (attention) | H-04, B-13, H-06 | Core barrier |
| 2 (working memory) | C-04, C-01, B-01 | Memory limitation |
| 3 (motivation) | H-05, F-06 | Feedback for engagement |

## Before → after example
See `assets/example-A2-digestive-system.md` for a full before/after transformation.

## Loading deeper context
If the agent needs pedagogical background (neuroscience, comorbidities, DUA framework connections), load `references/perfil-complet.md`.
```

**`corpusFJE/skills/adapt-for-tdah/references/perfil-complet.md`**: seccions 1-4 actuals (CONTINGUT ESPECÍFIC, CONNEXIONS, DETECCIÓ, HEURÍSTIQUES).

**`corpusFJE/skills/adapt-for-tdah/references/fonts.md`**: secció 5 actual.

**`corpusFJE/skills/adapt-for-tdah/assets/example-A2-digestive-system.md`**: l'exemple ABANS→DESPRÉS actual.

### Progressive disclosure en acció (exemple flux ATNE)

1. **Startup d'ATNE**: carrega l'índex amb `name` + `description` de cada skill (~16 perfils × ~50 tokens = ~800 tokens). Negligible.
2. **Usuari demana**: "Adapta aquest text per un alumne de 2n ESO amb TDAH, nivell B1 català."
3. **Gemini/Claude analitza la petició** i, mirant les descriptions, identifica que `adapt-for-tdah` encaixa.
4. **Tier 2 loading**: es carrega el cos del SKILL.md (~60 línies, ~1500 tokens). Només aquestes skills rellevants es carreguen, no tota la biblioteca.
5. **Execució**: l'agent aplica les regles de la skill al text d'entrada.
6. **Tier 3 (opcional)**: si l'usuari pregunta pel fonament pedagògic, es carrega `references/perfil-complet.md`. Si no, estalvi de tokens.

**Estalvi estimat** (per adaptació típica): de ~6000 tokens actuals (md sencer injectat) a ~2000 tokens (només la skill rellevant). **~65% de reducció**.

---

## 6. Mapping complet: estructura actual → estructura skills

Per a cada fitxer M*_*.md del corpusFJE, la transformació seria:

| Secció actual | Destinació skill |
|---|---|
| Frontmatter YAML | Frontmatter del SKILL.md (adaptant camps) |
| `## 1. CONTINGUT ESPECÍFIC` | `references/perfil-complet.md` (Tier 3) |
| `## 2. CONNEXIONS AMB ALTRES DOCUMENTS` | `references/connexions.md` (Tier 3) |
| `## 3. DETECCIÓ (Variables de Context)` | **Cos del SKILL.md** — és trigger detection (Tier 2) |
| `## 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT` | **Cos del SKILL.md** (Tier 2) |
| `## 5. FONTS DEL CORPUS` | `references/fonts.md` (Tier 3) |
| `## 6. INSTRUCCIONS PER A L'LLM` | **Cos del SKILL.md** (Tier 2 — nucli procedimental) |
| Exemples ABANS→DESPRÉS | `assets/*.md` (Tier 3) |
| Glossaris bilingües | `assets/glossaris/*.md` (Tier 3) |

---

## 7. Pla de migració (fases dins de la Fase E)

### E.1 — Anàlisi i decisió d'arquitectura (1-2 setmanes)
- [ ] Avaluar suport d'Agent Skills a Gemini (ATNE actual). Si no hi ha, decidir si refactoritzar ATNE perquè detecti i carregui skills manualment.
- [ ] Decidir entre Opció A, B, C (vegeu secció 4).
- [ ] Validar compliance amb l'spec oficial a [agentskills.io](https://agentskills.io).
- [ ] Documentar l'arquitectura triada al repo.

### E.2 — Prototip amb un sol perfil (1 setmana)
- [ ] Escollir un perfil senzill com a pilot (p.ex. M1_TDAH).
- [ ] Refactoritzar com a skill seguint l'arquitectura triada.
- [ ] Adaptar ATNE perquè consumeixi aquest skill en comptes del md original.
- [ ] Comparar: tokens consumits abans vs després, qualitat de sortida, facilitat de manteniment.

### E.3 — Migració massiva (2-3 setmanes)
- [ ] Migrar tots els perfils M1_* (15 skills).
- [ ] Migrar M2_DUA-principis-pautes com a "framework skill" (diferents nivells).
- [ ] Migrar M3_lectura-facil-comunicacio-clara (cas complex: ja té 4 seccions operatives).
- [ ] Migrar M3_generes-discursius i M3_generes-22 com a skills de gènere.
- [ ] Migrar M5_* (tecnopedagogia) com a skills de rol d'agent.
- [ ] Mantenir marc-general-ia-esborrany.md com a document transversal (no és una skill).

### E.4 — Integració als altres assistents FJE (ongoing)
- [ ] Documentar l'API de càrrega de skills perquè els altres 4 assistents FJE planificats la consumeixin.
- [ ] Exemple: l'assistent de recomanació de materials hauria de poder carregar `adapt-for-tdah` quan un docent busqui materials per un alumne TDAH.

### E.5 — Publicació (opcional)
- [ ] Avaluar si publicar la biblioteca com a project open-source compliant amb agentskills.io.
- [ ] Llicència: probablement CC BY-SA per al contingut pedagògic.

---

## 8. Consideracions tècniques

### 8.1 — Compatibilitat amb Gemini
ATNE actualment usa Gemini 2.5-flash (segons [project_atne.md](../../.claude/.../memory/project_atne.md)). El suport natiu d'Agent Skills és ecosistema-dependent:

| Plataforma | Suport natiu |
|---|---|
| Claude Code / Claude API | ✓ Natiu (skills són format d'Anthropic) |
| OpenAI Codex / GPT | ✓ Adoptat |
| Gemini | ⚠ No natiu; requereix implementació manual |

**Implicació per ATNE**: cal un "skill runtime" a la capa Python (evolució de `corpus_reader.py`) que:
1. Llegeix l'índex de skills al startup.
2. Selecciona skills rellevants (pot ser via regex simple sobre el perfil de l'alumne, o via crida prèvia a Gemini per raonament).
3. Injecta el cos de la skill seleccionada al prompt principal.
4. Carrega references/assets sota demanda si el prompt ho indica.

Aquesta capa és ~100-200 línies de Python addicionals. No és un bloqueig; de fet, és similar al que `corpus_reader.py` ja fa.

### 8.2 — Versionat
agentskills.io recomana versionar skills amb semver. Proposta:
- Major: canvi de l'estructura del skill o del seu `name`.
- Minor: canvi de contingut significatiu (noves regles, canvi de prioritats).
- Patch: correccions ortogràfiques, ajustos d'exemples.

Cada skill tindria el seu propi `version` al frontmatter. Un canvi major invalida càrregues cachejades.

### 8.3 — Compatibilitat retroactiva
Durant la transició (Opció B o C), els md actuals han de seguir funcionant per ATNE i qualsevol consumidor existent. El build script regenera la capa skills; si falla, els md són la font.

### 8.4 — Governança
Qui pot afegir/modificar skills?
- Proposta: PRs al repo corpusFJE requereixen review per part del responsable pedagògic (Miquel) i, si cal, validació tècnica per part del responsable d'ATNE/assistents.
- Skills "estables" (v1.x): canvis només per bug fixes i ajustos.
- Skills "experimentals" (v0.x): poden evolucionar lliurement.

---

## 9. Riscos i mitigacions

| Risc | Probabilitat | Impacte | Mitigació |
|---|---|---|---|
| Gemini no detecta bé quan activar una skill per `description` | Mitjana | Alt (l'adaptació no s'aplica) | Proves A/B amb diverses `description` + fallback heurístic basat en perfil |
| Divergència entre md originals i skills extrets (Opció B) | Mitjana | Mitjà | Build script com a font única; CI que falla si es detecta divergència |
| Refactor de `corpus_reader.py` trenca ATNE en producció | Mitjana | Alt | Fer-ho en branca; tests d'integració abans del merge |
| Skills públics amb vulnerabilitats (scripts malicioses) | Baixa (nosaltres som autors) | Alt | Política de code review estricta per a qualsevol skill que inclogui `scripts/` |
| Els altres 4 assistents FJE no adopten la biblioteca | Mitjana | Baix | Documentar l'API de càrrega; fer-la agnòstica de stack (Gemini/Claude/OpenAI) |
| Docents es confonen amb l'estructura nova | Alta si Opció A | Mitjà | Opció B o C per mantenir fitxers plans llegibles pels humans |

---

## 10. Dependències i prerequisits

### Necessàriament abans d'iniciar:
1. **Fase D completa**: ATNE llegeix de corpusFJE (no de la seva còpia local). Raó: fer refactor sobre un corpus desincronitzat multiplicaria la complexitat.
2. **Decisió sobre stack d'ATNE**: seguir amb Gemini o migrar a Claude. Si migrem a Claude, skills són gairebé zero-config. Si no, cal implementar el runtime.
3. **Marc general revisat**: el parking lot de "revisió de coherència d'agents IA amb marc general" hauria de resoldre's abans, perquè les skills incorporaran els comportaments validats.

### Desitjable però no bloquejant:
- Un stack de testing automàtic per validar que cada skill produeix sortides esperades amb inputs coneguts.
- Documentació del procés per a nous contribuents (docents que vulguin afegir perfils).

---

## 11. Mètriques d'èxit

Per valorar si la refactorització ha estat exitosa:

1. **Tokens per adaptació (ATNE)**: reducció d'almenys 50% vs baseline actual.
2. **Temps de desenvolupament per afegir un perfil nou**: < 1 jornada per a un docent tècnic.
3. **Reutilització**: 2+ dels altres assistents FJE consumint la mateixa biblioteca en 6 mesos.
4. **Qualitat de sortida**: sense regressions en avaluacions ja existents (eval_db.py d'ATNE).
5. **Divergència zero**: 0 incidents on una skill i el seu md original divergeixen sense intencionalitat.

---

## 12. Referències

- **agentskills.io** — spec oficial de l'estàndard obert Apache 2.0.
- **Anthropic Claude Code** — primera implementació de referència.
- **OpenAI Codex** — segona plataforma adoptant l'spec.
- **Memòries del projecte mineriaRAG** (nivell Claude):
  - `project_sync_atne_corpusfje.md` — convencions append-only i estat Fases A-C.
  - `project_assistants_scope.md` — scope dels 5 assistents FJE.
  - `feedback_font_veritat_corpus.md` — regla absoluta "corpusFJE és font única".
- **Repositoris relacionats**:
  - `github.com/miquelamor-ai/corpusFJE` — aquest repo (font de veritat)
  - `github.com/FundacioJesuitesEducacio/ATNE` — primer consumidor
  - `github.com/miquelamor-ai/mineriaRAG` — eina de construcció del corpus

---

## 13. Obertes (decisions pendents)

- [ ] Arquitectura: Opció A, B o C? (proposta inicial: C → B en gradients)
- [ ] Stack d'ATNE: Gemini o Claude per aprofitar natius?
- [ ] Nomenclatura: skills amb prefix (`adapt-*`, `detect-*`, `plan-*`) o flat?
- [ ] Versionatge: semver estricte o tagging semàntic més lleuger?
- [ ] Governança: qui pot fer merge de PRs de skills?

---

*Document viu. Actualitzar quan es prenguin decisions o quan l'spec d'agentskills.io evolucioni.*
