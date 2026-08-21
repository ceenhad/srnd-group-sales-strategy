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
 **rule dropped 2026-08-16: the expansion is fine.**
 See `brands/c-ats/`.)
- **Check the platform before specifying anything that touches it.** Engine, the canonical dataset and the
 Cinema Platform ADRs move faster than this repo. Where a decision here depends on what they hold or have
 settled, read the current state first — this work has already based a position on a superseded ADR once, and
 a strategy artefact that duplicates or contradicts a live system is worse than no artefact.
- **Facts about the present go in `evidence/current-state.md`.** The baseline — dealers, revenue shape, lead sources,
 what assets exist — is recorded there with unknowns marked **[?]** rather than inferred. Don't fill a gap by
 reasoning about it.
- **The work ratchets; it does not spiral.** **A thing is decided only when it went through the question box and
 a human answered it** — Neil, 2026-08-20: *"that's it. The gate is a human verifies the decisions."* *The question, its answer in the owner's words and the date **are** the
 decision — `registers/questions.md` § Answered is the record, and **there is no second copy of it.** So a session's
 conclusion is not a decision; nor is a proposed default nobody ratified, an inference from a document, or something
 that follows obviously from a decision. **If it was not asked and answered, it stays a question.***
- **A question earns the box only if the answer is a decision the business acts on.** *Test: would anything outside
 this repo be done differently tomorrow? **If the answer only settles a wording, a filing choice, whether a row
 stands or which document something lives in, it is not a question — it is work**, and putting it to an owner spends
 the scarcest thing in the process on the cheapest problem. Measured 2026-08-20: of 61 answered questions, **22 were
 pure repo housekeeping** and about a third produced anything the business would act on. Neil: **"what this indicates
 is that your questions are shite."*** New data from real work lands as **evidence**
 against a decision or an open item — it does not reopen the reasoning that produced the decision. After
 logging evidence, the next move is `NEXT.md`, not another pass through `group-strategy/`. **Prefer amending
 the plan over re-arguing the strategy.**
- **Fix the text; do not annotate it.** *When something here is wrong, **correct it and delete the wrong
 version.** Strikethrough, *"corrected"* markers, withdrawn findings and corrections-of-corrections are **deleted,
 not kept** — a reader cannot tell a finding from a retracted one, and the noise grows faster than the work.*
 **Two things survive a correction: what an owner actually said — verbatim — and a decision with its reason.**
 *Everything else is scaffolding, and scaffolding comes down. **A register is not a diary, and nothing here is
 immutable.***
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
- **Speaks to the trade — and the trade is wider than the dealer.** Content is read by whoever it reaches:
 architect, interior designer, AV consultant, integrator. **The dealer relationship remains the asset** and the
 dealer remains the hero of the sentence; what widens is who is holding the page. **The end user is not in this
 audience** — B2C runs only through the defined Cinema Store channels. *Face to face is narrower still: the
 integrator, at a push the AV consultant.* (`registers/premises.md` `PR-17`; `brands/c-ats/claims.md`
 `C2.27`–`C2.30`, 2026-08-19. — the old line read "the reader" as exclusive, which is what `PR-17` broke.)
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
- **Criticise the category in public; name a competitor only behind the partner gate.** What competitors
 do *as a category* may be stated plainly wherever it is true — jargon-heavy, too deep, overclaiming
 "diffusion" that is really scattering. **No competitor is named on a public page**, for or against.
 **Named comparison is legitimate work and sits behind the same gate as pricing** — partner-only, and
 measured. *And the measurement test applies to what we say about others exactly as it does to what we
 say about ourselves: no unmeasured claim about a rival, gated or not.* Promoted from C-ATS's own rules
 on `registers/questions.md` Q64, 2026-08-19 — it was never a one-brand obligation.

## Hard don'ts

- Don't collapse the group/brand layers — no brand specifics hard-coded into group strategy.
- Don't publish pricing (partner or end-user), anywhere, ever.
- Don't name material suppliers, manufacturing partners, or OEM relationships in public content. *The reason is
  commercial, not stylistic, which is what makes the rule hold: where a product is a converted bought-in material,
  naming the material tells a dealer where to buy it instead. Neil, 2026-08-21 (`registers/questions.md` `Q85`):
  **"a Rev panel we sell for X is literally the same an enterprising delaer could be for Y directly from e-foam etc."**
  **A compliance certificate names the material, so it is a gated project-basis disclosure — never a download.**
- Don't invent figures, test results, certifications, personas, or launch dates.
- Don't override a brand's own `CLAUDE.md` guardrails from the group layer.
