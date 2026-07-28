# Group — open items & sequencing

Group-level decisions and build order. Brand-specific open items live in each
`brands/<brand>/open-items.md`.

## Decisions needed (flag, don't guess)

- **Group identity line / positioning statement** — unresolved, but now anchored. Both current lines
  are weak (the store's "luxury solutions for high-tech environments"; the group site's "British
  manufacturing for high-end environments"). It should **derive from the moat** (`group/14-moat.md`):
  technical depth + understanding of the dealer's job → "we understand you, we make things to help,
  those things make you better than anyone." Draft against that spine; don't hard-code a tagline
  until settled.
- **Show dealers we value them (currently a total gap).** The relationship is entirely one-way
  today: dealers pay, and nothing goes back to signal the relationship itself is valued. This
  undercuts the moat and the dealer-as-asset thesis. Build real mechanisms that show dealers they're
  valued —
  recognition, reciprocity, loyalty, partner-not-wallet — most naturally at buyer-journey stage 6.
  Per coherence-not-invention: don't *claim* appreciation until it's real; build it, then say it.
  See `group/14-moat.md`.
- **Leyard — entirely uncovered, and possibly an on-ramp asset.** The group's only genuine third-party
  distributed line (`group/09-brand-portfolio.md`) has had no strategy work at all. It matters more than
  its "carried line" status suggests: per `group/17-on-ramp.md`, entry is governed by how much trust a
  first purchase requires, and an established outside brand asks the least trust of anything we sell — a
  dealer can try SRND without betting on SRND's own engineering. Decide Leyard's role (on-ramp door, LED
  credibility, margin line) and whether it needs its own material.
- **Entry products, per brand** — the low-risk, easy-to-specify item a stranger buys to try us, distinct
  from each brand's flagship (`group/17-on-ramp.md`). Some are obvious (DT's smaller enclosures and port
  holes, Pro-Fi's shipping Spatial cabinets); others need deciding, including whether a small Fabric Walls
  element can serve as one. Fulfilment on these must be exemplary — the first order tests us, not the
  product.
- **SRND Solutions go-to-market** — the forthcoming own-made sensors/interfaces line
  (`group/09-brand-portfolio.md`) deliberately doesn't fit inside a brand, yet the model makes
  brands the marketing surface. Decide how it reaches the trade: its own brand/playbook, or a
  cross-brand group line attached to installs. Also its launch timing (don't market before it ships).
- **Store roster vs group reality** — `srnd.store`'s "World Class Brands" menu lists more than the
  current group roster (six own brands + Leyard as the only third-party line). Reconcile the store
  to reality (or confirm what's genuinely still carried) so public listings match the group truth.
- **C-ATS naming** — the group site uses "C-ATS" and spells out "Complete Acoustic Treatment System"
  openly, but the C-ATS brand-truth `CLAUDE.md` still flags the "Complete" expansion as unresolved
  and prefers "C-ATS"/"Cinema". Resolve the canonical name and align brand truth, the group site and
  the store. Affects all C-ATS-facing copy.
- **Partner program definition** — the stage-4 policy, shared across brands. The registration and
  gating *mechanism* is handled by engine (already live); the open work is the program *behind* it:
  approval criteria, what registration grants, tier structure, MOQs, design-tool access, CE credits,
  co-marketing. This is a policy decision, not a build.
- **Channel selection, priority & spend** — from the candidate landscape (`group/12-channels.md`),
  decide which channels SRND actually promotes through, at what priority and budget, and who owns
  each. Verify current status/membership (names and events change). A decision, not a list.
  Evaluate each channel online-first, EI-style (`group/12-channels.md`).
- **Activate the EI microsite (quick win)** — `essentialinstall.com/srnd/` is paid for and
  running near-empty. Feed it regularly (company pages + virtual case studies linking to the brand
  sites) and push through EI news/newsletter/podcast. Low cost, already sunk; just needs using.
- **Cross-brand contact-cadence coordination** — the oversaturation risk
  (`group/02-commercial-model.md`); a group-level discipline with no brand home.
- **Which brands beyond C-ATS get a playbook next**, and in what order (Fabric Walls, Display
  Technologies, Light Walls, Pro-Fi).
- **Whether reusable patterns move up to group templates** — the growth-lever idea
  (`brands/c-ats/growth-levers.md`) is a candidate. (The layered content build has been moved up —
  see `group/11-intro-campaign.md`.)

## Suggested sequencing (dependency order; a proposal, not a decision)

1. **Define the partner program** — approval criteria, what registration grants, tier structure,
   MOQs, tool access. The registration/gating *mechanism* already runs in engine; this is the policy
   behind it. Cheap, unblocks everything downstream.
2. **Per-brand: consolidate dealer lists + set pricing tiers** — brand work, unblocks lever-1
   targeting and the gated pricing.
3. **Content production against the buyer journey via the studio** — buildable now; the bulk of the
   work. Doesn't wait on the decisions above.
4. **Public-safe reference/proof assets (stage 5)** per brand, built from real jobs without naming
   NDA installs.
5. **Cross-brand cadence coordination** — stand up the group-level discipline once more than one
   brand is running direct actions in parallel.
6. **Paid outlet spend** — last, once the above give something worth promoting and validated
   audiences.

**Note — operations live in engine.** `engine.srnd.group` already runs the operational side
(registrations, pricing, jobs), and the settled process ultimately runs there. This repo keeps the
strategy clear enough to hand off, but doesn't specify engine — it's a separate system, out of scope
here.

## Launch

Each brand's public front-end launch is its own gating step, best taken once that brand's
stage-1→4 operations (content + the shared registration/pricing gate) exist — so the first real
visitors meet a working buyer journey rather than a shopfront that can't take an order.

## Provenance / migration status

- Group layer drawn from `ceenhad/c-ats-shopify:SALES-AND-MARKETING-PLAN.md` (2026-07). That file
  remains the C-ATS site repo's record; this repo is now the source of truth for the group strategy
  and the C-ATS strategy playbook. The C-ATS *site/theme* work stays in the C-ATS repo.
- Portal current-state observations (`group/07-portal-and-pricing.md`) captured from the live
  srnd.store, 2026-07 — supersede the plan's "flow doesn't exist yet" at the group level.
