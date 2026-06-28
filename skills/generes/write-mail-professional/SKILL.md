---
name: write-mail-professional
description: 'Instrument per adaptar o generar un correu electrònic professional:
  estructura de 7 parts (assumpte-salutació-introducció-cos-tancament-comiat-signatura),
  propòsit clar al primer paràgraf, registre formal consistent i asincronicitat canal
  electrònic. HCL Explicar + Justificar (B1+). HCL secundària: Argumentar (B2+). Citat
  explícitament al MALL com a exemple de gènere nou generat per les noves tecnologies.
  Rúbrica gradada 8 passos × 5 nivells MECR (A1→C1). Pre-A1 no s''aplica.'
author: FJE — Fundació Jesuïtes Educació
version: 1.1.0
tools_required: []
agent_role: adapter
genre_key: mail_professional
triggers:
- path: params.genere_discursiu
  equals: mail_professional
macro_tipologia: conversacional
label_ca: Correu electrònic professional
mecr_range:
- A1
- A2
- B1
- B2
- C1
translanguaging: true
multimodal: false
moduls_relacionats:
- M3
font_canonic: M3_genere-escriure-mail-professional.md
font_version: 1.1.0
generat_at: '2026-06-28'
generat_per: build_skills.py@v2-2026-05-26
checksum_font: 31fbbf354a6d6b2c
---

# Escriure/adaptar un correu electrònic professional — skill operativa per a LLM

El correu electrònic professional és un **text comunicatiu asíncron** entre interlocutors amb una relació professional o institucional, enviat a través del canal electrònic. El seu tret definitori és la **combinació de formalitat i eficiència digital**: l'estructura és formal (com la carta), però el canal és electrònic (cap + `A:`, `CC:`, `Assumpte:`) i el ritme d'intercanvi és asíncron. El **propòsit comunicatiu ha de ser clar des del primer paràgraf** (estructura de piràmide directa: primer la informació o la sol·licitud, no el preàmbul). El MALL el cita explícitament com a exemple de **gènere nou generat per les noves tecnologies** ("correus electrònics, missatges de mòbil"), el que li dona un estatut propi dins del repertori de gèneres contemporanis.

**Tipologia MALL (macro)**: Conversacional (interacció escrita entre interlocutors amb torns asíncrons). El gènere pertany a la macro-tipologia **Conversacional** del M3 (vegeu `macro_tipologia: conversacional` al frontmatter): hi ha un emissor, un receptor específic, i una expectativa de resposta o acció.
**HCL principal**: Explicar (informar d'un fet o situació) + Justificar (demanar o argumentar motius, B1+).
**HCL secundàries**: Argumentar — persuadir, presentar una candidatura, rebatjar una objecció (B2+).
**No s'adapta a pre-A1**: el mail professional requereix comprensió del **destinatari institucional** i de la relació formal emissor-receptor, i demana producció escrita funcional mínima. Igual que la carta, la distinció de registre com a variació conscient no és accessible a pre-A1.
**Translanguaging (A1-A2)**: el cos del mail pot incloure expressions en L1 entre claudàtors quan l'alumne no troba el mot en llengua de destinació. No s'aplica mai a l'assumpte, la salutació ni el comiat, que son els ancoratges formals del gènere.

**Distinció clau vs gèneres propers:**
- **vs carta**: la carta va en paper, porta encapçalament postal (lloc, data, adreça) i no té camp `Assumpte:` ni `A:`. El mail professional no porta adreça postal, però té camp `Assumpte:` obligatori, pot admetrer un to lleugerament més àgil que la carta i mai porta data manuscrita. Un mail no és una carta digital: son gèneres distints.
- **vs diàleg**: el diàleg és sincronia (oral o teatral); el mail és asincronicitat escrita. El mail es llegeix i es respon en diferit, la qual cosa permet —i exigeix— estructura i planificació que el diàleg en temps real no requereix.
- **vs missatge de WhatsApp/xat**: el mail professional té registre formal, cap emoji, cap abreviatura (`xq`, `q tal`, `ok`), cap informalitat tonal. Són canals distints amb convencions radicalment distintes. La confusió entre els dos és un error de competència sociolingüística que cal abordar explícitament.

**Connexions MALL transversals:**
- *Registre formal consistent com a competència professional*: mantenir el `vostè`, les fórmules de salutació i comiat formals, i la veu neutral és una competència directament transferible a la vida laboral, les relacions amb organismes i la FP. L'alumne que aprèn a no tutear un proveïdor ni posar emojis en un mail institucional adquireix una competència professional real i avaluable.
- *El camp Assumpte com a operació de síntesi*: escriure un assumpte clar, concís i informatiu és una microtasca cognitiva d'alt valor: l'alumne ha de destil·lar el propòsit del mail en 5-8 paraules. Aquesta habilitat és transferible a títols, resums i presentacions.
- *Piràmide directa com a convenció professional*: el que s'espera primer en un mail no és un preàmbul sinó la informació o sol·licitud. Aprendre a escriure en piràmide directa (QUÈ → PER QUÈ → COM) és una competència de comunicació professional de primer ordre.
- *Asincronicitat i planificació*: a diferència del diàleg oral, el mail dóna temps per pensar, revisar i estructurar. Ensenyar a aprofitar aquest temps (esborrar, rellegir, comprovar el to) és ensenyar metacognició de la comunicació escrita.

**Aclariment d'ús — què descriu aquesta rúbrica.**
Aquesta rúbrica descriu el **correu adaptat o generat per a la LECTURA i el modelatge** de l'alumne (el model que llegeix i imita), no la producció autònoma lliure. Principi pedagògic MALL: l'alumne llegeix models al màxim del seu abast cognitiu, amb la forma lingüística ajustada al seu nivell.
**Sub-granularitat dins de A1**: es treballa amb `fase_lectora: [alfabetica_emergent, alfabetica_fluida]`; no hi ha nivell logogràfic perquè el gènere requereix producció escrita funcional mínima.

## Modulació per nivell (format vertical jerarquitzat)

### pre-A1 — Emergent


**1. Assumpte**
- Síntesi del propòsit: 2-4 paraules. Propòsit central ("Sol·licitud informació"). Fórmula fixada.

**2. Salutació**
- Ancoratge formal: Fórmula fixada: "Benvolguda / Benvolgut," (sense nom). Pot usar "A qui correspongui,".

**3. Introducció**
- Propòsit al 1r paràgraf: 1 frase: qui sóc + per quin motiu escric. Frase simple (8-10 paraules).

**4. Cos**
- Informació / sol·licitud: 1 frase. 1 sol punt, 1 sol·licitud. Vocabulari molt freqüent.

**5. Tancament**
- Acció esperada: 1 frase fixada: "Quedo a l'espera de resposta."

**6. Comiat**
- Fórmula de tancament: Fórmula fixada: "Atentament,"

**7. Signatura**
- Identificació del remitent: Nom + cognom.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: (oral o escrit mínim) "El meu mail diu qui sóc i per quin motiu escric?"

### A1 — Inicial


**1. Assumpte**
- Síntesi del propòsit: 4-6 paraules. Propòsit + objecte ("Demanda de pressupost material escolar").

**2. Salutació**
- Ancoratge formal: Fórmula fixada + càrrec si es coneix ("Benvolguda directora,").

**3. Introducció**
- Propòsit al 1r paràgraf: 1-2 frases: qui sóc + motiu + context breu.

**4. Cos**
- Informació / sol·licitud: 2-3 frases. 1 motiu, 1 sol·licitud. Connectors bàsics ("perquè", "i").

**5. Tancament**
- Acció esperada: 1-2 frases. Indica l'acció esperada ("Li demano que m'enviï...").

**6. Comiat**
- Fórmula de tancament: "Atentament," o "Cordialment,"

**7. Signatura**
- Identificació del remitent: Nom + cognom + curs/grup.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He explicat el motiu i he demanat una sola cosa clarament?"

### A2 — Funcional


**1. Assumpte**
- Síntesi del propòsit: 5-8 paraules. Assumpte informatiu i específic. Pot incloure referència ("Ref: oferta X").

**2. Salutació**
- Ancoratge formal: Salutació ajustada al destinatari (nom, càrrec, institució).

**3. Introducció**
- Propòsit al 1r paràgraf: 2-3 frases: presentació, motiu i referència al context (reunió prèvia, anunci, etc.).

**4. Cos**
- Informació / sol·licitud: 3-5 frases. Motiu justificat. Connector causal ("per tant", "ja que"). Veu formal consistent.

**5. Tancament**
- Acció esperada: Tancament amb acció esperada + termini si cal ("Esperaria resposta abans del...").

**6. Comiat**
- Fórmula de tancament: "Atentament," / "Amb una salutació cordial," / "Cordialment,"

**7. Signatura**
- Identificació del remitent: Nom + cognom + centre + curs.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El meu mail és formal de principi a fi? El lector sap exactament què li demano?"

### B1 — Estratègic


**1. Assumpte**
- Síntesi del propòsit: Assumpte precís i complet. Indica propòsit i context en 8-10 paraules.

**2. Salutació**
- Ancoratge formal: Salutació precisa amb nom/càrrec/títol.

**3. Introducció**
- Propòsit al 1r paràgraf: Introducció clara i directa. Pot incloure referència a interacció prèvia o marc.

**4. Cos**
- Informació / sol·licitud: Múltiples punts ben organitzats. Connectors acadèmics. Veu impersonal si cal. Pot usar llista numerada.

**5. Tancament**
- Acció esperada: Tancament estratègic: acció esperada + disponibilitat per ampliar informació.

**6. Comiat**
- Fórmula de tancament: Fórmula ajustada al grau de formalitat del destinatari.

**7. Signatura**
- Identificació del remitent: Nom + cognom + càrrec si escau + dades de contacte.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "He organitzat bé els punts? El to és consistent? He revisat l'assumpte?"

### B2 — Acadèmic


**1. Assumpte**
- Síntesi del propòsit: Assumpte professional ple. Pot incloure referència, data o número d'expedient.

**2. Salutació**
- Ancoratge formal: Salutació protocol·lària completa. Admet matisació de to (Sr./Sra. + cognom en contextos molt formals).

**3. Introducció**
- Propòsit al 1r paràgraf: Introducció estratègica: situa el context, indica el propòsit i anticipa l'estructura del mail.

**4. Cos**
- Informació / sol·licitud: Cos argumentat. Veu professional plena. Anticipació d'objeccions o riscos si cal. Gestió de la persuasió.

**5. Tancament**
- Acció esperada: Tancament professional: acció esperada, termini, oferta de seguiment, to de col·laboració.

**6. Comiat**
- Fórmula de tancament: Fórmula protocol·lària ajustada al context (institució, empresa, rang del destinatari).

**7. Signatura**
- Identificació del remitent: Signatura professional completa: nom, càrrec, departament, telèfon, adreça electrònica.

**8. Autoavaluació metacognitiva**
- Reflexió sobre el procés: "El mail és professional, precís i estratègic? El to és adequat a la relació amb el destinatari?"

### C1+ — Crític


