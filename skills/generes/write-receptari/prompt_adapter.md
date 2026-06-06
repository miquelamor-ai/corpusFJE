---
tipus: derivat
font_canonic: M3_genere-escriure-receptari.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-06'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 1d9ba51d307f5c5d
---

# Escriure/adaptar una recepta — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una recepta per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Completitud i format**: Llista de 3-5 ingredients. Sense quantitats. 1 ingredient per línia.
- **Seqüència d'ús**: Ingredients en qualsevol ordre (llista simple).
- **Claredat i precisió**: Passos numerats. 1 verb + 1 objecte. ≤6 paraules per pas.
- **Observació i verificació**: 1 indicador per pas crític: "fins que sigui daurat".
- **Precisió temporal**: Temps global aproximat: "uns 20 minuts".
- **Verificabilitat final**: 1 frase: com ha de quedar (color o textura principals).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Completitud i format**: Llista de 4-6 ingredients amb quantitats bàsiques ("1 tassa", "2 ous").
- **Seqüència d'ús**: Ingredients ordenats aproximadament per l'ordre en qué s'usen.
- **Claredat i precisió**: Passos numerats. 1 acció culinària + context breu. ≤10 paraules per pas.
- **Observació i verificació**: 1-2 indicadors sensorials per pas crític (color, textura, olor).
- **Precisió temporal**: Temps per a les fases principals: "fregir 5 minuts / coure 20 minuts".
- **Verificabilitat final**: 1-2 frases que descriuen el resultat en termes sensorials concrets.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Completitud i format**: Ingredients amb quantitats i unitats de mesura estàndard. Llista completa.
- **Seqüència d'ús**: Ingredients ordenats estrictament per l'ordre d'ús. Separació per fases si cal.
- **Claredat i precisió**: Passos numerats amb indicador sensorial o temporal si cal. 1-2 accions relacionades.
- **Observació i verificació**: Indicadors sensorials als passos clau. Permeten saber si el pas s'ha executat correctament.
- **Precisió temporal**: Temps específic per a cada pas que en requereix. Indicador sensorial alternatiu.
- **Verificabilitat final**: Resultat descrit amb 2-3 indicadors sensorials. Com saber que ha sortit bé.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Completitud i format**: Ingredients completament especificats (graus, temps de repòs si cal).
- **Seqüència d'ús**: Agrupació per fases de preparació si la recepta és complexa.
- **Claredat i precisió**: Passos numerats complets i autònoms. Pot incloure condicions simples ("si bull, baixa el foc").
- **Observació i verificació**: Indicadors sensorials precisos i variats (color, so, tacte, olor). Sempre preferits al temps.
- **Precisió temporal**: Temps amb marge ("10-12 minuts") i indicador sensorial com a confirmació.
- **Verificabilitat final**: Resultat complet: aspecte, textura, olor i gust. Criteris de qualitat. Racions o quantitat final.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Completitud i format**: Ingredients amb quantitats precises, variants i possibles substitucions explicitades.
- **Seqüència d'ús**: Organització professional per fases i subfases si cal. Cada fase amb subtítol.
- **Claredat i precisió**: Passos tècnicament precisos. Temperatures, temps i textures especificats sempre.
- **Observació i verificació**: Indicadors sensorials complets que permeten reproduir la recepta sense ajuda externa.
- **Precisió temporal**: Temps i temperatures precisos. Alternatives per a equipaments o altituds diferents.
- **Verificabilitat final**: Resultat professional: criteris precisos + variacions acceptables + errors comuns amb solució.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


