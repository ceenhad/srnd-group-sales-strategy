# SRND Group — Sales & Marketing Strategy

This repo is the **group-level** operating home for SRND's sales & marketing. It holds the
strategy and the mechanics **once**, at the group level, and each brand inherits them as an
instance for execution.

The organising principle SRND runs on: **awareness is per-brand, buying is shared.** Each brand
builds awareness independently through its own front-end; every brand transacts through one shared
store (the SRND B2B portal). This repo is where the shared half — the strategy, the buyer-journey
mechanics, the commercial model, the owned production assets — is developed. Brand folders are
where it filters down to execution.

## How to read this repo

1. **`group/`** — the master strategy and reusable mechanics. Brand-agnostic. This is the source
   of truth; brands inherit from it, they do not fork it.
2. **`brands/<brand>/`** — how one brand *instantiates* the group templates: its positioning, which
   channels it points the engine at, its content spine, its range. C-ATS is the first instance.
3. **`brands/_template/`** — the blank instance a new brand is stamped from.

## The group → brand contract

- **Group owns:** the dealer-as-asset thesis, the commercial model (one store, direct-global,
  distributor exceptions, cross-brand cadence), the buyer-journey *wheel* (as a template), the
  touchpoint set, the "done well" mechanics checklist, the production engine (studio + Experience
  Centre), the metric definitions, and the pricing-gate **policy**.
- **Brand owns:** its positioning and proof, which growth levers/channels it attacks, its content
  spine and creative, its product range and pricing tiers, its channel-specific open items.
- **The test for where something lives:** if it only makes sense across brands or over the whole
  dealer base (cross-sell, cadence coordination, the shared portal, the shared studio), it's
  **group**. If it's the specific problem one brand solves and the proof it offers, it's **brand**.

## Provenance

The group layer here is lifted from the C-ATS sales & marketing plan
(`ceenhad/c-ats-shopify:SALES-AND-MARKETING-PLAN.md`), which was written C-ATS-first but repeatedly
described itself as "C-ATS's instance of a process meant to run in parallel across every SRND
brand." This repo makes that structure real: the group parts move up here; the C-ATS-specific parts
become `brands/c-ats/`.

## Status

Build, not optimisation. The strategy is substantially worked out; the machinery to run it
(portal registration/gated pricing, content production against the wheel, per-brand instances
beyond C-ATS) is partially built and partially still to build. See `open-items.md`.
