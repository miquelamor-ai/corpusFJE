---
tipus: derivat
font_canonic: M3_genere-escriure-instructiu.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-11'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 3d1e320968642a3f
---

# Escriure/adaptar un text instructiu — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere escriure/adaptar un text instructiu per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Completitud i ordre**: Llista de 3-5 materials. Sense quantitats. 1 material per línia.
- **Claredat i precisió**: Passos numerats. 1 verb + 1 objecte. ≤5 paraules per pas.
- **Independència operativa**: Cada pas s'executa sense mirar el pas següent. Cap referència implícita.
- **Rigor processal**: Ordre d'execució respectat. No reordenar per legibilitat.
- **Verificabilitat**: 1 frase: qué s'ha aconseguit. Com es nota que ha sortit bé.
- **No instruccions en passiva**: Cap instrucció en passiva. "Afegeix l'agua" (no "S'afegirà l'agua"). Imperatiu consistent.
- **No condicionals niats**: Cap condicional ("si X, fes Y"). Linealitat estricta.
- **Fidelitat al text font**: Fidelitat al procés principal i a l'ordre dels passos.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Completitud i ordre**: Llista de 4-6 materials amb quantitats bàsiques ("1 tassa", "2 ous").
- **Claredat i precisió**: Passos numerats. 1 verb + 1 objecte concret. ≤8 paraules per pas.
- **Independència operativa**: Cada pas independent. Sense "després de fer el pas anterior".
- **Rigor processal**: Ordre processal estricte. L'ordre és estructuralment obligatori.
- **Verificabilitat**: Resultat de 1-2 frases: qué s'obté i com es nota que és correcte.
- **No instruccions en passiva**: Idem. Cap construcció passiva ni impersonal ("s'ha d'afegir").
- **No condicionals niats**: Idem. Condicionals simples admesos en nota al final, no dins dels passos.
- **Fidelitat al text font**: Fidelitat al procés, a l'ordre i als materials essencials.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Completitud i ordre**: Llista completa amb quantitats i especificitats bàsiques. Materials en ordre d'ús.
- **Claredat i precisió**: Passos numerats. 1 verb precís + 1 objecte + context breu si cal.
- **Independència operativa**: Passos estrictament independents. Test: puc fer el pas 3 sense saber el pas 4?
- **Rigor processal**: Ordre cronològic respectat sense excepcions. Cap inversió per "lògica narrativa".
- **Verificabilitat**: Resultat amb les característiques esperades del producte o procés acabat.
- **No instruccions en passiva**: Idem. El subjecte "tu" (implícit) és sempre l'executor.
- **No condicionals niats**: Idem. Alternatives opcionals en nota al final del pas, entre parèntesis.
- **Fidelitat al text font**: Fidelitat al procés, a l'ordre, als materials i als indicadors de qualitat.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Completitud i ordre**: Materials amb quantitats, tipus i condicions si escau. Llista exhaustiva.
- **Claredat i precisió**: Passos numerats. 1-2 accions estretament relacionades per pas. Pot incloure condicions simples.
- **Independència operativa**: Independència total. Cap referència implícita a un pas anterior ni posterior.
- **Rigor processal**: Ordre processal pur. Qualsevol reordenació trencaria el resultat final.
- **Verificabilitat**: Resultat amb criteris de qualitat o avaluació del producte.
- **No instruccions en passiva**: Idem. Pot incloure l'imperatiu de primera plural ("Barregem") si el context és col·lectiu.
- **No condicionals niats**: Idem. Pot incloure bifurcacions simples en paràgraf separat.
- **Fidelitat al text font**: Fidelitat a la complexitat tècnica del procés original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Completitud i ordre**: Materials completament especificats. Alternatives si n'hi ha. Ordenats per fases si el procés és complex.
- **Claredat i precisió**: Passos numerats. Completament autònoms. Precisió tècnica màxima. Pot incloure notes tècniques en cursiva.
- **Independència operativa**: Passos absolutament autònoms i complets en si mateixos. Cap sobreentès.
- **Rigor processal**: Ordre processal rigorós. Pot incloure passos previs de preparació clarament separats.
- **Verificabilitat**: Resultat amb criteris precisos i possibles variacions acceptables.
- **No instruccions en passiva**: Idem. Precisió tècnica màxima amb l'imperatiu adequat al registre professional.
- **No condicionals niats**: Condicionals simples admesos si el context professional ho requereix, però sempre en pas separat.
- **Fidelitat al text font**: Fidelitat a la complexitat, a la precisió tècnica i a les variacions del text original.

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)


