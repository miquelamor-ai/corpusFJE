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

---

## Addenda 2026-05-31 — Anti-apropiació del carisma ignasià

Aquesta addenda formalitza dues regles editorials sobre l'ús del vocabulari ignasià al corpus. Emergeix de la sessió de treball amb Itinerarium (briefing 03 d'Itinerarium, decisions C.1 i C.2). Aplica a tot el corpus i complementa la regla general de veu genèrica.

### Regla 1 — Els conceptes ignasians són actituds, no tècniques

Conceptes com **cura personalis**, **magis**, **discerniment**, **examen**, **contemplatiu en l'acció** són **principis i actituds del *modus operandi*** que han d'inspirar la pràctica, **NO etiquetes intercanviables per a tècniques concretes**.

**Prohibit**:
- Anomenar una dinàmica concreta com a "Cura Personalis", "Magis" o "Discerniment".
- Dir que una graella d'observació és "El meu examen ignasià".
- Etiquetar una metodologia operativa amb nom espiritual ("La sessió Cura Personalis").

**Per què**: instrumentalitzar el carisma el **buida**. Si "Cura Personalis" passa a ser el nom d'una tècnica concreta, perd la seva capacitat d'orientar tota la pràctica i es converteix en una eina substituïble. La pràctica perd l'horitzó i el concepte perd substància.

**Permès i recomanat**:
- "La sessió cultiva la cura personalis com a actitud, que es manifesta en escoltar de debò i fer-se present a cada alumne."
- "El docent es pregunta des del seu examen quotidià com millorar la pràctica."
- "Aquesta proposta s'arrela en el principi del *magis*: no aspirem al mínim, sinó al servei més complet possible."

### Regla 2 — No "ignasià" allò que és universal

Pràctiques pedagògiques d'origen no ignasià (Lesson Study, observació entre iguals, comunitats professionals d'aprenentatge, anàlisi col·laborativa de casos, mapa d'empatia, DAFO, etc.) són **universals**. Es poden inscriure dins una sensibilitat ignasiana, però no es transformen en pràctiques ignasianes pel fet d'usar-les en un centre FJE.

**Prohibit**:
- Anomenar "Lesson Study ignasià" o "DAFO ignasià" una dinàmica concreta.
- Atribuir origen ignasià a marcs que en tenen d'altres (Hattie, Wiliam, DuFour, Cummins...).
- Suggerir que el sentit de la dinàmica només existeix dins el marc ignasià.

**Per què**: confondre origen i adopció genera confusió epistèmica i fa el discurs **no creïble**. Una observació entre iguals és bona pràctica perquè és bona pràctica, no perquè sigui ignasiana. La inspiració ignasiana s'expressa en **com s'adopta** —amb quina actitud, des de quin horitzó, amb quina cura— no en **canviar-ne el nom**.

**Permès i recomanat**:
- "Un docent ignasià hi reflexiona des de l'horitzó del *magis* i la cura personalis."
- "Aquesta pràctica universal s'inscriu de manera natural al *modus operandi* ignasià pel valor que dóna al discerniment comunitari."
- "L'equip FJE adopta el Lesson Study amb l'actitud reflexiva pròpia de la tradició ignasiana, sense renomenar la pràctica."

### Casos d'aplicació al corpus

- **[M0_PPI-paradigma-pedagogic-ignasia.md](../M0_PPI-paradigma-pedagogic-ignasia.md)**, **[M0_cura-personalis.md](../M0_cura-personalis.md)**, **[M0_magis-i-servei.md](../M0_magis-i-servei.md)** — Aquests són els docs **font del concepte** ignasià. La seva veu és normativa: descriuen què és cada concepte i la seva tradició.
- **[M7_desenvolupament-professional-docent.md](../M7_desenvolupament-professional-docent.md)** — Aquest doc cita la inspiració ignasiana sense apropiar-se de tècniques (CPA = universal, Lesson Study = universal, A-D-D = inspirat).
- **Marcs operatius (M2, M3, M5, M6, M7 que no són M0)** — Mencionen el carisma com a horitzó actitudinal, no com a etiqueta de tècniques.
- **`tipus: instrument`, `tipus: protocol`, skills (`*.md`)** — En cap cas porten nom de concepte ignasià. Les eines i protocols són operatius; la inspiració ignasiana està a l'actitud de qui les usa.

### Test ràpid d'anti-apropiació

Davant la temptació d'usar vocabulari ignasià al títol d'una dinàmica, un protocol o un instrument, pregunta't:

1. **Substituible?** ¿Aquesta dinàmica/protocol/eina podria ser substituïda per una altra de funció equivalent i el sentit es mantindria? Si sí, no és el concepte ignasià: és una tècnica. **No la nominis amb el concepte.**
2. **Funcional?** ¿La pràctica és funcional pel concepte que la nomena o per la seva pròpia evidència empírica? Si funciona per evidència empírica (Hattie, Wiliam, DuFour...), el seu origen és aquest. **El nom ha de fer honor a l'origen.**
3. **Reversible?** ¿Si traguéssim el nom ignasià, la pràctica continuaria sent vàlida? Si sí, el nom era ornamental. **Treu-lo i fes explícita l'actitud que volies senyalar.**

Aquestes regles són complementàries a la veu genèrica del corpus i a la regla de no citar noms propis d'eines: el carisma ignasià també es preserva amb un ús precís del seu vocabulari.
