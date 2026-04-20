# Context i decisions per a compartir amb ATNE

**Propòsit**: aquest document agrupa les decisions i descobertes preses al projecte mineriaRAG durant el 2026-04-20 que afecten ATNE. Està al repo corpusFJE (font de veritat única) perquè qualsevol persona/agent que treballi a ATNE pugui llegir-lo i alinear-se.

**Audiència**: humans o agents IA (p.ex. Claude Code, assistents Gemini/OpenAI) que treballin al repo ATNE.

---

## TL;DR (llegir primer)

1. **Font de veritat única del corpus pedagògic = `github.com/miquelamor-ai/corpusFJE`**. No mantenir còpies locals divergents. Qualsevol canvi al contingut del corpus es fa al repo corpusFJE, no a `ATNE/corpus/`.
2. **ATNE/corpus/ està desincronitzat amb corpusFJE** (estat 2026-04-20 abans de fer Fase D). Els 18 md allà són subconjunt del corpusFJE però van divergir per edicions no propagades. Ja ho hem solucionat al corpusFJE (Fases A+B+C, 9 commits). Ara ATNE ha d'actualitzar-se.
3. **Inspiració Agent Skills**: el corpusFJE podria refactoritzar-se per complir l'estàndard obert [agentskills.io](https://agentskills.io). Això beneficia directament ATNE (menys tokens) i facilita interoperabilitat amb altres assistents FJE. Pla complet: [skills-refactor-plan.md](./skills-refactor-plan.md).
4. **ATNE forma part d'un ecosistema de 5 assistents FJE**, no és un projecte aïllat. Vegeu [fje-assistants-overview.md](./fje-assistants-overview.md) per context estratègic.

---

## 1. Context estratègic

### Ecosistema FJE (més enllà d'ATNE)
FJE planeja **5 assistents IA cara-docent** (ATNE és el primer operatiu):
1. **ATNE** — adaptació de materials didàctics (en curs)
2. Disseny curricular
3. Avaluació
4. Convivència, tutoria, acompanyament
5. Gestió i organització

Els 4 següents consumiran la mateixa base de coneixement pedagògic (corpusFJE). Per tant, les decisions que prenguem amb ATNE estableixen el patró per als altres.

**Implicació pràctica per ATNE**: evitar decisions d'arquitectura que siguin difícils de generalitzar. Si una funcionalitat és específica d'ATNE, aïllar-la clarament; si és generalitzable, dissenyar-la pensant en reutilització.

Context complet: [fje-assistants-overview.md](./fje-assistants-overview.md).

---

## 2. Decisions preses al mineriaRAG el 2026-04-20 que afecten ATNE

### 2.1 — Sincronització massiva ATNE → corpusFJE (Fases A+B+C)
S'han integrat al corpusFJE **totes les capes operatives d'ATNE** que no hi eren:

**Fase A** (2 fitxers on corpusFJE era més gran — merge acurat):
- `M1_alumnat-nouvingut.md` — afegida secció 6 d'ATNE + URLs XTEC. Commit `d5fe8e5`.
- `M1_acollida-marc-conceptual.md` — no calia merge (ATNE tenia versió antiga; corpusFJE ja estava superior amb 24/36 mesos normatius, taula MECR, 15 fonts).

**Fase B** (2 fitxers nous només a ATNE — copia completa a corpusFJE):
- `M3_generes-discursius.md` — 4 macro-gèneres. Commit `edd801a`.
- `M3_generes-22.md` — 22 sub-gèneres amb regles crítiques (llegit per `corpus_reader.py`). Commit `975316a`.

**Fase C** (14 fitxers comuns — append-only de la secció 6 d'ATNE):
- 13 M1_* (TDAH, TDL, altes-capacitats, alumnat-TEA, creuament-variables, discapacitat-auditiva/intel·lectual/visual, dislèxia, trastorn-coordinació-dispraxia, trastorns-emocionals-conducta, vulnerabilitat-socioeducativa).
- `M2_DUA-principis-pautes.md` — amb blocs DUA Accés/Core/Enriquiment.
- `M3_lectura-facil-comunicacio-clara.md` — cas especial: 4 seccions operatives afegides (6, 7, 8, 9).
- Commits: `d4b6b0d`, `74b52d0`, `436a593`, `01b179f`, `07dbf4b`, `e149567`.

**Total**: 9 commits a `origin/master` de corpusFJE, +700 línies afegides, 0 supressions de contingut.

### 2.2 — Regla absoluta: corpusFJE és font de veritat única
A partir de 2026-04-20, cap projecte (inclòs ATNE) pot:
- Crear nous directoris amb md del corpus pedagògic.
- Editar md del corpus fora del repo corpusFJE.
- Mantenir còpies locals sense propagar canvis al repo.

Si ATNE necessita una funció sobre el corpus, l'ha d'afegir a `corpus_reader.py` que llegeix del corpusFJE (directament o via mecanisme de Fase D).

### 2.3 — Convencions de merge adoptades
Per si ATNE vol replicar el flux en el seu propi repo:
- **Append-only estricte**: no modificar contingut existent, només afegir-ne.
- **Branques dedicades** per cada fitxer/batch.
- **Verificació abans de commit**: diff byte-a-byte + `comm -23` per confirmar 0 línies perdudes.
- **Numeració de seccions 1, 2, 3, 4, 6, 5**: mantenir aquest ordre (secció 6 entre 4 i 5) per coherència amb com ATNE referenciava "secció 6" abans.
- **Fonts**: opció C — dues taules (acadèmiques + URLs XTEC) coexisteixen a la mateixa secció 5.

---

## 3. Què ha de fer ATNE ara (Fase D del pla)

ATNE encara llegeix del seu `ATNE/corpus/` local, que ja està **desincronitzat** respecte corpusFJE. Cal escollir un mecanisme per convergir:

### Opció D.1 — git submodule
Fer que `ATNE/corpus/` sigui un submodule apuntant a `github.com/miquelamor-ai/corpusFJE`. Avantatges: simple, explícit. Inconvenient: cal `git submodule update` periòdicament.

### Opció D.2 — Script de sync
Un `scripts/sync_corpus.py` que:
- Fa `git pull` del corpusFJE a un directori temporal.
- Copia els md rellevants a `ATNE/corpus/`.
- Es pot cron-njar o executar manualment.

### Opció D.3 — Llegir de Supabase
Si la indexació a Supabase pgvector ja està operativa, ATNE pot consumir el corpus via queries a la base de dades en comptes de fitxers locals. Tira els md locals completament.

### Opció D.4 — Llegir directament del repo GitHub via API
ATNE fa una crida a l'API de GitHub (o clona a memòria) cada vegada que cal llegir un md. Funciona però pot ser lent per ús interactiu.

**Recomanació inicial**: Opció D.1 (submodule) per simplicitat a curt termini, migrant a D.3 (Supabase) quan la capa de vector store estigui estable.

**Prerequisit a qualsevol opció**: resoldre el fet que `ATNE/corpus/` actual està versionat al repo ATNE. Cal decidir si:
- Esborrar els md del repo ATNE i substituir per submodule/sync.
- O bé deixar com a backup i simplement deixar de llegir-los.

### Tasques concretes per ATNE (Fase D)
1. [ ] Decidir mecanisme (D.1 / D.2 / D.3 / D.4).
2. [ ] Implementar-lo en una branca d'ATNE.
3. [ ] Actualitzar `corpus_reader.py` per llegir de la nova font.
4. [ ] Validar amb tests d'integració que les adaptacions surten igual o millor.
5. [ ] Eliminar `ATNE/corpus/` antic del repo (o reduir-lo a un README que apunti al corpusFJE).
6. [ ] Actualitzar README d'ATNE documentant la dependència.

---

## 4. Inspiració futura: Agent Skills (Fase E)

Un cop resolta la Fase D, es proposa refactoritzar el corpusFJE per complir l'estàndard **agentskills.io**. Això beneficia ATNE directament:

### Beneficis per ATNE
- **Reducció de tokens**: actualment ATNE injecta md sencers al prompt. Amb skills, només el "body" de les skills rellevants (estimació: ~65% de reducció).
- **Progressive disclosure natiu**: l'agent carrega només les skills necessàries per a la petició.
- **Code reuse amb altres assistents**: si ATNE usa skills, els altres 4 assistents FJE podran usar les mateixes sense duplicar.

### Implicacions d'implementació per ATNE
- **Stack**: Gemini no té suport natiu d'Agent Skills (Claude i OpenAI sí). ATNE ha d'escollir:
  - **Implementar skill runtime manualment** en Python (~200 línies, evolució de `corpus_reader.py`).
  - **O migrar a Claude** per aprofitar el suport natiu.
- **Refactor de `corpus_reader.py`**: passar de lectura de blocs per clau a lectura de skills per descripció.
- **Nou component**: un "skill matcher" que, donat un perfil d'alumne, seleccioni quines skills són rellevants abans d'injectar-les al prompt.

### Pla complet
Vegeu [skills-refactor-plan.md](./skills-refactor-plan.md) al mateix repo corpusFJE per l'anàlisi exhaustiva, mapping de seccions, opcions A/B/C, fases de migració, riscos, mètriques d'èxit.

---

## 5. Parking lot (coses pendents de revisar o decidir)

### 5.1 — Revisió de coherència d'agents IA amb marc general
Els md del corpusFJE (que ara també són font d'ATNE) contenen fragments tipus:

> *"Un alumne amb discapacitat intel·lectual lleu diu a l'agent que té molts deures i no sap com començar. L'agent li suggeriria: 'És normal sentir-se així de vegades. Pots demanar al teu professor...'"*

Això suggereix que l'agent parla **directament amb l'alumne**. Cal validar si aquest patró és coherent amb el marc general (`marc-general-ia-esborrany.md`), on probablement l'agent és **eina del docent**, no substitut en la relació amb l'alumne.

Si el marc general ho contradiu, caldrà reformular aquests fragments perquè donin recomanacions **al docent** sobre com adreçar-se a l'alumne, no a l'alumne directament.

**Impacte per ATNE**: si el patró canvia, les instruccions de secció 6 també ho faran — podria afectar la veu i el to de les adaptacions generades.

### 5.2 — Decisió d'stack d'inferència per l'ecosistema FJE
ATNE usa Gemini 2.5-flash. Els altres assistents FJE futurs podrien usar altres models. Decisió pendent: anar a un stack únic (simplifica interoperabilitat i skills) o permetre heterogeneïtat (més flexibilitat).

### 5.3 — Governança del corpus
Com s'aproven canvis al corpusFJE? Review pedagògic + tècnic? Versionat de perfils? Protocols per a canvis que afectin assistents en producció?

---

## 6. Glossari ràpid

| Terme | Significat |
|---|---|
| **corpusFJE** | `github.com/miquelamor-ai/corpusFJE` — font de veritat del contingut pedagògic |
| **mineriaRAG** | `github.com/miquelamor-ai/mineriaRAG` — eina de construcció del corpus (scraping, classificació, etc.) |
| **ATNE** | Adaptador de Textos a Necessitats Educatives — primer assistent operatiu |
| **Secció 6** | Capa operativa d'un md de perfil — "INSTRUCCIONS PER A L'LLM" que ATNE injecta al prompt |
| **Fase A/B/C** | Sincronització 2026-04-20: merge/copy/append-only de contingut d'ATNE cap a corpusFJE |
| **Fase D** | Pendent: ATNE passa a llegir des de corpusFJE en lloc de còpia local |
| **Fase E** | Futur: refactor del corpusFJE com a biblioteca d'Agent Skills |
| **Agent Skills** | Estàndard obert (agentskills.io) per empaquetar capacitats procedimentals d'un agent LLM |
| **Progressive disclosure** | Patró de càrrega de skills en 3 nivells: metadata → body → recursos |

---

## 7. Referències (enllaços)

- [skills-refactor-plan.md](./skills-refactor-plan.md) — Pla detallat de Fase E.
- [fje-assistants-overview.md](./fje-assistants-overview.md) — Visió global del projecte FJE.
- [agentskills.io](https://agentskills.io) — Estàndard obert Agent Skills.
- `github.com/miquelamor-ai/corpusFJE` — Repo del corpus (font de veritat).
- `github.com/FundacioJesuitesEducacio/ATNE` — Repo d'ATNE.

---

## 8. Com usar aquest document a ATNE

Si comences una sessió al repo ATNE amb Claude Code, Gemini o un altre assistent:

1. **Llegeix primer aquest document** (o almenys la TL;DR).
2. **Assumeix que ATNE/corpus/ local pot estar desactualitzat** fins que la Fase D estigui completa. El corpusFJE sempre té la versió bona.
3. **No facis edicions directes als md d'ATNE/corpus/**. Si cal modificar contingut pedagògic, fes-ho al repo corpusFJE.
4. **Si tens dubtes d'arquitectura**, consulta primer [fje-assistants-overview.md](./fje-assistants-overview.md) per veure si hi ha decisions ja preses.

---

*Document viu. Qualsevol que treballi al projecte pot actualitzar-lo amb noves decisions rellevants per a ATNE. El Miquel és el responsable últim de coherència.*
