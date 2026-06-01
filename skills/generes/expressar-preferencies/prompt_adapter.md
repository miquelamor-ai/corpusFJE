---
tipus: derivat
font_canonic: M3_genere-expressar-preferencies.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-01'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: ff727a7c217cb3f4
---

# Expressar preferències — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere expressar preferències per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **1a persona i directesa**: Oral: "M'agrada [X]" / "No m'agrada [X]". Mediat per adult si cal. Pictograma de cara somrient/trista + paraula clau.
- **Concretesa del referent**: El referent és un objecte, un animal, un aliment o una activitat quotidiana. Visual i tocable. L'adult el pot mostrar amb imatge o objecte real.
- **Gradacio de la preferència**: "Molt" / "una mica" / "gens". L'adult pot mostrar una escala de cares (somrient/neutra/trista) i l'alumne assenyala.
- **Imatge + paraula**: Pictograma de cara emocional + paraula clau del referent + dibuix o foto si cal. L'adult escriu la paraula, l'alumne assenyala o dicta.
- **Veu personal**: La preferència és propia (no copiada del company o del docent). L'adult verifica amb pregunta: "És el que tu penses, o el que pensa el company?"
- **Metacognicao**: Autoavaluacio oral mediada: l'adult pregunta "Has dit el que a TU t'agrada?" i registra la resposta.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **1a persona i directesa**: Escrit: "M'agrada [X]" / "No m'agrada [X]". 1 frase en primera persona. Sense "trobo que" ni "em sembla".
- **Concretesa del referent**: El referent és concret i conegut. L'alumne el nomena amb paraules que ja sap. Cap referent abstracte (la pau, la justicia).
- **Gradacio de la preferència**: "M'agrada molt X" / "M'agrada una mica X" / "No m'agrada gens X". Gradacio en 3 nivells amb suport pictografic.
- **Imatge + paraula**: Pictograma de cara emocional + paraula clau del referent escrita per l'alumne. La imatge i la paraula son codeterminals.
- **Veu personal**: La preferència és en primera persona i autentica. No és una descripcio neutra ni una generalitzacio ("tothom agrada X").
- **Metacognicao**: "He dit el que a mi m'agrada. He posat el dibuix o la foto del que m'agrada."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)


### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


