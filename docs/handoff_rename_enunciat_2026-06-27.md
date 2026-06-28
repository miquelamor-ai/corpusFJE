# Handoff — rename write-activitat → write-enunciat (Fase 2)

**Data:** 2026-06-27
**Origen:** briefing ATNE (smoke test Fil 3 + consulta NotebookLM MALL FJE)
**De:** Claude (mineriaRAG) **→** Miquel + Claude (ATNE)

---

## Estat actual

### ✅ FASE 1 — FETA (branca `fix/skills-fase3-macro-hcl`, commit `f84735c`)

No toca cap contracte amb ATNE. Es pot mergejar a `master` quan es vulgui.

- `write-activitat`: `macro_tipologia: hibrida` → **`instructiva`**. Era l'única skill
  amb una macro fora de les 7 canòniques; feia fallar `validate_skills_writers.py`
  i **avortava tot el `build-skills.yml`** (per això cap skill de Fase 3 es regenerava
  i van caldre SKILL.md manuals).
- Reenquadrament HCL (decisió pedagògica de Miquel): comprendre la consigna **no és
  una HCL**, és la competència d'accés prèvia. L'operació demandada és variable i la
  fixa la consigna: pot ser una **HCL del MALL** (Descriure, Definir, Explicar,
  Justificar, Argumentar, Demostrar) o una **operació procedimental** (calcular,
  resoldre, ordenar, classificar). Resol el forat de "Calcula".
- Es regeneren els 3 derivats canònics (SKILL.md + prompt_adapter.md + rubrica.json)
  de les **5 skills de Fase 3** (write-activitat, write-cv, write-informe-tecnic,
  write-instancia, write-mail-professional).
- Validador: **31/31 OK**.

### ⏳ FASE 2 — PENDENT DE COORDINACIÓ (aquest doc)

El rename **toca el contracte `genre_key` amb ATNE** → s'ha de fer en lockstep o el
gènere deixa de funcionar a producció durant la finestra de desajust.

---

## Canvis a corpusFJE (els fa mineriaRAG quan es doni el GO)

1. **Directori:** `skills/generes/write-activitat/` → `skills/generes/write-enunciat/`
2. **Fitxer M3:** `M3_genere-escriure-activitat.md` → `M3_genere-escriure-enunciat.md`
3. **Frontmatter del M3:**
   - `genre_key: activitat` → `genre_key: enunciat`  ⚠️ **contracte ATNE**
   - `label_ca: "Activitat (exercici / tasca)"` → `label_ca: "Enunciat (exercici / activitat / tasca)"`
   - `titol: "Adaptar un document d'activitat"` → `titol: "Adaptar un enunciat escolar"`
   - `skill_meta: write-activitat@...` → `skill_meta: write-enunciat@corpusFJE/skills/generes/write-enunciat`
   - `descripcio`: ja reescrita a la Fase 1 amb el concepte "enunciat" (no cal tocar).
4. **Derivats:** el `build-skills.yml` els regenera sols després del push
   (SKILL.md `name`+`triggers`+`genre_key` passen a `enunciat`).
5. Netejar derivats orfes del directori antic.

## Canvis a ATNE (lockstep, els fa Claude-ATNE / Miquel)

- **Selector de gènere:** el valor que ATNE envia a `params.genere_discursiu` ha de
  passar de `"activitat"` a `"enunciat"` (és el que dispara el trigger de la skill).
  Etiqueta visible: la de `label_ca`.
- Qualsevol referència hardcoded a `"activitat"` com a clau de gènere.
- **Seqüència sense tall:** mergejar el rename a corpusFJE `master` **i** desplegar
  ATNE amb el selector actualitzat **alhora**. Si es fa el merge sol, el gènere
  "enunciat" no s'activarà fins que ATNE enviï "enunciat".

## ⚠️ Decisió oberta — header de sortida

El bloc que ATNE escriu i parseja és literalment `## Activitat`. Opcions:

- **(A, recomanada per fer-ho segur) Mantenir `## Activitat`.** El rename afecta
  identitat/selector però NO el parser de sortida. Zero canvis addicionals a ATNE.
  Lleugera incoherència nominal, totalment reversible.
- **(B) Canviar a `## Enunciat`.** Coherència total, però obliga ATNE a actualitzar
  el parser **alhora** i a treure `## Enunciat` de la llista de headers PROHIBITS
  del M3 (avui hi és). Més coordinació.

Miquel: pendent. Per defecte s'assumeix (A) tret que digueu el contrari.

---

## 🔎 Troballa separada (NO és aquest rename) — HCL "Interpretar/Valorar"

Revisant tot el corpus, **"Interpretar/Valorar"** apareix com a HCL principal o de
suport en **6 skills ja validades**: write-ressenya (principal), write-assaig,
expressar-preferencies, write-dialeg, write-diari, write-diari-camp.

Tampoc és a les 6 HCL canòniques que cita el briefing (Descriure, Definir, Explicar,
Justificar, Argumentar, Demostrar). És una **HCL composta diferent** de la
"Interpretar" sola de write-activitat (ja corregida). No s'ha tocat: és una decisió
pedagògica separada i de més abast.

**Pregunta per a Miquel:** "Interpretar/Valorar" és una HCL acceptada al canon MALL
de FJE (algunes formulacions de Jorba/Sanmartí l'inclouen) o també s'ha de normalitzar?
Segons la resposta, caldria una passada coordinada a aquestes 6 skills.
