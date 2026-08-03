#!/usr/bin/env python3
"""Generate INDEX.md — the whole library on one page, by concept and by register.

registry.yml is the source of truth, but it is a 350-line YAML file: correct,
machine-checked, and unreadable at a glance. This renders the same information as
tables a human can scan, and marks the gaps that still need writing.

    python3 scripts/build_index.py            # write INDEX.md
    python3 scripts/build_index.py --check    # exit 1 if INDEX.md is stale

INDEX.md is GENERATED. It is excluded from the site build (_config.yml): it lists
facilitator and panelist articles, and the public site publishes neither.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("en", "fi", "sv")
REGISTERS = ("facilitator", "panelist", "public")
LABEL = {"facilitator": "Fasilitoija", "panelist": "Panelisti", "public": "Julkinen"}
OUT = ROOT / "INDEX.md"


def front_matter(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    if not t.startswith("---"):
        return {}
    end = t.find("\n---", 3)
    return yaml.safe_load(t[3:end]) if end != -1 else {}


def load_disk() -> dict:
    """{(register, id): {lang: front matter}} for everything actually on disk."""
    out: dict = {}
    for p in sorted((ROOT / "articles").rglob("*.md")):
        register, lang = p.parts[-3], p.parts[-2]
        if lang in LANGS:
            out.setdefault((register, p.stem), {})[lang] = front_matter(p)
    return out


def title_of(langs: dict) -> str:
    for l in ("en", "fi", "sv"):
        if l in langs and langs[l].get("title"):
            return str(langs[l]["title"])
    return "—"


def render(reg: dict, disk: dict) -> str:
    concepts = reg.get("concepts") or []

    # id -> (concept, register)
    placed: dict[str, tuple[str, str]] = {}
    for c in concepts:
        for register, ids in (c.get("registers") or {}).items():
            for aid in ids or []:
                if aid != "TODO":
                    placed[aid] = (c["concept"], register)

    counts = {r: [0, 0, 0] for r in REGISTERS}   # artikkelia, julkisia, kb_include
    for aid, (_c, register) in placed.items():
        cfg = next((c["articles"][aid] for c in concepts
                    if aid in (c.get("articles") or {})), {}) or {}
        counts[register][0] += 1
        counts[register][1] += bool(cfg.get("public"))
        counts[register][2] += bool(cfg.get("kb_include"))

    n_files = sum(len(v) for v in disk.values())
    L = []
    L.append("# Metodix Library — sisällysluettelo\n")
    L.append("> **GENEROITU** tiedostoista `registry.yml` ja `articles/`. Älä muokkaa käsin —")
    L.append("> aja `python3 scripts/build_index.py`. CI tarkistaa että tämä vastaa levyä.\n")
    L.append(f"**{len(placed)} artikkelia · {n_files} tiedostoa · "
             f"{len(concepts)} käsitettä · fi / en / sv**\n")

    L.append("| Rekisteri | Artikkeleita | Julkisella sivulla | AI-helpdeskin lähteenä |")
    L.append("|---|---|---|---|")
    for r in REGISTERS:
        a, p, k = counts[r]
        L.append(f"| {LABEL[r]} | {a} | {p} | {k} |")
    L.append("")

    # ── Käsitematriisi — se yhden silmäyksen näkymä ──
    L.append("## Käsitteet × rekisterit\n")
    L.append("Yksi rivi per käsite. **TODO** = artikkeli puuttuu vielä. "
             "Viiva = tietoinen valinta, ei aukko.\n")
    L.append("| Käsite | Fasilitoija | Panelisti | Julkinen |")
    L.append("|---|---|---|---|")
    todo = []
    for c in concepts:
        cells = []
        for r in REGISTERS:
            ids = (c.get("registers") or {}).get(r) or []
            if not ids:
                cells.append("–")
            elif ids == ["TODO"]:
                cells.append("**TODO**")
                todo.append((c["concept"], r))
            else:
                cells.append(" · ".join(f"`{i}`" if i != "TODO" else "**TODO**" for i in ids))
        L.append(f"| {c['concept']} | {cells[0]} | {cells[1]} | {cells[2]} |")
    L.append("")
    if todo:
        L.append(f"**Kirjoittamatta: {len(todo)}** — "
                 + ", ".join(f"{c} ({LABEL[r].lower()})" for c, r in todo) + "\n")

    # ── Rekisterikohtaiset taulukot ──
    for r in REGISTERS:
        def sort_key(aid: str, _r=r):
            fm = next(iter(disk.get((_r, aid), {}).values()), {})
            return (fm.get("order") or 999, aid)

        rows = sorted(((aid, cid) for aid, (cid, reg) in placed.items() if reg == r),
                      key=lambda t: sort_key(t[0]))
        if not rows:
            continue
        L.append(f"## {LABEL[r]}rekisteri\n")
        head = "| # | Tunniste | Otsikko | Kielet | Versio | Päivitetty |"
        if r == "facilitator":
            head = "| # | Tunniste | Otsikko | Kielet | AI | Versio | Päivitetty |"
        elif r == "panelist":
            head = "| # | Tunniste | Otsikko | Kielet | Julkinen | Versio | Päivitetty |"
        L.append(head)
        L.append("|" + "---|" * (head.count("|") - 1))
        for aid, cid in rows:
            langs = disk.get((r, aid), {})
            any_fm = next(iter(langs.values()), {})
            order = any_fm.get("order", "")
            have = " ".join(l for l in LANGS if l in langs) or "—"
            link = f"[`{aid}`](articles/{r}/{'en' if 'en' in langs else 'fi'}/{aid}.md)"
            base = [str(order), link, title_of(langs), have]
            tail = [str(any_fm.get("version", "")), str(any_fm.get("last_updated", ""))]
            if r == "facilitator":
                mid = ["✓" if any_fm.get("kb_include") else ""]
            elif r == "panelist":
                mid = ["✓" if any_fm.get("public") else ""]
            else:
                mid = []
            L.append("| " + " | ".join(base + mid + tail) + " |")
        L.append("")

    L.append("---\n")
    L.append("*Metodix Oy · info@metodix.fi · www.metodix.eu*")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit 1 if INDEX.md is out of date")
    args = ap.parse_args()

    reg = yaml.safe_load((ROOT / "registry.yml").read_text(encoding="utf-8"))
    text = render(reg, load_disk())

    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("INDEX.md is out of date — run: python3 scripts/build_index.py")
            return 1
        print("INDEX: PASS")
        return 0

    OUT.write_text(text, encoding="utf-8")
    print(f"INDEX.md written ({len(text.splitlines())} riviä)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
