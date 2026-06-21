---
name: generate-illustracions
description: 'Use when the teacher has activated the "illustracions" complement (BETA).
  Instructs the LLM to insert [IMATGE: <concepte curt en català>] markers at key visual
  points in the adapted text. The BACKEND resolves each marker via a 3-step pipeline:
  (1) Wikimedia Commons search, (2) FLUX fallback, (3) skip if not renderable. The
  LLM only places markers; it does NOT write English briefs — that''s the backend''s
  job.

  '
author: FJE — Fundació Jesuïtes Educació
version: 4.0.0-canonic
complement_key: illustracions
agent_role: complements
tools_required:
- name: image_generation
  provider: pollinations
  endpoint: https://image.pollinations.ai/prompt/{prompt}
  model: flux
  params:
    enhance: false
    safe: true
    private: true
    width: 1024
    height: 768
    nologo: true
    referrer: atne-fje
    seed_strategy: document
  positive_suffix: Single clear focal point, clean composition, soft cream paper background,
    no text, no letters, no captions, no signage.
  default_preset: aquarela_storybook
  style_presets:
    vectorial_editorial:
      label_ca: Vectorial editorial pla
      spine: Flat vector illustration, clean geometric shapes, bold simple outlines,
        limited flat color palette, smooth shapes, friendly editorial style, no gradients,
        no texture, centered composition.
      default_for:
        mecr:
        - B1
        - B2
        - C1
        - C2
        subjects:
        - socials
        - ciutadania
        - economia
        - filosofia
        - llengua
    isometric_infografic:
      label_ca: Isomètric infogràfic
      spine: Isometric 3D illustration, 30 degree angle, clean geometric shapes, crisp
        edges, limited color palette with soft pastels, subtle shading, infographic
        textbook style, high clarity.
      default_for:
        mecr:
        - A2
        - B1
        - B2
        - C1
        - C2
        subjects:
        - tecnologia
        - fisica
        - quimica
        - biologia_sistemes
        - matematiques
    aquarela_storybook:
      label_ca: Aquarel·la storybook
      spine: Soft watercolor storybook illustration, gentle wet-edge washes, warm
        palette of ochre sap green and dusty blue, hand-drawn feel, cozy lighting,
        loose brushwork, paper texture background, children book aesthetic.
      default_for:
        mecr:
        - A1
        - A2
        subjects:
        - literatura
        - contes
        - ciencies_naturals_primaria
        - religio
        contexts:
        - lectura_facil
        - nouvinguts
        - primaria_inicial
        - primaria_mitja
    icona_minimalista:
      label_ca: Icona minimalista
      spine: Minimalist flat icon, single concept, centered, thick rounded outlines,
        two or three flat colors, solid shapes, no gradient, generous padding, pictogram
        style, high legibility.
      default_for:
        contexts:
        - dua_acces
        - vocabulari_abstracte
        - glossari_visual
    claymation_plastilina:
      label_ca: Claymation plastilina
      spine: Handmade claymation style, stop-motion plasticine figures, soft studio
        lighting, visible fingerprint texture, saturated but warm colors, shallow
        depth of field, tabletop scene, cheerful children's educational look.
      default_for:
        mecr:
        - A1
        - A2
        - B1
        contexts:
        - primaria_stem_ludic
        - infantil
    escala_grisos_carbonet:
      label_ca: Escala de grisos (carbonet)
      spine: Monochrome charcoal and graphite drawing, soft grey tones, hand-drawn
        on textured cream paper, expressive loose lines, subtle cross-hatching, high
        contrast, no color, editorial book illustration style, dignified historical
        feel.
      default_for:
        subjects:
        - historia
        - filosofia
        - literatura_classica
        contexts:
        - impressio_bn
        - baixa_visio_contrast
    fotografia_documental:
      label_ca: Fotografia documental
      spine: Vintage documentary photograph, warm sepia and amber tones, 35mm film
        grain, natural soft window light, shallow depth of field, authentic atmosphere,
        editorial photojournalism style, slight age patina.
      default_for:
        subjects:
        - natura
        - arquitectura
        - geografia
        - ciencies_actuals
      restrictions:
        require_caption: Il·lustració IA
        people_framing: wide_or_silhouette_only
        forbidden_framings:
        - close_up
        - portrait
        - waist_up_with_people
        rationale: Les fotos IA amb persones en primer pla poden confondre's amb documents
          reals. Plans amplis, mitjana distancia o silueta son segurs. Sempre exportar
          amb caption "Il·lustració IA".
triggers:
- path: params.complements.illustracions
  equals: true
moduls_relacionats:
- M2
- M3
font_canonic: M3_instrument-generar-illustracions.md
font_version: 4.0.0-canonic
generat_at: '2026-06-21'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 85ecf87c5bfb6c03
---

# Generar il·lustracions — skill operativa per a LLM

El complement d'il·lustracions insereix marcadors `[IMATGE: concepte curt en catala]` al text adaptat perquè es resolguin en imatges. Es proven tres vies en ordre: Wikimedia Commons (imatges reals amb llicencia lliure), FLUX.1-schnell (generació IA), skip (si el concepte no és visualitzable). La il·lustració no decora — ancla conceptes que son difícils de descriure verbalment.

**Tipologia MALL**: Mediacio (suport multimodal cognitiu).
**HCL associada**: cap HCL productiva — el complement suporta l'acces i l'ancoratge conceptual del text.
**Principi rector**: menys és mes. Cada il·lustració afegeix carrega cognitiva de processament visual. A B2-C1, una il·lustració sense valor informatiu addicional distreu en lloc d'ancorar.
**Feature BETA**: qualitat no garantida; demora de 1-3 minuts per imatge; el docent sempre pot substituir o regenerar.

**Format del marcador:**
```
[IMATGE: concepte curt en catala]
```
- Delimitadors obligatoris: `[IMATGE:` a l'inici, `]` al final.
- Idioma: catala. Es tradueix si cal.
- En linia propia, DAVANT del paragraf on s'introdueix el concepte (pre-A1/A1) o al costat (A2+).
- Longitud: 3-8 paraules. Concepte nuclear, no descripcio d'escena.
- Mai dins de llistes, taules, bastides, glossaris, pictogrames o altres complements.
- Mai incloure estil, paleta, viewpoint o enquadrament (s'afegeix automaticament).

**Els 7 presets d'estil** (el docent tria al Pas 2; si no, s'aplica el default per MECR + assignatura):

| Preset | Per a qui / quan |
|---|---|
| Aquarel·la storybook | Primaria, LF, nouvinguts, literatura, A1-A2 |
| Vectorial editorial pla | ESO+, humanitats, conceptes abstractes, B1+ |
| Isometric infografic | STEM, processos, sistemes, diagrames, A2+ |
| Icona minimalista | DUA Acces, vocabulari abstracte, glossari visual |
| Claymation plastilina | Primaria STEM ludic, infantil, A1-B1 |
| Escala de grisos (carbonet) | Historia, filosofia, impressio B/N, baixa visio |
| Fotografia documental | Natura, arquitectura, geografia, ciencia actual |

**Diferencia clau amb pictogrames:**
- **Pictogrames**: sistema AAC (emojis o ARASAAC), vocabulari, referencia lexica, TEA/CAA.
- **Il·lustracions**: ancoratge conceptual de processos, sistemes, llocs, escenes; no és AAC.

**Connexions MALL transversals:**
- *Imatge com a bastida d'acces (pre-A1/A1)*: l'alumne nouvingut que no coneix "fotosintesi" pot aprendre el concepte si veu la imatge PRIMER. La sequencia imatge → paraula és la logica de l'aprenentatge, no la del text.
- *Imatge com a ampliacio cognitiva (B1+)*: als nivells alts, la il·lustració no simplifica — complexifica. Un diagrama pot donar en un cop d'ull la informacio que requereix 3 paragraf de text. L'ampliacio és el valor afegit, no la simplificacio.
- *Preset com a coherencia de registre*: triar el preset adequat al context (aquarel·la per a primaria, vectorial per a ESO) és una decisio pedagogica sobre el registre visual. Un poema il·lustrat amb infografic isometric envia un missatge contradictori.

**Aclariment d'us — que descriu aquesta rubrica.**
Aquesta rubrica descriu el **complement d'il·lustracions generat per al text adaptat**. **No descriu la produccio autonoma de l'alumne**: els marcadors s'insereixen al text adaptat i les imatges es generen automàticament. El registre d'us és del docent (observacio de si l'alumne usa el suport visual durant la lectura).

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Nombre d'il·lustracions**
- Densitat: Maxim 4-5. Una per idea principal. Alta densitat justificada (text ≈ imatge).

**2. Posicio al text**
- Anticipacio vs ancoratge: Imatge DAVANT de la paraula/frase que il·lustra. L'alumne veu la imatge PRIMER. Anticipacio visual.

**3. Especificitat del marcador**
- Concretesa del concepte: Concepte molt concret i universal: "gat", "arbre", "pluja". 1-2 paraules.

**4. Preset d'estil**
- Registre visual: Pictograma o il·lustració clara i simple. Sense elements distractors.

**5. Autoavaluacio mediada**
- Metacognicao: "He vist la imatge i he dit el que era." (oral, mediat per adult)

### A1 — Inicial


**1. Nombre d'il·lustracions**
- Densitat: 3-4 il·lustracions. Una per paragraf o per concepte clau.

**2. Posicio al text**
- Anticipacio vs ancoratge: Imatge immediatament DAVANT o AL COSTAT del concepte clau.

**3. Especificitat del marcador**
- Concretesa del concepte: Concepte concret: "cel·lula animal", "volca en erupcio". 1-3 paraules.

**4. Preset d'estil**
- Registre visual: Il·lustracò o foto realista. Molt clara, sense text a la imatge.

**5. Autoavaluacio mediada**
- Metacognicao: "He mirat la imatge i m'ha ajudat a entendre la paraula difícil."

### A2 — Funcional


**1. Nombre d'il·lustracions**
- Densitat: 2-3 il·lustracions. Als punts de maxim ancoratge conceptual.

**2. Posicio al text**
- Anticipacio vs ancoratge: Imatge al costat del concepte que ancora, dins del paragraf.

**3. Especificitat del marcador**
- Concretesa del concepte: Concepte concret + context: "fotosintesi a fulla verda". 2-4 paraules.

**4. Preset d'estil**
- Registre visual: Foto realista o il·lustracó educativa. Pot tenir etiquetes simples.

**5. Autoavaluacio mediada**
- Metacognicao: "La imatge m'ha ajudat a entendre el proces o el concepte."

### B1 — Estratègic


**1. Nombre d'il·lustracions**
- Densitat: 1-2 il·lustracions als conceptes abstractes o processos clau.

**2. Posicio al text**
- Anticipacio vs ancoratge: Imatge al concepte abstracte o al proces que beneficia d'ancoratge visual.

**3. Especificitat del marcador**
- Concretesa del concepte: Concepte especific del contingut: "cadena trofica marina", "cambra del parlament".

**4. Preset d'estil**
- Registre visual: Diagrama o foto cientifica/geografica. Etiquetes disciplinars.

**5. Autoavaluacio mediada**
- Metacognicao: "He identificat quins conceptes necessitaven imatge i quins no."

### B2 — Acadèmic


**1. Nombre d'il·lustracions**
- Densitat: 1-2 il·lustracions molt selectives (diagrama, proces, dada visual clau).

**2. Posicio al text**
- Anticipacio vs ancoratge: Imatge estrategica: diagrama d'un proces, taula de dades, mapa conceptual visual.

**3. Especificitat del marcador**
- Concretesa del concepte: Concepte disciplinar: "diagrama de l'aparell respiratori", "mapa de la Revolucio Francesa".

**4. Preset d'estil**
- Registre visual: Diagrama, mapa, grafic. Llegenda si cal.

**5. Autoavaluacio mediada**
- Metacognicao: "He usat les il·lustracions com a suport visual per a conceptes que no s'expliquen facilment amb paraules."

### C1+ — Crític


**1. Nombre d'il·lustracions**
- Densitat: 0-1 il·lustració. Reservada per a diagrames o infografies que condensin dades.

**2. Posicio al text**
- Anticipacio vs ancoratge: Imatge de suport a l'argument: infografia, grafic, mapa.

**3. Especificitat del marcador**
- Concretesa del concepte: Concepte complex: "infografia comparativa de sistemes politics", "grafic evolucio PIB".

**4. Preset d'estil**
- Registre visual: Infografia, grafic estadistic, mapa tematic.

**5. Autoavaluacio mediada**
- Metacognicao: — (N/A: a C1 rarament es genera il·lustracó; si es genera, l'autoavaluacio és igual que B2)

