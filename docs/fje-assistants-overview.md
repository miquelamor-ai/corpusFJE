# Projecte FJE — Visió global dels assistents IA

**Document transversal**: aquest document viu al corpusFJE (la font de veritat comuna) però el seu abast supera qualsevol projecte individual (mineriaRAG, ATNE, futurs assistents). Funciona com a **parking lot superior** per no oblidar decisions estratègiques que afecten l'ecosistema FJE.

**Última actualització**: 2026-04-20
**Responsable**: Miquel Amor
**Estat**: viu, s'actualitza a mesura que es prenen decisions

---

## 1. Visió

Construir una família coherent d'assistents IA per a Jesuïtes Educació (FJE) que comparteixin una mateixa base de coneixement pedagògic (**corpusFJE**) i que s'alimentin mútuament en comptes de duplicar esforços.

Principi: **una font de veritat pedagògica, múltiples eines que la consumeixen**.

---

## 2. Els 5 assistents previstos (orientats a docents/centre)

| # | Nom | Àmbit | Estat | Repo |
|---|---|---|---|---|
| 1 | **ATNE** (Adaptador de Textos a Necessitats Educatives) | Materials didàctics — adaptació de textos | En desenvolupament | `github.com/FundacioJesuitesEducacio/ATNE` |
| 2 | Disseny curricular | Escenaris, programacions, seqüències didàctiques | Planificat | — |
| 3 | Avaluació | Feedback, instruments, proves, informes | Planificat | — |
| 4 | Convivència, tutoria i acompanyament | Dinàmiques, tutoria, facilitació | Planificat | — |
| 5 | Gestió i organització | Planificació de centre i aula | Planificat | — |

---

## 3. Els assistents cara-alumne (segona línia, més endavant)

Basats en els **7 rols d'IA d'Ethan Mollick** + nivells de delegació:
Tutor, Coach, Mentor, Teammate, Student (IA aprèn, alumne ensenya), Tool, Simulator.

Són conceptualment diferents:
- Cara-alumne (no cara-docent com els 5 anteriors)
- Corpus diferent: curricular, no pedagògic-guia
- Arquitectura diferent: més conversacional, menys RAG-pesat
- Estat: **no prioritat immediata**. Pendent de tenir els 5 cara-docent estables.

---

## 4. Infraestructura compartida

### 4.1 — Corpus (font de veritat única)
**`github.com/miquelamor-ai/corpusFJE`** — pedagogia, perfils d'alumnat, DUA, lectura fàcil, gèneres discursius, marc IA, etc.

**Regla dura** (2026-04-20, aplicable a qualsevol projecte Antigravity): cap projecte pot mantenir una còpia local divergent del corpus. Tot canvi es fa al repo corpusFJE i es sincronitza via el mecanisme decidit a Fase D del pla de sincronització.

### 4.2 — Eina de construcció del corpus
**`github.com/miquelamor-ai/mineriaRAG`** — pipeline Human-in-the-Loop per:
- Scraper web (trafilatura + BeautifulSoup)
- Classificació Gemini
- Revisió humana
- Generació d'entrades RAG amb plantilla
- Exportació al corpusFJE

### 4.3 — Indexació per a inferència (proposta)
**Supabase pgvector** — vector store central perquè tots els assistents consumeixin la mateixa indexació sense duplicar processat.

Tables projectades:
- `rag_fje` (embeddings + metadades dels chunks)
- `kg_nodes`, `kg_edges` (knowledge graph curricular)

Estat: decisió presa (SESSIONS.md), implementació parcial.

### 4.4 — Biblioteca de skills (Fase E — vegeu [skills-refactor-plan.md](./skills-refactor-plan.md))
Proposta de fer que el contingut operatiu del corpusFJE compleixi l'estàndard obert **agentskills.io** perquè qualsevol dels assistents pugui carregar skills sota demanda sense duplicar lògica.

---

## 5. Decisions estratègiques preses (registre)

### 2026-04-20 — Font de veritat única
- corpusFJE és l'únic repo autoritzat per al contingut pedagògic.
- Cap projecte pot mantenir còpies locals divergents.
- Regla a foc per a tots els projectes Antigravity.
- ATNE/corpus i mineriaRAG/output/_sintesis: pendents d'esborrar (Fase D).

### 2026-04-20 — Abast d'ATNE com a pilot
- ATNE és el primer assistent operatiu.
- Les decisions d'arquitectura que prenem amb ATNE (com llegeix del corpus, com gestiona perfils, etc.) es generalitzaran als altres 4 assistents.
- El que funciona a ATNE ha de ser replicable; el que es refactora a ATNE ha de propagar-se al patró comú.

### 2026-04-20 — Inspiració Agent Skills
- S'ha identificat el patró Agent Skills (agentskills.io) com un camí natural per al corpusFJE.
- Pendent d'anàlisi detallada (vegeu [skills-refactor-plan.md](./skills-refactor-plan.md)).
- No tocar l'arquitectura actual fins que la Fase D (sync ATNE↔corpusFJE) no estigui tancada.

### 2026-03 — Stack ATNE
- Python FastAPI + HTML/JS pur (zero frameworks JavaScript pesats).
- Gemini 2.5-flash per a adaptació.
- Supabase per a vector store i knowledge graph.

### 2026-03 — Model del projecte de diversitat
- Tres nivells: perfil → característica (constitutiva/contextual).
- Una característica pot ser constitutiva (TDAH, dislèxia, TEA) o contextual (nouvingut, vulnerabilitat).
- Aquest model governa l'estructura del corpus M1.

---

## 6. Parking lot estratègic (no oblidar)

Coses pendents que no són urgents però que no es poden perdre de vista:

### 6.1 — Revisió de coherència dels agents IA amb el marc general
Revisar tots els md del corpusFJE que descriuen com ha d'actuar un agent d'IA en la interacció amb alumnat (heurístiques + instruccions LLM) i assegurar que són coherents amb `marc-general-ia-esborrany.md`.

**Fragment crític detectat** (exemple): els md de perfils M1_* tenen "Exemples complets de raonament" on l'agent sembla parlar directament a l'alumne ("L'agent li suggeriria: 'És normal sentir-se així...'"). Cal validar si aquest patró és coherent amb el marc general (on probablement l'agent és eina del docent, no substitut) o cal reformular.

Prioritzar revisió de: `M5_proposits-aprenentatge`, `M5_arquitectura-proposit-rol-nivell`, `M5_nivells-delegacio-mihia`.

### 6.2 — Governança del corpus
Definir:
- Qui pot fer PRs al corpusFJE?
- Quin flux de review (tècnic + pedagògic)?
- Versionat de perfils (semver? date-based?)
- Com validem canvis a perfils vius que ATNE i altres assistents ja consumeixen?

### 6.3 — Stack d'inferència per ecosistema FJE
Decisió pendent: tots els assistents han d'usar el mateix model (p.ex. tots Claude, o tots Gemini) o es permet heterogeneïtat?
- **A favor d'un sol stack**: interoperabilitat, skills natives, contractes de cost/privacitat uniformes.
- **A favor d'heterogeneïtat**: flexibilitat, evitar lock-in, escollir el millor model per cada cas.

### 6.4 — Desplegament i escala
- Com desplegarem els assistents quan surtin de pilot? (Cloud Run ja insinuat a ATNE via `cloudbuild.yaml`)
- Autenticació unificada (SSO FJE)?
- Telemetria compartida per mesurar ús i efectivitat educativa?

### 6.5 — Avaluació contínua
- Cal un framework d'avaluació que mesuri qualitat pedagògica de sortides, no només mètriques tècniques.
- ATNE ja té `evaluator_agent.py` i `evaluator_rubrics.py` — generalitzar com a eina comuna?

---

## 7. Convencions transversals (aplicables a tots els assistents)

- **Idioma de comunicació amb usuari**: sempre català.
- **To**: pràctic, clar, amb el "per què" de cada decisió (preferència explícita del Miquel, que no és programador).
- **Formats de codi**: UTF-8, LF o CRLF segons plataforma (el repo és mixt; acceptable).
- **Commits**: missatges en català, format `tipus: descripció` (`feat`, `fix`, `sync`, `docs`, `refactor`).
- **Documentació**: cada decisió important queda a `docs/` del repo corresponent o al parking lot d'aquest document.

---

## 8. Com usar aquest document

Si estàs treballant en un projecte nou o modificació gran:

1. **Consulta primer aquest document** per veure si la decisió encaixa amb el marc global.
2. **Si la decisió afecta més d'un projecte** (p.ex. refactor de sincronització, canvi d'stack), afegeix-la a la secció 5 (decisions) un cop presa.
3. **Si és un tema que s'ha de vigilar però no és urgent**, posa'l al parking lot (secció 6).
4. **Si descobreixes una inconsistència** entre aquest document i alguna altra ubicació, assenyala-la explícitament al Miquel abans de procedir.

---

*Aquest document s'actualitza manualment. No hi ha cap eina automàtica que el mantingui sincronitzat amb les memòries Claude de cada projecte — la sincronització és responsabilitat d'escriure les decisions aquí quan es prenen.*
