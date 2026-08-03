# Metodix Library

An open, versioned library of Delphi and futures research method articles, written in
three **registers** — for facilitators, for panelists, and for the public — in English,
Finnish and Swedish.

Maintained by **Metodix Oy**. Part of the Metodix Delphi ecosystem: planning (DPE) →
data collection (Pronoia) → analysis (DAE). Content is licensed CC BY 4.0.

*Avoin, versioitu Delfoi- ja tulevaisuudentutkimuksen metodikirjasto. · Ett öppet,
versionerat metodbibliotek för Delfoi- och framtidsforskning.*

---

## Why registers

The same concept needs different articles for different readers. A facilitator running
a study, a panelist answering without a login, and a researcher reading about the
method with no product involved are asking three different questions. They get three
different articles, not three translations of one.

| Register | Reader | Where it appears |
|---|---|---|
| `facilitator` | researcher running a study | Pronoia's in-app reader |
| `panelist` | invited expert, not logged in | the "?" on the response page |
| `public` | researchers, students, clients | this site |
| *(report)* | commissioner, reviewer | method appendix, derived from `public` |

The relationship is **not one-to-one**: one facilitator article can correspond to
several panelist articles. `registry.yml` records which articles belong to the same
concept, and it is the source of truth for every distribution decision.

## Layout

```
registry.yml                              concept map — which articles are the same thing
articles/<register>/<lang>/<id>.md        every article; id == filename
scripts/validate.py                       structural validator (18 rules)
scripts/test_validate.py                  the validator's own tests
templates/article-template.md             front matter schema for a new article
assets/                                   shared maps and icons
_config.yml                               site build; publishes the public register only
index.md                                  public front page
```

Registers are separate directories so that a runtime filter is never the only thing
keeping facilitator content off a public page.

## Before you commit

```bash
pip install 'pyyaml<7'
python3 scripts/validate.py --root .     # VALIDATE: PASS required
python3 scripts/test_validate.py         # if you changed validate.py
```

`validate.py` exits 1 on any error, and CI runs it on every push and pull request. It
checks structure, not content; the content gate is the checklist in
[CONTRIBUTING.md](CONTRIBUTING.md), and a human walks it.

Warnings about articles listed in `registry.yml` but not yet on disk are expected —
the registry was written from the full inventory of 24 articles, and they arrive one
migration at a time.

## Reading the library from other systems

Pronoia, the reports and the plugins **read; they never write**. All content changes
are made here, through a pull request.

Read against a **release tag, never `main`**:

```
https://raw.githubusercontent.com/oraakkeli/metodix-library/<tag>/articles/<register>/<lang>/<article_id>.md
```

`main` carries work in progress. A tag is a deliberate decision, which is exactly what
a consumer of a method definition needs. `article_id` is permanent — code, deep links
(`?help=<id>`) and AI citations all point at it, and it never changes. Content changes
bump `version`.

## Releases and DOIs

Each release is tagged and archived in Zenodo with its own DOI. A study freezes the tag
it ran under, so its report can cite the method definition that was in force at the
time rather than the current one. Cite a single article by naming it inside the release:

> Konsensus ja dissensus [`03-konsensus-dissensus` v1.2], Metodix Library v0.1.0, DOI …

See [CITATION.cff](CITATION.cff).

## Language

English is the starting point and the fallback — the language that always works. New
articles are written in English first (`source_lang: en`); Finnish and Swedish are
translations. The 24 articles migrated from Pronoia in 2026 are grandfathered with
`source_lang: fi`. The `source_lang` field always tells you which case you are in.

## License

CC BY 4.0 — see [LICENSE.md](LICENSE.md). Attribution: author + "Metodix Library /
Metodix Oy" + the article URL. Per-article exceptions go in the article's `license`
field; the library-wide license is not reopened.

---

Metodix Oy · [www.metodix.eu](https://www.metodix.eu) · info@metodix.fi
