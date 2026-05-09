---
title: "Guia d'estil — Veu del corpus FJE"
version: 1.0
data: 2026-05-08
status: vigent
---

# Guia d'estil — Veu del corpus FJE

## Principi

El corpus pedagògic FJE s'escriu en **veu genèrica**. Ha de ser vàlid tant per a un docent que el llegeix directament com per a un assistent IA que el recupera via RAG, com per a qualsevol acompanyant de l'alumnat (tutors, famílies, mentors, equips d'orientació).

**No** es dirigeix a "l'assistent", "la IA" ni "l'agent" com a interlocutor.

### Per què

1. El coneixement pedagògic és **agnòstic respecte a qui l'aplica**. Una bona estratègia per a un alumne nouvingut funciona igual la faci un docent o un assistent IA.
2. **Reduïm fricció** amb docents reticents a la IA: si el corpus parla en termes d'IA, sembla "no és per a ells".
3. **Multipliquem la utilitat** del mateix corpus.

### El que NO és aquesta guia

No és una capa de seguretat. Si un assistent no ha de fer una cosa, això es resol al **system prompt de l'assistent**, no contaminant el corpus.

---

## Excepcions — on SÍ que es parla d'IA / assistents / agents

Aquests documents tenen l'IA com a **tema substantiu** i mantenen la terminologia:

- **M5 — Tecnopedagogia** (tots els fitxers).
- **M8 — Ètica IA i seguretat** (tots els fitxers).
- **`M0_glossari-ignasia-IA.md`** (glossari específic).
- **`M6_avaluacio-competencial-AIA.md`** (avaluació amb IA).
- **`marc-general-ia-esborrany.md`** (marc institucional sobre IA).
- Documents que parlin específicament de **com integrar eines IA** al flux pedagògic.

---

## Substitucions canòniques

Aquests són els patrons recurrents detectats al corpus i com reescriure'ls.

### 1. Capçaleres i marcadors d'activació

| Original | Reescriptura |
|---|---|
| `Heurístiques per a l'Agent DOCENT` | `Heurístiques per al docent` |
| `Heurístiques per a l'Agent ALUMNE` | `Heurístiques per a l'alumne` |
| `Heurístiques i raonament per a l'agent` | `Heurístiques i raonament pedagògic` |
| `L'agent ha d'activar aquest document quan...` | `Aquest document és pertinent quan...` |
| `Senyals del docent` (per activar l'agent) | `Senyals del docent` (es pot mantenir, és genèric) |
| `Co-activació obligatòria: ...consultar...` | `Documents complementaris: cal llegir conjuntament...` |

### 2. Prescripcions

| Original | Reescriptura |
|---|---|
| `L'agent ha de promoure...` | `Cal promoure...` o `Convé promoure...` |
| `L'assistent ha de preguntar...` | `Convé preguntar...` o `Una pregunta útil és...` |
| `L'agent intervindrà quan...` | `Cal intervenir quan...` |
| `L'IA ha de detectar...` | `Cal detectar...` o `Senyals a detectar:...` |
| `L'agent oferirà...` | `Es pot oferir...` |

### 3. Davant situacions de l'alumnat

| Original | Reescriptura |
|---|---|
| `Davant d'un alumne que diu X, l'assistent ha de Y` | `Davant d'un alumne que diu X, una resposta adequada és Y` |
| `Si l'alumne mostra X, l'agent...` | `Si l'alumne mostra X, convé...` |

### 4. Subjectes genèrics utilitzables

Per donar agència visible sense decantar-se per docent o IA:

- **"l'acompanyant"** — neutre, vàlid per a docent, tutor, mentor, IA.
- **"qui ensenya"** / **"qui acompanya"** — focus en l'acció.
- **"l'adult de referència"** — quan implica responsabilitat humana directa.
- **"la persona educadora"** — formal, s'usa en documents normatius.
- **"l'equip docent"** — quan és col·lectiu.

### 5. Veu impersonal (passiva i infinitius)

Quan l'agència no és essencial:
- `Cal X.` / `Convé X.` / `És recomanable X.`
- `Una bona pràctica és X.`
- `S'aconsella X quan...`

⚠️ **Evitar passives buides** del tipus *"s'ha de fer"* sense complement. Si la frase no té sentit sense un actor, posa-li agència.

---

## Mediació humana explícita

Quan una acció **només** la pot fer un humà — no és intercanviable amb una eina — cal dir-ho al text. Exemples:

- Decisions d'avaluació final amb conseqüències acadèmiques.
- Contenció emocional intensa o crisi.
- Contacte i acompanyament a famílies.
- Observació longitudinal de l'alumne.
- Coordinació amb serveis externs (EAP, CSMIJ, serveis socials).

**Fórmules útils:**
- `Aquesta decisió correspon al docent / a l'equip docent.`
- `Requereix la mediació d'un adult de referència.`
- `No és delegable a una eina; cal una persona educadora.`

**No** cal marcar el cas contrari (no cal dir "això es pot fer amb una eina"). Per defecte, tot és delegable a qui el sistema concret permeti.

---

## Falsos positius — NO tocar

Aquestes paraules apareixen al corpus amb sentit **no-IA** i s'han de preservar:

- **"agents educatius"** = professionals humans (docents, EAP, tutors, orientadors...).
- **"agents socials"** = entitats, serveis socials, comunitat.
- **"agent humà"** o **"agents humans"** (rar però possible).
- **"l'alumne és agent del seu aprenentatge"** = l'alumne com a subjecte actiu.
- **"agents de canvi"** = persones o col·lectius que transformen.
- **"IA"** dins de sigles no relacionades (cap detectada al corpus actual, però atenció).

**Test**: si pots substituir "agent" per "assistent IA" i la frase queda absurda → és un fals positiu. No tocar.

---

## Casos límit — preguntar abans d'editar

- Documents del **GRUP C** (mixtos): `M2_carrega-friccio-cognitiva.md`, `M2_models-disseny-instruccional.md`. Aquí l'IA és tema substantiu en alguns chunks i terminologia inadequada en d'altres. **Decisió chunk a chunk.**
- **`AAU_system_prompt_diversitat.md`**: és un system prompt, no contingut pedagògic. Probablement s'ha de moure fora del corpus.
- Mencions a **noms propis d'eines** (ChatGPT, Gemini, Claude, ATNE, AAU, LAIA, etc.): **regla per defecte = NO mencionar**. Les eines canvien de nom amb el temps; els documents del corpus no han de quedar lligats a un nom concret. Substituir per *"el sistema"*, *"la pipeline RAG"*, *"l'eina d'adaptació"*, *"aquest sistema"* o reformulació impersonal. Excepcions: quan el document parla **literalment** d'una eina específica per nom (ex. una guia operativa d'una eina concreta) i es vol que aquesta referència sigui explícita.

---

## Test ràpid de revisió

Llegint un chunk genericitzat, fes-te aquestes preguntes:

1. ¿Funcionaria si qui ho llegeix és un docent humà?
2. ¿Funcionaria si qui ho llegeix és un assistent IA?
3. ¿Funcionaria si qui ho llegeix és un tutor familiar?
4. Si la resposta a alguna és **no**, ¿és perquè l'acció realment requereix una persona? → fer-ho explícit amb "correspon al docent".
5. ¿He perdut precisió o accionabilitat respecte a l'original? → recuperar-la amb un subjecte genèric ("l'acompanyant", "qui ensenya"), no amb passives buides.

---

## Aplicació

- **Lots de revisió**: per mòduls, validats per Miquel abans de commit.
- **Versionat**: cada lot, un commit amb missatge clar (`refactor(M1): veu genèrica — ...`).
- **Reversible**: el git permet desfer qualsevol lot que no convingui.
