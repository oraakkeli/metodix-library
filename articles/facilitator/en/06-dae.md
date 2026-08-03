---
article_id: 06-dae
concept: kuvaileva-vs-tulkitseva
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: Pronoia and DAE — the division of labour
order: 6
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

# Pronoia and DAE — the division of labour

Pronoia and the DAE ecosystem are different tools for different tasks. Understanding the boundary between them matters methodologically, because it prevents confusing **description** with **interpretation**.

## Who does what

**Pronoia = facilitation and description.** Designing the phenomenon and theses, the panel, rounds, dialogue, the pause, the PIRE inter-round assistant, and **descriptive results reports** (distributions, central tendency, consensus/dissensus, round movement, arguments verbatim).

**DAE = deep analysis.** Interpretive analysis with quality gates (κ/QVG) and human review: theming, scenarios, argument and discourse analysis, causal layers, multi-level perspective, synthesis. DAE is the methodological authority.

## Descriptive vs. interpretive

A Pronoia report tells you **what the panel said and how views moved** — not *what it means*. "What it means" is interpretation, and that belongs to DAE. This boundary appears in the footer of every Pronoia report: the report is not an analysis but its source material.

## How the handoff happens

Pronoia has a DAE Export tab that produces the material the DAE pipeline reads: an eDelphi CSV, a Handoff Package (JSON read by DAE CP-0/CP-2), and DAE_STATE.json. After any round, the data can be sent to DAE for real analysis.

## What if DAE is not available?

Not everyone has the DAE ecosystem. For them Pronoia offers **descriptive report forms** (summary, per-thesis result cards with arguments, round comparison) in HTML/PDF and Word. They provide a proper overview — but deliberately stay descriptive; they do not replace DAE's interpretation.

## Why the boundary is kept strict

If Pronoia started doing interpretive analysis — or if PIRE/AI assistants generated "finished" conclusions — it would create a false sense of precision and a risk of malpractice of the method. That is why generative assistants (e.g. deepening suggestions) are always drafts that the facilitator owns, flagged as requiring audit.
