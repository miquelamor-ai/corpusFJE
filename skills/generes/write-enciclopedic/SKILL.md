---
name: write-enciclopedic
description: 'Use when adapting or generating an enciclopèdic entry for students.
  Activates when genre_discursiu == "enciclopedic". Applies single-sentence nuclear
  definition, category-first structure, and immediate concrete example. Output: enciclopèdic
  entry in markdown with term, definition, expanded explanation, and example.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
genre_key: enciclopedic
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
  equals: enciclopedic
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-enciclopedic.md
font_version: 4.0.0-canonic
generat_at: '2026-05-31'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: adc27032f38800dd
---

# Escriure/adaptar una entrada enciclopèdica — skill operativa per a LLM

L'entrada enciclopèdica defineix un terme amb la màxima precisió possible, usant la fórmula **"categoria + especificitat"** i el contextualitza amb una explicació ampliada i un exemple concret. El seu tret definitori és l'absència de circularitat: la definició no pot usar el terme ni paraules de la mateixa arrel per explicar-se.

**Tipologia MALL**: Expositiva/Descriptiva.
**HCL principal**: Descriure — definir i caracteritzar un terme amb precisió i sense circularitat.
**HCL secundàries**: Explicar — relació entre característiques del terme (B1+).
**No s'adapta a pre-A1**: l'entrada enciclopèdica requereix la comprensió del concepte abstracte **"categoria"** — ser capaç de situar un terme dins d'una classe superior ("la balena és un mamífer" implica saber que mamífer és una categoria que inclou la balena, no només que la balena és un animal). La fórmula `categoria + especificitat` és una operació de classificació abstracta inaccessible sense base lecto-escriptora mínima i sense coneixement de les categories disciplinars. (Decisió 6 canònica Fase B.)

**Connexions MALL transversals:**
- *Definició com a base del CALP*: aprendre a construir una definició precisa és aprendre la lògica del pensament científic. La fórmula "és un [categoria] que [especificitat]" és exportable a totes les matèries i és una de les competències acadèmiques més transferibles del currículum.
- *Exemple com a ancoratge ZDP*: sense un exemple concret i proper, la definició abstracta no s'integra al coneixement previ de l'alumne. L'exemple és el pont entre la definició formal i la comprensió real.
- *Absència de circularitat com a criteri de qualitat*: detectar que una definició és circular ("el fotosíntesi és el procés de fotosíntesi...") és una competència metacognitiva. El "test de la circularitat" és una eina de pensament crític exportable a totes les matèries.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu l'**entrada enciclopèdica adaptada per a la LECTURA** de l'alumne. **No descriu la producció autònoma de l'alumne** — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix base lecto-escriptora mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Definició nuclear**
- Precisió i estructura: 1 frase ≤10 paraules. Estructura: "X és un Y que Z."

**2. Absència de circularitat**
- Coherència lògica: Test: la definició no usa el terme per definir-se. Criteri bàsic.

**3. Categoria primer**
- Estructura lògica: Categoria explícita a la primera paraula de la definició: "és un animal / un lloc / un procés...".

**4. Exemple concret**
- Accessibilitat i ancoratge: 1 exemple molt visual i quotidià. 1 frase.

**5. Explicació ampliada**
- Profunditat i coherència: 2-3 frases simples amb detalls addicionals del terme. Una característica per frase.

**6. Criteris transversals**
- Llargada: Definició (1 frase) + 2-3 frases d'explicació + 1 exemple.
- Sense remissions: Cap remissió a altres entrades ("vegeu també...").
- Sense etimologia inicial: L'etimologia no substitueix la definició. Si apareix, va darrere de la definició.
- Fidelitat al text font: Fidelitat a la categoria i al tret diferencial principals del terme.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He escrit una frase que diu qué és el terme. He posat un exemple."

### A1 — Inicial


**1. Definició nuclear**
- Precisió i estructura: 1 frase clara. Categoria + especificitat. Sense circularitat.

**2. Absència de circularitat**
- Coherència lògica: Definició que no usa el terme ni paraules de la mateixa arrel.

**3. Categoria primer**
- Estructura lògica: Categoria clara: [Terme] és un [categoria] que [especificitat].

**4. Exemple concret**
- Accessibilitat i ancoratge: 1 exemple concret pres del context immediat de l'alumne. Immediat a la definició.

**5. Explicació ampliada**
- Profunditat i coherència: 3 frases amb detalls rellevants. Vocabulari accessible.

**6. Criteris transversals**
- Llargada: Definició (1 frase) + 3 frases + 1 exemple.
- Sense remissions: Idem.
- Sense etimologia inicial: Idem.
- Fidelitat al text font: Fidelitat a la categoria, al tret diferencial i a l'exemple.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He dit a quina categoria pertany el terme i qué el fa diferent. He posat un exemple."

### A2 — Funcional


**1. Definició nuclear**
- Precisió i estructura: 1 frase precisa amb terminologia adequada. Sense circularitat ni sinònim com a definició.

**2. Absència de circularitat**
- Coherència lògica: Definició sense circularitat i sense sinònim com a definició ("la democràcia és un govern popular" és circular si no s'explica "popular").

**3. Categoria primer**
- Estructura lògica: Categoria i especificitat ben diferenciades. La categoria situa el terme dins d'una classe superordinal.

**4. Exemple concret**
- Accessibilitat i ancoratge: Exemple concret + contraexemple si és útil per delimitar el concepte.

**5. Explicació ampliada**
- Profunditat i coherència: 3-4 frases amb relació entre característiques. 1 terme tècnic nou introduït.

**6. Criteris transversals**
- Llargada: Definició + 3-4 frases + exemple + contraexemple si escau.
- Sense remissions: Idem.
- Sense etimologia inicial: Idem.
- Fidelitat al text font: Fidelitat a la categoria, al tret diferencial, a l'exemple i al to factual.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "La meva definició no usa el terme per definir-se. He explicat 2-3 característiques."

### B1 — Estratègic


**1. Definició nuclear**
- Precisió i estructura: 1 frase completa amb terminologia específica de la matèria. Pot delimitar el terme respecte a termes propers.

**2. Absència de circularitat**
- Coherència lògica: Idem. La delimitació respecte a termes propers s'explicita a l'Explicació ampliada (Pas 5), no a la definició nuclear.

**3. Categoria primer**
- Estructura lògica: Categoria dins del camp lèxic de la matèria amb precisió disciplinar.

**4. Exemple concret**
- Accessibilitat i ancoratge: 1-2 exemples elaborats amb connexió explícita amb la definició.

**5. Explicació ampliada**
- Profunditat i coherència: Explicació amb múltiples característiques. Comparació amb termes propers.

**6. Criteris transversals**
- Llargada: Definició + explicació (4-5 frases) + 1-2 exemples.
- Sense remissions: Idem.
- Sense etimologia inicial: Idem.
- Fidelitat al text font: Fidelitat a la complexitat conceptual i al context disciplinar.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He delimitat el terme respecte a termes propers. He usat vocabulari específic de la matèria."

### B2 — Acadèmic


**1. Definició nuclear**
- Precisió i estructura: Definició nuclear rigorosa amb matisos terminològics i referència al debat si és rellevant.

**2. Absència de circularitat**
- Coherència lògica: Idem. Si hi ha debat terminològic, es recull a l'Explicació ampliada (Pas 5). La definició nuclear segueix sent binary: no usa el terme ni arrels.

**3. Categoria primer**
- Estructura lògica: Categoria amb precisió i referència a la taxonomia disciplinar si escau.

**4. Exemple concret**
- Accessibilitat i ancoratge: Exemples variats. Pot incloure un exemple límit o de frontera que posi a prova la definició.

**5. Explicació ampliada**
- Profunditat i coherència: Explicació completa amb matisos, variants i possibles debats sobre la delimitació del terme.

**6. Criteris transversals**
- Llargada: Text complet amb tots els matisos necessaris.
- Sense remissions: Idem. La referència a termes relacionats, si escau, s'integra al cos de l'explicació sense remissió formal.
- Sense etimologia inicial: L'etimologia pot aparèixer si aporta matisos al significat, però mai com a única definició.
- Fidelitat al text font: Fidelitat a la complexitat, als matisos i als debats si els hi ha.

**7. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He presentat el terme amb matisos, variants i possibles debats sobre la seva definició."

### C1+ — Crític


