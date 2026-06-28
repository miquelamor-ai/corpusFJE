---
tipus: derivat
font_canonic: M3_genere-escriure-cv.md
font_version: 1.0.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: f2613f61f48cd95a
---

# Escriure/adaptar un currículum vitae (CV) — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un currículum vitae (cv) per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Identificació**: Nom + correu + telèfon. Sense foto, sense DNI. Format llista simple.
- **Síntesi del valor del candidat**: No s'inclou (massa abstracte per a A2).
- **Trajectòria acadèmica**: Llistat simple: títol + any + centre. Ordre cronològic invers. Frases nominals mínimes (3-6 paraules).
- **Trajectòria laboral**: 1-2 entrades màxim. Càrrec + empresa + dates. 1 frase nominal de funció per entrada ("Atenció al client", "Preparació de comandes").
- **Plurilingüisme del candidat**: Llista: llengua + nivell (paraula simple: "bàsic", "bo", "natiu"). La L1 del candidat s'inclou amb "llengua materna" o "nivell nadiu".
- **Habilitats transversals**: Llista simple: nom de la competència o eina ("Word", "Instagram", "Caixa registradora"). Sense nivells.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Identificació**: Ídem. Pot afegir-se perfil LinkedIn si n'hi ha.
- **Síntesi del valor del candidat**: Opcional: 1-2 frases nominals molt simples sobre l'objectiu professional.
- **Trajectòria acadèmica**: Llistat estructurat. Pot afegir-se una línia breu de descripció per entrada rellevant.
- **Trajectòria laboral**: Totes les entrades rellevants. 2-3 frases nominals de funcions per entrada. Connector d'enumeració ("Tasques principals: ...").
- **Plurilingüisme del candidat**: Llista amb nivell MECR si es coneix ("Català B2", "Castellà C1"). L1 amb "parlant natiu de...".
- **Habilitats transversals**: Llista amb nivell simple ("coneixements de...", "experiència en...").

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Identificació**: Ídem. Selecció conscient de les dades rellevants per al context (p.ex. omissió de dades no pertinents).
- **Síntesi del valor del candidat**: 2-3 frases nominals que sintetitzen el perfil i l'objectiu de manera específica per a l'oferta.
- **Trajectòria acadèmica**: Selecció de la formació rellevant per a l'oferta. Cursos i certificacions identificats com a valor afegit.
- **Trajectòria laboral**: Entrades seleccionades per rellevància. Funcions amb verbs d'acció en forma nominal ("Gestió de...", "Coordinació de..."). Resultats si n'hi ha.
- **Plurilingüisme del candidat**: Taula o llista estructurada amb nivell MECR i, si n'hi ha, certificació acreditada.
- **Habilitats transversals**: Competències digitals categoritzades (ofimàtica, eines de sector, xarxes). Competències transversals seleccionades per rellevància.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Identificació**: Ídem. Format net i professional, adaptat a l'estàndard del sector.
- **Síntesi del valor del candidat**: 3-5 frases nominals que argumenten el valor del candidat, amb paraules clau del sector i quantificació si és possible.
- **Trajectòria acadèmica**: Formació presentada amb relació explícita a les competències i al perfil professional. Distinció formació reglada / complementària.
- **Trajectòria laboral**: Entrades amb funcions detallades, resultats quantificats si és possible ("Increment de les vendes en un 15%", "Atenció a 50+ clients diaris"). Relació explícita amb les competències del perfil.
- **Plurilingüisme del candidat**: Format complet: llengua, nivell MECR, certificació, context d'ús professional si és rellevant.
- **Habilitats transversals**: Competències digitals amb nivell i evidència si és possible. Competències transversals argumentades amb exemples breus.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


