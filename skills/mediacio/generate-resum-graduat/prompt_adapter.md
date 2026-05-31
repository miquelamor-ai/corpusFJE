---
tipus: derivat
font_canonic: M3_instrument-generar-resum-graduat.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-05-31'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 84118c29a936765d
---

# Generar resum graduat — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar resum graduat per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Estructura del suport**: Activitat oral: "De qui parla? Qué fa? Com acaba?" El docent escriu el dictat de l'alumne. Sense marc escrit.
- **Calibrat ZDP**: Cap forat: activitat oral.
- **Coherència discursiva**: Preguntes orals adaptades: narratiu → "Qui? Qué fa? Com acaba?" / expositiu → "De qué parla? Qué és important?"
- **Modalitat de producció**: Recapitular oral: reordenar informació oral o visual. El docent escriu el dictat; l'alumne dicta.
- **Metacognició**: "He dit el que passava al text en veu alta." (oral, mediat per adult)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Estructura del suport**: Frase marc amb 1-2 forats + opcions tancades a triar. "El text parla de [tria: opció A / opció B / opció C]."
- **Calibrat ZDP**: Forat de 1-3 paraules. Opcions totes plausibles: una sola correcta.
- **Coherència discursiva**: Marc adaptat: narratiu → personatge / acció / desenllaç. Expositiu → tema / punt clau / final.
- **Modalitat de producció**: Recapitular assistit: triar la resposta correcta és una forma de recapitular. Cap escriptura de frases pròpies.
- **Metacognició**: "He triat la resposta correcta. He omplert els buits amb la paraula que encaixava."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Estructura del suport**: Marc de 2-3 frases amb 3-4 forats oberts (sense opcions). L'alumne omple amb paraules pròpies.
- **Calibrat ZDP**: Forat d'1 frase (5-10 paraules) sense opcions: l'alumne reformula (no copia). Connectors donats entre frases.
- **Coherència discursiva**: Marc de 2-3 frases adaptat amb connectors donats (Primer... Llavors... Al final...).
- **Modalitat de producció**: Resumir amb bastida completa: primera producció escrita del resum. Marc molt explícit amb connectors donats.
- **Metacognició**: "He escrit el resum amb el marc. He usat les meves paraules (no he copiat frases del text)."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Estructura del suport**: Marc de 3 parts (tema / punts clau / conclusió) amb 1-2 frases lliures per part. Connectors no donats.
- **Calibrat ZDP**: Forat de 2-3 frases amb paraules pròpies i reorganització de la informació.
- **Coherència discursiva**: Marc de 3 seccions etiquetades: Tema / Punts clau / Conclusió. Connectors no donats.
- **Modalitat de producció**: Resumir amb marc parcialment retirat: l'alumne construeix les idees; el marc proposa l'estructura.
- **Metacognició**: "He resumit les idees principals en 3 parts. He usat connectors per lligar les idees."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Estructura del suport**: Criteris de qualitat del resum (4-5 ítems basats en les macroregles). L'alumne escriu el resum complet.
- **Calibrat ZDP**: Criteri obert: "Has seleccionat les idees principals (no els exemples)? Has generalitzat?"
- **Coherència discursiva**: Criteris que cobreixen les macroregles: selecció (excloure exemples), generalització (categoria), construcció (inferit).
- **Modalitat de producció**: Resumir amb criteris: l'alumne usa les macroregles per produir i autoavaluar el resum.
- **Metacognició**: "He seleccionat les idees principals (no els exemples). He comprovat que el resum s'entén sense llegir el text."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Estructura del suport**: Rúbrica metacognitiva: l'alumne justifica les tries. Resum lliure + reflexió sobre el que ha inclòs i deixat fora.
- **Calibrat ZDP**: Criteri metacognitiu: "Explica per qué has triat incloure aquesta idea i no aquella altra."
- **Coherència discursiva**: Reflexió discursiva: "Qué has decidit NO incloure i per qué? Quin criteri de selecció has usat?"
- **Modalitat de producció**: Resumir i reflexionar: el resum és el punt de partida d'una reflexió metacognitiva sobre les decisions de selecció.
- **Metacognició**: "He justificat per qué he triat cada idea i per qué n'he deixat d'altres fora. He revisat que el meu resum és precís i honest."

