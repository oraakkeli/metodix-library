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
version: '1.2'
last_updated: '2026-08-12'
license: CC-BY-4.0
authors:
- Metodix Oy
status: published
public: false
kb_include: true
original_source: Delphi-Pronoia frontend/help
---

# Security and transparency

As facilitator you are the study's **data controller**: you are responsible for what
data is collected, how panelists are informed and how their rights are met. This
article gathers the essentials; the full account is `docs/SECURITY-TRANSPARENCY.md`.

## Where the data lives

The material sits on a **server located in the EU** and is processed under EU data
protection law. Traffic is encrypted, panelists reach the study through personal,
time-limited invite links with no passwords, backups stay in the EU, and software changes pass
automated checks and a staging environment before production. Current processors and
retention periods are in the public notice: /privacy.

Data does not leave the service by itself. The two situations where it does are both
your decisions: **using the AI features** and **exporting the material** (CSV, DAE
handoff, reports).

> As controller, note: the infrastructure provider and the AI service are processors
> of personal data. The current list is in the notice.

## Your account and signing in

A facilitator has a **personal account**: email and password. Shared logins are not
used, because a shared login makes it impossible to see afterwards who did what — and
impossible to remove access from one person at a time.

- **A new account comes from an invitation.** Open registration is closed after the
  first administrator. The account invitation link is single-use and expires. (A
  panelist's invite link is a different thing: it is personal and **reusable** — the
  same address carries them from round to round — but it too expires, and you can
  renew or revoke it on the Panelists tab. Renewing kills the old link, so exactly one
  live link exists per panelist.)
- **You can reset your own password** from the sign-in page if email delivery is
  configured on the server. An administrator can also reset it.
- **Two-factor authentication** is optional for everyone and **required of
  administrators**. You turn it on from your profile page with an authenticator app
  (Google Authenticator on a phone, Apple Passwords on a Mac, and others). Save the
  backup codes during setup — they are not shown a second time.
- **You can see your own sessions.** The profile page lists the devices where you are
  signed in, and you can end any of them or all but the current one.

An administrator can end a user's sessions without closing the account. They **cannot**
see anyone else's session list and cannot disable another person's two-factor.

## Who can see your study

A study has three roles:

| Role | Sees | Can change | Personal data |
|---|---|---|---|
| **Owner** | everything | everything, incl. members, AI mode, blind mode, deletion | yes (except in blind mode) |
| **Facilitator** | everything | the study's content | yes (except in blind mode) |
| **Viewer** | results | nothing | **never** |

Viewer is the role you hand to a funder or an evaluator: read access to results is not
access to the people behind them.

A study may belong to an **organisation** (university, municipality, company). Then the
organisation's admin is an owner even after the researcher leaves the institution, and
AI costs come from the organisation's wallet. Without an organisation the study is
personal — that is the default and fully supported.

**Ownership can be transferred** (Team & access page). Do it before you leave a
project: a study whose only owner is gone is stuck.

## Access history

Every change of rights is written to an immutable log: who added whom, what the role
was before and after, when an invitation was sent, revoked or accepted, when the study
was attached to an organisation, and when blind mode was switched off. The log is on
the study's **Team & access** page and is owner-level information.

This is the answer an institution asks for: *who has had access to this panel, and
since when*. Rows are never edited or deleted, and they survive the deletion of the
study or the user.

## AI and Anthropic

When the AI features are on, some data is processed through Anthropic's API: the
helpdesk sends your question + the method library, deepening suggestions send the
theses and **panelists' arguments under pseudonyms** (P-NN), AI panelists send theses +
profile. **Names and email addresses are never sent** — only pseudonyms and content.

**Choose the study's AI level** in settings ("AI use in this study"): *No AI* (nothing
goes to the AI service), *Method help only* (default; method assistance, no panel
content), or *Full* (also AI panelists, R0 chat, deepening, coding). The choice gates
every AI call.

If you want nothing sent to the AI service in any study: **do not set
`ANTHROPIC_API_KEY`** (the host switch). The AI features then degrade cleanly and
Pronoia runs without the AI service regardless of the study's AI level. The switch has
no bearing on where the data lives or on exports.

## Anonymity

Panelists see each other only under pseudonyms. **Facilitator-blind** mode hides names
and emails from you as well. **Recommendation for sensitive panels: run
facilitator-blind.** The DAE handoff and the CSV export **never** contain names or
email addresses — regardless of the blind setting. Remember: free text can identify a
person through its content even when the identifier is hidden.

Blind mode is **self-blinding**, not team management: it hides identities from
everyone, including the owner who switched it on. Turning it off reveals every panelist
to the whole team, and **that act is written to the access history**.

## Anonymization when the study ends

When the study is complete, anonymize it: the **🔒 Anonymize study** button on the
Panelists tab permanently removes names and email addresses and invalidates the invite
links. What remains is genuinely anonymous research data — pseudonyms with no key back
to a person. The action is **irreversible** (two-step confirmation) and is timestamped.
Anonymizing an open study cuts off panelist access — do it only at the end.

## The small-cell rule (n < 3)

A panel-matrix cell with fewer than three people can identify a person without a name.
The matrix health card warns about such cells (🔒) and they travel to the analysis
export as a machine-readable `small_cells` list. **Do not publish cell-level figures
from cells of fewer than three people without the consent of those involved.**

The same threshold is enforced in software: group-level results are not shown for
groups of fewer than three, small groups are folded into an "Other" group, and if that
group too falls below three, the whole breakdown is withheld — otherwise a small
group's figures could be derived by subtracting from the total.

## Public privacy notice

At **/privacy** there is a public privacy and AI notice (fi/en/sv). The link is added
automatically to every invitation message and to the panelist's home view. For more on
AI transparency, see the article *AI transparency and AI panelists*.

## Panelist rights

Inform panelists before R0: what is collected and why, whether AI is used, how
anonymity works, the retention period and their rights (access, rectification,
**erasure**). Erasure is supported: you can delete a study, a panelist, a thesis and a
comment, and an administrator can delete a user account entirely.

## Quick check before publishing

1. AI on or off? Does it suit how sensitive the material is?
2. Sensitive panel → facilitator-blind.
3. Panelists informed? The invitation automatically carries the AI note and the
   /privacy link.
4. Team roles checked — is viewer the right role for someone who only follows along?
5. AI model version pinned (reproducibility, see the AI models document)?
6. Exports treated as confidential; retention and final deletion agreed.
7. Small matrix cells (n < 3) checked — no cell-level figures in reports without
   consent.
8. When the study ends: 🔒 Anonymize study.
