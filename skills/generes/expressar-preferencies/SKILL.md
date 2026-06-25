---
name: expressar-preferencies
description: 'Instrument per expressar preferencies personals (gènere expressiu de
  BICS): preferència principal en 1a persona, referent específic i concret, grau d''intensitat
  i suport multimodal (pictograma + paraula). HCL Valorar/Preferir (BICS). Pre-A1
  SÍ (oral, concret, mediat). Multimodal obligatori. Rubrica gradada 6 passos × 2
  nivells MECR (pre-A1→A1). A A2+ evoluciona cap a write-opinio.'
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
tools_required: []
agent_role: adapter
genre_key: expressar-preferencies
triggers:
- path: params.genere_discursiu
  equals: expressar-preferencies
mecr_range:
- pre_A1
- A1
translanguaging: false
multimodal: true
moduls_relacionats:
- M3
font_canonic: M3_genere-expressar-preferencies.md
font_version: 4.0.0-canonic
generat_at: '2026-06-25'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: ff727a7c217cb3f4
---

# Expressar preferències — skill operativa per a LLM

Expressar preferencies és un genere expressiu de la comunicacio interpersonal basica (BICS) en que l'alumne formula de manera simple i autentica el que li agrada, el que no li agrada i el que prefereix. El seu tret definitori és l'**autenticitat de la veu personal**: la preferència és subjectiva i intransferible. L'alumne no argumenta ni justifica — simplement expressa. Quan l'alumne pot justificar i comparar, el genere evoluciona cap a `write-opinio` (A2+).

**Tipologia MALL**: Expressiva interpersonal (BICS).
**HCL principal**: Valorar/Preferir — manifestar el gust, la preferència o el rebuig personal sobre un referent concret i proper.
**HCL secundaries**: cap a A1 final, petita Justificacio ("M'agrada perquè és...") com a primer tret CALP.
**Nota MALL**: expressar preferencies és la porta d'entrada a la HCL Interpretar/Valorar. A pre-A1 i A1, la preferència es vehicula per BICS i requereix un referent concret, quotidià i visual. No requereix inferència simbolica ni abstracció temporal. A partir de A2, la preferència s'obre a la comparació, la justificació i la perspectiva — és a dir, al CALP de `write-opinio`.
**Pre-A1 SÍ (D6)**: "M'agrada el gat" o "No m'agrada la sopa" son enunciats accessibles oralment fins i tot a fase logografica. El referent és concret i visual. El docent pot mediar amb gest, imatge i pictograma. La preferència no requereix inferència de segon nivell ni abstracció temporal.
**Multimodal obligatori**: pictograma de cara emocional + paraula clau + referent. El suport visual és part del genere, no un afegit: a pre-A1 i A1 la imatge no acompanya el text — li dona sentit.

**Per que fonts academiques per a un genere de BICS:**
- **Common Core W.K.1** (literal: "Use a combination of drawing, dictating, and writing to compose opinion pieces in which they tell a reader the topic or the name of the book they are writing about and state an opinion or preference about the topic or book.") — documenta que expressar-preferencies és un genere curricular autonomous fins i tot a educacio infantil.
- **Kant, *Critica del Judici* §7**: la preferència ("agrado") és un judici subjectiu de la sensació, no un judici de coneixement ni un judici moral. Distinció fonamental: la preferència no s'argumenta (és Wahrhaftig, autentica, pero no es defensa).
- **Habermas, *Teoria de l'accio comunicativa***: la Wahrhaftigkeit (autenticitat) és una de les tres pretensions de validesa del discurs. L'alumne que expressa "M'agrada X" fa una pretensio d'autenticitat, no de veritat objectiva ni de correccio normativa.
- **Toulmin, *The Uses of Argument* (1958)**: la preferència és un claim simple sense warrant: "M'agrada X" (claim), sense "perquè Y" (warrant) a pre-A1/A1. La separació Toulmin claim/warrant és la base per entendre quan la preferència es converteix en opinio.
- **Kuhn, D. (1991): *The Skills of Argument***: el raonament inferencial sobre preferencies (per que m'agrada) apareix a A2+. A pre-A1/A1, el nen pot expressar la preferència sense poder justificar-la. Forçar la justificació a aquests nivells és demanar CALP des d'un context de BICS.

**Connexions MALL transversals:**
- *BICS com a porta al CALP*: expressar-preferencies és el genere mes accessible de l'espectre BICS-CALP. Pero en si mateixa no és trivial: l'autenticitat de la veu personal, el referent concret i la modalitat multimodal son els tres eixos que la fan pedagogicament valuosa.
- *Continuum expressar-preferencies → write-opinio → write-assaig*: els tres generes son un continuum de la HCL Interpretar/Valorar. A pre-A1/A1: preferència sola. A A2/B1: preferència + justificació = opinio. A B2/C1: opinio + refutació + tesi = assaig. El docent pot usar expressar-preferencies com a primer graó d'aquest continuum.
- *Multimodalitat com a primera llengua*: per a l'alumne a fase logografica, el pictograma no és un suport al text — és el text. Expressar preferencies multimodal és el primer genere on la imatge i la paraula son codeterminals.

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **text/instrument d'expressio de preferencies adaptat per a la LECTURA i USE** de l'alumne. **No descriu un genere autònom de produccio escrita complexa**: a pre-A1 és oral i multimodal; a A1 és escrit breu amb suport visual. Principi pedagogic MALL: l'alumne produeix al maxim del seu abast, mediat per l'adult si cal.
**Sub-granularitat dins de pre-A1**: es treballa amb `fase_lectora: logografica` (oral + pictograma, mediat per adult) i `fase_lectora: alfabetica_emergent` (oral + primera paraula escrita).

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Preferència principal**
- 1a persona i directesa: Oral: "M'agrada [X]" / "No m'agrada [X]". Mediat per adult si cal. Pictograma de cara somrient/trista + paraula clau.

**2. Referent específic**
- Concretesa del referent: El referent és un objecte, un animal, un aliment o una activitat quotidiana. Visual i tocable. L'adult el pot mostrar amb imatge o objecte real.

**3. Intensitat o grau**
- Gradacio de la preferència: "Molt" / "una mica" / "gens". L'adult pot mostrar una escala de cares (somrient/neutra/trista) i l'alumne assenyala.

**4. Suport multimodal**
- Imatge + paraula: Pictograma de cara emocional + paraula clau del referent + dibuix o foto si cal. L'adult escriu la paraula, l'alumne assenyala o dicta.

**5. Autenticitat**
- Veu personal: La preferència és propia (no copiada del company o del docent). L'adult verifica amb pregunta: "És el que tu penses, o el que pensa el company?"

**6. Autoavaluacio mediada**
- Metacognicao: Autoavaluacio oral mediada: l'adult pregunta "Has dit el que a TU t'agrada?" i registra la resposta.

### A1 — Inicial


**1. Preferència principal**
- 1a persona i directesa: Escrit: "M'agrada [X]" / "No m'agrada [X]". 1 frase en primera persona. Sense "trobo que" ni "em sembla".

**2. Referent específic**
- Concretesa del referent: El referent és concret i conegut. L'alumne el nomena amb paraules que ja sap. Cap referent abstracte (la pau, la justicia).

**3. Intensitat o grau**
- Gradacio de la preferència: "M'agrada molt X" / "M'agrada una mica X" / "No m'agrada gens X". Gradacio en 3 nivells amb suport pictografic.

**4. Suport multimodal**
- Imatge + paraula: Pictograma de cara emocional + paraula clau del referent escrita per l'alumne. La imatge i la paraula son codeterminals.

**5. Autenticitat**
- Veu personal: La preferència és en primera persona i autentica. No és una descripcio neutra ni una generalitzacio ("tothom agrada X").

**6. Autoavaluacio mediada**
- Metacognicao: "He dit el que a mi m'agrada. He posat el dibuix o la foto del que m'agrada."

### A2 — Funcional


### B1 — Estratègic


### B2 — Acadèmic


### C1+ — Crític


