# C-ATS standard rooms — what this file is and what it is not

> **⚠ Two corrections from Neil, 2026-08-19, and neither is cosmetic.**
>
> **1. *"I don't know what that engine is. I suspect an old and useless idea. Cinema Tools Pro is the source for all
> this."*** *I ran `engines/modal_analysis/` **without checking what governs it** — the fifth time today I checked
> that something works rather than whether it is current. **On the evidence it is current**: `ADR 042` is `accepted`
> at **version 5**, revised 2026-08-16, its slug is `acoustic-treatment-placement-engine`, and it supersedes 43 and
> 47. **But the directory name says `modal_analysis`, which does not tell anyone it is the treatment placement
> engine** — which is plausibly why it is not recognised by name. *Cinema Tools Pro is the product; this is an engine
> inside it. **Neil's call either way; the ADR is the evidence, not my reading of it.***
>
> **2. *"Even then I need to tune the model a bit."*** **So no quantity from this engine is publishable yet, whatever
> its provenance.** *That is a firmer constraint than the missing finish schedule below, and it applies to any output,
> not just box counts.*
>
> **What survives both.** *The geometry is arithmetic. The reverberation target is the formula an accepted ADR
> mandates. **Nothing else in this file should be relied on until the model is tuned.***

**Generated 2026-08-19** by running `cinema-platform` `products/cinema-tools/engines/modal_analysis/`
(`acoustic_treatment.py`, `c_ats_panels.py`) at commit `0fb875f`. **The room dimensions are not invented** — every
value is drawn from the platform's own parameter space in `docs/validation/room-dimension-sweep/room_dim_sweep.csv`
(Lx 4–12 m, Ly 3–7 m, Lz 2.4/2.5/2.7/3.0/3.5 m, 195 distinct rooms).

## What it contains

**Geometry and reverberation targets only.** Volume, wall area, ceiling-plus-floor area, total surface, and three
target reverberation times per room.

## What it does not contain, and why

**No box counts, and none can honestly be added from here.** *The chain from a room to a panel quantity needs a
**finish schedule** — what every surface is actually made of. The engine reads that from a design document's
build-ups and finishes, and its own code warns what happens when that is faked:* **"a design whose finishes were
captured through the finish picker silently fell back to the absorptive market defaults — the RT allocator then
sized treatment for a room that did not exist."** *Inventing a palette to produce a number would be exactly that
failure, and exactly the one `../../method.md` § "The four that failed on 2026-08-19" describes.*

**So this file is the geometry half. The missing input is nameable, not mysterious: a stated finish schedule per
standard room.** *That is a decision — carpet or hard floor, plasterboard or fabric walls — not a calculation, and
the grades already imply it (the design rules: **"Gold flips the floor to a wood walkway"**).*

## ⚠ Three columns, and the one named after C-ATS is the legacy target

| Column | What it is |
|---|---|
| `reverberation_target_s` | **The correct target, and now confirmed by an accepted ADR rather than by my reading.** **`ADR 042` §8:** *"A room is designed to ONE volume-scaled reverberation target, `Tm = 0.3·(V/100)^(1/3)`… the target is the design's, and **the engine names it so: `reverberation_target_s`, not the document it came from**."* *I first computed this column by hand and did not use the function the ADR names. **Regenerated from `at.reverberation_target_s(V)`; it matches the hand figure exactly at every volume.*** |
| `legacy_cats_target_s` | **The legacy CATS target** — `cats_target_s()`, which computes **Rettinger × 0.85** (ratio verified 0.850 at every volume). **Kept in the file as a warning, not as an option** |

**This is a trap worth naming, and the ADR closes it.** *A function called `cats_target_s` is what anyone building a
C-ATS table would reach for by name — and it returns the **legacy** figure. **`ADR 042` §8 names the correct one
outright**, and the naming is deliberate in a second way: it is called `reverberation_target_s` **rather than after
RP22**, because the target is the design's and RP22 only grades it — which is `../../registers/premises.md` `PR-15`
implemented in a function name.* The design rules already flag the divergence: they give
the volume-scaled formula as **"the formula"** and note **"cf. the legacy CATS Rettinger×0.85 ≈ 0.327 s at
105 m³"**, which this run reproduces exactly.* **The two diverge in both directions:** *the legacy target is
**looser** in small rooms (0.256 vs 0.198 s at 28.8 m³) and **tighter** in large ones (0.384 vs 0.430 s at
294 m³).* **A table built on the wrong column would under-treat small rooms and over-treat large ones.**

## Reproducing it

*Run against a `cinema-platform` clone; `sys.path` must include `engines/modal_analysis/`. The two target functions
are `at.cats_target_s(V)` and `at.rettinger_target_s(V)`; the volume-scaled figure is arithmetic. Box arithmetic is
`c_ats_panels.boxes_for_area(m2)` — **verified: 1.44 m² → 1 box, 10 m² → 7 boxes**, rounding up as the rules
require.*
