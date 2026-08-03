#!/usr/bin/env python3
"""Metodix Library — validate.py:n negatiiviset testit.

Rakentaa registry.yml:stä synteettisen artikkelipuun, rikkoo sitä yksi sääntö
kerrallaan ja tarkistaa, että (a) oikea sääntö laukeaa ja (b) paluuarvo on 1.

Positiivinen testi (ehjä puu → PASS, exit 0) ajetaan ensin.

    python3 scripts/test_validate.py
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

LANGS = ("en", "fi", "sv")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def build_fixture(dest: Path, registry: Path) -> int:
    shutil.copy(registry, dest / "registry.yml")
    shutil.copy(HERE / "validate.py", dest / "validate.py")
    reg = yaml.safe_load(registry.read_text(encoding="utf-8"))
    n = 0
    for c in reg["concepts"]:
        cfgs = c.get("articles") or {}
        for register, arts in (c["registers"] or {}).items():
            for i, aid in enumerate(arts or []):
                if aid == "TODO":
                    continue
                cfg = cfgs.get(aid) or {}
                for lang in LANGS:
                    d = dest / "articles" / register / lang
                    d.mkdir(parents=True, exist_ok=True)
                    fm = {
                        "article_id": aid, "concept": c["concept"], "register": register,
                        "lang": lang, "source_lang": "fi", "title": f"{aid} ({lang})",
                        "order": i + 1, "version": "1.0", "last_updated": "2026-08-02",
                        "license": "CC-BY-4.0", "status": "published",
                        "public": bool(cfg.get("public")),
                        "translations": [l for l in LANGS if l != lang],
                        "kb_include": bool(cfg.get("kb_include")),
                    }
                    if register == "public":
                        fm.pop("order")
                    (d / f"{aid}.md").write_text(
                        "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
                        + "---\n\n" + f"# {fm['title']}\n\nRunko.\n", encoding="utf-8")
                    n += 1
    return n


def main() -> int:
    registry = ROOT / "registry.yml"
    if not registry.exists():
        print(f"VIRHE: {registry} puuttuu", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory() as tmp:
        work, backup = Path(tmp) / "work", Path(tmp) / "backup"
        work.mkdir()
        n = build_fixture(work, registry)
        shutil.copytree(work, backup)

        def run() -> tuple[int, str]:
            r = subprocess.run([sys.executable, "validate.py", "--root", "."],
                               cwd=work, capture_output=True, text=True)
            return r.returncode, r.stdout

        def restore() -> None:
            shutil.rmtree(work)
            shutil.copytree(backup, work)

        code, out = run()
        print(f"positiivinen testi ({n} tiedostoa): exit={code} "
              f"{'✓' if code == 0 else '✗ ' + out}")
        results = [("ehjä puu läpi", "—", code == 0)]

        art = work / "articles/facilitator/fi/03-konsensus-dissensus.md"
        reg_f = work / "registry.yml"

        def sub(path: Path, old: str, new: str):
            return lambda: path.write_text(path.read_text(encoding="utf-8").replace(old, new),
                                           encoding="utf-8")

        cases = [
            ("front matter puuttuu", "V1",
             lambda: art.write_text("# Ei front matteria\n", encoding="utf-8")),
            ("article_id ≠ tiedostonimi", "V2",
             sub(art, "article_id: 03-konsensus-dissensus", "article_id: vaara-tunniste")),
            ("register ≠ hakemisto", "V3",
             sub(art, "register: facilitator", "register: panelist")),
            ("translations ≠ levy", "V5",
             lambda: (work / "articles/facilitator/sv/03-konsensus-dissensus.md").unlink()),
            ("kb_include luonnoksessa", "V9", sub(art, "status: published", "status: draft")),
            ("version väärää muotoa", "V12", sub(art, "version: '1.0'", "version: v1")),
            ("H1 puuttuu", "V13",
             lambda: art.write_text(re.sub(r"\n# .*\n", "\n", art.read_text(encoding="utf-8")),
                                    encoding="utf-8")),
            ("order puuttuu", "V14",
             lambda: art.write_text(re.sub(r"\norder: \d+", "", art.read_text(encoding="utf-8")),
                                    encoding="utf-8")),
            ("artikkeli kahdessa käsitteessä", "V7",
             sub(reg_f, "      panelist: [p2-kierrokset]",
                 "      panelist: [p2-kierrokset, p3-erimielisyys]")),
            ("see_also osoittaa tyhjään", "V8",
             sub(reg_f, "see_also: [p1-vastaaminen]", "see_also: [ei-olemassa]")),
            ("concept ≠ registry", "V11",
             sub(art, "concept: konsensus-dissensus", "concept: pire")),
            ("articles-lohko ≠ registers", "V16",
             sub(reg_f, "      03-konsensus-dissensus:\n", "      ei-olemassa-oleva:\n")),
            ("public ≠ registry", "V17", sub(art, "public: false", "public: true")),
        ]

        # V19 vaatii kirjainkokoa EROTTAVAN levyn: macOS:llä törmäystä ei voi
        # fyysisesti luoda, joten testi ohitetaan siellä ja ajetaan CI:ssä (Linux).
        # Se on sama epäsymmetria jonka takia koko sääntö on olemassa.
        probe = work / "CaseProbe.tmp"
        probe.write_text("x", encoding="utf-8")
        case_sensitive = not (work / "caseprobe.tmp").exists()
        probe.unlink()
        if case_sensitive:
            cases.append(("kirjainkokotörmäys", "V19",
                          lambda: (work / "Registry.yml").write_text("x", encoding="utf-8")))
        else:
            print(f"{'kirjainkokotörmäys':34} V19   OHITETTU (levy ei erota kirjainkokoa)")

        for name, rule, mutate in cases:
            restore()
            mutate()
            code, out = run()
            ok = code == 1 and f"[{rule}]" in out
            results.append((name, rule, ok))
            print(f"{name:34} {rule:5} exit={code} {'✓' if ok else '✗'}")

    failed = [r for r in results if not r[2]]
    print(f"\n{len(results) - len(failed)}/{len(results)} läpi")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
