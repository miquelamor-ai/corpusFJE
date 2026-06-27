---
name: write-informe-tecnic
description: 'Instrument per adaptar o generar un informe tècnic professional: presentació
  de resultats, anàlisi i recomanacions dirigida a un destinatari decisor (client,
  empresa, organisme). Invariant del gènere: resum executiu sempre present (B1+) +
  cadena lògica problema→anàlisi→conclusions→recomanacions. HCL Justificar (dominant)
  + Explicar + Descriure. Rúbrica gradada 8 passos × 4 nivells MECR (A2→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 1.0.0
tools_required: []
agent_role: adapter
genre_key: informe_tecnic
triggers:
- path: params.genere_discursiu
  equals: informe_tecnic
macro_tipologia: explicativa
label_ca: Informe tècnic
mecr_range:
- A2
- B1
- B2
- C1
translanguaging: true
multimodal: true
moduls_relacionats:
- M3
- M2
font_canonic: M3_genere-escriure-informe-tecnic.md
font_version: 1.0.0
generat_at: '2026-06-27'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 0812766766edaf22
---

# Escriure/adaptar un informe tècnic — skill operativa per a LLM

L'informe tècnic professional presenta els resultats d'una anàlisi, inspecció, estudi o intervenció, amb una cadena lògica tancada: **problema → anàlisi → conclusions → recomanacions**, adreçada a un **destinatari decisor** (client, empresa, organisme, superior jeràrquic) que ha d'actuar a partir del document. El tret definitori que el distingeix de l'informe acadèmic és doble: la **secció de recomanacions és constitutiva del gènere** (no opcional) i el **resum executiu és obligatori** perquè el destinatari professional sovint no llegeix el document complet.

**Tipologia MALL (macro)**: Explicativa (amb HCL dominant Justificar).
**HCL principal**: Justificar — vincular els resultats tècnics amb solucions, recomanacions o teoria de forma raonada i explícita.
**HCL secundàries**: Explicar — causa-efecte dels resultats i del procediment · Descriure — estat actual de la instal·lació, producte, situació o servei objecte d'inspecció (actiu a A2-B1).
**No s'adapta a pre-A1 ni A1**: l'informe tècnic requereix la distinció metacognitiva resultats/recomanacions (el que he trobat vs el que cal fer) i un destinatari explícit extern a l'aula. Sense base lecto-escriptora consolidada i sense CALP mínim, la cadena lògica del gènere no és operativa.

**Diferència clau vs `write-informe` (acadèmic):**
- L'informe acadèmic presenta dades a un professor (audiència avaluadora).
- L'informe tècnic presenta resultats i recomanacions a un client o empresa (audiència decisora). Sense destinatari explícit, no és un informe tècnic professional, és un informe genèric.
- La secció de recomanacions és **constitutiva** de l'informe tècnic: no pot faltar. A l'informe acadèmic és opcional.
- El lèxic especialitzat del sector (manteniment, electricitat, restauració, administració, construcció...) és part de l'invariant disciplinari del gènere: no es substitueix per sinònims quotidians.

**Connexions MALL transversals:**
- *CALP professional*: l'informe tècnic operacionalitza el CALP en contextos de Formació Professional. La veu impersonal, les dades mesurables i la cadena justificativa son el CALP en la seva expressió professional i sectorial.
- *Justificar com a habilitat epistèmica nuclear*: l'HCL Justificar no és només un connector lògic; és la competència que permet a un tècnic dir "els resultats impliquen X, per tant cal fer Y". Sense la justificació, l'informe es queda en descripció (no és informe tècnic).
- *Destinatari explícit com a variable de disseny textual*: a diferència d'altres gèneres, l'informe tècnic es pensa sempre per a qui l'ha de llegir i per a quina decisió ha de servir. L'alumne aprèn que l'audiència decisora condiciona el format, el lèxic i el nivell de detall.
- *Multimodalitat al servei de la precisió tècnica*: taules de mesures, esquemes d'instal·lació, gràfics de tendència, fotografies de la intervenció son el format natiu de les dades tècniques. A diferència del pòster científic (la lligadura dada–visual és estètica i comunicativa), aquí la taula de mesures és evidència legal i professional: les dades no es poden aproximar ni arrodonir.
- *Translanguaging per capes*: a diferència de l'informe acadèmic (translanguaging: false), l'informe tècnic admet pont L1 per a l'alumnat nouvingut a la bastida lingüística del voltant, però mai als termes tècnics sectorials, a les dades ni a la cadena justificativa. La porta de decisió és idèntica a la del pòster científic (`alfabetitzacio_l1`).

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu l'**informe tècnic adaptat per a la LECTURA** de l'alumne (el model que llegeix/interpreta), no la producció autònoma de l'alumne — la producció és tasca d'un derivat propi. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast cognitiu, amb la forma lingüística ajustada al seu nivell.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Portada i destinatari**
- Identificació professional: Títol + nom de l'alumne + a qui va dirigit (1 línia: "Per a: [empresa/persona]"). Data.

**2. Resum executiu**
- Síntesi per al decisor: Absenta o molt breu (2-3 frases: "He inspeccionat X. He trobat Y. Cal fer Z."). Pot ser oral amb l'adult.

**3. Introducció**
- Context i abast: 2-3 frases: de quina instal·lació/producte/situació es tracta i per quin motiu s'ha fet l'informe.

**4. Metodologia / Procediment**
- Traçabilitat del procés: Llista de 3-5 passos de com s'ha fet la inspecció o l'anàlisi. Frases simples.

**5. Resultats i dades**
- Fidelitat a les mesures: Dades en taula simple (2-3 columnes). Valor + unitat sempre intactes. 1-2 frases que diuen "s'ha observat X".

**6. Anàlisi i discussió**
- HCL Justificar: 1-2 frases: "Això vol dir que..." o "Per tant...". La connexió resultat → implicació és explícita però simple.

**7. Conclusions i recomanacions**
- Cadena lògica tancada: Conclusions: 1-2 frases ("He trobat que..."). Recomanacions: llista de 2-3 ítems simples ("Cal canviar X"). Blocs SEPARATS.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He separat el que he trobat del que cal fer?"

### A1 — Inicial


**1. Portada i destinatari**
- Identificació professional: Portada completa: títol, autor, data, destinatari (nom + càrrec + empresa), número d'informe si escau.

**2. Resum executiu**
- Síntesi per al decisor: Resum executiu de 3-5 línies: problema principal + conclusió central + recomanació clau. Autònom: llegit sol, el decisor pot actuar.

**3. Introducció**
- Context i abast: Context, objectiu de l'informe i abast (què s'ha inspeccionat/analitzat i què no).

**4. Metodologia / Procediment**
- Traçabilitat del procés: Procediment en paràgraf breu: instruments usats, condicions de la inspecció, mostra o àmbit analitzat.

**5. Resultats i dades**
- Fidelitat a les mesures: Dades en taula o gràfic amb llegenda. Descripció objectiva de la tendència o l'estat ("el valor supera el llindar de...").

**6. Anàlisi i discussió**
- HCL Justificar: Anàlisi per bloc de resultats: connexió resultat → causa probable → implicació. Connector "per tant" i "a causa de" actius.

**7. Conclusions i recomanacions**
- Cadena lògica tancada: Conclusions: 2-3 derivades explícitament de l'anàlisi. Recomanacions: llista ordenada, cada una lligada a una conclusió específica.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu resum explica el problema i la recomanació principal en 3-5 línies."

### A2 — Funcional


**1. Portada i destinatari**
- Identificació professional: Portada professional amb tots els camps estàndard del sector.

**2. Resum executiu**
- Síntesi per al decisor: Resum executiu de 1 paràgraf: context breu + principals troballes + recomanació prioritària. Formal.

**3. Introducció**
- Context i abast: Introducció estructurada: context sectorial, objectiu, abast, marc normatiu o legal aplicable si escau.

**4. Metodologia / Procediment**
- Traçabilitat del procés: Metodologia amb instruments, mostra, condicions i limitacions del procés. Variables identificades.

**5. Resultats i dades**
- Fidelitat a les mesures: Dades organitzades per categories o subsistemes. Gràfic o taula per a la comparació. Descripció objectiva.

**6. Anàlisi i discussió**
- HCL Justificar: Anàlisi argumentada: relació causal entre resultats i causes, comparació amb valors de referència o normativa. Justificació de les conclusions.

**7. Conclusions i recomanacions**
- Cadena lògica tancada: Conclusions argumentades amb referència als resultats. Recomanacions prioritzades (urgents / a mig termini). Blocs diferenciats amb H3 propis.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Les meves recomanacions deriven de les conclusions, i les conclusions, de les dades."

### B1 — Estratègic


**1. Portada i destinatari**
- Identificació professional: Portada formal amb identificació institucional completa (empresa emissora, empresa receptora, referència de l'encàrrec).

**2. Resum executiu**
- Síntesi per al decisor: Resum executiu professional complet: context, objectiu, metodologia sintètica, conclusions principals prioritzades, recomanació clau. Llegit sol, substitueix el cos per a la direcció.

**3. Introducció**
- Context i abast: Introducció acadèmico-professional: context, objectiu, hipòtesi o pregunta tècnica, abast, normativa i referències al sector.

**4. Metodologia / Procediment**
- Traçabilitat del procés: Metodologia rigorosa: instruments calibrats, condicions de mesura, mostra representativa, normativa tècnica aplicada, incertesa de mesura.

**5. Resultats i dades**
- Fidelitat a les mesures: Dades en formats variats (taules, gràfics, fotografies etiquetades). Anàlisi estadística si escau. Traçabilitat de cada mesura.

**6. Anàlisi i discussió**
- HCL Justificar: Anàlisi crítica: relació causal documentada, discussió de causes alternatives, comparació amb normativa i literatura tècnica, reconeixement de limitacions de l'anàlisi.

**7. Conclusions i recomanacions**
- Cadena lògica tancada: Conclusions amb discussió de limitacions. Recomanacions prioritzades per impacte, cost i urgència. Proposta de seguiment. Blocs amb rigor acadèmico-professional.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "L'informe és autònom: el decisor pot llegir el resum i actuar sense llegir el cos complet. Les recomanacions estan prioritzades i justificades."

### B2 — Acadèmic


### C1+ — Crític


