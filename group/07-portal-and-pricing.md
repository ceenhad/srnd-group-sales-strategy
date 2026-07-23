# The portal & pricing — the shared store and the gate

The portal (the SRND B2B store) is the shared commerce back-end every brand transacts through, and
the home of the stage-4 gate. Both the store and the pricing policy are **group-owned**; brands
supply their range and tiers into it.

## Pricing policy — fully gated (settled, not deferred)

**Pricing is registered-partner-only.** The question of published pricing was fought and settled:
no public prices. Any £0.00 shown publicly is not a placeholder waiting to be filled with public
numbers — public pages carry no pricing by design, and pricing is visible only once a dealer is a
registered partner. One consequence, now deliberate rather than a limitation: public marketing
claims stay qualitative (performance, depth, measured data), never value/price-led.

**This extends to end users — no end-user pricing is shown either.** That call is made too: we lose
more than we gain by making end-user prices visible. So pricing is *fully* gated — no one sees a
price without being a registered partner, and end clients who buy direct do so by enquiry, not off a
published price.

## Current state of the portal (observed on srnd.store, 2026-07)

The live SRND B2B store already implements more of the stage-4 gate than the C-ATS plan assumed. As
observed:

- **Registration / gate exists at group level.** Brand pages carry "Apply for Trade Partner Account
  to View Partner Pricing" and "Register for SRND Store To View List Pricing." There is an Account
  Application flow, a Trade Account structure, and **B2B Finance (90-day interest-free credit)**.
- **The store is the shared back-end** the commercial model (`02-commercial-model.md`) describes —
  full multi-currency/multi-country, organised by category (Video, Audio, Cinema Construction &
  Interiors, Lighting) and by a "World Class Brands" menu. Note: that store menu still lists a
  broader set than the current group roster (see `09-brand-portfolio.md` — the group's own brands
  plus Leyard as the sole third-party line); the store list is treated as legacy until reconciled.
- **Each brand has a front-end page on the store** (e.g. `/pages/complete-acoustic-treatment-system`
  for CATS) linking to that brand's collections — the "independent brand front-ends, one store"
  model made concrete.

**So the plan's "the registration + gated-pricing flow doesn't exist yet" is out of date.** The
registration and gating *mechanism* is handled by engine (`engine.srnd.group`, a separate system —
see the README), not something this strategy has to build. What still needs pinning down is the
*policy behind it*, not the mechanism:

- registration/approval criteria and what approval grants;
- partner **pricing tiers** (the numbers) per brand — publication is settled, the tiers are not set;
- MOQs, design-tool access, CE credits, co-marketing terms.

## Open reconciliation

- Set the partner-program policy above (a decision, not a build — engine runs the mechanism).
- Any brand copy asserting a pricing posture must match the fully-gated policy. (C-ATS's
  `about.html` "recommended retail price" line is a known contradiction fixed in the C-ATS source;
  audit other brands for the same.)

> **Group vs brand.** The store and the pricing *policy* are group-owned and shared. A brand's
> *range and tier numbers* are brand-owned and live in `brands/<brand>/product-pricing.md`.
