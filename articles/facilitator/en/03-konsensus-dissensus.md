---
article_id: 03-konsensus-dissensus
concept: konsensus-dissensus
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: Consensus vs. dissensus
order: 3
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

# Consensus vs. dissensus

A common misconception about Delphi is that the goal is always **unanimity**. It is not. The goal depends on the question: sometimes you seek a shared estimate (consensus), sometimes you map and sharpen reasoned disagreement (dissensus).

## Two goal logics

**Consensus-seeking.** The purpose of feedback is to narrow the distribution toward a shared estimate. The metric is narrowing spread and stability. Suited to forecasts and questions where a "correct" estimate exists.

**Dissensus-valuing.** The purpose of feedback is to map and sharpen disagreement — to produce **several reasoned futures**, not a single number. Extremes are not lured toward the middle but asked to justify. Suited to value questions and ruptures.

## A hard rule

In dissensus mode the feedback is **never the central value alone** — always the distribution AND anonymized reasoning. This prevents artificial consensus at the architectural level: value disagreement is not accidentally "smoothed" away.

## In Pronoia

A study's basic character comes from the Delphi type: **classical ≈ consensus**, **argumentative ≈ dissensus**. PIRE reads this as the default. A single thesis can still be tagged P (probability → consensus) or D (desirability → dissensus), overriding the study default — so that even in a consensus-seeking study a single value thesis can be dissensus. The PIRE card always shows where the mode for each thesis comes from.

## Readability, not a consensus light

The result views used to carry a traffic light where green meant consensus and red meant dissensus. **It is gone.** The facilitator's overview now shows a **readability badge**: whether the result can be read at all — is the round closed, is coverage sufficient — not whether the panel agrees. The panelist's view lost the light entirely: what belongs to a panelist is their own position relative to the panel, not a verdict about it.

Thesis-level information is descriptive: the distribution, the median, the interquartile range, and the **position** — where on the scale the panel sits. Colour shows position, not whether the result is good. The consensus classification with calibrated thresholds is made in the DAE analysis, because the threshold depends on the number of respondents and the length of the scale and cannot be read off these figures.

Disagreement is not a failure — it may be the study's most important finding. This used to need saying, because a red light implied otherwise. The display no longer makes that claim, so the explanation is no longer needed.

## Consensus in time questions

Consensus is computed for **time window** theses too: it measures how tightly the panelists' earliest and latest estimates land on the same years (interquartile widths relative to the answer range). The figure appears in the convergence table alongside the scale theses. "Will never happen" answers are reported as a share outside the quartiles — a large never share next to a narrow median window is a dissensus finding in itself. In a **time series**, dispersion is read from the width of the interquartile band; the band widening towards distant years is normal and shows how far the panel's view carries. (See the article "Time questions".)

## A deeper reading

What the ecosystem actually computes — Agreement A and its calibrated threshold, stability and coverage, the four places where disagreement is found, and the variation-specific indicators CDI/CCI/RCI/BCI — is gathered in the article **"Panel state — what is measured and how to read it"**.
