# SRND Group — Context for Claude Code

Steering context for anyone (human or Claude) working on SRND **group-level** sales & marketing
strategy in this repo. Read this before writing. It is the group layer; each brand carries its own
brand-truth `CLAUDE.md` in `brands/<brand>/` (C-ATS's brand truth lives with the C-ATS product
repo and is summarised in `brands/c-ats/`). This file is not marketing copy.

## What SRND Group is

SRND Group **designs, manufactures and distributes the systems behind high-end environments**, from
its own factory in Kirkbymoorside, North Yorkshire. It sells **to the trade** — everything is built
to be specified, quoted and installed by professionals. The promise is *"six brands, one group, one
relationship"*: whatever mix of brands a partner uses, they deal with one team, one account, one
point of contact — transacting through the shared SRND store, with operations run in engine
(`engine.srnd.group`).

Formed **March 2023** to bring several established companies together as one group. The name is the
initials of founders **Simon Ridley and Neil Davidson**, and reads as **"surround"** — a nod to the
audio/AV work at the core.

> **Identity line is unresolved.** Neither the store's "luxury solutions for high-tech environments"
> nor the group site's "British manufacturing for high-end environments" is felt to be strong enough
> yet. Treat the description above as working context, not a settled tagline — see `registers/open-items.md`.

## The brands

Six specialist brands, each with its own site and range, covering the room system end to end:
**Display Technologies** (projection), **Fabric Walls** (stretch-fabric wall/ceiling systems),
**Light Walls** (addressable lighting), **C-ATS** (acoustic treatment — the 3 Rs), **Pro-Fi** (audio
systems), and **SRND Distribution** (the trade distribution arm). **Six is the roster — there is no seventh
line in waiting.** *("SRND Solutions" was carried here as a forthcoming sensors-and-interfaces line; retired
2026-08-16 as stale, having been named before the work that would fill it existed. The nearest real thing is
LWCP's spatial sensing, which is a layer of LWCP until it proves otherwise.)* In distribution, **Leyard** is the only genuine
third-party brand; other names on the store are carried lines or components (Ultrasuede is a fabric
used within Fabric Walls, not a standalone brand). Full roster: `group-strategy/commercial-model.md`.

## The core idea

**The dealer relationship is the asset**, counted across every brand and over years, and — done
well — compounding. A dealer won through one brand is a doorway the whole group cross-sells
through, because the brands serve the **same room**. This changes the economics of everything
here: we don't triage dealers by any single brand's order size. See `group-strategy/the-group-play.md`.

## Non-negotiable discipline

- **Coherence, not invention.** SRND's external and internal stories diverge sharply — world-class
  engineering (DT Commander, LWCP measured colour, …) behind thin public telling. The job is to make
  one true story flow group → brand → product by **surfacing what's genuinely there**, not
  manufacturing claims. The substance is real; draw it out, don't make it up. (This is the positive
  face of "flag, don't guess" — and see the README's "Why this exists".)
- **Group ≠ brand. Keep the layers clean.** Group strategy is brand-agnostic; it must not bake in
  one brand's specifics. A brand playbook applies the group strategy; it must not re-invent it.
  If you're writing something that only one brand can use, it belongs in that brand's folder.
- **Brand-truth guardrails still bind.** When group work touches a brand's content, that brand's
  own hard don'ts apply and apply hardest — there's no group licence to override brand truth.
  (For C-ATS: scattering never diffusion; panels named by problem not mechanism; no invented
  performance figures; no supplier names; no NDA install details; don't tease the commercial range;
  ~~don't hard-code the "Complete" name expansion~~ — **rule dropped 2026-08-16: the expansion is fine.**
  See `brands/c-ats/`.)
- **Check the platform before specifying anything that touches it.** Engine, the canonical dataset and the
  Cinema Platform ADRs move faster than this repo. Where a decision here depends on what they hold or have
  settled, read the current state first — this work has already based a position on a superseded ADR once, and
  a strategy artefact that duplicates or contradicts a live system is worse than no artefact.
- **Facts about the present go in `evidence/current-state.md`.** The baseline — dealers, revenue shape, lead sources,
  what assets exist — is recorded there with unknowns marked **[?]** rather than inferred. Don't fill a gap by
  reasoning about it.
- **The work ratchets; it does not spiral.** **SRND OS is the source of record for what is decided**;
  **nothing enters `decided.md` without Neil's
  explicit approval** (it is empty by instruction, 2026-08-16). New data from real work lands as **evidence**
  against a decision or an open item — it does not reopen the reasoning that produced the decision. After
  logging evidence, the next move is `NEXT.md`, not another pass through `group-strategy/`. **Prefer amending
  the plan over re-arguing the strategy.**
- **Flag, don't guess.** Buyer-truth, channel validation, pricing tiers, name expansions — where a
  fact isn't sourced from real jobs or a settled decision, leave it out and flag it in
  `registers/open-items.md`. Don't invent personas, figures, or roadmaps.
- **Build it, then say it.** Where the group has the intent but not yet the reality, the reality comes
  first and the claim waits. This has now surfaced three times independently — dealer appreciation, the
  partner programme, and the whole room being genuinely easier to buy — which makes it the group's
  characteristic failure mode rather than a coincidence. Announcing something we don't yet practise costs
  more than silence. See `group-strategy/partner-programme.md`, `group-strategy/the-group-play.md`.
- **Don't fence us to cinema — in trade.** High-end cinema is the heartland of revenue and credibility and
  should lead where it's strongest, but the group is explicitly determined not to remain a cinema-only trade
  supplier, and none of the underlying competences are cinema-specific. Name the *problem*, never the room
  type; lead with cinema credibility, never a cinema-only definition. **The reverse holds in B2C:** the
  consumer proposition stays DIY home cinema, deliberately. See `group-strategy/the-group-play.md`.

## The shared portal (settled policy)

- **Pricing is registered-partner-only — fully gated.** No public prices, and no end-user prices
  either. Public marketing claims stay qualitative (performance, depth, measured data), never
  value/price-led. This is decided, not deferred. See `group-strategy/commercial-model.md`.
- **Direct to dealer, globally, through the store.** Distributors are a deliberate case-by-case
  exception (scale or language barrier only), never the default. See `group-strategy/commercial-model.md`.

## Voice

- Confident, technical, honest, plainspoken. Problems solved, not mechanisms.
- Speaks to the trade partner (the dealer/integrator) first — they are the reader and the asset.
- No manufactured urgency, no superlatives, no unbacked claims. The content *is* the rep; a rep who
  fumbles the pitch loses a valuable dealer.
- **Never lead with our own brilliance — lead with the dealer's win.** Our technical depth is
  genuinely unmatched, but *asserting* superiority reads as arrogance (a real reputational risk in a
  niche world). Depth is expressed only as **what makes the dealer better** — depth spent on the
  customer reads as generosity; depth asserted reads as arrogance. The dealer is the hero, always.
  See `group-strategy/the-group-play.md`.
- **The Scandinavian register (group-wide voice principle).** Restraint over superlatives; substance
  carried in plain language and in owned proper nouns, not genericised adjectives. Accept being
  underestimated on first read — let the work re-rate the brand. Voice does substance; imagery does
  emotion. No superlative without a measurement behind it. Originated in Pro-Fi's voice code and
  adopted across all brands (`brands/pro-fi/positioning.md` §5). It sharpens, not replaces, the
  dealer-first rule above.
- **No superlative arms race between brands.** No brand claims to be *the* most complex, critical or
  hardest part of a project. Each element is demanding in its own terms; state it plainly. Coherence
  across the brand docs matters more than any one brand's emphasis.

## Hard don'ts

- Don't collapse the group/brand layers — no brand specifics hard-coded into group strategy.
- Don't publish pricing (partner or end-user), anywhere, ever.
- Don't name material suppliers, manufacturing partners, or OEM relationships in public content.
- Don't invent figures, test results, certifications, personas, or launch dates.
- Don't override a brand's own `CLAUDE.md` guardrails from the group layer.
