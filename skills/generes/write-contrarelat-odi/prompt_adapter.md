---
tipus: derivat
font_canonic: M3_genere-escriure-contrarelat-odi.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-25'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 562dc178c65cf28c
---

# Escriure/adaptar un contrarelat de l'odi — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un contrarelat de l'odi per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Reconeixement del mecanisme**: Identificació oral guiada: "Qui rep el dany? Que diu el text que no és veritat o que no és respectuós?" Model visual (imatge + frase).
- **Tria de modalitat i decisió de respondre**: No s'aplica: modalitat predeterminada (counterspeech simplificat, resposta directa).
- **Reconeixement de la humanitat de tots**: "La persona que diu això segurament tem ___." (1 frase guiada amb model). Cap judici de l'autor; reconeixement del dany a la victima.
- **Correcció factual**: 1 fet concret que contradiu el discurs d'odi. Font senzilla i assolible ("a classe hem vist que...").
- **Marc de dignitat i sentit**: "Una altra manera de veure-ho és ___." (1 frase guiada amb model).
- **Compromís comu**: "Podem fer ___." (1 acció concreta i immediata, guiada per model).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Reconeixement del mecanisme**: Identificació escrita: quin grup és l'objectiu? Quin mecanisme (estereotip / generalització / deshumanització)? 1-2 frases amb model.
- **Tria de modalitat i decisió de respondre**: Triar: "Puc respondre amb fets?" (counterspeech directe) o "Cal canviar el marc?" (counter-narrative). 1 frase de justificació.
- **Reconeixement de la humanitat de tots**: Empàtic vers l'autor (comprendre la por o necessitat al darrere, sense validar el discurs) + vers la victima (reconèixer el dany). 2 frases.
- **Correcció factual**: 2 fets verificats. Font citada breument. Connexió directa amb la falsedat identificada al Pas 1.
- **Marc de dignitat i sentit**: Narrativa breu (2-3 frases) que proposa un marc d'inclusió o dignitat. Apel·lació a un valor compartit (justicia, respecte, igualtat).
- **Compromís comu**: 1 acció deliberativa concreta i assolible per a l'alumne o el grup. Formulació positiva (cap a, no contra).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Reconeixement del mecanisme**: Identificació del mecanisme retòric concret (fal·làcia, apel·lació emocional, generalitzacio abusiva) + audiencia diana.
- **Tria de modalitat i decisió de respondre**: Selecció de modalitat justificada amb argumentació: per quin motiu tries counterspeech o counter-narrative en aquest cas concret?
- **Reconeixement de la humanitat de tots**: Imaginar-se com se sent la victima: "Que deu sentir quan llegeix aquest discurs?" I per que l'autor el diu: "Quina por o necessitat hi pot haver al darrere?" 2 frases de perspectiva, sense validar el discurs.
- **Correcció factual**: 3 fets estructurats amb fonts. Distinció explícita entre fet / opinió / falsedat. Presentació ordenada.
- **Marc de dignitat i sentit**: Narrativa alternativa coherent: reconstruir la imatge del grup estigmatitzat amb evidencies i, si és possible, testimoniatge personal.
- **Compromís comu**: Crida especifica a l'audiencia: acció deliberativa + participació democratica. Formulació que inclou el grup diana.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Reconeixement del mecanisme**: Analisi del context de producció: qui parla, a qui, per quin motiu, en quin medi. Efecte sobre la victima i sobre l'audiencia.
- **Tria de modalitat i decisió de respondre**: Analisi de l'audiencia per triar modalitat: la resposta directa arriba a qui necessita llegir-la? O cal canviar el marc? Justificació estrategica.
- **Reconeixement de la humanitat de tots**: Analisi de l'emoció dominant al discurs d'odi (por, ràbia, inseguretat, necesitat d'identitat) + proposta d'empatia especifica que no valida el discurs.
- **Correcció factual**: Fact-checking sistematic: cada afirmació discriminatoria del discurs d'odi confrontada amb evidencia verificada. Fonts diverses i creïbles citades.
- **Marc de dignitat i sentit**: Counter-narrative completa: canvia el marc del debat. Apel·la a valors compartits (drets humans, dignitat, ciutadania) i proposa una comprensió alternativa.
- **Compromís comu**: Crida a l'acció comunitaria fonamentada: connecta l'acció amb valors compartits i institucions democratiques. Llista de recursos o vies concretes.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Reconeixement del mecanisme**: Identificació del mecanisme ideologic de fons (construcció de l'Altre, exclusió sistematica, reificació) + cadena de distorsió fins al text.
- **Tria de modalitat i decisió de respondre**: Discerniment ignasià complet: Quina resposta serveix MES el bé de la persona i el bé comu? No la mes efectiva retòricament, sinó la mes justa i reconciliadora.
- **Reconeixement de la humanitat de tots**: Lectura hermenèutica des de *Fratelli tutti*: "cultura del descart" com a diagnòstic estructural. Resposta que dignifica l'autor i la victima, no que condemna ni exclouen.
- **Correcció factual**: Analisi epistemologica: d'on ve la falsedat? Quins interessos serveix? Com es perpetua i amplifica? Fonts primaries citades. Mecanismes de verificació explicitats.
- **Marc de dignitat i sentit**: Narrativa transformadora (counter-narrative indirecte): proposa una comprensió del mon que fa impossible el discurs d'odi. Apel·la a la fraternitat universal (*Fratelli tutti*) i a les 4 dimensions civils.
- **Compromís comu**: Crida transformadora (CG36): proposa condicions estructurals per a la reconciliació. No acció individual sino canvi de cultura. Fonamentada en *Fratelli tutti* cap. VI (dialeg i amistat social).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


