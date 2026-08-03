---
# ── Identity ────────────────────────────────────────────────────────────────
# article_id is permanent and must equal the filename stem. It must match
# ^[a-z0-9-]+$ — anything else returns 400 from Pronoia's API. New ids carry no
# numeric prefix; reading order lives in `order`.
article_id: my-article-slug

# The concept this article belongs to. Must already exist in registry.yml, and
# this article's id must be listed there under `registers` and `articles`.
concept: my-concept

# ── Placement ───────────────────────────────────────────────────────────────
# register and lang must match the directory: articles/<register>/<lang>/
register: public          # facilitator | panelist | public
lang: en                  # en | fi | sv
source_lang: en           # the language this article is authored in.
                          # `en` for new articles; `fi` for the 2026 migration.

# Other languages in which THIS file exists on disk. Must match reality exactly —
# validate.py compares it against the other language directories.
translations: [fi, sv]

# ── Content metadata ────────────────────────────────────────────────────────
title: "Article title"
version: "1.0"            # N.N — bumped by every content change
last_updated: 2026-08-03  # YYYY-MM-DD — set by every content change
license: CC-BY-4.0
authors: ["Metodix Oy"]

# ── Distribution ────────────────────────────────────────────────────────────
# These two MUST match registry.yml, which is the source of truth for
# distribution decisions. validate.py fails if they drift (V17).
status: published         # draft | published
public: true              # may this file appear on the public site?
kb_include: false         # feed to the AI helpdesk's grounding corpus?
                          # facilitator register only, published only.

# Reading order in the in-app reader. REQUIRED for facilitator and panelist;
# omit for public.
# order: 1

# ── Optional ────────────────────────────────────────────────────────────────
# doi: ""
# first_published: 2026-08-01
# original_source: "https://metodix.fi/..."
# stateHelpId: ...        # facilitator: the study state that surfaces this article
---

# Article title

An H1 is required. Pronoia reads the title from it, and validate.py fails without
it (V13).

Opening: two or three sentences on what the reader gets from this article.

## Sections

Write for the register you chose. A panelist article is readable in 60 seconds and
uses no product-internal names. A public article is understandable without Pronoia.
A facilitator article says what the reader should *do*, not only what is true.

State a fact in one place only. If it has a canonical home elsewhere, link to it —
a repeated fact is a future contradiction.

---
*Sources and attribution here. This article is part of the Metodix Library (CC BY 4.0).*
