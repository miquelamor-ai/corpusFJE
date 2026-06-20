#!/usr/bin/env python3
"""validate_skills_writers.py — Gate de qualitat per a les skills write-*.

Valida que el frontmatter del .md font (`skills/generes/write-*/M3_genere-*.md`)
de TOTA skill `write-*` compleixi el contracte del catàleg derivable que ATNE
consumeix al Pas 2 (decisions traçades a
`docs/canon_generes_skills_atne_2026-06-19.md`).

Si alguna skill falla, el script retorna codi 1 i el build de corpusFJE
s'atura ABANS de regenerar derivats (SKILL.md, prompt_adapter.md). Així una
skill incompleta MAI arriba a producció ni trenca ATNE.

Camps OBLIGATORIS al frontmatter font (7):
  1. genre_key       — slug snake_case, coincideix amb el directori sense "write-"
  2. macro_tipologia — vocabulari controlat (les 7 macros M3)
  3. label_ca        — etiqueta visible UI en català, primera lletra majúscula
  4. mecr_range      — llista no buida amb valors ∈ {pre-A1, A1, A2, B1, B2, C1, C2, C1+}
  5. moduls_relacionats — llista no buida, almenys "M3"
  6. agent_roles     — llista no buida (p.ex. [adapter, generator])
  7. descripcio      — descripció en català, no buida, ≥ 60 caràcters

Camps OPCIONALS (recomanats):
  - tipologia — descripció rica (admet "/"), informativa. Si hi és al .md font,
                build_skills.py la propaga al SKILL.md derivat. Per a les 22 skills
                v2 històriques viu només al SKILL.md (preservada del bootstrap);
                el canon 2026-06-19 NO l'exigeix al font per no trencar res.

El camp "name" del SKILL.md derivat el genera build_skills.py des del directori,
i el "description" en anglès del SKILL.md el preserva entre regeneracions; per
això NO són obligatoris al .md font (vegeu build_skills.py).

Ús:
    python .tooling/validate_skills_writers.py [--quiet]
Sortida:
    exit 0 — totes les skills compleixen.
    exit 1 — almenys una falla. Llista emesa per stderr.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills" / "generes"

MACRO_TIPOLOGIA_VALIDS = {
    "narrativa", "descriptiva", "explicativa",
    "argumentativa", "instructiva", "conversacional", "poetica",
}

MECR_VALIDS = {"pre-A1", "A1", "A2", "B1", "B2", "C1", "C1+", "C2"}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None


def validate(md_path: Path) -> list[str]:
    """Retorna llista d'errors per a aquesta skill (buida = OK)."""
    errs: list[str] = []
    text = md_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return ["frontmatter YAML absent o invàlid"]

    skill_dir = md_path.parent.name  # p.ex. "write-noticia"
    if not skill_dir.startswith("write-"):
        return [f"directori inesperat: {skill_dir!r} (ha de començar per 'write-')"]
    expected_key_dir = skill_dir[len("write-"):].replace("-", "_")

    # 1) genre_key
    gk = fm.get("genre_key")
    if not gk or not isinstance(gk, str):
        errs.append("genre_key absent o no string")
    else:
        if not re.fullmatch(r"[a-z][a-z0-9_]*", gk):
            errs.append(f"genre_key '{gk}' no és snake_case ASCII")
        # Coherència amb el directori (admet diferències menors documentades)
        if gk != expected_key_dir and not (
            # Cas conegut: el dir pot usar guions, el key snake_case (p.ex. "diari-camp" -> "diari_camp")
            gk == expected_key_dir
        ):
            # No bloquem, és una alerta tova si coincideix la forma snake del dir
            if gk != expected_key_dir:
                errs.append(
                    f"genre_key '{gk}' no concorda amb el directori "
                    f"'{skill_dir}' (esperat: '{expected_key_dir}')"
                )

    # 2) macro_tipologia
    macro = fm.get("macro_tipologia")
    if not macro:
        errs.append("macro_tipologia absent")
    elif macro not in MACRO_TIPOLOGIA_VALIDS:
        errs.append(
            f"macro_tipologia '{macro}' no és al vocabulari controlat "
            f"({sorted(MACRO_TIPOLOGIA_VALIDS)})"
        )

    # 3) label_ca
    label = fm.get("label_ca")
    if not label or not isinstance(label, str):
        errs.append("label_ca absent o no string")
    else:
        if not label.strip():
            errs.append("label_ca buit")
        elif not label[0].isupper():
            errs.append(f"label_ca '{label}' no comença per majúscula")

    # 4) tipologia — OPCIONAL (informatiu, viu sovint al SKILL.md derivat per a
    #    les skills v2 històriques). No bloqueja el build.

    # 5) mecr_range
    mecr = fm.get("mecr_range")
    if not isinstance(mecr, list) or not mecr:
        errs.append("mecr_range absent o buit (ha de ser llista)")
    else:
        bad = [v for v in mecr if v not in MECR_VALIDS]
        if bad:
            errs.append(f"mecr_range conté valors no vàlids: {bad}")

    # 6) moduls_relacionats
    mods = fm.get("moduls_relacionats")
    if not isinstance(mods, list) or not mods:
        errs.append("moduls_relacionats absent o buit (ha de ser llista)")
    elif "M3" not in mods:
        errs.append(f"moduls_relacionats no inclou 'M3' (ha d'incloure'l): {mods}")

    # 7) agent_roles
    roles = fm.get("agent_roles")
    if not isinstance(roles, list) or not roles:
        errs.append("agent_roles absent o buit (ha de ser llista, p.ex. [adapter, generator])")

    # 8) descripcio (en català, al .md font)
    desc = fm.get("descripcio")
    if not desc or not isinstance(desc, str):
        errs.append("descripcio absent o no string")
    elif len(desc.strip()) < 60:
        errs.append(f"descripcio massa curta (<60 caràcters): {len(desc.strip())}")

    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true",
                    help="Només emetre output si hi ha errors.")
    args = ap.parse_args()

    md_files = sorted(SKILLS_DIR.glob("write-*/M3_genere-*.md"))
    if not md_files:
        print(f"ERROR: cap fitxer write-*/M3_genere-*.md trobat a {SKILLS_DIR}",
              file=sys.stderr)
        return 2

    total = len(md_files)
    failed: list[tuple[Path, list[str]]] = []

    if not args.quiet:
        print(f"-> Validant {total} skills write-* (.md font)...")

    for md in md_files:
        errs = validate(md)
        if errs:
            failed.append((md, errs))
        elif not args.quiet:
            print(f"  [OK] {md.relative_to(ROOT)}")

    if failed:
        print(f"\n[FAIL] {len(failed)}/{total} skills no compleixen el canon:",
              file=sys.stderr)
        for md, errs in failed:
            print(f"\n  {md.relative_to(ROOT)}:", file=sys.stderr)
            for e in errs:
                print(f"    - {e}", file=sys.stderr)
        print(
            "\nReferencia: docs/canon_generes_skills_atne_2026-06-19.md "
            "§2 (Camps obligatoris).",
            file=sys.stderr,
        )
        return 1

    if not args.quiet:
        print(f"\n-> OK {total}/{total} skills compleixen el canon.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
