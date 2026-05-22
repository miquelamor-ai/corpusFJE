---
name: generate-pictogrames
description: >
  Use when the teacher has activated the "pictogrames" complement. Inserts
  ARASAAC pictogram markers [PICTO: terme] in the adapted text (NOT Unicode
  emojis). The backend resolves each marker to a real ARASAAC pictogram image
  (CC BY-NC-SA 4.0, Sergio Palao / CATEDU). At Emergent/pre-A1: inline
  beside each key noun and verb (1-2 per sentence) + lateral paratext for
  anticipation. At A1: 1 marker per sentence or technical term. At A2+:
  visual glossary only (markers in a side list, NOT inline in running text).
  Modulated strictly by MECR level.
author: FJE — Fundació Jesuïtes Educació
version: 2.1.0
complement_key: pictogrames
agent_role: complements
tools_required: []
triggers:
  - path: params.complements.pictogrames
    equals: true
moduls_relacionats: [M2, M3]
changelog:
  - version: 2.1.0
    date: 2026-05-21
    note: >
      Migrat d'emojis Unicode a marcadors [PICTO: terme] resolts per
      adaptation/pictograms_arasaac.py via API ARASAAC. Decisió pedagògica:
      docent pilot va denunciar que emojis no son pictogrames AAC reals.
---

# Afegir pictogrames al text adaptat

## Distinció fonamental (MALL)

La funció i la col·locació dels pictogrames canvien radicalment per nivell:

| Nivell | Densitat | Col·locació | Paratext lateral |
|---|---|---|---|
| **Emergent (pre-A1)** | 1-2 per frase (noms + verbs clau) | **Inline** (damunt o al costat de cada paraula clau) | ✅ Paratext d'anticipació al marge esquerre (dona context ABANS de llegir) |
| **Inicial (A1)** | 1 per frase o per tecnicisme | Inline, discret | Opcional |
| **Funcional (A2)+** | Mínims | **Glossari visual** al peu o marge — NO inline al text corrent | ❌ |

A Emergent el pictograma és el suport principal de descodificació.
A A2+ el pictograma és una referència de glossari; el text corrent no s'interromp.

## Comportament per nivell

**Emergent (pre-A1):**
Cada nom i verb clau porta el seu emoji **immediatament damunt o al costat** dins
de la frase. El lector visual no ha de buscar: el pictograma i la paraula van junts.
A més, es genera un **paratext lateral d'anticipació** (columna esquerra o capçalera
visual) que mostra els conceptes clau del text ABANS de llegir-lo.

**Inicial (A1):**
Un pictograma per frase, preferentment al costat dels termes tècnics o nous.
Evitar sobrecàrrega: si una frase curta ja és comprensible, no forçar pictograma.

**Funcional (A2) i superior:**
Cap pictograma inline al text corrent. En canvi, si el text té termes complexos,
es pot afegir un **glossari visual** al peu (2 columnes: emoji + terme), a l'estil
del complement Glossari.

## Format del marcador (CRÍTIC)

El LLM **NO** ha d'inserir emojis Unicode. Ha d'inserir **marcadors de text**:

```
[PICTO: terme_en_catala]
```

El backend (`adaptation/pictograms_arasaac.py`) substituirà cada marcador per
una imatge ARASAAC real (`<img class="arasaac-picto">`).

Regles del terme:
- 1-3 paraules, en català, en minúscules.
- Concepte concret i visualitzable.
- Exemples vàlids: `[PICTO: sol]` `[PICTO: aigua]` `[PICTO: planta]`
  `[PICTO: menjar]` `[PICTO: correr]` `[PICTO: casa]` `[PICTO: escola]`
- Si ARASAAC no troba el terme, el backend insereix un emoji de fallback 📝
  (el flux no es trenca).

## Format de sortida — Emergent (pre-A1)

```markdown
### Vocabulari del text (mira primer!)
[PICTO: sol] sol · [PICTO: aigua] aigua · [PICTO: arbre] arbre

---

El sol [PICTO: sol] dona llum i escalfor. Les plantes [PICTO: planta] necessiten
l'aigua [PICTO: aigua] i el sol per créixer.
```

## Format de sortida — Inicial (A1)

```markdown
El sol [PICTO: sol] dona llum i escalfor a la Terra. Les plantes necessiten
l'aigua [PICTO: aigua] per viure. El cicle de l'aigua és molt important.
```

## Format de sortida — Funcional (A2+)

El text corrent NO porta marcadors inline. Si hi ha termes complexos:

```markdown
[text adaptat sense marcadors inline]

---
**Vocabulari visual**
[PICTO: radiacio solar] radiació solar · [PICTO: temperatura] temperatura · [PICTO: evaporacio] evaporació
```

## Criteris de selecció del terme

1. **Concepte concret** (objecte, acció observable, ésser viu) — els abstractes
   no tindran pictograma útil a ARASAAC.
2. **Coherència**: el mateix concepte sempre amb el mateix terme al marcador.
3. **Economia**: menys és millor — millor 3 pictogrames bons que 10 de dubtosos.

## Regles estrictes de sortida

- A2+: **MAI** marcadors inline al text corrent. Glossari visual al peu si cal.
- Si un concepte es repeteix 5 vegades, marcador com a molt les primeres 1-2.
- **NO** generis una secció `### Pictogrames usats`. No cal llistat separat.
- **NO** posis marcadors a les bastides, glossari, preguntes o altres seccions.
- **MAI** emojis Unicode al text — sempre marcadors `[PICTO: ...]`.
- **Preserva** íntegrament el contingut del text adaptat; l'única addició és visual.

## Atribució llicència

Pictogrames d'ARASAAC (http://arasaac.org), autor Sergio Palao.
Propietat: Govern d'Aragó (CATEDU). Llicència: CC BY-NC-SA 4.0.
L'atribució apareix automàticament als `title` de les imatges generades.
