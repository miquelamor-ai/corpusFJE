"""test_rubrica.py — tests unitaris + integrals per a rubrica.json.

Test harness que:
1. Re-corre build_rubrica.py sobre els 38 skills amb M*.md.
2. Validacio estructural de cada rubrica.json (smoke test contra l'esquema v1.0).
3. Comparacio semantica dels 2 pilots (glossari + bastides-lectura) amb els
   pilots ATNE (rubrica_glossari_v2.json, rubrica_bastides_lectura.json).
4. Reporta cobertura de blocs per skill + skills problematics.

No depen de jsonschema (smoke test amb checks manuals dels camps esperats).

Us:
    python test_rubrica.py [--regenerate] [--out-dir <dir>]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
CORPUSFJE_DIR = THIS_DIR.parent
SKILLS_DIR = CORPUSFJE_DIR / "skills"

# Pilot ATNE de referencia (cobertura semantica)
ATNE_PILOT_GLOSSARI = Path("C:/Users/miquel.amor/Documents/GitHub/ATNE/tests/pilot_glossari_2026_05_31/rubrica_glossari_v2.json")
ATNE_PILOT_BASTIDES = Path("C:/Users/miquel.amor/Documents/GitHub/ATNE/tests/pilot_glossari_2026_05_31/rubrica_bastides_lectura.json")

# Esquema v1.0: blocs requerits + opcionals
REQUIRED_BLOCKS = {"_meta", "transversals", "levels", "passos_meta"}
OPTIONAL_BLOCKS = {
    "principi_general", "regla_seleccio_per_perfil",
    "senyals_activacio", "anti_senyals",
    "heuristiques_docent", "case_overrides",
    "checks_automatics_post_generacio", "post_edicio_pas3",
    "alfabets_no_llatins_que_activen_translit",
}
ALL_BLOCKS = REQUIRED_BLOCKS | OPTIONAL_BLOCKS

# Constants canòniques
FAMILIES_CANONIQUES = {"mediacio", "generes", "adaptacio", "bastida", "avaluacio"}
NIVELLS_VALIDS = {"pre-A1", "A1", "A2", "B1", "B2", "C1+", "C1", "C2"}
ETIQUETES_VALIDES = {"Emergent", "Inicial", "Funcional", "Estratègic", "Acadèmic", "Crític"}
TIPUS_ENUM = {"binary", "qualitative", "countable", "structural",
              "cross_source", "metacognitive", "enumerable"}


def regenerate_all(out_dir: Path) -> dict:
    """Re-corre build_rubrica.py sobre tots els M*.md del corpus."""
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for m3 in SKILLS_DIR.rglob("M3_*.md"):
        skill_name = m3.parent.name
        skill_out = out_dir / skill_name
        skill_out.mkdir(parents=True, exist_ok=True)
        proc = subprocess.run(
            ["python", str(THIS_DIR / "build_rubrica.py"), str(m3), "--out", str(skill_out)],
            capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        if proc.returncode == 0:
            results[skill_name] = {"status": "regenerated", "m3_path": str(m3)}
        else:
            results[skill_name] = {"status": "error", "stderr": proc.stderr[:300]}
    return results


def validate_rubrica(rubrica: dict, skill_name: str) -> list:
    """Smoke test estructural d'un rubrica.json. Retorna llista d'errors (buida = OK)."""
    errors = []

    # 1. Blocs requerits presents
    missing = REQUIRED_BLOCKS - set(rubrica.keys())
    if missing:
        errors.append(f"FALTEN blocs requerits: {missing}")

    # 2. Blocs presents són canònics
    extra = set(rubrica.keys()) - ALL_BLOCKS
    if extra:
        errors.append(f"BLOCS no canonics: {extra}")

    # 3. _meta validations
    meta = rubrica.get("_meta", {})
    if meta:
        for required_field in ("name", "version", "font_canonic", "skill_name"):
            if required_field not in meta:
                errors.append(f"_meta sense '{required_field}'")
        family = meta.get("family")
        if family and family not in FAMILIES_CANONIQUES:
            errors.append(f"_meta.family invalida: {family!r} (acceptades: {FAMILIES_CANONIQUES})")
        if meta.get("skill_name") != skill_name:
            errors.append(f"_meta.skill_name no concorda amb dir: '{meta.get('skill_name')}' vs '{skill_name}'")

    # 4. levels: cada nivell amb etiqueta valida
    levels = rubrica.get("levels", {})
    for niv, blk in levels.items():
        if niv not in NIVELLS_VALIDS:
            errors.append(f"levels: nivell invalid {niv!r}")
        etiqueta = blk.get("etiqueta")
        if etiqueta and etiqueta not in ETIQUETES_VALIDES:
            errors.append(f"levels.{niv}.etiqueta no canonica: {etiqueta!r}")
        if "passos" in blk and not isinstance(blk["passos"], list):
            errors.append(f"levels.{niv}.passos no es llista")

    # 5. passos_meta: cada entry amb tipus valid
    for i, p in enumerate(rubrica.get("passos_meta", [])):
        if "id" not in p or "titol" not in p or "tipus" not in p:
            errors.append(f"passos_meta[{i}] sense id/titol/tipus")
        elif p["tipus"] not in TIPUS_ENUM:
            errors.append(f"passos_meta[{i}].tipus invalid: {p['tipus']!r}")

    return errors


def semantic_coverage_vs_pilot(rubrica: dict, pilot: dict, skill: str) -> dict:
    """Comparació semàntica: quins camps del pilot ATNE no tenim, quins tenim extra."""
    our_blocks = set(rubrica.keys())
    pilot_blocks = set(pilot.keys())
    coverage = {
        "our_blocks": sorted(our_blocks),
        "pilot_blocks": sorted(pilot_blocks),
        "comuns": sorted(our_blocks & pilot_blocks),
        "only_mineriaRAG": sorted(our_blocks - pilot_blocks),
        "only_ATNE_pilot": sorted(pilot_blocks - our_blocks),
        "coverage_pct": round(len(our_blocks & pilot_blocks) / len(pilot_blocks) * 100, 1) if pilot_blocks else 100.0,
    }

    # Comparacio detallada de levels
    our_levels = rubrica.get("levels", {})
    pilot_levels = pilot.get("levels", {})
    if our_levels and pilot_levels:
        coverage["levels_diff"] = {
            "our_count": len(our_levels),
            "pilot_count": len(pilot_levels),
            "our_keys": sorted(our_levels.keys()),
            "pilot_keys": sorted(pilot_levels.keys()),
        }

    return coverage


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--regenerate", action="store_true",
                    help="re-corre build_rubrica.py abans dels tests (default: usa l'output existent al corpusFJE)")
    ap.add_argument("--out-dir", type=Path, default=Path("/tmp/test_rubrica_full"),
                    help="dir de sortida si --regenerate (default: /tmp/test_rubrica_full)")
    ap.add_argument("--inplace", action="store_true",
                    help="usa els rubrica.json existents als directoris de skill (no regenera)")
    args = ap.parse_args()

    # Pas 1: regenerar si toca
    if args.regenerate:
        print(f"[1/4] Regenerant 38 rubrica.json a {args.out_dir}...")
        regen_results = regenerate_all(args.out_dir)
        n_ok = sum(1 for r in regen_results.values() if r["status"] == "regenerated")
        n_err = sum(1 for r in regen_results.values() if r["status"] == "error")
        print(f"      OK: {n_ok} | Errors: {n_err}")
        if n_err:
            for name, r in regen_results.items():
                if r["status"] == "error":
                    print(f"      ERROR {name}: {r['stderr'][:200]}")
        source_dir = args.out_dir
    elif args.inplace:
        source_dir = SKILLS_DIR
        print(f"[1/4] Usant rubrica.json in-place als directoris de skill...")
    else:
        source_dir = args.out_dir
        if not source_dir.exists():
            print(f"ERROR: {source_dir} no existeix. Usa --regenerate o --inplace.", file=sys.stderr)
            return 1
        print(f"[1/4] Usant rubrica.json a {source_dir}")

    # Pas 2: carregar i validar cada rubrica.json
    print(f"\n[2/4] Validant rubrica.json...")
    if args.inplace:
        rubrica_files = list(SKILLS_DIR.rglob("rubrica.json"))
    else:
        rubrica_files = list(source_dir.glob("*/rubrica.json"))

    validations = {}
    for path in rubrica_files:
        skill_name = path.parent.name
        try:
            rubrica = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            validations[skill_name] = {"errors": [f"JSON parse error: {e}"], "blocks": []}
            continue
        errors = validate_rubrica(rubrica, skill_name)
        validations[skill_name] = {"errors": errors, "blocks": sorted(rubrica.keys()),
                                    "n_levels": len(rubrica.get("levels", {})),
                                    "n_passos_meta": len(rubrica.get("passos_meta", []))}

    n_clean = sum(1 for v in validations.values() if not v["errors"])
    n_errors = sum(1 for v in validations.values() if v["errors"])
    print(f"      Total: {len(validations)} | Clean: {n_clean} | Amb errors: {n_errors}")
    for skill, v in validations.items():
        if v["errors"]:
            print(f"      [FAIL] {skill}:")
            for err in v["errors"]:
                print(f"         - {err}")

    # Pas 3: comparació semàntica vs pilots ATNE
    print(f"\n[3/4] Comparant pilots vs ATNE...")
    coverages = {}
    for skill, pilot_path in [("generate-glossari", ATNE_PILOT_GLOSSARI),
                                ("generate-bastides-lectura", ATNE_PILOT_BASTIDES)]:
        rubrica_path = source_dir / skill / "rubrica.json" if not args.inplace else SKILLS_DIR / "mediacio" / skill / "rubrica.json"
        if not rubrica_path.exists():
            print(f"      [SKIP] {skill}: no s'ha trobat rubrica.json a {rubrica_path}")
            continue
        if not pilot_path.exists():
            print(f"      [SKIP] {skill}: pilot ATNE no existeix a {pilot_path}")
            continue
        rubrica = json.loads(rubrica_path.read_text(encoding="utf-8"))
        pilot = json.loads(pilot_path.read_text(encoding="utf-8"))
        cov = semantic_coverage_vs_pilot(rubrica, pilot, skill)
        coverages[skill] = cov
        print(f"      [{skill}]")
        print(f"         Cobertura blocs pilot: {cov['coverage_pct']}%")
        print(f"         Blocs comuns: {len(cov['comuns'])}")
        print(f"         Només mineriaRAG: {cov['only_mineriaRAG']}")
        print(f"         Només ATNE pilot: {cov['only_ATNE_pilot']}")

    # Pas 4: resum final
    print(f"\n[4/4] RESUM FINAL")
    print(f"      Total skills processats: {len(validations)}")
    print(f"      Clean (validació OK): {n_clean}/{len(validations)}")
    print(f"      Amb errors estructurals: {n_errors}")
    print(f"      Cobertura semàntica pilots:")
    for skill, cov in coverages.items():
        print(f"         {skill}: {cov['coverage_pct']}%")

    # Distribucio blocs
    bloc_count = {}
    for v in validations.values():
        for b in v["blocks"]:
            bloc_count[b] = bloc_count.get(b, 0) + 1
    print(f"      Distribucio blocs (skills que el porten):")
    for b in sorted(bloc_count):
        print(f"         {b}: {bloc_count[b]}/{len(validations)}")

    # Return code: 0 si tot net, 1 si hi ha errors
    return 0 if n_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
