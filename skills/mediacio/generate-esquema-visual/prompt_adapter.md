---
tipus: derivat
font_canonic: M3_instrument-generar-esquema-visual.md
font_version: 1.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-25'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 153f17d80ff1c914
---

# Generar esquema visual — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar esquema visual per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Selecció**: El concepte més imatge-amigable del text. Sovint un objecte concret amb pictograma.
- **Format de la cel·la arrel**: Una sola paraula o frase de 2 paraules amb pictograma al costat.
- **Total nodes**: 2-3 nodes. Seqüències temporals bàsiques (abans→després) o relacions imatge→paraula.
- **Profunditat de l'arbre**: 1 nivell (arrel + fills directes).
- **Marcat textual**: Llista markdown amb guions `-` i sagnia de 2 espais per nivell. PICTOGRAMES inline obligatoris a l'arrel i a les fulles principals.
- **Format prohibit**: NO fletxes Unicode (→, ↓, ↔). NO ASCII-art (|, ├, └, ─). NO emojis decoratius.
- **Predominant**: Seqüència temporal simple o relació part-tot.
- **Etiquetes a les connexions**: No (només estructura).
- **Una sola arrel**: Una sola arrel per esquema. Sense múltiples nodes a profunditat 0.
- **Node central canònic**: A gèneres procedimentals (instructiu/receptari/manual): el node central és el PRODUCTE/OBJECTIU final, NO un apartat seqüencial. A gèneres expositius: el TEMA principal. A gèneres narratius: NO s'aplica esquema visual.
- **No-soroll visual**: Cap node decoratiu sense informació.
- **Fidelitat al text font**: Cada node ha de poder traçar-se a una frase o concepte del text adaptat.
- **Reflexió sobre el procés**: "He mirat l'esquema quan no entenia com es connectaven les coses."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Selecció**: El subjecte/tema principal explícit del títol.
- **Format de la cel·la arrel**: Una sola paraula clau.
- **Total nodes**: 3-4 nodes. Enumeració de qualitats o parts d'un objecte (descripció simple).
- **Profunditat de l'arbre**: 1-2 nivells.
- **Marcat textual**: Llista markdown amb guions `-` i sagnia 2 espais. Pictogrames recomanats per a fulles concretes.
- **Format prohibit**: Idem.
- **Predominant**: Enumeració paral·lela (germans).
- **Etiquetes a les connexions**: No.
- **Una sola arrel**: Idem.
- **Node central canònic**: Idem.
- **No-soroll visual**: Idem.
- **Fidelitat al text font**: Idem.
- **Reflexió sobre el procés**: "He buscat l'arrel quan no entenia de què parlava el text."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Selecció**: El tema principal o producte final del text.
- **Format de la cel·la arrel**: Una frase nominal curta (1-4 paraules).
- **Total nodes**: 4-6 nodes. Seqüència de passos d'instrucció o esdeveniments cronològics.
- **Profunditat de l'arbre**: 2 nivells (arrel → branca → fulla).
- **Marcat textual**: Llista markdown amb guions `-` i sagnia 2 espais.
- **Format prohibit**: Idem.
- **Predominant**: Seqüència cronològica o passos numerats.
- **Etiquetes a les connexions**: Opcional ("primer", "després").
- **Una sola arrel**: Idem.
- **Node central canònic**: Idem.
- **No-soroll visual**: Idem.
- **Fidelitat al text font**: Idem.
- **Reflexió sobre el procés**: "He fet servir l'esquema per recordar l'ordre dels passos."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Selecció**: El concepte abstracte o procés que organitza el text.
- **Format de la cel·la arrel**: Frase nominal (3-6 paraules).
- **Total nodes**: 6-8 nodes. Relacions causa-efecte o hipòtesi-evidència.
- **Profunditat de l'arbre**: 2-3 nivells.
- **Marcat textual**: Idem.
- **Format prohibit**: Idem.
- **Predominant**: Causa-efecte explícita o hipòtesi-evidència.
- **Etiquetes a les connexions**: Etiquetes amb connectors lògics (perquè, llavors).
- **Una sola arrel**: Idem.
- **Node central canònic**: Idem.
- **No-soroll visual**: Idem.
- **Fidelitat al text font**: Idem (i a derivacions justificades a B1+).
- **Reflexió sobre el procés**: "He revisat l'esquema per veure quina idea és central i quines són secundàries."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Selecció**: El concepte clau analític del text.
- **Format de la cel·la arrel**: Concepte abstracte expressat amb 1-2 paraules tècniques.
- **Total nodes**: 8-12 nodes amb subnivells. Estructures complexes amb arrel + branques + sub-branques.
- **Profunditat de l'arbre**: 3 nivells.
- **Marcat textual**: Idem.
- **Format prohibit**: Idem.
- **Predominant**: Categorització jeràrquica abstracta.
- **Etiquetes a les connexions**: Etiquetes amb connectors causals/contrastius.
- **Una sola arrel**: Idem.
- **Node central canònic**: Idem.
- **No-soroll visual**: Idem.
- **Fidelitat al text font**: Idem.
- **Reflexió sobre el procés**: "He construït el meu propi esquema d'un text similar per veure si entenia l'estructura."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Selecció**: El concepte estructurant del discurs (no necessàriament explícit).
- **Format de la cel·la arrel**: Concepte abstracte amb possible distinció disciplinar.
- **Total nodes**: 10-15 nodes amb 3-4 nivells de profunditat. Estructures conceptuals amb categories i sub-categories.
- **Profunditat de l'arbre**: 3-4 nivells.
- **Marcat textual**: Idem.
- **Format prohibit**: Idem.
- **Predominant**: Estructures discursives complexes (tesi-arguments-refutació).
- **Etiquetes a les connexions**: Etiquetes amb metallenguatge ("contraargument", "pressupòsit").
- **Una sola arrel**: Idem.
- **Node central canònic**: Idem.
- **No-soroll visual**: Idem.
- **Fidelitat al text font**: Idem (els meta-discursius sí entren).
- **Reflexió sobre el procés**: "He reflexionat sobre si l'esquema captura l'estructura argumental real del text o és una simplificació."

