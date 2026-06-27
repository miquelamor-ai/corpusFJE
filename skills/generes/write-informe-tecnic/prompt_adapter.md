---
tipus: derivat
font_canonic: M3_genere-escriure-informe-tecnic.md
font_version: 1.0.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-27'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 0812766766edaf22
---

# Escriure/adaptar un informe tècnic — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un informe tècnic per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Identificació professional**: Títol + nom de l'alumne + a qui va dirigit (1 línia: "Per a: [empresa/persona]"). Data.
- **Síntesi per al decisor**: Absenta o molt breu (2-3 frases: "He inspeccionat X. He trobat Y. Cal fer Z."). Pot ser oral amb l'adult.
- **Context i abast**: 2-3 frases: de quina instal·lació/producte/situació es tracta i per quin motiu s'ha fet l'informe.
- **Traçabilitat del procés**: Llista de 3-5 passos de com s'ha fet la inspecció o l'anàlisi. Frases simples.
- **Fidelitat a les mesures**: Dades en taula simple (2-3 columnes). Valor + unitat sempre intactes. 1-2 frases que diuen "s'ha observat X".
- **HCL Justificar**: 1-2 frases: "Això vol dir que..." o "Per tant...". La connexió resultat → implicació és explícita però simple.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Identificació professional**: Portada completa: títol, autor, data, destinatari (nom + càrrec + empresa), número d'informe si escau.
- **Síntesi per al decisor**: Resum executiu de 3-5 línies: problema principal + conclusió central + recomanació clau. Autònom: llegit sol, el decisor pot actuar.
- **Context i abast**: Context, objectiu de l'informe i abast (què s'ha inspeccionat/analitzat i què no).
- **Traçabilitat del procés**: Procediment en paràgraf breu: instruments usats, condicions de la inspecció, mostra o àmbit analitzat.
- **Fidelitat a les mesures**: Dades en taula o gràfic amb llegenda. Descripció objectiva de la tendència o l'estat ("el valor supera el llindar de...").
- **HCL Justificar**: Anàlisi per bloc de resultats: connexió resultat → causa probable → implicació. Connector "per tant" i "a causa de" actius.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Identificació professional**: Portada professional amb tots els camps estàndard del sector.
- **Síntesi per al decisor**: Resum executiu de 1 paràgraf: context breu + principals troballes + recomanació prioritària. Formal.
- **Context i abast**: Introducció estructurada: context sectorial, objectiu, abast, marc normatiu o legal aplicable si escau.
- **Traçabilitat del procés**: Metodologia amb instruments, mostra, condicions i limitacions del procés. Variables identificades.
- **Fidelitat a les mesures**: Dades organitzades per categories o subsistemes. Gràfic o taula per a la comparació. Descripció objectiva.
- **HCL Justificar**: Anàlisi argumentada: relació causal entre resultats i causes, comparació amb valors de referència o normativa. Justificació de les conclusions.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Identificació professional**: Portada formal amb identificació institucional completa (empresa emissora, empresa receptora, referència de l'encàrrec).
- **Síntesi per al decisor**: Resum executiu professional complet: context, objectiu, metodologia sintètica, conclusions principals prioritzades, recomanació clau. Llegit sol, substitueix el cos per a la direcció.
- **Context i abast**: Introducció acadèmico-professional: context, objectiu, hipòtesi o pregunta tècnica, abast, normativa i referències al sector.
- **Traçabilitat del procés**: Metodologia rigorosa: instruments calibrats, condicions de mesura, mostra representativa, normativa tècnica aplicada, incertesa de mesura.
- **Fidelitat a les mesures**: Dades en formats variats (taules, gràfics, fotografies etiquetades). Anàlisi estadística si escau. Traçabilitat de cada mesura.
- **HCL Justificar**: Anàlisi crítica: relació causal documentada, discussió de causes alternatives, comparació amb normativa i literatura tècnica, reconeixement de limitacions de l'anàlisi.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


