---
tipus: derivat
font_canonic: M3_genere-escriure-practica-laboratori.md
font_version: 1.0.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-25'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: ab740d351200be86
---

# Escriure/adaptar una pràctica de laboratori — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una pràctica de laboratori per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Orientació i predicció**: Títol-etiqueta (1-3 paraules). La hipòtesi la formula oralment l'adult; l'alumne la valida amb un gest o una imatge ("Sí/No").
- **Identificació dels elements**: Imatge o dibuix del muntatge amb etiquetes mínimes. L'adult llegeix la llista de materials.
- **Passos de la investigació**: Adult guia oralment. L'alumne segueix el muntatge visual. Cap text de procediment.
- **Registre de les observacions**: Taula de dades simple preomplerta amb 1-2 valors nuclears (valor + unitat intactes). L'adult llegeix la taula. Imatge del resultat visible.
- **Inviolabilitat de l'objecte**: Dades, unitats, símbols, termes tècnics i hipòtesi original INTACTES. El text mínim els envolta.
- **HCL Justificar (el cor del gènere)**: Vincle causal mínim mediat oralment per l'adult: "[El resultat] passa perquè [terme tècnic]." L'adult verbalitza la connexió dada–teoria; l'alumne confirma. Per a alumnes amb CALP en L1, la connexió pot ser més rica via oralitat/L1.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Orientació i predicció**: Títol curt (3-5 paraules). Hipòtesi en 1 frase molt simple: "Crec que [el/la X] [fa/és]..." amb vocabulari nuclear.
- **Identificació dels elements**: Llista de materials (nom + icona si cal). Dibuix del muntatge etiquetat amb els noms dels elements.
- **Passos de la investigació**: 2-3 passos en frases molt simples ("Primer... Després... Final..."). Imatge de cada pas clau.
- **Registre de les observacions**: Taula de dades amb valors mesurats (valor + unitat sempre). 1 frase que diu "He obtingut [X unitat]."
- **Inviolabilitat de l'objecte**: Idem. Els termes tècnics poden portar un pictograma de suport. La hipòtesi oral de l'adult es manté sense corregir.
- **HCL Justificar (el cor del gènere)**: 1 frase de justificació simple ancorada a la dada: "[X] ha passat perquè [raó nuclear]." Connector causal "perquè" obligatori.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Orientació i predicció**: Títol + hipòtesi en 1 frase clara: "Crec que si [condició], llavors [resultat], perquè [raó breu]."
- **Identificació dels elements**: Llista de materials. Esquema del muntatge etiquetat. 1-2 frases del procediment principal.
- **Passos de la investigació**: 3-5 passos numerats en frases simples (8-12 paraules). Connectors bàsics de seqüència ("primer", "a continuació", "finalment").
- **Registre de les observacions**: Taula de dades completa. Gràfic simple si escau. 1-2 frases que descriuen el resultat principal ("La temperatura ha pujat fins a [X °C].").
- **Inviolabilitat de l'objecte**: Idem. Els termes tècnics poden portar definició integrada molt breu. La hipòtesi escrita no es modifica.
- **HCL Justificar (el cor del gènere)**: 1-2 frases de justificació amb connector causal. Connexió directa resultat → explicació: "Els resultats mostren [X] perquè [principi científic simple]."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Orientació i predicció**: Títol informatiu + hipòtesi amb relació entre variables: "Si augmento [variable independent], espero que [variable dependent] augmenti perquè [marc teòric breu]."
- **Identificació dels elements**: Materials llistats + esquema del muntatge. Procediment en 3-5 passos numerats. Identificació de la variable que es canvia.
- **Passos de la investigació**: 5-7 passos numerats. Connectors de seqüència i frases amb veu activa. Inclusió de les condicions de control.
- **Registre de les observacions**: Taula + gràfic adequat al tipus de dada. 2-3 frases que descriuen la tendència ("A mesura que [X] augmenta, [Y] disminueix.").
- **Inviolabilitat de l'objecte**: Idem. Definicions integrades on calgui. La hipòtesi és la referència explícita de la conclusió.
- **HCL Justificar (el cor del gènere)**: 2-3 frases de justificació amb connexió explícita dada–teoria: "El valor de [X unitat] confirma que [principi científic], ja que [dada suport]." Veu impersonal emergent.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Orientació i predicció**: Títol precís + hipòtesi formulada amb variables nomenades explícitament i fonamentació teòrica breu.
- **Identificació dels elements**: Materials + esquema. Procediment en passos numerats. Variables independent, dependent i controlades identificades.
- **Passos de la investigació**: Passos numerats amb justificació breu de les condicions experimentals. Veu impersonal emergent.
- **Registre de les observacions**: Taula + gràfic. Descripció objectiva de la relació entre variables. Indicació de la unitat de mesura de cada valor.
- **Inviolabilitat de l'objecte**: Idem. Terminologia disciplinària plena. La hipòtesi s'esmenta explícitament a la conclusió ("La nostra hipòtesi ha estat [confirmada/refutada] perquè...").
- **HCL Justificar (el cor del gènere)**: Paràgraf d'anàlisi: justificació de cada resultat clau connectant amb la teoria de referència. Discussió si els resultats s'aparten de l'esperable. Connectors acadèmics ("per tant", "en conseqüència", "tot i que").

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Orientació i predicció**: Títol acadèmic + hipòtesi rigorosa amb relació de causalitat explícita, variables i marc teòric de referència citat.
- **Identificació dels elements**: Materials + esquema. Procediment detallat. Variables identificades i justificació breu del disseny experimental.
- **Passos de la investigació**: Procediment detallat en veu impersonal. Justificació del control de variables. Pot incloure referències a protocols estàndard.
- **Registre de les observacions**: Taula + gràfic rigorosos. Descripció analítica de la relació, identificació de valors atípics i valoració de la repetibilitat.
- **Inviolabilitat de l'objecte**: Idem. Rigor terminològic i simbòlic complet. La hipòtesi és el fil conductor de tot el document.
- **HCL Justificar (el cor del gènere)**: Anàlisi rigorosa: connexió explícita dada–teoria amb citació de referència. Discussió de les fonts d'error experimental (error instrumental, error humà, condicions no controlades). Contrastació del resultat obtingut amb el valor teòric o experimental esperat.

