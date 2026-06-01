"""build_rubrica.py — generador determinista de rubrica.json des d'un M*.md canonic.

Mòdul germà de build_skills.py. Reutilitza el parser comú (parse_instrument).
Genera un rubrica.json conforme a l'esquema v1.0 FROZEN 2026-06-01
(docs/esquema_rubrica_canonic_v1.md al repo mineriaRAG).

Regla fundacional aplicada: extracció determinista + font única. Tot camp del JSON
prové del M*.md (frontmatter, taula Modulació, taula Metadades, body) o és una
excepció pactada documentada (transliteració, post_edicio_pas3 al codi UI).

Ús:
    python build_rubrica.py <M*.md> [--out <dir>]
    # Per defecte: --out = <dir-del-M*.md>/  (escriu rubrica.json al costat del SKILL.md)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import yaml

# Enum canònic de tipus de pas (segons esquema v1.0)
TIPUS_ENUM = {"binary", "qualitative", "countable", "structural",
              "cross_source", "metacognitive", "enumerable"}


def _deburr(text: str) -> str:
    """Treu accents per a slugs (à→a, è→e, ç→c, etc.)."""
    nfd = unicodedata.normalize("NFD", text)
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn")


def _normalize_tipus(raw: str) -> str:
    """Normalitza 'qualitative` + `enumerable' o '`binary`' a un enum canònic."""
    if not raw:
        return "qualitative"
    cleaned = raw.replace("`", "").lower()
    # Cerca el primer enum vàlid que aparegui
    for valid in ["countable", "binary", "structural", "cross_source",
                  "metacognitive", "enumerable", "qualitative"]:
        if valid in cleaned:
            return valid
    return "qualitative"


def _longest_descriptor(descriptors: dict) -> str:
    """Triar el descriptor més llarg (evita 'Idem.' o '...')."""
    candidates = [(len(d.strip()), d.strip()) for d in descriptors.values() if d and d.strip()]
    if not candidates:
        return ""
    return max(candidates)[1]


def _short_slug(text: str, max_words: int = 4) -> str:
    """Slug humà-llegible: primer N paraules, sense accents."""
    text = _deburr(text)
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return "_".join(words[:max_words])

# Reutilitza el parser comú de build_skills.py
from build_skills import (
    Instrument,
    NIVELLS,
    NIVELL_ETIQUETA,
    extract_section,
    parse_instrument,
    is_no_aplicable,
)

# Esquema versió: actualitzar quan canviï el contracte amb ATNE
RUBRICA_SCHEMA_VERSION = "1.0.0"
BUILD_TAG = "build_rubrica.py@v1.0-2026-06-01"

# Constants compartides amb ATNE
FAMILIES_CANONIQUES = {"mediacio", "generes", "adaptacio", "bastida", "avaluacio"}

# Llista canònica d'alfabets no llatins (codis ISO 639-3 + ISO 15924).
# Font: docs/transliteracio_standards_l1_2026-05-31.md v1.1
# Per a v1.1+ externalitzar a corpusFJE/canon/alfabets_no_llatins.json
ALFABETS_NO_LLATINS_ISO = [
    "ar-Arab",   # àrab estàndard
    "ar-MA-Arab", # darija marroquí (variant)
    "zgh-Tfng",  # amazic en Tifinagh (variant llatí NO necessita translit)
    "fa-Arab",   # persa/farsi
    "ur-Arab",   # urdú
    "zh-Hans",   # xinès simplificat
    "zh-Hant",   # xinès tradicional
    "pa-Guru",   # pendjabi en Gurmukhi
    "hi-Deva",   # hindi en Devanagari
    "bn-Beng",   # bengalí
    "ru-Cyrl",   # rus
    "uk-Cyrl",   # ucraïnès
    "bg-Cyrl",   # búlgar
    "ja-Jpan",   # japonès
    "ko-Hang",   # coreà
    "he-Hebr",   # hebreu
    "th-Thai",   # tai
    "am-Ethi",   # amhàric
    "hy-Armn",   # armeni
    "ka-Geor",   # georgià
]


# =======================================================================
# Builders per bloc de l'esquema
# =======================================================================


def _build_meta(instrument: Instrument, font_path: Path) -> dict:
    """Construeix _meta des del frontmatter + path."""
    fm = instrument.frontmatter
    skill_name = font_path.parent.name

    # family: del frontmatter o inferit del path (skills/<family>/<skill>/)
    family = fm.get("family") or fm.get("categoria_principal")
    if not family:
        # Heurística: skills/<family>/<skill>/M*.md
        try:
            family = font_path.parent.parent.name
        except IndexError:
            family = "mediacio"
    if family not in FAMILIES_CANONIQUES:
        # Normalitza valors antics
        if family == "instrument":
            family = "mediacio"
        elif family == "genere":
            family = "generes"

    meta = {
        "name": f"rubrica_{skill_name.replace('-', '_')}",
        "version": RUBRICA_SCHEMA_VERSION,
        "font_canonic": _relative_to_corpusfje(font_path),
        "font_version": str(fm.get("version", "unknown")),
        "generat_at": date.today().isoformat(),
        "skill_name": skill_name,
        "family": family,
    }

    # Propaga camps opcionals del frontmatter
    for k in ("mecr_range", "agent_roles", "complement_key", "genre_key",
              "translanguaging", "multimodal", "variables_configurables"):
        if k in fm:
            meta[k] = fm[k]

    # Camps opcionals des del body
    if estrategia := extract_section(instrument.body, "Estratègia"):
        meta["estrategia"] = estrategia.split("\n")[0].strip()
    if us := extract_section(instrument.body, "Ús operatiu"):
        meta["us"] = us.split("\n")[0].strip()

    return meta


def _relative_to_corpusfje(path: Path) -> str:
    """Retorna path relatiu a corpusFJE/ (per a font_canonic)."""
    parts = path.parts
    if "corpusFJE" in parts:
        idx = parts.index("corpusFJE")
        return "/".join(parts[idx + 1:])
    return str(path)


def _build_transversals(instrument: Instrument) -> dict:
    """Extreu transversals des de la secció corresponent + Format de sortida."""
    transversals = {}

    # Secció "Criteris transversals" o "Regles transversals"
    body = instrument.body
    for header in ("Criteris transversals", "Regles transversals"):
        if section := extract_section(body, header):
            transversals.update(_parse_transversals_section(section))
            break

    # Cel·les del pas 5 "Criteris transversals" de la taula Modulació
    # (alguns skills ho tenen com a pas dins la taula, no com a secció separada)
    transversals_from_celles = _extract_transversals_from_celles(instrument)
    for k, v in transversals_from_celles.items():
        transversals.setdefault(k, v)

    # Format de sortida
    if fmt := _build_format_output(instrument):
        transversals["format_output"] = fmt

    return transversals


def _parse_transversals_section(section: str) -> dict:
    """Parser de bullets dins una secció de criteris transversals.

    Format esperat (variants):
        - **No-circularitat**: el terme no apareix dins la pròpia definició.
        - **Fidelitat al text font**: tots els termes del glossari apareixen literalment...

    Mapping a noms canònics del JSON: {bullet → camp transversal}.
    """
    transversals = {}
    bullets = re.findall(r"^[-*]\s+\*\*(.+?)\*\*[:.]?\s*(.+?)(?=\n[-*]|\Z)",
                        section, re.DOTALL | re.MULTILINE)
    for label, content in bullets:
        canonical = _normalize_transversal_name(label)
        if not canonical:
            continue
        rule = content.strip().replace("\n", " ")
        transversals[canonical] = {
            "type": _infer_transversal_type(canonical),
            "rule": rule,
        }
    return transversals


def _normalize_transversal_name(label: str) -> str | None:
    """Mapeig de labels humans a noms canònics del JSON."""
    label_low = label.lower().strip()
    mapping = {
        "no-circularitat": "no_circularitat",
        "no circularitat": "no_circularitat",
        "no-recursivitat": "no_recursivitat",
        "llengua de definició": "llengua_definicio",
        "llengua de la definició": "llengua_definicio",
        "fidelitat al text font": "fidelitat_text_font",
        "fidelitat text font": "fidelitat_text_font",
        "selecció pertinent": "seleccio_pertinent",
        "separació de blocs": "separacio_blocs",
    }
    for key, val in mapping.items():
        if key in label_low:
            return val
    return None


def _infer_transversal_type(name: str) -> str:
    """Tipus per defecte segons el camp transversal."""
    if name in ("fidelitat_text_font", "seleccio_pertinent"):
        return "cross_source"
    if name in ("no_circularitat", "llengua_definicio", "no_recursivitat"):
        return "binary"
    return "structural"


def _extract_transversals_from_celles(instrument: Instrument) -> dict:
    """Si la taula Modulació té un pas de Criteris transversals (típic glossari),
    extreu les regles des de les cel·les. Pren el descriptor MÉS LLARG per evitar
    'Idem.' que apareix quan els nivells alts repeteixen el pre-A1."""
    transversals = {}
    for c in instrument.celles:
        pas_low = c.pas.lower()
        if "criteris transversals" not in pas_low and "transversals" not in pas_low:
            continue
        canonical = _normalize_transversal_name(c.dimensio)
        if not canonical:
            continue
        # Pren el descriptor més llarg (evita 'Idem.' a nivells alts)
        descriptor = _longest_descriptor(c.descriptors)
        if descriptor and not is_no_aplicable(descriptor):
            transversals[canonical] = {
                "type": _infer_transversal_type(canonical),
                "rule": descriptor,
            }
    return transversals


def _build_format_output(instrument: Instrument) -> dict | None:
    """Extreu format_output de la secció Format de sortida (literals H2/H3)."""
    section = extract_section(instrument.body, "Format de sortida")
    if not section:
        return None

    fmt = {"type": "structural"}

    # H2 literals (cerca patrons `## ...` entre backticks o en bullets)
    h2_matches = re.findall(r"`(##\s+[^`\n]+)`", section)
    h3_matches = re.findall(r"`(###\s+[^`\n]+)`", section)
    if h2_matches:
        fmt["h2_exact"] = h2_matches if len(h2_matches) > 1 else h2_matches[0]
    if h3_matches:
        fmt["h3_exact"] = h3_matches

    # Regla literal en prosa
    first_line = section.split("\n")[0].strip()
    if first_line and not first_line.startswith(("#", "-", "*", "`")):
        fmt["rule"] = first_line

    return fmt if len(fmt) > 1 else None


def _build_levels(instrument: Instrument) -> dict:
    """Construeix levels.{MECR} amb passos[] per cada nivell."""
    levels = {}
    for nivell in NIVELLS:
        level_block = {
            "etiqueta": NIVELL_ETIQUETA[nivell],
            "passos": [],
        }
        for c in instrument.celles:
            descriptor = c.descriptors.get(nivell, "").strip()
            if not descriptor or is_no_aplicable(descriptor):
                continue
            pas_meta = {
                "pas_id": _pas_id_from_pas(c.pas, c.dimensio),
                "descriptor": descriptor,
            }
            if countable := _extract_countable(descriptor):
                pas_meta["countable"] = countable
            level_block["passos"].append(pas_meta)
        levels[nivell] = level_block
    return levels


def _pas_id_from_pas(pas: str, dimensio: str) -> str:
    """Genera pas_id canonic: 'pas_N' o '<paslow>_<dimlow>' si vol semàntic."""
    m = re.match(r"^(\d+)", pas.strip())
    if m:
        pas_num = m.group(1)
        dim_slug = _short_slug(dimensio, max_words=3)
        return f"pas_{pas_num}_{dim_slug}" if dim_slug else f"pas_{pas_num}"
    # Sense numèric: usa el primer mot deburrejat
    slug = _short_slug(pas, max_words=2)
    return slug or "pas_0"


def _extract_countable(descriptor: str) -> dict | None:
    """Extreu min/max + unitat d'un descriptor amb números.

    Exemples:
        "3-5 termes" → {min:3, max:5, unitat:'terms'}
        "Fins a 6 paraules" → {max:6, unitat:'paraules'}
        "5 preguntes" → {min:5, max:5, unitat:'items'}
    """
    # "X-Y unitat" o "X a Y unitat"
    m = re.search(r"(\d+)\s*[-a]\s*(\d+)\s*(termes?|paraules|frases|items?|nodes|connectors|iniciadors|branques|torns|paràgrafs|criteris)", descriptor, re.IGNORECASE)
    if m:
        return {
            "min": int(m.group(1)),
            "max": int(m.group(2)),
            "unitat": _normalize_unitat(m.group(3)),
        }
    # "Fins a X unitat"
    m = re.search(r"[Ff]ins a (\d+)\s*(termes?|paraules|frases|items?|nodes|connectors|iniciadors|branques)", descriptor)
    if m:
        return {
            "max": int(m.group(1)),
            "unitat": _normalize_unitat(m.group(2)),
        }
    # "X unitat" (valor únic)
    m = re.search(r"^(\d+)\s+(termes?|paraules|frases|items?|nodes|connectors|iniciadors|branques)", descriptor)
    if m:
        n = int(m.group(1))
        return {"min": n, "max": n, "unitat": _normalize_unitat(m.group(2))}
    return None


def _normalize_unitat(raw: str) -> str:
    """Normalitza unitat a l'enum canònic."""
    raw_low = raw.lower().rstrip("s")
    mapping = {
        "terme": "terms",
        "paraule": "paraules",
        "frase": "frases",
        "item": "items",
        "node": "nodes",
        "connector": "connectors",
        "iniciador": "iniciadors",
        "branque": "branques",
        "torn": "torns",
        "paràgraf": "parraps",
        "criteri": "criteris",
    }
    return mapping.get(raw_low, raw_low + "s")


def _build_passos_meta(instrument: Instrument) -> list:
    """Construeix passos_meta des de les cel·les amb metadades."""
    passos_meta = []
    seen = set()
    for c in instrument.celles:
        pas_id = _pas_id_from_pas(c.pas, c.dimensio)
        if pas_id in seen:
            continue
        seen.add(pas_id)
        entry = {
            "id": pas_id,
            "titol": _clean_pas_title(c.pas),
            "dimensio": c.dimensio,
            "tipus": _normalize_tipus(c.tipus),
        }
        if c.requires_source:
            entry["requires_source_text"] = c.requires_source.lower() in ("sí", "si", "yes", "true", "parcial")
        if c.validation_hint:
            entry["validation_hint"] = c.validation_hint
        passos_meta.append(entry)
    return passos_meta


def _clean_pas_title(pas: str) -> str:
    """Treu numeració i format del títol del pas."""
    title = re.sub(r"^\d+\.\s*", "", pas).strip()
    return re.sub(r"\*\*", "", title).strip()


# =======================================================================
# Opcionals — només si la secció existeix al M*.md
# =======================================================================


def _extract_principi_general(instrument: Instrument) -> dict | None:
    section = extract_section(instrument.body, "Principi general")
    if not section:
        return None
    # Format esperat: paràgrafs amb **Label** o **Label.** o **Label:** a inici
    # (workflow Fase 2 normalització els escriu així, no com a bullets).
    # Captura: **label** seguit de qualsevol cosa fins a doble salt de línia o final.
    paragraphs = re.findall(
        r"^\*\*(.+?)\*\*\s*(.+?)(?=\n\n\*\*|\n\n_|\n\n##|\Z)",
        section, re.DOTALL | re.MULTILINE
    )
    result = {}
    for label, content in paragraphs:
        label_low = label.lower()
        content = content.strip().replace("\n", " ")
        if "regla" in label_low and ("selecció" in label_low or "simple" in label_low):
            result["regla_seleccio_simple"] = content
        elif "límit" in label_low or "judici" in label_low or "no decideix" in label_low:
            result["no_judici_qualitatiu_complex"] = content
    return result or None


def _extract_regla_seleccio_per_perfil(instrument: Instrument) -> dict | None:
    section = extract_section(instrument.body, "Regla de selecció per perfil")
    if not section:
        return None
    # Format esperat: subseccions per perfil amb ### nom + bullets
    # Accepta variants de capçalera amb dos punts DINS o FORA dels asteriscos:
    # **Inclou si:**, **Inclou si**:, **Inclou si**.
    perfils = {}
    for match in re.finditer(r"^###\s+(.+?)\n(.*?)(?=^###|\Z)",
                              section, re.DOTALL | re.MULTILINE):
        perfil = match.group(1).strip()
        body = match.group(2).strip()
        entry = {}
        # Patró flexible: **Label** o **Label:** o **Label.** o **Label**:
        if inclou := re.search(
            r"\*\*Inclou si[:.]?\*\*[:.]?\s*\n?((?:[-*]\s+.+?\n?)+)",
            body, re.IGNORECASE
        ):
            entry["inclou_si"] = _parse_bullets(inclou.group(1))
        if exclou := re.search(
            r"\*\*Exclou(?:\s+expl[ií]citament)?[:.]?\*\*[:.]?\s*\n?((?:[-*]\s+.+?\n?)+)",
            body, re.IGNORECASE
        ):
            entry["exclou_explicitament"] = _parse_bullets(exclou.group(1))
        if raonament := re.search(
            r"\*\*Raonament(?:\s+pedag[oò]gic)?[:.]?\*\*[:.]?\s*(.+?)(?=\n\n\*\*|\n\n##|\n\n###|\Z)",
            body, re.DOTALL | re.IGNORECASE
        ):
            entry["raonament"] = raonament.group(1).strip().replace("\n", " ")
        if entry:
            perfils[perfil] = entry
    return perfils or None


def _parse_bullets(text: str) -> list:
    return [re.sub(r"^[-*]\s+", "", line).strip()
            for line in text.split("\n")
            if line.strip().startswith(("-", "*"))]


def _extract_senyals(instrument: Instrument, mode: str) -> list:
    """mode='activacio' → 'Quan aplicar-ho' / 'Senyals docent'.
       mode='anti'     → 'Quan NO aplicar-ho' / 'Anti-senyals'."""
    headers = ("Quan aplicar-ho", "Senyals docent") if mode == "activacio" else ("Quan NO aplicar-ho", "Anti-senyals")
    section = ""
    for header in headers:
        if section := extract_section(instrument.body, header):
            break
    if not section:
        # Fallback: cerca dins "## Detecció"
        deteccio = extract_section(instrument.body, "Detecció")
        if not deteccio:
            return []
        sub_header = "Senyals docent" if mode == "activacio" else "Anti-senyals"
        m = re.search(rf"\*\*{sub_header}.*?\*\*.*?\n((?:[-*]\s+.+?\n)+)",
                      deteccio, re.DOTALL | re.IGNORECASE)
        section = m.group(1) if m else ""
    bullets = _parse_bullets(section)
    return [{"name": _short_slug(b, max_words=4), "description": b} for b in bullets if b]


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", _deburr(text).lower()).strip("_")


def _extract_heuristiques(instrument: Instrument) -> list:
    if not instrument.heuristiques:
        return []
    heur = []
    for match in re.finditer(r"\*\*(H\d+)\s*[—–-]\s*(.+?)\*\*\s*\n+(.+?)(?=\n\n\*\*H\d+|\Z)",
                              instrument.heuristiques, re.DOTALL):
        heur.append({
            "id": match.group(1),
            "titol": match.group(2).strip(),
            "descripcio": match.group(3).strip().replace("\n", " "),
        })
    return heur


def _extract_case_overrides(instrument: Instrument) -> dict | None:
    section = extract_section(instrument.body, "Casos especials")
    if not section:
        section = extract_section(instrument.body, "Case overrides")
    if not section:
        return None
    cases = {}
    for match in re.finditer(r"^###\s+(.+?)\n(.*?)(?=^###|\Z)",
                              section, re.DOTALL | re.MULTILINE):
        nom = _slugify(match.group(1))
        body = match.group(2).strip()
        # Per ara, captura tot el body com a descriptor; estructuració fina post-pilot
        cases[nom] = {
            "trigger": {"raw": match.group(1).strip()},
            "modulacio": {"descripcio": body[:500]},
        }
    return cases or None


def _extract_checks_automatics(instrument: Instrument) -> list:
    """Genera checks_automatics_post_generacio des de les metadades amb hints regex."""
    checks = []
    for c in instrument.celles:
        if not c.validation_hint:
            continue
        hint = c.validation_hint.lower()
        check = None
        if c.tipus == "binary" and ("regex" in hint or "no apareix" in hint):
            check = {
                "name": _slugify(c.dimensio)[:40],
                "type": "qualitative",  # POLÍTICA NO INVENCIÓ: si el M3 no porta regex literal, queda qualitative
                "rule": c.validation_hint,
            }
        elif c.tipus == "structural":
            check = {
                "name": _slugify(c.dimensio)[:40],
                "type": "qualitative",
                "rule": c.validation_hint,
            }
        elif c.tipus == "countable":
            check = {
                "name": _slugify(c.dimensio)[:40],
                "type": "countable",
                "uses_field": f"levels.<mecr>.passos[{_pas_id_from_pas(c.pas, c.dimensio)}].countable",
            }
        if check:
            checks.append(check)
    return checks


def _extract_post_edicio_pas3(instrument: Instrument) -> dict | None:
    """post_edicio_pas3 és EXCEPCIÓ PACTADA: viu al codi UI ATNE com a decisió de
    producte, NO al M*.md. Per al cas glossari (l'únic que el necessita), s'inclou
    hardcoded al rubrica.json amb la llista canònica de 4 toggles + filosofia."""
    fm = instrument.frontmatter
    if fm.get("complement_key") != "glossari":
        return None
    return {
        "valvula_humana": True,
        "accions_disponibles_per_docent": [
            "toggle_columna_CA",
            "toggle_columna_pictograma",
            "toggle_columna_L1",
            "toggle_columna_transliteracio",
            "eliminar_entry",
            "afegir_entry",
            "editar_definicio",
        ],
        "comportament_toggles": "Toggles operen client-side amb columnes ja generades pel LLM. Si el docent desactiva una columna, s'amaga al render i s'exclou de l'export PDF.",
        "filosofia": "ATNE proposa, docent decideix. La lògica de defaults condicionals per perfil (quan cada toggle està ON o OFF) viu al codi UI ATNE com a excepció pactada (no canonitzable al JSON).",
    }


def _get_alfabets_no_llatins(instrument: Instrument) -> list | None:
    """Inclou només si l'skill té translanguaging=true o complement_key=glossari."""
    fm = instrument.frontmatter
    if fm.get("translanguaging") or fm.get("complement_key") == "glossari":
        return ALFABETS_NO_LLATINS_ISO
    return None


# =======================================================================
# Funció principal
# =======================================================================


def generar_rubrica_json(instrument: Instrument, font_path: Path) -> dict:
    """Genera rubrica.json canonic v1.0 des d'un Instrument parsejat."""
    rubrica = {
        "_meta": _build_meta(instrument, font_path),
        "transversals": _build_transversals(instrument),
        "levels": _build_levels(instrument),
        "passos_meta": _build_passos_meta(instrument),
    }
    # Opcionals (només si la secció existeix al M*.md)
    if principi := _extract_principi_general(instrument):
        rubrica["principi_general"] = principi
    if perfil := _extract_regla_seleccio_per_perfil(instrument):
        rubrica["regla_seleccio_per_perfil"] = perfil
    if senyals := _extract_senyals(instrument, "activacio"):
        rubrica["senyals_activacio"] = senyals
    if anti := _extract_senyals(instrument, "anti"):
        rubrica["anti_senyals"] = anti
    if heur := _extract_heuristiques(instrument):
        rubrica["heuristiques_docent"] = heur
    if cases := _extract_case_overrides(instrument):
        rubrica["case_overrides"] = cases
    if checks := _extract_checks_automatics(instrument):
        rubrica["checks_automatics_post_generacio"] = checks
    if post := _extract_post_edicio_pas3(instrument):
        rubrica["post_edicio_pas3"] = post
    if alfabets := _get_alfabets_no_llatins(instrument):
        rubrica["alfabets_no_llatins_que_activen_translit"] = alfabets

    return rubrica


# =======================================================================
# CLI
# =======================================================================


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("font", type=Path, help="ruta al M*.md canònic")
    ap.add_argument("--out", type=Path, default=None,
                    help="directori de sortida (per defecte: <dir-font>/)")
    ap.add_argument("--stdout", action="store_true",
                    help="escriu rubrica.json a stdout en lloc de fitxer")
    args = ap.parse_args()

    if not args.font.is_file():
        print(f"ERROR: no existeix {args.font}", file=sys.stderr)
        return 2

    print(f"-> Parsing {args.font.name}...", file=sys.stderr)
    instrument = parse_instrument(args.font)
    print(f"  Frontmatter: {len(instrument.frontmatter)} camps", file=sys.stderr)
    print(f"  Cel.les modulacio: {len(instrument.celles)}", file=sys.stderr)

    rubrica = generar_rubrica_json(instrument, args.font)
    json_text = json.dumps(rubrica, indent=2, ensure_ascii=False)

    if args.stdout:
        print(json_text)
        return 0

    out = args.out if args.out else args.font.parent
    out.mkdir(parents=True, exist_ok=True)
    rubrica_path = out / "rubrica.json"
    rubrica_path.write_text(json_text, encoding="utf-8")
    print(f"  [OK] {rubrica_path}", file=sys.stderr)
    print(f"  blocs presents: {list(rubrica.keys())}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
