---
tipus: derivat
font_canonic: M3_instrument-generar-glossari.md
font_version: 4.0.0-canonic
vista: C.prompt-adapter-llm
generat_at: '2026-06-11'
generat_per: build_skills.py@prototip-2026-05-24
checksum_font: 42ff043b336a1ad2
---

# Generar glossari — prompt d'adaptació parametritzat per nivell

Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).

## Plantilla

```
Adapta el text font següent al gènere generar glossari per a un alumne de nivell {{NIVELL}} ({{ETIQUETA_MALL}}).

Segueix aquests criteris (extrets de la rúbrica canònica):

{{LLISTA_DESCRIPTORS_DEL_NIVELL}}

Criteris transversals (cal complir a tots els nivells):
{{LLISTA_CRITERIS_TRANSVERSALS}}

Text font:
{{TEXT_FONT}}
```

## Llistes per nivell (per a substitució)

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a pre-A1 (Emergent)

- **Nombre**: 3-5 termes.
- **Tipologia lèxica**: Objectes reals i noms concrets. Sense tecnicismes.
- **Estructura**: Emoji o pictograma + terme en negreta. Sense taula (massa complexa).
- **Suport visual**: Pictograma obligatori a cada terme. L'adult pot complementar amb imatge real.
- **Llargada**: Fins a 6 paraules. Paraules molt freqüents.
- **Recursos pedagògics**: Paraules immediates de l'experiència de l'alumne.
- **Inclusió L1**: Afegeix el terme en L1 amb alfabet original (àrab, xinès, urdú, ciríl·lic, armeni…).
- **Notes contrastives**: Sense notes. La imatge és el pont.
- **No-circularitat**: El terme no apareix dins de la pròpia definició a cap nivell.
- **No-recursivitat**: La definició no usa cap paraula més tècnica que el terme mateix.
- **Llengua de definició**: Llengua de SORTIDA del text adaptat (català, castellà, anglès…). **MAI** usis termes d'una altra llengua com a fallback ni dins la definició. La L1 (si existeix) va a la columna pròpia, NO dins la cel·la d'explicació.
- **Selecció pertinent**: Cap connector, cap nom propi excepte si és clau per a la matèria, cap paraula quotidiana òbvia (excepte a Emergent on els objectes concrets sí entren).
- **Fidelitat al text font**: Tots els termes del glossari apareixen literalment al text adaptat (fidelitat al lèxic nuclear del text).
- **Reflexió sobre el procés**: "He mirat les imatges del glossari quan al text he trobat una paraula que no he reconegut."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A1 (Inicial)

- **Nombre**: 5-8 termes.
- **Tipologia lèxica**: Noms i verbs d'acció principals del text.
- **Estructura**: Taula de 2 columnes: Terme | Explicació.
- **Suport visual**: Emoji recomanat si el terme té representació visual clara.
- **Llargada**: Fins a 8 paraules en català molt senzill (A1).
- **Recursos pedagògics**: Català A1 sense tecnicismes dins la definició. No repetir el terme.
- **Inclusió L1**: Columna addicional "Traducció (L1)" en alfabet original. Taula de 3 columnes.
- **Notes contrastives**: Sense notes. La traducció directa és el pont.
- **No-circularitat**: El terme no apareix dins de la pròpia definició a cap nivell.
- **No-recursivitat**: La definició usa només vocabulari A1 (mai termes més complexos sense explicar-los).
- **Llengua de definició**: Idem (llengua de sortida).
- **Selecció pertinent**: Idem. **Exclou explícitament a A1 + etapa primària inicial**: objectes domèstics (mitja, botó, agulla, fil, retolador, llapis, paper, plat, got, casa, taula, porta), parts del cos (cap, mà, ulls, boca, peu), verbs d'acció bàsics (posar, lligar, dibuixar, jugar, mirar, fer). Aquests són **coneixement previ**, no termes a explicar. Si el text no en conté CAP de realment nou per al nivell, escriu només la nota «Aquest text no necessita glossari nou per al teu nivell» sense taula.
- **Fidelitat al text font**: Tots els termes apareixen literalment al text adaptat.
- **Reflexió sobre el procés**: "Quan llegint el text he trobat una paraula difícil, he anat al glossari a buscar-la abans de demanar ajuda."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a A2 (Funcional)

- **Nombre**: 8-10 termes.
- **Tipologia lèxica**: Noms + verbs + adjectius clau.
- **Estructura**: Taula de 2 columnes; pot afegir una analogia o exemple integrat.
- **Suport visual**: Emoji opcional per a termes concrets; no per a abstractes.
- **Llargada**: Fins a 10 paraules.
- **Recursos pedagògics**: Pot incloure una analogia simple ("és com…") o un exemple concret del text.
- **Inclusió L1**: Columna addicional. Si no existeix paraula exacta en L1, usar la més propera amb aclariment breu.
- **Notes contrastives**: Aclariment breu quan no hi ha equivalent exacte.
- **No-circularitat**: El terme no apareix dins de la pròpia definició a cap nivell.
- **No-recursivitat**: Pot usar termes d'A2 màx.; tecnicismes només si s'expliquen integrats.
- **Llengua de definició**: Idem.
- **Selecció pertinent**: Idem.
- **Fidelitat al text font**: Tots els termes apareixen literalment al text adaptat.
- **Reflexió sobre el procés**: "He fet servir el glossari per entendre el text. He intentat dir el significat amb les meves paraules a algú."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B1 (Estratègic)

- **Nombre**: 10-12 termes.
- **Tipologia lèxica**: Inclou habilitats cognitives lèxicament marcades (hipòtesi, causa, conseqüència).
- **Estructura**: Taula de 2 columnes; **ordre alfabètic** dels termes; pot afegir una tercera columna "Exemple en frase".
- **Suport visual**: Referència opcional a la il·lustració del text si n'hi ha.
- **Llargada**: Fins a 12 paraules.
- **Recursos pedagògics**: Pot usar vocabulari lleugerament tècnic acompanyat d'un exemple.
- **Inclusió L1**: Columna addicional. Pot afegir nota sobre diferències conceptuals entre L1 i català.
- **Notes contrastives**: Notes conceptuals quan la categoria L1 difereix de la del català.
- **No-circularitat**: El terme no apareix dins de la pròpia definició a cap nivell.
- **No-recursivitat**: Pot usar termes B1 màx.; tecnicismes acompanyats d'exemple.
- **Llengua de definició**: Idem.
- **Selecció pertinent**: Idem.
- **Fidelitat al text font**: Tots els termes apareixen al text o són col·locacions necessàries per a la comprensió.
- **Reflexió sobre el procés**: "He reflexionat sobre si sabia usar els termes del glossari en una frase pròpia, i així he sabut quins encara no domino."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a B2 (Acadèmic)

- **Nombre**: 12-15 termes.
- **Tipologia lèxica**: Lèxic d'especialitat (CALP). Inclou col·locacions ("realitzar una hipòtesi").
- **Estructura**: Taula de 2-3 columnes; **ordre alfabètic** obligatori; pot incloure referència creuada interna.
- **Suport visual**: No necessari; el lector processa el terme sense suport visual.
- **Llargada**: Fins a 15 paraules.
- **Recursos pedagògics**: Vocabulari acadèmic (CALP) propi del camp; pot referenciar un altre terme del glossari.
- **Inclusió L1**: Columna addicional. Pot afegir nota sobre diferències morfosintàctiques rellevants.
- **Notes contrastives**: Notes morfosintàctiques o de col·locació quan són rellevants per a la comprensió.
- **No-circularitat**: El terme no apareix dins de la pròpia definició a cap nivell.
- **No-recursivitat**: Pot usar lèxic d'especialitat propi del camp si el lector ja el coneix.
- **Llengua de definició**: Idem.
- **Selecció pertinent**: Idem.
- **Fidelitat al text font**: Termes literals + col·locacions + derivacions conceptualment necessàries.
- **Reflexió sobre el procés**: "He pensat quina diferència hi ha entre els termes del glossari que es poden confondre i com triaria un o l'altre."

### `{{LLISTA_DESCRIPTORS_DEL_NIVELL}}` per a C1+ (Crític)

- **Nombre**: 15-18 termes.
- **Tipologia lèxica**: CALP d'especialitat. Pot incloure termes meta-discursius i lèxic conceptual abstracte.
- **Estructura**: Taula completa; **ordre alfabètic** obligatori; pot incloure etimologia breu o distinció entre termes similars.
- **Suport visual**: No necessari.
- **Llargada**: Fins a 20 paraules.
- **Recursos pedagògics**: Definició precisa amb matís conceptual; pot incloure distinció entre termes similars o etimologia breu.
- **Inclusió L1**: Columna opcional. L'alumne ja pot gestionar el text sense suport explícit en L1.
- **Notes contrastives**: Notes autonomes; pot incloure registre o variació diatòpica si és rellevant.
- **No-circularitat**: El terme no apareix dins de la pròpia definició a cap nivell.
- **No-recursivitat**: Lèxic d'especialitat lliure dins del camp; referència creuada quan calgui.
- **Llengua de definició**: Idem.
- **Selecció pertinent**: Idem (els meta-discursius sí entren).
- **Fidelitat al text font**: Termes literals + col·locacions + derivacions + termes conceptualment connectats que amplien la xarxa lèxica del camp.
- **Reflexió sobre el procés**: "He reflexionat sobre com s'usaria el terme en un altre context i si la definició encara seria vàlida."

