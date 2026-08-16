---
id: 40
scope: srnd-group-strategy
slug: engine-owns-the-mechanical-record
area: record
title: "Engine owns the mechanical record; this repo specifies the layer above it"
status: proposed
version: 1
revised: 2026-08-17
supersedes: []
superseded_by: null
---

# ADR 0040 — Engine owns the mechanical record; this repo specifies the layer above it

- **Status:** **Proposed** — 2026-08-17. **Not accepted.** Only Neil moves this to `accepted` (ADR 0001 §3).
- **Source:** `proposals.md` via ADR 0014, split to one decision per ADR.

## Decision

**Engine owns SKU, name, weight, dimensions, stock and pricing** because that is what an operational system is built for. It was never designed to hold why a product sells, what doubt it must remove, who specifies it, or what we may claim. **The deliverable is three answers per field — what data, why, and how it will be used.** A field with no stated consumer never gets filled in.

## Provenance

**Was `S16a`**, then part of ADR 0014 before the split.
