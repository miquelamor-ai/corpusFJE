---
tipus: derivat
font_canonic: M3_genere-escriure-noticia.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-06'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 46bc1184369e743f
---

# Escriure/adaptar una notícia — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar una notícia per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Fets clau**: L'adult explica el fet amb una imatge. L'alumne assenyala el personatge principal.
- **Llargada i forma**: 1-5 paraules acompanyades d'un pictograma a l'esquerra. Sense verb obligatori.
- **Estil literal**: Concepte únic, suport visual obligatori.
- **Cobertura 5W**: Cobreix 2W: Qui i Què. Lectura mediada per adult.
- **Llargada de frase**: Frases de fins a 8 paraules.
- **Estructura sintàctica**: Frase única amb suport visual; sintaxi mínima.
- **Ordre informatiu**: 1-2 frases amb pictograma de suport; el fet principal apareix primer.
- **Volum del cos**: 1-2 frases.
- **Cita directa**: Sense cites. L'adult és la font.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Fets clau**: Respon "Qui?" i "Què?" en 1-2 paraules.
- **Llargada i forma**: Fins a 10 paraules. Verb concret en present o passat.
- **Estil literal**: Sense metàfores ni jocs de paraules.
- **Cobertura 5W**: Cobreix 3W: Qui, Què i On.
- **Llargada de frase**: Frases de fins a 12 paraules.
- **Estructura sintàctica**: Frase simple Subjecte + Verb + Complement.
- **Ordre informatiu**: 2-3 frases ordenades del fet més important al menys important.
- **Volum del cos**: 2-3 frases.
- **Cita directa**: Sense cites.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Fets clau**: Identifica 2-3 fets principals del text font.
- **Llargada i forma**: Fins a 12 paraules. Verb + complement informatiu.
- **Estil literal**: Sense metàfores. Llenguatge directe.
- **Cobertura 5W**: Cobreix 4-5W (afegeix Quan i, si escau, Per què).
- **Llargada de frase**: Frases de fins a 15 paraules.
- **Estructura sintàctica**: Pot incloure una subordinada simple.
- **Ordre informatiu**: 2-3 paràgrafs amb piràmide invertida clara.
- **Volum del cos**: 2-3 paràgrafs breus.
- **Cita directa**: Una cita directa breu integrada al text.
- **Atribució**: Atribució clara: "Segons [persona], '…'".
- **Avaluació de fonts**: Opcional: "Qui ho ha dit? On ho diu el text?".

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Fets clau**: Jerarquitza 3-4 fets per rellevància informativa.
- **Llargada i forma**: Fins a 15 paraules. Clar i informatiu, sense adjectius valoratius.
- **Estil literal**: Sense metàfora. Pot tenir matís però sentit literal.
- **Cobertura 5W**: Cobreix les 5W completes.
- **Llargada de frase**: Frases de fins a 18 paraules.
- **Estructura sintàctica**: Subordinació causal admissible (perquè, ja que).
- **Ordre informatiu**: 3 paràgrafs amb piràmide invertida explícita i transició lògica.
- **Volum del cos**: 3 paràgrafs estructurats.
- **Cita directa**: Una cita directa més una atribució indirecta.
- **Atribució**: Font identificada per a cada dada principal.
- **Avaluació de fonts**: El lector identifica la font de cada dada principal.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Fets clau**: Identifica l'angle informatiu i la selecció editorial.
- **Llargada i forma**: Fins a 18 paraules. Pot incloure un matís causal.
- **Estil literal**: Sense metàfora. Pot tenir matís complex però unívoc.
- **Cobertura 5W**: Cobreix les 5W més un context breu.
- **Llargada de frase**: Frases de fins a 22 paraules.
- **Estructura sintàctica**: Subordinació complexa amb connectors elaborats.
- **Ordre informatiu**: 3-4 paràgrafs amb detall creixent en zones secundàries.
- **Volum del cos**: 3-4 paràgrafs estructurats.
- **Cita directa**: Dues a tres cites amb contrast de punts de vista.
- **Atribució**: Atribució explícita i avaluada per a cada font.
- **Avaluació de fonts**: El lector avalua la credibilitat de cada font i ho explicita al text.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Fets clau**: Analitza la intencionalitat i l'enquadrament ideològic de la peça.
- **Llargada i forma**: Sense límit estricte de paraules; precisió i claredat com a criteri únic.
- **Estil literal**: Llenguatge precís; els jocs de paraules només són admissibles si no comprometen la claredat informativa.
- **Cobertura 5W**: Cobreix 5W més context i implicació informativa.
- **Llargada de frase**: Sense límit estricte; claredat com a criteri únic.
- **Estructura sintàctica**: Sintaxi lliure amb claredat obligatòria.
- **Ordre informatiu**: Estructura de crònica completa amb piràmide flexibilitzada però jerarquitzada.
- **Volum del cos**: Múltiples paràgrafs sense límit estricte.
- **Cita directa**: Múltiples cites amb contrast i jerarquització de credibilitat.
- **Atribució**: Atribució i triangulació explícites; detecció de biaix de selecció.
- **Avaluació de fonts**: El lector contrasta fonts, detecta biaix i analitza l'enquadrament.

