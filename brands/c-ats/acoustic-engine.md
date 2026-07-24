# CATS — the acoustic engineering differentiator (measured data + RT60 designer)

The CATS equivalent of DT's Commander, Light Walls' measured colour, and Pro-Fi's voicing platform:
the un-copyable **measurement + modelling** layer. Captured from `ceenhad/c-ats-shopify`
(`data/c-ats-pack-rules-2026.md`, `CALCULATOR-AUDIT.md`, `CLAUDE.md`) and the referenced acoustic
engine in **cinema-tools** (not in this session — see note). Raw input; respect the brand-truth
guardrails throughout (scattering never diffusion; no invented figures).

## The thesis

CATS isn't "acoustic foam and diffusers" — it's **engineered, measured acoustics reduced to the
3 Rs** (Reflection / Resonance / Reverberation), one panel per problem, delivered as a **repeatable,
physics-driven design** within a shallow (~50 mm) depth. The differentiator is the **measured
per-panel data plus the modelling engine** that turns a room into a specified solution — not the
panels alone.

## Measured data (the asset)

- **BSRIA-measured per-panel absorption** (Sabines) is the ground-truth input — e.g. the Resonance
  Control Panel was **BSRIA-tested (2019)**. Held as `c-ats-acoustic-data.json`; feeds the engine's
  per-panel catalogue.
- This is measured performance, not declared — the honest, data-backed basis the brand-truth
  guardrails insist on.

## The RT60 modelling engine (in cinema-tools)

Neil built a from-scratch **RT60 treatment designer** (`engines/modal_analysis/acoustic_treatment.py`):
- Computes **per-octave-band RT60** (Sabine / Eyring / Fitzroy [headline, per-axis] / Arau /
  Millington) against a **CATS target (Rettinger × 0.85)**, and outputs a **panel-quantity
  recommendation {RES-CP, REV-CP, REF-CP}** with per-axis breakdown and a "needs +X m² Sabines"
  hint per band. **Quantities are physics-driven, not template-driven.**
- **Placement** is a separate concern — an 11-layer placement algorithm (the old 2015 coverage grids
  become layout/placement guidance, not counts).
- **Packs/grades (Bronze/Silver/Gold)** become a *presentation layer* over the engine — a scope +
  target-T60 tier fed in; the engine returns the quantities.

## Two tiers (the commercial shape)

- **Tier-1 (paid)** — the full RT60 designer / configurator: a measured, room-specific design.
- **Tier-0 (free)** — the **same engine** run with default surface materials (by market) + a
  grade-selected target, taking just room size + speaker format → {RES/REV/REF} quantities packaged
  as a pack + layout diagram. "Best-in-class because it's physics-based, not a template." Top-of-funnel
  lead-gen (cf. the group content-placement + the free selector).

## Caveats — do NOT overclaim (from the repo's own audit)

- **Resonance modelling has a known blind spot.** The tools size resonance off 125/250 Hz Sabine
  RT60 and miss the ~20–80 Hz modal region, so they can return **RES = 0 by construction** — which
  Neil ruled **wrong regardless of what the engine outputs.** The engine is **not ground truth for
  resonance**; a real ~90 m³ cinema needs bass/resonance trapping. Any messaging must not lean on the
  engine's resonance numbers.
- **The engine is kept off the storefront** — a decision (2026-06-10): no live thin-client wiring the
  store to the engine; **offline calibration only** (bake a grid of canonical rooms). The free
  selector is a parametric rule set, not a live engine call.
- Some engine work was **blocked** on converting the BSRIA data into the panel catalogue; status per
  the C-ATS repo.

## Status / where the engine lives

The engine and its validation refs live in the **cinema-tools** project (not currently in this
session). This capture is from the C-ATS repo's reconciliation docs. To go as deep as DT/LWCP/Pantheon,
add the cinema-tools repo. Treat the engine as a real, in-progress asset — not a shipping storefront
feature.

> **Cross-brand pattern (four-for-four).** DT → the Commander (control); Light Walls → measured
> colour; Pro-Fi → measured/verified voicing; **CATS → measured acoustics + the RT60 design engine.**
> The group's repeated, defensible edge is the **measurement + modelling + data layer**, the part a
> competitor can't copy from a datasheet (`../../group/13-competitors.md`). CATS's own version of the
> "copyability" point: the panels are simple; the measured data and the design engine are the moat.
