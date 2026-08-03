#!/usr/bin/env python3
"""Metodix Library — rakennevalidaattori (M3).

Tarkistaa, että kirjaston artikkelit ja registry.yml ovat keskenään ristiriidattomat.
Ei arvota sisältöä — se on laatuportin (M4) ja ihmisen tehtävä.

Käyttö:
    python3 scripts/validate.py                 # repon juuresta
    python3 scripts/validate.py --root .        # eksplisiittinen juuri
    python3 scripts/validate.py --strict        # varoituksetkin kaatavat

Paluuarvot:
    0  ei virheitä  (varoituksia voi olla, ellei --strict)
    1  vähintään yksi virhe
    2  ajo epäonnistui (puuttuva registry.yml, rikkinäinen YAML)

HUOM: tämä skripti KUTSUU sys.exit(1) virheistä. Se ei ole itsestäänselvyys —
DAE:n gate-validaattori näytti vuosia "ISSUE"-rivejä ja palautti silti 0, jolloin
mikään CI ei koskaan estänyt mitään. Sama virhe ei toistu tässä.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("VIRHE: pyyaml puuttuu (pip install pyyaml)", file=sys.stderr)
    raise SystemExit(2)

# ── Vakiot ────────────────────────────────────────────────────────────────────

REGISTERS = ("facilitator", "panelist", "public")
LANGS = ("en", "fi", "sv")

# Pronoian API validoi tunnisteen tällä. Tunniste, joka ei täytä tätä, ei ole
# haettavissa /api/help/{article_id}:llä — se palauttaa 400. Siksi sääntö on tässä.
ID_RE = re.compile(r"^[a-z0-9-]+$")
LEGACY_PREFIX_RE = re.compile(r"^(\d{2}|p\d)-")
VERSION_RE = re.compile(r"^\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_FIELDS = (
    "article_id", "concept", "register", "lang", "source_lang",
    "title", "version", "last_updated", "license", "status", "public",
)

# ── Tulokset ──────────────────────────────────────────────────────────────────


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def err(self, rule: str, msg: str) -> None:
        self.errors.append(f"[{rule}] {msg}")

    def warn(self, rule: str, msg: str) -> None:
        self.warnings.append(f"[{rule}] {msg}")


# ── Front matter ──────────────────────────────────────────────────────────────


def split_front_matter(text: str) -> tuple[dict | None, str]:
    """Palauta (front matter dictinä, runko). None jos front matteria ei ole."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    raw = text[3:end]
    body = text[end + 4:]
    try:
        fm = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        raise ValueError(f"front matterin YAML ei jäsenny: {e}") from e
    return (fm if isinstance(fm, dict) else None), body


# ── Tarkistukset ──────────────────────────────────────────────────────────────


def check_article(path: Path, root: Path, rep: Report) -> dict | None:
    """V1–V5, V9, V10, V12, V13. Palauttaa front matterin tai None."""
    rel = path.relative_to(root)
    text = path.read_text(encoding="utf-8")

    try:
        fm, body = split_front_matter(text)
    except ValueError as e:
        rep.err("V1", f"{rel}: {e}")
        return None
    if fm is None:
        rep.err("V1", f"{rel}: front matter puuttuu tai on tyhjä")
        return None

    missing = [f for f in REQUIRED_FIELDS if f not in fm]
    if missing:
        rep.err("V1", f"{rel}: pakollisia kenttiä puuttuu: {', '.join(missing)}")
        return fm

    aid = fm["article_id"]

    # V2 — tunnisteen muoto ja tiedostonimi
    if not ID_RE.match(str(aid)):
        rep.err("V2", f"{rel}: article_id '{aid}' ei täytä ^[a-z0-9-]+$ "
                      "(Pronoian API palauttaisi 400)")
    if path.stem != aid:
        rep.err("V2", f"{rel}: tiedostonimi ei vastaa article_id:tä '{aid}'")

    # V3/V4 — hakemisto kertoo rekisterin ja kielen
    parts = rel.parts
    if len(parts) >= 3 and parts[0] == "articles":
        dir_register, dir_lang = parts[1], parts[2]
        if fm["register"] != dir_register:
            rep.err("V3", f"{rel}: register='{fm['register']}' ≠ hakemisto '{dir_register}'")
        if fm["lang"] != dir_lang:
            rep.err("V4", f"{rel}: lang='{fm['lang']}' ≠ hakemisto '{dir_lang}'")
    if fm["register"] not in REGISTERS:
        rep.err("V3", f"{rel}: tuntematon register '{fm['register']}'")
    if fm["lang"] not in LANGS:
        rep.err("V4", f"{rel}: tuntematon lang '{fm['lang']}'")
    if fm["source_lang"] not in LANGS:
        rep.err("V4", f"{rel}: tuntematon source_lang '{fm['source_lang']}'")

    # V5 — translations vastaa levyä
    declared = set(fm.get("translations") or [])
    if fm["lang"] in declared:
        rep.err("V5", f"{rel}: translations sisältää oman kielen '{fm['lang']}'")
    actual = {
        d.name for d in path.parent.parent.iterdir()
        if d.is_dir() and d.name in LANGS and (d / path.name).exists()
    } - {fm["lang"]}
    if declared != actual:
        rep.err("V5", f"{rel}: translations={sorted(declared)} ≠ levyllä {sorted(actual)}")

    # V9/V10 — luonnos ei saa vuotaa
    if fm.get("kb_include") and fm["status"] != "published":
        rep.err("V9", f"{rel}: kb_include=true mutta status='{fm['status']}' "
                      "(luonnos päätyisi AI-helpdeskin groundingiin)")
    if fm.get("kb_include") and fm["register"] != "facilitator":
        rep.err("V9", f"{rel}: kb_include=true vain fasilitoijarekisterissä "
                      f"(nyt '{fm['register']}')")
    if fm["public"] and fm["status"] != "published":
        rep.err("V10", f"{rel}: public=true mutta status='{fm['status']}'")

    # V12 — muodot
    if not VERSION_RE.match(str(fm["version"])):
        rep.err("V12", f"{rel}: version '{fm['version']}' ei ole muotoa N.N")
    if not DATE_RE.match(str(fm["last_updated"])):
        rep.err("V12", f"{rel}: last_updated '{fm['last_updated']}' ei ole YYYY-MM-DD")

    # V13 — H1 säilytettävä (Pronoian _help_title lukee sen ennen T4:n parseria)
    if not any(ln.startswith("# ") for ln in body.splitlines()):
        rep.err("V13", f"{rel}: H1-otsikko puuttuu (Pronoian varafallback rikkoutuu)")

    # V14 — order pakollinen sovelluksen rekistereissä
    if fm["register"] in ("facilitator", "panelist") and "order" not in fm:
        rep.err("V14", f"{rel}: order puuttuu (lukujärjestys sovelluksen lukijassa)")

    # V15 — uusissa tunnisteissa ei numeroetuliitettä
    if LEGACY_PREFIX_RE.match(str(aid)) and aid not in LEGACY_IDS:
        rep.warn("V15", f"{rel}: uusi tunniste '{aid}' käyttää numeroetuliitettä; "
                        "järjestys kuuluu order-kenttään")

    return fm


def check_registry(reg: dict, rep: Report
                   ) -> tuple[dict[str, str], dict[str, dict], dict[str, dict]]:
    """V6–V8, V11, V16, V18. Palauttaa (id → käsite, käsite → tiedot, id → asetukset)."""
    membership: dict[str, str] = {}
    concepts: dict[str, dict] = {}

    for c in reg.get("concepts") or []:
        name = c.get("concept")
        if not name:
            rep.err("V7", "registry.yml: käsite ilman `concept`-kenttää")
            continue
        if name in concepts:
            rep.err("V7", f"registry.yml: käsite '{name}' esiintyy kahdesti")
        concepts[name] = c
        regs = c.get("registers") or {}
        if not isinstance(regs, dict):
            rep.err("V7", f"registry.yml: '{name}'.registers ei ole kartta "
                          "rekisteri → lista (ks. M1 löydös 1)")
            continue
        for r, ids in regs.items():
            if r not in REGISTERS:
                rep.err("V7", f"registry.yml: '{name}' viittaa tuntemattomaan rekisteriin '{r}'")
            for aid in ids or []:
                if aid == "TODO":
                    continue
                if aid in membership:
                    rep.err("V7", f"registry.yml: '{aid}' kuuluu kahteen käsitteeseen "
                                  f"('{membership[aid]}' ja '{name}') — jäsenyys on "
                                  "yksikäsitteinen, ristiviittaus kuuluu see_also-kenttään")
                membership[aid] = name

    # V16/V18 — articles-lohko vastaa registers-karttaa
    settings: dict[str, dict] = {}
    for name, c in concepts.items():
        arts = c.get("articles") or {}
        members = {a for r, ids in (c.get("registers") or {}).items()
                   for a in (ids or []) if a != "TODO"}
        for aid in sorted(members - set(arts)):
            rep.err("V16", f"registry.yml: '{aid}' on käsitteen '{name}' registers-kartassa "
                           "mutta puuttuu articles-lohkosta (public/kb_include määrittelemättä)")
        for aid in sorted(set(arts) - members):
            rep.err("V16", f"registry.yml: '{aid}' on käsitteen '{name}' articles-lohkossa "
                           "mutta ei registers-kartassa")
        for aid, cfg in arts.items():
            cfg = cfg or {}
            for f in ("public", "kb_include"):
                if f not in cfg:
                    rep.err("V16", f"registry.yml: '{aid}'.{f} puuttuu")
            if cfg.get("public") is False and not cfg.get("public_reason"):
                rep.warn("V18", f"registry.yml: '{aid}' on public: false ilman "
                                "public_reason-perustelua")
            settings[aid] = cfg

    for name, c in concepts.items():
        for aid in c.get("see_also") or []:
            if aid not in membership:
                rep.err("V8", f"registry.yml: '{name}'.see_also viittaa tuntemattomaan "
                              f"artikkeliin '{aid}'")
        for e in c.get("exits_library") or []:
            if e.get("id") in membership:
                rep.err("V8", f"registry.yml: '{e['id']}' on merkitty poistuvaksi mutta "
                              "esiintyy yhä registers-kartassa")

    return membership, concepts, settings


def cross_check(found: dict[tuple[str, str], dict], membership: dict[str, str],
                settings: dict[str, dict], rep: Report) -> None:
    """V6, V11, V17 — levy vs. registry."""
    ids_on_disk = {aid for (aid, _lang) in found}

    for aid in sorted(ids_on_disk - set(membership)):
        rep.err("V6", f"'{aid}' on levyllä mutta puuttuu registry.yml:stä")
    for aid in sorted(set(membership) - ids_on_disk):
        rep.warn("V6", f"'{aid}' on registry.yml:ssä mutta ei vielä levyllä")

    for (aid, lang), fm in found.items():
        expected = membership.get(aid)
        if expected and fm.get("concept") != expected:
            rep.err("V11", f"{aid}.{lang}: concept='{fm.get('concept')}' ≠ "
                           f"registry.yml '{expected}'")
        cfg = settings.get(aid)
        if cfg:
            for f in ("public", "kb_include"):
                if f in cfg and bool(fm.get(f)) != bool(cfg[f]):
                    rep.err("V17", f"{aid}.{lang}: {f}={fm.get(f)} ≠ registry.yml "
                                   f"{cfg[f]} — registry on jakelupäätösten lähde")


# ── Ajo ───────────────────────────────────────────────────────────────────────

LEGACY_IDS: set[str] = set()


def main() -> int:
    ap = argparse.ArgumentParser(description="Metodix Library -rakennevalidaattori")
    ap.add_argument("--root", default=".", help="repon juuri (oletus: .)")
    ap.add_argument("--strict", action="store_true", help="varoituksetkin kaatavat")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    reg_path = root / "registry.yml"
    if not reg_path.exists():
        print(f"VIRHE: {reg_path} puuttuu", file=sys.stderr)
        return 2
    try:
        reg = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"VIRHE: registry.yml ei jäsenny: {e}", file=sys.stderr)
        return 2

    global LEGACY_IDS
    LEGACY_IDS = set(reg.get("meta", {}).get("legacy_ids") or [])

    rep = Report()
    membership, _concepts, settings = check_registry(reg, rep)

    found: dict[tuple[str, str], dict] = {}
    articles_dir = root / "articles"
    if not articles_dir.exists():
        rep.warn("V0", "articles/ puuttuu — vain registry.yml tarkistettu")
    else:
        for path in sorted(articles_dir.rglob("*.md")):
            fm = check_article(path, root, rep)
            if fm and "article_id" in fm and "lang" in fm:
                key = (fm["article_id"], fm["lang"])
                if key in found:
                    rep.err("V6", f"'{key[0]}' esiintyy kahdesti kielellä '{key[1]}'")
                found[key] = fm

    cross_check(found, membership, settings, rep)

    # ── Tuloste ──
    for w in rep.warnings:
        print(f"VAROITUS {w}")
    for e in rep.errors:
        print(f"VIRHE    {e}")

    n_art = len({aid for (aid, _l) in found})
    print(f"\n{n_art} artikkelia · {len(found)} tiedostoa · "
          f"{len(membership)} registryssä · "
          f"{len(rep.errors)} virhettä · {len(rep.warnings)} varoitusta")

    if rep.errors or (args.strict and rep.warnings):
        print("VALIDATE: BLOCK")
        return 1
    print("VALIDATE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
