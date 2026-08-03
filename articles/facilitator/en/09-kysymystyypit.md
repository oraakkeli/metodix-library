---
article_id: 09-kysymystyypit
concept: kysymystyypit
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: 'Question types: a selection guide with examples'
order: 9
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

# Question types: a selection guide with examples

Pronoia has ten question types (+ criterion variables). The choice of type decides *what you can learn from the panel*: the same topic yields different knowledge as a scale rating, a timing estimate or a resource allocation. Rule of thumb: pick the lightest type that answers your research question — and always ask for the rationale.

## Basic types

### Scale (scale)
**What:** the panelist rates a statement on a numeric scale (default 1–9); optional **criterion variables** (e.g. probability × desirability) produce several ratings of the same thesis.
**Use when:** you want to measure support, probability or desirability and track consensus across rounds. The workhorse of Delphi.
**Example:** *"General-purpose AI handles more than half of municipal customer service by 2035."* Criteria: probability + desirability.
**Result:** distribution, central tendencies, IQR, position on the scale; the P×D gap reveals threat/wish tensions.

### Open (open)
**What:** a text answer only, no numeric rating.
**Use when:** you are mapping a phenomenon you cannot yet phrase as statements — round 0/1 ideation, weak signals, collecting concepts.
**Example:** *"What is the most important change in expert work that no one takes seriously yet?"*
**Result:** qualitative material for argument analysis; often the raw material for the next round's theses.

### Ranking (ranking)
**What:** the panelist puts the given options in order of preference.
**Use when:** you need a priority order over a bounded set — but intensity does not matter (cf. allocation).
**Example:** *"Rank the drivers by their impact on the quality of remote teaching: teachers' skills · tools · pedagogical models · students' self-direction."*
**Result:** mean rank per option; dispersion flags the most contested items.

### Multiple choice (multichoice)
**What:** selection from given options (one or several).
**Use when:** the question is a classification or "which of these" — no order, no intensity.
**Example:** *"Which barriers slow AI adoption in your organisation the most? (choose 1–3)"*
**Result:** selection shares; a quick map to base follow-up questions on.

## Structuring and prioritisation types

### Grouping (grouping)
**What:** the panelist sorts items into facilitator-defined bins by dragging (card-sort).
**Use when:** you want the panel to classify a set of phenomena — e.g. signals by maturity, theses by acceptability, or actions by urgency.
**Example:** items = 8 weak signals; bins = *Hot · Cool · Cold*. Or: actions into bins *Now · 3 yrs · 10 yrs · Never*.
**Result:** per item a bin distribution + modal bin; disagreement shows as spread across bins.

### Allocation (allocation)
**What:** the panelist distributes a fixed total (default 100 points) among options.
**Use when:** order is not enough and you need *how much* — resource allocation, or distributing probability mass over mutually exclusive scenarios.
**Example:** *"Distribute 100 points on how the municipality should weight climate actions: transport · buildings · energy · food · offsets."* Or: *"Distribute 100% over four scenarios by probability."*
**Result:** mean allocation + dispersion per option; normalised, it reads directly as probabilities.

### 2×2 positioning (xy)
**What:** the panelist places the topic as a point on a two-axis plane by dragging.
**Use when:** two dimensions must be judged *relative to each other* — classically impact × uncertainty (deriving scenario axes) or probability × desirability as one map.
**Example:** thesis = *"Quantum computing breaks current encryption"*; axes = impact (x) × uncertainty (y).
**Result:** scatter + centroid + quadrant distribution; two camps in different corners is a finding in itself and a scenario-axis candidate.

## Time types

### Temporal estimate (temporal)
**What:** the panelist gives **a single year** when the statement comes true — or "not within this horizon".
**Use when:** you want a quick timing estimate over a large set of theses; the distribution expresses the panel's uncertainty.
**Example:** *"In which year will more than half of matriculation exams be taken with AI assistance?"* (range 2026–2050).
**Result:** year histogram + median + beyond share. A bimodal distribution = timing dissensus.

### Time window (timewindow)
**What:** the panelist gives **two years** (earliest–latest) under a chosen criterion (*possible* or *probable*); a "never" option is available.
**Use when:** each panelist's *own uncertainty* is part of the data — a narrow window is a confident stance, a wide one an uncertain one. Analytically richer than temporal, heavier to answer.
**Example:** *"A fusion power plant feeds electricity into the Finnish grid."* Criterion: probable; range 2030–2070; never allowed.
**Result:** window bars + median window + earliest/latest quartiles + never share; consensus from IQR width.

### Time series (timeseries)
**What:** the facilitator enters a realised historical series; the panelist continues it with ≥3 evenly spaced estimate points (dragging on the chart or number fields).
**Use when:** the phenomenon has a measurable volume and historical data — quantitative foresight where everyone anchors to the same starting point.
**Example:** *"Share of remote work in expert workdays (%)"*: history 2010–2025, estimates for 2030/2035/2040.
**Result:** median curve + interquartile band extending the history; the widening of the band shows how far the panel's view carries.

## Quick picker

Support/probability → **scale** · ideation → **open** · order → **ranking** · categories → **multichoice** or **grouping** · how much → **allocation** · two dimensions → **2×2** · when (quick) → **temporal** · when + uncertainty → **time window** · how much in the future → **time series**. And in all of them: the rationale is what Delphi lives on.
