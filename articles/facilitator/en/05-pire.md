---
article_id: 05-pire
concept: pire
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: PIRE — the inter-round assistant
order: 5
version: '1.0'
last_updated: '2026-06-27'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# PIRE — the inter-round assistant

PIRE (Pronoia Inter-Round Engine) is an **advisory aid for the gap between rounds**. It reads the previous round's results and the study's locked choices (orientation, consensus/dissensus) and proposes, one thesis at a time, how to build the next round. PIRE proposes — you confirm.

## Signals

For each thesis PIRE identifies a signal:

- **Convergence** — the estimate is stable and narrow; consider locking the question.
- **Stable dissensus** — genuine tension (wide spread, opposing reasons); recycle the arguments.
- **Noisy spread** — wide, unstructured; possible wording flaw → reformulate.
- **Emergent theme** — a new topic or reversal; raise it as a statement.
- **Bandwagon flag** — suspiciously sharp convergence; don't read it as consensus.

## Operations and the mask

From the signal a proposed **operation** (O1–O7) is derived: statistical feedback, extreme-position justification, argument recycling, theming, scenarios, convergent feedback, or panel supplement. **Locked choices constrain** the allowed operations: orientation and the question mode intersect to define the operation space, and the mask cannot be bypassed (e.g. in dissensus mode the central value alone is forbidden).

## Facilitator handles

Each card has four handles: accept the proposal, change the operation (from the allowed set), flip the mode (consensus⇄dissensus), or lock the thesis. "Build round from PIRE choices" copies the unlocked theses as a base; you edit them into final form.

## Boundary: PIRE ≠ analysis

PIRE is **quick triage, not deep analysis**. It proposes the operational next step but does not interpret for you. Theming, scenarios, and argument analysis — genuine interpretation — are done in the DAE ecosystem under quality gates. This boundary is deliberate: an over-deterministic inter-round engine would lead to malpractice of the method.
