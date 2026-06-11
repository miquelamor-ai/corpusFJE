---
name: generate-glossari
description: 'Use when the teacher has activated the "glossari" complement. Generates
  a markdown glossary of key terms from the adapted text. Monolingüe or bilingüe (with
  L1 column in native script) depending on whether the student is a newcomer. Quantity
  and format modulated by MECR level: Emergent uses a visual icon+word list (no table);
  from A1 upwards uses a markdown table.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: glossari
agent_role: complements
tools_required: []
triggers:
- path: params.complements.glossari
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-glossari.md
font_version: 4.0.0-canonic
generat_at: '2026-06-11'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 42ff043b336a1ad2
---

# Generar glossari — skill operativa per a LLM

El glossari és un instrument de **mediació lèxica** que acompanya el text adaptat i ofereix definicions dels termes clau. La seva funció és reduir la càrrega cognitiva lèxica perquè l'alumne pugui centrar-se en la comprensió del contingut. Inclou una **variant bilingüe** per a alumnat nouvingut amb L1 coneguda.

**Tipologia MALL**: Mediació lèxica (suport).
**HCL principal**: Descriure — definir amb precisió creixent (CALP).
**Principi rector CALP de Cummins** (llargada de la definició per nivell): pre-A1=6 paraules · A1-A2=8-10 paraules · B1=12 paraules · B2=15 paraules · C1=20 paraules.

**Connexions MALL transversals:**
- *Translanguaging / TOLC*: la variant bilingüe és una estratègia de translanguaging explícita. El terme en L1 activa el coneixement previ i redueix l'ansietat lingüística.
- *Multimodalitat*: a pre-A1 i A1, els emojis/pictogrames fan el glossari accessible sense lectura plena.
- *CALP de Cummins*: la gradació de la complexitat de la definició és la implementació directa del concepte de llengua acadèmica.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **glossari adaptat per a la LECTURA** de l'alumne (què el docent presenta perquè l'alumne consulti). **No descriu la producció autònoma de l'alumne** — això es treballa amb un derivat propi (rúbrica d'avaluació formativa), pertinent per al cas de **glossari col·laboratiu** (B1+ ; vegeu H4) on l'alumnat construeix el glossari sota la guia del docent.
**Sub-granularitat dins de pre-A1 i A1**: es treballa amb la variable independent `fase_lectora` del frontmatter (logografica · alfabetica_emergent · alfabetica_fluida), no amb columnes addicionals.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Selecció de termes**
- Nombre: 3-5 termes.
- Tipologia lèxica: Objectes reals i noms concrets. Sense tecnicismes.

**2. Format de presentació**
- Estructura: Emoji o pictograma + terme en negreta. Sense taula (massa complexa).
- Suport visual: Pictograma obligatori a cada terme. L'adult pot complementar amb imatge real.

**3. Explicació / definició (CALP)**
- Llargada: Fins a 6 paraules. Paraules molt freqüents.
- Recursos pedagògics: Paraules immediates de l'experiència de l'alumne.

**4. Variant bilingüe (nouvingut L1)**
- Inclusió L1: Afegeix el terme en L1 amb alfabet original (àrab, xinès, urdú, ciríl·lic, armeni…).
- Notes contrastives: Sense notes. La imatge és el pont.

**5. Criteris transversals**
- No-circularitat: El terme no apareix dins de la pròpia definició a cap nivell.
- No-recursivitat: La definició no usa cap paraula més tècnica que el terme mateix.
- Llengua de definició: Llengua de SORTIDA del text adaptat (català, castellà, anglès…). **MAI** usis termes d'una altra llengua com a fallback ni dins la definició. La L1 (si existeix) va a la columna pròpia, NO dins la cel·la d'explicació.
- Selecció pertinent: Cap connector, cap nom propi excepte si és clau per a la matèria, cap paraula quotidiana òbvia (excepte a Emergent on els objectes concrets sí entren).
- Fidelitat al text font: Tots els termes del glossari apareixen literalment al text adaptat (fidelitat al lèxic nuclear del text).

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He mirat les imatges del glossari quan al text he trobat una paraula que no he reconegut."

### A1 — Inicial


**1. Selecció de termes**
- Nombre: 5-8 termes.
- Tipologia lèxica: Noms i verbs d'acció principals del text.

**2. Format de presentació**
- Estructura: Taula de 2 columnes: Terme | Explicació.
- Suport visual: Emoji recomanat si el terme té representació visual clara.

**3. Explicació / definició (CALP)**
- Llargada: Fins a 8 paraules en català molt senzill (A1).
- Recursos pedagògics: Català A1 sense tecnicismes dins la definició. No repetir el terme.

**4. Variant bilingüe (nouvingut L1)**
- Inclusió L1: Columna addicional "Traducció (L1)" en alfabet original. Taula de 3 columnes.
- Notes contrastives: Sense notes. La traducció directa és el pont.

**5. Criteris transversals**
- No-circularitat: El terme no apareix dins de la pròpia definició a cap nivell.
- No-recursivitat: La definició usa només vocabulari A1 (mai termes més complexos sense explicar-los).
- Llengua de definició: Idem (llengua de sortida).
- Selecció pertinent: Idem. **Exclou explícitament a A1 + etapa primària inicial**: objectes domèstics (mitja, botó, agulla, fil, retolador, llapis, paper, plat, got, casa, taula, porta), parts del cos (cap, mà, ulls, boca, peu), verbs d'acció bàsics (posar, lligar, dibuixar, jugar, mirar, fer). Aquests són **coneixement previ**, no termes a explicar. Si el text no en conté CAP de realment nou per al nivell, escriu només la nota «Aquest text no necessita glossari nou per al teu nivell» sense taula.
- Fidelitat al text font: Tots els termes apareixen literalment al text adaptat.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "Quan llegint el text he trobat una paraula difícil, he anat al glossari a buscar-la abans de demanar ajuda."

### A2 — Funcional


**1. Selecció de termes**
- Nombre: 8-10 termes.
- Tipologia lèxica: Noms + verbs + adjectius clau.

**2. Format de presentació**
- Estructura: Taula de 2 columnes; pot afegir una analogia o exemple integrat.
- Suport visual: Emoji opcional per a termes concrets; no per a abstractes.

**3. Explicació / definició (CALP)**
- Llargada: Fins a 10 paraules.
- Recursos pedagògics: Pot incloure una analogia simple ("és com…") o un exemple concret del text.

**4. Variant bilingüe (nouvingut L1)**
- Inclusió L1: Columna addicional. Si no existeix paraula exacta en L1, usar la més propera amb aclariment breu.
- Notes contrastives: Aclariment breu quan no hi ha equivalent exacte.

**5. Criteris transversals**
- No-circularitat: El terme no apareix dins de la pròpia definició a cap nivell.
- No-recursivitat: Pot usar termes d'A2 màx.; tecnicismes només si s'expliquen integrats.
- Llengua de definició: Idem.
- Selecció pertinent: Idem.
- Fidelitat al text font: Tots els termes apareixen literalment al text adaptat.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He fet servir el glossari per entendre el text. He intentat dir el significat amb les meves paraules a algú."

### B1 — Estratègic


**1. Selecció de termes**
- Nombre: 10-12 termes.
- Tipologia lèxica: Inclou habilitats cognitives lèxicament marcades (hipòtesi, causa, conseqüència).

**2. Format de presentació**
- Estructura: Taula de 2 columnes; **ordre alfabètic** dels termes; pot afegir una tercera columna "Exemple en frase".
- Suport visual: Referència opcional a la il·lustració del text si n'hi ha.

**3. Explicació / definició (CALP)**
- Llargada: Fins a 12 paraules.
- Recursos pedagògics: Pot usar vocabulari lleugerament tècnic acompanyat d'un exemple.

**4. Variant bilingüe (nouvingut L1)**
- Inclusió L1: Columna addicional. Pot afegir nota sobre diferències conceptuals entre L1 i català.
- Notes contrastives: Notes conceptuals quan la categoria L1 difereix de la del català.

**5. Criteris transversals**
- No-circularitat: El terme no apareix dins de la pròpia definició a cap nivell.
- No-recursivitat: Pot usar termes B1 màx.; tecnicismes acompanyats d'exemple.
- Llengua de definició: Idem.
- Selecció pertinent: Idem.
- Fidelitat al text font: Tots els termes apareixen al text o són col·locacions necessàries per a la comprensió.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He reflexionat sobre si sabia usar els termes del glossari en una frase pròpia, i així he sabut quins encara no domino."

### B2 — Acadèmic


**1. Selecció de termes**
- Nombre: 12-15 termes.
- Tipologia lèxica: Lèxic d'especialitat (CALP). Inclou col·locacions ("realitzar una hipòtesi").

**2. Format de presentació**
- Estructura: Taula de 2-3 columnes; **ordre alfabètic** obligatori; pot incloure referència creuada interna.
- Suport visual: No necessari; el lector processa el terme sense suport visual.

**3. Explicació / definició (CALP)**
- Llargada: Fins a 15 paraules.
- Recursos pedagògics: Vocabulari acadèmic (CALP) propi del camp; pot referenciar un altre terme del glossari.

**4. Variant bilingüe (nouvingut L1)**
- Inclusió L1: Columna addicional. Pot afegir nota sobre diferències morfosintàctiques rellevants.
- Notes contrastives: Notes morfosintàctiques o de col·locació quan són rellevants per a la comprensió.

**5. Criteris transversals**
- No-circularitat: El terme no apareix dins de la pròpia definició a cap nivell.
- No-recursivitat: Pot usar lèxic d'especialitat propi del camp si el lector ja el coneix.
- Llengua de definició: Idem.
- Selecció pertinent: Idem.
- Fidelitat al text font: Termes literals + col·locacions + derivacions conceptualment necessàries.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He pensat quina diferència hi ha entre els termes del glossari que es poden confondre i com triaria un o l'altre."

### C1+ — Crític


**1. Selecció de termes**
- Nombre: 15-18 termes.
- Tipologia lèxica: CALP d'especialitat. Pot incloure termes meta-discursius i lèxic conceptual abstracte.

**2. Format de presentació**
- Estructura: Taula completa; **ordre alfabètic** obligatori; pot incloure etimologia breu o distinció entre termes similars.
- Suport visual: No necessari.

**3. Explicació / definició (CALP)**
- Llargada: Fins a 20 paraules.
- Recursos pedagògics: Definició precisa amb matís conceptual; pot incloure distinció entre termes similars o etimologia breu.

**4. Variant bilingüe (nouvingut L1)**
- Inclusió L1: Columna opcional. L'alumne ja pot gestionar el text sense suport explícit en L1.
- Notes contrastives: Notes autonomes; pot incloure registre o variació diatòpica si és rellevant.

**5. Criteris transversals**
- No-circularitat: El terme no apareix dins de la pròpia definició a cap nivell.
- No-recursivitat: Lèxic d'especialitat lliure dins del camp; referència creuada quan calgui.
- Llengua de definició: Idem.
- Selecció pertinent: Idem (els meta-discursius sí entren).
- Fidelitat al text font: Termes literals + col·locacions + derivacions + termes conceptualment connectats que amplien la xarxa lèxica del camp.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He reflexionat sobre com s'usaria el terme en un altre context i si la definició encara seria vàlida."

