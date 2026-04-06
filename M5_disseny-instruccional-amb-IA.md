---
modul: M5
titol: "Disseny instruccional amb IA: criteris, auditoria i plantilla"
tipus: estrategia
descripcio: "Seqüència de disseny del docent (4 passos Q>R>N + verificació), 7 criteris de disseny, 8 preguntes d'auditoria, plantilla operativa i connexió GRR-MIHIA"
review_status: esborrany
generat_at: 2026-04-06
---

# 1. CONTINGUT ESPECÍFIC

## Descripció i fonament

El disseny d'activitats amb IA segueix quatre decisions en cascada (arquitectura Q>R>N) i una verificació final amb el marc cognitiu:

| Pas | Pregunta del docent | Decisió |
|---|---|---|
| 1 | "Què vull que passi cognitivament?" | Triar una Quest |
| 2 | "Com ha d'actuar la IA?" | Triar un Rol compatible (matriu d'afinitats) |
| 3 | "Quanta autonomia?" | Triar un Nivell (rang nadiu × sostre d'etapa) |
| 4 | "Hi ha fricció productiva?" | Verificar amb els 7 criteris |

Aquesta seqüència integra el backward design (Wiggins & McTighe), el GRR (Fisher & Frey), el marc de fricció productiva (Novokshanova) i la distinció rendiment vs. aprenentatge (Soderstrom & Bjork; Chase & Galvin). No és un formulari burocràtic sinó una eina de pensament que el docent interioritza.

### GRR aplicat a la IA

| Fase GRR | Nom | Amb IA | MIHIA |
|---|---|---|---|
| 1 | Jo faig | El docent modela com usar la IA correctament | N0-N1 |
| 2 | Nosaltres fem | Exercici col·lectiu amb IA, el docent guia | N1-N2 |
| 3 | Vosaltres feu | Grups usen IA amb pautes clares | N2-N3 |
| 4 | Tu fas | L'alumne usa IA autònomament amb criteri | N3-N4 |

**Regla d'or**: mai proposar ús autònom (Fase 4) sense modelatge previ (Fase 1). El GRR gradua no només l'autonomia sinó la fricció productiva: a les fases inicials, el docent modela com gestionar la fricció.

### Bastida progressiva de prompts

| Nivell | Bastida | L'alumne... |
|---|---|---|
| Principiant | Prompt complet donat pel docent, omple buits | Executa dins estructura tancada |
| Intermedi | Estructura donada, redacta el contingut | Decideix què preguntar |
| Avançat | Crea el seu propi prompt amb criteris de qualitat | Formula amb autonomia |
| Expert | Avalua, compara i optimitza prompts | Judici meta sobre la interacció |

### Disseny = avaluació (Chase & Galvin, 2026)

Una activitat en què la IA pot fer el treball cognitiu nuclear no és un problema ètic, és un problema de disseny: ja no mesura el que pretén mesurar. Les respostes discursives (normes "podeu/no podeu usar IA") són insuficients; cal redisseny estructural. La decisió sobre quins indicadors observables han de ser íntegrament humans i quins poden ser suportats per IA es pren **indicador per indicador**, no activitat per activitat.

### Set criteris de disseny

| # | Criteri | Pregunta de verificació |
|---|---|---|
| 1 | Objectiu cognitiu explícit | Quin esquema ha de construir l'alumne? |
| 2 | IA per a càrrega extrínseca, no germana | S'elimina esforç que construiria aprenentatge? |
| 3 | Moment de generació autònoma | L'alumne fa/prova/produeix ABANS que la IA l'assisteixi? |
| 4 | CFF activa | Quina funció de forçat cognitiu té la interacció? |
| 5 | Fricció productiva induïda | On i com es produirà Descoberta/Recursivitat/Resistència? |
| 6 | Mode ICAP ≥ Constructive | L'alumne genera o dialoga, no rep passivament? |
| 7 | Avaluació sense IA possible | Almenys una dimensió es pot avaluar sense assistent? |

### Vuit preguntes d'auditoria

Per a activitats existents que ja incorporen IA:

1. Quina càrrega s'externalitza? (Extrínseca → bo. Intrínseca → risc.)
2. L'alumne ha generat alguna cosa abans? (No → risc de paradoxa.)
3. Hi ha CFF identificable? (No → risc de rendició cognitiva.)
4. Mode ICAP? (Passive/Active → reformular.)
5. En 10 repeticions, millorarà o perdrà l'habilitat? (Macnamara)
6. Ho pot fer sense IA? (No → risc de dependència.)
7. L'avaluació discrimina rendiment/aprenentatge? (No → cega a la paradoxa.)
8. Fiabilitat de l'assistent auditada? (Si < 70% → crossover point.)

### Plantilla de disseny

```
0. TIPUS I DURADA
   Granularitat: Exercici / Activitat / Tasca / Projecte
   Durada / Nombre de sessions

1. CONTEXT
   Etapa / Matèria / Tema / Objectiu d'aprenentatge

2. DISSENY Q>R>N
   Quest triada i justificació
   Rol assignat (verificat a la matriu d'afinitats)
   Nivell MIHIA (rang nadiu × sostre d'etapa)
   Família del rol (procesual / mixt / productiu)

3. PREPARACIÓ (Jo faig)
   Modelatge del docent / CFF establerta / Activació de previs

4. INTERACCIÓ AMB IA (Nosaltres fem → Tu fas)
   Prompt (amb bastida segons nivell)
   Moviment de fricció esperat / Mode ICAP esperat

5. POST-IA (Fricció productiva)
   Què fa l'alumne amb el resultat
   On resideix la propietat cognitiva (McCrea)
   Càrrega externalitzada = extrínseca?

6. EVIDÈNCIA D'APRENENTATGE
   Indicadors observables (per a cada: amb IA / sense IA / indiferent)
   Pregunta Macnamara
   Reflexió metacognitiva
```

### Granularitat didàctica

| Granularitat | Durada | Integració IA |
|---|---|---|
| Exercici | 5-20 min | Un sol rol, un sol nivell |
| Activitat | 1 sessió | 1-2 rols, un nivell predominant |
| Tasca | 2-5 sessions | Diversos rols, progressió de nivells |
| Projecte | 1-4+ setmanes | Mapa complet de rols i nivells per fase |

Una tasca o projecte pot incloure fases amb IA i fases sense IA (N0).

## Quan i per a qui

*   **Per al docent que dissenya activitats noves amb IA**: la seqüència de 4 passos i la plantilla.
*   **Per al docent que vol auditar activitats existents**: les 8 preguntes d'auditoria.
*   **Per al coordinador pedagògic que forma docents**: els 7 criteris com a checklist.
*   **Per al dissenyador d'assistents institucionals**: els criteris A-H (documentats a M2_carrega-friccio-cognitiva).

## Recursos

*   Plantilla de disseny (secció anterior)
*   Matriu d'afinitats Quest × Rol (M5_quests-missions-aprenentatge)
*   Taula de sostres per etapa (M5_nivells-delegacio-mihia)
*   7 criteris + 8 auditoria (M2_carrega-friccio-cognitiva)
*   21 exemples (exemples-rols-mihia.md)

## Com implementar

**Nivell bàsic** (docent que comença): fer-se les 4 preguntes en ordre. No cal memoritzar les 10 Quests; cal saber fer-se les preguntes. La plantilla pot omplir-se mentalment, no necessàriament per escrit.

**Nivell intermedi** (docent amb experiència): usar la plantilla escrita per dissenyar unitats didàctiques amb IA. Passar les 8 preguntes d'auditoria a activitats existents. Seqüenciar rols dins de tasques complexes.

**Nivell avançat** (coordinador/formador): usar els 7 criteris per avaluar pràctiques de tot un departament. Dissenyar la progressió de nivells al llarg del curs. Configurar assistents institucionals amb els criteris A-H.

## Adaptacions

*   **Per etapa**: a primària, la plantilla es simplifica (no cal formalitzar el pas 2 i 3; el docent decideix implícitament). A FP, el camp "Context" inclou competència professional i context laboral real.
*   **Per centre**: la plantilla pot tenir camps addicionals segons el projecte educatiu del centre (competències transversals pròpies, connexió amb PPI, etc.).
*   **Per mòdul**: a FP, cada mòdul professional pot tenir la seva matriu d'afinitats Quest × Rol ajustada al perfil de sortida.

## Indicadors d'èxit

*   El docent pot justificar per què ha triat una Quest, un Rol i un Nivell concrets.
*   L'activitat passa les 8 preguntes d'auditoria sense alertes.
*   L'alumne mostra almenys un dels 3 moviments de fricció productiva durant la interacció.
*   L'avaluació discrimina entre rendiment (amb IA) i aprenentatge (sense IA).
*   El mode ICAP observat és Constructive o Interactive.

## Errors comuns

1.  **Omplir la plantilla com a tràmit burocràtic.** La plantilla és una eina de pensament, no un formulari. Si el docent l'omple sense fer-se les preguntes de veritat, no serveix. Millor fer-se les 4 preguntes mentalment que omplir la plantilla mecànicament.

2.  **Saltar el pas 4 (verificació de fricció).** Triar Q, R i N no garanteix aprenentatge. La verificació amb els 7 criteris és la comprovació que l'activitat realment genera aprenentatge, no només rendiment.

3.  **No preveure la fase post-IA.** Què fa l'alumne amb el resultat de la IA és tant o més important que la interacció mateixa. Si l'alumne no reelabora, no compara, no jutja, no reescriu, la interacció ha estat passiva.

4.  **Dissenyar l'activitat i l'avaluació com a actes separats.** Chase i Galvin (2026) demostren que són el mateix acte. Cada indicador observable ha de decidir si la IA hi pot ser o no. Això no es pot fer si es dissenya primer l'activitat i després l'avaluació.

5.  **No adaptar la bastida de prompts al nivell de l'alumnat.** Un alumne principiant amb un prompt obert genera interaccions de baixa qualitat. Un alumne expert amb un prompt tancat se sent limitat. La bastida progressiva existeix per calibrar.

# 2. CONNEXIONS AMB ALTRES DOCUMENTS DEL CORPUS

*   **M5_arquitectura-quest-rol-nivell**: La seqüència de 4 passos opera dins l'arquitectura Q>R>N. Pas 1 = Quest, Pas 2 = Rol, Pas 3 = Nivell.
*   **M5_quests-missions-aprenentatge**: Pas 1: triar Quest. Matriu d'afinitats per al pas 2.
*   **M5_rols-IA-educacio**: Pas 2: triar Rol. Verificar família (procesual/mixt/productiu).
*   **M5_nivells-delegacio-mihia**: Pas 3: triar Nivell. Sostre d'etapa. GRR ↔ MIHIA.
*   **M2_carrega-friccio-cognitiva**: Pas 4: 7 criteris + 8 auditoria. Criteris d'assistents A-H.
*   **M2_models-disseny-instruccional**: Granularitat didàctica, GRR, fases FJE, scaffolding.
*   **M5_prompt-engineering-educatiu**: Bastida progressiva de prompts.

# 3. DETECCIÓ (Variables de Context)

**Senyals del docent**
*   "Vull dissenyar una activitat que incorpora IA. Per on començo?"
*   "Com sé si la meva activitat amb IA realment funciona?"
*   "Necessito una plantilla o un checklist per verificar les meves activitats."
*   "He fet una activitat amb IA i els alumnes no han après res. Què ha fallat?"
*   "Com graduo els prompts per als meus alumnes?"

**Senyals de l'alumne**
*   L'alumne no entén per què ha de "perdre el temps" escrivint primer si la IA pot fer-ho directament — necessita entendre la lògica del pas 3 (generació autònoma prèvia) i la CFF.

**Senyals de context**
*   S'està planificant una unitat didàctica o projecte amb integració de IA.
*   Es fa formació docent sobre disseny d'activitats amb IA.
*   Es revisen activitats existents per millorar-les.
*   S'elabora el pla d'ús de IA d'un departament o centre.

**Anti-senyals**
*   El docent ja domina el sistema i necessita informació sobre un eix concret (Q, R o N), no sobre la plantilla global.
*   La consulta és teòrica, no operativa (activar M2_carrega-friccio-cognitiva en lloc d'aquest document).

# 4. HEURÍSTIQUES I RAONAMENT PER A L'AGENT

**Principi general:** L'agent ha de guiar el docent pas a pas per la seqüència de disseny, verificar la coherència de les decisions i alertar si algun criteri no es compleix.

### Heurístiques per a l'Agent DOCENT

1.  **Heurística: Guiar pas a pas, no presentar tot de cop.**
    *   **Quan aplica:** Quan un docent comença a dissenyar una activitat amb IA.
    *   **Fonament:** La seqüència de 4 passos és un procés guiat, no una llista de requisits. Si el docent rep els 7 criteris, les 8 preguntes d'auditoria, la plantilla de disseny i les matrius de cop, la càrrega cognitiva extrínseca el paralitza. Ironia: el marc de fricció s'ha d'aplicar a la formació docent mateixa.
    *   **Exemple complet de raonament:** Un docent diu: "Vull fer una activitat de ciències amb IA." L'agent començaria pel pas 1: "Quin és l'objectiu d'aprenentatge?" El docent respon: "Que entenguin el cicle de l'aigua." L'agent: "Vols que l'entenguin millor (Clarity), que el comparin amb un altre cicle (Compare) o que l'expliquin a algú (Reverse)?" El docent tria Clarity. Pas 2: "Quins rols serveixen Clarity? Mentor Socràtic (★★) o Teachable Agent (★★). Quin prefereixes?" I així successivament. Cada pas depèn de l'anterior; l'agent no avança fins que el docent ha decidit.

2.  **Heurística: Usar les 8 preguntes d'auditoria com a diagnòstic ràpid.**
    *   **Quan aplica:** Quan un docent descriu una activitat existent que "no funciona" amb IA.
    *   **Fonament:** Les 8 preguntes són un checklist de diagnòstic que identifica on falla l'activitat. Cada pregunta apunta a un mecanisme concret de la paradoxa del rendiment: càrrega externalitzada incorrecta, absència de CFF, mode ICAP massa baix, etc. El diagnòstic permet proposar reformulacions específiques, no genèriques.
    *   **Exemple complet de raonament:** Un docent diu: "Els alumnes usen la IA per fer resums i les notes han pujat, però als exàmens no milloren." L'agent passaria les 8 preguntes: P1 (càrrega?) → La IA fa el resum = càrrega germana externalitzada (risc). P2 (generació prèvia?) → No, l'alumne va directament a la IA. P3 (CFF?) → No n'hi ha. P4 (ICAP?) → Passiu (rep el resum). P5 (Macnamara?) → En 10 repeticions, l'alumne perdrà la capacitat de resumir. Diagnòstic clar: paradoxa del rendiment en estat pur. Reformulació: l'alumne fa primer el seu resum (P2), la IA l'avalua sense reescriure (P1, ara extrínseca), l'alumne ha de trobar un error al feedback (P3, CFF), i reescriu (P4, ara Constructive).

3.  **Heurística: Insistir en la fase post-IA com a moment crític d'aprenentatge.**
    *   **Quan aplica:** Quan l'activitat acaba quan l'alumne rep l'output de la IA.
    *   **Fonament:** El moment crític no és la interacció amb la IA sinó el que l'alumne fa DESPRÉS. La propietat cognitiva (McCrea) resideix en l'acte de reelaborar, jutjar, integrar o rebutjar l'output. Si l'activitat acaba quan la IA respon, l'alumne no ha fet el treball cognitiu que genera aprenentatge.
    *   **Exemple complet de raonament:** Un docent dissenya una activitat on l'alumne demana feedback a la IA sobre un text argumentatiu. L'agent verificaria: "Què fa l'alumne amb el feedback? Si simplement l'aplica sense pensar, no hi ha aprenentatge de criteri. Afegim un pas: l'alumne ha de decidir quins suggeriments accepta i quins rebutja, i justificar cada decisió per escrit. Ara la fase post-IA és un exercici de judici avaluatiu (Tai et al., 2018) i de Resistència (Novokshanova)."

4.  **Heurística: Adaptar la bastida de prompts a la progressió de l'alumnat.**
    *   **Quan aplica:** Quan el docent prepara els prompts que usarà l'alumnat.
    *   **Fonament:** Un alumne principiant amb un prompt obert genera interaccions de baixa qualitat (no sap què preguntar, la IA respon genèricament, l'alumne copia). Un alumne expert amb un prompt tancat se sent limitat. La bastida progressiva (principiant → intermedi → avançat → expert) tradueix el GRR al nivell operatiu de la interacció amb l'assistent.
    *   **Exemple complet de raonament:** Un docent prepara una activitat amb Crític/Editor per a 3r ESO (principiants amb IA). L'agent suggerira una bastida de prompt: "Dóna'ls el prompt complet: 'Ets un professor de català. Llegeix el meu text argumentatiu i assenyala 3 punts febles (estructura, arguments, connectors). No reescriguis res, només explica.' L'alumne omple el buit (el seu text) però la instrucció ja està formulada. A mesura que guanyin experiència, podràs donar-los només l'estructura: 'Demana a la IA que actuï com a [rol], que revisi [aspecte] i que [restricció]'. I més endavant, que formulin el prompt ells mateixos."

5.  **Heurística: Aplicar el pas 4 com a test àcid final.**
    *   **Quan aplica:** Després de completar els passos 1-3.
    *   **Fonament:** Triar Q, R i N no garanteix aprenentatge. El pas 4 aplica els 7 criteris del marc cognitiu com a verificació final. Si algun criteri falla, cal reformular abans de dur l'activitat a l'aula. Especialment: si no hi ha CFF (criteri 4) o si el mode ICAP és Passive/Active (criteri 6), l'activitat té un risc alt de paradoxa del rendiment.
    *   **Exemple complet de raonament:** Un docent ha triat Quest Compare + Generador de Casos (N3) per a economia. L'agent verifica: C1 (objectiu cognitiu?) → Sí, comparar dues polítiques fiscals. C2 (càrrega?) → La IA genera els casos (extrínseca), l'alumne compara (germana). ✓ C3 (generació prèvia?) → L'alumne ha d'escriure la seva hipòtesi primer. ✓ C4 (CFF?) → Pre-compromís. ✓ C5 (fricció?) → Descoberta (veure diferències entre polítiques). ✓ C6 (ICAP?) → Constructive (l'alumne genera la comparació). ✓ C7 (avaluació sense IA?) → Examen comparatiu sense accés a la IA. ✓ L'activitat passa els 7 criteris.

### Heurístiques per a l'Agent ALUMNE

1.  **Heurística: Entendre per què "primer escriu tu" no és una restricció arbitrària.**
    *   **Quan aplica:** Quan l'alumne pregunta per què ha d'escriure primer si la IA pot fer-ho directament.
    *   **Fonament:** L'efecte generació (Slamecka & Graf) demostra que generar una resposta pròpia millora la retenció. El pre-compromís (CFF) activa coneixements previs i crea un punt de referència per comparar amb l'output de la IA. Sense generació prèvia, l'alumne no sap què sabia ni què no sabia, i la Descoberta no es produeix.
    *   **Exemple complet de raonament:** Un alumne diu: "Per què he d'escriure un resum si la IA el fa millor?" L'agent li explica: "Escriure primer no serveix per generar un bon resum — serveix per activar el teu cervell. Quan escrius el que recordes, veus què saps i què no. Després, quan la IA t'assenyala el que et falta, tens una sorpresa útil (Descoberta): 'Ah, no havia pensat en això!' Si la IA et dona el resum directament, no tens aquesta sorpresa — tot et sembla obvi perquè ho llegeixes fet. Però no l'has après."

2.  **Heurística: Fer la verificació personal post-IA.**
    *   **Quan aplica:** Quan l'alumne ha acabat d'interactuar amb la IA.
    *   **Fonament:** La fase post-IA és el moment on resideix la propietat cognitiva. L'alumne pot fer-se tres preguntes: (1) He pensat jo o ha pensat la IA? (2) Podria fer això sol la pròxima vegada? (3) Què he après que no sabia abans?
    *   **Exemple complet de raonament:** Un alumne ha iterat amb un Mentor Socràtic sobre un dilema ètic. L'agent li suggerira les 3 preguntes: "Has pensat tu o la IA? → Jo he respost les preguntes, la IA m'ha qüestionat. He pensat jo. ✓ Podria fer-ho sol? → Podria identificar febleses en el meu argument sense la IA? Potser no totes, però algunes. Ho practicaré. Què he après? → Que el meu argument sobre X era feble perquè no considerava Y." Ara l'alumne ha fet metacognició explícita i sap què ha après de la interacció.

3.  **Heurística: Demanar la bastida de prompt adequada al seu nivell.**
    *   **Quan aplica:** Quan l'alumne no sap com formular una interacció productiva amb la IA.
    *   **Fonament:** Un alumne que no sap què preguntar obtindrà respostes genèriques i tendirà a copiar-les. Demanar al docent (o a l'agent) un prompt estructurat no és debilitat; és bastida pedagògica legítima que es retirarà quan l'alumne pugui formular-lo sol.
    *   **Exemple complet de raonament:** Un alumne vol usar la IA com a Crític per millorar el seu text però no sap com. L'agent li proporcionaria el prompt bastida: "Copia això i enganxa el teu text al final: 'Ets un professor exigent. Llegeix el meu text i digues-me 3 coses que podria millorar. No reescriguis res, només explica.' Quan tinguis més experiència, podràs escriure el teu propi prompt. Per ara, això t'assegurarà una interacció productiva."

---

## 5. FONTS DEL CORPUS

| # | Títol | URL |
|---|-------|-----|
| 1 | ADR Arquitectura Quest-Rol-Nivell (JE, 2026) | file://docs/decisions/arquitectura-quest-rol-nivell.md |
| 2 | Chase, A.-M. & Galvin, K. (2026). Thinking to Learn | file://upload/Chase_Galvin_2026_ThinkingToLearn.pdf |
| 3 | Fisher, D. & Frey, N. Gradual Release of Responsibility | file://upload/Fisher_Frey_GRR.pdf |
| 4 | Novokshanova, E. (2025). Productive Friction | file://upload/Novokshanova_2025_ProductiveFriction.pdf |
| 5 | McCrea, P. (2025). Cognitive Ownership | file://upload/McCrea_2025_CognitiveOwnership.pdf |
| 6 | docs/marcs-teorics/friccio-cognitiva-extens.md | file://docs/marcs-teorics/friccio-cognitiva-extens.md |
| 7 | Khan, S. et al. (2025). Teaching with AI | file://upload/Khan_Fisher_Frey_2025_TeachingWithAI.pdf |

*7 documents font · secció generada manualment*
