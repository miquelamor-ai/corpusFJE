---
tipus: derivat
font_canonic: M3_genere-escriure-resum.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-06'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: d6ba1ea0a1bdf465
---

# Escriure/adaptar un resum — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un resum per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Claredat i directesa**: 1 frase que diu de qué tracta el text. Directa. Al principi.
- **Fidelitat i imparcialitat**: No afegir opinions pròpies: sense "crec que", "m'agrada", "és interessant".
- **Coherència i estructura**: "I", "però", "perquè". Pocs però presents.
- **Síntesi i selecció**: 3-4 frases. Màxim 1/3 del text font.
- **Síntesi sense preàmbul**: Cap "En aquest text…", "L'autor diu que…" com a primera frase. La primera paraula del resum és ja contingut.
- **No còpia literal**: Cap frase copiada del text font. Reformulació sempre.
- **Fidelitat al text font**: Fidelitat a la idea principal i a les 2-3 idees secundàries del text font.
- **Reflexió sobre el procés**: "He escrit la idea principal en la primera frase. No he escrit la meva opinió."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Claredat i directesa**: Idea principal en 1-2 frases. Primer paràgraf. Directa i sense preàmbul.
- **Fidelitat i imparcialitat**: Sense afegir informació nova ni opinions. Veu neutra i impersonal.
- **Coherència i estructura**: "Per tant", "d'altra banda", "però". Variats i usats per connectar les idees.
- **Síntesi i selecció**: 4-6 frases (o ~1/4 del text font). Proporcional a la complexitat del font.
- **Síntesi sense preàmbul**: Idem. Sense meta-comentaris sobre el text o l'autor.
- **No còpia literal**: Idem. Cap fragment de més de 4 paraules consecutives idèntiques al font.
- **Fidelitat al text font**: Fidelitat a la idea principal, a les idees secundàries i a l'ordre del font.
- **Reflexió sobre el procés**: "He connectat les idees amb connectors. No he afegit informació nova."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Claredat i directesa**: Idea principal condensada amb precisió. Primera frase densa i informativa.
- **Fidelitat i imparcialitat**: Reformulació que manté el punt de vista de l'autor original sense adoptar-lo.
- **Coherència i estructura**: Connectors que reflecteixen la relació real entre idees del text font (causa, contrast, conseqüència).
- **Síntesi i selecció**: ~1/4 o 1/5 del text font. Preservar estructura lògica per davant de la llargada mecànica.
- **Síntesi sense preàmbul**: Idem. Cap frase buida de contingut al resum.
- **No còpia literal**: Idem. La reformulació captura el sentit, no el text superficial.
- **Fidelitat al text font**: Fidelitat a la idea principal, a les idees secundàries, als connectors i a la relació lògica del font.
- **Reflexió sobre el procés**: "El meu resum té les idees en el mateix ordre que el text original. He eliminat exemples però no idees."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Claredat i directesa**: Idea principal amb el matís necessari. Primera frase que capta el nucli del text font.
- **Fidelitat i imparcialitat**: Veu de l'autor preservada. Distinció clara entre el que diu l'autor i qui resumeix.
- **Coherència i estructura**: Connectors precisos que reprodueixen l'estructura lògica del text font.
- **Síntesi i selecció**: Proporció conscient: la llargada reflecteix la importància relativa de cada idea del font.
- **Síntesi sense preàmbul**: Idem. Densitat informativa alta.
- **No còpia literal**: Idem. La reformulació preserva els matisos semàntics rellevants del font.
- **Fidelitat al text font**: Fidelitat a la complexitat informativa i al registre del text font.
- **Reflexió sobre el procés**: "He mantingut la veu de l'autor. La llargada és proporcional al text font."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Claredat i directesa**: Idea principal amb tots els matisos que el text font implica, sense sobrecarregar.
- **Fidelitat i imparcialitat**: Veu de l'autor preservada amb precisió. Atribució explícita si cal ("Segons l'autor...").
- **Coherència i estructura**: Connectors sofisticats que capturen la lògica argumentativa o expositiva de l'autor.
- **Síntesi i selecció**: Condensació rigorosa: cada frase del resum aporta informació nova i necessària del font.
- **Síntesi sense preàmbul**: Idem. Màxima densitat: cada frase és contingut del font, no comentari sobre el font.
- **No còpia literal**: Idem. La reformulació pot conservar termes tècnics si no existeix paràfrasi adequada.
- **Fidelitat al text font**: Fidelitat total: idea principal, idees secundàries, relació lògica i matisos del font.
- **Reflexió sobre el procés**: "El meu resum és dens, fidel i complet. Qualsevol persona pot entendre el text font llegint el meu resum."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


