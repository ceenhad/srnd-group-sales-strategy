# SRND Group — Sales & Marketing Strategy

This repo is the **group-level** operating home for SRND's sales & marketing. It holds the strategy
and the standards **once**, at the group level, and each brand applies them in its own playbook for
execution.

> **Start with [`NEXT.md`](NEXT.md)** — the working plan. The clear-strategy phase is complete for four
> brands and the group layer; what remains runs as a **parallel path** alongside normal business, not as a
> programme of projects. Everything else here is the reasoning behind it.

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

**The spine that story flows from is the moat** (`group-strategy/the-group-play.md`): deep technical depth joined to
a deep understanding of the dealer's job — *"we understand you, we make things to help, those things
let you be better than anyone else."*

The organising principle SRND runs on: **the group introduces, the brands focus the marketing, the
store sells.** `srnd.group` opens the funnel and introduces the company (the start of a series of
landing pages); the brands are how the sales & marketing is focused, each with its own fairly
functional site; and every brand's purchase routes back to one shared store (`srnd.store`, the
online face of distribution). Operations run in engine. (Web architecture:
`group-strategy/commercial-model.md`.) This repo is where the shared half — the strategy, the buyer journey,
the commercial model, the owned content operation — is developed. Brand folders are where it filters
down to execution.

## How to read this repo — six functional areas

*Restructured 2026-08-17. **The folder says what kind of thing a file is**, which determines how it is read,
how fast it goes stale, and what may be written in it. Numbering is gone: it implied a reading order that did
not exist.*

| Area | Holds | Behaves like |
|---|---|---|
| **`group-strategy/`** | the group play, commercial model, buyer journey, partner programme, channels, competitors | **Argument.** Slow-changing, argued once |
| **`motion/`** | sales motion, motion design, content, tools, tasks, work items, task shapes, standards, adjacency map | **The machinery of selling.** Changes when the design changes |
| **`brands/`** | six brands, each applying the above | **Application.** Inherits, never forks |
| **`registers/`** | the record schema and form, product register, backlog, questions, open items, proposals | **State, not prose.** Rows with a status |
| **`evidence/`** | archive findings, engine audit, current state, closed runs | **Measured. Append-only, and it never argues** |
| **`operations/`** | engine handoff, store worklist | **What leaves this repo** |
| **`decisions/`** | ADRs and their generated catalogue | **What is decided, and by whom** |
| **`data/`** | the sales history itself | Source, extracts, loaders. Sensitive |

**Start with [`method.md`](method.md)** for how the work is done, then `group-strategy/the-group-play.md` for
why. *`NEXT.md` is the plan of record but is marked as needing its own session — read it as the plan that was.*

**Two rules hold the shape:**

- **One kind per file.** Evidence may not argue; registers may not narrate; strategy holds no work items.
- **An ADR belongs to one area and is written when a decision is made in it** — never scraped out of a pile
  afterwards (`decisions/0001`).

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

## Status — plan rev 1

**Rev 1 is the marker in the sand, set 2026-08-04.** It is the first point at which the whole chain holds
together in one set: the strategy, the four jobs a rep does, the 46 tasks beneath them, the 168 work items
beneath those, and the product record every one of them reads from. The visual summary of rev 1 is
`product-model-visual.html`.

What rev 1 does *not* mean is that the contents are verified. Most of the task and work-item rows are claims
assembled from these documents rather than from watching the work happen, and they say so where they stand.
Rev 1 is the shape being fixed, not the facts. **From here the plan is amended, not re-argued** — evidence
lands against a decision or an open item, and a decision changes only as a dated reversal in `decided.md`.

What rev 1 produced that the repo did not have before is an **order**, in `NEXT.md`: ask engine, fill the
record, open the routes, build the primitives.

**Step 0 — the QA session — has run.** Completed 2026-08-08 (`evidence/2026-08-08-tasks-qa-run.md`): all four passes
over the 46 tasks, no task struck, and the reading produced the forward chain *fill the record → write the
shape → skip what already works* (`NEXT.md` § "What the QA produced"). The work-item register was resolved by
block; the backlog prune the QA directed was executed 2026-08-14.

This is a build, not an optimisation. The strategy is substantially worked out; the operations to
run it (partner registration and gated pricing, content production against the buyer journey,
per-brand playbooks beyond C-ATS) are partially built and partially still to build, and are headed
for engine. See `registers/open-items.md`.
