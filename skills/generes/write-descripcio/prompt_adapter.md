---
tipus: derivat
font_canonic: M3_genere-escriure-descripcio.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-25'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: add77b7c71a804e8
---

# Escriure/adaptar una descripció — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una descripció per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Precisió i situació**: Assenyalar i dir el nom oralment. Dictat a l'adult.
- **Seqüència i coherència**: Llista oral de noms (parts assenyalades a la imatge o objecte real).
- **Varietat i precisió**: Pictograma o imatge en lloc d'adjectius escrits.
- **Accessibilitat i precisió**: Assenyalar l'objecte real o la imatge (sense text).
- **Distinció i organització**: Enumeració oral de parts (sense separació).
- **Llargada**: Enumeració oral. Dictat a l'adult (format llista).
- **Adjectius subjectius**: Cap adjectiu subjectiu (ni oral ni escrit). Tots referits a la imatge real.
- **Fidelitat al text font**: Fidelitat a les parts visibles de l'objecte o imatge presentat.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Precisió i situació**: 1 frase que diu què és: "Això és un ocell."
- **Seqüència i coherència**: 3-4 característiques ordenades de dalt a baix o de fora a dins. Una per frase.
- **Varietat i precisió**: Adjectius molt freqüents i concrets: "vermell", "gran", "rodó".
- **Accessibilitat i precisió**: Comparacions molt quotidianes: "és com una pilota", "és del color del cel".
- **Distinció i organització**: Descripció física únicament. Una característica per frase.
- **Llargada**: 3-4 frases. Format llista o frases simples.
- **Adjectius subjectius**: Cap adjectiu valoratiu genèric ("bonic", "especial"). Tots concrets i verificables.
- **Fidelitat al text font**: Fidelitat a les característiques principals de l'objecte o persona descrits.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Precisió i situació**: Frase general que situa l'objecte amb categoria: "El colibrí és un ocell molt petit."
- **Seqüència i coherència**: 5-6 característiques en ordre espacial explícit amb connectors simples.
- **Varietat i precisió**: Adjectius variats i concrets. Sense subjectius genèrics ("bonic", "interessant").
- **Accessibilitat i precisió**: Comparacions concretes i variades: "de la mida d'una mà", "tan llarg com un llapis".
- **Distinció i organització**: Distinció incipient entre descripció física i descripció funcional en frases separades. Al menys una frase conté el connector "serveix per" o "s'utilitza per".
- **Llargada**: 5-6 frases o 1-2 paràgrafs curts.
- **Adjectius subjectius**: Idem.
- **Fidelitat al text font**: Fidelitat a les característiques i a la funció essencial.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Precisió i situació**: Descripció general amb categoria i 1 tret diferencial: "El colibrí és un ocell diminut conegut pel seu vol estacionari."
- **Seqüència i coherència**: 6-8 característiques amb ordre espacial clar i progressiu. Connectors: "a la part superior", "al centre".
- **Varietat i precisió**: Adjectius precisos i variats del camp lèxic de la unitat. Sense superlatius sintètics.
- **Accessibilitat i precisió**: Comparacions funcionals: "té X, que permet Y". Pot comparar amb elements de la mateixa categoria.
- **Distinció i organització**: Separació explícita entre descripció física i funció o impacte en paràgrafs o blocs diferenciats.
- **Llargada**: 1-2 paràgrafs amb 6-8 característiques.
- **Adjectius subjectius**: Idem.
- **Fidelitat al text font**: Fidelitat a les característiques, la funció i el to factual del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Precisió i situació**: Descripció general amb context i funció integrats.
- **Seqüència i coherència**: Ordre espacial respectat amb matisos i descripció funcional integrada.
- **Varietat i precisió**: Adjectius precisos del camp lèxic de la matèria. Superlatius analítics admissibles.
- **Accessibilitat i precisió**: Comparació amb altres elements de la mateixa categoria amb matís.
- **Distinció i organització**: Descripció física, funcional i emocional ben diferenciades.
- **Llargada**: 2-3 paràgrafs complets.
- **Adjectius subjectius**: Idem. Superlatius d'ordre espacial o quantitatiu admissibles si son terminologia ("el punt més alt", "la zona més densa").
- **Fidelitat al text font**: Fidelitat a les característiques, la funció, el context i el to.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Precisió i situació**: Descripció general amb matisos conceptuals i terminologia precisa.
- **Seqüència i coherència**: Ordre espacial exhaustiu amb matisos conceptuals i terminologia específica de la disciplina.
- **Varietat i precisió**: Adjectius tècnics i de matís conceptual. Terminologia disciplinar.
- **Accessibilitat i precisió**: Comparació de l'objecte amb arquetips o fenòmens de la mateixa disciplina per precisar-ne el matís diferencial.
- **Distinció i organització**: Distinció terminològica entre descripció observable i processos subjacents.
- **Llargada**: Text complet amb tots els matisos necessaris.
- **Adjectius subjectius**: Idem. Terminologia valorativa disciplinar admissible si s'usa en el camp lèxic corresponent.
- **Fidelitat al text font**: Fidelitat a la complexitat descriptiva del text original, incloent matisos i terminologia.

