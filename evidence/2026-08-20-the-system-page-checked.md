# The C-ATS "system" page, checked against the record — 2026-08-20

> **⚠⚠ THIS FILE WAS SUBSTANTIALLY WRONG AND IS CORRECTED BELOW — read the correction first.**
> *Two things came out after it was written. **(1) Neil: "the website you just analysed has been auto generated
> based on answers in this repo."** So it is not a mockup someone wrote — **it is an output of this method**, and
> every divergence is a repo or pipeline question, never a copywriting one. **(2) I had audited one page as if it
> were the site.** *There are five: `/`, `/the-system/`, `/products/`, `/technical-information/`,
> `/start-your-project/`.* **The technical page answers almost everything flagged below**, including the one thing I
> called a defect. **See `2026-08-20-the-site-is-an-output-correction.md` — the findings there supersede §3, §5 and
> §7 of this file, and narrow §4.*** **What survives: §1, §2, §6.**

*`https://cats-98x.pages.dev/the-system/`, supplied by Neil. **Fetched and read as raw HTML**, not through a summary
— `../method.md`: a summary is not a source.*

> **The page is far further along than this repo's own note about it.** *`PR-18` records the C-ATS site as *"an
> in-play mockup pending this process being complete and learned from."* **This page has already absorbed much of
> that process** — including the **43 mm** resonance depth Neil corrected on 2026-08-19, which means it is current to
> within a day. **The stale description is the repo's, not the site's.**

---

## 1 · What it gets right, and worth recording as such

**Every hard guardrail holds.** *No price anywhere · trade-only stated outright (*"C-ATS panels are supplied to
trade"*) · **no competitor named** · the category criticised rather than a rival (*"rooms are not improved by adding
absorption until everything sounds dead"*), which is exactly what `Q64` permits in public · **the word "diffusion"
never appears**, and the reflection panel is described by what it does rather than by a mechanism (`C5.15`).*

**And two lines do work this repo spent days arriving at.** *"**Send the room, not a parts list**" is `C6.20` and
`Q68` in five words. And "**Depth is the constraint, and it is the point**" carries Neil's own framing — depth as a
design goal, with the floor-area argument attached.*

**One incidental confirmation for `DAT-1`.** *The page states **50 mm** for reflection and reverberation and
**43 mm** for resonance — **correctly**. So the wrong depth is confined to the canonical dataset
(`panels.json` carries 50 mm for RES-CP); **the public-facing side is already right**, which narrows `DAT-1` to a
data fix with no content consequence.*

## 2 · The finding: `DR-Q52` is being answered by publication

**`operations/decision-request-q52-cats-rules-publication.md` status: *raised — no decision made*.** *Meanwhile
**five items from its own "proposed publishable" column are live on this page**:*

| `DR-Q52` proposed publishable | On the page |
|---|---|
| **Per-axis flatness** in place of one overall RT60 | *"the same decay on every axis: length, width and height"* |
| **The over-damping guard** | *"rooms are not improved by adding absorption until everything sounds dead"*; *"the goal is not simply less of it"* |
| **Corner-straddle placement; the ceiling-corner lever** | *"corner loaded, **including ceiling corners**, because that is where modal pressure is highest"* |
| **That reflections are triaged, not all treated** | *"placed where reflections actually land… each panel facing a gap"* |
| **Worked results — room, grade, box count** | *"each layout shows a panel package and where it goes for a room of that size"* |

**And nothing from the "proposed not" column appears** — *no scoring weights, no budget formula, no placement
algorithm, no material catalogue, nothing sufficient to reproduce a design without the engine.*

> **So the decision has been taken in practice, and it landed exactly where the request proposed.** *That is a good
> outcome and it is worth saying plainly: **`DR-Q52`'s publishable/proprietary line is validated by the page rather
> than contradicted by it.*** **Two consequences.** *(1) **`T4` is gated on `DR-Q52` and should probably be
> ungated** — the corner material it was waiting for is now public. (2) The DR can likely be **closed as confirmed
> in practice**, which is Neil's call, not this repo's. *Note it is not a violation: nothing was decided against.*

## 3 · Two things the page promises that do not exist yet

**This is `../CLAUDE.md`'s named failure mode — *build it, then say it* — and it is the only real risk on the page.**

| The promise | The state |
|---|---|
| **"Start from a designed reference room. Each layout shows a panel package and where it goes for a room of that size, so the shape of the answer is visible before a design is commissioned."** | **`EST-7` is half done.** *The geometry exists — eight rooms from the platform's own 195-room sweep — but **there is no finish schedule per room**, the model **needs tuning** (Neil, 2026-08-19), and **there is exactly one worked room**. So the layouts the page promises are not published and cannot be yet* |
| **"03 Verify — once the room is built, its performance can be measured on site, so the targets the design set can be shown to have been met."** | **`P7`: verification is a capability, not an offer.** *`C3.4`/`C4.5` record it as something we can do; **it is not priced, not in a service ladder and not sold**. The page makes it step 3 of how a project runs* |

**Neither is untrue — both are things we can do.** *The gap is that a dealer arriving at step 01 finds nothing to
start from, and a dealer reaching step 03 finds nothing to buy.* **`EST-7` and `P7` were backlog items; the page
makes them commitments.**

## 4 · One factual discrepancy to resolve — and not by assertion

**The page and the product record disagree about which panel is checkerboarded.**

- **Page, on Reflection:** *"placed where reflections actually land, **in a checkerboard layout**, mirrored side to
  side, with each panel facing a gap."*
- **`product-records.md`, on Reflection:** *"first-reflection points — side walls between screen and prime seat,
  rear wall behind the heads, ceiling"* — **no checkerboard.**
- **`product-records.md`, on Reverberation:** *"broad wall and ceiling coverage, **checkerboarded toward the rear**;
  around surround speakers."*
- **Page, on Reverberation:** *"positioned around loudspeakers to guard against comb filtering as well as decay"* —
  **the checkerboard is gone.**

**So checkerboarding has moved from the reverberation panel to the reflection panel. One of the two is wrong.**
*The design rules live in `cinema-platform`, so **this resolves against the platform, not by picking a side here.***
**And it has a consequence downstream:** *`brands/c-ats/draft-answers.md` answers `N3` question 10 — *"checkerboard
or continuous?"* — **against the reverberation panel**. If the page is right, that answer is aimed at the wrong
product.*

## 5 · The one thing I would call a defect

**The test-basis block omits the mounting condition.**

*The page states: BS EN ISO 354 · BSRIA independent test house · 210 m³ reverberation chamber · tested 2019,
reported 2020, published in full · 6 octave bands, 125 Hz–4 kHz · 5 published coefficient sheets, one per panel,
plus a boundary condition.* **All good, and more provenance than the record itself holds — but the record is
emphatic about one caveat that must travel with the figures:**

> *`product-records.md`, **Test basis**: "BSRIA, BS EN ISO 354:2003, **free/unfixed mounting — design-stage
> reference figures, not installed-effective values**."* **And `Q46` (Neil): in the lab *"they literally just lay
> them loose on the floor, which is not reality in any case"* — the modelling default is the **glued** series.**

**So a specifier can download five coefficient sheets and apply them as installed values.** *That is the exact
failure the record exists to prevent, and it is one sentence to fix.* **The published chart already plots
Reflection A and B**, so the honest version is available without adding any new claim.

## 6 · One unsourced claim about the category

> *"Acoustic treatment normally costs a room **100 mm to 200 mm or more** on every treated wall."*

**`Q64` binds this: *"the measurement test applies to what we say about others exactly as it does to what we say
about ourselves — no unmeasured claim about a rival, gated or not."*** *The claim is almost certainly true and is
**cheap to source** — competitor panel depths are published dimensions — but **this repo has no record of it**, so
right now it is an assertion about the category with nothing behind it.* **Either source it or soften it to the
comparison the page can already prove: our own depths, stated plainly.**

## 7 · Where the page under-sells, and it is the layer that comes first

**The isolation section is correct and well written** — *"isolation does not determine treatment performance, it
provides the conditions in which treatment behaves predictably… where a room needs both, they are specified
separately."* **It draws the product boundary exactly as the record does.**

**But it never says we do it.** *`Q79` (Neil, 2026-08-19): **isolation has always been sold**, it fits no other
brand, and **it belongs under C-ATS** because it is the acoustic consultant's work. There is a **Sound Isolation**
store category of ten items and a **six-step service ladder** — discovery, design, drawings, details, BOM, build
guide.* **And `C1.40` puts isolation **first** in the project: it sets the room's structural dimensions and travels
with the architectural design.**

> **So the page hands the earliest and highest-value layer to somebody else, in a section explaining why it
> matters.** *That is `P2` — isolation is a sold layer with no plan — now with a page attached. **Not an error on
> the page; a gap in what the page was given to say.***

## 8 · A voice note, not an error

*"In **a cinema or a listening room** that floor area is worth more than the treatment."* — **`../CLAUDE.md` says
name the problem, never the room type**, while also saying **lead with cinema credibility**. *This leads with
cinema, which is permitted; it is worth a look only because the same sentence works without the room types and would
then travel to every other room the system suits.*

## What to do, in order

1. **Fix the mounting caveat** (§5) — *one sentence, and it is the only defect.*
2. **Resolve the checkerboard question against the platform** (§4), then correct whichever of page or record is
   wrong — *and `draft-answers.md` with it.*
3. **Source or soften the 100–200 mm claim** (§6).
4. **Decide `DR-Q52`** (§2) — *it has been answered in practice; closing it un-gates `T4`.*
5. **Then the two promises** (§3): *`EST-7`'s finish schedules and tuning, and whether verification becomes a real
   offer (`P7`).*
6. **And give the page the isolation half** (§7), once `P2` has a plan behind it.
