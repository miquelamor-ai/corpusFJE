---
modul: M10
titol: "Política de protecció de dades amb IA"
tipus: politica
descripcio: "Política institucional v0 (proposta màrtir) sobre protecció de dades en l'ús de la IA a FJE. 4 pàgines · categories d'eines A/B/C · 6 regles operatives · 11 tipus de dades excloses · procediment d'incidència 6 passos · drets dels subjectes · pendent assessoria legal externa per a versió CDX."
review_status: esborrany
generat_at: 2026-05-24
paraules_clau: ["política", "protecció de dades", "RGPD", "LOPDGDD", "IA generativa", "incidència", "DPO", "proposta màrtir"]
---

# Política de protecció de dades amb intel·ligència artificial
## Proposta màrtir · v0 · Maig 2026

> **Aquest document és una proposta màrtir.** Es validarà definitivament al Consell de Direcció de Xarxa entre gener i març de 2027 (Fase D del pla de desplegament), amb la concurrència d'assessoria legal externa especialitzada en educació i protecció de dades. Fins aleshores té caràcter orientatiu. Es publica ara per donar criteri operatiu a centres, professorat i àrees de gestió mentre es completa el marc jurídic definitiu.

---

> **Com entenem la integració de la IA**
>
> A Jesuïtes Educació, entenem que la integració de la IA ha d'estar al servei de la persona i del seu desenvolupament integral. Cerquem augmentar la qualitat de l'aprenentatge, de la pràctica docent i de la gestió, no substituir cap dimensió que els fa créixer integralment. Aquest marc concreta com fer-ho possible.

---

## 1. Propòsit

Aquesta política estableix les condicions per al **tractament de dades personals** quan s'utilitzen sistemes d'intel·ligència artificial generativa. No regula l'ús pedagògic de la IA (això ho fan P1 i P2); regula què passa amb la **dada** quan entra a una eina d'IA.

Té tres objectius:

- **Protegir** alumnat, famílies, personal i la pròpia institució de cessions no autoritzades de dades.
- **Donar seguretat operativa** al docent i al personal de gestió sobre què poden i no poden fer.
- **Demostrar diligència** institucional davant les obligacions del RGPD, LOPDGDD i regulació educativa.

## 2. Abast

S'aplica a:

- Tot el personal de la xarxa: docent, gestió, equips directius, paraescolars i orientadors.
- Qualsevol dada personal d'alumnat, famílies, professorat o tercers vinculada a la institució.
- Qualsevol eina d'IA generativa, homologada o no, utilitzada en l'exercici professional.

No s'aplica a:

- L'ús personal d'IA fora de l'exercici professional, sempre que no s'introdueixin dades de la institució.
- Dades anònimes, agregades o sintètiques sense risc de reidentificació.

## 3. Marc legal de referència

- **Reglament (UE) 2016/679** (RGPD).
- **Llei Orgànica 3/2018** de protecció de dades personals i garantia dels drets digitals (LOPDGDD).
- **AI Act (Reglament IA UE)** quan sigui aplicable.
- **LOMLOE · LEC** quant a dades educatives.
- Orientacions de l'**Agència Espanyola de Protecció de Dades** (AEPD) i de l'**Autoritat Catalana de Protecció de Dades** (APDCAT) sobre IA i educació.
- Polítiques internes de Jesuïtes Educació quant a tractament de dades.

## 4. Categories d'eines i ús permès

Inspirada en el protocol de governança de dades sensibles DOP, aquesta classificació s'estén a totes les eines d'IA professional.

### Categoria A · IA institucional amb governança plena
- Eina self-hosted del centre o de la xarxa (per exemple, ATNE).
- Serveis amb contracte LOPD/RGPD signat amb la institució i compromís explícit de no-utilització de dades per entrenament.
- Compte i autenticació corporativa.

**Ús permès**: sí, amb les regles operatives generals.

### Categoria B · IA empresarial amb compte institucional
- Versions EDU/empresa de Gemini Workspace, NotebookLM, Microsoft 365 Copilot.
- Compte gestionat pel centre amb contracte específic.
- Generalment compleixen, però **cada contracte cal verificar-lo**.

**Ús permès**: sí, amb pseudonimització obligatòria de dades nominatives i les regles operatives generals.

### Categoria C · IA pública o de consumidor
- ChatGPT consumidor, Claude.ai consumidor, Gemini de gmail personal, Character.AI, Replika i similars.
- Comptes individuals dels professionals.
- Sense garanties contractuals.

**Ús permès**: **no** per a cap dada vinculada a la institució. Sí per a consultes generals abstractes (com es planteja un problema teòric, redacció d'una secció general d'un document sense referències personals).

## 5. Regles operatives transversals

Vàlides per a les categories A i B; obligatòries totes per a B; recomanables i auditables per a A.

### Regla 1 · Pseudonimització abans de qualsevol consulta

Abans d'introduir text que pugui contenir dades personals, substituir:

- Noms propis → "alumne A", "alumna B".
- Cognoms → eliminats.
- Dates exactes de naixement → franja d'edat.
- Centres concrets → "centre".
- Localitzacions específiques → "barri", "ciutat".
- Identificadors administratius (NIE, NIA, matrícula) → eliminats.
- Telèfons, adreces, correus personals → eliminats.

### Regla 2 · Mínim necessari

Introduir només la informació estrictament necessària per a l'objectiu de la consulta. Si una pregunta es pot respondre sense dada personal, fer-la sense.

### Regla 3 · Verificació de l'output

Quan l'output de la IA es reutilitzi en context institucional (informes, comunicats, materials), verificar humanament abans d'utilitzar-lo.

### Regla 4 · Traçabilitat

Quan l'ús sigui rellevant (per exemple, generació de materials avaluables), deixar registre amb declaració d'ús (eina, prompt abstracte, data, resultat).

### Regla 5 · Mai introducció de dades sensibles

Veure secció 6.

## 6. Dades que mai s'introdueixen a IA

Independentment de la categoria d'eina, les següents dades **no es poden introduir mai**:

- Informes psicopedagògics o orientadors identificables.
- Dades NESE, SIEI, SIAL, AACC, Acollida identificables.
- Dades de salut o discapacitat de qualsevol persona.
- Dades familiars sensibles (situació socioeconòmica, conflictes familiars, custòdia).
- Dades de conducta i mesures disciplinàries individualitzades.
- Valoracions emocionals o psicològiques identificables.
- Dades biomètriques o de reconeixement facial/veu.
- Informació financera identificable.
- Comunicacions privades amb famílies amb dades identificables.
- Documents d'identitat (DNI, passaport, NIE).
- Imatges identificables d'alumnat o personal sense autorització específica.

Aquestes dades requereixen tractament en àmbits específics i mai surten del perímetre institucional sense base legal específica.

## 7. Obligacions del personal

Tot membre del personal que utilitzi IA en exercici professional es compromet a:

1. **Conèixer** aquesta política i la Política d'ús d'IA del seu col·lectiu (P1, P2).
2. **Utilitzar només eines** de categoria A o B per a usos amb dades institucionals.
3. **Pseudonimitzar** sempre abans d'introduir dades.
4. **Respectar** la llista de dades que mai s'introdueixen.
5. **Reportar** qualsevol incidència al referent IA d'escola o, en absència, a la direcció pedagògica.
6. **Acceptar** revisió periòdica de l'ús quan així s'estableixi al protocol d'auditoria.

## 8. Procediment davant incidència

Si es produeix una de les següents situacions, s'activa el procediment d'incidència de dades:

- Introducció involuntària de dades sensibles a una eina d'IA.
- Filtració d'output amb dades identificables a destinataris no autoritzats.
- Sospita de compromís d'una credencial corporativa d'eina d'IA.
- Detecció d'ús d'eina d'IA no homologada amb dades institucionals per part de personal o alumnat.

**Resposta institucional**:

1. **Aturada immediata** de l'ús problemàtic.
2. **Notificació al DPO de xarxa** dins de 24 hores des de la detecció.
3. **Avaluació de l'afectació**: quines dades, quins subjectes, quina extensió.
4. **Comunicació als afectats** si l'incident és susceptible de causar risc als drets dels subjectes (segons l'art. 34 RGPD).
5. **Notificació a l'autoritat de control** (AEPD/APDCAT) si l'incident és susceptible de causar risc per als drets (art. 33 RGPD), dins de 72 hores.
6. **Registre intern** de l'incident, la resposta i les mesures preventives.

El **DPO de xarxa** és el punt de contacte únic per a totes les incidències.

## 9. Autoritzacions famílies

L'ús d'IA amb dades d'alumnat menor d'edat requereix base legal específica. La xarxa preveu:

- **Autorització general de tractament IA** com a annex a la documentació d'inici de curs (a desplegar curs 27-28).
- **Autoritzacions específiques** per a usos puntuals d'alta sensibilitat (imatge, veu, dades identificables en pilots).
- **Renovació anual** de les autoritzacions amb informació transparent del que s'ha fet l'any anterior.

Mentre no estigui validada la política d'autoritzacions (P6, prevista per a curs 27-28), els centres apliquen el principi de cautela: cap dada identificable d'alumnat menor a cap eina d'IA.

## 10. Drets dels subjectes

Els subjectes de les dades (alumnat, famílies, personal) tenen els drets reconeguts pel RGPD i la LOPDGDD:

- **Accés** a la informació sobre quines dades es tracten amb IA.
- **Rectificació** d'inexactituds.
- **Supressió** quan correspongui.
- **Oposició** al tractament en circumstàncies específiques.
- **Limitació** del tractament.
- **Portabilitat** quan correspongui.

Per a l'exercici d'aquests drets, el punt de contacte és el **DPO de xarxa**.

## 11. Governança i revisió

- **Revisió anual** d'aquesta política per part del Consell Pedagògic, amb suport del DPO i d'assessoria legal externa.
- **Actualització de la llista d'eines homologades** trimestralment per part de la Direcció de Transformació Digital.
- **Modificacions substantives** requereixen aprovació del Consell de Direcció de Xarxa.

## 12. Sancions i responsabilitat

L'incompliment d'aquesta política s'incorpora al règim ordinari del centre amb les següents gradacions:

- **Lleu**: ús d'eina no homologada amb dades no sensibles. Conversa amb direcció + formació.
- **Greu**: introducció de dades sensibles a IA homologada sense pseudonimitzar, o ús d'IA no homologada amb dades institucionals. Procediment d'incidència + mesura correctora.
- **Molt greu**: introducció de dades de les enumerades a la secció 6 a qualsevol IA, ús per a decisions automatitzades sobre persones, o exposició de dades identificables a tercers. Procediment disciplinari ordinari i, si correspon, notificació a autoritat de control.

---

## Annex 1 · Eines amb base legal a la xarxa

| Eina | Categoria | Base legal | Estat |
|---|---|---|---|
| ATNE (xarxa) | A | Self-hosted · sense sortida de dades | Pilot |
| MAGINIA | A | Plataforma pròpia · RLS Supabase | Producció |
| CREATIVIA / CREACTIVITAT | A | Eina pròpia · en redisseny | En refer |
| Gemini Workspace EDU | B | Contracte EDU corporatiu | Producció |
| NotebookLM EDU | B | Contracte EDU corporatiu | Producció |
| Microsoft 365 Copilot EDU | B | Subscripció EDU del centre | Producció |
| ChatGPT, Claude.ai, Character.AI, Replika consumidor | C | Sense conveni | Prohibides per a dades institucionals |

## Annex 2 · Plantilla d'incidència de dades

> Data i hora de detecció · Persona que detecta · Eina implicada · Tipus de dades · Subjectes afectats (nombre i tipologia) · Acció aturada · DPO notificat (sí/no, hora) · Avaluació de risc · Mesura aplicada · Aprenentatges per a prevenció.

## Annex 3 · Glossari ràpid

- **DPO** (Data Protection Officer / Delegat de Protecció de Dades): figura institucional responsable de supervisar el compliment del RGPD a la xarxa.
- **Pseudonimitzar**: substituir identificadors directes per claus que no permeten la reidentificació directa.
- **Anonimitzar**: tractar les dades de manera que no permetin cap reidentificació, ni directa ni indirecta.
- **Dada sensible (categoria especial)**: dada que revela origen ètnic, opinions, salut, vida sexual, biometria, etc. (art. 9 RGPD).
- **Base legal**: justificació jurídica del tractament (consentiment, interès legítim, obligació legal, etc.).

---

*Document de proposta màrtir v0 · Maig 2026 · Jesuïtes Educació · Equip de redacció: Direcció de Transformació Digital + Coordinació Marc IA · Assessoria legal externa pendent per a la versió definitiva. Mappat al pla mestre: 2.3 (Capa governança) + B4 (esborrany v0) → D3 (versió per validar CDX). Revisió: jun 26 inici amb assessoria → Q1 27 versió CDX.*
