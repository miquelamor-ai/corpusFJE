---
tipus: derivat
font_canonic: M3_instrument-generar-tolc.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-20'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: a50ac73d09c2b8b3
---

# Generar TOLC / transllenguatge — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar tolc / transllenguatge per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Tipus de pregunta comparativa**: Oral: "Com es diu X en la teva llengua?" — cap escriptura. El docent recull la resposta.
- **Forma de l'acarament**: Cap escriptura. Assenyalar o dibuixar el concepte.
- **Semblances primer**: Cap observació: activitat oral i manipulativa.
- **Pont de producció**: Oral mediat: "Dibuixa o assenyala mentre ho dius." Dictat a l'adult si l'alumne vol escriure.
- **Protecció de l'alumne**: Sempre voluntari. "Si vols, si pots." Cap exposició pública.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Tipus de pregunta comparativa**: Pregunta oral + pictograma: "Com es diu [paraula clau] en la teva llengua?" Resposta optional escrita.
- **Forma de l'acarament**: Taula 2 columnes: 3-5 parells paraula L1 (alfabet original) / paraula català.
- **Semblances primer**: Cap observació a A1: massa càrrega metalingüística.
- **Pont de producció**: Dictat a l'adult o assenyalar. "Pots dir-ho en veu alta si vols."
- **Protecció de l'alumne**: Sempre voluntari. La consigna no exposa l'alumne. La taula és personal.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Tipus de pregunta comparativa**: Activació escrita: "Com es diu «[concepte clau]» en la teva llengua?"
- **Forma de l'acarament**: Taula 2 columnes: 3-5 parells + 1 observació de semblança/diferència estructural senzilla.
- **Semblances primer**: 1 frase positiva: semblances primer, diferències com a curiositat. Mai observació negativa.
- **Pont de producció**: Frase curta: escriu en català una idea del text usant un connector de la taula (si vols, primer en L1).
- **Protecció de l'alumne**: Voluntari. Mai exigir L1 públicament. "Comparteix-ho si vols" sempre present.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Tipus de pregunta comparativa**: Activació comparativa: "«[concepte]» en [L1] s'expressa com ___. En català usem ___. Qué observes?"
- **Forma de l'acarament**: Contrast de connectors i construccions causals L1↔català. Taula o paràgraf breu.
- **Semblances primer**: Observació sobre construcció causal o estructural (ordre SVO, posició adjectiu, connectors).
- **Pont de producció**: Paràgraf breu: resumir en L1 una part del text, o traduir una conclusió al català usant els connectors apressos.
- **Protecció de l'alumne**: Voluntari. Mediació accessible sense revelar la L1 si l'alumne no vol.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Tipus de pregunta comparativa**: Activació metalingüística: contrast de construccions gramaticals entre L1 i català.
- **Forma de l'acarament**: Contrast de l'organització del gènere entre L1 i català. Com s'estructura el text en cada llengua.
- **Semblances primer**: Observació sobre l'organització del gènere entre les dues llengues. Gèneres similars i divergents.
- **Pont de producció**: Mediació complexa: mediar un text complet entre L1 i català. Comparar l'organització de les idees.
- **Protecció de l'alumne**: Voluntari. L'alumne pot triar fer la mediació en L1 o directament en català.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Tipus de pregunta comparativa**: Activació crítica: contrast entre sistemes lingüístics i convencions culturals del gènere discursiu.
- **Forma de l'acarament**: Contrast d'intenció comunicativa i convencions retòriques entre L1 i català. Biaix cultural del gènere.
- **Semblances primer**: Observació crítica sobre com les dues llengues codifiquen el coneixement de forma diferent. Convencions retòriques.
- **Pont de producció**: Contrast escrit: analitza com el gènere treballat es construiria diferent en L1 i en català.
- **Protecció de l'alumne**: Voluntari. L'alumne decideix el grau d'integració de la seva L1 en l'anàlisi crítica.

