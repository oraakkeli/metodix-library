---
article_id: 14-paneelin-tila
concept: paneelin-tila
register: facilitator
lang: en
source_lang: fi
translations:
- fi
- sv
title: Panel state — what is measured and how to read it
order: 13
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

# Panel state — what is measured and how to read it

When a round closes, the facilitator's first question is always the same: **where is the panel now?** The answer is not one number but three questions that are easily confused.

- **Where is the panel?** One thesis's distribution in one round.
- **Does it stay there?** The change between two rounds — stability.
- **Is anyone there?** How many answered and how many came back — coverage.

The third is the one most often forgotten, and it is decisive. **A missing dimension cannot be substituted by another.** Stable agreement produced by the six panelists who remained is not a stronger result than moving disagreement among forty. That is why the ecosystem's composite indicators are aggregated **geometrically**: if one sub-index is zero, the whole figure is zero and nothing can compensate for it.

## Three measures that must not be conflated

**Agreement at thesis level — Agreement A.** The base measure is van der Eijk's *Agreement A*, built precisely for ordered rating scales (1–5, 1–7, forced ±3). It runs from **−1 to +1**: +1 is complete agreement, 0 is flat dispersion, −1 is the panel split between the two ends of the scale. It is computed from a single distribution and needs no second round.

**Process — stability and convergence.** Between two rounds we look at how much the distribution moved and whether the quartiles narrowed. The established rule of thumb is the **15 % rule**: a smaller change counts as stable. Direction and stability are different things — a distribution can narrow and still wobble, or stay wide and be completely still. The latter is often the more valuable finding.

**Study state — the lead indicator.** The thesis-level figures are gathered into one state, which depends on the variation: **CDI, CCI, RCI or BCI**.

Confusing these is the most common error: "the panel agrees" can mean any of the three, and they lead to different actions.

## Why the threshold is derived, not chosen

This is the methodological core of the measurement, and it changes how the figures are read.

A has a **strong positive small-sample bias**. From a completely random distribution of eight panelists, A averages about 0.20, and one in twenty produces as much as 0.55. A fixed threshold — say "above 0.40 is consensus" — therefore makes a small panel look unanimous even when its answers are pure noise. This was precisely why test panels always looked uniform.

The solution is not a better threshold but **deriving it every time**: the ecosystem draws thousands of random panels of the same size and the same scale as your thesis, and reads the ceiling of the noise from them. On a five-point or longer scale that ceiling follows the form **≈ 1.55 / √n** — about 0.28 with thirty panelists, above 0.50 with eight. On a shorter scale the coefficient is larger: the length of the scale matters too, not only the number of respondents.

Two practical rules:

- **Do not compare A across theses without their thresholds.** A thesis that emerged later and was answered by 12 people is not more unanimous than a 40-respondent thesis, even if its figure is higher.
- **Every figure states its own criterion.** The result always carries the threshold used and its basis. If no criterion is shown, the figure was not meant to be reported.

The same discipline governs the valley test, the quadrant structure and the explanatory power of a group split. Not one threshold is chosen by hand.

## Four places where disagreement is found

A unanimous-looking figure is not proof of unanimity. A panel can disagree in four ways, of which only the first shows up directly in A.

**1. Negative A.** The classic split, mass at both ends of the scale. The clearest and the rarest.

**2. A valley in the distribution.** The panel splits in two, but close enough together that A stays positive. This happened to the clearest dividing line in the CoWup Delphi: 43 % against 54 % across the valley, and A still +0.16. Without a separate valley test the panel's most interesting split would never have reached the tension map. The test is null-calibrated and **requires human confirmation** — it is an observation, not a classification.

**3. The anti-diagonal of the quadrant.** Each criterion variable can be unanimous on its own while the panel still splits. Next section.

**4. Between-group dispersion.** Moderate A does not mean the question was not understood; it can mean **two internally coherent images of the future** whose sum looks scattered. In the Learning Analytics Delphi the thesis "A lost promise" scored A = 0.39 in aggregate — "moderate agreement" — but inside a future image A was 0.81. This is the premise of Petri Tapio's Disaggregative Policy Delphi, and the rule that follows is: **low A is a question, not an answer.**

## Two criterion variables — the quadrant is not the sum of two numbers

A thesis is typically assessed on two criteria: probable and desirable (or impactful, or feasible). Their **joint distribution is information in its own right**, not a derivative of the margins.

The proof is simple. A panel that lands in the cells "improbable & undesirable" + "probable & desirable", and a panel that lands in the cells "improbable & desirable" + "probable & undesirable", produce **exactly the same marginal distributions** — identical figures on both axes. Yet the first is in harmony and the second is tearing apart.

The quadrant is read knowing the axes. Probability × desirability with a positive relationship is **wishful thinking**: what I want, I also judge likely — and what I do not want, I judge unlikely. Probability × impact with the same relationship is not that but a statement that "the more likely, the more consequential". The ecosystem refuses to name the phenomenon if the axes have not been declared.

## The variation decides what a figure means

The same distribution means different things in different variations. Each therefore has **its own lead indicator** and a gate that must be passed before the headline figure can be read.

| Variation | Indicator | Sub-indices | Gate — without this the headline figure does not hold |
|---|---|---|---|
| **Classical** | CCI | agreement × stability × coverage | **Stability.** Without it consensus is not interpreted at all. |
| **Argument** | CDI | polarization × stability × argumentation | **Argumentation.** A stable split without reasons is not a result. |
| **Real-Time** | RCI | position × settling × exposure | **Settling, then exposure.** A position does not count if the respondent has not seen the group's state. |
| **Barometer** | BCI | magnitude of change × continuity confidence | **Comparability.** If the theses or the panel changed, the change is an artefact. |

**Classical (CCI):** *exploration → convergence → crystallization*, or *dissensus*. If the distribution wobbles, you are still in exploration no matter how narrow it happens to be right now. A stable split is not a failed consensus but **dissensus** — it moves on to tension analysis.

**Argument (CDI):** *exploration → articulation → crystallization*, with *collapse*, *divergence* and *noise* as side paths. Here the good news is a **high** CDI: argued, stable, rival futures. Disagreement disappearing is not a victory but a reason to suspect artificial consensus. A stable but under-argued split is *articulation* — ask for the reasoning, not for a new vote. If the distribution is still moving, what matters is whether the movement is structured (*divergence*) or not (*noise* — check how the thesis is worded).

**Real-Time (RCI):** *seeding → flow → settling → settled → confirmed*. In a roundless setting stability means equilibrium, not the difference between rounds. A panel can look settled merely because some have not come back to look — which is why exposure is a gate of its own.

**Barometer (BCI):** *baseline → stable → signal → alert*, with *artefact* as the failure state. Here **change is the finding**, not an error — the opposite of the others. But it is readable only once the comparability of the waves has been established: a quietly edited thesis produces change that tells you about the thesis, not about the world.

**The first round is a special case in all of them.** There is no stability when there is nothing to compare against. The indicator is then undefined — not zero, not a guess. A single round's "consensus" is a description of a distribution, not a result of a process.

## Does the panel talk to itself?

Delphi **assumes** interaction: experts see each other's reasoning and develop their positions. The ecosystem now measures that assumption too, because it turned out to be unreliable.

All 783 arguments from two real Delphis were screened for references between panelists. Genuine peer references numbered **two** — about 0.5 %. At the same time, speech directed at the facilitator (edit proposals, terminology notes, criticism of how the question was posed) made up more than a quarter of everything in one round. The panelists wrote actively — in one direction.

**This is not the panel's fault.** Neither setup had a channel in which a panelist could address another: they did not decline to converse, no conversation was opened to them. The rule is therefore strict — a monologic corpus **must not be reported as a characteristic of the panel** ("the panel did not engage", "the discussion stayed thin") before it has been established whether a channel existed. That is design information: to be asked, not inferred.

The same applies to the **climate**, which is derived from dialogue moves: if there are no moves for a structural reason, the climate is not reported at all — not even as "neutral". No emotional weather is read from an empty distribution.

In Pronoia the channel does exist: the **dialogue phase**, where a panelist sees a pseudonymous peer view and can respond to others' reasoning. That is the only place a peer reference can arise — the preparatory Round 0 chat is held with Kastalia, so it runs between a panelist and an assistant, not between panelists. The measured 0.5 % is therefore both the methodological justification for the dialogue phase and the baseline against which its effect can be established.

## Where each figure is computed

**In Pronoia**, PIRE performs a fast triage between rounds: median, interquartile range and an adjustable threshold → a signal and a proposed operation. It is **deliberately coarse** and made for building the next round, not for reporting; the readability badge serves the same purpose: it says whether the result can be read, not whether the panel agrees. **In the DAE analysis** the calibrated instrument set is computed — Agreement A with its own thresholds, the valley test, the quadrant, the explanatory power of a group split, and the variation's lead indicator. That is where the report's figures come from.

Two limits hold in both:

- **Indicators are computed from human voices only.** A position produced by AI is not a panelist's voice. An AI panel may be run alongside as a benchmark, but it is reported separately — compared, not blended.
- **The machine computes, the human interprets.** The valley test, the naming of groups and the confirmation of peer references are human work. The machine tells you where to look, not what to see.

## Facilitator's checklist

- Ask the three questions separately: where the panel is, whether it stays there, whether anyone is there.
- Do not read a single round's consensus as a result of the process — stability begins with the second round.
- Do not compare A across theses without thresholds; a small n raises the figure without anything having changed.
- When A is moderate, ask whether the dispersion is unstructured or between groups. Different conclusion, different action.
- Look at the quadrant, not at two marginal distributions. The same two figures describe two different panels.
- In an Argument Delphi, disagreement disappearing is suspicious, not successful.
- Before you describe a panel as quiet, check whether it had a channel to speak.

*See also "Consensus vs. dissensus", "Orientations N/S/R/E/D", "PIRE — the inter-round assistant" and "Pronoia and DAE".*
