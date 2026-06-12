#!/usr/bin/env python3
"""build_index_relacions.py — Índex de relacions del corpusFJE (briefing 13).

Derivat DETERMINISTA (sense LLM) per a la via OFFLINE d'autoria de fitxes:
recorre tots els documents del corpus, n'extreu front-matter + secció `## Fonts`
+ enllaços doc↔doc, i emet un índex de relacions (NO graph; graph-upgradable)
amb `documents[]`, `perTema` i `perFase`.

Universe = `corpusFJE/_manifest.json` (el conjunt de "documents" que el corpus
reconeix: 232 `.md` de contingut M0-M11 + JSON de currículum). El manifest fixa
QUÈ és un document i la seva classificació de mòdul; aquest script ENRIQUEIX cada
doc obrint el `.md` per a `paraules_clau`, `block`, `id`, la secció de Fonts i els
enllaços markdown a altres docs.

Direcció única: corpusFJE (font) → [aquest script] → `_index_relacions.json`.
Esquema segons `mirar-coms/briefings/13-index-relacions-corpus-per-mineria.md`.

`perObjectiuADD` NO s'emet en v1: requereix el mapatge bloc→codi A-D-D que viu
app-side (Itinerarium). En el seu lloc s'emet `perFase` (derivable del corpus).
Quan Itinerarium ens passi la taula bloc→codi, s'afegeix sense rehacer la resta.

Ús:
    python build_index_relacions.py            # escriu el JSON i mostra stats
    python build_index_relacions.py --check    # no escriu; surt !=0 si hi ha drift
    python build_index_relacions.py --no-curriculum   # omet els nodes de currículum
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

import yaml

# Consola de Windows (cp1252) → UTF-8 per als accents del log.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Arrel del corpus: per defecte l'arrel del repo (aquest script viu a .tooling/),
# així corre igual a la GitHub Action i en local. Override amb CORPUS_DIR si cal.
CORPUS = Path(os.environ.get("CORPUS_DIR") or Path(__file__).resolve().parent.parent)
MANIFEST = CORPUS / "_manifest.json"
OUT = CORPUS / "_relacions-corpus.json"

VERSION = "1.0"
GENERAT = "2026-06-11"  # segell fix: els scripts deterministes no fan Date.now()
FONT_DESC = (
    "Derivat del front-matter i les seccions ## Fonts dels docs de corpusFJE. "
    "Índex de relacions (no graph). Graph-upgradable. Join amb l'app per slug de "
    "tema i id de dinàmica. Universe = _manifest.json."
)

# ── Regex de domini ───────────────────────────────────────────────────────────
FM_SPLIT = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FONTS_HEADING = re.compile(
    r"^(#{2,4})\s+(?:\d+(?:\.\d+)*\.?\s*)?(fonts|refer[eè]ncies|bibliografia)\b", re.I
)
MD_LINK = re.compile(r"\]\(\s*(?:<)?([^)>\s]+?\.md)(?:#[^)>]*)?(?:>)?\s*\)")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.*\S)\s*$")
EMPH = re.compile(r"\*\*?(.+?)\*\*?")
LINK_TEXT = re.compile(r"\[([^\]]+)\]\([^)]*\)")
MOD_PREFIX = re.compile(r"^M\d+_")
FAMILY_PREFIX = re.compile(r"^(?:dinamica-|genere-|protocol-)")

# Tags estructurals (no temàtics): s'exclouen de `temes` i del fallback de
# relacionats, perquè tota dinàmica els porta i no indiquen relació de contingut.
HARD_STOP_TAGS = {
    "dinamica-formacio", "a-d-d", "cpa", "abans", "durant", "despres",
    "transversal", "formacio",
}
# Un tag present en més de STOP_DF docs és massa genèric per indicar una relació
# pairwise específica (s'usa només al fallback de tags compartits).
STOP_DF = 15

# Mapatge bloc → codi A-D-D (BLOCK2CODE d'Itinerarium, briefing 17 §1). El codi
# ja codifica la fase (A-* abans, D-* durant, Ds-* despres). Els protocols de
# facilitació (phase: transversal) NO tenen bloc aquí → cap objectiu.
BLOCK2CODE = {
    "Visió i compromís amb la missió": "A-1",
    "Diagnòstic honest de la realitat": "A-2",
    "Objectius i teoria del canvi": "A-3",
    "Vincles, cura mútua i llenguatge compartit": "A-4",
    "Aprenentatge actiu": "D-1",
    "Reflexió durant la pràctica": "D-2",
    "Implementació acompanyada": "D-3",
    "Cura emocional del canvi": "D-4",
    "Transferència real a l'aula": "Ds-1",
    "Seguiment i evidències documentades": "Ds-2",
    "Reflexió post-pràctica": "Ds-3",
    "Impacte mesurable en l'alumnat": "Ds-4",
}


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = s.replace("·", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def strip_md(s: str) -> str:
    """Treu èmfasi i deixa el text dels enllaços markdown (per a entrades de Fonts)."""
    s = LINK_TEXT.sub(r"\1", s)
    s = EMPH.sub(r"\1", s)
    return s.strip()


def stem_of(path: str) -> str:
    """Nom de fitxer sense extensió (clau de node candidata)."""
    return Path(path).stem


def topic_slug(stem: str) -> str:
    """Slug temàtic: treu el prefix de mòdul (M0_) i de família (dinamica-/genere-)."""
    t = MOD_PREFIX.sub("", stem)
    t = FAMILY_PREFIX.sub("", t)
    return slugify(t)


# ── Parsing d'un .md de contingut ─────────────────────────────────────────────
def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_SPLIT.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        if not isinstance(fm, dict):
            fm = {}
    except yaml.YAMLError:
        fm = {}
    return fm, m.group(2)


def section_lines(body: str, heading_re: re.Pattern) -> list[str]:
    """Retorna les línies sota el primer heading que casa, fins al següent heading
    de nivell <= el del heading trobat (o EOF)."""
    lines = body.splitlines()
    start = None
    level = 0
    for i, ln in enumerate(lines):
        m = heading_re.match(ln)
        if m:
            start = i + 1
            level = len(m.group(1))
            break
    if start is None:
        return []
    out = []
    for ln in lines[start:]:
        h = HEADING.match(ln)
        if h and len(h.group(1)) <= level:
            break
        out.append(ln)
    return out


def extract_fonts(body: str) -> list[str]:
    block = section_lines(body, FONTS_HEADING)
    fonts: list[str] = []
    for ln in block:
        m = LIST_ITEM.match(ln)
        if m:
            txt = strip_md(m.group(1))
            if txt:
                fonts.append(txt)
    if not fonts:  # sense llista: agafa línies de prosa no buides
        for ln in block:
            t = strip_md(ln.strip())
            if t and not t.startswith(("|", ">")):
                fonts.append(t)
    # dedup preservant ordre
    seen, uniq = set(), []
    for f in fonts:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    return uniq


def extract_md_links(body: str) -> list[str]:
    return [m.group(1) for m in MD_LINK.finditer(body)]


# ── Build ─────────────────────────────────────────────────────────────────────
def load_universe() -> list[dict]:
    """Aplana el manifest a una llista d'entrades amb el seu grup de mòdul."""
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = []
    for modul, entries in data["modules"].items():
        for e in entries:
            rows.append({**e, "modul": modul})
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="No escriu; !=0 si hi ha drift.")
    ap.add_argument("--no-curriculum", action="store_true", help="Omet els nodes de currículum.")
    args = ap.parse_args()

    rows = load_universe()

    # 1a passada: id estable per path (basename; si col·lisió, ruta relativa).
    stems: dict[str, int] = {}
    for r in rows:
        stems[stem_of(r["path"])] = stems.get(stem_of(r["path"]), 0) + 1
    relpath_noext_to_id: dict[str, str] = {}
    for r in rows:
        rel = r["path"][:-3] if r["path"].endswith(".md") else Path(r["path"]).with_suffix("").as_posix()
        st = stem_of(r["path"])
        relpath_noext_to_id[rel] = st if stems[st] == 1 else Path(r["path"]).with_suffix("").as_posix()

    documents: list[dict] = []
    raw_links: dict[str, list[str]] = {}      # id → [target relpath_noext]
    tags_by_id: dict[str, set] = {}
    modul_by_id: dict[str, str] = {}
    n_curriculum = n_content = n_fonts = 0

    for r in rows:
        path = r["path"]
        is_curr = path.startswith("curriculum/")
        if is_curr and args.no_curriculum:
            continue
        rel_noext = path[:-3] if path.endswith(".md") else Path(path).with_suffix("").as_posix()
        node_id = relpath_noext_to_id[rel_noext]
        modul = r["modul"]
        tipus = r.get("tipus")
        titol = r.get("titol") or stem_of(path)

        node = {
            "id": node_id,
            "path": path,
            "modul": modul,
            "tipus": tipus,
            "titol": titol,
            "fase": None,
            "tags": [],
            "temes": [],
            "fonts": [],
            "relacionats": [],
        }

        temes: set = set()
        if is_curr:
            n_curriculum += 1
            # tema dels segments de la ruta (etapa + matèria) + slug del títol
            parts = [p for p in Path(path).parts[1:-1]]  # entre 'curriculum/' i el fitxer
            for p in parts:
                temes.add(slugify(p))
            temes.add(topic_slug(stem_of(path)))
            temes.add(slugify(titol))
            node["fase"] = None
        else:
            n_content += 1
            text = (CORPUS / path).read_text(encoding="utf-8", errors="replace")
            fm, body = parse_frontmatter(text)

            pclau = fm.get("paraules_clau") or []
            if isinstance(pclau, str):
                pclau = [pclau]
            tags = [str(t).strip() for t in pclau if str(t).strip()]
            node["tags"] = tags

            phase = fm.get("phase")
            if phase in ("abans", "durant", "despres", "transversal"):
                node["fase"] = phase
            if tipus == "dinamica" and fm.get("id"):
                node["dinamica_id"] = str(fm["id"])          # join amb data/dinamiques.json
            if fm.get("block"):
                node["block"] = str(fm["block"])

            fonts = extract_fonts(body)
            node["fonts"] = fonts
            if fonts:
                n_fonts += 1

            # temes: slug temàtic del fitxer + tags (sense els estructurals)
            temes.add(topic_slug(stem_of(path)))
            for t in tags:
                s = slugify(t)
                if s and s not in HARD_STOP_TAGS:
                    temes.add(s)

            raw_links[node_id] = extract_md_links(body)

        temes.discard("")
        node["temes"] = sorted(temes)
        documents.append(node)
        tags_by_id[node_id] = set(slugify(t) for t in node["tags"])
        modul_by_id[node_id] = modul

    valid_ids = {d["id"] for d in documents}

    # 2a passada: relacionats = enllaços markdown explícits (resolts) + fallback
    # de tags compartits (≥2) dins el mateix mòdul.
    by_id = {d["id"]: d for d in documents}
    for node_id, targets in raw_links.items():
        src_dir = Path(by_id[node_id]["path"]).parent
        rels: set = set()
        for tgt in targets:
            # resol relatiu a la carpeta del doc; normalitza a ruta de corpus
            try:
                resolved = (src_dir / tgt).resolve().relative_to(CORPUS.resolve()).as_posix()
            except Exception:
                resolved = tgt
            key = resolved[:-3] if resolved.endswith(".md") else resolved
            tid = relpath_noext_to_id.get(key)
            if tid and tid in valid_ids and tid != node_id:
                rels.add(tid)
        by_id[node_id]["relacionats"] = sorted(rels)

    # fallback de tags compartits: només tags DISCRIMINATIUS (ni estructurals ni
    # massa freqüents), llindar ≥2 compartits, dins el mateix mòdul. Evita que les
    # dinàmiques (que comparteixen tags genèrics) quedin totes connectades entre si.
    from collections import Counter
    df = Counter()
    for ts in tags_by_id.values():
        df.update(ts)
    disc_by_id = {
        i: {t for t in ts if t not in HARD_STOP_TAGS and df[t] <= STOP_DF}
        for i, ts in tags_by_id.items()
    }
    tagged = [i for i, t in disc_by_id.items() if t]
    for i in tagged:
        if by_id[i]["relacionats"]:
            continue  # ja té arestes explícites; no afegim soroll
        ti, mi = disc_by_id[i], modul_by_id[i]
        shared = sorted(
            j for j in tagged
            if j != i and modul_by_id[j] == mi and len(ti & disc_by_id[j]) >= 2
        )
        if shared:
            by_id[i]["relacionats"] = shared

    # índexs invertits
    documents.sort(key=lambda d: d["id"])
    per_tema: dict[str, list[str]] = {}
    for d in documents:
        for t in d["temes"]:
            per_tema.setdefault(t, []).append(d["id"])
    per_tema = {t: sorted(ids) for t, ids in sorted(per_tema.items())}

    per_fase: dict[str, list[str]] = {}
    for d in documents:
        if d["fase"]:
            per_fase.setdefault(d["fase"], []).append(d["id"])
    per_fase = {f: sorted(ids) for f, ids in per_fase.items()}

    # perObjectiuADD: dinàmiques (no transversals) → codi A-D-D via BLOCK2CODE.
    per_objectiu: dict[str, list[str]] = {}
    unmapped_blocks: set = set()
    for d in documents:
        if d.get("tipus") != "dinamica" or d.get("fase") == "transversal":
            continue
        block = d.get("block")
        if not block:
            continue
        code = BLOCK2CODE.get(block)
        if code:
            per_objectiu.setdefault(code, []).append(d["id"])
        else:
            unmapped_blocks.add(block)
    per_objectiu = {c: sorted(ids) for c, ids in sorted(per_objectiu.items())}

    n_rel = sum(1 for d in documents if d["relacionats"])
    index = {
        "version": VERSION,
        "generat": GENERAT,
        "font": FONT_DESC,
        "stats": {
            "documents": len(documents),
            "contingut": n_content,
            "curriculum": n_curriculum,
            "amb_fonts": n_fonts,
            "amb_relacionats": n_rel,
            "temes": len(per_tema),
            "objectius_A-D-D": len(per_objectiu),
        },
        "documents": documents,
        "perTema": per_tema,
        "perFase": per_fase,
        "perObjectiuADD": per_objectiu,
    }
    if unmapped_blocks:
        print(f"⚠️  blocks de dinàmica sense codi a BLOCK2CODE: {sorted(unmapped_blocks)}", file=sys.stderr)

    payload = json.dumps(index, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != payload:
            print("DRIFT: _index_relacions.json no coincideix amb el corpus actual.", file=sys.stderr)
            return 1
        print(f"OK — {len(documents)} docs, índex sincronitzat.")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    s = index["stats"]
    print(f"✅ Índex escrit a {OUT}")
    print(f"   Documents: {s['documents']}  (contingut {s['contingut']} · currículum {s['curriculum']})")
    print(f"   Amb ## Fonts: {s['amb_fonts']}   ·   amb relacionats: {s['amb_relacionats']}")
    print(f"   Temes (perTema): {s['temes']}   ·   fases (perFase): {list(per_fase)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
