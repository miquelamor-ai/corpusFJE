"""test_per_al_docent.py — round-trip de per_al_docent.json vs golden ATNE.

Valida que el JSON derivat del M2 és SUFICIENT i COMPLET per substituir el coneixement
«Per al docent» hardcoded a ATNE. Comprova dues coses contra el golden snapshot d'ATNE
(tests/golden/per_al_docent_snapshot.json):

  1. Igualtat directa de les tres taules canòniques:
       taxonomia_9cat · complement_to_categoria · lleis (== lleis_case_block).
  2. Round-trip de comportament: reimplementant l'algoritme amb NOMÉS el contingut del
     JSON, les categories obligatòries dels 5 perfils golden coincideixen amb
     contracte_case_block_per_perfil.

Si tot quadra, el refactor d'ATNE (substituir el hardcoded ×3 per consum del JSON) no pot
tenir regressions de comportament.

Font del contracte: ATNE/tests/golden/per_al_docent_snapshot.json
  (generat per ATNE/tests/golden/per_al_docent_snapshot.py des de prompt_builder.py).

Ús:
    python test_per_al_docent.py [--json <path>] [--snapshot <path>]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

THIS_DIR = Path(__file__).resolve().parent
DEFAULT_JSON = THIS_DIR / "per_al_docent.json"
DEFAULT_SNAPSHOT = Path(
    "C:/Users/miquel.amor/Documents/GitHub/ATNE/tests/golden/per_al_docent_snapshot.json"
)

# Perfils golden d'ATNE (ATNE/tests/golden/per_al_docent_snapshot.py::_GOLDEN_PROFILES),
# reduïts als camps que l'algoritme «Per al docent» necessita: condicions actives,
# L1 declarada i complements actius. El RESULTAT esperat (categories obligatòries) viu al
# snapshot d'ATNE sota contracte_case_block_per_perfil; aquí només reproduïm l'ENTRADA.
_GOLDEN_INPUTS = {
    "nouvingut_A2_arab__glos_bast_picto": {
        "conditions": ["nouvingut"], "l1": "Àrab",
        "complements": {"glossari": True, "bastides": True, "pictogrames": True}},
    "tdah_dislexia_B1__glos_esq_preg": {
        "conditions": ["tdah", "dislexia"], "l1": "",
        "complements": {"glossari": True, "esquema_visual": True, "preguntes_comprensio": True}},
    "aacc_B2__mapa_act_rub": {
        "conditions": ["altes_capacitats"], "l1": "",
        "complements": {"mapa_conceptual": True, "activitats_aprofundiment": True, "rubriques": True}},
    "tea_A2__esq_picto": {
        "conditions": ["tea"], "l1": "",
        "complements": {"esquema_visual": True, "pictogrames": True}},
    "sense_perfil_B1__glossari": {
        "conditions": [], "l1": "",
        "complements": {"glossari": True}},
}

_ORDER = "ABCDEFGHI"


def mandatory_cats(inp: dict, data: dict) -> list[str]:
    """Categories «Per al docent» obligatòries aplicant NOMÉS el JSON canon.

    Equival al case-block d'ATNE (_argumentacio_case_block):
      sempre A/B/E · complement→categoria · H si condició · I si multi · G si L1.
    """
    lleis = data["lleis"]
    comp_map = data["complement_to_categoria"]
    cats: set[str] = set(lleis["sempre"])  # A, B, E

    for comp, actiu in inp["complements"].items():
        if actiu:
            cats.update(comp_map.get(comp, []))

    active = inp["conditions"]
    if lleis.get("H_si_perfil_actiu") and active:
        cats.add("H")
    if lleis.get("I_si_multi_condicio") and len(active) >= 2:
        cats.add("I")
    if lleis.get("G_si_L1_declarada") and inp.get("l1"):
        cats.add("G")

    return [c for c in _ORDER if c in cats]


def run(json_path: Path, snapshot_path: Path) -> int:
    data = json.loads(json_path.read_text(encoding="utf-8"))

    # Sanitat estructural mínima (independent del snapshot d'ATNE).
    assert len(data["categories"]) == 9, "esperava 9 categories"
    assert data["lleis"]["sempre"] == ["A", "B", "E"], "lleis.sempre != [A,B,E]"
    assert list(data["lleis"]["metrica_A_paraules_per_mecr"]) == \
        ["pre-A1", "A1", "A2", "B1", "B2"], "mètrica MECR incompleta"

    if not snapshot_path.exists():
        print(f"[SKIP] snapshot ATNE no trobat a {snapshot_path}")
        print("       (CI sense ATNE: només s'ha validat que el JSON carrega i és estructuralment vàlid)")
        # Smoke: l'engine arrenca i és determinista
        _ = mandatory_cats(_GOLDEN_INPUTS["tdah_dislexia_B1__glos_esq_preg"], data)
        return 0

    snap = json.loads(snapshot_path.read_text(encoding="utf-8"))

    fails: list[str] = []

    # ── 1. Igualtat de les tres taules canòniques ──
    if data["taxonomia_9cat"] != snap["taxonomia_9cat"]:
        fails.append("taxonomia_9cat difereix del snapshot d'ATNE")
    if data["complement_to_categoria"] != snap["complement_to_categoria"]:
        fails.append("complement_to_categoria difereix del snapshot d'ATNE")
    if data["lleis"] != snap["lleis_case_block"]:
        fails.append("lleis difereix de lleis_case_block del snapshot d'ATNE")

    # ── 2. Round-trip de comportament (5 perfils golden) ──
    contracte = snap["contracte_case_block_per_perfil"]
    n_ok = 0
    for nom, inp in _GOLDEN_INPUTS.items():
        expected = contracte.get(nom)
        actual = mandatory_cats(inp, data)
        if expected is not None and actual == expected:
            n_ok += 1
        else:
            fails.append(f"perfil [{nom}]: esperat {expected} · calculat {actual}")

    print(f"Round-trip vs golden ATNE: {n_ok}/{len(_GOLDEN_INPUTS)} perfils OK")
    if fails:
        print(f"\n{len(fails)} DIVERGÈNCIES:")
        for f in fails:
            print(f"  · {f}")
        return 1

    print("✓ El per_al_docent.json reprodueix el snapshot d'ATNE 100%.")
    print("  taxonomia_9cat · complement_to_categoria · lleis idèntics; 5/5 perfils golden.")
    print("  El refactor d'ATNE pot consumir el JSON i eliminar el hardcoded (×3) sense regressions.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", type=Path, default=DEFAULT_JSON)
    ap.add_argument("--snapshot", type=Path, default=DEFAULT_SNAPSHOT)
    args = ap.parse_args()
    if not args.json.exists():
        print(f"ERROR: no existeix {args.json}. Genera'l amb build_per_al_docent.py.",
              file=sys.stderr)
        return 2
    return run(args.json, args.snapshot)


if __name__ == "__main__":
    sys.exit(main())
