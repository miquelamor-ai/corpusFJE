---
name: write-conte
description: 'Use when adapting or generating a conte (short story) for students.
  Activates when genre_discursiu == "conte". Applies linear chronology, explicit motivations,
  named emotions, and attributed dialogue. Output: conte in markdown with initial
  situation, conflict, and resolution.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: conte
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
  equals: conte
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-conte.md
font_version: 4.0.0-canonic
generat_at: '2026-05-26'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 07daf08075549d72
---

# Escriure/adaptar un conte — skill operativa per a LLM

El conte és un gènere narratiu breu amb estructura de cinc parts (situació inicial, conflicte, seqüència d'esdeveniments, clímax i resolució). La seva funció pedagògica és treballar la **HCL Narrar**: seqüenciar fets causalment, presentar personatges amb motivació i emoció explícites, i tancar el relat amb una resolució coherent. És el gènere "porta" a la ficció literària per la universalitat de la seva estructura.

**Tipologia MALL**: Narrativa (imaginar — construir mons possibles).
**HCL principal**: Narrar — seqüenciar fets causalment, presentar personatge amb conflicte i resolució.
**HCL secundàries**: Descriure context i personatges (A2+) · Interpretar motivacions i emocions (B1+) · Valorar intenció estètica i literarietat (B2+).
**Pre-A1 (Emergent)**: Oral i gestual — narració mediada per l'adult amb seqüència d'imatges.

**Connexions MALL transversals:**
- *Translanguaging / TOLC*: a pre-A1 i A1, l'alumne pot narrar oralment en L1 i l'adult fa el pont al català. Al text adaptat, paraules en L1 entre claudàtors `[...]` mantenen el fil narratiu quan el terme en català és opac.
- *Multimodalitat*: a pre-A1 i A1, les il·lustracions seqüenciades sostenen la narració i bastiden la cronologia. L'ordre visual és la bastida de la seqüenciació temporal.
- *Eix oral/escrit*: el conte es treballa primer oralment (narrar en veu alta) i després es passa a la producció escrita. Recomanat fins a A2.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **conte adaptat per a la LECTURA** de l'alumne (el que el docent presenta perquè l'alumne llegeixi). **No descriu la producció autònoma de l'alumne** — la producció narrativa de l'alumne s'avalua amb un derivat propi (rúbrica d'avaluació formativa). Principi pedagògic MALL: l'alumne llegeix models bons al màxim del seu abast i en produeix els seus textos; l'adaptació és tasca del docent.
**Sub-granularitat dins de pre-A1 i A1**: es treballa amb la variable independent `fase_lectora` del frontmatter (logografica · alfabetica_emergent · alfabetica_fluida), no amb columnes addicionals.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Situació inicial**
- Personatges i context: Adult narra. L'alumne assenyala el personatge principal a la imatge.

**2. Conflicte**
- Obstacle i causa: Adult explica el problema. L'alumne escolta i assenyala la imatge del conflicte.

**3. Seqüència d'esdeveniments**
- Ordre i causalitat: 2-3 imatges amb una frase oral per imatge. L'adult transcriu si l'alumne dicta.

**4. Clímax**
- Punt de màxima tensió: L'adult assenyala el moment de tensió. L'alumne el reconeix ("aquí és on tot va malament").

**5. Resolució**
- Coherència i tancament: L'adult llegeix la resolució. L'alumne identifica si ha anat bé o malament.

**6. Emocions nomenades**
- Varietat i situació: Cap escriptura d'emocions. L'adult pot preguntar oralment "Com es sent?"

**7. Diàleg**
- Atribució i funció: Sense diàleg escrit. L'adult pot dramatitzar les veus oralment.

**8. Criteris transversals**
- Cronologia: Imatges en ordre. L'adult sostè la seqüència.
- Temps verbals: L'adult usa el passat simple. L'alumne imita.
- Fidelitat al text font: Fidelitat al personatge i l'acció nuclear (qui, on, què passa).

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He vist les imatges i he dit el que passa a cada una." (oral, mediat per l'adult)

### A1 — Inicial


**1. Situació inicial**
- Personatges i context: 1 personatge + 1 lloc en 1-2 frases. Sense descripció de trets.

**2. Conflicte**
- Obstacle i causa: 1 problema en 1 frase. "El lleó té gana però no hi ha menjar."

**3. Seqüència d'esdeveniments**
- Ordre i causalitat: 2-3 frases de fets en ordre cronològic. Sense connectors causals obligatoris.

**4. Clímax**
- Punt de màxima tensió: 1 frase sobre el moment decisiu. Visual i inequívoc.

**5. Resolució**
- Coherència i tancament: 1 frase de resolució. Positiva o negativa, clara i inequívoca.

**6. Emocions nomenades**
- Varietat i situació: 1 emoció nomenada en un moment clau. Vocabulari bàsic ("content", "trist", "tenia por").

**7. Diàleg**
- Atribució i funció: Sense diàleg o 1 frase molt simple, clarament atribuïda.

**8. Criteris transversals**
- Cronologia: Ordre temporal clar. No flashbacks.
- Temps verbals: Passat simple consistent. Cap barreja amb present.
- Fidelitat al text font: Fidelitat al personatge, l'acció i el final.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit qui és el personatge, on és i què li passa. He escrit el final."

### A2 — Funcional


**1. Situació inicial**
- Personatges i context: 1-2 personatges amb un tret cadascun. Lloc en 1 frase de context.

**2. Conflicte**
- Obstacle i causa: Conflicte clar: el personatge vol X però hi ha un obstacle. Causa no obligatòria.

**3. Seqüència d'esdeveniments**
- Ordre i causalitat: 3-4 frases ordenades amb connectors temporals simples ("primer", "després", "llavors").

**4. Clímax**
- Punt de màxima tensió: El moment de màxima tensió es pot identificar clarament al text.

**5. Resolució**
- Coherència i tancament: Resolució en 1-2 frases. Coherent amb el conflicte plantejat.

**6. Emocions nomenades**
- Varietat i situació: 1-2 emocions nomenades situades en moments clau del conte.

**7. Diàleg**
- Atribució i funció: 1-2 torns de diàleg atribuïts per nom ("En Marc va dir: '...'"). Diàleg informatiu.

**8. Criteris transversals**
- Cronologia: Connectors temporals garanteixen l'ordre. No flashbacks.
- Temps verbals: Passat simple consistent. Imperfet per a descripcions ("era", "tenia").
- Fidelitat al text font: Fidelitat al personatge, l'acció, el conflicte i el final.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu conte té un problema i un final. He nomenat com se sent el personatge."

### B1 — Estratègic


**1. Situació inicial**
- Personatges i context: 1-2 personatges amb tret i desig inicial clars. Lloc amb ambient breu.

**2. Conflicte**
- Obstacle i causa: Conflicte amb causa explícita. L'obstacle és comprensible per al lector.

**3. Seqüència d'esdeveniments**
- Ordre i causalitat: 3-4 esdeveniments amb connectors variats (temporals + causals). Causa i efecte explícits.

**4. Clímax**
- Punt de màxima tensió: Clímax marcat amb connector de contrast ("però", "de sobte"). Tensió nomenada.

**5. Resolució**
- Coherència i tancament: Resolució que connecta causalment amb el conflicte (com s'ha resolt).

**6. Emocions nomenades**
- Varietat i situació: 2-3 emocions variades situades en el moment de l'acció. Connexió causa-emoció explícita.

**7. Diàleg**
- Atribució i funció: 2-3 torns de diàleg atribuïts que fan avançar la trama. Veus diferenciades per nom.

**8. Criteris transversals**
- Cronologia: Cronologia lineal estricta. Connectors causals i temporals variats. No flashbacks.
- Temps verbals: Passat simple + imperfet correctes. Pluscuamperfet bàsic admissible.
- Fidelitat al text font: Fidelitat al conflicte, la seqüència principal i el to general.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit els 5 moments del conte en ordre. He explicat per què el personatge fa el que fa."

### B2 — Acadèmic


**1. Situació inicial**
- Personatges i context: Personatges amb motivació explícita. Context temporal i espacial integrat al relat.

**2. Conflicte**
- Obstacle i causa: Conflicte amb dimensió emocional. La causa s'explicita i impacta el personatge.

**3. Seqüència d'esdeveniments**
- Ordre i causalitat: Seqüència de 4-5 actes amb causa-efecte i tensió creixent cap al clímax.

**4. Clímax**
- Punt de màxima tensió: Clímax amb emoció nomenada del personatge + acció decisiva. Tensió crescuda gradualment.

**5. Resolució**
- Coherència i tancament: Resolució amb reflex emocional del personatge. Final tancat amb matís moderat.

**6. Emocions nomenades**
- Varietat i situació: Emocions integrades al text sense aparèixer llistades. Matisades i variades.

**7. Diàleg**
- Atribució i funció: Diàleg que revela caràcter o conflicte. Format narratiu o teatral ben marcat.

**8. Criteris transversals**
- Cronologia: Cronologia lineal. Pot incloure una pausa narrativa breu (aturada reflexiva).
- Temps verbals: Temps narratius consistents. Usos elaborats del pluscuamperfet.
- Fidelitat al text font: Fidelitat al matís emocional, el to i les relacions entre personatges.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu conte té tensió creixent i resolució coherent. Les emocions estan integrades al text, no llistades."

### C1+ — Crític


**1. Situació inicial**
- Personatges i context: Personatges complexos amb motivació i tensió interna. Context ric i funcional per a la trama.

**2. Conflicte**
- Obstacle i causa: Conflicte complex: pot incloure tensions morals, dilemes o contradicció interna del personatge.

**3. Seqüència d'esdeveniments**
- Ordre i causalitat: Seqüència causal elaborada. Cada acte prepara el clímax. Pot incloure paral·lelisme o recursivitat.

**4. Clímax**
- Punt de màxima tensió: Clímax amb decisió moral, reversió o canvi de perspectiva. Pot incloure ironia si el context ho justifica.

**5. Resolució**
- Coherència i tancament: Resolució oberta, irònica o ambigua si el context literari ho requereix. Ha de ser significativa.

**6. Emocions nomenades**
- Varietat i situació: Emocions complexes o contradictòries. Descripció interior del personatge possible.

**7. Diàleg**
- Atribució i funció: Diàleg amb subtext: el que es diu i el que es vol dir. Pot incloure ironia o doble sentit.

**8. Criteris transversals**
- Cronologia: Cronologia lineal o anacronia marcada intencionadament i clara per al lector.
- Temps verbals: Domini complet dels temps narratius. Pot usar present narratiu com a recurs estilístic.
- Fidelitat al text font: Fidelitat a la veu narrativa, el to, els recursos literaris i la intenció estètica.

**9. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu conte té personatges complexos, clímax ben construït i resolució significativa. He revisat que la veu narrativa sigui consistent."

