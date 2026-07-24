# SRND Group — Sales & Marketing Strategy

This repo is the **group-level** operating home for SRND's sales & marketing. It holds the strategy
and the standards **once**, at the group level, and each brand applies them in its own playbook for
execution.

## Why this exists — the core problem

SRND's **external and internal stories are wildly divergent.** The engineering is world-class — the
DT Commander control platform, LWCP's measured-per-unit colour moat, Fabric Walls' productised
system — but the public telling of it is thin to absent (commodity-looking webshops, ~85 LinkedIn
followers, little to no video). The team has been busy building the drum, not banging it.

So the job here is **coherence, not invention.** The material is real and already exists; the work
is to make one true story flow **group → brand → product**, drawing out what's genuinely there —
not manufacturing claims. Capturing the real internal substance (from the product/platform repos)
brand by brand, *before* writing messaging or touching websites, is what makes that possible.

Note the corollary: even the brands with *more* built externally (C-ATS, Fabric Walls) were put up
ad-hoc, with no plan followed beyond "have more than nothing." So the existing sites are
**placeholders to re-base on the plan, not strategy to preserve** — this is the first real plan, not
a tidy-up of an existing one.

The organising principle SRND runs on: **the group introduces, the brands focus the marketing, the
store sells.** `srnd.group` opens the funnel and introduces the company (the start of a series of
landing pages); the brands are how the sales & marketing is focused, each with its own fairly
functional site; and every brand's purchase routes back to one shared store (`srnd.store`, the
online face of distribution). Operations run in engine. (Web architecture:
`group/09-brand-portfolio.md`.) This repo is where the shared half — the strategy, the buyer journey,
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

## Relationship to engine.srnd.group

`engine.srnd.group` is SRND's internal operations platform — a **separate system, not maintained
from this repo**. It has replaced the old third-party tooling (Monday.com and others) and already
runs the operational side of the business: partner registrations, pricing, jobs — a big jump in
efficiency.

Keep the two apart. This repo owns the **strategy and mechanics** (the buyer journey, execution
standards, commercial model, partner/pricing policy). Engine owns **operations** and is the system
of record for anything operational the strategy relies on. The long-term goal is for the settled
process to run in engine, but **we don't document or specify engine here** — we only note where the
strategy hands off to it.

## Status

This is a build, not an optimisation. The strategy is substantially worked out; the operations to
run it (partner registration and gated pricing, content production against the buyer journey,
per-brand playbooks beyond C-ATS) are partially built and partially still to build, and are headed
for engine. See `open-items.md`.
