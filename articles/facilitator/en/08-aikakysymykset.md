---
article_id: 08-aikakysymykset
concept: aikakysymykset
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: 'Time questions: time window and time series'
order: 8
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

# Time questions: time window and time series

An ordinary scale thesis asks *how probable or desirable* something is. Time questions ask *when* and *how much*. Pronoia has two time question types, designed especially for foresight studies.

## Time window — when?

The panelist estimates the timing of an event as a **window**: the earliest and the latest point in time. Instead of a point forecast you get a range that also expresses the respondent's uncertainty — a narrow window is a confident stance, a wide one an uncertain stance.

**Criterion.** When creating the thesis, the facilitator chooses whether panelists estimate the **possible** or the **probable** timing. Possible produces wider windows (what is conceivable at all), probable narrower ones (what to prepare for). The criterion is shown to the panelist as the question prompt — mixing the two makes answers incomparable, so pick one.

**"Will never happen".** A classic lesson from timing Delphi: forcing a sceptic to name a year skews the distribution. The never option (on by default) lets doubt show honestly. Never answers are reported as a **share** and excluded from the timing quartiles — 30% never plus a narrow median window is a different finding than a narrow window alone.

**Results.** The panel's answers are drawn as window bars with the **median window** highlighted on top (from the median of the earliest estimates to the median of the latest). Consensus (0–1) is computed from the interquartile ranges of the earliest and latest estimates relative to the answer range: the more tightly panelists land on the same years, the higher the consensus. The same figure appears in the convergence table.

## Time series — how much?

The facilitator enters a **realised historical series** (e.g. electricity consumption 2010–2025), and the panelist continues it with at least three evenly spaced future points. History anchors the estimates: everyone sees the same starting point and takes a stance on the continuation of the same quantity.

**Parameters.** The name and unit of the quantity (y-axis), the interval in years (even spacing on the x-axis) and the number of estimate points (at least 3). The years to estimate are derived automatically from the last year of the history.

**Results.** The panel's estimates condense into a **median curve** and an **interquartile band** (Q1–Q3) extending the history; individual estimates show as faint paths. A wide band signals dissensus, and the *widening of the band over time* is particularly interesting — panels tend to agree more about near years than distant ones.

## Sibling type: temporal estimate

Pronoia also has a lighter **temporal estimate** (`temporal`): the panelist gives **a single year** (or "not within this horizon"), and the result is a year histogram + median. Division of labour: **temporal** when a quick point estimate is enough and the distribution captures uncertainty; **time window** when you want *each panelist* to express their own uncertainty (window width) and the criterion (possible/probable) — analytically richer but heavier to answer.

## Which one when?

**Time window**, when the question is about the timing of an event or transition ("when will X become common / possible"). **Time series**, when the phenomenon has a measurable volume and historical data ("how will the amount of X develop"). In both, the rationale matters as much as the numbers — dialogue and revisions work as in other thesis types, and round-to-round convergence is computed for time questions too.
