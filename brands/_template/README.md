# <Brand> — brand playbook (template)

Copy this folder to `brands/<brand>/` to start a new brand playbook. A playbook holds **only what is
specific to the brand**; everything structural comes from `../../group/` and must not be restated or
forked.

## What the brand takes from the group strategy (do not duplicate)

- The buyer journey (`../../group-strategy/buyer-journey.md`) — run your own version; put per-stage content
  in `content.md`.
- Commercial model, shared portal, fully-gated pricing policy (`../../group/`).
- Content production — studio + Experience Centre (`../../motion/content.md`); shared.
- Execution standards, touchpoint set, metric definitions (`../../group/`).

## Files to fill in

- `README.md` — one page: what this brand is, what it takes from the group strategy, what lives here.
- `positioning.md` — where the brand sits, its core problem/proposition, its buyer.
- `growth-levers.md` — which channels the brand prioritises (deepen vs widen).
- `content.md` — the brand's content, guardrails (from its `CLAUDE.md`), creative, layered build
  mapped to buyer-journey stages.
- `product-pricing.md` — the range and the (gated) tier numbers behind the shared gate.
- `product-records.md` — **the brand's products on the group form** (`../../registers/record-form.md`), one
  record per mechanism family rather than per SKU. The form is group; the fill is brand. Add the brand's record
  scopes to `../../registers/product-register.md` at the same time — the roster is what says a record is missing.
- `registers/open-items.md` — brand-specific decisions and sequencing.
- *(optional)* `competition-matrix.md` — where the brand outclasses competitors, dimension by
  dimension, with our column real and competitor columns filled from verified research. Useful
  wherever the differentiation is capability-led (see `brands/display-technologies/`).

## Rules

1. **Don't collapse the layers.** If something makes sense for more than one brand, it belongs in
   `group/`, not here. Propose moving it up rather than duplicating.
2. **Brand truth binds.** Carry the brand's hard don'ts into `content.md` guardrails; the group
   layer never licences overriding them.
3. **Flag, don't guess.** Unsourced buyer-truth, unvalidated channels, unset pricing tiers → into
   `registers/open-items.md`, not into copy. In a product record this is the `[?]` state, and **a named gap counts as
   progress** — a composed answer does not.
