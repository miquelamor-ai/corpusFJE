#!/usr/bin/env python3
"""
Genera _manifest.json amb el frontmatter de tots els fitxers del corpus.
S'executa via GitHub Action a cada push a master.
"""
import json
import os
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path


ALIAS_MAP = {
    'títol': 'titol',
    'mòdul': 'modul',
    'etiquetes': 'paraules_clau',
    'estat': 'review_status',
}


def module_of(path: str) -> str | None:
    """Replica la lògica de CorpusSpec::moduleOf de scriptorium."""
    # curriculum/<etapa>/...
    m = re.match(r'^curriculum/([^/]+)/', path)
    if m:
        return 'curriculum-' + m.group(1)
    # Fitxers pedagògics: M<n>_xxx.md amb n d'1 o 2 dígits (M0..M11).
    # Important: \d{1,2} — si fos un sol dígit, M10_* i M11_* caurien a M1.
    m = re.match(r'^M(\d{1,2})_', os.path.basename(path))
    if m:
        return 'M' + m.group(1)
    return None


def parse_frontmatter(content: str) -> dict:
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?', content, re.DOTALL)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return {ALIAS_MAP.get(k, k): v for k, v in fm.items()}


modules: dict[str, list[dict]] = {}

# Fitxers pedagògics (.md)
for md_path in sorted(Path('.').glob('**/*.md')):
    rel = md_path.as_posix()
    if rel.startswith('.'):
        continue
    mod = module_of(rel)
    if not mod:
        continue

    content = md_path.read_text(encoding='utf-8')
    fm = parse_frontmatter(content)

    entry = {
        'path': rel,
        'size': len(content.encode('utf-8')),
        'titol': fm.get('titol'),
        'tipus': fm.get('tipus'),
        'subtipus': fm.get('subtipus'),
        'review_status': fm.get('review_status'),
        'descripcio': fm.get('descripcio'),
        'last_editor': fm.get('last_editor'),
    }
    # Camps específics de dinàmiques (tipus: dinamica) per a l'agrupació A-D-D i
    # l'ordenació pedagògica a Scriptorium. S'afegeixen NOMÉS si el fitxer els té,
    # per no embrutar els ~500 docs no-dinàmica amb camps buits.
    for k in ('phase', 'phases_aplicables', 'ordre', 'guskey', 'stars', 'duration'):
        if k in fm:
            entry[k] = fm[k]
    modules.setdefault(mod, []).append(entry)

# Fitxers curriculars (.json dins curriculum/)
for json_path in sorted(Path('curriculum').glob('**/*.json')):
    rel = json_path.as_posix()
    mod = module_of(rel)
    if not mod:
        continue

    content = json_path.read_text(encoding='utf-8')
    try:
        data = json.loads(content)
        meta = data.get('meta', {})
    except json.JSONDecodeError:
        meta = {}

    modules.setdefault(mod, []).append({
        'path': rel,
        'size': len(content.encode('utf-8')),
        'titol': meta.get('area_materia') or meta.get('nom'),
        'tipus': meta.get('etapa'),
        'descripcio': meta.get('descripcio'),
        'decret': meta.get('decret'),
        'codi_area': meta.get('codi_area'),
        'readonly': True,
    })

manifest = {
    'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'modules': modules,
}

Path('_manifest.json').write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2),
    encoding='utf-8',
)

total = sum(len(v) for v in modules.values())
print(f"Manifest generat: {total} fitxers en {len(modules)} mòduls")
