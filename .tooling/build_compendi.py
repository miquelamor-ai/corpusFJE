# -*- coding: utf-8 -*-
"""
build_compendi.py — Generador de compendis imprimibles (PDF) del corpus FJE.

Pensat per córrer com a GitHub Action (runner Ubuntu amb Chromium) o en local
(Windows amb Microsoft Edge). NO fa servir cap LLM: extracció determinista.

Entrada: una especificació JSON de selecció, via variable d'entorn COMPENDI_SPEC
o com a primer argument (ruta a un fitxer .json).

    {
      "mode":    "per-module" | "combined" | "per-document",
      "modules": ["M1", "M3"],                         # mòduls sencers (M{n}_*.md a l'arrel)
      "files":   ["M3_generes-discursius.md",          # fitxers concrets (ruta relativa al repo)
                  "skills/generes/write-opinio/M3_genere-escriure-opinio.md"],
      "title":   "Nom del volum",                      # opcional (mode combined)
      "presets": ["generes"]                           # opcional: reculls predefinits
    }

Sortida: PDFs a la carpeta COMPENDI_OUT (per defecte "compendi/").

Render: Chromium/Edge headless (--print-to-pdf). Post-procés: PyMuPDF (fitz).
Origen: port de mineriaRAG/scripts/generar_compendi.py.
"""
import os, re, sys, glob, json, shutil, tempfile, subprocess, pathlib, unicodedata, html as htmlmod
import markdown
import fitz  # PyMuPDF

# ---------- CONFIG ----------
CORPUS  = pathlib.Path(os.environ.get("COMPENDI_CORPUS", ".")).resolve()
OUT_DIR = (CORPUS / os.environ.get("COMPENDI_OUT", "compendi")).resolve()
TMP     = pathlib.Path(tempfile.mkdtemp(prefix="compendi_"))

TIPUS_ORDRE = {"marc": 0, "estrategia": 1, "protocol": 2,
               "caracteristica": 3, "perfil": 3, "eina": 4, "normativa": 5}

# Presets: reculls temàtics predefinits (clau -> (títol, explicació, funció que retorna fitxers))
def _preset_generes():
    files = [str(CORPUS / "M3_generes-discursius.md")] + sorted(
        glob.glob(str(CORPUS / "skills" / "generes" / "*" / "M3_genere-*.md")))
    return [f for f in files if pathlib.Path(f).exists()]

PRESETS = {
    "generes": ("Gèneres discursius",
                "Recull complet dels gèneres discursius del corpus FJE: el marc conceptual i "
                "l'inventari MALL, seguit dels gèneres concrets (narratius, descriptius, expositius, "
                "argumentatius, instructius i de l'àmbit acadèmic i professional).",
                _preset_generes),
}

MODULE_META = {
    "M0":  ("Identitat i Missió — Per a què eduquem?",
            "Fonaments de la identitat i la missió educativa de la Fundació."),
    "M1":  ("Subjecte — A qui ensenyem?",
            "Caracterització de l'alumnat divers: TEA, TDAH, dislèxia, discalcúlia, discapacitats, "
            "altes capacitats, alumnat nouvingut, vulnerabilitat socioeducativa i trastorns emocionals, "
            "amb el model de caracterització de la diversitat i els plans individuals (PI/PAD)."),
    "M2":  ("Mètode — Com ensenyem?",
            "Metodologies i instruments de mediació pedagògica: DUA, aprenentatge cooperatiu, ABP i "
            "aprenentatge-servei, gamificació, programació multinivell, bastides, càrrega cognitiva, "
            "rutines i destreses de pensament, i disseny/adaptació/selecció de materials."),
    "M3":  ("Llengua — Com vehiculem el coneixement?",
            "Tractament de les llengües i comunicació accessible: MECR, MALL, TIL/TILC, lectura fàcil, "
            "estratègies de català com a L2, translanguaging, gèneres discursius, gradació lingüística "
            "i protocols d'observació de les destreses."),
    "M4":  ("Contingut Curricular — Què ensenyem?",
            "Continguts curriculars i la seva articulació."),
    "M5":  ("Tecnopedagogia — Com integrem la tecnologia?",
            "Integració de la IA i la tecnologia a l'aula: marcs TPACK/AIA i PCEK, accessibilitat "
            "digital, prompt engineering educatiu, rols de la IA, nivells de delegació i recursos "
            "digitals per a la diversitat."),
    "M6":  ("Avaluació — Com regulem l'aprenentatge?",
            "Avaluació competencial i formativa com a reguladora de l'aprenentatge."),
    "M7":  ("Entorn, Convivència i Família — On i com vivim l'escola?",
            "Entorn escolar, convivència i relació amb les famílies."),
    "M8":  ("Governança i Seguretat — Amb quins límits operem?",
            "Governança, seguretat i límits operatius de l'organització."),
    "M9":  ("Marc Legal i Normatiu — Dins quina normativa estem?",
            "Marc legal i normatiu (extracció mecànica de fonts oficials)."),
    "M10": ("Intel·ligència Artificial — Com integrem la IA?",
            "Corpus institucional del projecte d'integració de la IA."),
    "M11": ("Desenvolupament Professional — Com creixem i ens formem?",
            "Com creix i es forma qui educa: marc competencial docent i dinàmiques de formació."),
}

# ---------- CHROMIUM / EDGE ----------
def find_chrome():
    env = os.environ.get("CHROME_BIN")
    if env and pathlib.Path(env).exists():
        return env
    for name in ("google-chrome", "google-chrome-stable", "chromium-browser", "chromium",
                 "chrome", "msedge"):
        p = shutil.which(name)
        if p:
            return p
    for p in (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        if pathlib.Path(p).exists():
            return p
    print("ERROR: no s'ha trobat cap Chromium/Chrome/Edge. Defineix CHROME_BIN.")
    sys.exit(1)

CHROME = find_chrome()

# ---------- UTILITATS ----------
def slugify(s):
    s = s.split("—")[0].strip()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "compendi"

def parse_frontmatter(text):
    meta, body = {}, text
    if text.lstrip().startswith("---"):
        m = re.match(r"^﻿?\s*---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
        if m:
            fm, body = m.group(1), m.group(2)
            for line in fm.splitlines():
                mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
                if mm:
                    meta[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return meta, body

def strip_capa3(body):
    lines = body.splitlines()
    for i, ln in enumerate(lines):
        if re.match(r"^##\s+", ln):
            low = ln.lower()
            if re.search(r"^##\s+6[\.\)]", ln) or \
               ("instruccions" in low and ("llm" in low or "agent" in low or "operativ" in low)):
                return "\n".join(lines[:i]).rstrip()
    return body

def title_from_filename(fn):
    base = re.sub(r"^M\d+_", "", fn[:-3]).replace("_", " ").replace("-", " ").strip()
    return base[:1].upper() + base[1:]

def module_of(path):
    m = re.match(r"^(M\d+)_", os.path.basename(path))
    return m.group(1) if m else ""

def esc(s):
    return htmlmod.escape(s or "")

MD = markdown.Markdown(extensions=["extra", "sane_lists", "toc"], output_format="html5")
def md_to_html(body):
    MD.reset()
    return MD.convert(body)

def docs_from_files(file_paths):
    docs = []
    for fp in file_paths:
        fn = os.path.basename(str(fp))
        txt = pathlib.Path(fp).read_text(encoding="utf-8", errors="replace")
        meta, body = parse_frontmatter(txt)
        body = strip_capa3(body)
        docs.append(dict(title=meta.get("titol") or title_from_filename(fn),
                         tipus=meta.get("tipus", ""), desc=meta.get("descripcio", ""),
                         html=md_to_html(body), fn=fn))
    docs.sort(key=lambda d: (TIPUS_ORDRE.get(d["tipus"], 9), d["title"].lower()))
    for i, d in enumerate(docs, 1):
        d["token"] = f"MDOC{i:04d}"
    return docs

# ---------- CSS ----------
CSS = """
@page { size: A4; margin: 20mm 19mm 24mm 19mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Georgia","Cambria",serif; font-size: 10.6pt; line-height: 1.5; color:#1f2733; margin:0; }
.mk { color:#fff; font-size:1px; }
h1,h2,h3,h4 { font-family:"Segoe UI","Helvetica Neue",Arial,sans-serif; color:#14315c; line-height:1.25; }
a { color:#14315c; text-decoration:none; }
p { margin:0 0 .55em; text-align:justify; }
ul,ol { margin:.2em 0 .7em 1.1em; padding-left:.6em; }
li { margin:.12em 0; }
code { font-family:Consolas,monospace; background:#eef1f6; padding:.05em .3em; border-radius:3px; font-size:.92em; }
pre { background:#f4f6fa; border:1px solid #dde3ec; border-radius:6px; padding:.7em .9em; overflow:auto; font-size:.86em; }
pre code { background:none; padding:0; }
blockquote { margin:.4em 0 .8em; padding:.2em .9em; border-left:3px solid #b9c6db; color:#42505f; background:#f6f8fb; }
table { border-collapse:collapse; width:100%; margin:.5em 0 1em; font-size:.92em; }
th,td { border:1px solid #cdd6e4; padding:.32em .5em; text-align:left; vertical-align:top; }
th { background:#e8edf5; color:#14315c; }
hr { border:none; border-top:1px solid #d6deea; margin:1.1em 0; }
.cover { height:297mm; width:210mm; position:relative; color:#fff;
         background:linear-gradient(150deg,#0e2746 0%,#14315c 45%,#1f4a86 100%);
         page-break-after:always; overflow:hidden; }
.cover .rule { position:absolute; left:26mm; width:70mm; height:4px; background:#e8b53d; top:32%; }
.cover .band { position:absolute; left:0; right:0; top:34%; padding:0 26mm; }
.cover .kicker { font-family:"Segoe UI",sans-serif; letter-spacing:.32em; text-transform:uppercase; font-size:11pt; color:#9db8e0; margin-bottom:14mm; }
.cover h1 { color:#fff; font-size:34pt; margin:0 0 6mm; line-height:1.12; }
.cover .sub { font-family:"Segoe UI",sans-serif; font-size:14pt; color:#d7e3f4; font-weight:300; }
.cover .foot { position:absolute; left:26mm; right:26mm; bottom:24mm; font-family:"Segoe UI",sans-serif; font-size:10.5pt; color:#bcd0ec; border-top:1px solid #3a5a8c; padding-top:6mm; display:flex; justify-content:space-between; }
.module { page-break-before:always; }
.module .mhead { background:linear-gradient(135deg,#14315c,#1f4a86); color:#fff; border-radius:10px; padding:10mm 11mm; margin-bottom:8mm; }
.module .mtag { font-family:"Segoe UI",sans-serif; letter-spacing:.28em; text-transform:uppercase; font-size:10pt; color:#e8b53d; }
.module .mhead h1 { color:#fff; font-size:25pt; margin:3mm 0 4mm; }
.module .mhead .expl { font-family:"Segoe UI",sans-serif; font-weight:300; font-size:11.5pt; line-height:1.55; color:#e6eefa; text-align:justify; }
.module h2.idx { font-size:13pt; color:#14315c; margin:0 0 3mm; }
.toc-entry { display:flex; align-items:baseline; margin:.18em 0; font-family:"Segoe UI",sans-serif; font-size:10.4pt; }
.toc-entry .t { white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.toc-entry .dots { flex:1 1 auto; border-bottom:1px dotted #9fb0c8; margin:0 .5em; transform:translateY(-.2em); }
.toc-entry .pg { flex:0 0 auto; min-width:2.6em; text-align:right; color:#42505f; font-variant-numeric:tabular-nums; }
.toc-entry .tipus { color:#7587a0; font-weight:400; font-size:9pt; margin-left:.5em; }
.doc { page-break-before:always; }
.doc .dhead { border-bottom:2px solid #e8b53d; padding-bottom:3mm; margin-bottom:5mm; }
.doc .crumb { font-family:"Segoe UI",sans-serif; font-size:9pt; letter-spacing:.12em; text-transform:uppercase; color:#7587a0; }
.doc h1.dt { font-size:18pt; margin:1.5mm 0 2mm; }
.doc .badge { display:inline-block; font-family:"Segoe UI",sans-serif; font-size:8.5pt; letter-spacing:.08em; text-transform:uppercase; background:#e8edf5; color:#14315c; border:1px solid #cdd6e4; border-radius:20px; padding:.12em .8em; }
.doc .dlead { font-style:italic; color:#42505f; margin:.6em 0 0; }
.doc h1:not(.dt){ font-size:14pt; margin:1.1em 0 .35em; }
.doc h2 { font-size:13pt; margin:1.05em 0 .3em; color:#173a6b; }
.doc h3 { font-size:11.4pt; margin:.9em 0 .25em; color:#26456f; }
.doc h4 { font-size:10.6pt; margin:.8em 0 .2em; color:#3a536f; }
"""

# ---------- HTML ----------
PAGEMAP = {}
def toc_entry(cls, title, token, tipus=""):
    pg = PAGEMAP.get(token, "000")
    tip = f'<span class="tipus">{esc(tipus)}</span>' if tipus else ""
    return (f'<div class="toc-entry {cls}"><span class="t">{esc(title)}{tip}</span>'
            f'<span class="dots"></span><span class="pg">{pg}</span></div>')

def build_html_recull(s):
    """Portada + capçalera/índex + documents (mode module/combined)."""
    P = [f'<!doctype html><html lang="ca"><head><meta charset="utf-8"><style>{CSS}</style></head><body>']
    P.append(f'''<div class="cover"><div class="rule"></div>
      <div class="band">
        <div class="kicker">Fundació Jesuïtes Educació &middot; corpus FJE{(" &middot; Mòdul " + esc(s["mod"])) if s.get("mod") else ""}</div>
        <h1>{esc(s["title"])}</h1>
        <div class="sub">Compendi del coneixement pedagògic &middot; {len(s["docs"])} documents</div>
      </div>
      <div class="foot"><span>corpusFJE &middot; font de veritat pedagògica</span><span>Document generat automàticament</span></div>
    </div>''')
    P.append(f'<div class="module"><span class="mk">{s["token"]}</span>')
    P.append('<div class="mhead">')
    if s.get("mod"):
        P.append(f'<div class="mtag">Mòdul {esc(s["mod"])}</div>')
    P.append(f'<h1>{esc(s["title"])}</h1>')
    P.append(f'<div class="expl">{esc(s["expl"])}</div></div>')
    P.append(f'<h2 class="idx">Continguts &mdash; {len(s["docs"])} documents</h2>')
    for d in s["docs"]:
        P.append(toc_entry("", d["title"], d["token"], d["tipus"]))
    P.append('</div>')
    for d in s["docs"]:
        P.append(f'<div class="doc"><span class="mk">{d["token"]}</span><div class="dhead">')
        P.append(f'<div class="crumb">{esc(s.get("crumb") or s["title"])}</div>')
        P.append(f'<h1 class="dt">{esc(d["title"])}</h1>')
        if d["tipus"]: P.append(f'<span class="badge">{esc(d["tipus"])}</span>')
        if d["desc"]:  P.append(f'<div class="dlead">{esc(d["desc"])}</div>')
        P.append('</div>')
        P.append(d["html"])
        P.append('</div>')
    P.append('</body></html>')
    return "".join(P)

def build_html_doc(d, mod, mod_title):
    """Portada + contingut d'un sol document (mode per-document)."""
    P = [f'<!doctype html><html lang="ca"><head><meta charset="utf-8"><style>{CSS}</style></head><body>']
    P.append(f'''<div class="cover"><div class="rule"></div>
      <div class="band">
        <div class="kicker">Fundació Jesuïtes Educació &middot; corpus FJE &middot; Mòdul {esc(mod)}</div>
        <h1>{esc(d["title"])}</h1>
        <div class="sub">{esc(mod_title)}</div>
      </div>
      <div class="foot"><span>corpusFJE &middot; font de veritat pedagògica</span><span>Document generat automàticament</span></div>
    </div>''')
    P.append('<div class="doc"><span class="mk">MDOC0001</span><div class="dhead">')
    P.append(f'<div class="crumb">Mòdul {esc(mod)} &middot; {esc(mod_title)}</div>')
    P.append(f'<h1 class="dt">{esc(d["title"])}</h1>')
    if d["tipus"]: P.append(f'<span class="badge">{esc(d["tipus"])}</span>')
    if d["desc"]:  P.append(f'<div class="dlead">{esc(d["desc"])}</div>')
    P.append('</div>')
    P.append(d["html"])
    P.append('</div></body></html>')
    return "".join(P)

# ---------- RENDER ----------
def render(html_text, tag):
    html_path = TMP / f"_{tag}.html"
    html_path.write_text(html_text, encoding="utf-8")
    out_pdf = TMP / f"_{tag}.pdf"
    if out_pdf.exists():
        out_pdf.unlink()
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
           f"--user-data-dir={TMP/'_prof'}", "--no-first-run", "--disable-extensions",
           f"--print-to-pdf={out_pdf}", html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if not out_pdf.exists():
        print("ERROR render:", r.returncode, (r.stderr or "")[-800:]); sys.exit(1)
    return out_pdf

def map_pages(pdf_path, tokens):
    d = fitz.open(pdf_path); m = {}
    for i in range(d.page_count):
        txt = d[i].get_text()
        for tok in tokens:
            if tok not in m and tok in txt and d[i].search_for(tok):
                m[tok] = i
    d.close()
    return m

def footer_and_save(pdf_path, mod, out_final, toc, right_label):
    d = fitz.open(pdf_path)
    for i in range(1, d.page_count):
        pg = d[i]; w, h = pg.rect.width, pg.rect.height; y = h - 30
        pg.draw_line((52, y-8), (w-52, y-8), color=(.78,.83,.9), width=.6)
        left = f"corpus FJE · {mod}" if mod else "corpus FJE"
        pg.insert_text((52, y), left, fontname="helv", fontsize=8, color=(.46,.53,.63))
        num = str(i); tw = fitz.get_text_length(num, fontname="helv", fontsize=9)
        pg.insert_text(((w-tw)/2, y), num, fontname="helv", fontsize=9, color=(.26,.32,.4))
        rw = fitz.get_text_length(right_label, fontname="helv", fontsize=8)
        pg.insert_text((w-52-rw, y), right_label, fontname="helv", fontsize=8, color=(.46,.53,.63))
    d.set_toc(toc)
    out_final.parent.mkdir(parents=True, exist_ok=True)
    d.save(str(out_final), garbage=4, deflate=True)
    n = d.page_count; d.close()
    return n

# ---------- GENERADORS ----------
def gen_recull(title, expl, files, mod, slug, crumb=None):
    """Un volum: portada + índex + docs. mod pot ser '' (combinat multi-mòdul)."""
    global PAGEMAP
    files = [f for f in files if pathlib.Path(f).exists()]
    if not files:
        print(f"  [{title}] cap fitxer — saltat."); return None
    s = dict(mod=mod, title=title, expl=expl, token="MMODRECULL",
             docs=docs_from_files(files), crumb=crumb)
    tokens = [s["token"]] + [d["token"] for d in s["docs"]]
    PAGEMAP = {}
    p1 = render(build_html_recull(s), f"{slug}_p1")
    PAGEMAP = map_pages(p1, tokens)
    p2 = render(build_html_recull(s), f"{slug}_p2")
    def pg_of(tok, default=1):
        p = PAGEMAP.get(tok); return (p+1) if p is not None else default
    toc = [[1, s["title"], pg_of(s["token"])]]
    for d in s["docs"]:
        toc.append([2, d["title"], pg_of(d["token"])])
    out = OUT_DIR / f"corpusFJE_{(mod + '_') if mod else ''}{slug}.pdf"
    n = footer_and_save(p2, mod, out, toc, "Compendi")
    print(f"  FET -> {out.name}  ({n} pàgines, {len(s['docs'])} docs)")
    return out

def gen_document(fp):
    """Un PDF per a un sol document."""
    fp = pathlib.Path(fp)
    if not fp.exists():
        print(f"  [{fp.name}] no existeix — saltat."); return None
    mod = module_of(fp.name)
    mod_title = MODULE_META.get(mod, (mod, ""))[0]
    d = docs_from_files([fp])[0]
    pdf = render(build_html_doc(d, mod, mod_title), slugify(d["title"]))
    out = OUT_DIR / f"corpusFJE_{mod}_{slugify(d['title'])}.pdf"
    n = footer_and_save(pdf, mod, out, [[1, d["title"], 2]], "Document")
    print(f"  FET -> {out.name}  ({n} pàgines)")
    return out

# ---------- RESOLUCIÓ DE LA SELECCIÓ ----------
def module_files(mod):
    return sorted(glob.glob(str(CORPUS / f"{mod}_*.md")))

def resolve_and_generate(spec):
    mode     = spec.get("mode", "per-module")
    modules  = spec.get("modules", []) or []
    files    = [str((CORPUS / f).resolve()) for f in (spec.get("files", []) or [])]
    presets  = spec.get("presets", []) or []
    title    = spec.get("title")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    generated = []

    if mode == "combined":
        allfiles = []
        for mod in modules:
            allfiles += module_files(mod)
        allfiles += files
        for pk in presets:
            if pk in PRESETS:
                allfiles += PRESETS[pk][2]()
        seen, uniq = set(), []
        for f in allfiles:
            if f not in seen:
                seen.add(f); uniq.append(f)
        vol_title = title or "Compendi del corpus FJE"
        expl = ("Recull combinat generat des de Scriptorium a partir de la selecció de mòduls i "
                "documents del corpus FJE.")
        out = gen_recull(vol_title, expl, uniq, "", slugify(vol_title), crumb=vol_title)
        if out: generated.append(out)

    elif mode == "per-document":
        docs = []
        for mod in modules:
            docs += module_files(mod)
        docs += files
        for pk in presets:
            if pk in PRESETS:
                docs += PRESETS[pk][2]()
        seen = set()
        for f in docs:
            if f in seen: continue
            seen.add(f)
            out = gen_document(f)
            if out: generated.append(out)

    else:  # per-module
        # Mòduls sencers -> un PDF cadascun.
        for mod in modules:
            title_m, expl_m = MODULE_META.get(mod, (mod, ""))
            out = gen_recull(title_m, expl_m, module_files(mod), mod,
                             slugify(title_m), crumb=f"Mòdul {mod} · {title_m}")
            if out: generated.append(out)
        # Fitxers concrets solts -> agrupats pel seu mòdul en un PDF "selecció".
        by_mod = {}
        for f in files:
            by_mod.setdefault(module_of(os.path.basename(f)), []).append(f)
        for mod, fs in by_mod.items():
            title_m = MODULE_META.get(mod, (mod, ""))[0]
            out = gen_recull(f"{title_m} — selecció",
                             "Selecció de documents del mòdul feta des de Scriptorium.",
                             fs, mod, slugify(title_m) + "-seleccio",
                             crumb=f"Mòdul {mod} · {title_m}")
            if out: generated.append(out)
        # Presets -> volum propi.
        for pk in presets:
            if pk in PRESETS:
                t, e, fn = PRESETS[pk]
                out = gen_recull(t, e, fn(), "M3" if pk == "generes" else "",
                                 "compendi-" + slugify(t), crumb=t)
                if out: generated.append(out)

    return generated

# ---------- MAIN ----------
def load_spec():
    raw = os.environ.get("COMPENDI_SPEC")
    if not raw and len(sys.argv) > 1:
        raw = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    if not raw:
        print("ERROR: cal COMPENDI_SPEC (JSON) o un fitxer .json com a argument."); sys.exit(1)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: spec JSON invàlid: {e}"); sys.exit(1)

def main():
    print(f"Corpus:  {CORPUS}")
    print(f"Sortida: {OUT_DIR}")
    print(f"Chrome:  {CHROME}")
    spec = load_spec()
    print(f"Spec:    {json.dumps(spec, ensure_ascii=False)}")
    gen = resolve_and_generate(spec)
    print(f"\nGenerats {len(gen)} PDF(s):")
    for g in gen:
        print(f"  - compendi/{g.name}")
    if not gen:
        print("ERROR: cap PDF generat (selecció buida?)."); sys.exit(1)

if __name__ == "__main__":
    main()
