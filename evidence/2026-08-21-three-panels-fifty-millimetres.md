# "Three Panels, Fifty Millimetres" — the locked performance record, 2026-08-21

**Neil, 2026-08-21: *"that is locked for the record."*** *So this supersedes inference throughout the C-ATS record.*

**Source:** `https://claude.ai/code/artifact/a2588826-f03e-4686-8ef6-08a977505f3b` — *a private artefact. **The facts the
repo relies on are transcribed below** so nothing here depends on a reader having access to that link.* Built on BSRIA
100241/1, BS EN ISO 354:2003, 210 m³ chamber, tested 24 July 2019, transcription verified 21 August 2026.

## Construction and mechanism, per panel

| | Build | Mechanism |
|---|---|---|
| **RES** 600 × 600 | **3 mm acrylic bonded to a 40 mm foam** | **Membrane absorption.** The plate is **pressure-driven**, so a boundary loads it. Its hard face absorbs nothing at HF, so the only foam the room sees is the 40 mm edge band |
| **REV** 300 × 300 | **A single 50 mm foam** | Porous absorption rising to a plateau above 1 kHz. **A foam has a rigid backing whether it lies on a chamber floor or is stuck to a wall, so the lab figures *are* the installed condition** |
| **REF** 300 × 300 | **A 3 mm ABS moulding, relief to 50 mm** | Specular **break-up** from the relief, plus a panel resonance that bonding damps. **Not an absorber** — its discrete-object figures sit at the ISO 354 noise floor |

**Two things here are new to this repo.** *The REF panel is a **3 mm moulding with relief out to 50 mm**, not a 50 mm
solid — which is why the depth argument's "relief, not bulk" reading was right for the right reason. And **the REV
panel's lab condition is its installed condition**, which refines the free/unfixed caveat: it applies to the REF panel,
not to all three.*

## Complementary, not overlapping — the system-level argument

*All three boxes cover the same 1.44 m². **RES falls with frequency, REV rises, and they cross in the 400–500 Hz
region.** That crossing is what makes a full-range result out of two 50 mm devices, and it is invisible in any single
table.*

**Equivalent absorption area per box, m²:**

| Band | RES | REV | REF |
|---|---|---|---|
| 125 Hz | **1.52** | 0.48 | −0.00 |
| 250 Hz | **1.40** | 0.80 | 0.16 |
| 500 Hz | 1.28 | **1.76** | 0.96 |
| 1 kHz | 1.00 | **2.56** | 0.16 |
| 2 kHz | 0.60 | **2.72** | 0.00 |
| 4 kHz | 0.56 | **2.88** | 0.16 |

**The headline figure, and it is better than anything this repo had assembled: RES delivers 1.52 m² of absorption from
1.44 m² of coverage at 125 Hz** — more than its own area, at a 2.7 m wavelength, in 50 mm. *Measured. That single line
carries the whole low-frequency argument.*

*REF's 0.96 at 500 Hz is its panel resonance, not absorptive capacity — the only band where it registers at all.*

## The boundary ladder, and the loading reverses across the band

*Equivalent absorption area **per RES panel**, m², by number of bounding planes. All three BSRIA configurations stood
the panels on the chamber floor, **so the ladder counts bounding planes rather than walls.***

| Placement | Test | 125 | 250 | 500 | 1k | 2k | 4k |
|---|---|---|---|---|---|---|---|
| 1 plane — floor only | T3 | 0.150 | 0.183 | 0.300 | **0.303** | **0.250** | **0.207** |
| 2 planes — one wall | T5 | 0.283 | 0.277 | 0.310 | 0.273 | 0.177 | 0.150 |
| 3 planes — a corner | T4 | **0.383** | **0.350** | **0.317** | 0.247 | 0.150 | 0.137 |

**At 125 Hz: ×1.00 → ×1.89 → ×2.55 as planes are added. At 2 kHz: ×1.00 → ×0.71 → ×0.60.** *Two mechanisms in one
panel — **the plate loads up while the exposed foam edge band is shadowed** — and at 2 and 4 kHz the measured ratio
tracks the exposed edge count, 0.72 against 0.75 predicted for one wall.*

**And it found a live engine error, since fixed.** *A trap column stacks a vertical corner, so only its bottom and top
panel touches three planes and the rest touch two. **The engine credited the corner figure to all of them — on a
reference design, 12 of 20 traps over-credited by 36 % at 125 Hz.** Each trap is now credited the rung it landed on;
sizing still aims at a corner, because that is the intended use.*

## The tuning, calculated and correlated — `KNW-13` answered

*RES is a mass-spring absorber with a calculable tuning: **f₀ = K / √(m·d)**, with **m = 3.56 kg/m²** and **K ≈ 1600**
for a filled cavity.*

- **134 Hz** calculated
- The 125 Hz third-octave band spans **112–141 Hz**
- **Measured peak 0.47 at 125 Hz** — the maximum of the entire RES dataset — **with a notch of 0.31 immediately above
  it at 160 Hz**

**A notch above a peak is the signature of a resonance rather than a rising curve**, so the device's tuning appears
exactly where its construction says it should. *And because f₀ scales as 1/√(m·d), **a variant is predictable without a
new test** — a capability claim nothing in the brand makes.*

## Why 100 Hz is a floor — the arithmetic behind `Q96`

> *"It's simply not possible to measure panels below 100 Hz — it would need a nuclear bunker sized reverb chamber."*
> — Neil, 21 August 2026

**BSRIA's 210 m³ chamber has a Schroeder frequency of 309 Hz at T = 5 s and 390 Hz at T = 8 s** — so it is a diffuse
field only above roughly 300–400 Hz, and **even the 125 Hz figure carrying the low-frequency story sits below that
limit.**

| Diffuse down to | Volume needed (T = 8 s) | Against 210 m³ |
|---|---|---|
| 100 Hz | ~3,200 m³ | 15× |
| 50 Hz | ~12,800 m³ | 61× |
| 30 Hz | ~35,600 m³ | **170×** |

**So below 100 Hz calculation is not a stand-in for a missing measurement — it is the only method there is, and the
agreement at 125 Hz is what licenses it.** *Below that region the critical in-room factor is **subwoofer placement**,
not absorption, which is why the allocator sizes treatment from 125 Hz up and leaves the rest to the bass optimiser.*

## Two mountings, not two models — and one figure with no lab behind it

**Plane absorption coefficient αs, from 1.44 m² samples:**

| Panel | 125 | 250 | 500 | 1k | 2k | 4k |
|---|---|---|---|---|---|---|
| REV — foam | 0.25 | 0.51 | 0.88 | 1.09 | 1.07 | 1.18 |
| RES — acrylic + foam | 0.45 | 0.49 | 0.57 | 0.46 | 0.39 | 0.26 |
| **REF — mode A** *(no lab measurement)* | 0.01 | 0.08 | 0.28 | 0.11 | 0.01 | 0.06 |
| REF — mode B, lab | 0.01 | 0.20 | 0.54 | 0.12 | 0.04 | 0.09 |

**⚠ Read α above 1.0 correctly, and this corrects something this repo published today.** *REV reads 1.09 to 1.18 from
1–4 kHz. BSRIA attributes that to diffraction, and **the samples were 1.44 m² against the 10–12 m² the standard
wants**. **An α above 1 is not a coefficient you can apply over a wall.** It applies to contiguous coverage knowing it
over-predicts a large installation; the per-object figures are what a spaced layout should use; and the engine's
edge-gain factor must not be recalibrated to reconcile them, because the α it would multiply is already
edge-inflated.*

**Mode A is adhesive-bonded — the recommended install and the engine default — and its figures come from the legacy
CATS Calculator rather than from BSRIA, because BSRIA tested only unfixed panels.** *So the range's default install
condition is **the one figure in the set without a lab measurement behind it.** Recorded, not open — but it is the
honest caveat that belongs beside any mode-A number, and it is sharper than `DOC-4` states it.*

## The layout must still be aperiodic — and for a better reason

*The array-layout machinery was built to chase "diffusion uniformity". **C-ATS does not claim mathematical diffusion** —
a true diffusor needs far-field distance a small room does not have, and the objective is moving a reflection from
audible to inaudible. **The question was whether the aperiodic requirement survives that reframing. It does, for a
better reason than the one it was built on.***

*Measured on the spatial power spectra of the two candidate layouts: **uniformity 0.21 for a checkerboard against 0.66
for a maximum-length sequence.** A checkerboard repeats every two tiles and puts its energy in a single bin — the
shortest scale. The sequence never repeats and spreads across thirteen bins including two beside DC, the patch-wide
scales.*

## Two wording tensions to resolve, both minor

- **§01 says "every panel builds out 50 mm from the surface"** while RES is 3 mm + 40 mm = **43 mm** (`Q82`). *Read as
  the system envelope rather than a per-panel figure, but the two sentences sit adjacent.*
- **The crossover is given as "500 Hz" in the prose and "≈ 400 Hz" on the chart.** *This file says 400–500 Hz.*
