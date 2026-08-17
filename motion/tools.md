# Tools and calculators

*Where tools fit commercially, and what may be published where.*

*The `ceenhad/cinema-platform` repo is authoritative for what the tools are and how they're built; this is the
**group commercial** view, which is a wider frame because we are a manufacturer. **Grounded in Cinema Tools
ADR 017 v2, ADR 011 v2 and ADR 036 v2 — checked against the platform 2026-08-16.** Read from the platform's
current ADRs before acting; this document has twice cited retired ones.*

> **▲ Citations corrected 2026-08-16.** **ADR 017 went to version 2 on 2026-08-13, consolidating 001, 014,
> 019 and 073 into it**, and **ADR 020 was superseded by ADR 011** (lead capture). Both stale references in
> this document have been repointed. **What remains outstanding is the substance:** five decisions in the
> current 017 are still not reflected below, and they matter commercially: **Pro is internal tooling** whose stated purpose is *"to make
> the method reproducible by fewer people in less time"* (§4) · **four revenue lines carry the business —
> training, design services, the partner channel, product** (§10) · **lead capture is launch-blocking** (§9) ·
> **commercial cinema is the lead market** (§3) · **demand is measured before the curriculum or the partner
> programme is built** (§12). Prices and tiers live in the platform's `docs/product/`, not here.
> **The fix is not to restate them.** This page should cite current 017 and read from `docs/product/`;
> duplicating a live decision is what `CLAUDE.md` warns is worse than no artefact.

## Calculators are central, not a risk

Calculators are the single most important driver of engagement and time saving we have. They answer a real
question instantly, they demonstrate competence rather than asserting it, and used properly they capture a
lead while doing it. **Bias toward building them.** An earlier "no public calculators" rule in the C-ATS
strategy is withdrawn — it protected the wrong thing.

## What we are, and what we are not

- **An online services company?** No.
- **A paid design-tool vendor?** No.

**We are a manufacturer.** Tools help sell services and make money, but the service isn't where it stops: a
design specifies a room, and we make most of what goes into it.

That's the whole strategic point. For Kolosseum, Cinema Room Setup or DARDT the tool *is* the business, so it
has to pay for itself. **The ladder doesn't end at the report; it ends at the room being supplied** — the
largest rung, and the one the tool docs can't see from where they sit. Two consequences competitors without
factories can't copy: we can afford to be **more generous with tooling** and invest more in the engine, because
the payback is downstream rather than in the tool's P&L; and **engine depth pays twice**, once as a better
deliverable and once because a dealer who trusts our design work is a dealer we have a relationship with.

### But never build the tool around our own products

The tempting mistake, and a bad one. Push pull-through into the tool and the absurdity arrives at once: would
we only design rooms around Pro-Fi, and turn down every C-ATS design opportunity on a room using someone
else's speakers? Refuse a project because the ceiling mount isn't ours? Obviously not. Most rooms will always
contain other people's equipment, and design work on those rooms is business we want.

So there is **no specification-share target** and no quiet weighting of the catalogue. **The tool's job is to
be the best help available for whatever room is in front of the dealer.** Present in the catalogue and easy to
specify is sufficient. Brand-agnostic engines aren't a concession to minimise — they're what makes the tools
worth using and DARDT replaceable. A tool caught favouring us would destroy the trust that makes it valuable,
and cost us the design work on every room that isn't all-SRND, which is most of them. Pro-Fi's principle states
the posture: *informs, never blocks; the customer decides* — sell more only when it genuinely helps.

What the tools genuinely give us is better anyway: **they tell us a project exists and what it needs.** That's
the raw material for a relevant, timely conversation, and turning it into revenue is relationship and campaign
work (`buyer-journey.md`).

## What is sold: the report, not the tool

Under ADR 017 the monetised deliverable is **the report**, not tool access; residential design subscription is
retired; engine depth (**Tessellate**) is the IP; and speed-to-report — minutes rather than days — is the value
proposition. The platform's own phrasing is the cleanest statement of it: **"the deliverable is the recipe, not
the recipe-finder."**

Which is why free calculators cannot cannibalise paid design: what's sold is a deliverable carrying
**accountability** — measured data, judgement, and a result somebody stands behind and can verify. Arithmetic
was never the product. At group level the report is a stage, not the destination.

A discipline travels with it: **UI polish is a qualifier, not the IP.** It must not embarrass the engine, but
it isn't where we compete.

## The real failure mode is implication, not disclosure

A C-ATS calculator on the C-ATS website can never replace a £5,000 design service — but **its presence implies
it might.** The damage is done by placement and framing, not by giving anything away.

Three tests for any tool, drawn from tools we already run:

1. **Can it completely answer the question it poses?** DT Create can (screen size, then draw the screen). A
   reflection-point calculator can (geometry is the whole answer). "How much treatment does my room need"
   cannot, honestly, in a web form.
2. **Does it imply it answers a bigger question than it does?** The C-ATS failure mode. Tools must be visibly
   bounded, so nobody mistakes sizing for design.
3. **Does it close its own loop?** Real value to the user, a lead or data to us, and **no hidden manual work.**
   DT Create is the cautionary detail: it captures the lead well, but asking the user to *request* the CAD costs
   someone twenty minutes a time. Automating that — in hand — turns a good calculator into a good business
   process. Un-automated, a popular tool is a tax on our own people.

## Cinema Tools is the master brand for design tooling

Per **ADR 017 v2 decision 8**, **Cinema Tools is the master brand for the design surface**, and `cinema-tools.com` is
the lead-magnet front door. This is what resolves the implication problem structurally:

- **Free calculators live on cinema-tools.com**, for discovery, SEO and authority — each a discrete SEO landing
  page, with lead capture on PDF download landing in the **SRND Engine `leads` table** (**ADR 011 v2**). That is the
  on-ramp hinge in product form: a useful PDF traded for contact details, won willingly rather than extracted.
- **The C-ATS partner tool inherits the Cinema Tools brand** rather than being C-ATS-branded, and its outputs
  carry **"Powered By Cinema Tools"** bylines — one brand across the whole free → partner lifecycle. It is the
  closed-network residential variant: partner-gated, residential cinema and music rooms only, panel catalogue
  locked, methodology black-boxed (partners see results, not internals), with an endorsed 11-module scope from
  project model and room-data entry through multi-sub optimisation and treatment placement to the RP22
  scorecard, reports, drawings and the Pro Design workflow.
- **"Cinema Tools Online" is not used externally.**

So a capable tool never sits *on* a brand site implying that brand's paid service is unnecessary. The design
surface is Cinema Tools throughout; the brands sell products, services and accountability.

## The ladder

Free calculators → the partner-gated C-ATS reporting tool → **Pro Design escalation at £500, invoiced per
engagement** → brand-partnered recipe packs (Pro-Fi is the proof) → the full C-ATS design service and
verification where a project warrants it → **and then the products that build the room.**

> **Correction, 2026-08-16 (Neil).** This ladder previously carried a **"partner-network escalation"** rung
> between Pro Design and the recipe packs. **It was invented here** — the phrase appears nowhere in the
> platform documentation, which is authoritative for what the tools are. **Removed.** *Recorded because the
> failure is instructive: real rungs either side made an invented one in the middle read as sourced, and it
> survived long enough to be put to Neil as a question about a thing that does not exist.*

No subscription billing: partner access is gated by SRND-managed credentials. Which means **tool access as a
partner benefit is already the operating model**, not a proposal — and precisely the currency the partner
programme runs on (`partner-programme.md`).

## C-ATS specifically

- **No design-replacing calculator on the C-ATS site** — because of what its presence implies.
- **Do publish worked examples showing how quantities are derived.** Method transparency without suggesting a
  room can be solved by a form.
- **A reflection-point calculator is a good candidate**, and passes all three tests: it's *geometry, not
  acoustic design*. It answers where first reflections land, completely and honestly, and doesn't pretend to
  answer whether the room will perform. A placement tool, not a design tool — and the notable gap in the
  current set, sitting on the first of the 3 Rs.
- **Honesty flag:** the Room Resonances calculator is live and the resonance-sizing method has a known
  low-frequency blind spot. Of all the tools, this is the one whose limits must be stated plainly. C-ATS exists
  because competitors promised physics they couldn't deliver.

## The consumer channel

For DIY buyers on `cinema-store.com` there's no chargeable design to protect, so configurators and estimators
are pure asset. **No-calculators was only ever a channel rule, never a universal one** — worth stating, or the
trade caution gets applied here by reflex and removes an advantage.

## Noted, deliberately not pulled in

The platform is wider than tools: **Probata** — measurement-driven commissioning that proves an installed room
meets its design targets. **Probata is recognisably C-ATS verification and Pro-Fi calibration as a product**,
and Tessellate is shared substrate consumed by Pro-Fi's Lattice and Apollo — the group's technical depth as
common code. *(An earlier version of this paragraph attributed a "platform play is the durable bet" line to ADR 017. **That wording is not in 017 v2** — checked 2026-08-16 — so the claim is withdrawn rather than re-cited.)*

**Out of scope here** while the brand strategies settle. Flagged so it isn't forgotten.

> **Correction, 2026-08-15 → 16 (Neil).** This list previously also named **Auctor** (runtime and telemetry)
> and **Folio** (configuration). **Both carry no commercial value and are not part of the platform play** —
> along with **Lustre**, which the LWCP ADRs describe as an absorbed corpus. **Removed rather than struck**, so
> no future pass reinstates them from a half-sentence.
>
> **And Probata is undecided — but only as a tool.** *"Do we commercialise Probata is the unknown"*
> (`registers/questions.md` **Q38**). **The service it delivers is not in doubt:** *"**verification is mandatory in
> commercial cinemas**, and probably interesting as part of a calibration in residential"* (`Q36`).
> **Keep the two apart** — an earlier draft here merged them, which is a mistake with different economics on
> each side.
>
> **Note alongside it:** acoustic verification is advertised on `cinema-tools.com`, and Neil's own point
> (`registers/questions.md` Q36) is that **verification is mandatory in commercial cinemas** and attaches to calibration
> in residential.
>
> **The consequence worth carrying:** with Auctor and Folio out and Probata undecided, the platform's
> *"recurring lifecycle tail"* has little established behind it. **Do not repeat it as though it did.**
