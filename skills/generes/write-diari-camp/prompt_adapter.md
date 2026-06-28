---
tipus: derivat
font_canonic: M3_genere-escriure-diari-camp.md
font_version: 1.1.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 1506ac44089babf3
---

# Escriure/adaptar un diari de camp — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un diari de camp per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Contextualització**: Pictograma de data (número del dia) + nom del lloc en 1 paraula + icona del temps meteorològic. L'adult completa la capçalera i la llegeix en veu alta.
- **Orientació**: L'adult formula l'objectiu oralment. L'alumne pot assenyalar o dibuixar "què busquem".
- **Registre fidel**: Croquis de l'element observat + etiqueta d'1 paraula (nombre o nom). Mediació oral de l'adult ("Quants en veus?"). La dada (número, mesura) es manté intacta.
- **Inviolabilitat de l'observació**: Allò vist és allò vist. L'adult no omple el que l'alumne no ha observat. Croquis = document de camp.
- **Superfície del text**: Etiquetes i números. Mediació oral de l'adult. 0 o 1 paraula per element observat.
- **Salt inferencial explicit**: No s'escriu. L'adult formula oralment la pregunta "Per què creus que...?" L'alumne respon oralment.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Contextualització**: Data (dia/mes) + lloc en 1-2 paraules + 1 condició ambiental breu ("Sol", "Pluja").
- **Orientació**: 1 frase molt simple ("Busquem ocells"). L'adult pot dictar.
- **Registre fidel**: Croquis + etiqueta (nom + número). "He vist [N] [element]." 1 observació per bloc.
- **Inviolabilitat de l'observació**: El nombre i el nom de l'element observat es mantenen exactes. L'adult no "corregeix" allò no observat.
- **Superfície del text**: Frases de 3-5 paraules. Verbs d'observació bàsics ("veig", "hi ha", "compto"). 1 idea per línia.
- **Salt inferencial explicit**: Oral o dibuix breu. L'adult escriu la idea de l'alumne amb l'etiqueta `[Idea:]`.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Contextualització**: Data completa + lloc + hora + 1-2 condicions ambientals en frase breu ("Fa sol i 20 °C").
- **Orientació**: Objectiu en 1 frase clara ("Observem quines plantes creixen vora l'estany").
- **Registre fidel**: 2-3 observacions amb nom, número o mesura. Frases simples. Ús de "He vist", "He comptat", "He mesurat".
- **Inviolabilitat de l'observació**: Idem. Les observacions s'escriuen tal com s'han produït, no com "haurien" de ser.
- **Superfície del text**: Frases simples (8-12 paraules). Connectors temporals ("primer", "després"). Verbs de registre ("he observat", "he mesurat").
- **Salt inferencial explicit**: 1 frase d'interpretació, clarament separada i marcada `[Crec que:]`. Connector "potser".

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Contextualització**: Capçalera completa: data, lloc, hora, condicions meteorològiques/ambientals, observador. Frase per element.
- **Orientació**: Objectiu d'observació explícit, pot incloure hipòtesi inicial.
- **Registre fidel**: Observació seqüenciada: hora/ordre + allò observat + dada. Inici de veu impersonal ("S'observa").
- **Inviolabilitat de l'observació**: Idem. Distinció explícita entre "he vist" (observació) i "crec que" (interpretació).
- **Superfície del text**: Frases amb connectors temporals i causals. Veu impersonal emergent ("s'observa", "es registra").
- **Salt inferencial explicit**: Interpretació explícita i etiquetada (`[Interpretació:]`): "Potser X perquè he observat Y." Vincula observació i hipòtesi.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Contextualització**: Capçalera completa amb precisió: coordenades del lloc si aplica, metodologia d'observació declarada en 1 frase.
- **Orientació**: Objectiu formulat com a pregunta d'investigació + hipòtesi prèvia.
- **Registre fidel**: Registre sistemàtic amb variables declarades (hora, localització dins el transsecte, condicions locals). Veu impersonal consistent.
- **Inviolabilitat de l'observació**: Idem. Metodologia d'observació declarada i seguida; qualsevol desviació es registra.
- **Superfície del text**: Veu impersonal consistent. Vocabulari tècnic d'observació (CALP). Precisió en la descripció.
- **Salt inferencial explicit**: Bloc `[Interpretació:]` amb argumentació: observació → hipòtesi → vinculació amb model de referència.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Contextualització**: Capçalera de protocol científic: data, localització precisa, condicions ambientals amb mesures, observadors, protocol de mostratge.
- **Orientació**: Objectiu amb marc teòric de referència: la pregunta d'investigació es situa en relació a models o estudis previs.
- **Registre fidel**: Registre de protocol: variables múltiples, mètode de mostratge explícit, referència al protocol declarat a la capçalera.
- **Inviolabilitat de l'observació**: Idem. Rigor metodològic complet: l'observació és traçable, reproductible en condicions similars, i els límits de l'observació es reconeixen.
- **Superfície del text**: Registre acadèmic de camp ple. Terminologia disciplinària específica. Precisió i economia del llenguatge científic.
- **Salt inferencial explicit**: Discussió crítica de la interpretació: observació → hipòtesi → model de referència → límits de la inferència. Reconeixement del salt lògic.

