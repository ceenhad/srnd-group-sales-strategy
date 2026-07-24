# Pro-Fi — the opportunity (the speaker range + Pantheon)

Captured from **`ceenhad/pro-fi-design`** (the speaker range) and **`ceenhad/pro-fi-pantheon`** (the
software + electronics platform), 2026-07-24. The `pro-fi.uk` website is thin and out of date; this
is the real substance. Raw input for messaging. Status caveats at the end — the platform is
in-development toward a v1 launch, not shipping; don't overclaim.

## The thesis (what makes Pro-Fi Pro-Fi)

**The speakers deliberately have no house sound.** Sealed, active, DSP-coupled, AoIP-native,
detailed and transparent — built so they **defer to the *voicing*** the integrator and customer
arrive at together. *"Other manufacturers ship a house sound; the customer takes it or finds another
maker. Pro-Fi ships speakers that defer to the voicing applied to them."* What a Pro-Fi system is
worth is **not the speakers alone — it's the voicing** the properly-characterised, integrated system
delivers for this listener, in this room, for this purpose.

**Pantheon exists to make that voicing trustworthy** — *"the genuine outcome of a rigorous process,
rather than a marketing claim layered over ordinary engineering."* (Note how squarely this fits the
group pattern: the moat is the measurement + DSP + data layer, not the box.)

## Two repos, two halves

- **`pro-fi-design` — the speaker range** (canonical data + schemas; a math engine renders each
  cabinet from T/S params, with first-class provenance and CEDIA-RP1-1-honest disclosure). Ranges:
  **Spatial** (BMR satellites — dot/dash/cube), **Modular** (line-array blocks, stackable),
  **Stage** (BMR 2-way LCR), **Cinema** (2-way LCR; the Reference is now a **coax point-source** on
  FaitalPRO HX; `cinema_12_reference_coax` flagship), **LFE** (sealed subs 5/8/12/15, infra_21).
  ~32 cabinets; solid-aluminium, sealed, active.
- **`pro-fi-pantheon` — the platform** (software + electronics): the process that turns those
  speakers into trustworthy voicing.

## The process (Pantheon's spine)

Each stage produces durable data the next builds on:
- **Faithful speakers** — per-unit end-of-line measurement (**Vulcan**), model characterisation on a
  motorised turntable rig (**Daedalus**: Spinorama/CLF/GLL, polars, distortion), RP1-1 disclosure.
- **Always-in-path DSP appliance (Apollo)** — owns the signal path; applies voicing over a calibrated
  baseline; AES67 **source aggregation + variant bridging**; predictive protection; cloud-connected
  for ongoing service. Scales from a kitchen 2.1 to a commercial cinema (same software, sized HW).
- **One vendor-neutral network-audio engine (Ariadne)** — software AES67 / ST 2110-30 over a
  commodity NIC; turns any machine into a standards endpoint.
- **Comprehensive analysis from minimum measurement** — FR, distortion, reflections, modes, timing,
  headroom, automatically; **raw measurements preserved so better algorithms apply retroactively.**
- **Calibrated baseline + voicing layered over** — standards apply to the baseline; preference to the
  voicing; **voicings stored as semantic "intent" objects** that survive recalibration and transfer
  between systems.
- **Listener physiology** — audiograms become **per-ear hearing-corrective voicing presets**
  (genuinely novel and humane).
- **Subjective feedback as data** — "more kick," "too bright" captured verbatim, LLM-translated into
  measurable hypotheses, evaluated against the analysis record, with an audit trail.
- **Framework verification** — RP22 (residential immersive), AVIXA 10:2013 (commercial AV), **SMPTE
  RP 2096-1 (commercial cinema)** — as pluggable data, a property of the baseline.

**Products:** Apollo (DSP appliance) · Hermes (on-site commissioning UI, a surface of Apollo) ·
Vulcan (factory EOL test) · Daedalus (design-verification rig) · Olympus (cloud/fleet, remote
service) · Janus (third-party speaker-profile programme). Plus the **canonical dataset** as the data
spine. Design-for-install filter: **Easy · Visible · Tolerant · Recoverable** (remote diagnosis via
Olympus — a fault is "a short diff against the sign-off snapshot, not a truck roll").

## v1 launch market: commercial cinema

Chosen because: the standalone cinema audio-processor category is **structurally collapsing** (ICMPs
now embed AES67 decoders, making Dolby CP950 / Datasat / QSC DCP legacy); **AES67 source diversity**
(Dolby vs Dante vs generic, PTP/DSCP/multicast fights) is a live pain Apollo's aggregation/bridging
solves; Pro-Fi already has cinema presence (warm channel); and cinema's **recurring-revenue** logic
(SMPTE recert with audit trail, fleet analytics, drift detection — paid services) is sharp.
Residential cinema + high-end whole-home follow in **v1.5**; hospitality + commercial AV in **v2**.

## Why it compounds (data as asset)

Preserved measurement/calibration/voicing data becomes a Pro-Fi asset — informing speaker design,
field service and product evolution — and underwrites a **recurring-revenue stack** (service
contracts, cloud subscription, specialist services, partner programme) intended to exceed the
initial hardware sale over an install's life.

## Status — do NOT overclaim

- The platform vision is explicitly **"strategic vision… not a specification, not a commitment to
  timelines."** Pantheon is **in development toward a v1 launch** (active demo/beta-readiness work in
  the repo), not a shipping product line. The speaker range is a committed **design-intent
  catalogue** (renders/data), with production status per model.
- Treat as a strong, real platform story to *tell truthfully as direction* — don't present unshipped
  products/certs as available.

## What this means for the brand (flag — a scoping decision)

The `pro-fi.uk` site sells "luxury speakers & amps" and says nothing about the platform. The real
differentiator — **voicing you can trust, measured and auditable; hearing-corrective voicing; a
system that keeps improving after commissioning** — is invisible externally. Decide how the brand
front relates to Pantheon (as with DT/Commander and Light Walls/LWCP: a thin brand over a deep
measurement/DSP platform).

> **Cross-brand pattern (now three-for-three):** DT wins on the Commander (control); Light Walls on
> measured colour; Pro-Fi on measured/verified **voicing**. The group's real, repeated edge is the
> **measurement + control + data layer** — the un-copyable part (`../../group/13-competitors.md`).
