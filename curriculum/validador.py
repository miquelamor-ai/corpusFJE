"""
Validador multi-agent de fitxers JSON de currículum.

Agents:
  1. AgentSintaxi      — JSON ben format?
  2. AgentEsquema      — Camps obligatoris i tipus correctes?
  3. AgentCompletesa   — Cap camp buit o genèric?
  4. AgentCoherencia   — Consistència interna (codis únics, referències vàlides)?
  5. AgentInforme      — Consolida i presenta el resultat final.
"""

import json
import os
import sys
from pathlib import Path

# ─────────────────────────────────────────────
# AGENT 1 — SINTAXI
# ─────────────────────────────────────────────
class AgentSintaxi:
    """Verifica que el fitxer és JSON vàlid i llegible."""

    def __init__(self, path):
        self.path = Path(path)
        self.data = None
        self.errors = []
        self.warnings = []

    def executar(self):
        print(f"\n[Agent Sintaxi] Analitzant {self.path.name}...")
        if not self.path.exists():
            self.errors.append(f"Fitxer no trobat: {self.path}")
            return None

        try:
            with open(self.path, encoding="utf-8") as f:
                self.data = json.load(f)
            mida = self.path.stat().st_size / 1024
            print(f"  ✓ JSON vàlid ({mida:.1f} KB)")
        except json.JSONDecodeError as e:
            self.errors.append(f"Error de sintaxi JSON: {e}")
        except UnicodeDecodeError:
            self.errors.append("El fitxer no és UTF-8. Comprova l'encoding.")

        return self.data


# ─────────────────────────────────────────────
# AGENT 2 — ESQUEMA
# ─────────────────────────────────────────────
class AgentEsquema:
    """Verifica que els camps obligatoris existeixen i tenen el tipus correcte."""

    FAMÍLIES = {
        "lomloe": {
            "arrel": ["meta", "competencies_clau", "blocs_sabers", "competencies_especifiques", "sabers_basics"],
            "meta": ["familia", "etapa", "area_materia", "codi_area", "decret", "versio_schema"],
            "ce": ["codi", "text", "criteris_avaluacio"],
        },
        "fp": {
            "arrel": ["meta", "modul"],
            "meta": ["familia", "cicle_formatiu", "titol_cicle", "grau", "familia_professional", "versio_schema"],
            "modul": ["codi", "nom", "hores_totals", "uf"],
        },
        "infantil": {
            "arrel": ["meta", "ambits"],
            "meta": ["familia", "etapa", "cicle", "edat", "decret", "versio_schema"],
        },
    }

    def __init__(self, data):
        self.data = data
        self.errors = []
        self.warnings = []

    def executar(self):
        print("\n[Agent Esquema] Validant estructura...")
        if not self.data:
            self.errors.append("Sense dades per validar.")
            return

        familia = self.data.get("meta", {}).get("familia", "")
        if familia not in self.FAMÍLIES:
            self.errors.append(f"Família desconeguda: '{familia}'. Esperada: lomloe | fp | infantil")
            return

        regles = self.FAMÍLIES[familia]

        # Camps arrel
        for camp in regles["arrel"]:
            if camp not in self.data:
                self.errors.append(f"Camp obligatori absent a l'arrel: '{camp}'")

        # Camps de meta
        meta = self.data.get("meta", {})
        for camp in regles.get("meta", []):
            if camp not in meta:
                self.errors.append(f"Camp obligatori absent a 'meta': '{camp}'")

        # Validació específica LOMLOE
        if familia == "lomloe":
            self._validar_lomloe()

        # Validació específica FP
        elif familia == "fp":
            self._validar_fp()

        n_errors = len(self.errors)
        n_warn = len(self.warnings)
        if n_errors == 0:
            print(f"  ✓ Estructura correcta ({n_warn} avisos)")
        else:
            print(f"  ✗ {n_errors} errors d'esquema, {n_warn} avisos")

    def _validar_lomloe(self):
        ces = self.data.get("competencies_especifiques", [])
        if not isinstance(ces, list) or len(ces) == 0:
            self.errors.append("'competencies_especifiques' ha de ser una llista no buida.")
            return

        regles_ce = self.FAMÍLIES["lomloe"]["ce"]
        for i, ce in enumerate(ces):
            for camp in regles_ce:
                if camp not in ce:
                    self.errors.append(f"CE[{i}] '{ce.get('codi','?')}': falta camp '{camp}'")

        sabers = self.data.get("sabers_basics", {})
        if not isinstance(sabers, dict):
            self.errors.append("'sabers_basics' ha de ser un objecte.")
        elif len(sabers) == 0:
            self.warnings.append("'sabers_basics' és buit.")

    def _validar_fp(self):
        modul = self.data.get("modul", {})
        uf_list = modul.get("uf", [])
        if not isinstance(uf_list, list) or len(uf_list) == 0:
            self.errors.append("'modul.uf' ha de ser una llista no buida.")
            return

        for i, uf in enumerate(uf_list):
            for camp in ["codi", "nom", "hores", "resultats_aprenentatge"]:
                if camp not in uf:
                    self.errors.append(f"UF[{i}] '{uf.get('codi','?')}': falta camp '{camp}'")
            for j, ra in enumerate(uf.get("resultats_aprenentatge", [])):
                for camp in ["codi", "text", "criteris_avaluacio"]:
                    if camp not in ra:
                        self.errors.append(f"UF[{i}] RA[{j}] '{ra.get('codi','?')}': falta camp '{camp}'")


# ─────────────────────────────────────────────
# AGENT 3 — COMPLETESA
# ─────────────────────────────────────────────
class AgentCompletesa:
    """Detecta camps buits, textos massa curts o genèrics."""

    MIN_CHARS_TEXT = 20
    TEXTOS_GENERICS = ["...", "pendent", "TODO", "text aquí", "exemple"]

    def __init__(self, data):
        self.data = data
        self.errors = []
        self.warnings = []
        self._stats = {"camps_buits": 0, "textos_curts": 0, "textos_generics": 0}

    def executar(self):
        print("\n[Agent Completesa] Comprovant contingut...")
        if not self.data:
            return
        self._revisar_recursiu(self.data, path="")
        s = self._stats
        total = s["camps_buits"] + s["textos_curts"] + s["textos_generics"]
        if total == 0:
            print("  ✓ Tots els camps amb contingut adequat")
        else:
            print(f"  ⚠ {s['camps_buits']} camps buits, {s['textos_curts']} textos curts, {s['textos_generics']} textos genèrics")

    def _revisar_recursiu(self, node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                self._revisar_recursiu(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, item in enumerate(node):
                self._revisar_recursiu(item, f"{path}[{i}]")
        elif isinstance(node, str):
            self._revisar_text(node, path)

    def _revisar_text(self, text, path):
        # Ignora camps de metadades curts per disseny
        camps_curts_ok = {
            "codi", "familia", "etapa", "versio_schema", "decret", "font",
            "codi_area", "nota", "nota_estructura", "bloc_competencial",
            "data_decret", "grau", "cicle", "edat", "area_materia", "titol_cicle",
            "nom",  # noms de blocs, sentits, etc.
            # FP específics
            "cicle_formatiu", "familia_professional", "rd_titol", "resolucio_cat",
            "bloc",  # noms de blocs de contingut FP
        }
        # Camps que per disseny contenen codis curts (arrays de codis CC, blocs, etc.)
        paths_codis = {"competencies_clau", "blocs_sabers"}
        if any(p in path for p in paths_codis) and len(text) <= 20:
            return
        # Claus d'agrupament (CI, CM, CS, EIX1, AMB1...) apareixen com a valors de "eix" o "area"
        camp_fi = path.split(".")[-1].split("[")[0]
        if camp_fi in {"eix", "area"} and len(text) <= 6:
            return
        # Noms de sentits o blocs (Sentit numèric, Geometria i espai...) - camps "nom" dins sabers_basics
        if "sabers_basics" in path and camp_fi == "nom":
            return
        camp = path.split(".")[-1].replace("[", "").replace("]", "")

        if text.strip() == "":
            self._stats["camps_buits"] += 1
            self.errors.append(f"Camp buit: {path}")
            return

        if camp in camps_curts_ok:
            return

        if len(text.strip()) < self.MIN_CHARS_TEXT:
            self._stats["textos_curts"] += 1
            self.warnings.append(f"Text molt curt ({len(text)} car.): {path} → '{text[:40]}'")

        # Detecta textos genèrics NOMÉS si el text sencer és bàsicament el terme genèric
        for generic in self.TEXTOS_GENERICS:
            stripped = text.strip().lower()
            if stripped == generic.lower() or stripped.startswith(generic.lower() + " "):
                self._stats["textos_generics"] += 1
                self.warnings.append(f"Text genèric ('{generic}'): {path}")
                break


# ─────────────────────────────────────────────
# AGENT 4 — COHERÈNCIA
# ─────────────────────────────────────────────
class AgentCoherencia:
    """Verifica coherència interna: codis únics, agrupaments coherents, etc."""

    def __init__(self, data):
        self.data = data
        self.errors = []
        self.warnings = []

    def executar(self):
        print("\n[Agent Coherència] Verificant coherència interna...")
        if not self.data:
            return

        familia = self.data.get("meta", {}).get("familia", "")

        if familia == "lomloe":
            self._coherencia_lomloe()
        elif familia == "fp":
            self._coherencia_fp()

        n_errors = len(self.errors)
        n_warn = len(self.warnings)
        if n_errors == 0:
            print(f"  ✓ Coherència correcta ({n_warn} avisos)")
        else:
            print(f"  ✗ {n_errors} errors de coherència, {n_warn} avisos")

    def _coherencia_lomloe(self):
        ces = self.data.get("competencies_especifiques", [])

        # Codis CE únics
        codis = [ce.get("codi") for ce in ces]
        duplicats = [c for c in set(codis) if codis.count(c) > 1]
        if duplicats:
            self.errors.append(f"Codis CE duplicats: {duplicats}")
        else:
            print(f"    CE: {len(ces)} competències específiques, codis únics ✓")

        # Criteris d'avaluació: revisar que cada CE té almenys un agrupament vàlid per etapa.
        # Vocabulari CANÒNIC v1.2 (normalització 2026-06): claus de cicle/curs unificades
        # PRI_C1/C2/C3, ESO_C1/C2, BAT_1R/2N. (La variant antiga CI/CM/CS, 1r_3r/4t, 1r/2n
        # queda migrada; vegeu migració curriculum v1.2.)
        etapa = self.data.get("meta", {}).get("etapa", "")
        agrupaments_valids = {
            "eso":         {"ESO_C1", "ESO_C2"},
            "primaria":    {"PRI_C1", "PRI_C2", "PRI_C3"},
            "batxillerat": {"BAT_1R", "BAT_2N"},
        }
        valids = agrupaments_valids.get(etapa, set())

        for ce in ces:
            criteris = ce.get("criteris_avaluacio", {})
            if not isinstance(criteris, dict):
                self.errors.append(f"CE {ce.get('codi')}: 'criteris_avaluacio' ha de ser un objecte amb claus d'agrupament.")
                continue
            if valids and not any(k in criteris for k in valids):
                self.warnings.append(
                    f"CE {ce.get('codi')}: cap agrupament vàlid per a '{etapa}' "
                    f"(esperats: {sorted(valids)}, trobats: {sorted(criteris.keys())})."
                )

        # Sabers: revisar que els blocs declarats a blocs_sabers existeixen
        blocs_declarats = set(self.data.get("blocs_sabers", []))
        sabers = self.data.get("sabers_basics", {})
        for agrupament, contingut in sabers.items():
            if isinstance(contingut, dict):
                blocs_sabers = set(contingut.keys()) - {"nota"}
                blocs_no_declarats = blocs_sabers - blocs_declarats
                if blocs_no_declarats:
                    self.warnings.append(f"Sabers '{agrupament}': blocs no declarats a 'blocs_sabers': {blocs_no_declarats}")

        # Estadístiques de sabers
        for agrupament, contingut in sabers.items():
            if isinstance(contingut, dict):
                n_sabers = sum(
                    len(items) if isinstance(items, list) else
                    sum(len(v) for v in items.get("subapartats", {}).values() if isinstance(v, list))
                    for k, items in contingut.items() if k != "nota" and isinstance(items, dict)
                    for v in (items.get("subapartats", {}).values() if isinstance(items, dict) else [])
                )
                print(f"    Sabers '{agrupament}': {len(contingut)} blocs")

    def _coherencia_fp(self):
        modul = self.data.get("modul", {})
        hores_totals = modul.get("hores_totals", 0)
        uf_list = modul.get("uf", [])

        # Suma d'hores de UFs vs total del mòdul
        suma_hores_uf = sum(uf.get("hores", 0) for uf in uf_list)
        if hores_totals > 0 and suma_hores_uf != hores_totals:
            self.warnings.append(
                f"Hores del mòdul ({hores_totals}h) ≠ suma d'hores de les UFs ({suma_hores_uf}h)"
            )

        # Codis RA únics dins cada UF
        for uf in uf_list:
            ras = uf.get("resultats_aprenentatge", [])
            codis_ra = [ra.get("codi") for ra in ras]
            duplicats = [c for c in set(codis_ra) if codis_ra.count(c) > 1]
            if duplicats:
                self.errors.append(f"UF {uf.get('codi')}: RA duplicats: {duplicats}")

        print(f"    Mòdul: {len(uf_list)} UFs, {hores_totals}h total")


# ─────────────────────────────────────────────
# AGENT 5 — FONT I DECRET VIGENT
# ─────────────────────────────────────────────
class AgentFont:
    """Verifica que la font del document és vàlida, accessible i correspon al decret vigent."""

    # Decret vigent a Catalunya per etapa (familia, etapa) → decret esperat
    DECRETS_VIGENTS = {
        ("lomloe",   "infantil"):    "21/2023",
        ("infantil", "infantil"):    "21/2023",   # schema_infantil usa familia="infantil"
        ("lomloe",   "primaria"):    "175/2022",
        ("lomloe",   "eso"):         "175/2022",
        ("lomloe",   "batxillerat"): "171/2022",
    }

    DOMINIS_OFICIALS = {
        "educacio.gencat.cat",
        "xtec.gencat.cat",
        "boe.es",
        "dogc.gencat.cat",
        "gencat.cat",
    }

    def __init__(self, data):
        self.data = data
        self.errors = []
        self.warnings = []

    def executar(self):
        print("\n[Agent Font] Verificant font i decret vigent...")
        if not self.data:
            return

        meta    = self.data.get("meta", {})
        familia = meta.get("familia", "")
        etapa   = meta.get("etapa", "")
        decret  = meta.get("decret", "")
        font    = meta.get("font", "")

        # ── 1. Decret vigent ──────────────────────────────────────
        decret_esperat = self.DECRETS_VIGENTS.get((familia, etapa))
        if decret_esperat:
            if decret == decret_esperat:
                print(f"  ✓ Decret vigent: {decret}")
                # Avís especial: modificació pendent del Decret 171/2022 (BAT, curs 2026-2027)
                if decret == "171/2022":
                    self.warnings.append(
                        "Decret 171/2022 (Batxillerat): hi ha un projecte de modificació "
                        "publicat pel Departament (febrer 2026) que entra en vigor al curs 2026-2027. "
                        "Verificar continguts quan es publiqui al DOGC."
                    )
            else:
                self.errors.append(
                    f"Decret OBSOLET o incorrecte: el JSON usa '{decret}', "
                    f"però el vigent per a {etapa} ({familia}) és '{decret_esperat}'."
                )
        else:
            print(f"  ℹ Decret '{decret}' (etapa '{etapa}' sense regla de vigència definida)")

        # ── 2. Font present ───────────────────────────────────────
        if not font:
            self.warnings.append("Falta 'font' a meta. Cal indicar l'URL del document oficial.")
            return

        if not font.startswith("http"):
            self.warnings.append(
                "La 'font' és una descripció textual, no una URL verificable. "
                "Substitueix-la per la URL oficial del PDF del Departament."
            )
            return

        # ── 3. Domini oficial ─────────────────────────────────────
        from urllib.parse import urlparse
        domini = urlparse(font).netloc.lower()
        if any(of in domini for of in self.DOMINIS_OFICIALS):
            print(f"  ✓ Domini oficial: {domini}")
        else:
            self.warnings.append(f"Font no és un domini oficial reconegut: {domini}")

        # ── 4. Accessibilitat i verificació PDF ───────────────────
        try:
            import urllib.request
            import ssl
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode    = ssl.CERT_NONE
            req = urllib.request.Request(
                font,
                headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-3"},
            )
            with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
                primers_bytes = resp.read(4)
            if primers_bytes == b"%PDF":
                print(f"  ✓ PDF accessible i verificat: ...{font[-50:]}")
            elif primers_bytes:
                self.warnings.append(
                    f"La font és accessible però no sembla un PDF "
                    f"(capçalera: {primers_bytes!r}). Comprova la URL."
                )
            else:
                print(f"  ✓ Font accessible (resposta buida, possible PDF): {font[-50:]}")
        except Exception as exc:
            self.warnings.append(
                f"Font no accessible o timeout: ...{font[-50:]} "
                f"({type(exc).__name__}: {exc})"
            )


# ─────────────────────────────────────────────
# AGENT 6 — INFORME
# ─────────────────────────────────────────────
class AgentInforme:
    """Consolida els resultats de tots els agents i genera l'informe final."""

    def __init__(self, agents):
        self.agents = agents

    def executar(self, path):
        print("\n" + "═" * 60)
        print(f" INFORME DE VALIDACIÓ: {Path(path).name}")
        print("═" * 60)

        total_errors = []
        total_warnings = []

        for agent in self.agents:
            nom = agent.__class__.__name__
            errors = getattr(agent, "errors", [])
            warnings = getattr(agent, "warnings", [])
            total_errors.extend([(nom, e) for e in errors])
            total_warnings.extend([(nom, w) for w in warnings])

        if total_errors:
            print(f"\n❌ ERRORS ({len(total_errors)}):")
            for nom, msg in total_errors:
                print(f"   [{nom}] {msg}")

        if total_warnings:
            print(f"\n⚠  AVISOS ({len(total_warnings)}):")
            for nom, msg in total_warnings:
                print(f"   [{nom}] {msg}")

        if not total_errors and not total_warnings:
            print("\n✅ El fitxer supera totes les validacions sense errors ni avisos.")
        elif not total_errors:
            print(f"\n✅ Cap error crític. {len(total_warnings)} avisos menors.")
        else:
            print(f"\n🚫 {len(total_errors)} errors que cal corregir.")

        print("═" * 60)
        return len(total_errors) == 0


# ─────────────────────────────────────────────
# ORQUESTRADOR
# ─────────────────────────────────────────────
def validar(path_json):
    print(f"\n{'─'*60}")
    print(f" Iniciant validació multi-agent: {path_json}")
    print(f"{'─'*60}")

    # Agent 1: Sintaxi (llegeix el fitxer)
    a_sintaxi = AgentSintaxi(path_json)
    data = a_sintaxi.executar()

    # Agent 2: Esquema
    a_esquema = AgentEsquema(data)
    a_esquema.executar()

    # Agent 3: Completesa
    a_completesa = AgentCompletesa(data)
    a_completesa.executar()

    # Agent 4: Coherència
    a_coherencia = AgentCoherencia(data)
    a_coherencia.executar()

    # Agent 5: Font i decret vigent
    a_font = AgentFont(data)
    a_font.executar()

    # Agent 6: Informe final
    informe = AgentInforme([a_sintaxi, a_esquema, a_completesa, a_coherencia, a_font])
    ok = informe.executar(path_json)

    return ok


# ─────────────────────────────────────────────
# ENTRADA
# ─────────────────────────────────────────────
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Si no es passa argument, valida tots els JSONs de curriculum/
        base = Path(__file__).parent
        fitxers = list(base.rglob("*.json"))
        fitxers = [f for f in fitxers if "schemas" not in str(f)]

        if not fitxers:
            print("No s'han trobat fitxers JSON a validar.")
            sys.exit(1)

        print(f"Validant {len(fitxers)} fitxers JSON...")
        resultats = []
        for f in fitxers:
            ok = validar(str(f))
            resultats.append((f.name, ok))

        print("\n\n══ RESUM GLOBAL ══")
        for nom, ok in resultats:
            estat = "✅" if ok else "❌"
            print(f"  {estat} {nom}")
    else:
        ok = validar(sys.argv[1])
        sys.exit(0 if ok else 1)
