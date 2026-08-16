---
id: 4
scope: srnd-group-strategy
slug: pricing-credit-and-terms
area: commercial
title: "Pricing is partner-only; SRND extends no credit directly, and IWOCA covers the UK"
status: proposed
version: 2
revised: 2026-08-16
supersedes: []
superseded_by: null
---

# ADR 0004 — Pricing is partner-only; SRND extends no credit directly, and IWOCA covers the UK

- **Status:** **Accepted** — 2026-08-16, Neil, at version 2 with end-user pricing removed.
- **Source:** `proposals.md`, consolidated. **This is a sort, not a rewrite** — the decisions below are as they
  were recorded, with their original evidence. *Nothing has been added; where the original was thin it stays
  thin.*

## Context

Trade-price gating is standard practice in this business. The credit position was recorded absolutely and
then corrected.

## Decision

**1. Pricing is registered-partner-only.** No public prices in the trade channel.

> **Amended at ratification — Neil, 2026-08-16.** The original read *"registered-partner-only, **including end
> users**"*, which does not make sense as written — an end user is not a registered partner. **End-user pricing
> is removed from this ADR and dealt with on its own** (`questions.md` Q42). *What stands here is the trade
> channel: no public prices, partner-gated.*

**2. SRND extends no credit directly, anywhere.** Payment is taken through the store; a dealer who wants credit
uses a credit card. A uniform, deliberate position — not a gap to close for any territory, but a position to
state plainly when asked.

### Recorded reversal — and it matters commercially

**2026-08-12 (Neil; surfaced by the srnd-os promotion sync of 2026-08-11 and resolved by Simon the same day).**
*"The UK included"* was too absolute. **What stands: SRND extends no credit *directly*, anywhere. What was
omitted: a UK-only 90-day interest-free facility is provided through IWOCA** — a third-party finance provider,
unavailable outside the UK. **The OS's `practices/sales/` already records the reconciled fact.**

## Provenance

**Consolidates `C4`, `C8`** — the old `decided.md` IDs, kept so existing citations across the repo resolve to this
number (`DOC-28`).
