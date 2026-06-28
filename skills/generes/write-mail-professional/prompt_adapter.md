---
tipus: derivat
font_canonic: M3_genere-escriure-mail-professional.md
font_version: 1.1.0
vista: C.prompt-adapter-llm
generat_at: '2026-06-28'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 31fbbf354a6d6b2c
---

# Escriure/adaptar un correu electrònic professional — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un correu electrònic professional per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Síntesi del propòsit**: 2-4 paraules. Propòsit central ("Sol·licitud informació"). Fórmula fixada.
- **Ancoratge formal**: Fórmula fixada: "Benvolguda / Benvolgut," (sense nom). Pot usar "A qui correspongui,".
- **Propòsit al 1r paràgraf**: 1 frase: qui sóc + per quin motiu escric. Frase simple (8-10 paraules).
- **Informació / sol·licitud**: 1 frase. 1 sol punt, 1 sol·licitud. Vocabulari molt freqüent.
- **Acció esperada**: 1 frase fixada: "Quedo a l'espera de resposta."
- **Fórmula de tancament**: Fórmula fixada: "Atentament,"

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Síntesi del propòsit**: 4-6 paraules. Propòsit + objecte ("Demanda de pressupost material escolar").
- **Ancoratge formal**: Fórmula fixada + càrrec si es coneix ("Benvolguda directora,").
- **Propòsit al 1r paràgraf**: 1-2 frases: qui sóc + motiu + context breu.
- **Informació / sol·licitud**: 2-3 frases. 1 motiu, 1 sol·licitud. Connectors bàsics ("perquè", "i").
- **Acció esperada**: 1-2 frases. Indica l'acció esperada ("Li demano que m'enviï...").
- **Fórmula de tancament**: "Atentament," o "Cordialment,"

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Síntesi del propòsit**: 5-8 paraules. Assumpte informatiu i específic. Pot incloure referència ("Ref: oferta X").
- **Ancoratge formal**: Salutació ajustada al destinatari (nom, càrrec, institució).
- **Propòsit al 1r paràgraf**: 2-3 frases: presentació, motiu i referència al context (reunió prèvia, anunci, etc.).
- **Informació / sol·licitud**: 3-5 frases. Motiu justificat. Connector causal ("per tant", "ja que"). Veu formal consistent.
- **Acció esperada**: Tancament amb acció esperada + termini si cal ("Esperaria resposta abans del...").
- **Fórmula de tancament**: "Atentament," / "Amb una salutació cordial," / "Cordialment,"

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Síntesi del propòsit**: Assumpte precís i complet. Indica propòsit i context en 8-10 paraules.
- **Ancoratge formal**: Salutació precisa amb nom/càrrec/títol.
- **Propòsit al 1r paràgraf**: Introducció clara i directa. Pot incloure referència a interacció prèvia o marc.
- **Informació / sol·licitud**: Múltiples punts ben organitzats. Connectors acadèmics. Veu impersonal si cal. Pot usar llista numerada.
- **Acció esperada**: Tancament estratègic: acció esperada + disponibilitat per ampliar informació.
- **Fórmula de tancament**: Fórmula ajustada al grau de formalitat del destinatari.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Síntesi del propòsit**: Assumpte professional ple. Pot incloure referència, data o número d'expedient.
- **Ancoratge formal**: Salutació protocol·lària completa. Admet matisació de to (Sr./Sra. + cognom en contextos molt formals).
- **Propòsit al 1r paràgraf**: Introducció estratègica: situa el context, indica el propòsit i anticipa l'estructura del mail.
- **Informació / sol·licitud**: Cos argumentat. Veu professional plena. Anticipació d'objeccions o riscos si cal. Gestió de la persuasió.
- **Acció esperada**: Tancament professional: acció esperada, termini, oferta de seguiment, to de col·laboració.
- **Fórmula de tancament**: Fórmula protocol·lària ajustada al context (institució, empresa, rang del destinatari).

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


