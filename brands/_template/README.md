# <Brand> — brand instance (template)

Copy this folder to `brands/<brand>/` to stand up a new brand instance. A brand instance holds
**only what is specific to the brand**; everything structural is inherited from `../../group/` and
must not be restated or forked.

## What the brand inherits (do not duplicate)

- The wheel (`../../group/03-the-wheel.md`) — run your own instance; put per-stage content in
  `content.md`.
- Commercial model, shared portal, fully-gated pricing policy (`../../group/`).
- Production engine — studio + Experience Centre (`../../group/06-production-engine.md`); shared.
- Mechanics checklist, touchpoint set, metric definitions (`../../group/`).

## Files to fill in

- `README.md` — one page: what this brand is, what it inherits, what lives here.
- `positioning.md` — where the brand sits, its core problem/proposition, its buyer.
- `growth-levers.md` — which channels the brand points the shared engine at (deepen vs widen).
- `content.md` — the brand's content spine, guardrails (from its `CLAUDE.md`), creative, layered
  build mapped to wheel stages.
- `product-pricing.md` — the range and the (gated) tier numbers behind the shared gate.
- `open-items.md` — brand-specific decisions and sequencing.

## Rules

1. **Don't collapse the layers.** If something makes sense for more than one brand, it belongs in
   `group/`, not here. Propose the lift rather than duplicating.
2. **Brand truth binds.** Carry the brand's hard don'ts into `content.md` guardrails; the group
   layer never licences overriding them.
3. **Flag, don't guess.** Unsourced buyer-truth, unvalidated channels, unset pricing tiers → into
   `open-items.md`, not into copy.
