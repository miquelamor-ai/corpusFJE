"""build_per_al_docent.py — generador determinista de per_al_docent.json.

Mòdul germà de build_matriu_cobertura.py / build_rubrica.py. SENSE LLM.

Llegeix la secció "## Taxonomia «Per al docent» — categories d'argumentació" del
M2_instruments-mediacio-pedagogica.md (font canon única) i n'extreu:
  - categories[]            (codi, nom, sub_arees, naturalesa, descripcio)
  - taxonomia_9cat{}        (codi → nom; conveniència per al deep-equal del consumidor)
  - complement_to_categoria{}  (complement → [categories obligatòries])
  - lleis{}                 (sempre A/B/E, H/I/G, metrica_A_paraules_per_mecr)

El JSON resultant és el derivat que consumeix ATNE per a la secció «Per al docent»
(taxonomia + mapeig + lleis hardcoded fins ara a prompt_builder.py / pas3.html /
saber-ne.html). Round-trip validat a test_per_al_docent.py contra el golden snapshot
d'ATNE (tests/golden/per_al_docent_snapshot.json).

Regla fundacional (feedback-extraccio-determinista-font-unica): tot camp prové del M2;
res s'inventa. La detecció runtime de "nouvingut amb L1" (per a la llei G) és excepció
pactada que viu al codi consumidor, no aquí.

Ús:
    python build_per_al_docent.py <M2.md> [--out <dir>] [--stdout]
    # Per defecte --out = .tooling/ (al costat de build_matriu_cobertura.py)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

VERSION = "1.0"
BUILD_TAG = "build_per_al_docent.py@v1.0-2026-06-11"

# Títol exacte de la secció canònica al M2 (és contracte amb el M2).
SECTION_TITLE = "Taxonomia «Per al docent» — categories d'argumentació"


# =======================================================================
# Utilitats de parsing (germanes de build_matriu_cobertura.py)
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


def _table_rows(text: str) -> list[list[str]]:
    """Retorna les files de dades d'una taula markdown (sense capçalera ni
    separador), cada fila com a llista de cel·les ja despullades."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells:
            continue
        # Salta el separador de capçalera (|---|---|) i la capçalera (sense backtick a col0)
        if set(cells[0]) <= set("-: "):
            continue
        rows.append(cells)
    return rows


def _backtick_key(cell: str) -> str | None:
    m = re.search(r"`([^`]+)`", cell)
    return m.group(1).strip() if m else None


# =======================================================================
# Parsers de cada subsecció
# =======================================================================


def _parse_taxonomia(section: str) -> tuple[dict[str, dict], dict[str, str]]:
    """Parseja la taula de 9 categories + els bullets de descripció.

    Retorna (categories_by_code, noms) on categories_by_code[codi] = {
        nom, sub_arees, naturalesa, descripcio
    } i noms[codi] = nom.
    """
    sub = _extract_subsection(section, "Taxonomia de 9 categories A-I")
    if not sub:
        raise ValueError("Falta la subsecció '### Taxonomia de 9 categories A-I'.")

    cats: dict[str, dict] = {}
    for cells in _table_rows(sub):
        if len(cells) < 4:
            continue
        codi = _backtick_key(cells[0])
        if not codi or not re.fullmatch(r"[A-I]", codi):
            continue
        sub_arees = [t.strip() for t in cells[2].split("·") if t.strip()]
        cats[codi] = {
            "nom": cells[1].strip(),
            "sub_arees": sub_arees,
            "naturalesa": cells[3].strip(),
            "descripcio": "",
        }

    # Descripcions: línies "- **A. Nom** — descripció ..."
    for m in re.finditer(r"(?m)^- \*\*([A-I])\.\s*[^*]+\*\*\s*[—–-]\s*(.+)$", sub):
        codi, desc = m.group(1), m.group(2).strip()
        if codi in cats:
            cats[codi]["descripcio"] = desc

    if len(cats) != 9:
        raise ValueError(
            f"Taxonomia: esperava 9 categories A-I, n'he trobat {len(cats)}: {sorted(cats)}"
        )
    for codi in "ABCDEFGHI":
        if codi not in cats:
            raise ValueError(f"Taxonomia: falta la categoria '{codi}'.")
        if not cats[codi]["descripcio"]:
            raise ValueError(f"Taxonomia: la categoria '{codi}' no té descripció (bullet '- **{codi}. …**').")

    noms = {c: cats[c]["nom"] for c in "ABCDEFGHI"}
    return cats, noms


def _parse_mapeig(section: str) -> dict[str, list[str]]:
    """Parseja la taula complement → [categories]. Ordre = ordre del M2."""
    sub = _extract_subsection(section, "Mapeig complement → categoria/es obligatòria/es")
    if not sub:
        raise ValueError("Falta la subsecció '### Mapeig complement → categoria/es obligatòria/es'.")
    mapeig: dict[str, list[str]] = {}
    for cells in _table_rows(sub):
        if len(cells) < 2:
            continue
        comp = _backtick_key(cells[0])
        if not comp:
            continue
        cats = [t.strip() for t in cells[1].split("·") if t.strip()]
        for c in cats:
            if not re.fullmatch(r"[A-I]", c):
                raise ValueError(f"Mapeig[{comp}]: categoria no vàlida '{c}'.")
        mapeig[comp] = cats
    if not mapeig:
        raise ValueError("Mapeig complement→categoria buit.")
    return mapeig


def _parse_lleis(section: str) -> dict:
    """Parseja la subsecció de lleis: sempre A/B/E, H/I/G, mètrica MECR."""
    sub = _extract_subsection(section, "Lleis d'obligatorietat de categoria")
    if not sub:
        raise ValueError("Falta la subsecció '### Lleis d'obligatorietat de categoria'.")

    # ── sempre (de la línia "- **Sempre A, B, E** ...") ──
    m = re.search(r"(?m)^- \*\*Sempre\s+([^*]+)\*\*", sub)
    if not m:
        raise ValueError("Lleis: no trobo la línia '- **Sempre …**'.")
    sempre = re.findall(r"[A-I]", m.group(1))
    if sempre != ["A", "B", "E"]:
        raise ValueError(f"Lleis: 'sempre' esperava [A, B, E], he llegit {sempre}.")

    # ── lleis condicionals H/I/G (presència del marcador en negreta) ──
    h_law = bool(re.search(r"(?m)^- \*\*H si perfil actiu\*\*", sub))
    i_law = bool(re.search(r"(?m)^- \*\*I si multi-condició\*\*", sub))
    g_law = bool(re.search(r"(?m)^- \*\*G si L1 declarada\*\*", sub))
    if not (h_law and i_law and g_law):
        manquen = [n for n, b in (("H", h_law), ("I", i_law), ("G", g_law)) if not b]
        raise ValueError(f"Lleis: falten marcadors de llei condicional: {manquen}.")

    # ── mètrica A: taula MECR → màxim de paraules ──
    metrica: dict[str, int] = {}
    for cells in _table_rows(sub):
        if len(cells) < 2:
            continue
        mecr = _backtick_key(cells[0])
        if not mecr:
            continue
        num = re.search(r"\d+", cells[1])
        if not num:
            continue
        metrica[mecr] = int(num.group(0))
    esperats = ["pre-A1", "A1", "A2", "B1", "B2"]
    if list(metrica.keys()) != esperats:
        raise ValueError(
            f"Lleis: la mètrica MECR esperava {esperats}, he llegit {list(metrica.keys())}."
        )

    return {
        "sempre": sempre,
        "H_si_perfil_actiu": h_law,
        "I_si_multi_condicio": i_law,
        "G_si_L1_declarada": g_law,
        "metrica_A_paraules_per_mecr": metrica,
    }


# =======================================================================
# Builder principal
# =======================================================================


def build(md_path: Path) -> dict:
    md = md_path.read_text(encoding="utf-8")
    section = _extract_section(md, SECTION_TITLE)

    cats_by_code, noms = _parse_taxonomia(section)
    mapeig = _parse_mapeig(section)
    lleis = _parse_lleis(section)

    # Coherència interna: cada categoria referida al mapeig ha d'existir.
    for comp, cs in mapeig.items():
        for c in cs:
            if c not in noms:
                raise ValueError(f"Mapeig[{comp}]: categoria '{c}' no és a la taxonomia.")

    categories = [
        {
            "codi": c,
            "nom": cats_by_code[c]["nom"],
            "sub_arees": cats_by_code[c]["sub_arees"],
            "naturalesa": cats_by_code[c]["naturalesa"],
            "descripcio": cats_by_code[c]["descripcio"],
        }
        for c in "ABCDEFGHI"
    ]

    return {
        "version": VERSION,
        "_meta": {
            "source": _relative_to_corpusfje(md_path) + "#taxonomia-per-al-docent--categories-dargumentacio",
            "generat_at": date.today().isoformat(),
            "build_tag": BUILD_TAG,
            "validacio_pedagogica": "NotebookLM MALL FJE 2026-06-11 («Per al docent» apte producció)",
        },
        "categories": categories,
        "taxonomia_9cat": noms,
        "complement_to_categoria": mapeig,
        "lleis": lleis,
        "algoritme": (
            "Categories OBLIGATÒRIES per a un cas = unió de: (1) lleis.sempre [A,B,E]; "
            "(2) per cada complement actiu, complement_to_categoria[complement]; "
            "(3) H si hi ha ≥1 condició activa; (4) I si hi ha ≥2 condicions actives; "
            "(5) G si el perfil nouvingut té L1 declarada (detecció runtime al consumidor). "
            "La mètrica de A (paraules/frase) es tria per metrica_A_paraules_per_mecr[mecr_sortida]. "
            "Ordre de sortida de categories = A..I."
        ),
    }


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

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if not args.font.is_file():
        print(f"ERROR: no existeix {args.font}", file=sys.stderr)
        return 2

    print(f"-> Parsing {args.font.name} (secció '{SECTION_TITLE}')...", file=sys.stderr)
    try:
        data = build(args.font)
    except ValueError as e:
        print(f"ERROR de parsing: {e}", file=sys.stderr)
        return 1

    print(f"  categories: {len(data['categories'])}", file=sys.stderr)
    print(f"  complements mapejats: {len(data['complement_to_categoria'])}", file=sys.stderr)
    print(f"  sempre: {data['lleis']['sempre']}", file=sys.stderr)
    print(f"  mètrica MECR: {data['lleis']['metrica_A_paraules_per_mecr']}", file=sys.stderr)

    json_text = json.dumps(data, indent=2, ensure_ascii=False)

    if args.stdout:
        print(json_text)
        return 0

    out = args.out if args.out else Path(__file__).resolve().parent
    out.mkdir(parents=True, exist_ok=True)
    out_path = out / "per_al_docent.json"
    out_path.write_text(json_text, encoding="utf-8")
    print(f"  [OK] {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
