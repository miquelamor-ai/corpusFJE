---
tipus: derivat
font_canonic: M3_genere-escriure-enciclopedic.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-14'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 1432d06cb6eb9d4d
---

# Escriure/adaptar una entrada enciclopèdica — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una entrada enciclopèdica per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Precisió i estructura**: 1 frase ≤10 paraules. Estructura: "X és un Y que Z."
- **Coherència lògica**: Test: la definició no usa el terme per definir-se. Criteri bàsic.
- **Estructura lògica**: Categoria explícita a la primera paraula de la definició: "és un animal / un lloc / un procés...".
- **Accessibilitat i ancoratge**: 1 exemple molt visual i quotidià. 1 frase.
- **Profunditat i coherència**: 2-3 frases simples amb detalls addicionals del terme. Una característica per frase.
- **Llargada**: Definició (1 frase) + 2-3 frases d'explicació + 1 exemple.
- **Sense remissions**: Cap remissió a altres entrades ("vegeu també...").
- **Sense etimologia inicial**: L'etimologia no substitueix la definició. Si apareix, va darrere de la definició.
- **Fidelitat al text font**: Fidelitat a la categoria i al tret diferencial principals del terme.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Precisió i estructura**: 1 frase clara. Categoria + especificitat. Sense circularitat.
- **Coherència lògica**: Definició que no usa el terme ni paraules de la mateixa arrel.
- **Estructura lògica**: Categoria clara: [Terme] és un [categoria] que [especificitat].
- **Accessibilitat i ancoratge**: 1 exemple concret pres del context immediat de l'alumne. Immediat a la definició.
- **Profunditat i coherència**: 3 frases amb detalls rellevants. Vocabulari accessible.
- **Llargada**: Definició (1 frase) + 3 frases + 1 exemple.
- **Sense remissions**: Idem.
- **Sense etimologia inicial**: Idem.
- **Fidelitat al text font**: Fidelitat a la categoria, al tret diferencial i a l'exemple.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Precisió i estructura**: 1 frase precisa amb terminologia adequada. Sense circularitat ni sinònim com a definició.
- **Coherència lògica**: Definició sense circularitat i sense sinònim com a definició ("la democràcia és un govern popular" és circular si no s'explica "popular").
- **Estructura lògica**: Categoria i especificitat ben diferenciades. La categoria situa el terme dins d'una classe superordinal.
- **Accessibilitat i ancoratge**: Exemple concret + contraexemple si és útil per delimitar el concepte.
- **Profunditat i coherència**: 3-4 frases amb relació entre característiques. 1 terme tècnic nou introduït.
- **Llargada**: Definició + 3-4 frases + exemple + contraexemple si escau.
- **Sense remissions**: Idem.
- **Sense etimologia inicial**: Idem.
- **Fidelitat al text font**: Fidelitat a la categoria, al tret diferencial, a l'exemple i al to factual.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Precisió i estructura**: 1 frase completa amb terminologia específica de la matèria. Pot delimitar el terme respecte a termes propers.
- **Coherència lògica**: Idem. La delimitació respecte a termes propers s'explicita a l'Explicació ampliada (Pas 5), no a la definició nuclear.
- **Estructura lògica**: Categoria dins del camp lèxic de la matèria amb precisió disciplinar.
- **Accessibilitat i ancoratge**: 1-2 exemples elaborats amb connexió explícita amb la definició.
- **Profunditat i coherència**: Explicació amb múltiples característiques. Comparació amb termes propers.
- **Llargada**: Definició + explicació (4-5 frases) + 1-2 exemples.
- **Sense remissions**: Idem.
- **Sense etimologia inicial**: Idem.
- **Fidelitat al text font**: Fidelitat a la complexitat conceptual i al context disciplinar.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Precisió i estructura**: Definició nuclear rigorosa amb matisos terminològics i referència al debat si és rellevant.
- **Coherència lògica**: Idem. Si hi ha debat terminològic, es recull a l'Explicació ampliada (Pas 5). La definició nuclear segueix sent binary: no usa el terme ni arrels.
- **Estructura lògica**: Categoria amb precisió i referència a la taxonomia disciplinar si escau.
- **Accessibilitat i ancoratge**: Exemples variats. Pot incloure un exemple límit o de frontera que posi a prova la definició.
- **Profunditat i coherència**: Explicació completa amb matisos, variants i possibles debats sobre la delimitació del terme.
- **Llargada**: Text complet amb tots els matisos necessaris.
- **Sense remissions**: Idem. La referència a termes relacionats, si escau, s'integra al cos de l'explicació sense remissió formal.
- **Sense etimologia inicial**: L'etimologia pot aparèixer si aporta matisos al significat, però mai com a única definició.
- **Fidelitat al text font**: Fidelitat a la complexitat, als matisos i als debats si els hi ha.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


