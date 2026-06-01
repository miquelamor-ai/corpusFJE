---
name: generate-esquema-visual
description: Instrument de mediació visual que extreu l'estructura del text adaptat
  en forma de diagrama jeràrquic (arrel + ramificacions). Reforça la comprensió de
  relacions seqüencials, causa-efecte o jerarquia. Rúbrica gradada 5 passos × 6 nivells
  MECR.
author: FJE — Fundació Jesuïtes Educació
version: 1.0.0-canonic
tools_required: []
agent_role: complements
complement_key: esquema_visual
triggers:
- path: params.complements.esquema_visual
  equals: true
mecr_range:
- pre-A1
- A1
- A2
- B1
- B2
- C1
multimodal: true
moduls_relacionats:
- M2
- M3
- M5
font_canonic: M3_instrument-generar-esquema-visual.md
font_version: 1.0.0-canonic
generat_at: '2026-06-01'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 153f17d80ff1c914
---

# Generar esquema visual — skill operativa per a LLM

L'esquema visual és un instrument de **mediació estructural**. Extreu del text adaptat la xarxa d'idees principals i les organitza en un diagrama jeràrquic amb una arrel (concepte central) i ramificacions (subtemes, passos, causes/conseqüències). El frontend ATNE renderitza el diagrama com a SVG (Mermaid flowchart) a partir d'una llista Markdown amb sagnia.

**Tipologia MALL**: Mediació estructural (suport).
**HCL principal**: Categoritzar — distingir el central del perifèric.
**HCL secundàries**: Ordenar (seqüència), Relacionar (causa-efecte), Identificar (parts d'un tot).
**Principi rector**: *"L'esquema visualitza la idea, no la suplanta"* — un bon esquema ajuda a recordar; un esquema sobrecarregat substitueix la lectura.

**Connexions MALL transversals:**
- *Multimodalitat (DUA Representació)*: l'esquema ofereix una via complementària de comprensió per a l'alumnat amb dificultats de seqüenciació textual o memòria de treball.
- *Bastida retirable*: a primària inicial, el docent presenta l'esquema com a mapa de lectura previ; a B1+, l'alumne el reprodueix per si mateix; a B2+, l'alumne en construeix de propis.
- *No-substitut de mapa conceptual*: l'esquema visual representa estructura **lineal o jeràrquica** (passos, parts, seqüències); el mapa conceptual representa **relacions etiquetades** entre nodes (cau-efecte, sinonímia, oposició). Tots dos coexisteixen al canon.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Descriu l'esquema visual **per a la LECTURA** de l'alumne (mediació presentada per l'eina/docent). NO descriu la producció autònoma de l'alumne (això és tasca dels SKILLs `generate-bastides-lectura` i `generate-rubriques`).

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Concepte central (arrel)**
- Selecció: El concepte més imatge-amigable del text. Sovint un objecte concret amb pictograma.
- Format de la cel·la arrel: Una sola paraula o frase de 2 paraules amb pictograma al costat.

**2. Nombre de nodes**
- Total nodes: 2-3 nodes. Seqüències temporals bàsiques (abans→després) o relacions imatge→paraula.
- Profunditat de l'arbre: 1 nivell (arrel + fills directes).

**3. Format de presentació**
- Marcat textual: Llista markdown amb guions `-` i sagnia de 2 espais per nivell. PICTOGRAMES inline obligatoris a l'arrel i a les fulles principals.
- Format prohibit: NO fletxes Unicode (→, ↓, ↔). NO ASCII-art (|, ├, └, ─). NO emojis decoratius.

**4. Tipus de relacions**
- Predominant: Seqüència temporal simple o relació part-tot.
- Etiquetes a les connexions: No (només estructura).

**5. Criteris transversals**
- Una sola arrel: Una sola arrel per esquema. Sense múltiples nodes a profunditat 0.
- Node central canònic: A gèneres procedimentals (instructiu/receptari/manual): el node central és el PRODUCTE/OBJECTIU final, NO un apartat seqüencial. A gèneres expositius: el TEMA principal. A gèneres narratius: NO s'aplica esquema visual.
- No-soroll visual: Cap node decoratiu sense informació.
- Fidelitat al text font: Cada node ha de poder traçar-se a una frase o concepte del text adaptat.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He mirat l'esquema quan no entenia com es connectaven les coses."

### A1 — Inicial


**1. Concepte central (arrel)**
- Selecció: El subjecte/tema principal explícit del títol.
- Format de la cel·la arrel: Una sola paraula clau.

**2. Nombre de nodes**
- Total nodes: 3-4 nodes. Enumeració de qualitats o parts d'un objecte (descripció simple).
- Profunditat de l'arbre: 1-2 nivells.

**3. Format de presentació**
- Marcat textual: Llista markdown amb guions `-` i sagnia 2 espais. Pictogrames recomanats per a fulles concretes.
- Format prohibit: Idem.

**4. Tipus de relacions**
- Predominant: Enumeració paral·lela (germans).
- Etiquetes a les connexions: No.

**5. Criteris transversals**
- Una sola arrel: Idem.
- Node central canònic: Idem.
- No-soroll visual: Idem.
- Fidelitat al text font: Idem.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He buscat l'arrel quan no entenia de què parlava el text."

### A2 — Funcional


**1. Concepte central (arrel)**
- Selecció: El tema principal o producte final del text.
- Format de la cel·la arrel: Una frase nominal curta (1-4 paraules).

**2. Nombre de nodes**
- Total nodes: 4-6 nodes. Seqüència de passos d'instrucció o esdeveniments cronològics.
- Profunditat de l'arbre: 2 nivells (arrel → branca → fulla).

**3. Format de presentació**
- Marcat textual: Llista markdown amb guions `-` i sagnia 2 espais.
- Format prohibit: Idem.

**4. Tipus de relacions**
- Predominant: Seqüència cronològica o passos numerats.
- Etiquetes a les connexions: Opcional ("primer", "després").

**5. Criteris transversals**
- Una sola arrel: Idem.
- Node central canònic: Idem.
- No-soroll visual: Idem.
- Fidelitat al text font: Idem.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He fet servir l'esquema per recordar l'ordre dels passos."

### B1 — Estratègic


**1. Concepte central (arrel)**
- Selecció: El concepte abstracte o procés que organitza el text.
- Format de la cel·la arrel: Frase nominal (3-6 paraules).

**2. Nombre de nodes**
- Total nodes: 6-8 nodes. Relacions causa-efecte o hipòtesi-evidència.
- Profunditat de l'arbre: 2-3 nivells.

**3. Format de presentació**
- Marcat textual: Idem.
- Format prohibit: Idem.

**4. Tipus de relacions**
- Predominant: Causa-efecte explícita o hipòtesi-evidència.
- Etiquetes a les connexions: Etiquetes amb connectors lògics (perquè, llavors).

**5. Criteris transversals**
- Una sola arrel: Idem.
- Node central canònic: Idem.
- No-soroll visual: Idem.
- Fidelitat al text font: Idem (i a derivacions justificades a B1+).

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He revisat l'esquema per veure quina idea és central i quines són secundàries."

### B2 — Acadèmic


**1. Concepte central (arrel)**
- Selecció: El concepte clau analític del text.
- Format de la cel·la arrel: Concepte abstracte expressat amb 1-2 paraules tècniques.

**2. Nombre de nodes**
- Total nodes: 8-12 nodes amb subnivells. Estructures complexes amb arrel + branques + sub-branques.
- Profunditat de l'arbre: 3 nivells.

**3. Format de presentació**
- Marcat textual: Idem.
- Format prohibit: Idem.

**4. Tipus de relacions**
- Predominant: Categorització jeràrquica abstracta.
- Etiquetes a les connexions: Etiquetes amb connectors causals/contrastius.

**5. Criteris transversals**
- Una sola arrel: Idem.
- Node central canònic: Idem.
- No-soroll visual: Idem.
- Fidelitat al text font: Idem.

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He construït el meu propi esquema d'un text similar per veure si entenia l'estructura."

### C1+ — Crític


**1. Concepte central (arrel)**
- Selecció: El concepte estructurant del discurs (no necessàriament explícit).
- Format de la cel·la arrel: Concepte abstracte amb possible distinció disciplinar.

**2. Nombre de nodes**
- Total nodes: 10-15 nodes amb 3-4 nivells de profunditat. Estructures conceptuals amb categories i sub-categories.
- Profunditat de l'arbre: 3-4 nivells.

**3. Format de presentació**
- Marcat textual: Idem.
- Format prohibit: Idem.

**4. Tipus de relacions**
- Predominant: Estructures discursives complexes (tesi-arguments-refutació).
- Etiquetes a les connexions: Etiquetes amb metallenguatge ("contraargument", "pressupòsit").

**5. Criteris transversals**
- Una sola arrel: Idem.
- Node central canònic: Idem.
- No-soroll visual: Idem.
- Fidelitat al text font: Idem (els meta-discursius sí entren).

**6. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He reflexionat sobre si l'esquema captura l'estructura argumental real del text o és una simplificació."

