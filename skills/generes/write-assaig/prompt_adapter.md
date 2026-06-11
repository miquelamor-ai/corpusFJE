---
tipus: derivat
font_canonic: M3_genere-escriure-assaig.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-11'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: c73ffa809ede24af
---

# Escriure/adaptar un assaig — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un assaig per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Claredat i explicitació**: 1 frase que diu el que es defensa: "Crec que [tesi]." Al primer paràgraf.
- **Coherència i progressió**: 1 argument simple. "Crec que... perquè...".
- **Suport i credibilitat**: 1 exemple personal o molt proper per argument.
- **Pensament crític**: Sense refutació a A1 (massa complex). Acceptable que la postura sigui unilateral.
- **Tancament i coherència**: 1 frase: "Per tot això, crec que [tesi]." No introdueix arguments nous.
- **Varietat i precisió**: "Crec que... perquè..." (1 connector causal).
- **Reflexió sobre el procés**: "He escrit la meva opinió en una frase al principi. He donat 1 argument amb un exemple."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Claredat i explicitació**: Tesi clara de 1-2 frases amb connector d'opinió. Al primer paràgraf.
- **Coherència i progressió**: 2 arguments en paràgrafs separats. 1 connector causal per argument.
- **Suport i credibilitat**: 1 exemple concret per argument. Pot ser un fet quotidià o una observació directa.
- **Pensament crític**: Reconeixement d'un punt de vista diferent en 1 frase: "Alguns pensen que... però jo crec que..."
- **Tancament i coherència**: Conclusió de 2 frases que reprèn la tesi. No obre noves preguntes.
- **Varietat i precisió**: "A més", "però", "per exemple", "per tot això". Variats mínimament.
- **Reflexió sobre el procés**: "He escrit la tesi al principi. He donat 2 arguments amb un exemple cadascun."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Claredat i explicitació**: Tesi explícita que anuncia el tema i la postura. La tesi delimita l'abast de l'assaig.
- **Coherència i progressió**: 3 arguments ben diferenciats. 1 per paràgraf. Connector explícit per a cada un.
- **Suport i credibilitat**: 1 exemple o evidència per argument. Pot ser un fet, una dada o una cita breu.
- **Pensament crític**: Refutació d'un argument contrari. Connector de contrast: "tot i que", "però", "tanmateix".
- **Tancament i coherència**: Conclusió de 3 frases: resum de la postura + una implicació breu (opcional).
- **Varietat i precisió**: "Tanmateix", "per contra", "en conseqüència", "d'una banda... de l'altra".
- **Reflexió sobre el procés**: "He escrit 3 arguments, 1 per paràgraf. He reconegut un punt de vista diferent."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Claredat i explicitació**: Tesi matisada que reconeix la complexitat del tema sense diluir la postura.
- **Coherència i progressió**: 3-4 arguments jerarquitzats (del menys al més fort o a la inversa).
- **Suport i credibilitat**: 1-2 evidències per argument. Cites breus amb atribució clara.
- **Pensament crític**: Refutació elaborada d'1-2 arguments contraris amb evidències de suport.
- **Tancament i coherència**: Conclusió argumentada que connecta la tesi amb el context més ampli.
- **Varietat i precisió**: Connectors argumentatius variats i precisos. Distinció entre contrast, causa i conclusió.
- **Reflexió sobre el procés**: "He jerarquitzat els arguments i he refutat una objecció amb evidències."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Claredat i explicitació**: Tesi sofisticada amb matisos conceptuals i posicionament acadèmic precís.
- **Coherència i progressió**: 3-5 arguments amb relació entre si. Pot incloure argumentació per analogia.
- **Suport i credibilitat**: Evidències variades (dades, cites, analogies). Jerarquitzades per credibilitat.
- **Pensament crític**: Refutació sistemàtica de les objeccions principals i integració dels matisos.
- **Tancament i coherència**: Conclusió que sintetitza, pot obrir noves preguntes i té veu acadèmica pròpia.
- **Varietat i precisió**: Connectors sofisticats. Pot usar modalitzadors i connectors concessius.
- **Reflexió sobre el procés**: "L'assaig té tesi, arguments jerarquitzats, refutació i conclusió amb veu acadèmica pròpia."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


