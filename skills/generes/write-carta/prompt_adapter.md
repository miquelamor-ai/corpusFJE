---
tipus: derivat
font_canonic: M3_genere-escriure-carta.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: b2814a508b93ec18
---

# Escriure/adaptar una carta — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una carta per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Format i completitud**: Lloc i data en format simple: "Barcelona, 12 de maig".
- **Registre i adequació**: "Hola [nom]," (informal) / "Estimat/da [nom]:" (formal molt simple).
- **Claredat i posició**: 1 frase que diu per qué s'escriu: "T'escric per..." Sense preàmbuls.
- **Focus i concreció**: 1 petició molt simple: "Et demano que..." Sense acumulació de demandes.
- **Consistència i adequació**: Informal (amic/família) o formal molt simple (desconegut). Consistent en tot el text.
- **Comiat i signatura**: "Fins aviat, [nom]." (informal) / "Salutacions, [nom]." (formal). Consistent amb la salutació.
- **Fórmules arcaiques**: Cap fórmula arcaica. Si apareix al text font, s'actualitza.
- **Fidelitat al text font**: Fidelitat al motiu principal i al registre bàsic.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Format i completitud**: Lloc, data i nom del destinatari complets.
- **Registre i adequació**: Salutació ajustada al registre: informal (amic/família) / formal (autoritat/desconegut).
- **Claredat i posició**: Motiu explícit al primer paràgraf. Directe i clar. Cap introducció sobre el benestar del destinatari.
- **Focus i concreció**: 1 petició clara i directa. Sense preguntes múltiples ni demandes encadenades.
- **Consistència i adequació**: Distinció clara entre formal i informal. Registre consistent. Cap barreja.
- **Comiat i signatura**: Comiat ajustat al registre. Nom complet a la carta formal.
- **Fórmules arcaiques**: Idem. Cap fórmula arcaica ni expressió obsoleta.
- **Fidelitat al text font**: Fidelitat al motiu, al registre i a la petició essencial.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Format i completitud**: Encapçalament complet: lloc, data, nom i adreça del destinatari (carta formal).
- **Registre i adequació**: Salutació formal precisa: "Benvolgut/da senyor/a [cognom]:" sense errors de tractament.
- **Claredat i posició**: Motiu presentat amb connector introductori: "Em dirigeixo a vostè per informar-lo/la que..."
- **Focus i concreció**: Petició formulada amb justificació breu: "Li demano que... ja que..."
- **Consistència i adequació**: Registre formal o informal consistent. Vostè vs. tu ajustat al destinatari en tot el text.
- **Comiat i signatura**: Comiat formal: "Atentament," / informal: "Una salutació,". Signatura completa (nom i cognoms).
- **Fórmules arcaiques**: Idem. Fórmules de cortesia contemporànies.
- **Fidelitat al text font**: Fidelitat al motiu, al registre, a la petició i a l'estructura de 7 parts.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Format i completitud**: Encapçalament complet i ben formatat. Referència o assumpte si escau.
- **Registre i adequació**: Salutació formal amb tractament correcte i consistent amb el to de la carta.
- **Claredat i posició**: Motiu presentat amb context breu i connector formal. El lector sap per qué s'escriu a la primera frase.
- **Focus i concreció**: Petició argumentada: context + raó + demanda concreta. Anticipació possible: "Sóc conscient que..."
- **Consistència i adequació**: Registre formal sofisticat. Cap expressió col·loquial a la carta formal.
- **Comiat i signatura**: Comiat protocol·lari adequat al registre i al to de la carta.
- **Fórmules arcaiques**: Idem. Pot usar fórmules formals però no antiquades.
- **Fidelitat al text font**: Fidelitat a la complexitat argumentativa i al to del remitent.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Format i completitud**: Encapçalament professional complet. Pot incloure referència, assumpte i número d'expedient.
- **Registre i adequació**: Salutació formal o protocol·lària si el context ho exigeix. Tractament perfectament ajustat.
- **Claredat i posició**: Motiu presentat amb precisió i context necessari per al destinatari. Pot incloure referència a una comunicació prèvia.
- **Focus i concreció**: Petició amb argumentació elaborada i recursos de persuasió (empatia, reciprocitat).
- **Consistència i adequació**: Registre adaptat amb matisos de cortesia i protocol. El to és inequívocament professional o personal.
- **Comiat i signatura**: Comiat i signatura professionals. Pot incloure càrrec, institució o funció del remitent.
- **Fórmules arcaiques**: Idem. Registre professional actual, sense arcaismes.
- **Fidelitat al text font**: Fidelitat a la complexitat, al to i als recursos retòrics del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


