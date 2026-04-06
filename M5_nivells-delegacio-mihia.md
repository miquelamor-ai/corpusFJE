---
modul: M5
titol: "Nivells de delegació MIHIA (N0-N5)"
tipus: marc
descripcio: "Els 6 nivells d'autonomia cedida a la IA (No delegació → Agència autònoma), perfil de fricció per nivell, sostre per etapa i col·lapse de rols procesuals a N4"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Definició i principis

L'escala MIHIA (Model d'Interacció Humà-IA) estableix 6 graus d'autonomia cedida a la màquina. És el tercer eix de l'arquitectura Quest-Rol-Nivell: la Quest defineix la intenció, el Rol defineix el comportament de la IA, i el Nivell defineix quanta feina cognitiva es delega.

### Els 6 nivells

| Nivell | Nom | Qui genera | L'alumne... |
|---|---|---|---|
| **N0** | No delegació | 100% humà | Fa tota la tasca sense IA |
| **N1** | Exploració | Humà pregunta, IA informa | Rep informació, context, definicions |
| **N2** | Suport / Reacció | Humà crea, IA revisa o reacciona | Crea primer, després rep feedback |
| **N3** | Cocreació | Ambdós creen iterativament | Lidera el procés, itera, pren decisions |
| **N4** | Delegació supervisada | IA genera, humà valida | Rep producte complet, l'avalua i reelabora |
| **N5** | Agència autònoma | IA opera dins paràmetres | Dissenya el sistema (prompt, agent, chatbot) |

### N0 és una decisió pedagògica

No delegar (N0) és una decisió tan legítima com qualsevol altra. Adequada quan l'objectiu és exercitar una habilitat que la IA faria per l'alumne, preservar una dificultat desitjable (Bjork), garantir fracàs productiu previ (Kapur) o obtenir evidència d'habilitat autònoma.

### Perfil de fricció per nivell

La fricció no és lineal (no "puja" ni "baixa" amb el nivell): canvia de tipus.

| Nivell | Fricció | Tipus dominant | Risc principal |
|---|---|---|---|
| N0 | Màxima | Intrínseca pura | Cap risc de delegació |
| N1 | Alta | Transformar informació en raonament propi | Consum passiu (ICAP Actiu) |
| N2 | Molt alta | **Zona de fricció productiva màxima** | Risc moderat si no hi ha CFF |
| N3 | Alta amb suport | Recursivitat: iteració fins estabilitzar | Desalineació (seguir la IA en lloc de liderar) |
| N4 | Baixa | L'alumne avalua, no genera | **Risc alt de rendició cognitiva** |
| N5 | Mínima/ús, màxima/disseny | Fricció al meta-nivell | Competència = pensament computacional, no contingut |

### El col·lapse de N4 en rols procesuals

Els rols procesuals (Mentor Socràtic, Teachable Agent, Contrincant) col·lapsen a N4: la IA genera el diàleg complet i el rol perd l'essència. L'alumne ja no pensa, llegeix un producte. Excepció: N4 amb rols procesuals és acceptable si l'objectiu és aprendre enginyeria de prompts, no el contingut.

### Sostre de nivell per etapa

El mapa d'etapes estableix un sostre de Nivell per etapa. El rang efectiu d'una combinació (Quest, Rol) és: `rang nadiu ∩ sostre d'etapa`.

| Etapa | Sostre | Nivells predominants |
|---|---|---|
| I3-I5 (3-5 anys) | N0 | N0 |
| PRI-CI (6-8 anys) | N0-N1 | N0 |
| PRI-CS (8-12 anys) | N0-N1 | N0-N1 |
| ESO 1r cicle (12-14) | N0-N2 | N0-N2 |
| ESO 2n cicle (14-16) | N0-N3 | N1-N3 |
| Batxillerat (16-18) | N0-N4 | N1-N4 |
| FP Grau Mitjà | N0-N4 | N1-N4 |
| FP Grau Superior | N0-N5 | N2-N5 |

El sostre és un màxim, no un objectiu. Un alumne de batxillerat pot (i sovint ha de) treballar a N2.

### Progressió

1. No saltar més d'un nivell sense consolidar l'anterior.
2. Progressió no lineal: un alumne pot treballar a N3 en una matèria i a N1 en una altra (depèn del domini de contingut, no només de l'edat).
3. GRR obligatori (Fisher & Frey): mai proposar ús autònom (N4-N5) sense modelatge previ del docent (N0-N1).
4. N5 és excepcional: implica alfabetització en IA i pensament computacional.

### Connexió amb AI Fluency (Dakan-Feller)

| Mode AI Fluency | Nivells MIHIA |
|---|---|
| Automation (executa tasques) | N1-N2 |
| Augmentation (col·labora, potencia) | N2-N4 |
| Agency (agent autònom) | N4-N5 |

## Autors i evidència clau

*   **Dakan, R. & Feller, M.**: Model 4D i AI Fluency. Els nivells MIHIA operacionalitzen la progressió d'autonomia dins les 4D.
*   **Fisher, D. & Frey, N.**: Gradual Release of Responsibility. La connexió GRR ↔ MIHIA estableix que cada fase del GRR correspon a un rang de nivells.
*   **Vygotsky, L. S.**: Zona de Desenvolupament Proper. El nivell MIHIA adequat ha de situar l'alumne dins la ZDP: prou suport per avançar, prou repte per aprendre.
*   **Novokshanova, E. (2025)**: Fricció productiva. El perfil de fricció per nivell es fonamenta en els 3 moviments i les 3 fallades.
*   **Macnamara, B. N. et al. (2024)**: Skill decay. La pregunta "en 10 repeticions, millorarà o perdrà l'habilitat?" justifica la cautela amb N4.
*   **ADR Arquitectura Quest-Rol-Nivell (JE, 2026)**: Decisió de les 3 famílies de rols i el col·lapse a N4.

## Exemples concrets d'aplicació a l'aula

1.  **N0 → N2 (Filosofia, 4t ESO, Mentor Socràtic)**: L'alumne primer debat presencialment amb companys sobre el dilema del tramvia (N0, fricció màxima). Després escriu la seva posició i la IA li fa preguntes socràtiques per aprofundir (N2, Resistència). No salta a N3 o N4 fins que ha demostrat capacitat de raonament autònom.

2.  **N3 (Català, 3r ESO, Crític/Editor)**: Cicle de 3 revisions. L'alumne envia esborrany → IA dona feedback → alumne reescriu → envia versió 2 → IA valida millores i suggereix refinament → versió final. Recursivitat: mínim 3 iteracions. L'alumne lidera; la IA acompanya.

3.  **N4 legítim (Matemàtiques, 1r ESO, Generador de Casos)**: L'alumne demana 10 equacions de primer grau sense solucions. Les resol sol. Després demana solucions per verificar. Aquí N4 és legítim perquè la IA genera material (càrrega extrínseca) i l'alumne fa la feina cognitiva (càrrega germana: resoldre les equacions).

## Errors comuns — què NO fer

1.  **Tractar N0 com a mancança.** "Encara no hem arribat a usar la IA" implica que N0 és un estat provisional. No ho és. N0 pot ser la millor opció pedagògica per a una activitat concreta. El docent ha de saber justificar tant l'ús com el no-ús.

2.  **Saltar directament a N4 sense modelatge.** Si l'alumne no ha vist el docent usar la IA amb criteri (N0-N1), no ha practicat en grup (N2), i no ha iterat amb la IA (N3), delegar a N4 és pedagògicament arriscat. El GRR existeix per una raó.

3.  **Confondre el nivell amb la qualitat de l'activitat.** N4 no és "millor" que N2. N2 amb un Mentor Socràtic pot generar més aprenentatge que N4 amb un Generador de Casos. El nivell adequat depèn de la Quest, el Rol i l'objectiu, no d'una jerarquia de sofisticació.

4.  **Aplicar el sostre d'etapa rígidament.** "A ESO 1r cicle no es pot superar N2" és una guia, no una prohibició. Un alumne excepcionalment madur pot treballar a N3 en un context molt controlat. Però l'excepció no ha de convertir-se en la norma.

5.  **No verificar el rang nadiu del (Quest, Rol).** Un Mentor Socràtic a N4 col·lapsa. Un Generador de Casos a N1 queda molt limitat. Cada combinació (Quest, Rol) té un rang on funciona; fora d'aquest rang, el valor es degrada.

## Matissos i excepcions

*   **N4 per a rols productius és legítim i sovint és l'hàbitat natural.** Un Generador de Casos que genera 20 exercicis perquè l'alumne els resolgui opera a N4 sense cap problema: la fricció resideix en la resolució, no en la interacció amb la IA.

*   **N5 no és per a tothom ni per a tot.** N5 (Agència Autònoma) implica dissenyar sistemes (chatbots, agents, automatitzacions). La competència treballada és pensament computacional i les 4D a meta-nivell, no contingut curricular. A FP Grau Superior pot ser un objectiu formatiu real; a ESO, és excepcional.

*   **La progressió entre nivells depèn del domini, no de l'edat.** Un alumne de batxillerat expert en programació pot treballar a N4 en codi (delegació legítima) i a N1 en filosofia (exploració). El nivell ha de calibrar-se per matèria/domini, no per alumne de manera global.

*   **El sostre d'etapa pot ser més restrictiu per a centres concrets.** Un centre que acaba de començar amb IA pot establir un sostre intern de N2 per a tot l'alumnat durant el primer any, independentment de l'etapa. Això és una decisió institucional legítima (D1 de la cascada).

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M5_arquitectura-quest-rol-nivell**: El nivell és el tercer eix de l'arquitectura Q>R>N. La seqüència de disseny del docent inclou triar el Nivell com a pas 3.
*   **M5_rols-IA-educacio**: Les 3 famílies de rols tenen rangs nadius diferenciats; els procesuals col·lapsen a N4.
*   **M5_quests-missions-aprenentatge**: Cada combinació (Quest, Rol) té un rang de Nivells nadiu. El rang efectiu = rang nadiu ∩ sostre d'etapa.
*   **M2_carrega-friccio-cognitiva**: Cada nivell externalitza un tipus de càrrega diferent; el perfil de fricció canvia.
*   **M5_disseny-instruccional-amb-IA**: La tria del nivell és el pas 3 de la seqüència de disseny. Connexió GRR ↔ MIHIA.
*   **M5_AIA-TPACK-framework**: El nivell MIHIA es relaciona amb el grau d'integració tecnopedagògica.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Quin nivell d'autonomia hauria de tenir l'alumne amb la IA en aquesta activitat?"
*   "Els meus alumnes van directament a demanar que la IA els ho faci tot. Com ho evito?"
*   "Fins a quin punt poden usar la IA els alumnes de 1r ESO? I els de batxillerat?"
*   "Quan és legítim que la IA generi el producte i l'alumne el validi?"
*   "Com graduo la introducció de la IA al llarg del curs?"

**Senyals de l'alumne**
*   L'alumne opera sempre a N4 ("fes-me X"), sense haver passat per N2-N3.
*   L'alumne expressa frustració perquè "la IA no em deixa fer-ho directament" (signe que les CFF funcionen).
*   L'alumne tria conscientment entre nivells segons la tasca (signe de maduresa en D1).

**Senyals de context**
*   El centre introdueix IA per primera vegada i necessita un mapa de progressió.
*   S'estableixen normes d'ús de IA per etapa o per matèria.
*   Es dissenyen assistents institucionals i cal definir els nivells autoritzats.

**Anti-senyals**
*   La consulta és sobre competència digital genèrica, no sobre nivells de delegació a la IA.
*   L'alumne usa la IA per a tasques mecàniques (format, ortografia) on la noció de "nivell" no aplica.

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha de guiar el docent perquè triï el nivell de delegació que maximitza la fricció productiva per a la combinació Quest-Rol concreta, dins del sostre d'etapa.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Calcular el rang efectiu abans de dissenyar l'activitat.**
    *   **Quan aplica:** Quan el docent ja ha triat Quest i Rol i cal decidir el Nivell.
    *   **Fonament:** El rang efectiu és la intersecció del rang nadiu de la combinació (Quest, Rol) amb el sostre d'etapa. Si el Mentor Socràtic (rang nadiu N2-N3) s'aplica a PRI-CS (sostre N0-N1), el rang efectiu és N1 — que no és el nivell nadiu del rol. Això vol dir que el Mentor Socràtic a primària ha de funcionar d'una manera molt més limitada (exploració guiada) que a ESO (interacció plena).
    *   **Exemple complet de raonament:** Un docent de 5è de primària (PRI-CS, sostre N0-N1) vol usar un Mentor Socràtic. L'agent calcularia: rang nadiu del Mentor Socràtic = N2-N3. Sostre d'etapa = N0-N1. Intersecció = N1. A N1, el Mentor Socràtic funciona com a "font de preguntes preparades pel docent" (l'alumne rep preguntes que el docent ha configurat prèviament), no com a interlocutor socràtic obert. L'agent ho explicaria i suggerira alternatives si el docent vol un diàleg més ric: potser esperar a ESO o usar un format de preguntes-guia analògiques.

2.  **Heurística: Detectar el salt de nivells i proposar graduació.**
    *   **Quan aplica:** Quan l'activitat proposa un nivell que l'alumne no ha practicat.
    *   **Fonament:** El GRR (Fisher & Frey) estableix que l'autonomia s'allibera gradualment. Si l'alumne no ha vist el docent usar la IA amb criteri (Jo faig, N0-N1), saltar a N4 (Tu fas) és pedagògicament arriscat. L'alumne no té un model de referència per exercir les 4D i tendirà cap a la rendició cognitiva.
    *   **Exemple complet de raonament:** Un docent vol que els alumnes de 2n ESO generin resums complets amb IA (N4). L'agent preguntaria: "Els alumnes han vist com tu uses la IA per fer un resum? Han practicat en grup amb la IA revisant els seus resums (N2)? Han iterat amb la IA per millorar un resum (N3)?" Si la resposta és no a tot, suggerira una seqüència gradual: primer el docent demostra com usar la IA com a Crític d'un resum propi (N1), després els alumnes ho fan en parelles (N2), després individualment amb iteració (N3), i només al final, si dominen el procés, a N4.

3.  **Heurística: Justificar N4 amb la distinció càrrega extrínseca vs. germana.**
    *   **Quan aplica:** Quan el docent proposa una activitat a N4 i cal verificar si és legítim.
    *   **Fonament:** N4 és legítim quan la IA genera material auxiliar (càrrega extrínseca) i l'alumne fa la feina cognitiva (càrrega germana). N4 és problemàtic quan la IA genera l'objectiu d'aprenentatge mateix. La distinció és precisa: si la IA genera exercicis i l'alumne els resol = N4 legítim (Generador de Casos). Si la IA genera l'assaig i l'alumne el revisa = N4 problemàtic (la redacció era la càrrega germana).
    *   **Exemple complet de raonament:** Un docent proposa que la IA generi una entrevista completa amb un personatge històric (N4, Simulador). L'agent preguntaria: "Quin és l'objectiu d'aprenentatge?" Si és "que l'alumne practiqui fer preguntes d'entrevista", N4 elimina exactament la pràctica que l'alumne necessita (càrrega germana). Suggerira N2: l'alumne prepara les preguntes, la IA respon en personatge, l'alumne detecta anacronismes. Si l'objectiu és "que l'alumne analitzi un text sobre el període", N4 pot ser legítim: la IA genera el text i l'alumne l'analitza (la generació és extrínseca, l'anàlisi és germana).

4.  **Heurística: Establir el sostre institucional com a acte de D1 de la cascada.**
    *   **Quan aplica:** Quan un centre comença a integrar la IA i necessita un marc de nivells.
    *   **Fonament:** La cascada institució → docent → alumne estableix que la institució exerceix D1 decidint quins nivells s'autoritzen per etapa. Això no és restricció arbitrària sinó exercici de la Delegació institucional: la institució decideix quins espais segurs crea perquè docents i alumnes hi operin. El sostre pot ser més restrictiu que el marc general si el centre ho justifica.
    *   **Exemple complet de raonament:** Un centre acaba de començar amb IA i vol un marc clar. L'agent suggerira: primer any, sostre N2 per a tot l'alumnat (suport i reacció). Segon any, sostre N3 per a ESO-2n cicle i batxillerat (cocreació). Tercer any, sostre N4 per a batxillerat i FP. Cada ampliació va precedida de formació docent (el docent ha de dominar el nivell abans que l'alumne hi accedeixi). Això és GRR aplicat a escala institucional.

5.  **Heurística: Usar la pregunta Macnamara per validar el nivell.**
    *   **Quan aplica:** Com a verificació final de qualsevol activitat amb IA.
    *   **Fonament:** Macnamara et al. (2024) demostren que les habilitats no practicades es degraden. La pregunta "si l'alumne fa aquesta activitat 10 vegades, millorarà la seva habilitat o la perdrà?" és la prova àcida del nivell. Si la resposta és "la perdrà", el nivell és massa alt o la IA fa massa feina.
    *   **Exemple complet de raonament:** Un docent proposa que els alumnes usin la IA per traduir textos (N4, Traductor). L'agent faria la pregunta Macnamara: "Si l'alumne fa 10 traduccions amb la IA, millorarà com a traductor o deixarà de traduir?" Probablement la segona. Suggerira N2: l'alumne tradueix primer, la IA revisa i assenyala errors, l'alumne corregeix. Ara l'alumne practica traducció amb suport i millora en cada iteració.

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Triar el nivell segons el que necessita aprendre, no segons el que vol entregar.**
    *   **Quan aplica:** Quan l'alumne té llibertat per decidir com usar la IA.
    *   **Fonament:** La distinció rendiment vs. aprenentatge (Soderstrom & Bjork) implica que el nivell que maximitza la qualitat del producte no és el que maximitza l'aprenentatge. L'alumne que tria N2 (escriu primer, la IA revisa) aprèn més que l'alumne que tria N4 (la IA escriu, l'alumne valida), encara que el producte de N4 sigui millor.
    *   **Exemple complet de raonament:** Un alumne ha d'escriure un text argumentatiu i pot triar el nivell. L'agent li preguntaria: "Vols un text millor o vols ser millor escrivint?" Si vol ser millor, N2: escriu primer, la IA assenyala febleses, reescriu. Si vol un text millor per a una presentació on el contingut ja el domina, N4 pot ser legítim (delegació de producció, no d'aprenentatge). La clau és la consciència de la tria.

2.  **Heurística: Reconèixer quan el nivell és massa alt per al que necessita.**
    *   **Quan aplica:** Quan l'alumne nota que la IA li "fa la feina".
    *   **Fonament:** El col·lapse (Novokshanova) és el senyal que el nivell és massa alt: l'alumne ha sortit del bucle cognitiu. Si l'alumne nota que ha copiat l'output sense pensar-hi, la recomanació és baixar un nivell: de N4 a N3 (iterar) o de N3 a N2 (crear primer).
    *   **Exemple complet de raonament:** Un alumne ha demanat a la IA que generi un resum d'un tema (N4). Quan se n'adona que no ha entès el contingut, l'agent li suggerira: "Tanca el resum generat. Escriu tu un resum de 5 línies del que recordes (N0). Després envia'l a la IA: 'Què em falta? Quins errors tinc?' (N2). Ara estàs treballant a un nivell on realment aprens."

3.  **Heurística: Fer-se la pregunta Macnamara.**
    *   **Quan aplica:** Com a verificació personal abans i després d'usar la IA.
    *   **Fonament:** "Si faig això 10 vegades, milloraré la meva habilitat o la perdré?" és una pregunta metacognitiva que l'alumne pot aprendre a fer-se autònomament. Si la resposta és "la perdré", cal canviar el nivell o el rol.
    *   **Exemple complet de raonament:** Un alumne de FP utilitza la IA per redactar correus professionals cada dia (N4). Després d'un mes, l'agent li preguntaria: "Podries escriure aquest correu tu sol, sense la IA?" Si la resposta és no, l'alumne ha substituït la competència per la delegació. Suggerira alternar: dies amb IA (N2, la IA revisa) i dies sense IA (N0, l'alumne practica sol). Així manté l'habilitat i la potencia.

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | ADR Arquitectura Quest-Rol-Nivell (JE, 2026) | file://docs/decisions/arquitectura-quest-rol-nivell.md |
| 2 | Exemples d'Aplicació dels 7 Rols (JE, 2026) | file://public/exemples-rols-mihia.md |
| 3 | docs/marcs-teorics/friccio-cognitiva-extens.md | file://docs/marcs-teorics/friccio-cognitiva-extens.md |
| 4 | Macnamara, B. N. et al. (2024). Skill Decay and AI | https://doi.org/10.1186/s41235-024-00579-x |
| 5 | Fisher, D. & Frey, N. Gradual Release of Responsibility | file://upload/Fisher_Frey_GRR.pdf |
| 6 | Novokshanova, E. (2025). Productive Friction | file://upload/Novokshanova_2025_ProductiveFriction.pdf |

*6 documents font · secció generada manualment*
