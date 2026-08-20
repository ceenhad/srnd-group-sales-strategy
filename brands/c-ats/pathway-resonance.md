# C-ATS — the resonance pathway (the third door)

*The third and last C-ATS door, on the same eight slots (`pathway-reverberation.md`, `pathway-reflection.md`;
S22, `../../motion/motion-design.md`). The dealer whose client's room has bass in one seat and none in the next —
room resonance — and the panel that answers it, the **RES-CP**. Drafted for correction.*

**Read this door differently from the other two.** Doors 1 and 2 assemble from material inside the brand folder.
**This one does not — its central answer lives in another product.** *How many do I need* is answered, systemised
and running, but it sits in Cinema Tools rather than in anything C-ATS publishes. So this pathway is still
assembly; **the material is just somewhere the brand run would not have looked** (corrected 2026-08-18 — see the
gap section below, and `../../registers/questions.md` Q52).

> **⚠ The state of every slot now lives in `pathways.md`** (`MTH-1`, 2026-08-19). *This file was prose-with-tables,
> the shape `PR-9` broke; the register is the authoritative form and the slot table below is superseded by it.*
> **Two things changed that this file predates:** entry is keyed to the **three project moments** `M1`–`M3`, not to a
> symptom (`PR-14` broken, `PR-7` broken on its own falsifier, `claims.md` `C2.24`–`C2.26`); and **slot 4 confirms
> rather than proves** (`PR-4` — *"if it's not legal or safety no one gives a shit"*). **What is kept here is the
> per-door argument, which rows cannot hold.**

## The door

The problem, in the dealer's words: **`[?]`** (`product-records.md` `O1` — **unasked, not blocked**).
Ours, and not a dealer's: *"below roughly 200 Hz the room stops behaving like a room and starts behaving like an
instrument"* (`copy.md`).

The product: the RES-CP — 600 × 600 × 50 mm, 4 to a box. It is the largest panel, its effectiveness depends on
corner placement, and its quantity is the one nobody can currently state.

**It is not the range's lead product, and neither is any other panel** (Neil, 2026-08-18,
`../../registers/questions.md` Q50): *"C-ATS is an acoustic treatment system… it's not that one panel is more or
less important. The 3 Rs of acoustics is what defines the product."* **The system is the product; a door is a way
in to it, not a rank.** So `O5` and DEC-3 — entry product versus flagship — do not apply to C-ATS, and the
record's earlier "candidate flagship" line was inference, now struck.

## The pathway, slot by slot

| # | Gateway | The piece | Its one job | State today | The handoff |
|---|---|---|---|---|---|
| 1 | **G1** — the hook set | The resonance hooks (`hooks.md`, door 3) | Get a bite: the problem most rooms never solve, named | **Nothing live for this door.** The 3 Rs explainer set names resonance; no resonance-specific hook exists | Every hook → the fuller answer (slot 2) |
| 2 | **G1→G2** | The room-modes answer — why bass is uneven seat to seat, why it is a pressure problem and not an EQ problem, what corner loading does | Answer the question fully; open the proposition | **`[?]` — inventory it.** The staged knowledge base covers absorbers/diffusers/bass as a pillar; whether it answers *this* question at this depth is unverified (`content-plan.md` items 3–20) | → the 3 Rs proposition (slot 3) |
| 3 | **G2** — proposition | The 3 Rs block and the RES-CP on-ramp; and **the depth argument made concrete** — corner loading is what lets 50 mm do work that would otherwise need far greater depth (`copy.md`, `product-records.md` `O4`) | "This could work for me" | **Written, ready to paste** (`copy.md`); absent from the live homepage | → the proof (slot 4) |
| 4 | **G2→G3** — proof | The measured per-panel absorption area from **BSRIA test 4 — three panels in corners against two walls, the configuration it is actually used in** — with the configuration stated on the face of it | Remove the doubt the whole depth argument exists to answer: *can 50 mm do anything at low frequency?* This product cannot be sold on description, and here the data does the work outright | **Published but buried** (EST-5). **And carrying two live traps** — see below | → register to see pricing; a Zoom (slot 5) |
| 5 | **G3** — the hinge | Registration — **the same single hinge as the other two doors**, not a third copy of it | Make the gate worth crossing | Mechanism live in engine; grants only pricing today | → the store (slot 6) |
| 6 | **G4** — first order | The RES-CP listing on `srnd.store` | Take the order faultlessly | **Mockup, not a defect** (`PR-18`, 2026-08-19 — the site is an in-play mockup pending this process, so its state is not evidence). Listing exists; the **£0.00 "Sale price" presentation is broken** (EST-4). **And the order cannot currently be sized** — see slot 2's gap | Order confirmation → the install material (slot 7) |
| 7 | **G5** — first job | The corner-placement instruction page and its recording — **the third predictable question, and the only one of the three with no written answer** (`content-plan.md` item 37; DOC-2) | Prevent the known site failure: panels placed away from corners, where the device is much weaker | **Missing.** The other two panels' one-pagers are written; this one has never been drafted | → the verification offer; then slot 8 |
| 8 | **G6** — adjacency, the loop | Concealment behind fabric, as with every panel — **and the timing argument, which is strongest here**: the treatment sits behind the wall, so it must be decided *before the wall is built* (`product-records.md` `N6`) | Open the next layer at the moment it is relevant | Concealment article **staged**; adjacency page not written (`content-plan.md` item 45) | → **Fabric Walls stage 2** |

## The two traps in slot 4

Both are in `product-records.md` and neither is published, so anyone assembling this slot from the raw data will
get it wrong:

1. **The published surface coefficient in `panels.json` comes from BSRIA test 8**, a plane absorber in the centre
   of the room — **explicitly not the intended configuration.** Test 4 is. Quoting the wrong test understates a
   product whose whole case is that it works in corners.
2. **The test 4 figures already embody corner loading**, so a design tool must not also apply a corner factor —
   that double-counts. **This caveat currently lives in a JSON comment** and belongs in the published data note.

Neither is a content decision. Both are one line each in the place the numbers are published, and until they are
made this slot cannot be assembled safely.

## *How many do I need* — corrected 2026-08-18

**An earlier draft of this file said the quantity answer "is not written down anywhere" and called it the biggest
content gap C-ATS has. That was wrong, and it was wrong because I read `product-records.md` `N1` instead of
checking the platform** — which `../../CLAUDE.md` requires in as many words. Neil: *"how many panels — please see
Cinema Tools Pro."*

**What actually exists**, in `cinema-platform` `products/cinema-tools/`:

- **`docs/product/c-ats-system-design-rules.md`** — the C-ATS design method, systemised with Neil in 2026-06.
  A five-step design hierarchy; **per-axis Fitzroy flatness rather than one overall RT60**, with an over-damping
  guard; surface-palette matching as the foundation; the wall-on-isolation-mounts as structural LF treatment;
  reflection triage by ETC score against a **binding** budget; install-type A/B effects; **RES straddling the
  corner across both adjoining walls**, and ceiling corners as the height-axis lever; and the 1.44 m² box quantum.
- **The engine that implements it** — `engines/modal_analysis/treatment_systems.cats_system()` and
  `acoustic_treatment.py`, sizing in whole boxes off the BSRIA catalogue, carrying the REF A/B install choice and
  the RES corner Sabines without re-typing a single figure.
- **A worked reference** — Joppa Road, 7.05 × 4.95 × 2.6 m, 7.1.4, 7 seats: **Gold on carpet = 11 boxes,
  REF 6 + REV 1 + RES 4**, per-axis x 0.35 / y 0.20 / z 0.11; the wood-walkway variant flattens z to 0.30.
- ~~**A designed route to a dealer** — Tier-0, free: room + format + finishes + grade → boxes → trade basket~~
  **STRUCK same day.** That two-tier product is described in a document predating **ADR 017 v2 (accepted
  2026-08-13)**, whose decision 5 **withdraws Level 2 outright** — *"not a paid design environment, not a thin
  entry surface — withdrawn"* — and whose decision 4 makes **Cinema Tools Pro internal tooling with no external
  login**. **There is no self-serve design surface, and the one that was planned was cancelled.**

**So the honest state of this slot: the answer exists and there is no route from it to a dealer** — not a route
half-built, but a route withdrawn. Per ADR 017 §2 the engines' output is a paid deliverable; per §6 the only
public surfaces are the seven free Level 1 calculators. **Which of those C-ATS's sizing answer travels on is
undecided, and it is the substance of DR-Q52.**

**And the real open question is a boundary, not a gap.** `positioning.md` §1 promises *worked examples showing how
quantities are derived*; the platform black-boxes the methodology as IP. The design-rules document itself
separates them — the rules *"deliver a good result with minimal effort"* and the engine *"deepens the accuracy, it
does not replace the rules"* — so a rules layer can publish while the engine does not. **Where that line falls is
`../../registers/questions.md` Q52, and it gates this slot, `N1`/`N2`, and six candidate hooks.**

## The hook matrix — slot 1 is a set, not a piece

*Candidate angles, not copy; provenance and rejections in `hooks.md`. All hand to slot 2.*

| Appeal | Candidate hook angle | The substance behind it |
|---|---|---|
| **The problem named** | Bass that is heavy in one seat and gone in the next | `R1`, `D4` — room modes, the problem most rooms never solve |
| **Better results** | The problem no amount of processing fixes, because it is pressure and not response | `D3` — absorbs where modal pressure is highest |
| **Easier to do** | Corner loading, so 50 mm does what depth normally has to | `O4` — the depth argument made concrete |
| **The problem named** *(second angle)* | Measured in corners, which is how it is actually installed — not on a flat wall | BSRIA test 4, and the trap above |
| **More revenue** | The room problem a client can hear and cannot name — worth being the one who solves it | `R1` |

**Not a hook, on this door specifically:** corner placement, screw specification, and the too-few-for-the-volume
failure. All three are stage-5 support for someone fitting, and the second and third insinuate the dealer can't
(`../../motion/motion-design.md`, the hook test and B6).

## What writing it down shows

- **The template holds for a third time, and the third one is where it earns its keep.** Same eight slots. What
  changed is not the shape but the *state* — and because the shape is fixed, the emptiness is visible as
  particular slots rather than as a general sense that resonance is under-served.
- **Measured strength and pathway readiness are independent.** This door has a complete measured case behind it
  and is simultaneously the only one with a missing install one-pager, an unverified stage-2 answer, and a proof
  asset carrying two unpublished traps. **How well a problem is understood says nothing about how well it is
  served** — which is not visible until three doors are laid out the same way.
- **The single hinge is now confirmed by repetition.** Slot 5 is identical across all three doors. **A brand has
  one G3 piece, not one per door** — worth stating in the template before another brand writes three.
- **DEC-3 does not apply here.** Q50 dissolved it for C-ATS: no entry product, no flagship, one system.
- **The register items this pathway consumes:** EST-5, EST-4, DOC-2, and publication of the staged KB.
  **What it additionally needs authored, and cannot borrow:** the corner-placement one-pager
  (`content-plan.md` item 37) and the two data-note corrections above. ~~`N1`/`N2` — the quantity answer and the
  worked example~~ **struck: both exist in the platform.** What they need is a publication boundary (Q52) and a
  surface, not authoring.

## Guardrails (brand truth binds, hardest here)

**No modal-region figure below 125 Hz** — the BSRIA report does not extend there and the design tool is blind
below ~80 Hz, so no resonance numbers come from that tool (`product-records.md` `N9`). Treatment is not isolation,
and the two are never presented as substitutes. Panels named by problem, never mechanism. **C-ATS**, never the
expansion. Every configuration figure states the test it came from. The dealer's phrasing in "the door" stays
flagged until the archive supplies it.
