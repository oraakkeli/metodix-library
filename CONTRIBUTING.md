# Contributing to Metodix Library

This library serves four audiences from one source. Before you write or change
anything, know which **register** you are writing in — it decides almost everything
else.

> **Language.** This document, and every new article, is written in English first
> (`source_lang: en`); Finnish and Swedish are translations. The 24 articles migrated
> from Pronoia in 2026 are grandfathered with `source_lang: fi` — when one of those
> changes, the change is made in Finnish and English follows. The `source_lang` field
> always tells you which case you are in.

---

## 1. The four registers

| Register | Audience | Where it appears | Answers |
|---|---|---|---|
| `facilitator` | researcher running a study | Pronoia's in-app reader, surfaced by study state | *what does this mean, and what is my next step* |
| `panelist` | invited expert, **not logged in** | floating "?" on the response page | *what is being asked of me, and what happens to my data* |
| `public` | researchers, students, clients | the public library site | *what is this method, independent of any product* |
| — *(report)* | study commissioner, reviewer | method appendix in Pronoia/DAE reports | derived from `public`; not authored directly |

One concept may exist in several registers. **They are not translations of each
other** — they answer different questions and are written separately. `registry.yml`
records which articles belong to the same concept.

The relationship is **not one-to-one**: `09-kysymystyypit` (one facilitator selection
guide) corresponds to three panelist articles, one per question type a respondent
actually meets. That is correct, and merging them would make both worse.

---

## 2. Before you open a pull request

Run the structural validator. It checks form, not content:

```bash
python3 scripts/validate.py --root .
python3 scripts/test_validate.py     # if you changed validate.py itself
```

`VALIDATE: PASS` (exit 0) is required to merge. The validator will not tell you
whether an article is any good — that is what the rest of this document is for.

**The machine checks structure; the human checks content.** Do not add content
judgements to the validator. A quality gate you can pass by filling in the right
fields is not a quality gate.

---

## 3. The gate

### 3.1 Every article, every register

- [ ] `validate.py` passes
- [ ] Claims are supported; sources named where a claim is not self-evident
- [ ] All three languages exist, **or** `translations` honestly says otherwise
- [ ] `version` incremented and `last_updated` set, if content changed
- [ ] `article_id` unchanged (it never changes — see §5)
- [ ] Facts that have a canonical home elsewhere are **referenced, not repeated** —
      vendor names, retention periods, prices, legal statements. A repeated fact is a
      future contradiction (see §4)
- [ ] The article promises only what is true and durable: no guarantee the product
      cannot keep, no number that will quietly go stale under a version tag
- [ ] **Register cross-check** (see §4) — the most important line in this document

### 3.2 `facilitator` — additionally

- [ ] Matches the product as it is **now**: terms, phases, button labels
- [ ] States which study state it belongs to, so `stateHelpId` can surface it
- [ ] Says what the reader should *do*, not only what is true
- [ ] `kb_include` is correct — this article will be fed to the AI helpdesk verbatim

> `kb_include: true` means the article enters the assistant's grounding corpus.
> An unfinished or wrong article there affects every answer the assistant gives,
> silently. `status: draft` and `kb_include: true` together are a validator error
> for this reason.

### 3.3 `panelist` — additionally

- [ ] Readable in **60 seconds** — roughly one screen, ≤ 25 lines
- [ ] No unexplained jargon and no product-internal names (PIRE, DAE, orientation).
      Method terms may appear, but explained: "disagreement (dissensus)" not "dissensus"
- [ ] Answers the panelist's question, not the researcher's
- [ ] Reads safely to a stranger: this register is served **without login**, and
      several of its articles are public
- [ ] Nothing here reveals facilitator-side content — the register lives in its own
      directory precisely so that a runtime filter is not the only line of defence

### 3.4 `public` — additionally

- [ ] Understandable **without Pronoia**. This is the same question that decides
      `public: true/false`, so if you cannot answer yes, the article is not public yet
- [ ] Citable: author, year, sources
- [ ] No product-internal names, no UI instructions, no pricing
- [ ] Reads as a method article, not as documentation of a tool

> Facilitator articles are **not republished** as public articles. As of 2026-08-02
> every one of the 13 facilitator articles contains product-bound references, so the
> public register is authored separately, using the facilitator text as source
> material. Do not shortcut this by flipping `public` to `true`.

---

## 4. The register cross-check

**When you change an article, look at its siblings.**

`registry.yml` lists them under `registers:` for the concept. For example, changing
`03-konsensus-dissensus` (facilitator) means checking `p3-erimielisyys` (panelist),
because the panelist article makes a *promise* — "disagreement is valuable, you may
hold your position" — that the facilitator article's method must keep.

Three outcomes are acceptable:

1. Sibling updated in the same PR.
2. Sibling deliberately unchanged — **say so in the PR description**.
3. Sibling needs work beyond this PR — open an issue and link it.

Silence is not one of them. Register drift is worse than translation drift: the
reader gets the *wrong content* in the right language, and nothing looks broken.

> This is not hypothetical. Two facilitator articles on data protection drifted
> apart until they gave different answers to "where is the data stored" — and the
> statement turned out to be repeated in five places, one of them the public privacy
> statement. Nothing detected it for months. This checklist line exists because of that.
>
> The fix was not to correct all five. It was to give the fact **one** home — the
> public statement — and have everything else point at it.

`see_also` lists related articles that belong to a *different* concept. Those are
worth a glance but do not require action.

---

## 5. Identifiers, versions, files

- `article_id` is permanent. Content changes bump `version`; the id never changes.
  Code, deep links (`?help=<id>`) and AI citations all point at it.
- New ids carry **no numeric prefix**. Reading order lives in `order`. The numeric
  prefixes on the migrated articles (`03-`, `p3-`) are frozen history, not order.
- Ids must match `^[a-z0-9-]+$`. Anything else returns 400 from Pronoia's API.
- File path is `articles/<register>/<lang>/<article_id>.md`, and the file **must**
  keep an `# H1` heading: Pronoia reads the title from it.
- Filenames are case-sensitive on the server even when they are not on your Mac.
  A capital letter is the single most common cause of a broken link.

---

## 6. Where changes are made

All content changes are made **in this repository**. Pronoia, the reports and the
plugins read a release tag; they never write.

If you spot an error while using Pronoia, use "Suggest a correction", which opens an
issue here prefilled with the article id and version. Editing the copy inside Pronoia
does nothing lasting: it is a build artifact and the next build overwrites it.

Releases are tagged and each tag gets its own DOI. A study freezes the tag it ran
under, so a report can cite the method definition that was in force at the time —
not the current one. That only works if tags are cut deliberately: see `README.md`.

---

## 7. Adding a new article

1. Decide the **concept**. Does it already exist in `registry.yml`? If yes, you are
   adding a register variant, not a new concept.
2. Decide the **register**. If you cannot say which one, the article is not ready.
3. Add the entry to `registry.yml`: the id under `registers`, and a block under
   `articles` with `public` and `kb_include` (plus `public_reason` if `public: false`).
4. Write the article in `en` first, with full front matter.
5. Run `validate.py`. Translate. Run it again.
6. Open the PR. Complete the checklist in §3 in the PR description, including the
   register cross-check.

A human merges. The orange rule applies here too: **the publication decision is
always made by a person.**
