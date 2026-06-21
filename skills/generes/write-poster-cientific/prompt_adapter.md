---
tipus: derivat
font_canonic: M3_genere-escriure-poster-cientific.md
font_version: 4.2.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-21'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 9b85b94da72f8873
---

# Escriure/adaptar un pòster científic — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un pòster científic per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Orientació**: Títol-etiqueta (1-3 paraules) + imatge. La pregunta la formula oralment l'adult.
- **Síntesi del procediment**: Imatge dels materials amb etiquetes mínimes. Sense text de mètode.
- **Lligadura dada–visual**: Dada nuclear amb la seva imatge/icona. La dada (valor + unitat) es manté intacta; el text és l'etiqueta.
- **Inviolabilitat de l'objecte**: Dades, unitats, símbols i termes tècnics INTACTES. El text mínim els envolta sense deformar-los.
- **Superfície del text**: Etiquetes i paraules clau. Mediació oral de l'adult. Frase 0 o 1 idea per bloc.
- **Tancament argumentatiu**: Conclusió ancorada a la dada i la imatge amb el vincle causal preservat ("Flota per la densitat [valor]"), mediada oralment. Per a alumnes amb CALP en L1, admet conclusions més riques via oralitat/L1: el límit és la superfície lingüística, no l'operació cognitiva.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Orientació**: Títol curt + pregunta de 3-5 paraules ("Què flota?").
- **Síntesi del procediment**: Llista visual de materials (paraula + icona). Mètode en 1 frase molt simple.
- **Lligadura dada–visual**: 2-3 dades amb representació visual simple (barres, símbols). Valor + unitat sempre.
- **Inviolabilitat de l'objecte**: Idem. Els termes tècnics poden portar un pictograma de suport.
- **Superfície del text**: Frases de 3-5 paraules. Vocabulari nuclear. 1 idea per bloc.
- **Tancament argumentatiu**: Conclusió simple amb vincle causal lligat a la dada ("El més pesat va al fons perquè la densitat és més alta"). Per a alumnes amb CALP en L1, admet conclusions més riques via oralitat/L1.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Orientació**: Títol + pregunta o objectiu en 1 frase clara.
- **Síntesi del procediment**: Materials en llista. Mètode en 1-2 frases simples.
- **Lligadura dada–visual**: Dades en taula o gràfic simple etiquetat. Frase que diu què mostra.
- **Inviolabilitat de l'objecte**: Idem. Els termes tècnics poden portar definició integrada molt breu.
- **Superfície del text**: Frases simples (8-12 paraules). Connectors bàsics ("perquè", "i").
- **Tancament argumentatiu**: 1-2 conclusions derivades de les dades. Connector "per tant".

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Orientació**: Títol informatiu + pregunta d'indagació explícita.
- **Síntesi del procediment**: Materials + mètode en 2-3 frases. Què s'ha fet i com.
- **Lligadura dada–visual**: Dades en gràfic/taula. Frase que descriu la tendència ("el valor puja quan...").
- **Inviolabilitat de l'objecte**: Idem. Definicions integrades on calgui.
- **Superfície del text**: Frases amb connectors causals ("per tant", "ja que"). Veu impersonal emergent.
- **Tancament argumentatiu**: 2 conclusions justificades explícitament des de la dada (HCL Justificar: "X perquè la dada mostra Y") + 1 implicació.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Orientació**: Títol precís + objectiu o hipòtesi formulada.
- **Síntesi del procediment**: Mètode concís amb variables identificades.
- **Lligadura dada–visual**: Dades en gràfic adequat al tipus. Descripció objectiva de la relació.
- **Inviolabilitat de l'objecte**: Idem. Terminologia disciplinària plena.
- **Superfície del text**: Veu impersonal consistent. Vocabulari acadèmic.
- **Tancament argumentatiu**: Conclusió argumentada + implicació o aplicació del resultat.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Orientació**: Títol acadèmic + pregunta de recerca i marc del problema.
- **Síntesi del procediment**: Mètode amb control de variables i justificació breu del disseny.
- **Lligadura dada–visual**: Dades en format rigorós. Anàlisi de la relació i de la seva fiabilitat.
- **Inviolabilitat de l'objecte**: Idem. Rigor terminològic i simbòlic complet, sense glosses.
- **Superfície del text**: Registre acadèmic ple. Precisió i economia del llenguatge de pòster.
- **Tancament argumentatiu**: Conclusió amb discussió de límits de les dades i obertura a noves preguntes.

