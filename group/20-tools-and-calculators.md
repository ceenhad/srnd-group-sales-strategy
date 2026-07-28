# Tools and calculators

*Where calculators fit commercially, and the rule for what may be published where. Internal.*

*The Cinema Platform repo (`ceenhad/cinema-platform`) is authoritative for what the tools are and how
they're built — in particular Cinema Tools ADR 014, which defines the three-level structure. This
document is the **commercial** position: it references that structure rather than redefining it, and the
platform is otherwise deliberately kept outside this repo's scope.*

## Calculators are central, not a risk

Calculators are the single most important driver of engagement and time saving we have. They answer a
real question instantly, they demonstrate competence rather than asserting it, and — used properly —
they capture a lead while doing it. The strategy should be biased *toward* building them.

An earlier draft of the C-ATS strategy said "no public calculators" on the grounds that a calculator
commoditises chargeable design. That reasoning was wrong and is withdrawn. What C-ATS sells isn't
arithmetic: it's measured data, judgement, and the fact that C-ATS puts its name behind the result and
can verify it in the finished room. **Accountability cannot be commoditised.** A tool produces a number;
only we can be responsible for it.

## The real failure mode is implication, not disclosure

The genuine objection is narrower and more important. A C-ATS calculator hosted on the C-ATS website
can never replace a £5,000 design service — but **its mere presence implies that it might.** The damage
is done by placement and framing, not by giving anything away.

That gives a three-part test for any tool, drawn from tools we already run:

1. **Can it completely answer the question it poses?** DT Create can — ideal screen size, then draw the
   screen. A reflection-point calculator can — the geometry is the whole answer. "How much treatment
   does my room need" cannot, honestly, in a web form.
2. **Does it imply it answers a bigger question than it does?** This is the C-ATS failure mode. A tool
   must be visibly bounded, so nobody mistakes sizing for design.
3. **Does it close its own loop?** Real value to the user, a lead or data to us, and **no hidden manual
   work.** DT Create is the cautionary detail here: it captures the lead well, but asking the user to
   *request* the CAD means someone then spends twenty minutes generating and emailing it. Automating
   that generation and delivery — already in hand — is what turns a good calculator into a good business
   process. Un-automated, a popular tool is a tax on our own people.

## Hosting is the structural answer

The implication problem is solved by *where* a tool lives, not by how it's worded.

- **`cinema-tools.com` — the neutral property.** Free, credited to SRND but not a brand front. A
  capable calculator here undercuts nothing, because Cinema Tools isn't C-ATS. This is why holding
  Cinema Tools apart from the brands was right, and it means the answer already exists rather than
  needing invention.
- **Brand sites — product-configuring tools.** Tools that size and specify *our product* and lead to a
  purchase, a CAD or a quote. DT Create is the model.
- **`cinema-store.com` — buying-support tools.** For self-builders there is no chargeable design to
  protect, so configurators and estimators are pure asset. **No-calculators was only ever a channel
  rule, never a universal one** — worth stating plainly, or the trade caution gets applied here by
  reflex and removes an advantage. (The AVshop.no reference runs both a system configurator and an
  automatic sound-isolation calculator; see `19-direct-and-carried-lines.md`.)

## The tiering already exists

Cinema Tools ADR 014 defines a three-level structure, and it does the commercial work we need:

- **Level 1 — Calculators.** Free, no login, deliberately scoped to *basic residential* design. Seven
  tools; **each one a discrete SEO landing page** targeting specific search queries, with **optional
  lead capture on PDF download**.
- **Level 2 — Cinema Tools Online.** A *paid* design environment covering commercial and residential
  design in depth.
- **Level 3 — Cinema Tools Pro.** Local installable for heavy compute — FEM solves, multi-sub modal
  optimisation, **treatment placement** — with an interactive 3D front end.

Why that settles the C-ATS worry: a free tool cannot imply it replaces serious design when visibly more
capable **paid** tiers of the same product line exist, and the capability that actually competes with a
design service — treatment placement — sits at Level 3 behind local heavy compute, not in a web form.
The tiering communicates the boundary that an isolated calculator on a brand site cannot.

Two of these are group-strategy assets already built rather than planned, and should be recognised as
such:

- **Lead capture on PDF download is the on-ramp hinge in product form.** A free tool that trades a
  useful PDF for contact details is precisely the registration-and-permission moment
  (`17-on-ramp.md`) — and it is voluntary, valuable and honest, which is how permission should be won.
- **Calculators as individual SEO landing pages** are the GEO/AEO strategy implemented, not aspired to.

## C-ATS specifically

- **No design-replacing calculator on the C-ATS site.** Not because of what it would reveal, but because
  of what its presence would imply.
- **Do publish worked examples showing how quantities are derived.** Method transparency, without
  suggesting the room can be solved by a form. This is the bridge that lets a competent dealer handle
  straightforward rooms.
- **A reflection-point calculator is a good candidate**, and it passes all three tests: it is *geometry,
  not acoustic design*. It answers "where do first reflections land" completely and honestly, and it
  doesn't pretend to answer "will this room perform" — which is what the design service and verification
  own. A placement tool, not a design tool. It is also the notable gap in Cinema Tools' own set, sitting
  directly on the first of the 3 Rs.
- **Honesty flag:** the Room Resonances calculator is live, and the resonance-sizing method has a known
  low-frequency blind spot (`../brands/c-ats/measured-acoustics.md`). Of all the tools, this is the one
  whose limits must be stated plainly. C-ATS exists because competitors promised physics they couldn't
  deliver; a tool that oversimplifies would be that same sin committed by us.

## What's still open

- **The Cinema Tools Online ↔ C-ATS design-service overlap.** Already flagged as unresolved in ADR 014
  (the historical "C-ATS partner tool" framing). This is the real strategic question — not whether to
  publish calculators, but where a paid design *service* ends and a paid design *tool* begins, and
  whether they are competitors, a ladder, or the same offer sold two ways.
- **Whether tool access becomes a partner benefit.** Giving registered partners access to serious design
  tooling costs no margin and is exactly the currency the partner programme runs on — spend the depth,
  not the margin (`18-partner-programme.md`). Worth deciding alongside the Level 2 commercial model.
- **Cinema Expert's role.** `cinema-expert.com` is a skeleton with three headings — Instructions,
  Knowledge Base, **Certification**. The partner programme needs a training and certification
  programme it doesn't yet have, and C-ATS already has prior art in tiered dealer certification. The
  property may already be the right home for it. Worth a proper look.
- **Automate DT Create end-to-end** so lead capture doesn't cost manual time (in hand).

## Noted, deliberately not pulled in

The platform is wider than tools: **Folio** (configuration), **Probata** (measurement-driven
commissioning that proves an installed room meets its design targets and cited standards), and
**Auctor** (runtime and telemetry). Probata in particular is recognisably C-ATS verification and Pro-Fi
calibration as a product, and the modal-analysis engine (**Tessellate**) is shared substrate consumed by
Pro-Fi's Lattice and Apollo — the group's technical depth as common code across brands.

That is a significant strategic asset, and it is **deliberately out of scope here** while the brand
strategies are settled. Flagged so it isn't forgotten, not adopted.
