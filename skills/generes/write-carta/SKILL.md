---
name: write-carta
description: 'Use when adapting or generating a carta for students. Activates when
  genre_discursiu == "carta". Applies motive-first structure, single concrete petition,
  and register adjusted to addressee. Output: carta in markdown with header, greeting,
  motive, body, petition, farewell, and signature.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: carta
tipologia: Argumentativa / Dialogada
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
  equals: carta
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-carta.md
font_version: 4.0.0-canonic
generat_at: '2026-06-06'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: d665eb4e9c28a9c3
---

# Escriure/adaptar una carta — skill operativa per a LLM

La carta és un text comunicatiu adreçat a un **destinatari específic** amb estructura convencional de 7 parts. El seu tret definitori és la doble exigència: el **motiu al primer paràgraf** (sense preàmbuls) i la **única petició per carta** (una demanda, una acció esperada del destinatari). El registre —formal o informal— és determinat exclusivament per la relació entre remitent i destinatari i ha de ser consistent en tot el text.

**Tipologia MALL**: Argumentativa/Comunicativa (carta formal) · Expressiva/Narrativa (carta informal).
**HCL principal**: Justificar — carta formal B1+: argumentar la petició amb raons ordenades · Narrar+Descriure — carta informal A1-A2: explicar la situació i demanar de forma directa.
**HCL secundàries**: Argumentar (anticipació d'objeccions, B2+) · Persuadir retòricament (C1).
**No s'adapta a pre-A1**: la carta requereix la comprensió del **destinatari com a constructor de registre** — saber que "Hola" vs "Benvolgut" depèn de la relació social és una abstracció sociolingüística que requereix comprensió del context comunicatiu com a variació conscient. (Decisió 6 canònica Fase B.)
**Translanguaging (A1-A2)**: la carta personal (informal) a A1-A2 pot incloure expressions en L1 entre claudàtors si l'alumne no troba el mot en llengua de destinació. El docent valora el contingut separat de la forma. No s'aplica a la carta formal.

**Connexions MALL transversals:**
- *Registre com a competència sociolingüística*: saber quan usar "tu" o "vostè", "Hola" o "Benvolgut", és una competència de relació social visible i avaluable. La carta és el gènere on la variació de registre és més explícita i on l'error de registre té conseqüències comunicatives reals.
- *El motiu al primer paràgraf com a claredat comunicativa*: comunicar el propòsit de manera directa és una competència professional i acadèmica transferible a correus electrònics, instàncies i sol·licituds. La carta ensenya a evitar les introduccions que retarden el missatge.
- *Una sola petició com a focus comunicatiu*: la regla "una carta = una petició" és una heurística de comunicació formal exportable a totes les situacions professionals. L'alumne que aprèn a no acumular demandes aprèn a pensar comunicativament amb focus: saber quin és el "desig principal" és una competència de síntesi i priorització.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu la **carta adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Encapçalament**
- Format i completitud: Lloc i data en format simple: "Barcelona, 12 de maig".

**2. Salutació**
- Registre i adequació: "Hola [nom]," (informal) / "Estimat/da [nom]:" (formal molt simple).

**3. Motiu al primer paràgraf**
- Claredat i posició: 1 frase que diu per qué s'escriu: "T'escric per..." Sense preàmbuls.

**4. Una sola petició**
- Focus i concreció: 1 petició molt simple: "Et demano que..." Sense acumulació de demandes.

**5. Registre**
- Consistència i adequació: Informal (amic/família) o formal molt simple (desconegut). Consistent en tot el text.

**6. Criteris transversals**
- Comiat i signatura: "Fins aviat, [nom]." (informal) / "Salutacions, [nom]." (formal). Consistent amb la salutació.
- Fórmules arcaiques: Cap fórmula arcaica. Si apareix al text font, s'actualitza.
- Fidelitat al text font: Fidelitat al motiu principal i al registre bàsic.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit a qui va la carta i per qué. He fet una sola petició. He signat."

### A1 — Inicial


**1. Encapçalament**
- Format i completitud: Lloc, data i nom del destinatari complets.

**2. Salutació**
- Registre i adequació: Salutació ajustada al registre: informal (amic/família) / formal (autoritat/desconegut).

**3. Motiu al primer paràgraf**
- Claredat i posició: Motiu explícit al primer paràgraf. Directe i clar. Cap introducció sobre el benestar del destinatari.

**4. Una sola petició**
- Focus i concreció: 1 petició clara i directa. Sense preguntes múltiples ni demandes encadenades.

**5. Registre**
- Consistència i adequació: Distinció clara entre formal i informal. Registre consistent. Cap barreja.

**6. Criteris transversals**
- Comiat i signatura: Comiat ajustat al registre. Nom complet a la carta formal.
- Fórmules arcaiques: Idem. Cap fórmula arcaica ni expressió obsoleta.
- Fidelitat al text font: Fidelitat al motiu, al registre i a la petició essencial.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He posat salutació i comiat adequats al destinatari. He dit el motiu al principi."

### A2 — Funcional


**1. Encapçalament**
- Format i completitud: Encapçalament complet: lloc, data, nom i adreça del destinatari (carta formal).

**2. Salutació**
- Registre i adequació: Salutació formal precisa: "Benvolgut/da senyor/a [cognom]:" sense errors de tractament.

**3. Motiu al primer paràgraf**
- Claredat i posició: Motiu presentat amb connector introductori: "Em dirigeixo a vostè per informar-lo/la que..."

**4. Una sola petició**
- Focus i concreció: Petició formulada amb justificació breu: "Li demano que... ja que..."

**5. Registre**
- Consistència i adequació: Registre formal o informal consistent. Vostè vs. tu ajustat al destinatari en tot el text.

**6. Criteris transversals**
- Comiat i signatura: Comiat formal: "Atentament," / informal: "Una salutació,". Signatura completa (nom i cognoms).
- Fórmules arcaiques: Idem. Fórmules de cortesia contemporànies.
- Fidelitat al text font: Fidelitat al motiu, al registre, a la petició i a l'estructura de 7 parts.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He usat el registre correcte (formal/informal). He fet una sola petició amb justificació."

### B1 — Estratègic


**1. Encapçalament**
- Format i completitud: Encapçalament complet i ben formatat. Referència o assumpte si escau.

**2. Salutació**
- Registre i adequació: Salutació formal amb tractament correcte i consistent amb el to de la carta.

**3. Motiu al primer paràgraf**
- Claredat i posició: Motiu presentat amb context breu i connector formal. El lector sap per qué s'escriu a la primera frase.

**4. Una sola petició**
- Focus i concreció: Petició argumentada: context + raó + demanda concreta. Anticipació possible: "Sóc conscient que..."

**5. Registre**
- Consistència i adequació: Registre formal sofisticat. Cap expressió col·loquial a la carta formal.

**6. Criteris transversals**
- Comiat i signatura: Comiat protocol·lari adequat al registre i al to de la carta.
- Fórmules arcaiques: Idem. Pot usar fórmules formals però no antiquades.
- Fidelitat al text font: Fidelitat a la complexitat argumentativa i al to del remitent.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva carta té context, petició argumentada i registre consistent de principi a fi."

### B2 — Acadèmic


**1. Encapçalament**
- Format i completitud: Encapçalament professional complet. Pot incloure referència, assumpte i número d'expedient.

**2. Salutació**
- Registre i adequació: Salutació formal o protocol·lària si el context ho exigeix. Tractament perfectament ajustat.

**3. Motiu al primer paràgraf**
- Claredat i posició: Motiu presentat amb precisió i context necessari per al destinatari. Pot incloure referència a una comunicació prèvia.

**4. Una sola petició**
- Focus i concreció: Petició amb argumentació elaborada i recursos de persuasió (empatia, reciprocitat).

**5. Registre**
- Consistència i adequació: Registre adaptat amb matisos de cortesia i protocol. El to és inequívocament professional o personal.

**6. Criteris transversals**
- Comiat i signatura: Comiat i signatura professionals. Pot incloure càrrec, institució o funció del remitent.
- Fórmules arcaiques: Idem. Registre professional actual, sense arcaismes.
- Fidelitat al text font: Fidelitat a la complexitat, al to i als recursos retòrics del text original.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva carta és professional, ben estructurada i usa recursos de persuasió adequats al destinatari."

### C1+ — Crític


