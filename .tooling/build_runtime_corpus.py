#!/usr/bin/env python3
"""build_runtime_corpus.py — variant RUNTIME de l'índex (briefing 17 §2, opció A).

Deriva, des de l'índex offline (`_index_relacions.json`) + els `.md` de contingut
del corpus, els fitxers que consumeix Itinerarium en RUNTIME per enriquir les
propostes de tema lliure:

    data/corpus/_index.json        — {temes:[{slug,tema,tags,nItems}]} per al fuzzy-match
    data/corpus/<slug>.json        — {objectius,fragments,evidencies}, un per tema

OPCIÓ A (determinista, briefing 18): cada ítem porta `font` = el DOCUMENT del
corpus (verbatim, traçable, citable), NO una font bibliogràfica per frase (això
exigiria un LLM + gate). Contracte d'ítem: {text, doc, font} — sense `font` no
s'inclou. Només material verbatim del corpus; cap inferència.

Abast: NOMÉS docs de CONTINGUT (M0-M11). El currículum (JSON) queda fora del
runtime de formació docent. Un tema sense material de contingut → cap fitxer.

Ús:
    python index_relacions/build_runtime_corpus.py            # dry-run (stats + mostra)
    python index_relacions/build_runtime_corpus.py --write    # escriu a staging
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index_relacions as bx  # helpers + CORPUS

OFFLINE = bx.OUT                       # _relacions-corpus.json (màster offline)
OUT_DIR = bx.CORPUS / "data" / "corpus"  # carpeta servida a Itinerarium
GENERAT = bx.GENERAT
FRAG_MAX = 300
MAX_OBJ_PER_DOC = 8
MAX_ITEMS_PER_TEMA = 15
MIN_ITEMS = 3  # llindar de riquesa (Itinerarium briefing 19): es cura el soroll a l'origen

OBJECTIUS_H = re.compile(r"^(#{2,4})\s+(?:\d+(?:\.\d+)*\.?\s*)?Objectius\b", re.I)
ABSTRACT_H = re.compile(r"^(#{2,4})\s+(?:\d+(?:\.\d+)*\.?\s*)?Abstract\b", re.I)


# Nota de contracte per al camp `evidencies` (explícita, a cada fitxer + a _index).
EV_NOTA = (
    "Camp reservat per a l'opció B (material bibliogràfic gated). Buit a l'opció A; "
    "NO és un error i el consumidor no l'ha de tractar com a tal ni construir-hi en contra."
)

# Elisions catalanes: "en l alumnat" → "en l'alumnat", "d aprenentatge" → "d'aprenentatge".
APOS = re.compile(r"\b([ldsnmt]) ")


def prettify(slug: str) -> str:
    """Etiqueta llegible per a un docent des d'un slug (sense guions ni majúscules rares)."""
    s = APOS.sub(r"\1'", slug.replace("-", " ").strip())
    return (s[:1].upper() + s[1:]) if s else slug


def font_str(titol: str) -> str:
    """Citació visible (briefing 19): 'corpusFJE · <títol del doc>'. El `doc` (id)
    queda per a traçabilitat/join."""
    return f"corpusFJE · {titol}"


def short(text: str, maxlen: int = FRAG_MAX) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= maxlen:
        return text
    cut = text[:maxlen].rsplit(" ", 1)[0].rstrip(",;:· ")
    return cut + "…"


def extract_doc(path: str) -> dict:
    """objectius (## Objectius) + fragment (## Abstract o descripcio), verbatim."""
    text = (bx.CORPUS / path).read_text(encoding="utf-8", errors="replace")
    fm, body = bx.parse_frontmatter(text)
    objectius = []
    for ln in bx.section_lines(body, OBJECTIUS_H):
        m = bx.LIST_ITEM.match(ln)
        if m:
            t = bx.strip_md(m.group(1))
            if t:
                objectius.append(t)
    abstract = " ".join(l for l in bx.section_lines(body, ABSTRACT_H)).strip()
    fragment = short(bx.strip_md(abstract)) if abstract else None
    if not fragment and fm.get("descripcio"):
        fragment = short(bx.strip_md(str(fm["descripcio"])))
    return {"objectius": objectius[:MAX_OBJ_PER_DOC], "fragment": fragment}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Escriu els fitxers a staging.")
    args = ap.parse_args()

    idx = json.loads(OFFLINE.read_text(encoding="utf-8"))
    doc_meta = {d["id"]: d for d in idx["documents"]}
    per_tema = idx["perTema"]
    # etiquetes netes: els temes que vénen d'un `block` reusen el nom clar del block.
    block_labels = {bx.slugify(d["block"]): d["block"] for d in idx["documents"] if d.get("block")}

    # cache d'extracció per doc de contingut
    cache: dict[str, dict] = {}

    def get(doc_id: str) -> dict | None:
        d = doc_meta.get(doc_id)
        if not d or d["path"].startswith("curriculum/"):
            return None  # només contingut
        if doc_id not in cache:
            cache[doc_id] = extract_doc(d["path"])
        return cache[doc_id]

    tema_files: dict[str, dict] = {}
    truncated = 0
    for slug, ids in per_tema.items():
        objectius, fragments = [], []
        tags: set = set()
        for doc_id in ids:
            ex = get(doc_id)
            if ex is None:
                continue
            d = doc_meta[doc_id]
            f = font_str(d.get("titol") or doc_id)
            for t in d.get("tags", []):
                tags.add(t)
            for o in ex["objectius"]:
                objectius.append({"text": o, "doc": doc_id, "font": f})
            if ex["fragment"]:
                fragments.append({"text": ex["fragment"], "doc": doc_id, "font": f})
        items = objectius + fragments
        if len(items) < MIN_ITEMS:
            continue  # sota el llindar de riquesa (o sense material) → cap fitxer
        # cap d'ítems per tema (prioritza objectius)
        if len(items) > MAX_ITEMS_PER_TEMA:
            truncated += 1
            keep_obj = objectius[:MAX_ITEMS_PER_TEMA]
            keep_frag = fragments[: max(0, MAX_ITEMS_PER_TEMA - len(keep_obj))]
            objectius, fragments = keep_obj, keep_frag
        tema_files[slug] = {
            "version": "1.0",
            "generat": GENERAT,
            "slug": slug,
            "tema": block_labels.get(slug) or prettify(slug),
            "font": "Derivat de _relacions-corpus.json · opció A: material verbatim del corpus, font = document (no biblio per frase)",
            "objectius": objectius,
            "fragments": fragments,
            "evidencies": [],  # opció A: no derivable per frase sense LLM+gate
            "nota_evidencies": EV_NOTA,
            "nItems": len(objectius) + len(fragments),
        }

    index_file = {
        "version": "1.0",
        "generat": GENERAT,
        "font": "Temes amb material de corpus citable (opció A determinista, font=document).",
        "nota_evidencies": EV_NOTA,
        "temes": [
            {"slug": s, "tema": tf["tema"], "tags": sorted(
                {t for did in per_tema[s] if (m := doc_meta.get(did)) and not m["path"].startswith("curriculum/")
                 for t in m.get("tags", []) if bx.slugify(t) not in bx.HARD_STOP_TAGS}), "nItems": tf["nItems"]}
            for s, tf in sorted(tema_files.items())
        ],
    }

    n_obj = sum(len(tf["objectius"]) for tf in tema_files.values())
    n_frag = sum(len(tf["fragments"]) for tf in tema_files.values())
    print(f"Temes amb material: {len(tema_files)}  ·  objectius: {n_obj}  ·  fragments: {n_frag}")
    print(f"Temes amb truncació (>{MAX_ITEMS_PER_TEMA} ítems): {truncated}")
    top = sorted(tema_files.values(), key=lambda t: -t["nItems"])[:6]
    print("Top temes per nItems:")
    for t in top:
        print(f"   {t['slug']}: {t['nItems']} ítems ({len(t['objectius'])} obj + {len(t['fragments'])} frag)")

    if not args.write:
        # mostra un fitxer d'exemple
        ex = next((tf for tf in tema_files.values() if tf["objectius"]), next(iter(tema_files.values())))
        print("\n=== mostra: data/corpus/" + ex["slug"] + ".json ===")
        print(json.dumps(ex, ensure_ascii=False, indent=2)[:1400])
        print("\nDry-run: cap fitxer escrit. Torna amb --write per generar a staging.")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUT_DIR.glob("*.json"):  # neteja temes obsolets entre execucions
        old.unlink()
    (OUT_DIR / "_index.json").write_text(json.dumps(index_file, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for slug, tf in tema_files.items():
        (OUT_DIR / f"{slug}.json").write_text(json.dumps(tf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n📦 Escrits {len(tema_files)} fitxers de tema + _index.json a {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
