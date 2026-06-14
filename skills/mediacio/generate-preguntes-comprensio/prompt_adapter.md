---
tipus: derivat
font_canonic: M3_instrument-generar-preguntes-comprensio.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-14'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 3c6d476df71dbc7a
---

# Generar preguntes de comprensió — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar preguntes de comprensió per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Activació + propòsit**: Adult estableix el propòsit en veu alta. Consigna de predicció visual: "Assenyala la imatge que creus que explica de qué va el text."
- **Aturada estratègica**: Adult atura i pregunta: "Mostra'm on és [element del text]." Assenyalar o apuntar.
- **3 plànols cognitius**: Literal: "Assenyala la imatge de [element del text]" o "Dibuixa [element]." Inferencial: "Per qué creus que...?" (oral, mediat). Crític: "Qué hauries fet tu?" (oral).
- **Format + modalitat + acarament**: Consignes d'acció (mai V/F). Cap numeració: usar `-`. Cap etiqueta visible [Literal]. Màxim 6 consignes.
- **Metacognició**: "He assenyalat les imatges que m'ha demanat el mestre." (oral, mediat per adult)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Activació + propòsit**: Activació: "Escriu 1 paraula sobre el que saps de [tema]." Propòsit: "Llegeix per saber [X concret]."
- **Aturada estratègica**: "Para a [punt]. Hi ha alguna paraula que no entens? Marca-la amb ?."
- **3 plànols cognitius**: Literal: V/F senzill o omple buit amb llista tancada. Inferencial: inferència mínima connectada a evidència visual o mot clau del text ("Per qué creus que [element]? Mira [part del text]"). Crític: oral o dibuix ("T'ha agradat? Dibuixa com t'has sentit").
- **Format + modalitat + acarament**: Mai V/F de frase complexa. Mai "copia i enganxa" (resposta copiable sense processament). Frases pregunta: màxim 10 paraules. Màxim 8 preguntes totals. LITERARI: "Qui és el personatge? Com se sent?" INFORMATIU: "Quina és la informació més important?"
- **Metacognició**: "He respost si és vertader o fals. He omplert els buits."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Activació + propòsit**: Activació: "Escriu 2-3 coses que saps sobre [tema]." Propòsit: "Llegeix per trobar [2 informacions concretes]."
- **Aturada estratègica**: "Para a [punt]. Escriu en 1 frase el que ha passat fins ara."
- **3 plànols cognitius**: Literal: ordenar seqüències, relacionar amb fletxes. Inferencial: causa literal al text ("Per qué...? Busca-ho al text"). Crític: "Qué hauria passat si [canvi]?" Resposta breu.
- **Format + modalitat + acarament**: Frases pregunta: màxim 12 paraules. Màxim 10 preguntes. LITERARI: pregunta afectiva. INFORMATIU: pregunta de precisió. Acarament L1 (si nouvingut): "Com es diu [terme clau] en la teva llengua?"
- **Metacognició**: "He ordenat les idees. He trobat la idea principal."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Activació + propòsit**: Activació + 2 preguntes pròpies: "Qué saps? Qué et preguntes?" Propòsit: "Llegeix per entendre com [causa-efecte o seqüència]."
- **Aturada estratègica**: "Para a [punt]. Quina hipòtesi tens sobre el que passarà o dirà a continuació?"
- **3 plànols cognitius**: Literal: 1-2 frases, resposta explícita al text. Inferencial: deducció relacional ("Quin efecte té [causa]? Argumenta-ho"). Crític: postura justificada (literari: sentiments; informatiu: fiabilitat de les dades).
- **Format + modalitat + acarament**: Frases pregunta: màxim 15 paraules. Màxim 10 preguntes. LITERARI: símbols i metàfores simples. INFORMATIU: jerarquitzar amb connectors. Acarament L1 (si nouvingut): "El text s'escriuria igual en la teva llengua?"
- **Metacognició**: "He deduït informació que no estava explícita al text. He fet una hipòtesi durant la lectura."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Activació + propòsit**: Activació del marc teòric o experiència prèvia. Propòsit d'avaluació: "Llegeix per avaluar si [afirmació] és vàlida."
- **Aturada estratègica**: "Para a [punt]. Quina idea principal s'ha presentat fins ara? Com s'estructura argumentalment?"
- **3 plànols cognitius**: Literal: resum de 3-5 frases amb jerarquització. Inferencial: justificació + referència al text. Crític: argumentació oberta + avaluació de la fiabilitat.
- **Format + modalitat + acarament**: Màxim 10 preguntes. LITERARI: veu narrativa i intenció estètica. INFORMATIU: fiabilitat de les dades. Acarament L1 (si nouvingut): contrast d'argumentació entre català i L1.
- **Metacognició**: "He argumentat les meves respostes amb referències al text. He avaluat si les dades eren fiables."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Activació + propòsit**: Propòsit d'anàlisi autorial: "Llegeix per analitzar com l'autor construeix la seva postura i quines proves aporta."
- **Aturada estratègica**: "Para a [punt]. Quina és la postura de l'autor fins aquí? Quines proves ha aportat? N'hi ha d'absents?"
- **3 plànols cognitius**: Literal: síntesi estructurada jerarquitzada. Inferencial: relacions implícites complexes, ironia, subtext. Crític: judici sobre intencionalitat, contrast amb fonts alternatives.
- **Format + modalitat + acarament**: Màxim 10 preguntes (prioritzar qualitat). LITERARI: intertextualitat i intencionalitat. INFORMATIU: contrast de fonts i biaix. Acarament L1 (si nouvingut): contrast metalingüístic i discursiu.
- **Metacognició**: "He analitzat la intencionalitat de l'autor i he qüestionat les seves afirmacions. He contrastat amb el que ja sabia."

