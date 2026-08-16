---
id: 14
scope: srnd-group-strategy
slug: the-product-record-schema-first
area: record
title: "A schema before documentation; engine owns the mechanical layer; definition comes first"
status: superseded
version: 1
revised: 2026-08-16
supersedes: []
superseded_by: 39
---

# ADR 0014 — A schema before documentation; engine owns the mechanical layer; definition comes first

- **Status:** **Superseded** — 2026-08-17, split into ADRs 0039–0043, one decision each, on Neil's instruction. *A bundle cannot be accepted or rejected cleanly.*
- **Source:** `proposals.md`, consolidated. **This is a sort, not a rewrite** — the decisions below are as they
  were recorded, with their original evidence. *Nothing has been added; where the original was thin it stays
  thin.*

## Context

Capturing what needs to be documented has to precede what is and will be documented — without a defined
required set per product, "the manuals are poor" is an opinion rather than a measurable gap.

## Decision

**1. A product data schema comes before any documentation work.** Without it the gap is an opinion rather
than a measurable one. **Completeness becomes a gate on new products.** *The Screen Wall — demonstrable since
ISE 2023 with no page and no datasheet — is what its absence looks like.*

**2. Engine owns the mechanical record; this repo specifies the sales and marketing layer above it.** Engine
handles SKU, name, weight, dimensions, stock and pricing because that is what an operational system is built
for; it was never designed to hold why a product sells, what doubt it must remove, who specifies it, or what we
may claim. **The deliverable is three answers per field — what data, why, and how it will be used.** A field
with no stated consumer never gets filled in.

**3. Definition comes before everything else.** You cannot state what problem a product solves until you have
stated what it is and what it does — and definition is not SKU, name and weight either. **The definitional
layer is missing in the middle:** engine holds the object, marketing holds the pitch, and nothing holds the
canonical account of what the thing is.

**4. The archive seeds the corpus; it does not close it.** Frequency data **proposes** a ranked list, and that
is all it does. The schema defines the required set, and the answers still have to be written.

**5. Website copy is generated from the product record, not written per page.** *The C-ATS Shopify site kept
its theme placeholder hero because there was no canonical source for what belongs there, and the 3 Rs vanished
from the homepage for the same reason.*

## Provenance

**Consolidates `S16`, `S16a`, `S16b`, `S17`, `S19`** — the old `decided.md` IDs, kept so existing citations across the repo resolve to this
number (`DOC-28`).
