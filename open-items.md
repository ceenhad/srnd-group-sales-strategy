# Group — open items & sequencing

Group-level decisions and build order. Brand-specific open items live in each
`brands/<brand>/open-items.md`.

## Decisions needed (flag, don't guess)

- **Partner program definition** — the stage-4 policy, shared across brands. The registration and
  gating *mechanism* is handled by engine (already live); the open work is the program *behind* it:
  approval criteria, what registration grants, tier structure, MOQs, design-tool access, CE credits,
  co-marketing. This is a policy decision, not a build.
- **Cross-brand contact-cadence coordination** — the oversaturation risk
  (`group/02-commercial-model.md`); a group-level discipline with no brand home.
- **Which brands beyond C-ATS get a playbook next**, and in what order.
- **Whether reusable patterns move up to group templates** — the growth-lever idea
  (`brands/c-ats/growth-levers.md`) and the layered content build
  (`brands/c-ats/content.md`) are candidates.

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
