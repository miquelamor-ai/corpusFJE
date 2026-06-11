#!/usr/bin/env python3
"""build_dinamiques.py — contracte i derivació de les dinàmiques de formació (M11).

Aquest mòdul és l'AUTORITAT del contracte `.md ↔ json` de les dinàmiques:
defineix com es construeix un `M11_dinamica-*.md` a partir d'un registre
(record_to_md) i com es torna a llegir (md_to_record). Tenir-ho en un sol
lloc garanteix que el seeder de mineriaRAG (factoria) i la GitHub Action de
derivació no divergeixin mai.

Direcció canònica (font única = corpusFJE):

    dinamiques/<fase>/M11_dinamica-<id>.md   (MÀSTER, editable a Scriptorium)
        │  [build_dinamiques.py, determinista, sense LLM]
        ▼
    dinamiques/_dinamiques.json              (DERIVAT, el consumeix Itinerarium)

Ús (derivació, l'executa la Action a cada push d'un .md):
    python .tooling/build_dinamiques.py            # escriu dinamiques/_dinamiques.json
    python .tooling/build_dinamiques.py --check     # no escriu; surt !=0 si hi ha drift

El schema del JSON derivat és idèntic al que consumia històricament l'app
(`id, phase, block, title, stars, role, duration, guskey, purpose,
objectives, schedule[{temps,text}], materials, simple, indicators`).
El camp `ordre` del frontmatter NO surt al JSON: només fixa l'ordre.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

# ── Constants del domini ──────────────────────────────────────────────────────
PHASES = ["abans", "durant", "despres"]
PHASE_RANK = {p: i for i, p in enumerate(PHASES)}
PHASE_LABEL = {
    "abans": "abans de la formació",
    "durant": "durant la formació",
    "despres": "després de la formació",
}
MATERIALS_SEP = " · "
GENERAT_AT = "2026-06-11"

REPO_ROOT = Path(__file__).resolve().parent.parent
DINAMIQUES_DIR = REPO_ROOT / "dinamiques"
OUT_JSON = DINAMIQUES_DIR / "_dinamiques.json"

# Camps del JSON derivat, en ordre estable (drop-in per a l'app consumidora).
JSON_FIELDS = [
    "id", "phase", "block", "title", "stars", "role", "duration", "guskey",
    "purpose", "objectives", "schedule", "materials", "simple", "indicators",
]

# Seccions H2 del cos (l'ordre és l'ordre d'escriptura).
H_PROPOSIT = "Propòsit"
H_OBJECTIUS = "Objectius"
H_DESENV = "Desenvolupament"
H_MATERIALS = "Materials"
H_SIMPLE = "Versió simplificada"
H_INDICADORS = "Indicadors d'observació"
H_CONNEXIO = "Connexió amb el marc"  # no es deriva: només cross-ref humà


# ── Conversió emfàtica HTML ↔ Markdown (bijectiva per al nostre contingut) ────
def html_to_md(s: str) -> str:
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s, flags=re.S)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s, flags=re.S)
    return s


def md_to_html(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s, flags=re.S)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s, flags=re.S)
    return s


def html_to_text(s: str) -> str:
    """Treu tota èmfasi: per a la descripció del frontmatter (text pla)."""
    return re.sub(r"</?(?:em|strong)>", "", s)


def _cell(s: str) -> str:
    return s.replace("|", "\\|")


def _uncell(s: str) -> str:
    return s.replace("\\|", "|")


# ── Construcció: record → .md ─────────────────────────────────────────────────
def slugify(s: str) -> str:
    s = s.lower()
    repl = (("à", "a"), ("á", "a"), ("è", "e"), ("é", "e"), ("í", "i"),
            ("ò", "o"), ("ó", "o"), ("ú", "u"), ("ï", "i"), ("ü", "u"),
            ("ç", "c"), ("·", ""), ("'", " "), ("’", " "))
    for a, b in repl:
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def build_frontmatter(rec: dict, ordre: int) -> dict:
    """Frontmatter canònic d'una dinàmica (ordre d'inserció = ordre de sortida)."""
    items = [
        ("modul", "M11"),
        ("titol", rec["title"]),
        ("tipus", "dinamica"),
        ("descripcio", html_to_text(rec["purpose"]).strip()),
        ("id", rec["id"]),
        ("ordre", ordre),
        ("block", rec["block"]),
        ("phase", rec["phase"]),
    ]
    # phases_aplicables: només si la dinàmica serveix per a més d'una fase
    # (cross-fase). Si no hi és, s'entén = [phase]. Es col·loca just després de phase.
    pa = rec.get("phases_aplicables")
    if pa and list(pa) != [rec["phase"]]:
        items.append(("phases_aplicables", list(pa)))
    items += [
        ("guskey", rec["guskey"]),
        ("stars", rec["stars"]),
        ("role", rec["role"]),
        ("duration", rec["duration"]),
        ("paraules_clau", ["dinamica-formacio", "A-D-D", rec["phase"], "CPA", slugify(rec["block"])]),
        ("moduls_relacionats", ["M11"]),
        ("review_status", "esborrany"),
        ("generat_at", GENERAT_AT),
    ]
    return dict(items)


def record_to_md(rec: dict, ordre: int) -> str:
    fm = build_frontmatter(rec, ordre)
    fm_yaml = yaml.safe_dump(
        fm, sort_keys=False, allow_unicode=True, default_flow_style=None, width=10_000
    ).rstrip("\n")

    lines: list[str] = ["---", fm_yaml, "---", ""]

    lines += [f"## {H_PROPOSIT}", "", html_to_md(rec["purpose"]).strip(), ""]

    lines += [f"## {H_OBJECTIUS}", ""]
    lines += [f"- {html_to_md(o).strip()}" for o in rec["objectives"]]
    lines += [""]

    lines += [f"## {H_DESENV}", "", "| Temps | Pas |", "|---|---|"]
    for step in rec["schedule"]:
        lines.append(f"| {_cell(step['temps'].strip())} | {_cell(html_to_md(step['text']).strip())} |")
    lines += [""]

    lines += [f"## {H_MATERIALS}", ""]
    mats = [m.strip() for m in re.split(r"\s*·\s*", rec["materials"]) if m.strip()]
    lines += [f"- {html_to_md(m)}" for m in mats]
    lines += [""]

    lines += [f"## {H_SIMPLE}", "", html_to_md(rec["simple"]).strip(), ""]

    lines += [f"## {H_INDICADORS}", ""]
    lines += [f"- {html_to_md(i).strip()}" for i in rec["indicators"]]
    lines += [""]

    lines += [
        f"## {H_CONNEXIO}",
        "",
        (
            f"Aquesta dinàmica s'inscriu en el cicle de formació **Abans–Durant–Després** "
            f"(fase _{PHASE_LABEL[rec['phase']]}_) i, segons el model d'avaluació de la "
            f"formació de Guskey, treballa cap al nivell **{rec['guskey']}** d'impacte. "
            f"La fonamentació (CPA, A-D-D, Guskey) viu al marc "
            f"[Desenvolupament professional docent](../M11_desenvolupament-professional-docent.md); "
            f"aquesta fitxa només n'és la concreció operativa."
        ),
        "",
    ]

    return "\n".join(lines) + "\n"


# ── Lectura: .md → record ─────────────────────────────────────────────────────
def _split_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError("frontmatter absent o malformat")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def _sections(body: str) -> dict[str, str]:
    out: dict[str, str] = {}
    cur = None
    buf: list[str] = []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*?)\s*$", line)
        if h:
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur = h.group(1)
            buf = []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out


def _bullets(block: str) -> list[str]:
    return [md_to_html(m.group(1).strip())
            for m in re.finditer(r"^-\s+(.*)$", block, re.MULTILINE)]


def _table(block: str) -> list[dict]:
    rows = []
    for line in block.splitlines():
        m = re.match(r"^\|(.+)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if len(cells) != 2:
            continue
        temps, text = cells
        if temps.lower() == "temps" or set(temps) <= set("-: "):
            continue  # capçalera o separador
        rows.append({"temps": _uncell(temps), "text": md_to_html(_uncell(text))})
    return rows


def md_to_record(text: str) -> dict:
    fm, body = _split_frontmatter(text)
    sec = _sections(body)
    rec = {
        "id": fm["id"],
        "phase": fm["phase"],
        "block": fm["block"],
        "title": fm["titol"],
        "stars": fm["stars"],
        "role": fm["role"],
        "duration": fm["duration"],
        "guskey": fm["guskey"],
        "purpose": md_to_html(sec.get(H_PROPOSIT, "").strip()),
        "objectives": _bullets(sec.get(H_OBJECTIUS, "")),
        "schedule": _table(sec.get(H_DESENV, "")),
        "materials": MATERIALS_SEP.join(_bullets(sec.get(H_MATERIALS, ""))),
        "simple": md_to_html(sec.get(H_SIMPLE, "").strip()),
        "indicators": _bullets(sec.get(H_INDICADORS, "")),
    }
    if fm.get("phases_aplicables"):
        rec["phases_aplicables"] = list(fm["phases_aplicables"])
    rec["_ordre"] = fm.get("ordre", 10_000)
    return rec


# ── Build del JSON derivat ────────────────────────────────────────────────────
def build_json(dinamiques_dir: Path = DINAMIQUES_DIR) -> list[dict]:
    records = []
    for md in dinamiques_dir.glob("**/M11_dinamica-*.md"):
        records.append(md_to_record(md.read_text(encoding="utf-8")))
    records.sort(key=lambda r: (PHASE_RANK.get(r["phase"], 99), r["_ordre"]))
    out = []
    for r in records:
        obj = {}
        for k in JSON_FIELDS:
            obj[k] = r[k]
            # phases_aplicables (opcional) just després de phase, si la dinàmica
            # és cross-fase. Si no hi és, el consumidor entén = [phase].
            if k == "phase" and r.get("phases_aplicables"):
                obj["phases_aplicables"] = r["phases_aplicables"]
        out.append(obj)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Deriva dinamiques/_dinamiques.json des dels .md màster.")
    ap.add_argument("--check", action="store_true",
                    help="No escriu; retorna codi !=0 si el JSON al disc no coincideix.")
    args = ap.parse_args()

    data = build_json()
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        current = OUT_JSON.read_text(encoding="utf-8") if OUT_JSON.exists() else ""
        if current != payload:
            print("DRIFT: dinamiques/_dinamiques.json no està sincronitzat amb els .md.", file=sys.stderr)
            return 1
        print(f"OK — {len(data)} dinàmiques, JSON sincronitzat.")
        return 0

    OUT_JSON.write_text(payload, encoding="utf-8")
    by_phase = {p: sum(1 for d in data if d["phase"] == p) for p in PHASES}
    print(f"OK — {len(data)} dinàmiques derivades a {OUT_JSON.relative_to(REPO_ROOT)}")
    print(f"     Per fase: {by_phase}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
