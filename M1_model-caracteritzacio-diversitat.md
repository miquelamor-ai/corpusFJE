---
titol: "Model de caracterització de la diversitat"
modul: M1
tipus: marc
subtipus: arquitectural
paraules_clau: [diversitat, caracteristica, perfil, neurodiversitat, inclusio, DUA, caracteritzacio, constitutiva, contextual]
descripcio: "Marc conceptual del sistema de tres nivells (característica, perfil, grup) que governa com el sistema RAG representa i processa la diversitat de l'alumnat. Inclou la distinció constitutiva/contextual i les implicacions pedagògiques, ètiques i tècniques."
review_status: draft
generat_at: 2026-03-18T00:00:00
---

# 1. Definició i principis

La diversitat a l'aula no és una excepció ni un problema a resoldre — és la norma. Qualsevol grup d'alumnes conté una varietat de maneres d'aprendre, de comunicar-se, de processar la informació i de relacionar-se amb el coneixement. El repte pedagògic no és reduir aquesta diversitat a categories fixes i estanques, sinó disposar d'un sistema de representació prou ric i prou flexible per donar-hi resposta de manera precisa, eficient i respectuosa.

Aquest model de tres nivells permet representar i processar la diversitat de l'alumnat. No és una classificació diagnòstica ni una eina d'etiquetatge — és un sistema funcional que permet recuperar el coneixement pedagògic adequat per a cada situació concreta, respectant la complexitat real de les persones.

El model parteix de tres premisses. Primera: cap alumne encaixa en una sola categoria — la majoria de situacions impliquen combinacions de factors. Segona: no totes les circumstàncies que condicionen l'aprenentatge tenen el mateix caràcter: algunes formen part de la identitat de la persona de manera estable (constitutives), d'altres són transitòries (contextuals). Confondre les dues categories és un error pedagògic i ètic. Tercera: les barreres a l'aprenentatge resideixen en el context, no en la persona — principi central al DUA que orienta tota la terminologia del model.

## El model de tres nivells

**Nivell 1 — La característica**: Unitat mínima. Una sola dimensió de la diversitat d'un alumne. No és la persona — és un aspecte de la persona. Cada característica té la seva pròpia lògica d'adaptació. Al corpus, cada característica té el seu propi document de `tipus: caracteristica`.

**Nivell 2 — El perfil**: La persona real amb totes les seves característiques combinades. No és un document del corpus — és una entitat de la base de dades (StudentMemory) construïda pel docent. Un perfil pot ser simple (una característica) o complex (tres o quatre que interactuen).

**Nivell 3 — El grup**: Conjunt de perfils d'una mateixa aula. Representat com a `ClassMemory` a la BD. Útil quan el docent vol generar materials per a tota la classe alhora.

## La distinció constitutiva / contextual

Una característica és **constitutiva** quan forma part de la identitat de la persona de manera estable: no desapareix, i la persona pot reivindicar-la com a part del seu ser. L'autisme és constitutiu. La dislèxia és constitutiva. Les altes capacitats són constitutives. Tècnicament, una característica constitutiva s'injecta sempre com a context al sistema sense qüestionar si segueix vigent.

Una característica és **contextual** quan respon a una situació transitòria que pot canviar. La condició de nouvingut és contextual. La vulnerabilitat socioeducativa és contextual. Molts trastorns emocionals associats a contextos de crisi es resolen amb el temps. Tractar una característica contextual com si fos constitutiva és un error que pot estigmatitzar. Tècnicament, les característiques contextuals activen una verificació periòdica.

## Implicació per al RAG

Quan el sistema rep un perfil d'alumne: (1) identifica quines característiques el componen; (2) recupera els documents `tipus: caracteristica` corresponents; (3) els injecta al prompt del sistema d'adaptació. Si la característica és constitutiva, s'injecta sempre. Si és contextual, el sistema pot verificar si segueix vigent.

## Exemples concrets

**Exemple 1 — Perfil complex constitutiu:** Una alumna de 2n ESO amb TEA, dislèxia i altes capacitats. El sistema recupera tres documents de característica. Per a un text científic, la dislèxia genera les barreres més visibles (format, frases curtes). Per a un debat oral, el TEA genera les barreres principals (ambigüitat, gestió de torns). Per a activitats d'enriquiment, les altes capacitats marquen el camí. Cal ponderar en funció del context de l'adaptació concreta, no en abstracte.

**Exemple 2 — Tensió entre característiques:** Un alumne nouvingut amb TEA. El document de nouvingut recomana analogies culturalment properes. El document de TEA avisa que les analogies i el pensament metafòric generen confusió en alumnes autistes, que processen millor la informació literal. Cal fer explícita la tensió a l'informe d'auditoria i proposar la solució adoptada perquè el docent pugui valorar-la.

## Errors comuns

**Confondre la característica amb la persona.** El document `alumnat-TEA.md` descriu la característica TEA, no en Pau. En Pau pot tenir TEA i moltes altres coses. Cal no tractar la característica com una descripció completa de la persona.

**Aplicar criteris d'adaptació mecànicament.** "Frases curtes per a alumnat amb dislèxia" és un principi, no una regla absoluta. Cal combinar-lo amb el principi de preservar el rigor conceptual.

**Tractar les característiques contextuals com si fossin constitutives.** Un nouvingut que porta dos anys i ha assolit B1 no hauria de rebre els mateixos suports que quan va arribar. Les característiques contextuals s'han de revisar periòdicament.

**Ignorar les fortaleses.** Cada document de característica inclou fortaleses. Cal incorporar-les a les adaptacions, no només reduir barreres.

**Patologitzar la diversitat.** El model no classifica alumnes com a "normals" i "especials". Tots els alumnes tenen un perfil.

## Matissos i excepcions

El model és una simplificació funcional. Alguns trastorns emocionals greus poden cronificar-se i adquirir un caràcter quasi-constitutiu. Una discapacitat adquirida és constitutiva tècnicament però no ho era des del principi. El model tampoc captura la variabilitat interna de cada característica: l'espectre del TEA és molt ampli. Els documents de característica han de reflectir aquesta variabilitat interna i evitar presentar el perfil com a homogeni.

---

# 2. Connexions amb altres documents

| Codi | Títol | Relació | Quan co-activar |
|------|-------|---------|-----------------|
| M1_neurodiversitat-NESE | Neurodiversitat i NESE | Marc general de la neurodiversitat | Co-activació obligatòria per a totes les característiques constitutives |
| M2_DUA-principis-pautes | DUA — Principis i Pautes | El model de característiques és una implementació de la filosofia DUA | Quan calgui fonamentació teòrica |
| M2_mesures-suports-inclusius | Mesures i suports inclusius | Nivells d'intervenció (universal, addicional, intensiu) que corresponen als perfils | Quan el perfil té 3+ característiques simultànies |
| M1_plans-individuals-PAD-PI | Plans individuals PAD-PI | Perfils complexos amb múltiples constitutives sovint requereixen PI | Quan el perfil és complex |
| M4_adaptacio-curricular | Adaptació curricular | Les adaptacions han de ser coherents amb els criteris curriculars vigents | En totes les adaptacions formals |
| Tots els `tipus: caracteristica` de M1 | — | Aquest document marc governa la lògica de tots ells | Co-activació obligatòria quan s'activa qualsevol característica |

---

# 3. Detecció

## Senyals del docent
- Pregunta com categoritzar un alumne que "no encaixa en un sol perfil"
- Menciona combinació de dues o més característiques en un alumne
- Demana aclariments sobre la diferència entre "tenir" una condició i "ser" una persona amb aquella condició
- Vol crear o actualitzar el perfil d'un alumne al sistema
- Pregunta si ha de marcar una característica com a permanent o temporal
- Vol entendre com funciona el sistema de recuperació de coneixement

## Senyals de l'alumne
- Es descriu amb múltiples factors que generen barreres d'aprenentatge
- El docent expressa incertesa sobre si una situació és permanent o transitòria

## Senyals de context
- Primera configuració del perfil d'un alumne nou
- Revisió anual de perfils existents
- Situació d'alumne amb diagnòstic complex o múltiple
- Aula molt diversa on el docent necessita entendre com funciona el sistema

## Anti-senyals
- El docent ja té el perfil configurat i vol una adaptació: activar directament els documents de característica, no aquest marc
- Pregunta sobre estratègies didàctiques concretes: activar `M2_DUA-principis-pautes` o documents d'estratègia

---

# 4. Heurístiques

> La persona és sempre més que la suma de les seves característiques. El model no classifica persones — recupera coneixement pedagògic per servir-les millor.

**H1 — Quan aplica:** El docent declara un perfil amb múltiples característiques i vol saber com es gestionen.
**Fonament:** Cap característica és "principal" de manera universal. La prioritat depèn del context específic de l'adaptació. Per a un text científic, la dislèxia genera les barreres més visibles. Per a un debat oral, el TEA genera les principals. Per a activitats d'enriquiment, les altes capacitats marquen el camí. No s'ha de jerarquitzar en abstracte — cal ponderar en funció del context concret. Aquesta flexibilitat és la que permet adaptacions realment precises en lloc d'adaptacions genèriques que apliquen el màxim de suports sense distingir context.
**Exemple complet:** Una docent de 2n ESO té una alumna amb TEA, dislèxia i altes capacitats i pregunta quina característica ha de "posar primera". La resposta depèn del context: per adaptar un text de biologia, cal prioritzar les pautes de la dislèxia (format, frases curtes, tipografia). Per dissenyar una activitat de debat, cal prioritzar les pautes del TEA (literalitat, predictibilitat, torns explícits). Per proposar activitats d'aprofundiment, cal prioritzar les fortaleses de les altes capacitats (connexions interdisciplinàries, pensament contrafactual). Cap característica mana sempre — el context mana.

**H2 — Quan aplica:** El docent pregunta si ha d'actualitzar el perfil d'un alumne autista que "ha millorat molt".
**Fonament:** Les característiques constitutives no desapareixen, però la seva manifestació i les barreres que generen sí que evolucionen. Un alumne autista de 10 anys i el mateix alumne a 16 anys necessiten adaptacions molt diferents perquè ha desenvolupat estratègies de compensació, ha après a navegar entorns socials i ha construït recursos cognitius. La constitutivitat de la característica no implica estatisme de les necessitats — implica permanència de la identitat.
**Exemple complet:** El docent d'un alumne autista de 4t ESO comenta que l'alumne "ja sap com funcionar" i es pregunta si segueix necessitant les mateixes adaptacions. L'observació és vàlida: la característica TEA és constitutiva i no desapareix, però les necessitats d'adaptació evolucionen. Cal revisar el perfil: potser ara necessita menys suport en literalitat (ha après a descodificar el doble sentit) però continua necessitant absència d'ironia no marcada en textos escrits i estructura explícita en les consignes. Cal revisar les necessitats prioritàries del perfil, no eliminar la característica.

**H3 — Quan aplica:** El docent minimitza una característica contextual ("ja porta un any aquí, ja s'ha adaptat").
**Fonament:** Una característica contextual pot seguir generant barreres significatives fins i tot quan la situació ha evolucionat parcialment. La competència oral i la competència lectora acadèmica evolucionen a velocitats molt diferents. Un alumne pot entendre la conversa de classe (BICS) però seguir lluitant amb els textos disciplinaris (CALP), que triguen entre 5 i 7 anys a consolidar-se en una L2.
**Exemple complet:** El docent d'un nouvingut que porta 14 mesos diu que "ja entén tot". Cal matisar: el nivell de comprensió oral ha millorat, però la comprensió de textos escrits complexos, el vocabulari acadèmic i la capacitat d'inferir significats culturals implícits solen trigar molt més. Cal revisar el perfil de manera detallada — quin aspecte de la característica nouvingut segueix actiu i quin no — en lloc de desactivar-lo globalment.

**H4 — Quan aplica:** S'ha generat una adaptació que redueix complexitat però no incorpora les fortaleses del perfil.
**Fonament:** DUA estableix que les adaptacions han de maximitzar l'accés i el repte simultàniament. Reduir barreres sense aprofitar fortaleses genera materials empobridors que poden desmotivar alumnes que ja perceben les adaptacions com un senyal de baixa expectativa. Les fortaleses no són dades accessòries — són el motor de l'aprenentatge.
**Exemple complet:** S'ha generat una adaptació per a un alumne amb altes capacitats que simplement simplifica menys el text. El document de la característica indica que aquest alumne té capacitat excepcional per establir connexions entre àrees i per fer pensament contrafactual. Cal revisar l'adaptació i incorporar preguntes que activin explícitament aquesta fortalesa: connexions amb altres matèries, preguntes que plantegin escenaris alternatius, invitació a qüestionar les premisses del text. No n'hi ha prou amb "reduir menys" — cal "reptar més".

**H5 — Quan aplica:** El perfil de l'alumne conté dues o més característiques amb criteris d'adaptació parcialment contradictoris.
**Fonament:** Les tensions entre característiques no s'han de resoldre en silenci. Fer-les visibles al docent li permet prendre decisions informades basades en el coneixement que té de l'alumne concret, que sempre supera el que el sistema pot inferir. La transparència sobre les tensions és part de la qualitat de l'adaptació.
**Exemple complet:** Davant un perfil d'un alumne nouvingut amb TEA, el document de nouvingut recomana analogies culturalment properes per facilitar la comprensió, mentre que el document de TEA avisa que les analogies i el pensament metafòric generen confusió en molts alumnes autistes, que processen millor la informació literal. Cal detectar la tensió i fer-la explícita: "S'ha detectat una tensió entre el suport lingüístic recomanat per a nouvingut (analogies) i el processament literal característic del TEA. S'ha optat per exemples visuals i concrets sense component metafòric. El docent pot valorar si aquesta decisió s'ajusta al coneixement que té de l'alumne."

**H6 — Quan aplica:** Un alumne descriu les seves dificultats sense usar terminologia clínica.
**Fonament:** Els alumnes no han de conèixer els seus diagnòstics per beneficiar-se dels suports adequats. Les descripcions funcionals ("em costa llegir paraules llargues", "m'estressa quan canvien les rutines") contenen tota la informació necessària per activar les estratègies pertinents. El paper no és diagnosticar — sinó acompanyar i adaptar des de l'observació funcional.
**Exemple complet:** Un alumne de 4t ESO diu que "les lectures llargues li semblen impossibles, veu les lletres barrejades quan porta una estona llegint i li costa molt copiar de la pissarra". La resposta no ha de ser "sembla que tens dislèxia". Cal validar l'experiència i proposar estratègies: dividir la lectura en fragments curts, usar un marcador de línia, augmentar el cos de lletra, alternar lectura oral i silenciosa. Cal informar el docent tutor de les observacions per si cal derivar a un professional.

**H7 — Quan aplica:** Un alumne mostra frustració per les seves dificultats.
**Fonament:** La motivació és una condició necessària per a l'aprenentatge. Partir de les fortaleses activa la motivació i construeix autoconfiança. La frustració sovint neix de la generalització ("no sé res") que cal refutar ancorant-se en evidències concretes del que l'alumne sí que ha aconseguit.
**Exemple complet:** Una alumna amb discapacitat intel·lectual lleu treballa en comprensió lectora i diu "és que jo no entenc res de res". Cal refutar suaument la generalització i ancorar la conversa en quelcom que l'alumna sí ha entès. Si ha identificat correctament el personatge principal del text, es parteix d'aquesta fortalesa observacional per construir la comprensió dels elements més abstractes. El missatge implícit: "Sí que pots — comencem des d'on estàs."

**H8 — Quan aplica:** El docent vol explicar el model a l'alumne o a la família.
**Fonament:** La transparència sobre com funciona el sistema incrementa la confiança i el compromís de totes les parts. L'alumne que entén per què rep determinats suports és més capaç d'activar-los autònomament. La família que comprèn la distinció constitutiva/contextual col·labora millor en la revisió periòdica dels perfils contextuals.
**Exemple complet:** Un tutor vol explicar a la família d'un alumne amb TDAH i vulnerabilitat socioeducativa per què rep dos tipus de suport diferent. La preparació de la conversa pot ser així: el TDAH és una característica constitutiva (forma part de com el seu fill processa el món i no desapareixerà, però amb els suports adequats deixa de ser una barrera), mentre que la vulnerabilitat socioeducativa és contextual (respon a la situació actual de la família i pot canviar — per això es revisa cada trimestre). Aquesta distinció ajuda la família a entendre que no es tracta d'un etiquetatge permanent sinó d'un acompanyament adaptat a la realitat canviant.

---

# 5. Fonts i referències

> ⚠️ **Fonts: revisió pendent.** Afegeix i verifica les fonts adequades per a aquest document.

- CAST (2018). *Universal Design for Learning Guidelines, version 2.2*. http://udlguidelines.cast.org
- Booth, T. & Ainscow, M. (2011). *Index for Inclusion* (3a ed.). Centre for Studies on Inclusive Education.
- Decret 150/2017, de 17 d'octubre, de l'atenció educativa a l'alumnat en el marc d'un sistema educatiu inclusiu. DOGC 7477.
- Tomlinson, C.A. (2014). *The Differentiated Classroom* (2a ed.). ASCD.
