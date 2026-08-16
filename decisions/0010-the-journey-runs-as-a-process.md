---
id: 10
scope: srnd-group-strategy
slug: the-journey-runs-as-a-process
area: motion
title: "Gateways, pathways, many hooks, many bites — and the destination is engine"
status: proposed
version: 1
revised: 2026-08-16
supersedes: []
superseded_by: null
---

# ADR 0010 — Gateways, pathways, many hooks, many bites — and the destination is engine

- **Status:** **Proposed** — 2026-08-16. **Not accepted.** Only Neil moves this to `accepted` (ADR 0001 §3).
- **Source:** `proposals.md`, consolidated. **This is a sort, not a rewrite** — the decisions below are as they
  were recorded, with their original evidence. *Nothing has been added; where the original was thin it stays
  thin.*

## Context

Most of a rep's job is pure mechanics: notice the state, choose the next right touch, make it, note the
response. Mechanics become process once the gateways have observable signals.

## Decision

**1. The journey runs as a process.** The buyer journey is defined with **gateways** between its stages;
content is generated as **pathways** that move a dealer through each gateway, start to finish and back round
the loop. The judgement residue stays human.

**2. Hooks are multiplied and categorised; every piece has a roadmap position; the funnel tracks like
e-commerce; elevation is engineered early.** G1 is a *set* of hooks per product — categorised by appeal
(**more revenue · time saved · easier to do · better results · the problem named**), placed indirectly, each
the head of a pathway with a named destination. Elevation runs product to brand to group as early as the
dealer's state allows — brand at the proposition, group at the hinge, **never at the cold open**, and
cross-sell prompts still wait for the first job.

**3. Many bites per stage — conversion is cumulative.** A single touch rarely converts, at any stage. Each
stage is worked as a repertoire of small touches at a regular rhythm, **value every time**, until the gateway
tips. Touches are judged by the pile, never per-touch; **a touch with no value in it is not a coin**;
regularity is part of the mechanism.

**4. The destination is engine.** The process ultimately runs automatically on top of the CRM and the product
database: signals observed, triggers fired, the content queue churned, outputs logged, results applied. **This
repo owes engine the state model, the content-plan and log shapes, the pathway structure and the schema's
sales layer — and specifies nothing of engine itself.**

**Ancestor evidence (2026-08-01).** The March 2023 programme had nine "bridges", explicit stage-end
definitions, and *"get each CRM company to the next bridge"*; the appeal categories appear near-verbatim in the
2023 *Purchase Events* map. **Three years old, in Neil's own hand.**

## Provenance

**Consolidates `S22`, `S23`, `S25`, `S26`** — the old `decided.md` IDs, kept so existing citations across the repo resolve to this
number (`DOC-28`).
