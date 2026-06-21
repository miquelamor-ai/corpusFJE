---
name: generate-tolc
description: 'Use when the teacher has activated the "tolc" complement. Generates
  a Transllenguatge/TOLC block: a bilingual anchor section that uses the student''s
  L1 as a cognitive bridge to Catalan. Includes vocabulary comparison, structural
  parallel, and a transfer prompt. Also integrates PBCS (Pedagogically-Based Code
  Switching) cues when appropriate. Only meaningful when newcomer profile is active
  with a known L1. At Emergent/pre-A1: oral recast prompts only — no written production.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: tolc
agent_role: complements
tools_required: []
triggers:
- path: params.complements.tolc
  equals: true
- path: profile.caracteristiques.nouvingut.l1
  exists: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-tolc.md
font_version: 4.0.0-canonic
generat_at: '2026-06-21'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: a50ac73d09c2b8b3
---

# Generar TOLC / transllenguatge — skill operativa per a LLM

El TOLC (Translation for Other Learning Contexts, Cummins) usa la **L1 de l'alumne com a pont cognitiu** cap al català. El complement genera un bloc estructurat en 5 parts: activació (pregunta comparativa), acarament (taula bilingüe L1↔català amb alfabet original), observació estructural (semblances primer, diferències com a curiositat), consigna de transferència (pont de producció), i clàusula de voluntarietat (mai exposar l'alumne). Complementat amb el **PBCS** (Pedagogically-Based Code Switching, alternança estratègica de codis), fa visible la diferència entre sistemes lingüístics.

**Tipologia MALL**: Mediació (transllenguatge actiu).
**HCL principals**: Comparar · Transferir · Reflexionar metalingüísticament.
**Principi rector — L1 com a recurs, no obstacle**: el TOLC materialitza el principi del MALL que totes les llengues de l'alumne son recursos cognitius. La L1 no és un problema a superar sinó un pont per construir. La Hipòtesi d'Interdependència de Cummins (2008) demostra que les competències de L1 transfereixen a L2 quan el pont es fa explícit.

**Activació condicional crítica**: el complement es genera ÚNICAMENT si:
1. El perfil de l'alumne té `nouvingut: true` actiu.
2. La L1 de l'alumne és **coneguda** (declarada al perfil).
Si la L1 no és declarada → es retorna advertència i no es genera el complement. Si el docent activa TOLC sense perfil nouvingut → el complement salta silenciosament.

**Alfabet original de la L1**: escriure les paraules en àrab, xinès, urdú, ciríl·lic, armeni o qualsevol altre alfabet en la seva forma original (no transliterada) és un acte de **reconeixement de la llengua de l'alumne**. La transliteració pot ser útil però no substitueix l'alfabet original.

**Principi de voluntarietat absoluta**: totes les consignes inclouen la clàusula "si vols, si pots" o equivalent. Mai exigir la L1 públicament. La taula bilingüe és personal. La consigna no exposa: "Si coneixes la paraula en una altra llengua, comparteix-ho si vols."

**PBCS — Alternança estratègica de codis**: el PBCS (diferent del transllenguatge espontani) fa visible la diferència entre sistemes lingüístics de manera controlada. L'alumne aprèn que les llengues no son traduccions literals les unes de les altres: l'ordre SVO, la posició de l'adjectiu, les construccions causals variam entre L1 i català. Aquesta consciència metalingüística accelera l'adquisició del català.

**Connexions MALL transversals:**
- *Semblances primer (principi pedagògic)*: l'observació estructural comença SEMPRE per les semblances entre L1 i català. "En la teva llengua i en català, les dues funcionen igual en aquest punt" és el millor punt de partida. Les diferències son interessants, no problemàtiques.
- *Taula bilingüe com a vocabulari actiu*: la taula no és per llegir — és per usar mentre es llegeix el text. L'alumne veu un terme difícil → consulta la taula → activa la xarxa semàntica en L1 → transfereix al català. Aquest procediment automatitza la transferència.
- *Consigna de transferència com a producció mediada*: a nivells inicials (dictat a l'adult, pre-A1/A1), la consigna de transferència és una forma de producció mediada. A nivells avançats (mediació complexa, B2-C1), és producció plena de mediació lingüística.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **bloc TOLC que es genera per a l'alumne nouvingut** (MEDIACIÓ PLURILINGÜE). **No descriu l'avaluació del docent ni la competència en L1**: el docent observa si l'alumne usa la taula durant la lectura i si la consigna de transferència li permet avançar.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → activació oral + assenyalar; `fase_lectora: alfabetica_emergent` → 1-2 paraules escrites en català.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Activació**
- Tipus de pregunta comparativa: Oral: "Com es diu X en la teva llengua?" — cap escriptura. El docent recull la resposta.

**2. Acarament (taula bilingüe)**
- Forma de l'acarament: Cap escriptura. Assenyalar o dibuixar el concepte.

**3. Observació estructural**
- Semblances primer: Cap observació: activitat oral i manipulativa.

**4. Consigna de transferència**
- Pont de producció: Oral mediat: "Dibuixa o assenyala mentre ho dius." Dictat a l'adult si l'alumne vol escriure.

**5. Caràcter voluntari**
- Protecció de l'alumne: Sempre voluntari. "Si vols, si pots." Cap exposició pública.

### A1 — Inicial


**1. Activació**
- Tipus de pregunta comparativa: Pregunta oral + pictograma: "Com es diu [paraula clau] en la teva llengua?" Resposta optional escrita.

**2. Acarament (taula bilingüe)**
- Forma de l'acarament: Taula 2 columnes: 3-5 parells paraula L1 (alfabet original) / paraula català.

**3. Observació estructural**
- Semblances primer: Cap observació a A1: massa càrrega metalingüística.

**4. Consigna de transferència**
- Pont de producció: Dictat a l'adult o assenyalar. "Pots dir-ho en veu alta si vols."

**5. Caràcter voluntari**
- Protecció de l'alumne: Sempre voluntari. La consigna no exposa l'alumne. La taula és personal.

### A2 — Funcional


**1. Activació**
- Tipus de pregunta comparativa: Activació escrita: "Com es diu «[concepte clau]» en la teva llengua?"

**2. Acarament (taula bilingüe)**
- Forma de l'acarament: Taula 2 columnes: 3-5 parells + 1 observació de semblança/diferència estructural senzilla.

**3. Observació estructural**
- Semblances primer: 1 frase positiva: semblances primer, diferències com a curiositat. Mai observació negativa.

**4. Consigna de transferència**
- Pont de producció: Frase curta: escriu en català una idea del text usant un connector de la taula (si vols, primer en L1).

**5. Caràcter voluntari**
- Protecció de l'alumne: Voluntari. Mai exigir L1 públicament. "Comparteix-ho si vols" sempre present.

### B1 — Estratègic


**1. Activació**
- Tipus de pregunta comparativa: Activació comparativa: "«[concepte]» en [L1] s'expressa com ___. En català usem ___. Qué observes?"

**2. Acarament (taula bilingüe)**
- Forma de l'acarament: Contrast de connectors i construccions causals L1↔català. Taula o paràgraf breu.

**3. Observació estructural**
- Semblances primer: Observació sobre construcció causal o estructural (ordre SVO, posició adjectiu, connectors).

**4. Consigna de transferència**
- Pont de producció: Paràgraf breu: resumir en L1 una part del text, o traduir una conclusió al català usant els connectors apressos.

**5. Caràcter voluntari**
- Protecció de l'alumne: Voluntari. Mediació accessible sense revelar la L1 si l'alumne no vol.

### B2 — Acadèmic


**1. Activació**
- Tipus de pregunta comparativa: Activació metalingüística: contrast de construccions gramaticals entre L1 i català.

**2. Acarament (taula bilingüe)**
- Forma de l'acarament: Contrast de l'organització del gènere entre L1 i català. Com s'estructura el text en cada llengua.

**3. Observació estructural**
- Semblances primer: Observació sobre l'organització del gènere entre les dues llengues. Gèneres similars i divergents.

**4. Consigna de transferència**
- Pont de producció: Mediació complexa: mediar un text complet entre L1 i català. Comparar l'organització de les idees.

**5. Caràcter voluntari**
- Protecció de l'alumne: Voluntari. L'alumne pot triar fer la mediació en L1 o directament en català.

### C1+ — Crític


**1. Activació**
- Tipus de pregunta comparativa: Activació crítica: contrast entre sistemes lingüístics i convencions culturals del gènere discursiu.

**2. Acarament (taula bilingüe)**
- Forma de l'acarament: Contrast d'intenció comunicativa i convencions retòriques entre L1 i català. Biaix cultural del gènere.

**3. Observació estructural**
- Semblances primer: Observació crítica sobre com les dues llengues codifiquen el coneixement de forma diferent. Convencions retòriques.

**4. Consigna de transferència**
- Pont de producció: Contrast escrit: analitza com el gènere treballat es construiria diferent en L1 i en català.

**5. Caràcter voluntari**
- Protecció de l'alumne: Voluntari. L'alumne decideix el grau d'integració de la seva L1 en l'anàlisi crítica.

