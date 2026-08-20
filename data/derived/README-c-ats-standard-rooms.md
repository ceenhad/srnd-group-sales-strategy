# C-ATS standard rooms — what this file is and what it is not

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
| `target_rt_volume_scaled_s` | **The current target** — `0.3 × (V/100)^⅓`, the volume-scaled formula the platform's own acoustic-target reference transcribes |
| `target_rt_legacy_cats_s` | **The legacy CATS target** — the engine's `cats_target_s()`, which computes **Rettinger × 0.85** (verified: the ratio is 0.850 at every volume tested) |
| `rettinger_s` | Rettinger, unscaled, for reference |

**This is a trap worth naming.** *A function called `cats_target_s` is what anyone building a C-ATS table would
reach for by name — and it returns the **legacy** figure. The design rules already flag the divergence: they give
the volume-scaled formula as **"the formula"** and note **"cf. the legacy CATS Rettinger×0.85 ≈ 0.327 s at
105 m³"**, which this run reproduces exactly.* **The two diverge in both directions:** *the legacy target is
**looser** in small rooms (0.256 vs 0.198 s at 28.8 m³) and **tighter** in large ones (0.384 vs 0.430 s at
294 m³).* **A table built on the wrong column would under-treat small rooms and over-treat large ones.**

## Reproducing it

*Run against a `cinema-platform` clone; `sys.path` must include `engines/modal_analysis/`. The two target functions
are `at.cats_target_s(V)` and `at.rettinger_target_s(V)`; the volume-scaled figure is arithmetic. Box arithmetic is
`c_ats_panels.boxes_for_area(m2)` — **verified: 1.44 m² → 1 box, 10 m² → 7 boxes**, rounding up as the rules
require.*
