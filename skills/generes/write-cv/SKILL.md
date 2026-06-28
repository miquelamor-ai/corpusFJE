---
name: write-cv
description: 'Instrument per adaptar o generar un currículum vitae: document d''identitat
  professional que presenta les competències, la formació i l''experiència d''una
  persona per a una finalitat de selecció o orientació. HCL Descriure + Definir (presentar
  competències, formació, experiència); HCL Argumentar (selecció estratègica del que
  es mostra, B2+). Invariant absolut: veracitat — el CV reflecteix la realitat del
  candidat; ATNE adapta la forma, mai inventa competències ni experiències. Estructura
  reconeixible per un seleccionador (dades personals + formació + experiència + competències).
  Rúbrica gradada 8 passos × 4 nivells MECR (A2→C1).'
author: FJE — Fundació Jesuïtes Educació
version: 1.0.0
tools_required: []
agent_role: adapter
genre_key: cv
triggers:
- path: params.genere_discursiu
  equals: cv
macro_tipologia: descriptiva
label_ca: Currículum vitae
mecr_range:
- A2
- B1
- B2
- C1
translanguaging: true
multimodal: false
moduls_relacionats:
- M3
- M7
font_canonic: M3_genere-escriure-cv.md
font_version: 1.0.0
generat_at: '2026-06-28'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: f2613f61f48cd95a
---

# Escriure/adaptar un currículum vitae (CV) — skill operativa per a LLM

El currículum vitae (CV) és el **document d'identitat professional** d'una persona: presenta de manera organitzada i succinta les seves competències, la seva formació i la seva experiència per a una finalitat de selecció, orientació professional o sol·licitud de formació. El seu tret definitori és que **el contingut reflecteix estrictament la realitat del candidat**: un CV que conté informació inventada no és un CV, és una falsificació. ATNE adapta la forma lingüística; mai genera competències o experiències que l'alumne no tingui.

**Tipologia MALL (macro)**: Descriptiva. El gènere pertany a la macro-tipologia **Descriptiva** del M3 (vegeu `macro_tipologia: descriptiva` al frontmatter): mostra les característiques, la trajectòria i les competències d'una persona en l'espai professional. La dimensió argumentativa (selecció estratègica de la informació rellevant per a l'oferta) és secundària i emergeix a B2+.
**HCL principal**: Descriure + Definir — presentar competències, formació i experiència de manera estructurada i verificable.
**HCL secundària**: Argumentar — selecció estratègica d'allò que es mostra en funció del perfil de l'oferta i ús de paraules clau del sector (B2+).
**S'aplica de A2 a C1**: el CV funcional mínim ja és viable a A2 (nom + formació + competències bàsiques). Pre-A1/A1 no s'aplica: un CV és producció escrita autònoma que requereix un mínim de control lingüístic i de consciència del gènere per ser significativa.

**Connexions MALL transversals:**
- *El CV com a gènere de l'esfera professional*: el MALL cita el CV explícitament com a "exemple canònic de gènere lligat a l'activitat professional". No és un gènere escolar derivat; és el gènere primari que l'alumnat necessitarà fora del sistema educatiu.
- *Forma nominal i registre despersonalitzat*: el CV no usa la primera persona narrativa ("Jo vaig estudiar...") sinó formes nominals i frases nominals ("Estudis en...", "Experiència en...") o tercera persona. Aprendre a sostenir aquest registre és, en si mateix, un aprenentatge lingüístic rellevant.
- *Veracitat com a valor professional*: el CV és el gènere on la mentida té conseqüències reals (contracte rescindit, crèdit perdut). Treballar el CV és treballar l'honestedat professional com a competència social i lingüística, no com a valor abstracte.
- *La L1 com a dada factual, no com a pont*: al CV la L1 apareix com a **competència lingüística real** del candidat ("Parlant natiu d'àrab", "Llengua materna: amazic"). Això no és translanguaging com a andamiatge pedagògic: és una dada professional factual del perfil. Per a alumnat nouvingut, això pot ser una fortalesa invisible que el CV visibilitza per primera vegada.
- *Estructura Europass com a model europeu estàndard*: el model Europass és el marc reconegut en el context educatiu i laboral europeu. ATNE adopta les seves sis seccions canòniques com a estructura de referència (vegeu §Invariant).

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **CV adaptat per a la producció/model** de l'alumne (el document que redacta o que rep com a plantilla per omplir), i el **CV adaptat** que ATNE genera a partir d'un CV font ja existent. En mode adaptació, ATNE ajusta la forma lingüística de les seccions sense modificar el contingut (que prové del candidat). En mode generació, ATNE proporciona una plantilla amb les seccions canòniques per nivell MECR, amb instruccions per omplir-les.

**Distinció de gèneres relacionats:**
- vs `write-carta` (carta de presentació): la carta dirigeix un missatge argumentatiu a un destinatari concret; el CV és el document d'identitat professional neutre que l'acompanya. Són gèneres complementaris però independents: el CV pot existir sense carta, i la carta fa referència al CV però no el substitueix.
- vs `write-biografia`: la biografia narra la trajectòria d'una persona en format continu (prosa); el CV llista i categoritza en seccions. La biografia pot usar primera persona i connectius temporals narratius; el CV usa formes nominals i ordre cronològic invers.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Dades personals i contacte**
- Identificació: Nom + correu + telèfon. Sense foto, sense DNI. Format llista simple.

**2. Perfil professional / resum**
- Síntesi del valor del candidat: No s'inclou (massa abstracte per a A2).

**3. Formació**
- Trajectòria acadèmica: Llistat simple: títol + any + centre. Ordre cronològic invers. Frases nominals mínimes (3-6 paraules).

**4. Experiència professional**
- Trajectòria laboral: 1-2 entrades màxim. Càrrec + empresa + dates. 1 frase nominal de funció per entrada ("Atenció al client", "Preparació de comandes").

**5. Competències lingüístiques**
- Plurilingüisme del candidat: Llista: llengua + nivell (paraula simple: "bàsic", "bo", "natiu"). La L1 del candidat s'inclou amb "llengua materna" o "nivell nadiu".

**6. Competències digitals i altres**
- Habilitats transversals: Llista simple: nom de la competència o eina ("Word", "Instagram", "Caixa registradora"). Sense nivells.

**7. Altres (voluntariat, formació complementària, publicacions)**
- Perfil ampli del candidat: Opcional. Si s'inclou: nom de l'activitat + entitat + any. Sense descripció.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés de construcció del CV: "El meu CV explica qui soc i quina formació tinc."

### A1 — Inicial


**1. Dades personals i contacte**
- Identificació: Ídem. Pot afegir-se perfil LinkedIn si n'hi ha.

**2. Perfil professional / resum**
- Síntesi del valor del candidat: Opcional: 1-2 frases nominals molt simples sobre l'objectiu professional.

**3. Formació**
- Trajectòria acadèmica: Llistat estructurat. Pot afegir-se una línia breu de descripció per entrada rellevant.

**4. Experiència professional**
- Trajectòria laboral: Totes les entrades rellevants. 2-3 frases nominals de funcions per entrada. Connector d'enumeració ("Tasques principals: ...").

**5. Competències lingüístiques**
- Plurilingüisme del candidat: Llista amb nivell MECR si es coneix ("Català B2", "Castellà C1"). L1 amb "parlant natiu de...".

**6. Competències digitals i altres**
- Habilitats transversals: Llista amb nivell simple ("coneixements de...", "experiència en...").

**7. Altres (voluntariat, formació complementària, publicacions)**
- Perfil ampli del candidat: Opcional. Entrades rellevants amb 1 frase nominal de descripció.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés de construcció del CV: "El meu CV té totes les seccions i les dates i els noms son correctes."

### A2 — Funcional


**1. Dades personals i contacte**
- Identificació: Ídem. Selecció conscient de les dades rellevants per al context (p.ex. omissió de dades no pertinents).

**2. Perfil professional / resum**
- Síntesi del valor del candidat: 2-3 frases nominals que sintetitzen el perfil i l'objectiu de manera específica per a l'oferta.

**3. Formació**
- Trajectòria acadèmica: Selecció de la formació rellevant per a l'oferta. Cursos i certificacions identificats com a valor afegit.

**4. Experiència professional**
- Trajectòria laboral: Entrades seleccionades per rellevància. Funcions amb verbs d'acció en forma nominal ("Gestió de...", "Coordinació de..."). Resultats si n'hi ha.

**5. Competències lingüístiques**
- Plurilingüisme del candidat: Taula o llista estructurada amb nivell MECR i, si n'hi ha, certificació acreditada.

**6. Competències digitals i altres**
- Habilitats transversals: Competències digitals categoritzades (ofimàtica, eines de sector, xarxes). Competències transversals seleccionades per rellevància.

**7. Altres (voluntariat, formació complementària, publicacions)**
- Perfil ampli del candidat: Inclou-lo si aporta valor al perfil per a l'oferta. Selecció estratègica.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés de construcció del CV: "He seleccionat la informació del meu CV pensant en el lloc de feina que vull."

### B1 — Estratègic


**1. Dades personals i contacte**
- Identificació: Ídem. Format net i professional, adaptat a l'estàndard del sector.

**2. Perfil professional / resum**
- Síntesi del valor del candidat: 3-5 frases nominals que argumenten el valor del candidat, amb paraules clau del sector i quantificació si és possible.

**3. Formació**
- Trajectòria acadèmica: Formació presentada amb relació explícita a les competències i al perfil professional. Distinció formació reglada / complementària.

**4. Experiència professional**
- Trajectòria laboral: Entrades amb funcions detallades, resultats quantificats si és possible ("Increment de les vendes en un 15%", "Atenció a 50+ clients diaris"). Relació explícita amb les competències del perfil.

**5. Competències lingüístiques**
- Plurilingüisme del candidat: Format complet: llengua, nivell MECR, certificació, context d'ús professional si és rellevant.

**6. Competències digitals i altres**
- Habilitats transversals: Competències digitals amb nivell i evidència si és possible. Competències transversals argumentades amb exemples breus.

**7. Altres (voluntariat, formació complementària, publicacions)**
- Perfil ampli del candidat: Inclou voluntariat, publicacions o premis si consoliden el perfil professional. Format consistent amb la resta del CV.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés de construcció del CV: "El meu CV argumenta per què soc el candidat adequat per a aquesta oferta concreta."

### B2 — Acadèmic


### C1+ — Crític


