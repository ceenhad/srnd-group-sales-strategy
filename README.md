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

**The spine that story flows from is the moat** (`group/00-strategy.md`): deep technical depth joined to
a deep understanding of the dealer's job — *"we understand you, we make things to help, those things
let you be better than anyone else."*

The organising principle SRND runs on: **the group introduces, the brands focus the marketing, the
store sells.** `srnd.group` opens the funnel and introduces the company (the start of a series of
landing pages); the brands are how the sales & marketing is focused, each with its own fairly
functional site; and every brand's purchase routes back to one shared store (`srnd.store`, the
online face of distribution). Operations run in engine. (Web architecture:
`group/01-commercial-model.md`.) This repo is where the shared half — the strategy, the buyer journey,
the commercial model, the owned content operation — is developed. Brand folders are where it filters
down to execution.

## How to read this repo

Start with **[`NEXT.md`](NEXT.md)** for what to do, then `group/00-strategy.md` for why.

1. **`group/`** — the group strategy and standards, in ten documents. Brand-agnostic, and the source of
   truth; brands apply it, they do not fork it.
   - `00-strategy.md` — the spine: dealer-as-asset, the moat, the whole room, beyond cinema, the standing
     disciplines. Read this one if you read nothing else.
   - `01-commercial-model.md` — brands, properties, gated pricing, the two stores, carried lines.
   - `02-buyer-journey.md` — the journey, the on-ramp, touchpoints, execution standards, metrics.
   - `03-partner-programme.md` — what registration grants and how partners are valued.
   - `04-content.md` — the owned assets, the rep with a face, placement rules, the campaign template.
   - `05-channels.md` · `06-competitors.md` — the named landscape, and what rivals do well.
   - `07-tools.md` — where calculators and design tools fit commercially.
   - `08-sales-motion.md` — how a sale is made with no salesforce: what content takes, what substitutes for
     the rest, and why it compounds and scales.
   - `09-motion-design.md` — how a sale gets made, journey-first: the six stages mapped to what serves each
     one; the **gateways** between stages with their observable signals; the **content pathways** that move a
     dealer gateway to gateway and back round the loop (`decided.md` S22); then the five pieces of machinery
     designed once as the group standard the brands inherit — with the decisions that remain marked, not
     guessed.
   - `store-split-worklist.md` — a working execution list, not strategy.
2. **`brands/<brand>/`** — each brand's playbook. Four are settled (C-ATS, Fabric Walls, Display
   Technologies, Pro-Fi), each in its own `positioning.md`; Light Walls is deliberately deferred.
3. **`brands/_template/`** — the starting point for a new brand playbook.
4. **The product layer**, in three files that do different jobs and should not be merged:
   - `product-data-schema.md` — **the argument.** What data the sales and marketing layer needs, why, and how it
     will be used. Engine holds the mechanical record; this is the layer above it.
   - `product-record-template.md` — **the form.** The same fields with stable IDs, fill states and completeness
     rules, plus the **generation gates**: which fields each piece of content or campaign material needs before it
     can be produced. What makes a record fillable by anyone and countable by anybody. **Group 04 is the knowledge
     layer** — the answers, the sizing rule, the comparison, the timing, what the dealer tells their client. Since
     content is the sales rep and the records are step 1 of the production line, **that group is the database the
     rep speaks from**, and it is the half that decides whether any of the rest is worth filling.
   - `product-register.md` — **the roster.** Every product in the group as a record scope, with its record state
     and marketing status. Says which record to open next, and which live products have no canonical account at all.
   - Filled records live with the brand — `brands/c-ats/product-records.md` (the worked standard) and
     `brands/display-technologies/product-records.md` (a skeleton, where the counted gaps are the deliverable).
5. **`current-state.md`** — the factual baseline: the sales side as it runs today and the marketing assets that
   exist, with gaps marked rather than guessed.
6. **`decided.md`** — the ratchet: what is settled, the evidence behind it, and closed to re-argument.
7. **`open-items.md`** — decisions still outstanding.
8. **`backlog.md`** — the action register: every discrete action in the repo extracted into one working
   surface (do / decide / fetch, with owners, effort and status), each workstream tagged by the motion
   component it develops (`group/09-motion-design.md`), prerequisite, or independent. `NEXT.md` holds the
   reasoning; this holds the trackable work. Deliberately no dates and no weeks.

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
