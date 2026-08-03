---
article_id: 12-ai-kayttomuodot
concept: ai-kayttomuodot
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: AI usage modes and costs
order: 11
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

# AI usage modes and costs

In Pronoia, AI is a complementary tool, not a dependency: every Delphi runs fully without AI, and all AI functions degrade to a rule-based fallback. This article explains how to choose AI use consciously, what services are available, and how to keep costs under control.

## The three modes

AI use is selected with a single setting, graded by how much data is exposed to the AI:

- **No AI (off)** — nothing is sent to an AI provider; the whole process runs rule-based.
- **Method help (assist)** — the default; facilitator support only (Ask Pronoia, profiles, translation). No panelist-authored content is sent out.
- **Full** — also panelist content: AI panelists, Round 0 chat, PIRE deepening, coding suggestions.

Before a study moves into the process (opening the first round), you must **choose the mode consciously**. "No AI" is a fully equal option there. The level can later be raised, but not lowered below what panelists have already taken part in.

## Services

**Method help (assist is enough, no panelist content):** Ask Pronoia (method guidance), profile generation (AI-panelist profiles from the phenomenon frame), translation.

**Panelist content (requires full mode):** AI panelists (synthetic perspective arguments), Round 0 intake chat, PIRE deepening, coding suggestions.

The largest but most predictable item is AI panelists (cost = panelists × theses × rounds). The Round 0 chat is the smallest but least predictable, because it is interactive.

## Costs and caps

The backend cost of AI is converted into fixed **credits**, so you see only one conversion (e.g. 100 credits = €1). Before every run, a **pre-flight estimate** is shown ("≈ 390 credits ≈ €3.90") based on the panel size.

Spending can be limited by three caps, of which the smallest binds: **wallet balance**, **per-study cap**, and **per-facilitator/month cap**. When a cap is reached, AI does not exceed it but degrades gracefully to the rule-based function — the process continues without further cost.

There are three payment models: platform credits, your own API key (BYO), or a host key. Note: "your own Claude account" means an Anthropic **API key** (console.anthropic.com), not a claude.ai subscription.

## When to use which — examples

- **Sensitive human panel** (e.g. touching patient data) → **off**. Strongest privacy: nothing is sent to an AI provider.
- **A single researcher needing method support** → **assist**. Ask Pronoia + translation; panelist content stays on the machine.
- **A pilot without a real panel** → **full**. AI panelists simulate argumentation (Route B) to test the theses.
- **A hybrid panel missing a perspective** → **full, selectively**. A few AI panelists fill the blind spot; humans form the backbone.
- **A large multilingual panel** → **full + caps**. Round 0 + translation; set a per-study cap in advance.
- **An organization running many studies** → **full + own API key**. Costs on your own bill, data under your own terms (data sovereignty).

## Facilitator checklist

1. Choose the mode consciously — off is a fully equal option.
2. In full mode, review the pre-flight estimate and set a per-study cap if needed before generating.
3. Make sure panelists receive the disclosure about AI use (invitation + /privacy).
4. Keep the number of AI panelists justified — they complement, they do not replace, real expertise.
