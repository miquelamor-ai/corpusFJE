---
tipus: derivat
font_canonic: M3_genere-escriure-manual.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-01'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 186ab4d2592520d2
---

# Escriure/adaptar un manual — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un manual per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Context i anunci**: 1 frase que diu qué s'explicarà. Directa i concreta.
- **Estructura i coherència**: 3 apartats. Ordre estricte: el més simple primer. Un concepte per apartat.
- **Accessibilitat i precisió**: 1 terme per apartat, definit al costat en parèntesi: "el fotó (una partícula de llum)".
- **Ordre i ancoratge ZDP**: Exemple molt quotidià ABANS del principi abstracte. "La sal es dissol a l'agua → l'osmosi és...".
- **Explicitació de relacions**: "Perquè", "per això". 1 per apartat. Simple i clar.
- **Desnominalitzar processos**: Convertir noms abstractes en processos verbals: "oxidació" → "quan s'oxida". A1: sempre.
- **No referència futura**: Cap "ho veurem més endavant" ni referència a apartats posteriors. El text és autocontingut.
- **Fidelitat al text font**: Fidelitat als conceptes principals i a la progressió bàsica.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Context i anunci**: 2 frases: qué s'explicarà i per qué és útil.
- **Estructura i coherència**: 3 apartats progressius. Cada un es recolza en l'anterior de manera explícita.
- **Accessibilitat i precisió**: 1 terme per apartat en negreta amb definició integrada a la frase.
- **Ordre i ancoratge ZDP**: Exemple concret per apartat. L'abstracció ve SEMPRE DESPRÉS de l'exemple.
- **Explicitació de relacions**: "Perquè", "per tant", "d'aquesta manera". Variats mínimament.
- **Desnominalitzar processos**: Idem. "la fotosíntesi" → "quan les plantes fabriquen aliment".
- **No referència futura**: Idem. Cap referència lateral o nota al peu que interrompi el flux.
- **Fidelitat al text font**: Fidelitat als conceptes, a la progressió i a les definicions essencials.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Context i anunci**: Entradeta que anuncia els apartats i la seva progressió lògica.
- **Estructura i coherència**: 3-5 apartats. Progressió lògica explicitada a l'entradeta o als subtítols.
- **Accessibilitat i precisió**: Termes tècnics en negreta definits a la primera aparició. Cap terme tècnic sense definir.
- **Ordre i ancoratge ZDP**: Exemple que connecta el concepte nou amb el que l'alumne ja sap (ZDP). L'ordre és sagrat.
- **Explicitació de relacions**: "Com a resultat", "per tant", "d'aquí se'n deriva". Variats. Distinció causa/efecte explícita.
- **Desnominalitzar processos**: Idem. La desnominalització és la estratègia principal per fer accessible el CALP.
- **No referència futura**: Idem. Cap nota al peu a A1-B1.
- **Fidelitat al text font**: Fidelitat als conceptes, a la progressió, a les definicions i als connectors causals del text font.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Context i anunci**: Entradeta que contextualitza el manual i el seu objectiu dins del camp.
- **Estructura i coherència**: 4-6 apartats. Progressió amb relació explícita entre ells. Pot tenir subapartats d'un nivell.
- **Accessibilitat i precisió**: Terminologia específica de la matèria, sempre definida a la primera aparició. Pot tenir glossari final.
- **Ordre i ancoratge ZDP**: Exemple elaborat + abstracció + connexió entre apartats.
- **Explicitació de relacions**: Connectors causals precisos i variats. Distinció causa/conseqüència/condició.
- **Desnominalitzar processos**: Idem. Pot mantenir el nom abstracte si va precedit de la desnominalització.
- **No referència futura**: Idem. Notes al peu admeses si no interrompen el flux principal.
- **Fidelitat al text font**: Fidelitat a la complexitat conceptual i al context disciplinar del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Context i anunci**: Entradeta professional que permet saber si el manual és el que es necessita abans de llegir-lo.
- **Estructura i coherència**: Estructura completa amb progressió rigorosa. Subapartats d'un o dos nivells si cal.
- **Accessibilitat i precisió**: Vocabulari tècnic ric i definit. Glossari final si hi ha molts termes. Pot incloure debat terminològic.
- **Ordre i ancoratge ZDP**: Exemple + abstracció + extensió conceptual. Pot incloure exemples límit o de frontera.
- **Explicitació de relacions**: Connectors sofisticats. Pot incloure concessius ("tot i que") i adversatius ("malgrat").
- **Desnominalitzar processos**: Idem. El nom abstracte és admissible quan el context disciplinar ho requereix i el procés ja s'ha explicat.
- **No referència futura**: Idem. Notes al peu admeses per a matisos tècnics avançats.
- **Fidelitat al text font**: Fidelitat a la complexitat, als matisos i als debats terminològics si n'hi ha.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


