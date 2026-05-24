---
modul: M10
titol: "Full de ruta acrònic del desplegament del Marc General d'IA"
tipus: pla-desplegament
descripcio: "Mapa del camí complet per al desplegament del Marc General d'IA a la xarxa FJE: 8 línies de treball, 53 milestones codificats, 16 decisions catalogades per òrgan, dependències i camí crític. Sense calendari — fixa l'ordre lògic i els punts on cal decisió."
review_status: esborrany
generat_at: 2026-05-22
paraules_clau: ["full de ruta", "desplegament", "marc general IA", "milestones", "decisions institucionals", "cicle 26-29", "gestió", "docència", "alumnat", "famílies"]
---

## INTRODUCCIÓ

Aquest document mostra **el camí complet** que cal recórrer per arribar a tancar el cercle al voltant dels tres cims del marc general d'IA: que **l'alumnat aprengui** sobre, per a i amb IA; que els **docents proposin i acompanyin** seqüències amb i sense IA; i que les **famílies estiguin informades** i donin suport.

És **acrònic** intencionalment: no fixa dates. Fixa **l'ordre lògic** —què va abans de què— i les **portes de decisió** —qui ha d'aprovar què perquè la peça següent es pugui obrir.

El calendari arribarà quan les decisions estiguin preses. Forçar dates abans és comprometre's amb un escenari abans que les condicions hi siguin.

---

## CONVENCIONS

### Codis de milestone

- **Fx** · fonament transversal (marc, polítiques, eines·base)
- **Gx** · línia gestió
- **Dx** · línia docent
- **Sx** · línia alumnat — sobre i per a IA
- **Ax** · línia alumnat — amb IA
- **FAMx** · línia famílies
- **Ex** · eines (assistents i agents)
- **Vx** · avaluació i revisió

### Codis de decisió

DECs catalogades a §4. Cada decisió té un òrgan que la pren i un milestone que desbloqueja.

### Símbols d'estat

- ✅ fet
- 🟡 en marxa
- 🟠 prototip o pilot
- ⬜ no iniciat

### Tipus de dependència

- `→` dependència dura — no es pot iniciar sense el precedent
- `~>` precondició pràctica — es pot iniciar sense, però es completa millor amb
- `‖` independent — es pot fer en paral·lel sense lligam

---

## 1. CAMÍ CRÍTIC

La cadena que si s'atura, atura tot:

```
F1·F2 → DEC-1 → F4 → F7 → DEC-4 → G2/D1 → D4 → D6/D7 → S1/A1 → Pilots
```

Llegida:

1. **F1·F2** — Marc tancat editorialment i polítiques v0 disponibles.
2. **DEC-1** — Aval del cicle de desplegament com a línia institucional de xarxa (CDX).
3. **F4** — Cicle institucionalitzat.
4. **F7** — Trobada institucional d'equips directius (descobriment col·lectiu).
5. **DEC-4** — Designació de la persona d'enllaç IA al centre (DG centre + cap pedagogia).
6. **G2/D1** — Persona designada · difusió al claustre.
7. **D4** — Formació marc, polítiques i protocols al claustre.
8. **D6/D7** — Formació CD alumnat amb IA · disseny d'activitats d'aula amb IA.
9. **S1/A1** — Currículum vertical i catàleg d'activitats.
10. **Pilots** — Primers grups d'alumnat amb activitats reals.

Si una d'aquestes peces falla:

- **DEC-1 sense aval**: cada centre s'arregla aïllat, sense cobertura institucional.
- **F7 sense trobada**: el marc no fa el pas de "criteris orientadors" a "marc validat" col·lectivament.
- **DEC-4 sense designació**: la formació al centre no té qui la sostingui entre sessions.
- **D4 sense formació al claustre**: l'aplicació de la IA es fa sense criteri institucional.

---

## 2. MAPA DE MILESTONES PER LÍNIA

### F · Fonament transversal

| Codi | Milestone | Estat | Decisions associades |
|------|-----------|-------|----------------------|
| **F1** | Marc General tancat editorialment | 🟡 | — |
| **F2** | Polítiques v0 disponibles (P1–P5) + llistes L1–L3 | ✅ | — |
| **F3** | Material i guies de difusió EEDD preparades | 🟡 | — |
| **F4** | Aval del cicle de desplegament com a línia institucional de xarxa | ⬜ | **DEC-1** |
| **F5** | Aval de la figura "enllaç IA d'escola" | ⬜ | **DEC-2** (requereix consens previ DTD + DG) |
| **F6** | Mandat al CSC per estudi de dedicació horària | ⬜ | **DEC-3** |
| **F7** | Trobada institucional EEDD · descobriment col·lectiu del marc | ⬜ | — |
| **F8** | Polítiques validades CDX (P1–P5 v.CDX) | ⬜ | **DEC-7** |
| **F9** | Assessoria legal protecció dades contractada | ⬜ | **DEC-15** |

### G · Línia gestió

La línia més senzilla i la primera a tancar.

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **G1** | Difusió de criteris orientadors a EEDD (pre-trobada) | ⬜ | — |
| **G2** | Persona d'enllaç IA al centre identificada | ⬜ | **DEC-4** (DG centre) |
| **G3** | Difusió del marc al propi ED del centre (post-trobada) | ⬜ | — |
| **G4** | Pla anual del centre amb línia IA reservada | ⬜ | **DEC-6** (DG centre) |
| **G5** | Decisions de governança del centre preses (què sí · què no · qui) | ⬜ | DG centre + cap ped |
| **G6** | Assistents i agents per a gestió homologats i en marxa | 🟠 | — |
| **G7** | Formació EEDD/gestió completada (3 nivells) | ⬜ | — |
| **G8** | ★ LÍNIA GESTIÓ TANCADA | — | — |

**Tres nivells de formació en gestió**:

- **N1g** · IA genèrica (eines comunes per a gestió)
- **N2g** · marc + polítiques + protocols FJE
- **N3g** · solucions FJE per a gestió (assistents, agents, MAGINIA, Scriptorium)

### D · Línia docent

Cinc nivells de formació concatenats. Habilita la línia alumnat.

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **D1** | Difusió marc al claustre del centre | ⬜ | — |
| **D2** | Reserva de slots formatius al pla anual | ⬜ | **DEC-5** (DG centre) |
| **D3** | Formació N1d · IA genèrica | ⬜ | — |
| **D4** | Formació N2d · marc + polítiques + protocols FJE | ⬜ | — |
| **D5** | Formació N3d · solucions FJE (ATNE, CREATIVIA, MAGINIA) | ⬜ | — |
| **D6** | Formació N4d · desenvolupar CD alumnat amb IA (sobre + per a) | ⬜ | — |
| **D7** | Formació N5d · dissenyar activitats d'aula que incorporen IA (amb) | ⬜ | — |
| **D8** | Docents amb pràctica i capacitat formativa cap a companys | ⬜ | — |
| **D9** | ★ LÍNIA DOCENT TANCADA | — | — |

**Cinc nivells de formació docent**:

- **N1d** · IA genèrica
- **N2d** · marc + polítiques + protocols
- **N3d** · solucions FJE per a la docència
- **N4d** · desenvolupar CD alumnat amb IA (sobre i per a) — habilita línia S
- **N5d** · dissenyar activitats d'aula amb IA (amb) — habilita línia A

### S · Línia alumnat · sobre i per a (currículum vertical CD)

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **S1** | Currículum vertical CD amb IA dissenyat | ⬜ | **DEC-10**, **DEC-11** |
| **S2** | Activitats per curs alineades amb el currículum vertical | ⬜ | — |
| **S3** | Materials de suport per a alumnat | ⬜ | — |
| **S4** | Programacions de centre incorporen línia "sobre+per a" | ⬜ | **DEC-12** |
| **S5** | Pilot real amb alumnat | ⬜ | — |
| **S6** | Consolidació + integració curricular regular | ⬜ | — |

### A · Línia alumnat · amb IA (mediadora a l'aula)

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **A1** | Catàleg d'activitats amb IA classificat per àrea, etapa, finalitat | 🟡 | — |
| **A2** | Materials i assistents per a alumnat preparats | ⬜ | **DEC-13** |
| **A3** | Formació específica docents per a aplicació (continuació N5d) | ⬜ | — |
| **A4** | Programacions de centre integren ús "amb" | ⬜ | **DEC-12** |
| **A5** | Pilot real amb alumnat | ⬜ | — |
| **A6** | Consolidació | ⬜ | — |

### FAM · Línia famílies

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **FAM1** | Codi famílies v0 disponible | ✅ | — |
| **FAM2** | Difusió de criteris orientadors a famílies | ⬜ | — |
| **FAM3** | Codi famílies validat CDX (v.CDX) | ⬜ | **DEC-8** |
| **FAM4** | Model d'autoritzacions tipus aprovat | ⬜ | **DEC-9** |
| **FAM5** | Sessions informatives a famílies del centre | ⬜ | — |
| **FAM6** | Compromisos i autoritzacions signades al centre | ⬜ | — |

### E · Eines (transversal)

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **E1** | MAGINIA en producció (cascada + escenaris + dinàmiques) | ✅ | — |
| **E2** | ATNE en producció (pilot → producció) | 🟠 | — |
| **E3** | CREATIVIA prototip refet | ⬜ | **DEC-14** |
| **E4** | Assistent IA per a alumnat — prototip demostrable | ⬜ | **DEC-13** |
| **E5** | Scriptorium en producció (corpusFJE) | ✅ | — |
| **E6** | LAIA (agregador d'assistents institucionals) | ✅ | — |

### V · Avaluació i revisió

| Codi | Milestone | Estat | Decisions |
|------|-----------|-------|-----------|
| **V1** | Indicadors definits per cada línia (gestió, docent, alumnat) | ⬜ | — |
| **V2** | Primera onada de recollida d'indicadors | ⬜ | — |
| **V3** | Primera revisió periòdica del marc | ⬜ | — |

---

## 3. DEPENDÈNCIES — GRAF DEL CAMÍ

Visió compacta. Les decisions són **portes** (◆) que un òrgan ha d'obrir per habilitar el milestone següent.

```
                          ╔═══════════════════════╗
                          ║   F1  Marc tancat     ║
                          ║   F2  Polítiques v0 ✅║
                          ╚══════════╤════════════╝
                                     │
                          ┌──────────┴──────────┐
                          │                     │
                          ▼                     ▼
                   F3  Material           E1·E2·E5·E6
                   difusió EEDD           Eines base
                          │                  (paral·lel)
                          ▼
                    ◆ DEC-1 CDX
                   "Aval cicle de
                    desplegament"
                          │
                          ▼
                       F4 cicle
                     institucional
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
         G1 difusió   ◆ DEC-2     ◆ DEC-3
         criteris     (precal      mandat
         orientadors   consens     CSC ≈ F6
         a EEDD        DTD+DG)
              │           │
              │           ▼
              │       F5 figura
              │       enllaç IA
              │           │
              ▼           ▼
        F7 TROBADA INSTITUCIONAL EEDD ★
        (descobriment col·lectiu marc)
                          │
        ┌─────────────────┼─────────────────────────┐
        │                 │                         │
        ▼                 ▼                         ▼
   LÍNIA GESTIÓ      LÍNIA DOCENT             LÍNIA FAMÍLIES
        │                 │                         │
        ▼                 ▼                         ▼
   ◆ DEC-4           ◆ DEC-4 (mateixa)        FAM2 difusió
   DG centre         + ◆ DEC-5 (slots)        criteris
   designa enllaç    + ◆ DEC-6 (línia IA)     orientadors
        │                 │                         │
        ▼                 ▼                         ▼
    G2 enllaç         D1 difusió               (espera FAM3/4)
    designat          claustre                        │
        │                 │                          ▼
        ▼                 ▼                     ◆ DEC-8/9 CDX
   G3-G4-G5          D2 slots                  validació codi
   governança        reservats                 + autoritzacions
        │                 │                          │
        ▼                 ▼                          ▼
   G6 assistents      D3-D4-D5                 FAM5-FAM6
   gestió             (3 primers              sessions+signat
        │             nivells)
        ▼                 │
   G7 formació           ▼
   EEDD/gestió      ◆ DEC-10 CPe
        │           ("sobre/per a/amb")
        ▼                 │
   ★ G8 LÍNIA              ▼
   GESTIÓ            D6 N4d  ──────→   ┐
   TANCADA           D7 N5d  ──────→   │
                          │            │ habiliten
                          ▼            │ línia
                     D8 docents        │ alumnat
                     transmissors      │
                          │            │
                          ▼            ▼
                    ★ D9 LÍNIA      LÍNIA ALUMNAT
                    DOCENT TANCADA    ┌───┴───┐
                                      │       │
                                      ▼       ▼
                                  LÍNIA S    LÍNIA A
                                  (sobre+    (amb)
                                   per a)
                                      │       │
                              ◆ DEC-10/11    │
                              ◆ DEC-12       ◆ DEC-12/13
                                      │       │
                                      ▼       ▼
                                  S1→S2→S3   A1→A2→A3
                                      │       │
                                      ▼       ▼
                              ◆ DEC-12 (centre · DG + cap ped)
                                      │       │
                                      ▼       ▼
                                  S4 progr.   A4 progr.
                                      │       │
                                      ▼       ▼
                                  S5 pilot    A5 pilot
                                      │       │
                                      ▼       ▼
                                  S6 conso.   A6 conso.
                                      │       │
                                      └───┬───┘
                                          ▼
                                      V1 indicadors
                                      V2 recollida
                                      V3 revisió marc
```

---

## 4. DECISIONS CATALOGADES PER ÒRGAN

### CDX · Consell de Direcció de Xarxa

| Codi | Decisió | Habilita | Qui proposa |
|------|---------|----------|-------------|
| **DEC-1** | Aval del cicle de desplegament com a línia institucional de xarxa | F4 + tota la cascada | DG + tàndem tècnic |
| **DEC-2** | Aval de la figura "enllaç IA d'escola" (perfil + funció) | F5 → G2/D1 | Tàndem + DG (**consens previ requerit**) |
| **DEC-3** | Mandat al CSC per estudi de dedicació horària de la figura | F6 → viabilitat de G2 | Tàndem tècnic |
| **DEC-7** | Validació de les 4 polítiques institucionals (P1–P4) | F8 → desplegament normatiu | CPe i CSC |
| **DEC-8** | Validació del codi famílies | FAM3 → FAM5/FAM6 | CSC + responsable famílies |
| **DEC-9** | Model d'autoritzacions famílies | FAM4 → FAM6 | CSC + jurídic |

### CSC · Consell de Serveis Centrals

| Codi | Decisió | Habilita | Qui proposa |
|------|---------|----------|-------------|
| **DEC-15** | Contracte assessoria legal externa protecció dades | F9 → P3 v.CDX | Direcció TD |

### CPe · Consell Pedagògic

| Codi | Decisió | Habilita | Qui proposa |
|------|---------|----------|-------------|
| **DEC-10** | Estructura "sobre / per a / amb": 1, 2 o 3 línies | S1, D6, D7 | Direcció pedagògica xarxa |
| **DEC-11** | Etapa pilot per al currículum vertical CD | S1 → S2 | Direcció ped + grup homòlegs |
| **DEC-12** | Estratègia d'abast (big bang / pilot etapa / vertical / onades) | S4, A4 | Direcció pedagògica xarxa |
| **DEC-13** | Rol pedagògic de l'assistent IA per a alumnat | A2, E4 | Tàndem + experts |

### DG escola + cap pedagogia centre

| Codi | Decisió | Habilita | Qui proposa |
|------|---------|----------|-------------|
| **DEC-4** | Designació de la persona d'enllaç IA del centre | G2 → tota la cascada del centre | Decisió pròpia |
| **DEC-5** | Reservar slots formatius al pla anual | D2 → D3-D7 al centre | Decisió pròpia |
| **DEC-6** | Triar IA com a línia formativa anual | G4 + accés a 15h formatives | Decisió pròpia |

### Tàndem tècnic intern

| Codi | Decisió | Habilita | Qui proposa |
|------|---------|----------|-------------|
| **DEC-14** | Especificació CREATIVIA refet | E3 | Tàndem |
| **DEC-16** | Protocol de validació del corpusFJE | Manteniment corpus | Persona referent + voluntaris |

---

## 5. QUÈ POT AVANÇAR JA · independent de decisions institucionals

Aquestes peces no esperen ni el CDX ni la trobada EEDD. Es poden treballar en paral·lel:

| Bloc | Acció |
|------|-------|
| **F3** | Tancar materials i guies de difusió EEDD (kit) |
| **E2** | Tancar pas ATNE pilot → producció |
| **E3** | Especificar CREATIVIA refet |
| **A1** | Començar catàleg d'activitats amb IA (pool MAGINIA + pràctiques actuals) |
| **S1 (parcial)** | Dissenyar primer esbós del currículum vertical CD com a proposta màrtir |
| **G1 / FAM2** | Difondre criteris orientadors (no marc validat) als centres que ho demanin |
| **V1 (esbós)** | Llistar candidats a indicadors per línia |
| **F9** | Buscar 3 candidates d'assessoria legal protecció dades (no contractar encara) |

Quan arribi DEC-1 i F7, l'ecosistema ja és a punt.

---

## 6. RESUM EXECUTIU DEL CAMÍ

1. **Fonament a punt** (F1-F2-F3) — quasi tancat.
2. **Aval institucional** (DEC-1 al CDX) → habilita parlar de "cicle de desplegament" oficialment.
3. **Trobada EEDD** (F7) — única finestra col·lectiva de descobriment.
4. **Decisió per centre** (DEC-4/5/6) — cada DG tria si entra, com i amb qui.
5. **Cascada en 3 línies** — gestió primer (tanca aviat), docent en paral·lel (5 nivells), alumnat com a horitzó (S + A).
6. **Famílies, eines i avaluació** — branques transversals que s'integren als pilots.

El cicle es tanca quan **els tres cims** (alumnat aprèn · docents proposen · famílies suporten) tenen tot el que necessiten. Es construeix capa a capa, peça a peça, sense forçar dates fins que les decisions estiguin preses.

---

## DOCUMENTS COMPLEMENTARIS

Cal llegir conjuntament amb:

- **`M0_marc-general-ia.md`** — Document fundacional del marc. El full de ruta el desplega operativament.
- **`M0_marc-institucional-IA.md`** — Marc institucional FJE sobre IA.
- **`M8_GDPR-privacitat-centre.md`** · **`M8_etica-algoritmica-biaixos.md`** · **`M8_reglament-europeu-IA-RIA.md`** — Fonament normatiu de les decisions DEC-7, DEC-15.
- **`M5_marc-AIA-PCEK.md`** · **`M5_nivells-delegacio-mihia.md`** — Fonament pedagògic de la formació docent (D4-D7).
- **`M9_drets-alumnat.md`** · **`M9_decrets-inclusio-ordenacio.md`** — Fonament per a la validació de polítiques alumnat i famílies (DEC-7, DEC-8, DEC-9).

---

## FONTS

Document de planificació intern · Fundació Jesuïtes Educació · maig 2026.

Versió 0 · acrònica · per a discussió interna i preparació de la peça pública del kit ED.
