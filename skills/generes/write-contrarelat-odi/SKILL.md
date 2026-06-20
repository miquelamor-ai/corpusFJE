---
name: write-contrarelat-odi
description: 'Instrument per adaptar o generar un contrarelat de l''odi: resposta
  argumentativa que desmunta discursos d''odi amb empatia, veritat verificable i narrativa
  alternativa. Basat en Izquierdo Grau (UAB 2019), Benesch (8 estrategies), marc ignasia
  (CG36 reconciliacio triple, PPI, Fratelli tutti) i Decret 175/2022. Modalitat configurable:
  counterspeech directe / counter-narrative indirecte. No s''aplica a pre-A1. Rubrica
  gradada 8 passos x 5 nivells MECR (A1->C1).'
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
tools_required: []
agent_role: adapter
genre_key: contrarelat_odi
triggers:
- path: params.genere_discursiu
  equals: contrarelat_odi
mecr_range:
- A1
- A2
- B1
- B2
- C1
translanguaging: true
multimodal: false
moduls_relacionats:
- M3
- M8
macro_tipologia: argumentativa
label_ca: Contrarelat de l'odi
font_canonic: M3_genere-escriure-contrarelat-odi.md
font_version: 4.0.0-canonic
generat_at: '2026-06-20'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 562dc178c65cf28c
---

# Escriure/adaptar un contrarelat de l'odi — skill operativa per a LLM

El contrarelat de l'odi (counter-narrative) és un genere **argumentatiu-dialogic** que respon a un discurs de discriminacio, estereotip o deshumanitzacio amb empatia, veritat verificable i proposta d'una narrativa alternativa que dignifica. **No es opinió generica**: el punt de partida sempre es un discurs alié concret (identificat com a d'odi, estigmatitzant o discriminatori), no una tesi propia. **No s'aplica a pre-A1**: la identificacio i la refutació d'un discurs requereix base lingüistica A1 i capacitat d'accés al context comunicatiu.

**Tipologia MALL**: Argumentativa + Mediació social (pont entre posicions polaritzades).
**HCL principals**: Argumentar · Refutar · Empatitzar · Proposar alternativa · Discernir.
**Principi rector ignasia — Reconciliació, no combat**: el contrarelat FJE no busca "guanyar" la discussio retórica sinó construir condicions de **reconciliació triple** (CG36 Decret 1, 2016): reconciliació amb la persona, amb la veritat i amb la dignitat de tots. La victoria retórica que humilia l'adversari és antipedagògica. El discerniment ignasià (UAP 1, 2019) prega: "Quina resposta serveix MÉS el bé de la persona concreta i el bé comu?"

**2 modalitats de resposta (configurable):**
- **Counterspeech directe** (resposta puntual): refuta el discurs d'odi concret amb fets i argumentació. El lector sap quin discurs s'esta refutant.
- **Counter-narrative indirecte / Alternative speech** (canvi de marc): no respon directament al discurs d'odi sinó que proposa un marc de sentit alternatiu que el fa impossible. L'objectiu és l'audiència terciaria (no l'autor del discurs sinó qui l'ha rebut).

**Fonaments academics:**
- **Izquierdo Grau, A. (UAB, 2019)**: *Contrarelats de l'odi a l'ensenyament i aprenentatge de les Ciencies Socials* (tesi doctoral, Excel·lent Cum Laude). Model conceptual aplicat a l'ESO català. Tradicio GREDICS (Santisteban, UAB).
- **Benesch, S. (Dangerous Speech Project)**: taxonomia de 8 estrategies de counterspeech (empatia, fact-checking, humor, vergonya, conseqüencies, to, afiliació, redirecció).
- **Consell d'Europa**: *Bookmarks* (2014/2020), *We CAN!* (2017) — marcs pedagògics operatius.
- **CG36 / PPI / Fratelli tutti**: dimensió ignasiana integradora (vegeu §Fonts).

**Distinció critica amb `write-opinio`:**
- `write-opinio`: defensa una tesi propia sobre qualsevol tema des del pensament propi.
- `write-contrarelat-odi`: respon sempre a un discurs alié concret, identificat com a perjudicial. L'opinió argumenta; el contrarelat desmunta i reconcilia.

**Connexions MALL transversals:**
- *Translanguaging*: a A1-A2, l'empatia activa (Pas 3) es pot expressar primer en L1 per ancoratge emocional autentic, i despres en catala. L'alumne nouvingut que descriu com afecta el discurs d'odi a la seva propia comunitat fa un acte de transllenguatge de gran valor testimonial.
- *Pre-A1 — NO generar*: identificar un discurs d'odi i produir una resposta requereix capacitat de lectura critica i acces al context comunicatiu. A pre-A1, el treball sobre el discurs d'odi es fa en format assemblea oral mediada pel docent, no amb instrument generat.
- *Connexio amb `write-opinio`*: el contrarelat presuposa el domini del genere opinió (A1+). A B2-C1, el contrarelat és la forma més sofisticada d'argumentació: no defensa una tesi propia sino que desmunta una tesi aliena i proposa un marc alternatiu.
- *Connexio amb `generate-activitats-aprofundiment`*: l'activitat de comprensió critica que identifica discurs d'odi en un text (Pas 3 crític de preguntes-comprensio) és el precedent natural del contrarelat. El contrarelat és la producció que surt de la comprensió critica.

**Marc civic-ignasiA:**
El contrarelat és l'expressió natural de les 4 C's FJE aplicades al discurs public:
- **Conscients**: identifiquen el mecanisme del discurs d'odi.
- **Competents**: construeixen una resposta amb fonts i argument.
- **Compassius**: reconeixen la humanitat de tots (autor i victima).
- **Compromesos**: proposen acció reconciliadora.

Les **4 dimensions civils** (Miquel, 2026) que estructura el contrarelat ignasià:
1. **Participació democratica** — la resposta al discurs d'odi és un acte de deliberació publica (Hess & McAvoy 2015).
2. **Inclusió** — el contrarelat desactiva marcs excloents i eixampla el "nosaltres".
3. **Diversitat** — reconeix i valora la multiplicitat de veus que el discurs d'odi silencia.
4. **Universalitat** — apel·la a drets humans universals com a marc comu (*Fratelli tutti* + DUDH 1948).

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **contrarelat que es genera per a la LECTURA i model de l'alumne** (ADAPTACIÓ ARGUMENTATIVA CRITICA). **No descriu la producció autonoma de l'alumne**: la rubrica avalua el text generat com a model; l'alumne el llegeix, analitza l'estrategia i en pot fer un de propi com a activitat derivada. La producció autónoma de l'alumne s'avalua amb l'instrument `generate-rubriques`.
**Sub-granularitat dins d'A1**: variable `fase_lectora: alfabetica_emergent` → suport visual i oral maxim; `fase_lectora: alfabetica_fluida` → lectura autonoma del text model.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Identificació del discurs d'odi**
- Reconeixement del mecanisme: Identificació oral guiada: "Qui rep el dany? Que diu el text que no és veritat o que no és respectuós?" Model visual (imatge + frase).

**2. Discerniment**
- Tria de modalitat i decisió de respondre: No s'aplica: modalitat predeterminada (counterspeech simplificat, resposta directa).

**3. Empatia activa**
- Reconeixement de la humanitat de tots: "La persona que diu això segurament tem ___." (1 frase guiada amb model). Cap judici de l'autor; reconeixement del dany a la victima.

**4. Fact-checking / Veritat verificable**
- Correcció factual: 1 fet concret que contradiu el discurs d'odi. Font senzilla i assolible ("a classe hem vist que...").

**5. Narrativa alternativa**
- Marc de dignitat i sentit: "Una altra manera de veure-ho és ___." (1 frase guiada amb model).

**6. Crida a l'acció reconciliadora**
- Compromís comu: "Podem fer ___." (1 acció concreta i immediata, guiada per model).

**7. Criteris transversals**
- Qualitat etica i retorica: 3 criteris simples: "No dic cap nom malament. Dic una cosa certa. Parlo amb respecte."

**8. Autoavaluació / Examen ignasià**
- Metacognició ètica: "He dit ___. M'agrada? Canviaria alguna cosa?" (oral, mediat per l'adult).

### A1 — Inicial


**1. Identificació del discurs d'odi**
- Reconeixement del mecanisme: Identificació escrita: quin grup és l'objectiu? Quin mecanisme (estereotip / generalització / deshumanització)? 1-2 frases amb model.

**2. Discerniment**
- Tria de modalitat i decisió de respondre: Triar: "Puc respondre amb fets?" (counterspeech directe) o "Cal canviar el marc?" (counter-narrative). 1 frase de justificació.

**3. Empatia activa**
- Reconeixement de la humanitat de tots: Empàtic vers l'autor (comprendre la por o necessitat al darrere, sense validar el discurs) + vers la victima (reconèixer el dany). 2 frases.

**4. Fact-checking / Veritat verificable**
- Correcció factual: 2 fets verificats. Font citada breument. Connexió directa amb la falsedat identificada al Pas 1.

**5. Narrativa alternativa**
- Marc de dignitat i sentit: Narrativa breu (2-3 frases) que proposa un marc d'inclusió o dignitat. Apel·lació a un valor compartit (justicia, respecte, igualtat).

**6. Crida a l'acció reconciliadora**
- Compromís comu: 1 acció deliberativa concreta i assolible per a l'alumne o el grup. Formulació positiva (cap a, no contra).

**7. Criteris transversals**
- Qualitat etica i retorica: 3 criteris explícits: sense atacs personals, 1 fet verificat, to respectuós. Autochecklist.

**8. Autoavaluació / Examen ignasià**
- Metacognició ètica: 2 preguntes senzilles: "He dit la veritat? He estat respectuós amb tothom?"

### A2 — Funcional


**1. Identificació del discurs d'odi**
- Reconeixement del mecanisme: Identificació del mecanisme retòric concret (fal·làcia, apel·lació emocional, generalitzacio abusiva) + audiencia diana.

**2. Discerniment**
- Tria de modalitat i decisió de respondre: Selecció de modalitat justificada amb argumentació: per quin motiu tries counterspeech o counter-narrative en aquest cas concret?

**3. Empatia activa**
- Reconeixement de la humanitat de tots: Imaginar-se com se sent la victima: "Que deu sentir quan llegeix aquest discurs?" I per que l'autor el diu: "Quina por o necessitat hi pot haver al darrere?" 2 frases de perspectiva, sense validar el discurs.

**4. Fact-checking / Veritat verificable**
- Correcció factual: 3 fets estructurats amb fonts. Distinció explícita entre fet / opinió / falsedat. Presentació ordenada.

**5. Narrativa alternativa**
- Marc de dignitat i sentit: Narrativa alternativa coherent: reconstruir la imatge del grup estigmatitzat amb evidencies i, si és possible, testimoniatge personal.

**6. Crida a l'acció reconciliadora**
- Compromís comu: Crida especifica a l'audiencia: acció deliberativa + participació democratica. Formulació que inclou el grup diana.

**7. Criteris transversals**
- Qualitat etica i retorica: 4 criteris: sense atacs personals, fets verificables, to respectuós, perspectiva de la victima visible. Autorevisió conscient.

**8. Autoavaluació / Examen ignasià**
- Metacognició ètica: 3 preguntes PPI (Paradigma Pedagogic Ignasià): "Que he apres? Com m'he sentit responent? Faré alguna cosa diferent?

### B1 — Estratègic


**1. Identificació del discurs d'odi**
- Reconeixement del mecanisme: Analisi del context de producció: qui parla, a qui, per quin motiu, en quin medi. Efecte sobre la victima i sobre l'audiencia.

**2. Discerniment**
- Tria de modalitat i decisió de respondre: Analisi de l'audiencia per triar modalitat: la resposta directa arriba a qui necessita llegir-la? O cal canviar el marc? Justificació estrategica.

**3. Empatia activa**
- Reconeixement de la humanitat de tots: Analisi de l'emoció dominant al discurs d'odi (por, ràbia, inseguretat, necesitat d'identitat) + proposta d'empatia especifica que no valida el discurs.

**4. Fact-checking / Veritat verificable**
- Correcció factual: Fact-checking sistematic: cada afirmació discriminatoria del discurs d'odi confrontada amb evidencia verificada. Fonts diverses i creïbles citades.

**5. Narrativa alternativa**
- Marc de dignitat i sentit: Counter-narrative completa: canvia el marc del debat. Apel·la a valors compartits (drets humans, dignitat, ciutadania) i proposa una comprensió alternativa.

**6. Crida a l'acció reconciliadora**
- Compromís comu: Crida a l'acció comunitaria fonamentada: connecta l'acció amb valors compartits i institucions democratiques. Llista de recursos o vies concretes.

**7. Criteris transversals**
- Qualitat etica i retorica: 5 criteris: tots els anteriors + fonts citades + modalitat justificada.

**8. Autoavaluació / Examen ignasià**
- Metacognició ètica: Examen ignasià simplificat: "He respost amb justicia? He dignificat la victima? He buscat reconciliació o m'he quedat al combat retòric?"

### B2 — Acadèmic


**1. Identificació del discurs d'odi**
- Reconeixement del mecanisme: Identificació del mecanisme ideologic de fons (construcció de l'Altre, exclusió sistematica, reificació) + cadena de distorsió fins al text.

**2. Discerniment**
- Tria de modalitat i decisió de respondre: Discerniment ignasià complet: Quina resposta serveix MES el bé de la persona i el bé comu? No la mes efectiva retòricament, sinó la mes justa i reconciliadora.

**3. Empatia activa**
- Reconeixement de la humanitat de tots: Lectura hermenèutica des de *Fratelli tutti*: "cultura del descart" com a diagnòstic estructural. Resposta que dignifica l'autor i la victima, no que condemna ni exclouen.

**4. Fact-checking / Veritat verificable**
- Correcció factual: Analisi epistemologica: d'on ve la falsedat? Quins interessos serveix? Com es perpetua i amplifica? Fonts primaries citades. Mecanismes de verificació explicitats.

**5. Narrativa alternativa**
- Marc de dignitat i sentit: Narrativa transformadora (counter-narrative indirecte): proposa una comprensió del mon que fa impossible el discurs d'odi. Apel·la a la fraternitat universal (*Fratelli tutti*) i a les 4 dimensions civils.

**6. Crida a l'acció reconciliadora**
- Compromís comu: Crida transformadora (CG36): proposa condicions estructurals per a la reconciliació. No acció individual sino canvi de cultura. Fonamentada en *Fratelli tutti* cap. VI (dialeg i amistat social).

**7. Criteris transversals**
- Qualitat etica i retorica: 6 criteris: tots els anteriors + coherencia entre empatia i crida + coherencia entre diagnòstic ideologic i narrativa alternativa.

**8. Autoavaluació / Examen ignasià**
- Metacognició ètica: Examen ignasià complet: "He servit el bé de la persona concreta i el bé comu? El meu contrarelat és mes just que el discurs original? He estat fidel a la veritat verificable? He obert la porta a la reconciliació?"

### C1+ — Crític


