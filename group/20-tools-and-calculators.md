# Tools and calculators

*Where calculators fit commercially, and the rule for what may be published where. Internal.*

*The Cinema Platform repo (`ceenhad/cinema-platform`) is authoritative for what the tools are and how
they're built. This document is the **group commercial** position — which is a wider frame than the tool
product's own monetisation model, because we are a manufacturer and the tools exist to pull product
through. It references the platform's decisions rather than restating them. Grounded in Cinema Tools **ADR 017** (commercial-first, engine depth as IP, report as the
monetised deliverable), **ADR 019** (C-ATS partner tool placement and brand framing), **ADR 036** (engines
are cloud-hosted; the local installable is retired) and **ADR 040** (operator surfaces over the design
spine). An earlier draft of this document leaned on ADR 014's three-level tiering; 017 and 036 retired
its substance, so it should not be used as a basis for commercial choices.*

## Calculators are central, not a risk

Calculators are the single most important driver of engagement and time saving we have. They answer a real
question instantly, they demonstrate competence rather than asserting it, and — used properly — they
capture a lead while doing it. The strategy should be biased *toward* building them.

An earlier version of the C-ATS strategy said "no public calculators" on the grounds that a calculator
commoditises chargeable design. That reasoning was wrong and is withdrawn.

## What we are, and what we are not

Two questions have to be answered before any tool decision makes sense, and the answer to both is no:

- **Are we an online services company?** No.
- **Are we a paid design-tool vendor?** No.

**We are a manufacturer.** Tools help us sell services and make money — that much is plainly true — but
the service is not where it stops. A design specifies a room, and we make most of what goes into it.

That distinction is the whole strategic point. For Kolosseum, Cinema Room Setup or DARDT, the tool *is*
the business, so the tool has to pay for itself. For us the tool leads to a specification, and the
specification leads to product supply across every brand in the room. **The ladder doesn't end at the
report; it ends at the room being supplied.**

Two consequences follow, and they are advantages competitors without factories cannot copy:

- **We can afford to be more generous with tooling** — and to invest more in the engine — than a tools
  company ever could, because the payback is downstream rather than in the tool's own P&L. Judging a tool
  on what it bills would get the answer wrong.
- **Engine depth pays twice** — once as a better deliverable, and once because a dealer who trusts our
  design work is a dealer we have a real relationship with.

### But do not build the tool around our own products

This is the tempting mistake, and it is a bad one. Push "pull-through" into the tool and the absurdity
arrives immediately: would we only design rooms around Pro-Fi, and turn down every C-ATS design
opportunity on a room using someone else's speakers? Refuse a project because the ceiling mount isn't
ours? Obviously not. Most rooms will always contain other people's equipment, and design work on those
rooms is good business we want.

So there is no "specification share" target and no quiet weighting of the catalogue. **The tool's job is
to be the best help available for whatever room is actually in front of the dealer.** Being present in
the catalogue and easy to specify is right and sufficient; designing around ourselves is not.

What the tool genuinely gives us is different, and better: **it tells us a project exists and what it
needs.** That is the raw material for a relevant, timely conversation — a 5 m cinema being built next
quarter, a room with a resonance problem, a dealer who has never bought treatment. Turning that into
revenue across the room is **relationship and campaign work**, not something engineered into software.

Which exposes the real weak link — see below.

### The platform's monetisation model sits inside this, not above it

Cinema Tools ADR 017 makes the monetised deliverable **the report** rather than tool access — residential
design subscription retired, engine depth (**Tessellate**) as the IP, speed-to-report as the value
proposition. The platform's own phrasing is the cleanest statement of it: **"the deliverable is the
recipe, not the recipe-finder."**

That is correct as the *tool product's* commercial model, and it is why free calculators cannot
cannibalise paid design — what's sold is a deliverable carrying accountability: measured data, judgement,
and a result somebody stands behind and can verify. Arithmetic was never the product.

But at group level the report is a **stage**, not the destination. Keep both in view, or the tooling gets
optimised as a standalone business and the product pull-through it exists to create gets forgotten.

A useful discipline travels with it: **UI polish is a qualifier, not the IP.** It must not embarrass the
engine, but it isn't where we compete. That is the same instinct as the group's voice — substance over
surface.

### Two honesty disciplines

**Assume the competition is good.** ADR 017's context reads a little dismissively of Kolosseum and Cinema
Room Setup ("without engine depth"). Both are very probably excellent, built by knowledgeable people —
there are plenty of those in this industry besides us. We have already made the opposite mistake in this
work, trusting a competitor's marketing over their real capability; assuming a competitor lacks depth is
the same failure inverted. Assess honestly in both directions.

**Brand-agnostic, and meant it.** The engines are deliberately brand-agnostic — any loudspeaker library,
any projector catalogue. That isn't a concession to be minimised; it is what makes the tools worth using
and what makes replacing DARDT possible. Pro-Fi's own principle states the posture: *informs, never
blocks; the customer decides*, and sell more only when it genuinely helps. A tool caught favouring us
would destroy the trust that makes it valuable in the first place — and would cost us the design work on
every room that isn't all-SRND, which is most of them.

## The real failure mode is implication, not disclosure

The genuine objection is narrower and more important than commoditisation. A C-ATS calculator hosted on
the C-ATS website can never replace a £5,000 design service — but **its mere presence implies that it
might.** The damage is done by placement and framing, not by giving anything away.

That gives a three-part test for any tool, drawn from tools we already run:

1. **Can it completely answer the question it poses?** DT Create can — ideal screen size, then draw the
   screen. A reflection-point calculator can — the geometry is the whole answer. "How much treatment does
   my room need" cannot, honestly, in a web form.
2. **Does it imply it answers a bigger question than it does?** This is the C-ATS failure mode. A tool
   must be visibly bounded, so nobody mistakes sizing for design.
3. **Does it close its own loop?** Real value to the user, a lead or data to us, and **no hidden manual
   work.** DT Create is the cautionary detail: it captures the lead well, but asking the user to *request*
   the CAD means someone then spends twenty minutes generating and emailing it. Automating that — already
   in hand — is what turns a good calculator into a good business process. Un-automated, a popular tool is
   a tax on our own people.

## Cinema Tools is the master brand for design tooling

Per ADR 019, **Cinema Tools is the master brand across the entire design surface**, and
`cinema-tools.com` is the lead-magnet front door. This is a stronger arrangement than hosting tools under
brand names, and it is what resolves the implication problem structurally:

- **Free calculators live on cinema-tools.com** and exist for discovery, SEO and authority.
- **The C-ATS partner tool inherits the Cinema Tools brand** rather than being a C-ATS-branded tool. Its
  outputs carry **"Powered By Cinema Tools"** bylines, so a partner and an end-user see one brand across
  the whole free → partner-engagement lifecycle.
- **"Cinema Tools Online" is not used externally** — it was internal framing tied to the retired
  subscription product.

So a capable tool never sits *on* a brand site implying that brand's paid service is unnecessary. The
design surface is Cinema Tools throughout; the brands sell products, services and accountability.

Two consequences worth recognising as group assets already built rather than planned:

- **Lead capture is the on-ramp hinge in product form.** Free calculators offer lead capture on PDF
  download, landing in the **SRND Engine `leads` table** (ADR 020 — Monday retired). A useful PDF traded
  for contact details is exactly the registration-and-permission moment (`17-on-ramp.md`), won willingly
  rather than extracted.
- **Each calculator is a discrete SEO landing page** targeting specific queries — the GEO/AEO strategy
  implemented, not aspired to.

## The ladder, and where it actually ends

ADR 017 sets out how design revenue arrives, and it is a ladder rather than a product:

free calculators (discovery and authority) → **partner-gated C-ATS reporting tool** (the residential
revenue route through the partner channel) → **Pro Design escalation at £500, invoiced per engagement**
→ partner-network escalation → brand-partnered recipe packs (Pro-Fi is the proof) → the full C-ATS design
service and verification where a project warrants it — **→ and then the products that build the room.**

That last rung is the one the tool docs can't see from where they sit, and it is the largest. Every rung
before it earns real money and builds real trust; none of them is the destination.

But note *how* the ladder is climbed. Product supply follows because a dealer trusts us, knows what we
make, and was given something relevant at the right moment — not because a tool steered them. The step
from "design delivered" to "room supplied" is earned, and it is the step we are currently weakest at.

No subscription billing: partner access is gated by SRND-managed credentials. **Which means tool access
as a partner benefit is already the operating model**, not a proposal — and it is precisely the currency
the partner programme runs on: spend the depth, not the margin (`18-partner-programme.md`).

## C-ATS specifically

- **The partner tool question is decided, not open.** Under ADR 019 the C-ATS tool is the closed-network
  residential variant of the thin web entry surface: partner-gated, residential cinema and music rooms
  only, C-ATS panel catalogue locked, residential report template fixed, and **methodology black-boxed —
  partners see results, not internals.** Scope is an endorsed 11-module list running from project model
  and room-data entry through multi-sub optimisation and treatment placement to the RP22 scorecard,
  report and drawing rendering, Pro Design workflow and an end-user request form.
- **No design-replacing calculator on the C-ATS site** — because of what its presence would imply, not
  what it would reveal.
- **Do publish worked examples showing how quantities are derived.** Method transparency without
  suggesting the room can be solved by a form.
- **A reflection-point calculator is a good candidate** and passes all three tests: it is *geometry, not
  acoustic design*. It answers "where do first reflections land" completely and honestly, and doesn't
  pretend to answer "will this room perform" — which is what the design service and verification own. A
  placement tool, not a design tool. It is also the notable gap in the current calculator set, sitting
  directly on the first of the 3 Rs.
- **Honesty flag:** the Room Resonances calculator is live, and the resonance-sizing method has a known
  low-frequency blind spot (`../brands/c-ats/measured-acoustics.md`). Of all the tools this is the one
  whose limits must be stated plainly. C-ATS exists because competitors promised physics they couldn't
  deliver; a tool that oversimplified would be that same sin committed by us.

## The consumer channel

For DIY buyers on `cinema-store.com` there is no chargeable design to protect, so configurators and
estimators are pure asset. **No-calculators was only ever a channel rule, never a universal one** — worth
stating plainly, or the trade caution gets applied here by reflex and removes an advantage. (AVshop.no
runs both a system configurator and an automatic sound-isolation calculator —
`19-direct-and-carried-lines.md`.)

## The real weak link: cross-selling

Everything above points at the same gap, and it is worth stating bluntly: **we are currently poor at
cross-selling.** The group thesis rests on it — a dealer won on one layer becoming a dealer served on
the others (`01-dealer-as-asset.md`, `16-whole-room.md`) — and the nurture that would actually make it
happen does not exist.

That matters more than any tool decision. A tool cannot substitute for it, and trying to make one do the
job (by steering specifications) breaks the tool without fixing the gap.

**And the strongest cross-sell argument was never marketing anyway — it is that buying the whole room from
us ought to be simply easier.** We would already hold the drawings, know how the parts integrate, and have
made them to meet each other; one order, one delivery, and no coordination burden landing on the dealer.
That is an argument no competitor selling one layer can answer.

The uncomfortable part is that it isn't true yet in practice. Tools and data are fragmented, so a dealer
buying across brands today still pieces it together themselves — which means the whole-room proposition
currently fails on the exact ground where it should be unbeatable. Much of what SRND Engine (and the
platform's canonical dataset) sets out to solve is this fragmentation; it is an operational problem, not a
messaging one.

So cross-selling has two legs, in order:

1. **Make it genuinely easier.** Coherent data, drawings that exist without someone generating them by
   hand, known integration, parts that fit, one order and one delivery. Largely Engine and canonical-data
   work, and out of scope for this repo to specify.
2. **Then tell them.** The **partner-development campaigns** identified in the on-ramp: permissioned,
   adjacency-aware, timed to what the dealer is actually doing (`17-on-ramp.md`), with the tools supplying
   the *trigger* by revealing a live project and its needs.

The order matters, by our own rule: don't claim it until it's real. That is the same discipline as the
appreciation gap and the partner programme — the third time it applies, which suggests it is the group's
characteristic failure mode rather than a coincidence.

Two disciplines already settled apply here and should not be forgotten under commercial pressure: a
single-brand dealer is not a failed dealer, and pushing adjacency at people who don't want it is the
oversaturation risk (`02-commercial-model.md`). Relevance is the whole game.

## What this surfaces for the group strategy

- **Two competitors we don't have documented.** ADR 017's context names **Kolosseum.io** (polished web
  design tool with RP22 Performance Level grading, RP23 nomenclature, multi-format CAD export, acoustic
  overlay 3D) and **Cinema Room Setup** (standards-encoded Atmos placement, Dolby-range sliders, synced
  multi-view). Both ship without engine depth, and both are setting baseline expectations. Neither appears
  in `13-competitors.md` — a real gap, and a different competitive front from the hardware rivals already
  documented.
- **The commercial C-ATS range is further along than the brand doc implies.** ADR 048 records an accepted
  commercial/boutique objective model — SMPTE ST 202 X-curve, Dolby Atmos baffle-wall, THX NC-30,
  volume-conditional RT, large-format kit-of-parts. The C-ATS strategy still treats the commercial range
  as "in development, internal only", which is right for external copy but understates internal progress.
- **Cinema Expert's role.** `cinema-expert.com` is a skeleton with three headings — Instructions,
  Knowledge Base, **Certification**. The partner programme needs a training and certification programme
  it doesn't have, and C-ATS has prior art in tiered dealer certification. Worth a proper look.
- **Automate DT Create end-to-end** so lead capture doesn't cost manual time (in hand).

## Noted, deliberately not pulled in

The platform is wider than tools: **Folio** (configuration), **Probata** (measurement-driven commissioning
proving an installed room meets its design targets and cited standards), and **Auctor** (runtime and
telemetry). Probata is recognisably C-ATS verification and Pro-Fi calibration as a product, and Tessellate
is shared substrate consumed by Pro-Fi's Lattice and Apollo — the group's technical depth as common code
across brands. Commercially, ADR 017 is explicit that the platform play is the durable bet and the
design-phase win alone is not the long-term moat.

That is a significant strategic asset, and it is **deliberately out of scope here** while the brand
strategies are settled. Flagged so it isn't forgotten, not adopted. Anything taken from it later should be
read from the platform repo's current ADRs, not from this summary.
