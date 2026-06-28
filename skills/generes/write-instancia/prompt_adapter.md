---
tipus: derivat
font_canonic: M3_genere-escriure-instancia.md
font_version: 1.1.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 8e2c49a289a2610f
---

# Escriure/adaptar una instància — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una instància per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Completesa i format**: Nom complet + DNI/NIE + adreça en un bloc compacte. Format convencional simplificat: "Jo, [NOM], amb DNI/NIE [X], domiciliat/ada a [ADREÇA]".
- **Formalitat del càrrec**: Càrrec en majúscules al final del document: "AL/A LA [CÀRREC] DE [INSTITUCIÓ]". Càrrecs habituals del context educatiu o local.
- **Densitat i estructura argumentativa**: 1 motiu clar exposat en 1-2 frases simples. Connector introductori: "Que". Fets verificables, no opinions.
- **Presència i precisió**: Absent o molt breu si és evident ("d'acord amb la normativa vigent"). No és obligatòria a B1 però no penalitza si és simple.
- **Concreció i fórmula**: Petició única, concreta i delimitable, precedida de "SOL·LICITA:" o "Per tot l'anterior, SOL·LICITA:". 1-2 frases màxim. Infinitiu o que + subjuntiu.
- **Formalitat**: Fórmula simple: "Cosa que espero em serà concedida."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Completesa i format**: Bloc d'identificació complet amb totes les dades reglamentàries. Format administratiu rigorós.
- **Formalitat del càrrec**: Càrrec institucional precís. Si el destinatari immediat no és el màxim òrgan, s'adreça a qui té competència sobre la petició.
- **Densitat i estructura argumentativa**: 2-3 motius exposats en paràgrafs numerats o en seqüència causal. Motius jerarquitzats: del més rellevant al més secundari. Connectors argumentatius ("en primer lloc", "a més a més", "per últim").
- **Presència i precisió**: Referència normativa present i identificada: article + llei o decret + any. Breu però precisa ("a l'empara de l'article 14 de la Llei X/YYYY").
- **Concreció i fórmula**: Petició principal + 1-2 peticions secundàries si escau (en ordre de preferència). Estructura clara: "1. Que se m'atorgui...; 2. Que se m'informi de...".
- **Formalitat**: Fórmula estàndard: "En espera de la vostra resolució favorable, us saludo atentament."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Completesa i format**: Bloc d'identificació complet. Si escau, títol professional o condició que reforça la legitimitat de la petició (qualitat de llicenciat/ada, de veí/na empadronat/da, de tutor/a legal).
- **Formalitat del càrrec**: Càrrec amb fórmula de tractament completa si el protocol ho exigeix ("Il·lm./Il·lma. Sr./Sra."). Coneixement del circuit administratiu: a qui s'adreça i per quins canals.
- **Densitat i estructura argumentativa**: 3 o més motius elaborats, amb jerarquització lògica i anticipació d'objeccions. Pot incitar a la concepció de la legitimitat de la petició i la competència de l'organisme. Argumentació densa i cohesionada.
- **Presència i precisió**: Citació legal precisa amb identificació de la norma, l'article i el seu contingut rellevant. Pot comparar normes o citar jurisprudència si escau. El LLM no valida si la norma és vigent; el docent revisa.
- **Concreció i fórmula**: Petició principal amb condicions o terminis si el context ho requereix. Referència al procediment administratiu esperat (resolució, notificació, termini legal).
- **Formalitat**: Fórmula completa adaptada al context institucional. Pot incloure referència al procediment de notificació preferit.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


