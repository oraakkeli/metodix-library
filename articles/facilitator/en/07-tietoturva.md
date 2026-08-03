---
article_id: 07-tietoturva
concept: tietosuoja
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: Security and transparency
order: 7
version: '1.0'
last_updated: '2026-08-02'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# Security and transparency

As facilitator you are the study's **data controller**: you are responsible for what data
is collected, how panelists are informed, and how their rights are met. This article covers
the essentials; the full statement is in `docs/SECURITY-TRANSPARENCY.md`.

## Where the data lives

The material is held on a **server located in the EU** and processed in accordance with
EU data protection law. Traffic is encrypted, panelists reach the study through single-use
invitation links without passwords, backups stay within the EU, and changes to the software
pass through automated checks and a staging environment before production. Current
processors and retention periods are listed in the public statement: /privacy.

The material does not leave the service automatically. The two situations in which it does
are both your decision: **using the AI features** and **exporting the material** (CSV,
DAE handoff, reports).

> As the data controller, note that the infrastructure provider and the AI service are
> processors of personal data. The current list is in the statement.

## AI and Anthropic

When AI features are enabled, some data is processed by the Anthropic API: the help desk
sends your question + the method library, deepening suggestions send theses and
**panelist arguments under pseudonyms** (P-NN), AI panelists send theses + profile.
**Names and emails are never sent** — only pseudonyms and content.

**Choose the study's AI level** in settings ("AI use in this study"): *No AI* (nothing is sent
to an AI provider), *Help only* (default; method help only, no panel content), or *Full* (also AI
panelists, R0 chat, deepening, coding). The choice gates every AI call.

If you want nothing sent to an AI provider on any study: **do not set `ANTHROPIC_API_KEY`**
(host master switch). AI features then degrade gracefully and Pronoia runs without an AI
provider regardless of a study's AI level. The switch does not affect where the data is
held, nor exports.

## Anonymity

Panelists see each other only by pseudonym. **Facilitator-blind** mode hides names and
emails from you too. **Recommended for sensitive panels: run facilitator-blind.** The DAE
handoff and CSV export **never** contain names or emails — regardless of the blind setting
(as of 07/2026). Note: free text can reveal identity through content even when the
identifier is hidden.

## Anonymization when the study ends (07/2026)

When a study is complete, anonymize it: the **🔒 Anonymize study** button on the Panelists
tab permanently deletes names and emails and revokes invite links. The remaining material
is truly anonymous research data — pseudonyms with no key back to a person. The action is
**irreversible** (two-step confirmation) and recorded with a timestamp. Anonymizing an
open study cuts panelist access — do it only at the end.

## The small-cell rule (n < 3)

A panel matrix cell with fewer than three humans can identify a person even without a
name. The matrix health card warns about such cells (🔒), and they travel as a
machine-readable `small_cells` list into the analysis export. **Do not publish cell-level
figures for cells of fewer than three people without their consent.**

## Access key (production)

In production the facilitator environment is protected by an access key: the browser asks
for it once and remembers it. You get the key from your administrator. Panelist response
links work without the key. (In local development no key is asked.)

## Public privacy notice

A public privacy & AI notice (fi/en/sv) lives at **/privacy**. The link is automatically
included in every invitation and on the panelist home view. For AI transparency in detail,
see the article *AI transparency and AI panelists*.

## Panelist rights

Inform panelists before R0: what is collected and why, whether AI is used, how anonymity
works, retention period, and rights (access, rectification, **erasure**). Erasure is
supported: you can delete a study, a panelist, a thesis, and a comment.

## Quick check before publishing

1. AI on or off? Appropriate for the data's sensitivity?
2. Sensitive panel → facilitator-blind.
3. Panelists informed? The invitation automatically carries the AI notice and the /privacy link.
4. AI model version pinned (reproducibility — see the AI models doc)?
5. Exports treated as confidential; retention and final deletion agreed.
6. Small matrix cells (n < 3) checked — no cell-level figures in reports without consent.
7. When the study ends: 🔒 Anonymize study.
