# Tools and calculators

*Where calculators fit commercially, and the rule for what may be published where. Internal.*

*The Cinema Platform repo (`ceenhad/cinema-platform`) is authoritative for what the tools are and how
they're built. This document is the **commercial** position and references those decisions rather than
restating them. Grounded in Cinema Tools **ADR 017** (commercial-first, engine depth as IP, report as the
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

## What is actually sold: the report, not the tool

This is the decision that settles the whole question, and it is already made. Under ADR 017 the monetised
deliverable is **the report**, not access to a tool — residential design-it-yourself subscription is
explicitly retired. The engine substrate (**Tessellate**) is the IP: what the engines *compute*, not how
the interface looks. Speed-to-report — minutes rather than days, with full acoustic and performance-level
evaluation — is the value proposition.

The platform's own phrasing is the cleanest statement of it: **"the deliverable is the recipe, not the
recipe-finder."**

Once that is understood, the anxiety about calculators dissolves. A free calculator cannot cannibalise a
paid design service, because what the service sells is a *deliverable carrying accountability* — measured
data, judgement, and a result somebody stands behind and can verify. Arithmetic was never the product.

A useful discipline travels with it: **UI polish is a qualifier, not the IP.** It must not embarrass the
engine, but it isn't where we compete. That is the same instinct as the group's voice — substance over
surface.

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

## The value ladder

ADR 017 sets out how design revenue actually arrives, and it is a ladder rather than a product:

free calculators (discovery and authority) → **partner-gated C-ATS reporting tool** (the residential
revenue route through the partner channel) → **Pro Design escalation at £500, invoiced per engagement**
→ partner-network escalation → brand-partnered recipe packs (Pro-Fi is the proof) → and, separately, the
full C-ATS design service and verification where a project warrants it.

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

For self-builders on `cinema-store.com` there is no chargeable design to protect, so configurators and
estimators are pure asset. **No-calculators was only ever a channel rule, never a universal one** — worth
stating plainly, or the trade caution gets applied here by reflex and removes an advantage. (AVshop.no
runs both a system configurator and an automatic sound-isolation calculator —
`19-direct-and-carried-lines.md`.)

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
