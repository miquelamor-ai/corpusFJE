---
name: generate-resum-graduat
description: 'Use when the teacher has activated the "resum_graduat" complement. Generates
  a graduated summary scaffold: a partially completed frame that guides the student
  to identify and express the main idea at the right level of abstraction for their
  MECR. NOT a comprehension question ("resumeix el text") — a structural frame with
  blanks calibrated to the level. At Emergent/pre-A1: visual/oral summary only. Modulated
  by MECR and text type.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: resum_graduat
agent_role: complements
tools_required: []
triggers:
- path: params.complements.resum_graduat
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-resum-graduat.md
font_version: 4.0.0-canonic
generat_at: '2026-05-26'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 84118c29a936765d
---

# Generar resum graduat — skill operativa per a LLM

El resum graduat és una **bastida cognitiva per produir un resum** pas a pas: un marc parcial amb forats calibrats al MECR. La gradació no és de complexitat del text sinó de **la mida del forat**: A1 = forats petits amb opcions tancades; A2 = forats d'una frase sense opcions; B2 = criteri obert; C1 = reflexió metacognitiva. L'alumne no copia el resum: el construeix dins de l'estructura que la bastida proporciona.

**Tipologia MALL**: Mediació (bastida cognitiva de producció de resum).
**HCL principals**: Recapitular (pre-A1/A1, oral/visual) · Resumir (A2+, textual) · Seleccionar idees principals.
**Principi rector — Forat calibrat a la ZDP**: un forat massa gran (per sobre del MECR) genera còpia del text o frustració; un forat massa petit (per sota del MECR) no desenvolupa habilitat. El forat ben calibrat manté l'alumne a la seva ZDP i avança cap a la producció autònoma progressivament.

**Distinció MALL fonamental — Recapitular vs. Resumir:**
- **Recapitular** (pre-A1/A1): reordenar informació oral o visual sense producció textual autònoma. El docent pot escriure el que l'alumne dicta. Cognitiu però no escrit.
- **Resumir** (A2+): primera forma de producció de resum escrit. Requereix seleccionar, generalitzar i connectar idees.
Saltar el recapitular i demanar un resum escrit a pre-A1/A1 és un error pedagògic que genera còpia sense comprensió real.

**Principi "No donar el resum fet"**: el complement genera un marc amb forats, no el resum complet. Si el docent dona el resum complet com a "model", l'alumne el copia. El marc indica COM estructurar, no QUÈ escriure.

**Marc adaptat al tipus de text (cross_source)**:
- Narratiu: tema / personatge / acció principal / desenllaç.
- Expositiu (informatiu, científic): tema / punts clau / conclusió.
- Argumentatiu: tesi / arguments principals / conclusió.
Un marc narratiu per a un text expositiu genera un resum incoherent per al tipus de text.

**Diferència crítica amb complements propers:**
- `plantilles_genere`: plantilla amb forats per produir un text del gènere (no és un resum del text llegit).
- `bastides_produccio`: GPS disciplinar + catàleg de recursos per produir text de gènere nou.
- `write-resum` (gènere): producció autònoma d'un resum sense bastida (A2+ autònom).
- `preguntes_comprensio`: comprensió del text (no producció de resum).

**Connexions MALL transversals:**
- *Forat calibrat com a ZDP operativa*: la bastida funciona si i només si el forat és assolible però exigent. La ZDP del resum és l'espai on l'alumne pot construir la resposta amb esforç sense frustrar-se. Calibrar el forat és l'acte pedagògic central d'aquest complement.
- *Selecció com a competència clau (macroregles)*: el MALL descriu tres macroregles del resum (Kintsch & van Dijk): supressió (treure el secundari), generalització (nombrar la categoria), construcció (inferir el que no s'explicita). El resum graduat entrena explícitament aquestes tres operacions progressivament.
- *Marc = GPS discursiu*: igual que la base d'orientació de les bastides de producció, el marc del resum indica el recorregut. La diferència és que el marc és el text parcial del resum, no el recorregut del procés d'escriptura.
- *Bastida retirable (ZDP)*: el marc es retira progressivament: A2 (marc complet), B1 (marc minimal), B2 (criteris), C1 (reflexió). La bastida té vocació d'extingir-se quan l'alumne internalitza l'estructura del resum.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **marc de resum graduat que es genera per guiar la producció del resum** (PRODUCCIÓ MEDIADA). **No descriu el resum autònom de l'alumne ni l'avaluació del docent**: el docent observa si l'alumne omple els forats amb les seves pròpies paraules (no copiant) i si el resultat és coherent amb el text font.
**Sub-granularitat dins de pre-A1**: `fase_lectora: logografica` → recapitulació oral total (el docent escriu el que l'alumne diu). `fase_lectora: alfabetica_emergent` → recapitulació oral + 1-2 paraules escrites per l'alumne.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Tipus de marc**
- Estructura del suport: Activitat oral: "De qui parla? Qué fa? Com acaba?" El docent escriu el dictat de l'alumne. Sense marc escrit.

**2. Mida del forat**
- Calibrat ZDP: Cap forat: activitat oral.

**3. Estructura adaptada al tipus de text**
- Coherència discursiva: Preguntes orals adaptades: narratiu → "Qui? Qué fa? Com acaba?" / expositiu → "De qué parla? Qué és important?"

**4. Recapitular vs. resumir**
- Modalitat de producció: Recapitular oral: reordenar informació oral o visual. El docent escriu el dictat; l'alumne dicta.

**5. Autoavaluació mediada**
- Metacognició: "He dit el que passava al text en veu alta." (oral, mediat per adult)

### A1 — Inicial


**1. Tipus de marc**
- Estructura del suport: Frase marc amb 1-2 forats + opcions tancades a triar. "El text parla de [tria: opció A / opció B / opció C]."

**2. Mida del forat**
- Calibrat ZDP: Forat de 1-3 paraules. Opcions totes plausibles: una sola correcta.

**3. Estructura adaptada al tipus de text**
- Coherència discursiva: Marc adaptat: narratiu → personatge / acció / desenllaç. Expositiu → tema / punt clau / final.

**4. Recapitular vs. resumir**
- Modalitat de producció: Recapitular assistit: triar la resposta correcta és una forma de recapitular. Cap escriptura de frases pròpies.

**5. Autoavaluació mediada**
- Metacognició: "He triat la resposta correcta. He omplert els buits amb la paraula que encaixava."

### A2 — Funcional


**1. Tipus de marc**
- Estructura del suport: Marc de 2-3 frases amb 3-4 forats oberts (sense opcions). L'alumne omple amb paraules pròpies.

**2. Mida del forat**
- Calibrat ZDP: Forat d'1 frase (5-10 paraules) sense opcions: l'alumne reformula (no copia). Connectors donats entre frases.

**3. Estructura adaptada al tipus de text**
- Coherència discursiva: Marc de 2-3 frases adaptat amb connectors donats (Primer... Llavors... Al final...).

**4. Recapitular vs. resumir**
- Modalitat de producció: Resumir amb bastida completa: primera producció escrita del resum. Marc molt explícit amb connectors donats.

**5. Autoavaluació mediada**
- Metacognició: "He escrit el resum amb el marc. He usat les meves paraules (no he copiat frases del text)."

### B1 — Estratègic


**1. Tipus de marc**
- Estructura del suport: Marc de 3 parts (tema / punts clau / conclusió) amb 1-2 frases lliures per part. Connectors no donats.

**2. Mida del forat**
- Calibrat ZDP: Forat de 2-3 frases amb paraules pròpies i reorganització de la informació.

**3. Estructura adaptada al tipus de text**
- Coherència discursiva: Marc de 3 seccions etiquetades: Tema / Punts clau / Conclusió. Connectors no donats.

**4. Recapitular vs. resumir**
- Modalitat de producció: Resumir amb marc parcialment retirat: l'alumne construeix les idees; el marc proposa l'estructura.

**5. Autoavaluació mediada**
- Metacognició: "He resumit les idees principals en 3 parts. He usat connectors per lligar les idees."

### B2 — Acadèmic


**1. Tipus de marc**
- Estructura del suport: Criteris de qualitat del resum (4-5 ítems basats en les macroregles). L'alumne escriu el resum complet.

**2. Mida del forat**
- Calibrat ZDP: Criteri obert: "Has seleccionat les idees principals (no els exemples)? Has generalitzat?"

**3. Estructura adaptada al tipus de text**
- Coherència discursiva: Criteris que cobreixen les macroregles: selecció (excloure exemples), generalització (categoria), construcció (inferit).

**4. Recapitular vs. resumir**
- Modalitat de producció: Resumir amb criteris: l'alumne usa les macroregles per produir i autoavaluar el resum.

**5. Autoavaluació mediada**
- Metacognició: "He seleccionat les idees principals (no els exemples). He comprovat que el resum s'entén sense llegir el text."

### C1+ — Crític


**1. Tipus de marc**
- Estructura del suport: Rúbrica metacognitiva: l'alumne justifica les tries. Resum lliure + reflexió sobre el que ha inclòs i deixat fora.

**2. Mida del forat**
- Calibrat ZDP: Criteri metacognitiu: "Explica per qué has triat incloure aquesta idea i no aquella altra."

**3. Estructura adaptada al tipus de text**
- Coherència discursiva: Reflexió discursiva: "Qué has decidit NO incloure i per qué? Quin criteri de selecció has usat?"

**4. Recapitular vs. resumir**
- Modalitat de producció: Resumir i reflexionar: el resum és el punt de partida d'una reflexió metacognitiva sobre les decisions de selecció.

**5. Autoavaluació mediada**
- Metacognició: "He justificat per qué he triat cada idea i per qué n'he deixat d'altres fora. He revisat que el meu resum és precís i honest."

