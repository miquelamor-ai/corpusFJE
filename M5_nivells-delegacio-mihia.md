---
title: "Nivells de delegació MIHIA (N0-N5)"
module: M5
id: M5_nivells-delegacio-mihia
review_status: esborrany
version: "1.0"
sources:
  - docs/decisions/arquitectura-quest-rol-nivell.md
  - docs/fonts/laia-knowledge/model-4d-mihia.md
  - public/exemples-rols-mihia.md
  - docs/marcs-teorics/friccio-cognitiva-extens.md
connections:
  - M5_arquitectura-proposit-rol-nivell
  - M5_rols-IA-educacio
  - M5_proposits-aprenentatge
  - M2_carrega-friccio-cognitiva
  - M5_disseny-instruccional-amb-IA
detection:
  - "Quan cal decidir quin grau d'autonomia cedeix l'alumne a la IA"
  - "Quan cal determinar el sostre de nivell per a una etapa educativa"
  - "Quan cal verificar si un nivell és coherent amb el rol i el propòsit d'aprenentatge"
---

# Nivells de delegació MIHIA (N0-N5)

> Document de referència per als skills: Classificador MIHIA, Generador d'Activitats, Dissenyador d'Assistents
> Amplia i especifica: `model-4d-mihia.md` (versió LAIA, §2)

---

## Contingut

### 1. Els 6 nivells

L'escala MIHIA (Model d'Interacció Humà-IA) estableix 6 graus d'autonomia cedida a la màquina. És el **tercer eix** de l'arquitectura Propòsit-Rol-Nivell, regulat pel mapa d'etapes.

| Nivell | Nom | Qui genera | Iteració | L'alumne... | 4D principal |
|---|---|---|---|---|---|
| **N0** | No delegació | 100% humà | Cap | Fa tota la tasca sense IA | D1 (decidir NO delegar) |
| **N1** | Exploració | Humà pregunta, IA informa | Baixa | Rep informació, context, definicions | D2 + D3 |
| **N2** | Suport / Reacció | Humà crea, IA revisa o reacciona | Mitjana | Crea primer, després rep feedback de la IA | D2 + D3 + D4 |
| **N3** | Cocreació | Ambdós creen iterativament | Alta | Lidera el procés, itera amb la IA, pren decisions | Totes 4D |
| **N4** | Delegació supervisada | IA genera, humà valida | Baixa-Mitjana | Rep un producte complet, l'avalua i el reelabora | D2 + D3 + D4 |
| **N5** | Agència autònoma | IA opera dins paràmetres | Mínima | Dissenya el sistema (prompt, agent, chatbot) | D1 + D4 |

### 2. Perfil de fricció per nivell

Cada nivell genera un perfil de fricció diferent. La fricció no és lineal (no "puja" ni "baixa" amb el nivell): canvia de tipus.

| Nivell | Fricció | Tipus dominant | Risc principal |
|---|---|---|---|
| **N0** | Màxima | Intrínseca pura (l'alumne fa tot) | Cap risc de delegació. Risc de no aprofitar la IA quan seria útil |
| **N1** | Alta | L'alumne transforma informació en raonament propi | Risc baix: pot consumir passivament (mode ICAP Actiu) |
| **N2** | Molt alta | **Zona de fricció productiva màxima**: l'alumne genera, la IA provoca | Risc moderat si no hi ha CFF activa |
| **N3** | Alta amb suport | Recursivitat: iteració fins estabilitzar significat | Risc de desalineació: l'alumne segueix la IA en lloc de liderar |
| **N4** | Baixa | L'alumne avalua, no genera | **Risc alt de rendició cognitiva** si l'alumne no reelabora |
| **N5** | Mínima durant l'ús, màxima durant el disseny | Fricció en el meta-nivell (disseny del sistema) | Competència treballada = pensament computacional, no contingut |

### 3. N0 és una decisió pedagògica, no una mancança

No delegar (N0) és una decisió tan legítima i pedagògicament fonamentada com qualsevol altra. Una activitat sense IA pot ser la millor opció quan:

- L'objectiu és que l'alumne exerciti una habilitat que la IA faria per ell
- La dificultat és desitjable i cal preservar-la íntegrament (Bjork)
- L'activitat requereix fracàs productiu previ a qualsevol suport (Kapur)
- L'avaluació necessita evidència d'habilitat autònoma

### 4. El col·lapse de N4 en rols procesuals

Els **rols procesuals** (Mentor Socràtic, Teachable Agent, Contrincant) **col·lapsen a N4**: la IA genera el diàleg complet i el rol perd l'essència — l'alumne ja no pensa, llegeix un producte.

| Rol procesual | A N2-N3 | A N4 |
|---|---|---|
| Mentor Socràtic | L'alumne respon preguntes, refina el pensament | La IA genera un diàleg socràtic complet → l'alumne el llegeix |
| Teachable Agent | L'alumne ensenya, detecta els propis buits | La IA genera errors i correccions → l'alumne els consumeix |
| Contrincant | L'alumne defensa posicions, argumenta | La IA genera debat complet → l'alumne l'observa |

**Excepció**: N4 amb rols procesuals és acceptable si l'objectiu explícit és aprendre **enginyeria de prompts**, no el contingut del domini.

### 5. Sostre de nivell per etapa educativa

El mapa d'etapes estableix un **sostre de Nivell** per etapa. El rang efectiu d'una combinació (Propòsit, Rol) és la **intersecció** del rang nadiu amb el sostre d'etapa.

| Etapa | Sostre MIHIA | Nivells predominants | Justificació |
|---|---|---|---|
| **I3-I5** (3-5 anys) | N0 | N0 | Manipulació, sensorialitat, joc. No delegació |
| **PRI-CI** (6-8 anys) | N0-N1 | N0 | Introducció conceptual: què és la IA, què no és |
| **PRI-CS** (8-12 anys) | N0-N1 | N0-N1 | Exploració guiada, primers contactes supervisats |
| **ESO 1r cicle** (12-14) | N0-N2 | N0-N2 | Suport i reacció. Fricció alta. Rols procesuals |
| **ESO 2n cicle** (14-16) | N0-N3 | N1-N3 | Cocreació. Iteració amb IA. Tots els rols |
| **Batxillerat** (16-18) | N0-N4 | N1-N4 | Delegació supervisada segons objectiu. Judici avaluatiu |
| **FP Grau Mitjà** | N0-N4 | N1-N4 | Contextual al mòdul professional |
| **FP Grau Superior** | N0-N5 | N2-N5 | Inclou disseny d'agents i sistemes (competència professional) |

**Nota**: el sostre és un màxim, no un objectiu. Un alumne de batxillerat pot (i sovint ha de) treballar a N2.

### 6. Progressió: regles

1. **No saltar més d'un nivell** sense haver consolidat l'anterior.
2. **Progressió no lineal**: un alumne pot treballar a N3 en una matèria i a N1 en una altra — el nivell depèn del domini de contingut, no només de l'edat.
3. **GRR obligatori** (Fisher & Frey): mai proposar ús autònom (N4-N5) sense modelatge previ del docent (N0-N1). L'alumne ha de veure com el docent usa la IA amb criteri.
4. **N5 és excepcional**: implica alfabetització en IA i pensament computacional. L'objectiu no és contingut curricular sinó disseny de sistemes.

### 7. Rang nadiu (Propòsit, Rol) × Nivell

Cada combinació (Propòsit, Rol) té un **rang de Nivells** on funciona amb sentit pedagògic. Fora d'aquest rang, el valor es degrada.

Exemples:

| Combinació | Rang nadiu | Fora de rang |
|---|---|---|
| Critique + Contrincant | N2-N3 | N4: debat generat, no viscut |
| Level-Up + Generador de Casos | N3-N4 | N1: massa limitat per generar exercicis |
| Repte integrador (*Mission*) + Simulador | N2-N3 | N4: missió resolta, no viscuda |
| Anchor + Teachable Agent | N2-N3 | N4: explicació generada, no construïda |
| Right-Sizing + Traductor | N3-N4 | N1: adaptació parcial, poc valor |

El **rang efectiu** en una activitat concreta és: `rang nadiu ∩ sostre d'etapa`.

### 8. Connexió amb AI Fluency (Dakan-Feller)

| Mode AI Fluency | Nivells MIHIA |
|---|---|
| **Automation** (IA executa tasques definides) | N1-N2 |
| **Augmentation** (IA col·labora, potencia) | N2-N4 |
| **Agency** (IA agent autònom dins paràmetres) | N4-N5 |

---

## Connexions

| Document | Relació |
|---|---|
| `M5_arquitectura-proposit-rol-nivell` | El nivell és el tercer eix de l'arquitectura P>R>N |
| `M5_rols-IA-educacio` | Les 3 famílies de rols tenen rangs nadius diferenciats; els procesuals col·lapsen a N4 |
| `M5_proposits-aprenentatge` | El rang efectiu és la intersecció del rang nadiu (Propòsit, Rol) amb el sostre d'etapa |
| `M2_carrega-friccio-cognitiva` | Cada nivell externalitza un tipus de càrrega diferent; el perfil de fricció canvia |
| `M5_disseny-instruccional-amb-IA` | La tria del nivell és el pas 3 de la seqüència de disseny del docent |
| `model-4d-mihia.md` | Les 4D i els nivells formen el marc transversal MIHIA |

---

## Detecció

Activar aquest document quan:

- Cal **decidir el nivell de delegació** per a una activitat concreta
- Cal verificar si el **sostre d'etapa** permet un nivell determinat
- Cal entendre per què un **rol procesual no funciona a N4** (col·lapse)
- Cal justificar per què **N0 és una decisió vàlida**, no una mancança
- Cal calcular el **rang efectiu** d'una combinació (Propòsit, Rol) per a una etapa
- Cal orientar la **progressió d'un alumne** d'un nivell al següent

---

*Versió 1.0 · Esborrany · Jesuïtes Educació Catalunya · 2026*
