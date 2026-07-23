# SRND Group — Sales & Marketing Strategy

This repo is the **group-level** operating home for SRND's sales & marketing. It holds the strategy
and the standards **once**, at the group level, and each brand applies them in its own playbook for
execution.

The organising principle SRND runs on: **awareness is per-brand, buying is shared.** Each brand
builds awareness independently through its own front-end; every brand transacts through one shared
store (the SRND B2B portal). This repo is where the shared half — the strategy, the buyer journey,
the commercial model, the owned content operation — is developed. Brand folders are where it filters
down to execution.

## How to read this repo

1. **`group/`** — the group strategy and standards. Brand-agnostic. This is the source of truth;
   brands apply it, they do not fork it.
2. **`brands/<brand>/`** — each brand's playbook: how it applies the group strategy — its
   positioning, which channels it prioritises, its content, its range. C-ATS is the first.
3. **`brands/_template/`** — the starting point for a new brand playbook.

## Group vs brand responsibilities

- **Group owns:** the dealer-as-asset thesis, the commercial model (one store, direct-global,
  distributor exceptions, cross-brand contact cadence), the buyer journey, the touchpoint set, the
  execution standards, the content operation (studio + Experience Centre), the metric definitions,
  and the pricing policy.
- **Brand owns:** its positioning and proof, which growth priorities/channels it pursues, its
  content and creative, its product range and pricing tiers, its channel-specific open items.
- **The test for where something lives:** if it only makes sense across brands or over the whole
  dealer base (cross-sell, contact-cadence coordination, the shared portal, the shared studio), it's
  **group**. If it's the specific problem one brand solves and the proof it offers, it's **brand**.

## Provenance

The group layer here is drawn from the C-ATS sales & marketing plan
(`ceenhad/c-ats-shopify:SALES-AND-MARKETING-PLAN.md`), which was written C-ATS-first but repeatedly
described itself as C-ATS's version of a process meant to run in parallel across every SRND brand.
This repo makes that structure real: the group parts move up here; the C-ATS-specific parts become
the C-ATS playbook in `brands/c-ats/`.

## Status

This is a build, not an optimisation. The strategy is substantially worked out; the operations to
run it (portal registration and gated pricing, content production against the buyer journey,
per-brand playbooks beyond C-ATS) are partially built and partially still to build. See
`open-items.md`.
