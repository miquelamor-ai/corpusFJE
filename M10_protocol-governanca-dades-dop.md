---
modul: M10
titol: "Protocol de governança de dades sensibles · DOP i NESE"
tipus: protocol-operatiu
descripcio: "Protocol operatiu de governança de dades sensibles per a Departaments d'Orientació Pedagògica (DOP), SIEI, SIAL, Aula d'Acollida i professionals NESE. Categories d'eines IA segons risc, regles operatives per al tractament d'informes psicopedagògics i dades NESE. Versió en producció (no màrtir)."
review_status: revisat
generat_at: 2026-05-25
paraules_clau: ["protocol", "governança dades", "DOP", "NESE", "SIEI", "SIAL", "informes psicopedagògics", "dades sensibles", "categories eines IA", "professionals NESE"]
---

# Protocol de governança de dades sensibles · DOPS i NESE
## Document operatiu per a equips directius i professionals NESE

> **Com entenem la integració de la IA**
> A Jesuïtes Educació, entenem que la integració de la IA ha d'estar al servei de la persona i del seu desenvolupament integral. Cerquem augmentar la qualitat de l'aprenentatge, de la pràctica docent i de la gestió, no substituir cap dimensió que els fa créixer integralment. Aquest marc concreta com fer-ho possible.

---

Aquest protocol estableix què entra a IA i què no, en el treball amb dades NESE. **És inflexible.** No està obert a interpretació individual ni a excepcions sense decisió institucional formal.

---

## Principi de fons

Les dades NESE pertanyen a l'alumne i al seu nucli pedagògic immediat. Sortir-ne sense protocol explícit és **cessió de criteri institucional** a un tercer (proveïdor d'IA) sense mandat per fer-ho. La intenció (estalvi de temps, qualitat d'output) és irrellevant per al fet jurídic.

---

## Mapa de tipologies d'eines

### Categoria A · IA institucional amb governança

- IA self-hosted del centre o de la xarxa
- Serveis amb contracte LOPD/RGPD signat amb la institució
- Compromís explícit de no-utilització de dades per entrenament

**Ús permès:** Sí, amb les regles operatives més avall.

### Categoria B · IA empresarial amb compte institucional

- Versions empresa de Microsoft Copilot, Google Workspace AI, Claude Enterprise, etc.
- Compte gestionat pel centre amb contracte adequat
- Generalment compleixen però **cal verificar el contracte específic**

**Ús permès:** Sí, amb anonimització obligatòria de dades nominatives.

### Categoria C · IA pública o personal

- ChatGPT públic, Gemini públic, Claude.ai personal, etc.
- Comptes individuals dels professionals
- **No** ofereixen garanties contractuals

**Ús permès:** **No** per a dades nominatives o derivades. Sí per a consultes generals abstractes (com es planteja un problema teòric, com es redacta una secció general d'un document).

---

## Regles operatives

### Regla 1 · Anonimització obligatòria

**Abans de qualsevol consulta a IA** (categoria A, B o C), substituir:

- Noms propis → "alumne A", "alumna B"
- Dates exactes de naixement → franja d'edat
- Centres concrets → "centre"
- Cognoms → eliminats
- Localitzacions específiques → "barri", "ciutat"
- Identificadors administratius → eliminats

### Regla 2 · Mínim necessari

Posar només la informació imprescindible per a la consulta. Si la pregunta és sobre estructura d'informe, no cal context clínic complet. Si és sobre adaptació curricular, no cal historial complet.

### Regla 3 · Sense copy-paste de fragments

Mai retallar i enganxar a IA fragments d'informes existents. Reescriure'n el resum anonimitzat per a la consulta.

### Regla 4 · Eines locals quan sigui possible

Per a tasques que es poden fer amb eines locals (correcció ortogràfica, formatatge), preferir-les a la IA del núvol.

### Regla 5 · Sandbox del centre quan es disposi

Si el centre disposa d'IA self-hosted o sandbox aïllat, és preferible per a aquestes tasques específiques.

---

## Casos pràctics

### Cas P.1. Esborrany d'informe psicopedagògic

**Què fer:** Redactar el contingut del dictamen amb dades reals al sistema gestor del centre. Per al pulit lingüístic i estructural, fer una versió anonimitzada (substituir noms, dates) i passar-la per IA categoria A o B. Recuperar la versió pulida i reintegrar les dades reals al sistema gestor.

**Què NO fer:** Copy-paste del dictamen complet a ChatGPT públic.

---

### Cas P.2. Comunicació amb família en altre idioma

**Què fer:** Redactar el missatge en català sense dades sensibles (només informació general: "ens reunim X dia, parlarem de l'evolució del seu fill"). Traduir amb IA. Si cal personalitzar més, fer-ho manualment.

**Què NO fer:** Generar amb IA el missatge complet incloent-hi historial.

---

### Cas P.3. Adaptació curricular per a alumne concret

**Què fer:** Especificar a la IA el perfil de manera abstracta ("alumne de 5è amb dificultats lectores i d'atenció, amb diagnòstic de TDAH"). NO el nom ni el codi d'expedient.

**Què NO fer:** Posar el nom o cap dada que permeti reidentificació.

---

### Cas P.4. Anàlisi de patrons en un grup

**Què fer:** Si voleu analitzar patrons del grup, exportar dades agregades i anonimitzades. Si la mostra és petita (menys de 5 alumnes), més restricció encara.

**Què NO fer:** Pujar fitxers Excel amb columnes nominatives a IA.

---

## Què passa quan algú trenca el protocol?

El protocol és **institucional** — no és una opinió individual. Quan es detecta:

1. **Conversa primer.** No sancionar abans d'entendre. Sovint és bona intenció + manca de formació.
2. **Auditoria del flux de dades.** Quina informació ha sortit, on, com.
3. **Comunicació institucional segons gravetat.** En els casos més greus, comunicació a la persona afectada (alumne/família).
4. **Reforç de formació.** No esperar que tothom entengui el protocol per inferència — fer-lo explícit periòdicament.
5. **Eines accessibles.** Si el protocol és restrictiu però no hi ha eina alternativa fàcilment accessible, l'incompliment és previsible. Responsabilitat institucional.

---

## Auditoria periòdica

**Anual mínim:** revisió de quines eines IA s'usen al centre, quines categories, quin contracte, qui té accés.
**Trimestral preferible:** mostra aleatòria de fluxos de treball amb consentiment dels professionals.
**Davant cada nova eina:** procés formal de validació abans d'integració.

---

## Decisió institucional formal

Aquest protocol ha de ser:

1. **Aprovat** per equip directiu.
2. **Signat** per professionals NESE com a part del contracte de funcions.
3. **Renovat** anualment amb actualització de categories d'eines.
4. **Visible** als documents d'alta de personal nou.

Sense aquest formalisme, el protocol és recomanació individual sense força institucional.
