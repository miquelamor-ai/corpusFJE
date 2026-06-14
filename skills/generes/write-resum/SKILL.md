---
name: write-resum
description: 'Use when adapting or generating a resum for students. Activates when
  genre_discursiu == "resum". Applies main-idea-first structure, logical connectors,
  and reformulation with accessible vocabulary. Output: resum in markdown with title,
  reference, and main/secondary ideas.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: resum
tipologia: Expositiva
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
  equals: resum
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-resum.md
font_version: 4.0.0-canonic
generat_at: '2026-06-14'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: d6ba1ea0a1bdf465
---

# Escriure/adaptar un resum — skill operativa per a LLM

El resum és un text secundari que condensa un text font mantenint les idees principals, la seva relació lògica i la veu original de l'autor. El seu tret definitori és la **fidelitat + reformulació**: el resum no interpreta ni afegeix opinió pròpia, però tampoc copia — reformula amb vocabulari accessible. A diferència del **resum graduat** (complement de mediació que crea un marc amb forats per omplir), el resum com a gènere és un text acabat i complet.

**Tipologia MALL**: Expositiva (text secundari).
**HCL principal**: Explicar — seleccionar la idea principal del text font, sintetitzar les idees secundàries i presentar-les de manera coherent i condensada, preservant la lògica de l'autor original.
**HCL secundàries**: Descriure (si el text font és descriptiu) · Narrar (si el text font és narratiu) — el resum adapta la seva HCL secundària al gènere del text font que condensa.
**Nota MALL**: resumir implica primer recapitular oralment ("de qué tracta?") i llavors produir el text escrit condensat. La recapitulació oral (A1-A2) és la bastida de la producció escrita.
**No s'adapta a pre-A1**: el resum escrit requereix selecció autònoma de la idea principal del text font i reformulació (no còpia). Aquesta doble operació — identificar la jerarquia informativa i parafrasear — requereix base lecto-escriptora mínima i comprensió del text font com a prerequisit. Per a pre-A1, millor recapitulació oral amb suport visual. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *HCL Explicar com a evidència de comprensió lectora*: saber escriure un resum és saber llegir. L'alumne que no sap quina és la idea principal no pot escriure un bon resum. El resum revela la comprensió lectora de manera directa i verificable: és l'instrument d'avaluació de comprensió lectora per excel·lència de totes les matèries.
- *Reformulació vs. còpia — la competència CALP clau*: la distinció entre resumir i copiar és una de les competències de més alta demanda cognitiva del CALP. Parafrasear (dir el mateix amb paraules pròpies) requereix comprensió profunda del significat, no només del text superficial. Cal treballar-la explícitament i de forma progressiva des de A1.
- *Recapitulació oral com a bastida ZDP (A1-A2)*: la seqüència pedagògica òptima és: (1) llegir el text, (2) recapitular oralment en parella ("explica de qué tracta"), (3) escriure el resum. La recapitulació oral actua com a bastida ZDP: l'alumne ancra la comprensió en el que ja pot dir oralment abans de produir-ho per escrit.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **resum adaptat per a la LECTURA** de l'alumne. **No descriu la producció autònoma** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Idea principal al 1r paràgraf**
- Claredat i directesa: 1 frase que diu de qué tracta el text. Directa. Al principi.

**2. Conservació de la veu original**
- Fidelitat i imparcialitat: No afegir opinions pròpies: sense "crec que", "m'agrada", "és interessant".

**3. Connectors lògics**
- Coherència i estructura: "I", "però", "perquè". Pocs però presents.

**4. Proporció i llargada**
- Síntesi i selecció: 3-4 frases. Màxim 1/3 del text font.

**5. Criteris transversals**
- Síntesi sense preàmbul: Cap "En aquest text…", "L'autor diu que…" com a primera frase. La primera paraula del resum és ja contingut.
- No còpia literal: Cap frase copiada del text font. Reformulació sempre.
- Fidelitat al text font: Fidelitat a la idea principal i a les 2-3 idees secundàries del text font.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit la idea principal en la primera frase. No he escrit la meva opinió."

### A1 — Inicial


**1. Idea principal al 1r paràgraf**
- Claredat i directesa: Idea principal en 1-2 frases. Primer paràgraf. Directa i sense preàmbul.

**2. Conservació de la veu original**
- Fidelitat i imparcialitat: Sense afegir informació nova ni opinions. Veu neutra i impersonal.

**3. Connectors lògics**
- Coherència i estructura: "Per tant", "d'altra banda", "però". Variats i usats per connectar les idees.

**4. Proporció i llargada**
- Síntesi i selecció: 4-6 frases (o ~1/4 del text font). Proporcional a la complexitat del font.

**5. Criteris transversals**
- Síntesi sense preàmbul: Idem. Sense meta-comentaris sobre el text o l'autor.
- No còpia literal: Idem. Cap fragment de més de 4 paraules consecutives idèntiques al font.
- Fidelitat al text font: Fidelitat a la idea principal, a les idees secundàries i a l'ordre del font.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He connectat les idees amb connectors. No he afegit informació nova."

### A2 — Funcional


**1. Idea principal al 1r paràgraf**
- Claredat i directesa: Idea principal condensada amb precisió. Primera frase densa i informativa.

**2. Conservació de la veu original**
- Fidelitat i imparcialitat: Reformulació que manté el punt de vista de l'autor original sense adoptar-lo.

**3. Connectors lògics**
- Coherència i estructura: Connectors que reflecteixen la relació real entre idees del text font (causa, contrast, conseqüència).

**4. Proporció i llargada**
- Síntesi i selecció: ~1/4 o 1/5 del text font. Preservar estructura lògica per davant de la llargada mecànica.

**5. Criteris transversals**
- Síntesi sense preàmbul: Idem. Cap frase buida de contingut al resum.
- No còpia literal: Idem. La reformulació captura el sentit, no el text superficial.
- Fidelitat al text font: Fidelitat a la idea principal, a les idees secundàries, als connectors i a la relació lògica del font.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu resum té les idees en el mateix ordre que el text original. He eliminat exemples però no idees."

### B1 — Estratègic


**1. Idea principal al 1r paràgraf**
- Claredat i directesa: Idea principal amb el matís necessari. Primera frase que capta el nucli del text font.

**2. Conservació de la veu original**
- Fidelitat i imparcialitat: Veu de l'autor preservada. Distinció clara entre el que diu l'autor i qui resumeix.

**3. Connectors lògics**
- Coherència i estructura: Connectors precisos que reprodueixen l'estructura lògica del text font.

**4. Proporció i llargada**
- Síntesi i selecció: Proporció conscient: la llargada reflecteix la importància relativa de cada idea del font.

**5. Criteris transversals**
- Síntesi sense preàmbul: Idem. Densitat informativa alta.
- No còpia literal: Idem. La reformulació preserva els matisos semàntics rellevants del font.
- Fidelitat al text font: Fidelitat a la complexitat informativa i al registre del text font.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He mantingut la veu de l'autor. La llargada és proporcional al text font."

### B2 — Acadèmic


**1. Idea principal al 1r paràgraf**
- Claredat i directesa: Idea principal amb tots els matisos que el text font implica, sense sobrecarregar.

**2. Conservació de la veu original**
- Fidelitat i imparcialitat: Veu de l'autor preservada amb precisió. Atribució explícita si cal ("Segons l'autor...").

**3. Connectors lògics**
- Coherència i estructura: Connectors sofisticats que capturen la lògica argumentativa o expositiva de l'autor.

**4. Proporció i llargada**
- Síntesi i selecció: Condensació rigorosa: cada frase del resum aporta informació nova i necessària del font.

**5. Criteris transversals**
- Síntesi sense preàmbul: Idem. Màxima densitat: cada frase és contingut del font, no comentari sobre el font.
- No còpia literal: Idem. La reformulació pot conservar termes tècnics si no existeix paràfrasi adequada.
- Fidelitat al text font: Fidelitat total: idea principal, idees secundàries, relació lògica i matisos del font.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu resum és dens, fidel i complet. Qualsevol persona pot entendre el text font llegint el meu resum."

### C1+ — Crític


