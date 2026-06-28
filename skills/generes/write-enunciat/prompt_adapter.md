---
tipus: derivat
font_canonic: M3_genere-escriure-enunciat.md
font_version: 1.3.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 0a8478074ae52891
---

# Adaptar un enunciat escolar — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere adaptar un enunciat escolar per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Orientació**: Títol-etiqueta (1-3 paraules) + icona de l'acció. La consigna la llegeix oralment l'adult.
- **Bastida del marc**: Absent o 1 oració mínima (SVO, present). Mediació oral de l'adult. Visual obligatori si hi ha dades.
- **Invariant de contingut**: Dades invariants. Imatge o esquema visual obligatori per a cada dada. Etiquetes mínimes.
- **Nucli de la tasca (INVARIANT de contingut)**: 1 consigna: verb d'1 sílaba + objecte mínim ("Dibuixa X", "Encercla X"). Icona del verb. Mediació oral obligatòria.
- **Superfície del text**: Etiquetes i paraules clau isolades. 0-1 frases per bloc. Mediació oral de l'adult.
- **Andamiatge del format**: "Respon aquí: ___" amb espai grafiat o gràfic. L'adult inicia la resposta oralment.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Orientació**: Títol curt (3-5 paraules) + icona o imatge de referència.
- **Bastida del marc**: 1-2 frases molt simples (SVO, vocabulari nuclear). Context ancorat en imatge o esquema.
- **Invariant de contingut**: Dades invariants. Representació visual de suport. Vocabulari de les etiquetes al mínim necessari.
- **Nucli de la tasca (INVARIANT de contingut)**: 1 consigna: verb + objecte clar (3-5 paraules). Icona del verb obligatòria. 0-1 subconsigna.
- **Superfície del text**: Frases de 3-5 paraules. Vocabulari nuclear. 1 idea per frase. Senyaladors visuals màxims.
- **Andamiatge del format**: "Escriu aquí:" + espai. Opció de dibuix o marca si la consigna ho permet.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Orientació**: Títol clar + breu descripció de la tasca en 1 frase.
- **Bastida del marc**: 2-3 frases simples. Connectors bàsics ("i", "però", "perquè"). Context comprensible de manera autònoma.
- **Invariant de contingut**: Dades invariants. Taula o gràfic si existia al original. Petita llegenda si cal.
- **Nucli de la tasca (INVARIANT de contingut)**: 1-2 consignes curtes. Verb de la consigna en **negreta**. Numeració explícita si n'hi ha més d'una.
- **Superfície del text**: Frases simples (8-12 paraules). Connectors bàsics. Sagnat i separació entre context i consigna.
- **Andamiatge del format**: "Escriu 1-2 frases." o "Marca amb X." Format de resposta explícit.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Orientació**: Títol informatiu + indicació de la HCL ("Expliqueu per què...").
- **Bastida del marc**: 1-2 frases amb connector causal o temporal. Context que dona el marc suficient per a la consigna.
- **Invariant de contingut**: Dades invariants. Taula o gràfic etiquetat amb frase explicativa breu.
- **Nucli de la tasca (INVARIANT de contingut)**: Consigna completa amb connector causal o condicional ("A partir de X, explica per què Y"). Subconsignes numerades.
- **Superfície del text**: Frases amb connectors causals i condicionals. Separació visual clara entre parts. Registre funcional-acadèmic emergent.
- **Andamiatge del format**: "Respon en 2-3 frases. Usa 'per tant' o 'perquè'." Connector guia explícit.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Orientació**: Títol precís que anticipa l'operació i el context.
- **Bastida del marc**: Paràgraf concís (3-5 frases) amb vocabulari acadèmic. Context que emmarca el problema amb precisió.
- **Invariant de contingut**: Dades invariants. Tots els elements del text font presents. Descripció objectiva si hi ha gràfics.
- **Nucli de la tasca (INVARIANT de contingut)**: Múltiples subconsignes jerarquitzades. Format visual que marca la jerarquia (numeració i sagnat).
- **Superfície del text**: Veu impersonal consistent. Vocabulari acadèmic. Estructura visual clara però sense senyaladors excessius.
- **Andamiatge del format**: Format de resposta implícit en la consigna. Estructura esperada derivada de la HCL.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Orientació**: Títol acadèmic amb formulació que inclou el repte i el marc disciplinari.
- **Bastida del marc**: Context ric amb vocabulari disciplinari, connexions conceptuals i marc del problema ben delimitat.
- **Invariant de contingut**: Dades invariants. Text font complet. Anàlisi de la relació entre les dades si la consigna ho demana.
- **Nucli de la tasca (INVARIANT de contingut)**: Consigna acadèmica amb múltiples operacions cognitives encadenades. Formulació precisa i densa.
- **Superfície del text**: Registre acadèmic ple. Precisió i densitat del llenguatge acadèmic. Sense bastides visuals addicionals.
- **Andamiatge del format**: Cap indicador de format. L'alumne domina el format de resposta acadèmica.

