---
id: 34
scope: srnd-group-strategy
slug: the-destination-is-engine
area: motion
title: "The destination is engine, and this repo specifies none of it"
status: proposed
version: 1
revised: 2026-08-17
supersedes: []
superseded_by: null
---

# ADR 0034 — The destination is engine, and this repo specifies none of it

- **Status:** **Proposed** — 2026-08-17. **Not accepted.** Only Neil moves this to `accepted` (ADR 0001 §3).
- **Source:** `proposals.md` via ADR 0010, split to one decision per ADR.

## Decision

**The process ultimately runs automatically on top of the CRM and the product database in engine**: signals observed, triggers fired, the content queue churned, outputs logged, results applied. **This repo owes engine the state model, the content-plan and log shapes, the pathway structure and the schema's sales layer — and specifies nothing of engine itself.**

## Provenance

**Was `S25`**, then part of ADR 0010 before the split.
