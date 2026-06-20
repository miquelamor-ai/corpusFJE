#!/usr/bin/env python3
"""Aplica el canon de gèneres (2026-06-19) als frontmatters dels M3_genere-*.md.

Afegeix dos camps nous al frontmatter de cada skill write-* font (.md):
  - macro_tipologia: vocabulari controlat de 7 valors (M3 §Taxonomia)
  - label_ca: etiqueta visible per a la UI en català

Decisions traçades a `corpusFJE/docs/canon_generes_skills_atne_2026-06-19.md`.
Font de veritat de l'assignació: `M3_generes-discursius.md` §Catàleg.

Script d'aplicació única (run-and-keep com a registre). Idempotent: si els
camps ja existeixen, els actualitza al valor canònic; no esborra res.

Ús: python .tooling/_apply_canon_generes_2026-06-19.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills" / "generes"

# Taula canon: genre_key -> (macro_tipologia, label_ca)
# Traçada a corpusFJE/docs/canon_generes_skills_atne_2026-06-19.md §1 i §3.
# Vocabulari controlat (7 macros M3): narrativa, descriptiva, explicativa,
# argumentativa, instructiva, conversacional, poetica.
CANON: dict[str, tuple[str, str]] = {
    # Narrativa (M3 §1)
    "conte": ("narrativa", "Conte"),
    "fabula": ("narrativa", "Faula"),
    "biografia": ("narrativa", "Biografia"),
    "noticia": ("narrativa", "Notícia de premsa"),
    "cronica": ("narrativa", "Crònica"),
    "diari": ("narrativa", "Diari personal"),
    # Descriptiva (M3 §2)
    "descripcio": ("descriptiva", "Descripció"),
    "enciclopedic": ("descriptiva", "Entrada enciclopèdica"),
    # Explicativa (M3 §3) — canon = "explicativa" (no "expositiva")
    "manual": ("explicativa", "Manual"),
    "divulgatiu": ("explicativa", "Text divulgatiu"),
    "informe": ("explicativa", "Informe"),
    "resum": ("explicativa", "Resum"),
    # Argumentativa (M3 §4)
    "opinio": ("argumentativa", "Article d'opinió"),
    "ressenya": ("argumentativa", "Ressenya"),
    "assaig": ("argumentativa", "Assaig"),
    "contrarelat_odi": ("argumentativa", "Contrarelat de l'odi"),
    # Instructiva (M3 §5)
    "instructiu": ("instructiva", "Text instructiu"),
    "receptari": ("instructiva", "Recepta"),
    "reglament": ("instructiva", "Reglament"),
    # Conversacional (M3 §6) — canon: M3 fixa la dominant a Conversacional
    "carta": ("conversacional", "Carta"),
    "entrevista": ("conversacional", "Entrevista"),
    "dialeg": ("conversacional", "Diàleg"),
    # Poètica (M3 §7)
    "poema": ("poetica", "Poema"),
    # Expressar preferències (skill no-write existent, gestionada a part)
    # NB: expressar-preferencies NO és al M3 §Catàleg; el seu .md font porta
    # genre_key="expressar_preferencies"; no s'inclou aquí (no és write-*).
}

# Special case: write-contrarelat-odi té tipologia buida i description en català.
# Decisió: omplir tipologia + redactar description en anglès curt.
CONTRARELAT_PATCH = {
    "tipologia": '"Argumentativa / Reflexiva"',
    "description": (
        '"Use when adapting or generating a counter-narrative response to a hate '
        "message (online or face-to-face). Activates when genre_discursiu == "
        '"contrarelat_odi". Dismantles the hate message with data, perspective and '
        "an alternative narrative, without reproducing its rhetoric. Output: "
        'counter-narrative text in markdown with empathic framing and evidence."'
    ),
}


# ── YAML mínim helpers ──────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^(---\n)(.*?)(\n---\n)", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str, str] | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3) + text[m.end():]


def get_field(fm_body: str, key: str) -> str | None:
    """Retorna el valor en brut (sense parsejar) del camp `key` al frontmatter,
    o None si no hi és. Només suporta camps d'una línia."""
    for line in fm_body.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(f"{key}:"):
            return stripped[len(key) + 1:].strip()
    return None


def has_field(fm_body: str, key: str) -> bool:
    return get_field(fm_body, key) is not None


def replace_field_inplace(fm_body: str, key: str, new_value: str) -> str:
    """Substitueix la línia `key: ...` per `key: new_value`. Falla si no hi és."""
    out = []
    found = False
    for line in fm_body.splitlines():
        if line.lstrip().startswith(f"{key}:"):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f"{indent}{key}: {new_value}")
            found = True
        else:
            out.append(line)
    if not found:
        raise KeyError(f"camp '{key}' no trobat al frontmatter")
    return "\n".join(out)


def add_field_after(fm_body: str, after_key: str, new_key: str, new_value: str) -> str:
    """Afegeix `new_key: new_value` just després de la línia que comença per `after_key:`.
    Si `after_key` no existeix, afegeix al final del frontmatter."""
    if has_field(fm_body, new_key):
        return replace_field_inplace(fm_body, new_key, new_value)
    out: list[str] = []
    inserted = False
    for line in fm_body.splitlines():
        out.append(line)
        if not inserted and line.lstrip().startswith(f"{after_key}:"):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f"{indent}{new_key}: {new_value}")
            inserted = True
    if not inserted:
        out.append(f"{new_key}: {new_value}")
    return "\n".join(out)


# ── Procés ──────────────────────────────────────────────────────────


def apply_to_file(md_path: Path, dry_run: bool) -> tuple[str, list[str]]:
    """Aplica el canon a un .md font. Retorna (estat, accions)."""
    text = md_path.read_text(encoding="utf-8")
    parts = split_frontmatter(text)
    if parts is None:
        return ("ERROR", ["no té frontmatter YAML"])
    pre, fm_body, rest = parts

    genre_key = get_field(fm_body, "genre_key")
    if genre_key is None:
        return ("SKIP", [f"sense genre_key al frontmatter ({md_path.name})"])
    # Treure cometes simples/dobles si n'hi ha
    gk = genre_key.strip().strip("'").strip('"')

    if gk not in CANON:
        return ("SKIP", [f"genre_key '{gk}' no és al canon (cas a revisar manualment)"])

    macro, label = CANON[gk]
    actions: list[str] = []

    # 1) macro_tipologia — afegir/actualitzar després de tipologia o genre_key
    anchor_for_macro = "tipologia" if has_field(fm_body, "tipologia") else "genre_key"
    new_fm = add_field_after(fm_body, anchor_for_macro, "macro_tipologia", macro)
    if new_fm != fm_body:
        actions.append(f"macro_tipologia: {macro}")
        fm_body = new_fm

    # 2) label_ca — afegir/actualitzar després de macro_tipologia
    new_fm = add_field_after(fm_body, "macro_tipologia", "label_ca", f'"{label}"')
    if new_fm != fm_body:
        actions.append(f'label_ca: "{label}"')
        fm_body = new_fm

    # 3) Cas especial write-contrarelat-odi: omplir tipologia + description
    if gk == "contrarelat_odi":
        for key, val in CONTRARELAT_PATCH.items():
            current = get_field(fm_body, key)
            if current is None:
                fm_body = add_field_after(fm_body, "genre_key", key, val)
                actions.append(f"{key}: (afegit)")
            elif current.strip().strip("'").strip('"') == "":
                fm_body = replace_field_inplace(fm_body, key, val)
                actions.append(f"{key}: (omplert, era buit)")

    if not actions:
        return ("OK (ja al dia)", [])

    new_text = pre + fm_body + rest
    if not dry_run:
        md_path.write_text(new_text, encoding="utf-8")
    return ("ACTUALITZAT" if not dry_run else "DRY-RUN", actions)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="No escriu; només mostra què faria.")
    args = ap.parse_args()

    md_files = sorted(SKILLS_DIR.glob("write-*/M3_genere-*.md"))
    if not md_files:
        print(f"ERROR: cap fitxer write-*/M3_genere-*.md trobat a {SKILLS_DIR}",
              file=sys.stderr)
        return 2

    print(f"-> {len(md_files)} fitxers M3_genere-*.md a processar")
    print(f"   dry-run={args.dry_run}\n")

    summary: dict[str, int] = {}
    for md in md_files:
        rel = md.relative_to(ROOT)
        status, actions = apply_to_file(md, args.dry_run)
        summary[status] = summary.get(status, 0) + 1
        marker = "[OK]" if status.startswith(("ACTUALITZAT", "DRY-RUN", "OK")) else "[!!]"
        print(f"  {marker} {rel}  [{status}]")
        for a in actions:
            print(f"       · {a}")

    print("\n-> Resum:")
    for k, v in summary.items():
        print(f"   {k}: {v}")
    return 0 if not any(k.startswith("ERROR") for k in summary) else 1


if __name__ == "__main__":
    sys.exit(main())
