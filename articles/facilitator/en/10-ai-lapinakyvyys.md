---
article_id: 10-ai-lapinakyvyys
concept: ai-lapinakyvyys
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: AI transparency and AI panelists
order: 10
version: '1.0'
last_updated: '2026-07-11'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# AI transparency and AI panelists

Pronoia uses AI in two roles: **AI panelists** take part in the panel as synthetic perspectives, and **AI generation features** assist the facilitator (e.g. thesis drafts, summaries). This article describes how the use of AI is made visible — both because the EU AI Act (2024/1689, Art. 50) requires it from 2 August 2026, and above all because the validity of a Delphi study requires that synthetic and human arguments remain distinguishable at every stage.

## What the panelist sees

When a study includes AI panelists, the panelist is shown an **AI notice** on the home view before they start responding. The notice states the presence, number and marking of AI panelists. It cannot be hidden. You can supplement the standard text with a study-specific note (the genai note in study settings) — for example explaining why AI panelists are used in this particular study.

In dialogue and results, content produced by AI panelists is always marked with the 🤖 indicator. Panelists see AI panelists under a pseudonymous code just like humans — but with an AI prefix.

## What the facilitator sees

In the facilitator view, AI panelists appear as **AI · role** (e.g. "AI · climate researcher"). The panel participation card shows human and AI counts separately (👤 / 🤖).

## Machine-readable marking in exports

All data leaving for analysis carries an explicit AI marking:

- **DAE Handoff (JSON)**: every panelist, argument, dialogue and revision record includes an `ai_generated` field (true/false). The payload's `ai_provenance` block summarises provenance: AI panelist count, default model used, and the marked fields.
- **CSV export**: an `ai_generated` column on every row.

The DAE analysis pipeline relies on these markings to keep synthetic and human arguments separate — the marking is not just a regulatory requirement but a precondition for analysis quality.

## Data protection in AI features

AI generation uses Anthropic's Claude API. Panelists' open responses are sent to the API **without identity data** (pseudonym only). API data is not used for model training. All AI features have a rule-based fallback, so a study can run entirely without AI.

## Facilitator checklist

1. Mention the use of AI panelists already in the invitation — don't let it come as a surprise.
2. Write a study-specific genai note: why AI panelists are used and what their profiles are based on.
3. Never strip AI markings from reports or publications — the marking is both a legal and a methodological requirement.
