---
id: 5
scope: srnd-group-strategy
slug: the-two-stores-and-the-carried-roster
area: commercial
title: "Two stores split by the self-evidence test; we carry nothing that competes with our own brands"
status: proposed
version: 1
revised: 2026-08-16
supersedes: []
superseded_by: null
---

# ADR 0005 — Two stores split by the self-evidence test; we carry nothing that competes with our own brands

- **Status:** **Proposed** — 2026-08-16. **Neil: accept with rewording, 2026-08-16** — the specific wording is not yet given, so this stays `proposed` until it is (`questions.md` Q43).
- **Source:** `proposals.md`, consolidated. **This is a sort, not a rewrite** — the decisions below are as they
  were recorded, with their original evidence. *Nothing has been added; where the original was thin it stays
  thin.*

## Context

One shared store is the group's buying model; a second, consumer-facing store exists for DIY. What goes
where needed a rule rather than a habit.

## Decision

**1. Two stores, split by the self-evidence test.** If a buyer already knows what it is, Cinema Store; if it
must be explained, specified or commissioned, `srnd.store`. **No product exists in both.** *(AVshop.no as the
DIY reference.)*

**2. Carried lines are Leyard, MadVR (as a Leyard accessory) and Advatek.** **Nothing that competes with our
own brands.**

**3. SRND Distribution is the sales arm for our own brands**, not an attempt to become a multi-brand
distributor.

### Known conflict, unresolved

**Engine shows 13 DT product codes published on both the `dt` store and `srnd_store`** (`engine-audit.md`).
Neil, 2026-08-16 (`questions.md` Q27): *"This is an ongoing improvement that needs to be made. Part of strategy
planning."* **So decision 1's "no product exists in both" is not the current state** — the store architecture
is unfinished work rather than a rule being breached.

## Provenance

**Consolidates `C2`, `C5`, `C6`** — the old `decided.md` IDs, kept so existing citations across the repo resolve to this
number (`DOC-28`).
