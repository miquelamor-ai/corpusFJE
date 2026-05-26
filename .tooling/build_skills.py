"""build_skills.py — generador determinista de derivats per a instruments i gèneres discursius.

Parsa un M*.md canònic (`tipus: instrument` o `tipus: genere-discursiu`) i en deriva
dos artefactes per a ATNE:
  - SKILL.md          (LLM operador, format vertical jerarquitzat per nivell)
  - prompt_adapter.md (LLM adapter, parametritzat per nivell)

Sense LLM. Generació 100% determinista a partir de la taula §4.X.4 i les
metadades §4.X.5. Coherència garantida amb la font; sortida reproduïble.

El derivat `rubrica_avaluacio_<niv>.md` (graella per al docent) s'ha
APARCAT (2026-05-24) fins que existeixi un consumidor — scriptorium amb
mòdul d'avaluació o ATNE en mode avaluador. La seva generació
requereix LLM-jutge per a les bandes Encara no/En procés/Aconseguit;
no aporta valor sense interfície per consumir-lo.

Sortida per defecte: `<directori del M*.md>/_derivats_v2/` perquè
**no es sobreescrigui** el SKILL.md productiu que ATNE consumeix avui.
Al moment del switch coordinat, els fitxers de `_derivats_v2/` reemplacen
els de producció en un únic commit.

Ús:
    python build_skills.py <M*.md> [--out <dir>]
    # Per defecte: --out = <dir-del-M*.md>/_derivats_v2/
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml

NIVELLS = ["pre-A1", "A1", "A2", "B1", "B2", "C1+"]
NIVELL_ETIQUETA = {
    "pre-A1": "Emergent",
    "A1": "Inicial",
    "A2": "Funcional",
    "B1": "Estratègic",
    "B2": "Acadèmic",
    "C1+": "Crític",
}


@dataclass
class Cella:
    pas: str  # "1. Identificació del fet"
    dimensio: str  # "Fets clau"
    descriptors: dict[str, str] = field(default_factory=dict)  # {nivell: text}
    # metadades:
    tipus: str = ""  # countable | binary | qualitative | ...
    requires_source: str = "no"  # no | parcial | sí
    validation_hint: str = ""


@dataclass
class Instrument:
    frontmatter: dict
    body: str
    celles: list[Cella]
    descripcio: str
    heuristiques: str
    fonts: str


# -----------------------------------------------------------------------
# Parser
# -----------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("Falta frontmatter YAML al fitxer M*.md")
    return yaml.safe_load(m.group(1)), m.group(2)


def extract_section(body: str, header: str) -> str:
    """Treu el contingut entre `## header` i el següent `## `."""
    pattern = re.compile(
        rf"^##\s+{re.escape(header)}.*?\n(.*?)(?=^##\s|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else ""


def parse_modulacio_table(modulacio_md: str) -> list[Cella]:
    """Parser de la taula `## Modulació per nivell`.

    Format esperat:
        | Pas | Dimensió | Pre-A1<br>Emergent | A1<br>Inicial | ... |
        |---|---|---|---|...|
        | **1. X** | dim1 | ... | ... | ... |
        |          | dim2 | ... | ... | ... |
    """
    lines = [l for l in modulacio_md.splitlines() if l.strip().startswith("|")]
    if len(lines) < 3:
        return []
    # primera fila = capçaleres; segona = separador; resta = files
    rows = []
    pas_actual = ""
    for line in lines[2:]:
        cells = [c.strip() for c in line.split("|")[1:-1]]  # split deixa buits a borda
        if len(cells) < 3:
            continue
        pas_cell = cells[0]
        if pas_cell:
            # neteja "**N. Nom**" → "N. Nom"
            pas_actual = re.sub(r"^\*\*|\*\*$", "", pas_cell).strip()
        dimensio = cells[1]
        descriptors = dict(zip(NIVELLS, cells[2:8]))
        rows.append(Cella(pas=pas_actual, dimensio=dimensio, descriptors=descriptors))
    return rows


def parse_metadades_table(metadades_md: str) -> dict[str, dict]:
    """Parser de `## Metadades de cel·la`.

    Retorna dict[clau] = {tipus, requires_source, validation_hint}
    on clau = "1.1" o equivalent (la primera columna de la taula).
    """
    lines = [l for l in metadades_md.splitlines() if l.strip().startswith("|")]
    if len(lines) < 3:
        return {}
    result = {}
    for line in lines[2:]:
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 4:
            continue
        clau_completa, tipus, req, hint = cells[:4]
        # extreu "1.1" de "1.1 Fets clau"
        m = re.match(r"^(\d+(?:\.\d+)?)\b", clau_completa)
        if not m:
            continue
        clau = m.group(1)
        result[clau] = {
            "tipus": tipus.strip("`"),
            "requires_source": req,
            "validation_hint": hint,
        }
    return result


def annotate_celles(celles: list[Cella], metadades: dict[str, dict]) -> None:
    """Lliga cada cel·la amb les seves metadades segons posició Pas.Dimensió."""
    # Recompte de dimensions per pas per generar la clau 1.1, 1.2, 2.1...
    pas_to_idx: dict[str, int] = {}
    for c in celles:
        pas_num_m = re.match(r"^(\d+)\.", c.pas)
        if not pas_num_m:
            continue
        pas_num = pas_num_m.group(1)
        pas_to_idx.setdefault(pas_num, 0)
        pas_to_idx[pas_num] += 1
        clau_amb_dim = f"{pas_num}.{pas_to_idx[pas_num]}"
        clau_simple = pas_num  # casos sense subdimensió (1 sola fila)
        meta = metadades.get(clau_amb_dim) or metadades.get(clau_simple)
        if meta:
            c.tipus = meta["tipus"]
            c.requires_source = meta["requires_source"]
            c.validation_hint = meta["validation_hint"]


def parse_instrument(path: Path) -> Instrument:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    modulacio = extract_section(body, "Modulació per nivell")
    metadades = extract_section(body, "Metadades de cel·la")
    descripcio = extract_section(body, "Descripció")
    heuristiques = extract_section(body, "Heurístiques docent")
    fonts = extract_section(body, "Fonts principals")
    celles = parse_modulacio_table(modulacio)
    metad_dict = parse_metadades_table(metadades)
    annotate_celles(celles, metad_dict)
    return Instrument(
        frontmatter=fm,
        body=body,
        celles=celles,
        descripcio=descripcio,
        heuristiques=heuristiques,
        fonts=fonts,
    )


# -----------------------------------------------------------------------
# Generadors de derivats
# -----------------------------------------------------------------------


def sha256_of_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def derivat_frontmatter(
    instrument: Instrument, font_path: Path, vista: str, nivell: str | None = None
) -> str:
    fm = {
        "tipus": "derivat",
        "font_canonic": font_path.name,
        "font_version": instrument.frontmatter.get("version", "unknown"),
        "vista": vista,
        "generat_at": date.today().isoformat(),
        "generat_per": "build_skills.py@prototip-2026-05-24",
        "checksum_font": sha256_of_file(font_path),
    }
    if nivell:
        fm["nivell_objectiu"] = nivell
        fm["escala"] = ["Encara no", "En procés", "Aconseguit"]
    return "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n"


# Camps Agent Skills (consumits per ATNE skills_loader.py):
# - name, description, author, version, agent_role, tools_required, triggers
# - genre_key (gèneres) o complement_key (mediació)
# - opcionals: tipologia, mecr_range, translanguaging, multimodal, moduls_relacionats
AGENT_SKILLS_FIELDS = {
    "name", "description", "author", "version", "agent_role",
    "tools_required", "triggers", "genre_key", "complement_key",
    "tipologia", "mecr_range", "translanguaging", "multimodal",
    "moduls_relacionats", "skill_meta",
}


def _read_existing_skill_frontmatter(skill_path: Path) -> dict | None:
    """Llegeix el SKILL.md de producció (paral·lel al M*.md font) i extreu
    el seu frontmatter Agent Skills. Retorna None si no existeix."""
    if not skill_path.is_file():
        return None
    text = skill_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None


def _derive_agent_skills_frontmatter(instrument: Instrument, font_path: Path) -> dict:
    """Construeix el frontmatter Agent Skills des del M*.md font quan no hi ha
    SKILL.md previ. Usat per als instruments NOUS sense SKILL.md de producció."""
    skill_folder = font_path.parent
    skill_name = skill_folder.name  # p.ex. "write-noticia" o "generate-glossari"
    src_fm = instrument.frontmatter

    fm = {
        "name": skill_name,
        "description": src_fm.get("descripcio", "").strip(),
        "author": "FJE — Fundació Jesuïtes Educació",
        "version": src_fm.get("version", "4.0.0-canonic"),
        "tools_required": [],
    }

    # agent_role: agafa primer d'agent_roles[] o defalleix a heurística pel nom
    roles = src_fm.get("agent_roles", [])
    if roles:
        fm["agent_role"] = roles[0]
    else:
        fm["agent_role"] = "complements" if skill_name.startswith("generate-") else "adapter"

    # triggers + key segons categoria
    if "genre_key" in src_fm:
        fm["genre_key"] = src_fm["genre_key"]
        fm["triggers"] = [{"path": "params.genere_discursiu", "equals": src_fm["genre_key"]}]
    elif "complement_key" in src_fm:
        fm["complement_key"] = src_fm["complement_key"]
        fm["triggers"] = [{"path": f"params.complements.{src_fm['complement_key']}", "equals": True}]

    # Opcionals propagats si existeixen
    for k in ("tipologia", "mecr_range", "translanguaging", "multimodal", "moduls_relacionats"):
        if k in src_fm:
            fm[k] = src_fm[k]

    return fm


def skill_md_frontmatter(instrument: Instrument, font_path: Path) -> str:
    """Genera frontmatter del SKILL.md derivat amb compatibilitat Agent Skills.

    Estratègia híbrida:
    - Si existeix SKILL.md de producció paral·lel: preserva el seu frontmatter
      Agent Skills (name, description, agent_role, triggers...) i hi afegeix
      camps de traçabilitat. Manté la 'description' en anglès curat.
    - Si no existeix (instruments nous): construeix el frontmatter Agent Skills
      des del M*.md font.
    - Sempre afegeix camps de traçabilitat: font_canonic, font_version,
      generat_at, checksum_font.
    """
    skill_path = font_path.parent / "SKILL.md"
    existing = _read_existing_skill_frontmatter(skill_path)

    if existing and existing.get("name"):
        # Preserva Agent Skills existent i actualitza només camps de traçabilitat.
        fm = {k: v for k, v in existing.items() if k in AGENT_SKILLS_FIELDS}
        # Actualitza version i moduls_relacionats des del M*.md (fonts de veritat)
        src_fm = instrument.frontmatter
        if "version" in src_fm:
            fm["version"] = src_fm["version"]
        if "moduls_relacionats" in src_fm:
            fm["moduls_relacionats"] = src_fm["moduls_relacionats"]
    else:
        # No hi ha SKILL.md previ: construeix tot des del M*.md font.
        fm = _derive_agent_skills_frontmatter(instrument, font_path)

    # Camps de traçabilitat (sempre afegits)
    fm["font_canonic"] = font_path.name
    fm["font_version"] = instrument.frontmatter.get("version", "unknown")
    fm["generat_at"] = date.today().isoformat()
    fm["generat_per"] = "build_skills.py@v2-2026-05-26"
    fm["checksum_font"] = sha256_of_file(font_path)

    return "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n"


def is_no_aplicable(descriptor: str) -> bool:
    t = descriptor.strip().lower()
    return t in {"—", "-", "n/a", "no aplicable.", "no aplica."} or t.startswith(
        "no aplicable"
    )


def generar_skill_md(instrument: Instrument, font_path: Path) -> str:
    # Frontmatter Agent Skills compatible (preservat o derivat) + traçabilitat
    fm_block = skill_md_frontmatter(instrument, font_path)
    titol = instrument.frontmatter.get("titol", font_path.stem)
    parts = [fm_block, f"# {titol} — skill operativa per a LLM\n\n"]
    parts.append(instrument.descripcio + "\n\n")
    parts.append("## Modulació per nivell (format vertical jerarquitzat)\n\n")
    for nivell in NIVELLS:
        etiqueta = NIVELL_ETIQUETA[nivell]
        parts.append(f"### {nivell} — {etiqueta}\n\n")
        pas_actual = ""
        for c in instrument.celles:
            desc = c.descriptors.get(nivell, "").strip()
            if not desc or is_no_aplicable(desc):
                continue
            if c.pas != pas_actual:
                parts.append(f"\n**{c.pas}**\n")
                pas_actual = c.pas
            parts.append(f"- {c.dimensio}: {desc}\n")
        parts.append("\n")
    return "".join(parts)


# NOTA: la funció generar_rubrica_avaluacio() ha quedat APARCADA (2026-05-24).
# Requereix LLM-jutge per generar el feedback per banda i no té consumidor avui.
# Es restaurarà quan scriptorium tingui mòdul d'avaluació o ATNE mode avaluador.


def generar_prompt_adapter(instrument: Instrument, font_path: Path) -> str:
    fm_block = derivat_frontmatter(instrument, font_path, vista="C.prompt-adapter-llm")
    titol = instrument.frontmatter.get("titol", font_path.stem)
    parts = [
        fm_block,
        f"# {titol} — prompt d'adaptació parametritzat per nivell\n\n",
        "Aquest prompt s'omple amb el nivell objectiu MECR (`{{NIVELL}}`) i opcionalment amb les variables de perfil (`{{fase_lectora}}`).\n\n",
        "## Plantilla\n\n",
        "```\n",
        f"Adapta el text font següent al gènere {titol.lower()} per a un alumne de nivell {{{{NIVELL}}}} ({{{{ETIQUETA_MALL}}}}).\n",
        "\n",
        "Segueix aquests criteris (extrets de la rúbrica canònica):\n",
        "\n",
        "{{LLISTA_DESCRIPTORS_DEL_NIVELL}}\n",
        "\n",
        "Criteris transversals (cal complir a tots els nivells):\n",
        "{{LLISTA_CRITERIS_TRANSVERSALS}}\n",
        "\n",
        "Text font:\n",
        "{{TEXT_FONT}}\n",
        "```\n\n",
        "## Llistes per nivell (per a substitució)\n\n",
    ]
    for nivell in NIVELLS:
        etiqueta = NIVELL_ETIQUETA[nivell]
        parts.append(f"### `{{{{LLISTA_DESCRIPTORS_DEL_NIVELL}}}}` per a {nivell} ({etiqueta})\n\n")
        for c in instrument.celles:
            desc = c.descriptors.get(nivell, "").strip()
            if not desc or is_no_aplicable(desc):
                continue
            if c.pas.startswith(("7.", "8.")):  # criteris transversals i metacognitiu fora
                continue
            parts.append(f"- **{c.dimensio}**: {desc}\n")
        parts.append("\n")
    return "".join(parts)


# -----------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("font", type=Path, help="ruta al M*.md canònic")
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="directori de sortida (per defecte: <dir-font>/_derivats_v2/)",
    )
    args = ap.parse_args()

    if not args.font.is_file():
        print(f"ERROR: no existeix {args.font}", file=sys.stderr)
        return 2

    print(f"-> Parsing {args.font.name}...")
    instrument = parse_instrument(args.font)
    print(f"  Frontmatter: {len(instrument.frontmatter)} camps")
    print(f"  Cel.les modulacio: {len(instrument.celles)}")
    print(f"  Cel.les amb metadades tipus: {sum(1 for c in instrument.celles if c.tipus)}")
    print(f"  Cel.les sense metadades: {sum(1 for c in instrument.celles if not c.tipus)}")

    out = args.out if args.out else args.font.parent / "_derivats_v2"
    out.mkdir(parents=True, exist_ok=True)

    skill_path = out / "SKILL.md"
    skill_path.write_text(generar_skill_md(instrument, args.font), encoding="utf-8")
    print(f"  [OK] {skill_path}")

    adapter_path = out / "prompt_adapter.md"
    adapter_path.write_text(generar_prompt_adapter(instrument, args.font), encoding="utf-8")
    print(f"  [OK] {adapter_path}")

    print("Fet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
