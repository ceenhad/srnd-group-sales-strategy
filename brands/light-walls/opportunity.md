# Light Walls — the opportunity (LWCP)

Captured from **`ceenhad/lwcp`** (README, docs/STRATEGY.md, the 2026-07-20 market-positioning &
opportunity research, ADRs), 2026-07-24. The thin Light Walls website is the visible tip; **LWCP —
the Light Walls Control Platform — is where the opportunity is.** Raw input for messaging. Status
caveats at the end: architecture/strategy are settled but the physical product is pre-fab — don't
present as shipping.

## The thesis (one line)

**A measured-quality lighting driver wrapped in whichever standard the market speaks.** Every colour
light already contains a calibration; LWCP's holds **measured per-unit data**, so the light is
actually on target — **for life**.

## What LWCP is

An architectural-grade pixel-and-white lighting platform, four parts:
- a **characterisation bench** that measures lighting products (spectrometer + native goniometric
  photometry — real TM-30 / IES / flicker / melanopic data);
- **drivers + light engines** that render measured colour (own-product Yuji 5050 high-CRI emitters +
  MY9291 drivers — already in production in the team's existing line, so the silicon/emitters are
  proven, not a bet);
- a **coordinator appliance** that orchestrates an installation (REST/WebSocket + DALI + Matter);
- a **design tool** that lets a lighting designer specify it in architectural terms.

## The moat — and why it's defensible

Per the market research (5-angle fan-out, adversarially verified): **on-driver data is already table
stakes** (DALI D4i mandates memory banks; Tridonic/Inventronics/Osram ship it). What no standard
field and no incumbent stores is a **per-unit *measured* spectral/goniometric/chromaticity profile
with active thermal/aging correction.** So the differentiator is **what is stored (measured-per-unit
fidelity), not that data lives on the driver.**

The genuinely defensible wedge is **three things held together, which no single incumbent has:**
1. **measured-per-unit colorimetric fidelity**,
2. executed as a **sensorless closed loop** (no optical sensing element — riding *free* D4i
   thermal/drive telemetry; undercuts Ketra's per-fixture optical sensing on cost),
3. surfaced through a **design-to-control-to-maintenance tool**.

**Freedom-to-operate has been cleared** on the two patents that threatened this (Ketra/Lutron
US8471496B2 to 2029; B/E Aerospace US9018858B2) — a formal counsel review is still advised before
the premium-driver certification spend, but the moat is not blocked.

## Where it sits (market position)

Across four incumbent clusters, holding what each lacks: **pixel-addressable** (like Advatek) +
**architecturally credentialled** (like Color Kinetics/Ketra) + **DT8/D4i standards-native** +
**modern network control & Matter** + **system-coordinated at scale** (like Hue) + **designed-for by
lighting designers in their own vocabulary** + **UK exclusive-design manufacture**. Each leg is
achievable alone; doing all at once is the category. The premium incumbents (Lutron/Ketra) are
**doubling down on closed ecosystems** and structurally can't follow into open Matter without
collapsing their premium — the disruption lever.

## The opportunity, by segment

- **(a) Architectural / colour-critical spec — the beachhead.** Galleries, museums, luxury retail,
  hospitality brand-consistency — where measured per-unit fidelity + D4i telemetry *substantiate* a
  spec claim competitors can only assert. DALI-2 is the dominant (if time-limited) beachhead.
- **(b) Circadian / human-centric — as substantiation, not a health claim.** Position as **"we can
  *prove* the melanopic target you're required to hit"** (WELL/UL EML thresholds computed from
  measured SPD + the spatial model), **never** "our light makes you healthier." (Healthcare, senior
  care, education, workplace.)
- **(c) Residential / prosumer via Matter — the disruption vector.** The premium/prosumer buyer
  trapped in closed ecosystems; companion app carries the quality story.

Business models surfaced: **profile-as-a-product** (the measured profile, with or without our
silicon); **calibration-as-a-service** at commissioning; **design-tool-as-lead-gen** (top of funnel).

## Three tiers (same hardware investment, three channels)

- **Tier 1** — retrofit / direct ingress (ArtNet/sACN) for integrators; broadens the funding base.
- **Tier 2** — DT8/D4i architectural luminaire; builds specifier credibility.
- **Tier 3 — the full system / "Light Walls"** — signature architectural installs, premium
  hospitality, brand experience; the **halo that proves the colour science**. Note the re-weighting:
  **calibrated white is the volume P&L; the pixel (Tier 3 / Light Walls) is the halo**, not the
  headline (~98% of the pro market is non-pixel, mostly white).

## Status — do NOT overclaim

- **Architecture and commercial strategy are settled; software is exercisable against mocks; the
  physical layer (custom PCBs, bring-up) waits on Stage 1A fab.** Not a shipping product line yet.
- FTO cleared on the two threatening patents, but formal FTO/patentability counsel review is
  recommended before the premium-driver cert spend.
- Open validations: confirm the "no incumbent stores measured per-unit profiles" gap is *empty* not
  merely undisclosed; size the addressable measured-quality niche (not the whole control/HCL TAM);
  per-pixel calibration workflow must be proven to scale.

## What this means for the brand (flag — a scoping decision)

The SRND "Light Walls" website today sells commodity-looking RGBW modules (down light / linear /
matrix) — i.e. the **Tier-3 pixel halo**, not the measured-quality driver/white play that is the real
commercial opportunity. **Decide how the brand relates to the full platform:** is "Light Walls" the
front for all of LWCP (measured-quality architectural lighting, standards-native, UK-made), or just
the pixel halo, with the driver/white play branded differently? This mirrors DT exactly — a thin
brand front over a deep, defensible **control/measurement** platform.

> **Cross-brand pattern worth noting:** like DT (the Commander control) and the competitor read
> ("hardware is copyable; measured data/control is not"), Light Walls' moat is **measurement + data
> + the closed-loop app layer** — not the LED. SRND's brands increasingly win on measurement and
> control, the un-copyable layer. (See `../../group/06-competitors.md`.)
