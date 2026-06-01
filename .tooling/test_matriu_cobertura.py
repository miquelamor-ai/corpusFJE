"""test_matriu_cobertura.py — round-trip de matriu_cobertura.json vs golden ATNE.

Valida que el JSON derivat del M2 és SUFICIENT i COMPLET: reimplementa
l'algoritme de defaultComplementsForProfile aplicant NOMÉS el contingut del
matriu_cobertura.json, genera les mateixes claus que el golden snapshot d'ATNE
i compara byte-a-byte (com a conjunts, l'ordre l'imposa complement_keys).

Si el JSON reprodueix el snapshot 711/711, el refactor d'ATNE (substituir el JS
hardcoded per consum del JSON) no pot tenir regressions.

Font del contracte: ATNE/tests/golden/matriu_complements_snapshot.json
  Clau: "<cond>|<mecr>|<curs>"
    cond ∈ {13 condicions, parelles 'a+b', 'NONE', 'NOUV_L1'}
    mecr ∈ {pre-A1,A1,A2,B1,B2,C1,C2,'','undef'}
    curs ∈ {'1r Primària','2n Primària','3r Primària','3r ESO',''}
  Valor: llista de complement_keys.

Ús:
    python test_matriu_cobertura.py [--json <path>] [--snapshot <path>]
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
DEFAULT_JSON = THIS_DIR / "matriu_cobertura.json"
DEFAULT_SNAPSHOT = Path(
    "C:/Users/miquel.amor/Documents/GitHub/ATNE/tests/golden/matriu_complements_snapshot.json"
)


# =======================================================================
# Reimplementació de l'algoritme aplicant NOMÉS el JSON
# =======================================================================


class MatriuEngine:
    """Aplica matriu_cobertura.json. Equival a defaultComplementsForProfile."""

    def __init__(self, m: dict):
        self.keys: list[str] = m["complement_keys"]
        self.base: dict[str, list[str]] = m["base"]
        self.visual_need: set[str] = set(m["visual_need_conditions"])
        self.primaria_inicial: set[str] = set(m["primaria_inicial_cursos"])
        r = m["rules"]
        self.bands: dict[str, list[str]] = r["mecr_bands"]
        self.r1_add: list[str] = r["R1_add_pictos"]["add"]
        self.r2_drop: set[str] = set(r["R2_drop_maps"]["drop"])
        self.r3 = r["R3_drop_glossari_disl"]
        self.fallback: list[str] = r["fallback"]["default"]
        self.r4_only: list[str] = r["R4_primaria_inicial"]["only"]
        self.a5_result: list[str] = r["A5_nouvingut_l1"]["result"]

    def band(self, mecr: str) -> str:
        m = (mecr or "").upper().replace("Ç", "C").strip()
        if m in ("PRE-A1", "A1"):
            return "low"
        if m in ("A2", "B1"):
            return "mid"
        return "high"  # B2/C1/C2 i fallback per a buit/desconegut

    def _order(self, active: set[str]) -> list[str]:
        return [k for k in self.keys if k in active]

    def complements(self, conditions: list[str], mecr: str, curs: str,
                    nouvingut_l1: bool = False) -> list[str]:
        band = self.band(mecr)
        known = [c for c in conditions if c in self.base]

        # Mòdul C — sense condicions reconegudes
        if not known:
            if band == "low" and curs in self.primaria_inicial:
                if nouvingut_l1:
                    return self._order(set(self.a5_result))
                return self._order(set(self.r4_only))
            return self._order(set(self.fallback))

        # Base = unió OR
        active: set[str] = set()
        for c in known:
            active.update(self.base[c])

        # Mòdul B — modulació banda low
        if band == "low":
            # R1
            if any(c in self.visual_need for c in known):
                active.update(self.r1_add)
            # R2
            active -= self.r2_drop
            # R3
            if (self.r3["if"] in known
                    and not any(u in known for u in self.r3["unless"])):
                active -= set(self.r3["drop"])

        return self._order(active)


# =======================================================================
# Decodificació de claus del snapshot → (conditions, mecr, curs, nouv_l1)
# =======================================================================


def decode_key(cond_tok: str, mecr: str, curs: str):
    """Tradueix el token de condició de la clau snapshot a un perfil.

    - 'NONE'    → cap condició (fallback)
    - 'NOUV_L1' → cap condició reconeguda PERÒ nouvingut amb L1 (excepció A5).
                  ATNE el modela com a perfil sense chip de condició però amb L1
                  declarada → entra al Mòdul C amb nouvingut_l1=True.
    - 'a+b'     → dues condicions
    - altrament → una condició
    """
    nouv_l1 = False
    if cond_tok == "NONE":
        conditions: list[str] = []
    elif cond_tok == "NOUV_L1":
        conditions = []
        nouv_l1 = True
    else:
        conditions = cond_tok.split("+")
    return conditions, mecr, curs, nouv_l1


# =======================================================================
# Test
# =======================================================================


def run(json_path: Path, snapshot_path: Path) -> int:
    matriu = json.loads(json_path.read_text(encoding="utf-8"))
    engine = MatriuEngine(matriu)

    if not snapshot_path.exists():
        print(f"[SKIP] snapshot ATNE no trobat a {snapshot_path}")
        print("       (CI sense ATNE: només s'ha validat que el JSON carrega i l'engine arrenca)")
        # Smoke mínim perquè el test no sigui silenciosament inútil
        _ = engine.complements(["disl"], "A1", "1r Primària")
        return 0

    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))

    n_ok = 0
    fails = []
    for key, expected in snapshot.items():
        cond_tok, mecr, curs = key.split("|")
        conditions, mecr, curs, nouv_l1 = decode_key(cond_tok, mecr, curs)
        actual = engine.complements(conditions, mecr, curs, nouvingut_l1=nouv_l1)
        if sorted(actual) == sorted(expected):
            n_ok += 1
        else:
            fails.append((key, sorted(expected), sorted(actual)))

    total = len(snapshot)
    print(f"Round-trip vs golden ATNE: {n_ok}/{total} OK")
    if fails:
        print(f"\n{len(fails)} DIVERGÈNCIES:")
        for key, exp, act in fails[:40]:
            print(f"  [{key}]")
            print(f"     esperat (ATNE): {exp}")
            print(f"     calculat (JSON): {act}")
        if len(fails) > 40:
            print(f"  ... i {len(fails) - 40} més")
        return 1

    print("✓ El matriu_cobertura.json reprodueix el snapshot d'ATNE 100%.")
    print("  El refactor R0 d'ATNE pot consumir el JSON sense regressions.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", type=Path, default=DEFAULT_JSON)
    ap.add_argument("--snapshot", type=Path, default=DEFAULT_SNAPSHOT)
    args = ap.parse_args()
    if not args.json.exists():
        print(f"ERROR: no existeix {args.json}. Genera'l amb build_matriu_cobertura.py.",
              file=sys.stderr)
        return 2
    return run(args.json, args.snapshot)


if __name__ == "__main__":
    sys.exit(main())
