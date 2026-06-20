---
tipus: derivat
font_canonic: M3_genere-escriure-fabula.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-20'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 952f37c4fbfcac05
---

# Escriure/adaptar una fàbula — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una fàbula per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Nombre i definició**: 2 personatges amb un tret únic cadascun (ràpid/lent, llest/ingenu). Noms genèrics ("La llebre", "La tortuga").
- **Consistència**: El personatge ràpid és ràpid de principi a fi. Cap canvi de caràcter.
- **Context i tensió**: Situació en 1-2 frases. Incident simple que posa la narració en moviment.
- **Causalitat i coherència**: Acció en 1-2 frases. Desenllaç clar i directe. Conseqüència evident del tret del personatge.
- **Format i universalitat**: 1 frase curta. Sempre precedida de "Moral:". Universal: aplicable fora de la historia.
- **Llargada**: 6-8 frases totals. Moral d'1 frase.
- **Llengua i registre**: Sense fórmules arcaiques ("En un llunyà temps..."). Llengua actual. Passat simple.
- **Fidelitat al text font**: Fidelitat a la moral original i als arquetips. L'acció pot simplificar-se.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Nombre i definició**: 2 personatges arquetípics ben definits des del primer paràgraf. Tret únic explícit al text.
- **Consistència**: Caràcter consistent en tots els actes del personatge.
- **Context i tensió**: Situació + fet desencadenant diferenciats en paràgrafs o frases separades. El fet crea una tensió senzilla.
- **Causalitat i coherència**: Acció narrada amb connectors temporals simples. Desenllaç coherent amb el caràcter.
- **Format i universalitat**: 1-2 frases. Precedida de "Moral:". Aplicable a situacions reals que l'alumne pot reconèixer.
- **Llargada**: 8-12 frases. Moral d'1-2 frases.
- **Llengua i registre**: Idem. Sense temps verbals arcaics.
- **Fidelitat al text font**: Fidelitat a la moral i als personatges arquetípics.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Nombre i definició**: 2-3 personatges amb tret únic consistent durant tota la fàbula. El tret s'anuncia al principi.
- **Consistència**: Caràcter mantingut fins al desenllaç. El desenllaç deriva directament del caràcter.
- **Context i tensió**: Situació amb context del tret dels personatges + fet que posa el tret a prova.
- **Causalitat i coherència**: Acció amb causa-efecte explícit. Desenllaç que deriva directament i de forma inequívoca del caràcter.
- **Format i universalitat**: 2 frases. Explícita, universal i ben argumentada. El lector no ha d'inferir-la.
- **Llargada**: 3-4 paràgrafs + moral.
- **Llengua i registre**: Idem. Registre literari simple admissible sense arcaisme.
- **Fidelitat al text font**: Fidelitat a la moral, als arquetips i a la tensió moral del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Nombre i definició**: 3-4 personatges amb trets complementaris o oposats. Les relacions entre trets generen el conflicte.
- **Consistència**: Caràcter consistent. Pot incloure un moment d'auto-engany del personatge (mantenir el tret fins a les últimes conseqüències).
- **Context i tensió**: Situació ben construïda que prepara el conflicte moral. Context suficient per comprendre els trets.
- **Causalitat i coherència**: Acció amb tensió creixent. Desenllaç que justifica plenament la moral, no pot ser d'una altra manera.
- **Format i universalitat**: Explícita. Connecta la historia amb un principi general aplicable fora del context concret.
- **Llargada**: 3-4 paràgrafs ben diferenciats + moral (2 frases).
- **Llengua i registre**: Idem. Recursos expressius admissibles si no son arcaics.
- **Fidelitat al text font**: Fidelitat a la moral, als arquetips i al to del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Nombre i definició**: Personatges amb complexitat arquetípica. El tret pot tenir matisos sense trencar l'arquetip ni la moral.
- **Consistència**: Arquetip consistent però amb matisos que enriqueixen la moral sense contradir-la.
- **Context i tensió**: Situació elaborada que posa en tensió valors o concepcions del món. El conflicte moral és evident des del principi.
- **Causalitat i coherència**: Acció elaborada. Desenllaç que pot tenir ironia lleugera si la moral ho suporta i s'explicita.
- **Format i universalitat**: Explícita però no simplista. Pot plantejar una tensió entre valors o un dilema, però mai implícita.
- **Llargada**: Fàbula completa amb riquesa descriptiva + moral elaborada (fins a 3 frases).
- **Llengua i registre**: Sense arcaismes que dificultin la comprensió. Usos estilístics conscients (pastitx literari) admissibles si no comprometen la claredat.
- **Fidelitat al text font**: Fidelitat a la moral, als arquetips, al to i a la intenció del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


