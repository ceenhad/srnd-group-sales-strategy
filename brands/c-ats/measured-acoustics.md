# CATS — the engineering differentiator (measured, engineered acoustics)

CATS's moat is its **own measured, engineered acoustics** — not a software platform. Captured from
`ceenhad/c-ats-shopify` docs, 2026-07-24. Respect the brand-truth guardrails throughout (scattering
never diffusion; no invented figures).

> **Scope correction.** An earlier version of this file framed the RT60 design *engine* as CATS's
> differentiator. That was wrong: that engine lives in a **separate project (cinema-tools), which is
> NOT the CATS brand** and is **not being pulled in.** CATS *feeds* measured data to such tools; the
> tools are not part of CATS's brand story. This file is about what CATS itself owns.

## The thesis (what CATS owns)

The 3 Rs (Reflection / Resonance / Reverberation) reduced to **one engineered panel per problem**,
with **BSRIA-measured performance**, delivered in a shallow (~50 mm) depth — a comprehensive,
repeatable, honest, data-backed solution. The differentiator is the **measured performance + the
disciplined 3 Rs engineering**, not marketing claims (brand truth: state benefits, never figures the
data doesn't support; scattering, never diffusion).

## The measured data (the genuinely CATS-owned asset)

- **BSRIA-measured per-panel absorption** (Sabines) — e.g. the Resonance Control Panel was
  **BSRIA-tested (2019)**. Measured, not declared. This is the real, defensible CATS asset: honest
  measured performance behind the 3 Rs.

## Design tooling is separate (not CATS, not pulled in)

- A physics-based **RT60 treatment designer** exists that turns CATS's measured data into panel
  quantities/placement — but it lives in the **separate cinema-tools project**, not the CATS brand.
  Per Neil, don't fold it into CATS and don't pull it in now.
- Known caveat on that tooling (from the C-ATS repo audit): a **resonance blind spot** (sizing off
  125/250 Hz Sabine RT60 misses the ~20–80 Hz modal region, can return RES = 0 by construction —
  ruled wrong). So **don't lean on resonance numbers from that tool**, and don't attribute the tool
  to the brand.

## Where CATS fits the group pattern

CATS's edge is **measured, engineered acoustic performance** — which fits the group's repeated
"measurement + data" pattern (DT → control; Light Walls → measured colour; Pro-Fi → voicing), but
CATS's version is the **measured panel performance + 3 Rs engineering discipline**, not a software
platform. Its "copyability" answer: simple-looking panels, but the measured data and the engineering
rigour are the substance (`../../group/13-competitors.md`).
