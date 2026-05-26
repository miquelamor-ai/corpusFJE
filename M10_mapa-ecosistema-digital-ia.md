---
modul: M10
titol: "Mapa de l'ecosistema digital de FJE per a la integració de la IA"
tipus: mapa-ecosistema
descripcio: "Visió de conjunt de tots els productes digitals de la xarxa FJE relacionats amb la integració de la IA: plataformes, assistents, agents, corpus i editors. Inventari complet (10 productes), diagrama d'integració, dependències entre eines, fases de maduresa, roadmap tècnic conjunt i punts de coherència amb el marc. Per a la Direcció de Transformació Digital i el seu equip."
review_status: esborrany
generat_at: 2026-05-26
paraules_clau: ["ecosistema digital", "MAGINIA", "ATNE", "CREATIVIA", "Scriptorium", "corpusFJE", "LAIA", "assistent alumnat", "skills currículum", "DTD", "infraestructura", "dependències", "roadmap tècnic"]
---

# Mapa de l'ecosistema digital de FJE per a la integració de la IA

**Per a Direcció de Transformació Digital i equip TD · maig 2026**

> Aquest document recull tots els productes digitals de la xarxa relacionats amb la integració de la IA, les seves dependències i les fases de maduresa. Serveix per a tenir vista de conjunt, prioritzar tècnicament i mantenir coherència amb el marc institucional.

---

## 1. Inventari complet

Deu productes a l'ecosistema, agrupats per capa funcional:

### Capa de coneixement (font de veritat)

- **corpusFJE** · repositori de coneixement institucional FJE (mòduls M0–M10) en format markdown amb frontmatter estructurat. Font canònica per a totes les capes superiors.
- **Skills i JSON de currículum** · estructures consultables del corpus per a assistents (rúbriques, escenaris, currículum LOMLOE).

### Capa d'edició

- **Scriptorium** · webapp PHP que permet a editors autoritzats consultar i modificar el corpusFJE sense saber Git ni Markdown. Audit log via GitHub. Sistema de propostes i comentaris.

### Capa de plataformes pedagògiques

- **MAGINIA** · plataforma de paquets de sessió, escenaris i dinàmiques per a la difusió del marc. Rol facilitador. Producció.
- **LAIA** · agregador d'assistents IA dins laNET (plataforma corporativa FJE). Accés institucional amb identificació prèvia. Convenis amb proveïdors externs cas a cas.

### Capa d'assistents pedagògics

- **ATNE** · Adaptador de Textos a Necessitats Educatives. Suport docent quotidià. Pilot a producció.
- **CREATIVIA / CREACTIVITAT** · Assistent per al disseny d'activitats i seqüències didàctiques que incorporin IA. En redisseny.
- **Assistent IA per a alumnat** · prototip per a abril 2027. Per dissenyar (rol pedagògic per definir).
- **Programació anual línia alumnat-famílies** · suport futur per a curs 27-28.

---

## 2. Estat de maduresa

| Producte | Estat | Stack | Hosting |
|---|---|---|---|
| **MAGINIA** | ✅ producció | Next.js 15 + TypeScript + Supabase | Vercel |
| **corpusFJE** | ✅ producció | Repo Markdown + JSON manifest | GitHub |
| **Scriptorium** | ✅ producció | PHP 8.3 + Slim 4 + GitHub API | Cloud Run (europe-west1) |
| **LAIA** | ✅ producció | Plataforma corporativa FJE | laNET |
| **ATNE** | 🟠 pilot · cap a producció | App pròpia | Cloud Run |
| **Skills i JSON currículum** | ✅ producció parcial | Estructures dins corpusFJE | GitHub |
| **CREATIVIA** | 🟡 redisseny | Vite + JS · re-fer com a prototip | Local (en redisseny) |
| **Assistent IA per a alumnat** | ⬜ per dissenyar | Per definir | Per definir |
| **Programació línia alumnat-famílies** | ⬜ per dissenyar | Pedagògic primer, tècnic després | Per definir |

---

## 3. Diagrama d'integració

```
                              ┌──────────────────────────────────────┐
                              │   corpusFJE (font canònica)          │
                              │   M0-M9 corpus pedagògic             │
                              │   M10 corpus institucional IA        │
                              │   + skills, JSON currículum          │
                              └──────────────┬───────────────────────┘
                                             │
                          ┌──────────────────┼──────────────────────┐
                          │                  │                      │
                          ▼                  ▼                      ▼
                ┌──────────────┐    ┌────────────────┐    ┌─────────────────┐
                │  Scriptorium │    │  Assistents IA │    │  MAGINIA        │
                │  edita corpus│    │  consulten via │    │  serveix sessions│
                │  (audit log) │    │  RAG           │    │  i materials    │
                └──────────────┘    └────────┬───────┘    └────────┬────────┘
                                             │                     │
                          ┌──────────────────┼─────────────┐       │
                          │                  │             │       │
                          ▼                  ▼             ▼       ▼
                ┌──────────────┐   ┌──────────────┐  ┌──────────┐  │
                │     ATNE     │   │  CREATIVIA   │  │ Assistent│  │
                │   adaptació  │   │  disseny     │  │ alumnat  │  │
                │   textos NESE│   │  seqüències  │  │ (futur)  │  │
                └──────────────┘   └──────────────┘  └──────────┘  │
                                                                   │
                                ┌──────────────────────────────────┘
                                │
                                ▼
                          ┌──────────────┐
                          │     LAIA     │
                          │  agregador   │
                          │  d'assistents│
                          │  a laNET     │
                          └──────────────┘
```

**Lectura**:
- El **corpusFJE** és font canònica única (regla 1 del Scriptorium).
- **Scriptorium** és l'única via d'edició estructurada del corpus.
- Els **assistents IA** consulten el corpus via RAG · no dupliquen contingut.
- **MAGINIA** consumeix el corpus per a sessions i materials (pipeline pendent d'implementar).
- **LAIA** agrega els assistents corporatius dins laNET, amb identificació institucional.

---

## 4. Dependències entre productes

| Producte | Depèn de | Aporta a |
|---|---|---|
| corpusFJE | — (fonament) | Tots els altres productes |
| Scriptorium | corpusFJE + GitHub API + Entra ID (futur) | Modifica corpusFJE |
| MAGINIA | corpusFJE (fetch HTMLs A4 · pipeline pendent) | Sessions i materials a facilitadors |
| ATNE | corpusFJE (skills, fonts pedagògiques) | Adaptació de textos a docent |
| CREATIVIA | corpusFJE (currículum, marc, escenaris) | Disseny de seqüències a docent |
| Assistent alumnat | corpusFJE (currículum, política d'ús alumnat, marc) + decisions pedagògiques (DEC-13) | Suport directe a alumnat |
| LAIA | Identificació institucional FJE + convenis externs (Gemini, etc.) | Punt d'accés agregat |

**Punts crítics de dependència**:
- Si el corpusFJE queda obsolet, tots els assistents pateixen.
- Si Scriptorium falla, l'edició s'ha de fer per Git (no escalable).
- Si MAGINIA no consumeix el corpus, hi haurà duplicats (situació actual provisional).

---

## 5. Roadmap tècnic conjunt

### Q1 26-27 (set-des 26)

- **Pipeline fetch corpus → MAGINIA** · build-time sync per a què el kit i les sessions consumeixin la font canònica. (sessió pròpia a MAGINIA)
- **Scriptorium · Bloc 1 (comentaris)** · compositor de respostes a `/my-proposals`, visualització del fil. (sessió a Scriptorium en marxa)
- **ATNE pas a producció** · escalat, monitor, recollida de feedback pilot.
- **CREATIVIA · prototip operatiu** · pilot a 1-2 centres Estat A.

### Q2 26-27 (gen-mar 27)

- **Scriptorium · Bloc 2 (visor maquetat amb anotacions)** · iframe HTML A4 + Recogito + persistència `.comments.json`.
- **HTMLs A4 dels documents M10 pugen al corpus** com a `<nom>.a4.html` (font única).
- **CREATIVIA producció** · disponibilitat ampla.
- **Assistent IA per a alumnat · especificació** (DEC-13 · CPe).

### Q3 26-27 (abr-jun 27)

- **Assistent IA per a alumnat · prototip demostrable** (D6 del pla mestre, abans abril 27).
- **Dashboard seguiment desplegament** (C7) · per centre i xarxa.
- **Materials gràfics del marc** (E1) · infographics, posters, cards.

### Curs 27-28

- **Assistent alumnat pilot real** · amb autoritzacions famílies signades (FAM6 + P6).
- **Programació anual línia alumnat-famílies** disponible (E5).
- **Revisió del marc** primera revisió formal (V3).

---

## 6. Coherència amb el marc institucional

L'ecosistema digital ha de mantenir-se alineat amb el Marc General i les seves polítiques. Punts clau:

- **No humanitzar la IA** en cap descripció, manual, UI o material d'assistent. La frase canònica del marc s'aplica.
- **Subordinació tecnològica** · l'eina pot dir/fer, però la decisió és humana.
- **Mediació humana explícita** als assistents pedagògics · l'assistent suggereix, el docent valida.
- **Política de protecció de dades** (`M10_politica-proteccio-dades-ia.md`) · cap eina del ecosistema utilitza dades sensibles sense base legal.
- **Llista d'eines homologades** (`M10_llista-eines-homologades.md`) · l'ecosistema propi és l'estàndard, no les eines consumidor.
- **Documents canònics al corpus**, no duplicats · MAGINIA fa fetch.

---

## 7. Punts oberts per a la conversa DTD

Aquestes són les decisions tècniques i estratègiques pendents:

- **Especificació de CREATIVIA refet** (DEC-14 · tàndem) · què canvia exactament respecte la versió anterior? Cal especificar abans del desenvolupament.
- **Pipeline fetch corpus → MAGINIA** · build-time sync, runtime via raw, o GitHub Action? Cost-benefici de cadascun.
- **Auth unificada** entre Scriptorium, MAGINIA, ATNE, CREATIVIA · Entra ID com a estàndard?
- **Hosting unificat** · tots a Cloud Run o cadascú al seu? Cost operatiu.
- **Telemetria i indicadors d'ús** · què es mesura a cada producte, on s'agreguen, qui en té accés.
- **Còpia de seguretat i recuperació** del corpusFJE · estratègia formal.
- **Assistent IA alumnat** · rol pedagògic (DEC-13 · CPe) + stack tècnic (DTD).
- **Programació anual línia alumnat-famílies** (E5) · qui ho lidera, com s'integra amb assistent alumnat.
- **LAIA · convenis amb proveïdors externs** · qui els gestiona, com es renoven, com es valida que es compleixen.
- **Documentació tècnica de cada producte** · cal mantenir-la a `docs/` del repo corresponent · qui ho fa.

---

## 8. Riscos tècnics identificats

| Risc | Probabilitat | Impacte | Mitigació actual |
|---|:-:|:-:|---|
| Pèrdua del corpusFJE per error de sincronia | baixa | alt | Git audit log + backups |
| Scriptorium auto-regenera manifest i elimina M10 | alta · ja ha passat | mitjà | Cal ajustar script de regeneració al mineriaRAG · pendent |
| Vulnerabilitat seguretat a MAGINIA · dades alumnat | baixa | alt | RLS Supabase + auth corporativa |
| ATNE escalat pobre · cau a producció | mitjana | alt | Pilot controlat · monitor |
| CREATIVIA redissenyat triga molt · es perd finestra docent | mitjana | mitjà | Plan B: ATNE cobreix algunes funcions |
| Assistent alumnat sense rol clar al desplegar | alta · ja apuntat | alt | Especificar abans del desplegament (DEC-13) |
| Convenis externs LAIA caduquen sense renovació | mitjana | alt | Procés de renovació amb 6 mesos d'avís |
| Duplicats corpus-MAGINIA sense sincronia | alta · ja existent | mitjà | Pipeline fetch (Q1 26-27) |

---

## 9. Ecosistema i altres mòduls del corpus

L'ecosistema no aïllat de la resta de coneixement institucional. Punts d'intersecció:

- **M5 Tecnopedagogia** (corpus pedagògic) · marc AIA-PCEK, MIHIA, prompt engineering. Els assistents han de saber-ne · alimentació RAG.
- **M8 Governança i seguretat** (corpus pedagògic) · GDPR, ètica, Reglament europeu IA. Els assistents han de complir-ne.
- **M10 Marc d'Integració de la IA** · totes les polítiques, llistes i protocols són d'aplicació a tot l'ecosistema.

---

## ANNEX · URLs i accés

| Producte | URL | Auth |
|---|---|---|
| MAGINIA | https://maginia.vercel.app/ | Cookie + Supabase |
| ATNE | https://atne-1050342211642.europe-west1.run.app/ | App pròpia |
| Scriptorium | https://scriptorium-1050342211642.europe-west1.run.app/ | @fje.edu |
| corpusFJE | https://github.com/miquelamor-ai/corpusFJE | GitHub |
| LAIA | (intern laNET) | identificació institucional FJE |

---

## ANNEX · Documents complementaris al corpusFJE

- **`M10_marc-general-ia.md`** · Marc al què tot ha de servir.
- **`M10_full-ruta-desplegament-ia.md`** · Camí amb decisions tècniques (DEC-13, DEC-14).
- **`M10_politica-proteccio-dades-ia.md`** · Què cal complir a nivell tècnic.
- **`M10_llista-eines-homologades.md`** · Eines pròpies i criteris.

---

*Mapa de l'ecosistema digital FJE · maig 2026 · per a Direcció de Transformació Digital.*
