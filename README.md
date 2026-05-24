# Corpus RAG — Jesuïtes Educació (FJE)

Corpus de coneixement pedagògic per alimentar assistents d'IA basats en RAG (Retrieval-Augmented Generation) per a la Fundació Jesuïtes Educació.

---

## Per a què

Aquest corpus és la **base de coneixement** que els assistents d'IA consulten per donar respostes fonamentades i contextualitzades als docents de les 8 escoles FJE. Està pensat per ser indexat en un vector store (chunks de 200-300 tokens) i recuperat mitjançant similitud semàntica.

### Assistents previstos

| # | Assistent | Funció |
|---|-----------|--------|
| 1 | Disseny curricular | Programacions, escenaris d'aprenentatge, seqüències didàctiques |
| 2 | Materials didàctics | Creació i adaptació de materials a la diversitat de l'alumnat |
| 3 | Avaluació | Instruments, feedback, informes |
| 4 | Convivència i tutoria | Acompanyament, dinàmiques de grup, tutoria ignasiana |
| 5 | Gestió i organització | Planificació de centre i aula |

L'assistent pilot (en desenvolupament) és el d'**adaptació de materials**, que cobreix tots els perfils de diversitat: nouvinguts, TEA, TDAH, altes capacitats, discapacitats, NESE, etc.

---

## Què conté

**Fitxers Markdown** organitzats en mòduls temàtics:

| Mòdul | Nom | Exemples |
|-------|-----|----------|
| **M0** | Identitat i Missió | PPI, *cura personalis*, educador samarità, ecologia integral |
| **M1** | Subjecte — A qui ensenyem? | Perfils: TEA, TDAH, nouvingut, altes capacitats, discapacitats |
| **M2** | Mètode — Com ensenyem? | DUA, aprenentatge cooperatiu, ABP, gamificació, multinivell |
| **M3** | Llengua — Com vehiculem? | TIL, TILC, MECR, lectura fàcil, translanguaging, català L2 |
| **M4** | Contingut Curricular | Adaptació curricular, competències bàsiques |
| **M5** | Tecnopedagogia | IA educativa, TPACK, accessibilitat digital, prompt engineering |
| **M6** | Avaluació | Avaluació formativa, feedback, portafoli, coavaluació |
| **M7** | Entorn i Família | Benestar emocional, enfocament restauratiu, famílies |
| **M8** | Governança i Seguretat | GDPR, ètica algorítmica, Reglament europeu IA |
| **M9** | Normativa | Decrets d'inclusió, drets alumnat, normativa lingüística |
| **M10** | Marc d'Integració de la IA (projecte FJE) | Marc general, full de ruta, polítiques, protocols, llistes, guies, casuística per col·lectiu, FAQs |

Cada fitxer segueix el patró de nom `M{N}_{nom-descriptiu}.md`.

### Distinció entre M0–M9 i M10

**M0–M9** són el **corpus pedagògic** (coneixement de domini per a docents, RAG, formació). Documents tipus perfil, marc conceptual, protocol pedagògic, estratègia, instrument o normativa externa.

**M10** és el **corpus institucional del projecte d'integració de la IA a FJE**: documents operatius i de governança que tradueixen el marc en pràctica institucional. Tipus pla-desplegament, marc-institucional, política, protocol-operatiu, guia-audiència, casuística, FAQ.

Tots dos servei per a (a) alimentar assistents IA via RAG i (b) consulta directa de docents, directius i personal de gestió.

---

## Com està estructurat cada fitxer

Tots els fitxers tenen la mateixa arquitectura de **dues capes**:

### Frontmatter YAML

```yaml
---
modul: M1
titol: "Alumnat amb TEA"
tipus: perfil
descripcio: "Trastorn de l'Espectre Autista: característiques, estratègies, detecció i suports"
etapa: [infantil, primaria, eso, batxillerat]
paraules_clau: [TEA, autisme, neurodiversitat, inclusió]
fonts: 20
generat_at: "2026-03-22"
review_status: esborrany
---
```

### CAPA 1 — Contingut pedagògic

El contingut varia segons el **tipus** de document:

| Tipus | Pregunta clau | Seccions principals |
|-------|---------------|---------------------|
| **perfil** | Qui és? | Descripció, manifestació per etapa, barreres, necessitats, fortaleses, senyals, comorbiditats, principis, línies vermelles |
| **marc** | Per què? | Definició, fonament, autors, exemples concrets, errors habituals, matisos |
| **protocol** | Com (pas a pas)? | Context, prerequisits, fases (acció/responsable/temps/eines/resultat), rols, indicadors d'èxit |
| **estrategia** | Com (flexible)? | Fonament, per a qui, recursos, 3 nivells d'implementació, adaptacions, errors |
| **eina** | Amb què? | Propòsit, components, guia pas a pas, exemple completat, adaptacions |
| **normativa** | Dins quin marc? | Àmbit, vigència, contingut amb citacions, obligacions, drets, implicacions pràctiques |

### CAPA 2 — Intel·ligència de l'agent (universal)

Aquesta capa és comuna a tots els fitxers i és la que l'agent d'IA utilitza per raonar:

- **Connexions** — 5-10 documents del corpus relacionats, amb motiu
- **Detecció** — Senyals observables: per al docent, per a l'alumne, del context, anti-senyals
- **Heurístiques** — Regles de raonament amb exemples narratius de 80+ paraules (mínim 5 per al docent H1-H5, 3 per a l'alumne H6-H8)
- **Fonts** — Totes les fonts originals amb títol i URL

Les heurístiques són **narratives** (no regles IF/THEN), perquè l'agent RAG raona per analogia.

---

## Com s'ha generat

El corpus es construeix amb el pipeline [mineriaRAG](https://github.com/miquelamor-ai/mineriaRAG), un procés Human-in-the-Loop en 5 passos:

```
Scraper/Ingest → Classificació (Gemini) → Revisió humana → Generació RAG (Gemini) → Exportació
```

1. **Extracció**: crawler web (XTEC, Ateneu, AEPD) + ingestió de fitxers locals (PDF, DOCX)
2. **Classificació**: Gemini 1.5 Pro assigna mòdul, subàmbit i tipus amb raonament metacognitiu
3. **Revisió humana**: un pedagog valida o corregeix cada classificació
4. **Generació**: Gemini 1.5 Pro sintetitza el document seguint la plantilla del tipus corresponent
5. **Exportació**: el fitxer .md es copia al corpus

### Fonts originals

- **XTEC Ateneu** — Cursos de formació docent (inclusió, acollida, DTGD, llengües)
- **XTEC Gencat** — Recursos d'acollida i nouvinguts
- **Corpus jesuïta** — Documentació ignasiana, PPI, Preferències Apostòliques Universals
- **AESIA / AEPD** — Regulació IA, protecció de dades
- **Documents locals** — PDFs i materials pedagògics interns FJE

### Validació de qualitat

El corpus es valida amb `audit_corpus.py` (al repo mineriaRAG), que verifica:
- Estructura: frontmatter, camps requerits, codificació UTF-8
- Contingut: paraules suficients, exemples, seccions esperades
- Fonts: secció FONTS, nombre mínim de citacions
- Corrupció: línies blob, duplicats, caràcters estranys

---

## Qui

### Creador i revisor pedagògic

**Miquel Amor** — Responsable de pedagogia i innovació, Fundació Jesuïtes Educació. Programa PASSAREL·LA.

### Organització

**Fundació Jesuïtes Educació (FJE)** — Xarxa de 8 escoles jesuïtes a Catalunya.

El corpus s'inspira en la **pedagogia ignasiana** de la Companyia de Jesús:
- *Cura personalis* — Atenció personalitzada a cada alumne
- Paradigma Pedagògic Ignasiá (PPI) — Context → Experiència → Reflexió → Acció → Avaluació
- Les 4 C — Competent, Conscient, Compassiu, Compromès
- *Magis* — Excel·lència al servei dels altres

### Xarxa internacional

- **EDUCSI** — Sector Educatiu Península Ibèrica (69 escoles)
- **Educate Magis** — Plataforma global d'escoles jesuïtes

---

## Idioma

Tot el corpus està en **català**, orientat a la pràctica docent a Catalunya.

---

## Llicència i ús

Corpus creat per a ús intern de la Fundació Jesuïtes Educació.
