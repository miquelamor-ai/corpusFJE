---
tipus: derivat
font_canonic: M3_genere-escriure-reglament.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-05-26'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 33c5c5fde43c6d7b
---

# Escriure/adaptar un reglament — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un reglament per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Organització i coherència**: 2 grups temàtics. Títol de grup molt curt (1-2 paraules: "A classe", "Al passadís"). 2-3 normes per grup.
- **Claredat i precisió**: Verb imperatiu + objecte. ≤6 paraules per norma. 1 conducta per norma.
- **Registre normatiu**: Imperatiu de 2a singular consistent: "Respecta", "Escolta", "Guarda". Cap passiva ni impersonal.
- **Granularitat i claredat**: Estrictament 1 conducta per ítem. Cap conjunció coordinada dins d'una norma ("i", "ni").
- **Orientació pedagògica**: La norma formula el que s'ha de fer ("Demana la paraula"), no el que no s'ha de fer.
- **Estructura i claredat**: Si hi ha conseqüències, estan en un bloc final separat de les normes. 1 frase per conseqüència.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Organització i coherència**: 2-3 grups temàtics amb títol curt. 3-4 normes per grup.
- **Claredat i precisió**: Verb imperatiu + objecte + context breu. ≤10 paraules per norma.
- **Registre normatiu**: Idem. Imperatiu de 2a singular o de 2a plural ("Respecteu") si el context és col·lectiu.
- **Granularitat i claredat**: Idem. Cap norma composta. Si es detecten dues conductes, es divideix en dos ítems.
- **Orientació pedagògica**: Idem. Si cal una norma negativa, va darrere de la positiva equivalent.
- **Estructura i claredat**: Bloc de conseqüències separat. Cada conseqüència lligada a un grup temàtic o a una norma concreta.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Organització i coherència**: 3-4 grups temàtics. Títols de grup que expliciten l'àmbit ("A l'espai comú", "Amb els materials").
- **Claredat i precisió**: Norma completa i autònoma. Pot incloure el context si determina l'aplicació ("Als passadissos, camina").
- **Registre normatiu**: Idem. Pot alternar imperatiu singular/plural segons el destinatari de cada grup temàtic.
- **Granularitat i claredat**: Idem. Cada ítem és atòmic: no pot descompondre's en subnormes sense perdre sentit.
- **Orientació pedagògica**: Idem. Revisió sistemàtica: cada "No X" té una formulació positiva equivalent.
- **Estructura i claredat**: Bloc de conseqüències amb estructura "Si [norma incomplerta] → [conseqüència]". Conseqüència educativa.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Organització i coherència**: 4-6 grups temàtics. Progressió lògica dels àmbits (de l'individual al col·lectiu o d'intern a extern).
- **Claredat i precisió**: Norma completa amb subjecte implícit clar. Pot incloure condicions d'aplicació simples.
- **Registre normatiu**: Idem. Pot usar l'infinitiu normatiu com a variant registral ("Respectar els torns de paraula").
- **Granularitat i claredat**: Idem. La granularitat és coherent dins de cada grup temàtic.
- **Orientació pedagògica**: Idem. El reglament reflecteix una orientació positiva global. Les normes negatives son excepcions justificades.
- **Estructura i claredat**: Bloc de conseqüències graduat (amonestació / mediació / sanció). Lligat explícitament a les normes.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Organització i coherència**: Estructura temàtica completa i coherent. Progressió que reflecteix la jerarquia de valors del reglament.
- **Claredat i precisió**: Norma tècnicament precisa. Pot incloure l'abast ("tothom", "en tot moment") quan és rellevant.
- **Registre normatiu**: Idem. Imperatiu o infinitiu normatiu, consistents dins de cada grup temàtic. Registre institucional precís.
- **Granularitat i claredat**: Idem. La granularitat és consistent a tot el reglament. Cap norma és redundant amb una altra.
- **Orientació pedagògica**: Idem. El reglament equilibra normes de conducta esperada i normes de conducta prohibida. La ràtio positiu/negatiu reflecteix els valors del context.
- **Estructura i claredat**: Bloc de conseqüències complet i proporcional. Pot incloure el procediment de resolució de conflictes.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


