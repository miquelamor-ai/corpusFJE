"""build_matriu_cobertura.py — generador determinista de matriu_cobertura.json.

Mòdul germà de build_rubrica.py / build_skills.py. SENSE LLM.

Llegeix la secció "## Matriu de cobertura perfil × complement" del
M2_instruments-mediacio-pedagogica.md (font canon única) i n'extreu:
  - complement_keys (ordre canon de les 12 columnes)
  - base (condició → complements pre-marcats)
  - visual_need_conditions
  - primaria_inicial_cursos
  - rules (mecr_bands + R1/R2/R3 + fallback + R4 + A5)

El JSON resultant codifica les DUES capes (base + lleis operatives) en forma
DECLARATIVA: el consumidor (ATNE) aplica les regles segons el camp `algoritme`,
NO s'expandeixen aquí les combinacions perfil×MECR×curs. El round-trip 711 es
valida a test_matriu_cobertura.py contra el golden snapshot d'ATNE.

Regla fundacional (feedback-extraccio-determinista-font-unica): tot camp prové
del M2; res s'inventa. La detecció runtime de "nouvingut amb L1" (per a A5) és
excepció pactada que viu al codi consumidor, no aquí.

Ús:
    python build_matriu_cobertura.py <M2.md> [--out <dir>] [--stdout]
    # Per defecte --out = .tooling/ (al costat de build_rubrica.py)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

VERSION = "1.0"
BUILD_TAG = "build_matriu_cobertura.py@v1.0-2026-06-01"

# Títol exacte de la secció canònica al M2 (és contracte amb el M2).
SECTION_TITLE = "Matriu de cobertura perfil × complement"


# =======================================================================
# Utilitats de parsing
# =======================================================================


def _relative_to_corpusfje(path: Path) -> str:
    """Retorna path relatiu a corpusFJE/ per al camp source."""
    parts = path.parts
    if "corpusFJE" in parts:
        idx = parts.index("corpusFJE")
        return "/".join(parts[idx + 1:])
    return path.name


def _extract_section(md: str, title: str) -> str:
    """Retorna el cos d'una secció H2 (## title) fins al següent H2 o EOF."""
    pattern = re.compile(
        rf"^##\s+{re.escape(title)}\s*\n(.*?)(?=^##\s+|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(md)
    if not m:
        raise ValueError(f"No s'ha trobat la secció '## {title}' al M2.")
    return m.group(1)


def _extract_subsection(section: str, h3_title: str) -> str:
    """Retorna el cos d'una subsecció H3 (### title) fins al següent H3 o EOF."""
    pattern = re.compile(
        rf"^###\s+{re.escape(h3_title)}\s*\n(.*?)(?=^###\s+|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(section)
    return m.group(1) if m else ""


def _parse_fenced_list(text: str) -> list[str]:
    """Extreu una llista de tokens d'un bloc ``` fenced ``` separats per
    coma, '·' o salt de línia. Conserva l'ordre, dedup preservant ordre."""
    m = re.search(r"```\s*\n(.*?)```", text, re.DOTALL)
    if not m:
        return []
    raw = m.group(1)
    tokens = re.split(r"[,·\n]+", raw)
    out: list[str] = []
    for t in tokens:
        t = t.strip()
        if t and t not in out:
            out.append(t)
    return out


def _parse_codi_table(text: str, col_value: int = 1) -> dict[str, list[str]]:
    """Parseja una taula markdown amb 1a columna = clau (entre backticks) i
    una columna de valors amb tokens separats per '·'. Salta capçalera i
    separador. Retorna {clau: [tokens]}.
    """
    result: dict[str, list[str]] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < col_value + 1:
            continue
        key_cell = cells[0]
        # Salta capçalera ('Condició') i separador ('---')
        if set(key_cell) <= set("-: "):
            continue
        m = re.search(r"`([^`]+)`", key_cell)
        if not m:
            continue
        key = m.group(1).strip()
        val_cell = cells[col_value]
        tokens = [t.strip() for t in val_cell.split("·") if t.strip()]
        result[key] = tokens
    return result


def _complements_in(text: str, complement_keys: list[str]) -> list[str]:
    """Retorna els complement_keys que apareixen com a paraula al text,
    en ordre canònic de complement_keys (estable)."""
    found = []
    for ck in complement_keys:
        if re.search(rf"`?\b{re.escape(ck)}\b`?", text):
            found.append(ck)
    return found


def _efecte_line(law_text: str) -> str:
    """Retorna NOMÉS la línia '*Efecte*: ...' d'una llei.

    Crucial per determinisme: el cos d'una llei conté també '*Condició*' i
    '*Fonament*' que poden mencionar complements en sentit negatiu (p.ex. R4
    explica que 'el glossari afegiria càrrega'). Extreure complements de tot el
    cos els capturaria erròniament. L'efecte real només viu a la línia *Efecte*.
    """
    m = re.search(r"\*Efecte\*\s*:?\s*(.+?)(?:\n|$)", law_text)
    return m.group(1) if m else ""


def _law_body(section: str, marker: str) -> str:
    """Extreu el cos d'una llei a partir del seu marcador en negreta
    (p.ex. '**R1 ') fins a la propera llei (**, blockquote o EOF)."""
    pattern = re.compile(
        rf"\*\*{re.escape(marker)}[^\n]*\*\*(.*?)(?=\n\*\*[A-RF]|\n>|\Z)",
        re.DOTALL,
    )
    m = pattern.search(section)
    return m.group(1) if m else ""


# =======================================================================
# Builder principal
# =======================================================================


def build(md_path: Path) -> dict:
    md = md_path.read_text(encoding="utf-8")
    section = _extract_section(md, SECTION_TITLE)

    # ── complement_keys (ordre canon) ──
    ck_block = _extract_subsection(section, "Ordre canònic de les 12 columnes de complement")
    complement_keys = _parse_fenced_list(ck_block)
    if len(complement_keys) != 12:
        raise ValueError(
            f"complement_keys: esperava 12, n'he trobat {len(complement_keys)}: {complement_keys}"
        )

    # ── base (condició → complements) ──
    base_block = _extract_subsection(section, "Matriu base (R0) — condició → complements pre-marcats")
    base = _parse_codi_table(base_block)
    # Valida que cada complement de base és canònic
    for cond, comps in base.items():
        for c in comps:
            if c not in complement_keys:
                raise ValueError(f"base[{cond}]: complement no canònic '{c}'")

    # ── visual_need_conditions ──
    vn_block = _extract_subsection(section, "Condicions amb necessitat visual prioritària")
    visual_need = _parse_fenced_list(vn_block)

    # ── primaria_inicial_cursos ──
    pi_block = _extract_subsection(section, "Cursos de primària inicial")
    primaria_inicial = _parse_fenced_list(pi_block)

    # ── mecr_bands ──
    bands_block = _extract_subsection(section, "Bandes de nivell MECR")
    mecr_bands = {}
    for line in bands_block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        m = re.search(r"`(low|mid|high)`", cells[0])
        if not m:
            continue
        band = m.group(1)
        mecr_bands[band] = [t.strip() for t in cells[1].split("·") if t.strip()]
    for required in ("low", "mid", "high"):
        if required not in mecr_bands:
            raise ValueError(f"mecr_bands sense banda '{required}'")

    # ── lleis operatives ──
    laws_block = _extract_subsection(section, "Lleis operatives — modulació de la matriu base")

    r1 = _law_body(laws_block, "R1")
    r2 = _law_body(laws_block, "R2")
    r3 = _law_body(laws_block, "R3")
    fb = _law_body(laws_block, "Fallback")
    r4 = _law_body(laws_block, "R4")
    a5 = _law_body(laws_block, "A5")
    if not all([r1, r2, r3, fb, r4, a5]):
        missing = [n for n, b in
                   [("R1", r1), ("R2", r2), ("R3", r3), ("Fallback", fb), ("R4", r4), ("A5", a5)]
                   if not b]
        raise ValueError(f"Lleis operatives no trobades al M2: {missing}")

    rules = {
        "mecr_bands": mecr_bands,
        "R1_add_pictos": {
            "when_band": "low",
            "if_any": "visual_need_conditions",
            "add": _complements_in(_efecte_line(r1), complement_keys),
        },
        "R2_drop_maps": {
            "when_band": "low",
            "drop": _complements_in(_efecte_line(r2), complement_keys),
        },
        "R3_drop_glossari_disl": {
            "when_band": "low",
            "if": "disl",
            "unless": ["cat", "tdl"],
            "drop": _complements_in(_efecte_line(r3), complement_keys),
        },
        "fallback": {
            "default": _complements_in(_efecte_line(fb), complement_keys),
        },
        "R4_primaria_inicial": {
            "when_band": "low",
            "no_conditions": True,
            "cursos": "primaria_inicial_cursos",
            "only": _complements_in(_efecte_line(r4), complement_keys),
        },
        "A5_nouvingut_l1": {
            "overrides": "R4",
            "when": "nouvingut_amb_l1",
            "detection": "runtime (excepció pactada — viu al codi consumidor)",
            "result": _complements_in(_efecte_line(a5), complement_keys),
        },
    }

    matriu = {
        "version": VERSION,
        "_meta": {
            "source": _relative_to_corpusfje(md_path) + "#matriu-de-cobertura-perfil--complement",
            "generat_at": date.today().isoformat(),
            "build_tag": BUILD_TAG,
            "validacio_pedagogica": "NotebookLM MALL FJE 2026-05-27 (Opció D)",
        },
        "complement_keys": complement_keys,
        "base": base,
        "visual_need_conditions": visual_need,
        "primaria_inicial_cursos": primaria_inicial,
        "rules": rules,
        "algoritme": (
            "1) Banda MECR via mecr_bands (high = fallback per a buit/desconegut). "
            "2) Base = unió OR de rules.base per cada condició present al perfil. "
            "3) Si banda=low I hi ha alguna condició reconeguda: aplica R1 (afegeix pictos "
            "si visual_need), R2 (treu mapes), R3 (treu glossari si disl pur). "
            "4) Si NO hi ha cap condició reconeguda: parteix de fallback.default; si banda=low "
            "I curs ∈ primaria_inicial_cursos aplica R4 (només preguntes_comprensio), EXCEPTE "
            "si nouvingut amb L1 declarada → A5 (glossari + preguntes_comprensio). "
            "R1–R3 i R4/A5 són mútuament exclusius. Ordre de sortida = complement_keys."
        ),
    }
    return matriu


# =======================================================================
# CLI
# =======================================================================


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("font", type=Path, help="ruta al M2_instruments-mediacio-pedagogica.md")
    ap.add_argument("--out", type=Path, default=None,
                    help="directori de sortida (per defecte: .tooling/ del corpus)")
    ap.add_argument("--stdout", action="store_true",
                    help="escriu el JSON a stdout en lloc de fitxer")
    args = ap.parse_args()

    if not args.font.is_file():
        print(f"ERROR: no existeix {args.font}", file=sys.stderr)
        return 2

    print(f"-> Parsing {args.font.name} (secció '{SECTION_TITLE}')...", file=sys.stderr)
    try:
        matriu = build(args.font)
    except ValueError as e:
        print(f"ERROR de parsing: {e}", file=sys.stderr)
        return 1

    print(f"  complement_keys: {len(matriu['complement_keys'])}", file=sys.stderr)
    print(f"  condicions base: {len(matriu['base'])}", file=sys.stderr)
    print(f"  visual_need: {matriu['visual_need_conditions']}", file=sys.stderr)
    print(f"  lleis: {list(matriu['rules'].keys())}", file=sys.stderr)

    json_text = json.dumps(matriu, indent=2, ensure_ascii=False)

    if args.stdout:
        print(json_text)
        return 0

    out = args.out if args.out else Path(__file__).resolve().parent
    out.mkdir(parents=True, exist_ok=True)
    out_path = out / "matriu_cobertura.json"
    out_path.write_text(json_text, encoding="utf-8")
    print(f"  [OK] {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
