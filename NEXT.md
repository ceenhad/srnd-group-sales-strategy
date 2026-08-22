# NEXT — handover

*Updated 2026-08-21, after PR #30 merged to `main`. **Next focus: Pro-Fi, in a local session.***

---

## Where things stand

**The C-ATS phase is closed.** *PR #30 merged — 92 files, +10,127 / −2,603, 152 commits. Every C-ATS question is
answered; nothing in that brand is waiting on an owner.*

**Two registers now hold the results, and the distinction between them does work.**

| | Holds |
|---|---|
| `decided.md` | `D-01`–`D-13`. Choices the business acts on — id, decision, kind, scope, the question that produced it, the owner's words verbatim, what is done differently |
| `established.md` | `E-01`–`E-18`. Settled facts — `basis` · `source` · `rests on`. A fact does not need approval to be true, but it needs it to be relied on |

*Both approved as a set: `https://claude.ai/code/artifact/80b5a86a-a58d-460f-8f38-183f706dc742`. Anything added later
enters the same way — put to Neil, reviewed, approved.*

**What is left of C-ATS needs other people.** *`DOC-42` the Class 0 certificate from the supplier · `DAT-3`/`DOC-7` the
EN 13501-1 classification · `DOC-17` blocked on `CON-3` · `KNW-18` and `ENG-28` flagged to Cinema Tools · `ENG-20` and
`ENG-27` specs to hand to the dev team · `EDU-7` when the sweep reaches it. **Nothing there is a producer task.***

---

## Pro-Fi — start here

**Read `brands/_template/the-brand-run.md` § The precondition before anything else.** *It is four rules and every one
of them was learned by breaking it on C-ATS.*

### The state, honestly

*Four files exist: `README.md`, `brand-data.md`, `opportunity.md`, `positioning.md`. **No `product-records.md`, no
`claims.md`, no pathways, no hooks, no segments, no training.** So this is a run from the start, not a continuation.*

**Five record scopes, none filled** (`registers/product-register.md` § Pro-Fi):

`PF-01` Spatial — BMR satellites, dot / dash / cube · `PF-02` Cinema — 2-way LCR, Reference coax point-source ·
`PF-03` Modular — stackable line-array blocks · `PF-04` Stage — BMR 2-way LCR · `PF-05` LFE — sealed subs 5 / 8 / 12 /
15, plus infra_21.

**Three things about that table matter more than its emptiness.**

- **Every `G3` is `[?]`** — nobody can currently say per product whether it is `pre-release` or `current`, because the
  store listing is gated on range and platform readiness (`BR-7`). **So no Pro-Fi product may generate public material
  until that is answered.** The gate is doing its job; do not work around it.
- **The amplifiers have no row and are a real product line.** A named gap.
- **The public site and the engineered range do not describe the same brand.** `pro-fi.uk` is thin and out of date; the
  live three-way split is shop structure, not record structure. **The gap between them is the work** — and per
  `../CLAUDE.md`, establish what that surface *is* before treating anything on it as evidence or a defect.

### The precondition applies doubly here, and this is the one instruction to take seriously

**Check `cinema-platform` before recording anything as missing.** *On the C-ATS run the single most important answer in
the brand — how many panels a room needs — was fully systemised in the platform while the brand's own record said it
was written down nowhere. That is `PR-20`, and it has now broken four times.*

**For an audio brand the odds are worse, because the platform visibly already does loudspeaker work.** *Cinema Tools'
own reports carry speaker layout analysis, per-seat reflection tracing across seventeen loudspeakers, bass headroom
and **bass system architecture**. `products/cinema-tools/engines/modal_analysis/` holds the reflection solver and
threshold modules.* **Assume Pro-Fi's selection logic, sizing and system rules already exist there. Look before
writing a single `[?]`.**

### Then, in order

1. **Fill the product record** — `registers/record-form.md` is the form, `brands/c-ats/product-records.md` the worked
   example. All three legs read from it; a run against an empty record produces invention.
2. **Drill `positioning.md` into rows** before building on it. *Confirmation means a name and a date. Note that Pro-Fi's
   §5 is where the **Scandinavian register** came from — the group-wide voice principle — so this file has already
   given the group something, and it deserves the same care C-ATS's got.*
3. **Then Legs 1–4** — one pathway per door, the hook set, the segment cut, the training opportunities.

---

## How to work, distilled from eight recorded failures

*Full list in `method.md` § Not getting into this mess again. These are the ones that cost most.*

- **A shared link is context, not a work order.** *Ask what is wanted before auditing anything.*
- **Establish what a surface is before treating it as evidence.** *Published offer, legacy remnant, or mock-up — they
  behave in opposite ways. Recorded in `../CLAUDE.md` with a status board and a flip condition.*
- **A flag saying *confirm current spec* means the claim cannot be built on until it is confirmed.** *An unconfirmed
  source is unusable, not usable-with-a-caveat. A 2015 brochure decode became the record's most-cited advantage and
  reached a published page.*
- **Reading the platform is not the same as building on it.** *Check whether an artefact is locked before any of it
  leaves the evidence file.*
- **One question per box, and a partial answer gets asked again rather than logged.** *Watch for the word "and".*
- **Before listing work as yours, name the mechanism by which it lands.** *"Apply at source" was a queue item that
  could not be performed.*
- **Write the test, not the list.** *A rule derived from today's state needs the condition under which it stops being
  true written next to it.*
- **Heaviness is not relevance.** *Filter questions by the active phase first, weight second.*

**Run `python3 tools/check.py` before every commit.** *It enforces the mechanical invariants and has caught defects
every time it was skipped.*

---

## Standing constraints — verbatim force

*Never publish pricing, partner or end-user, anywhere. Never name material suppliers, manufacturing partners or OEM
relationships in public content — the reason is commercial (`D-06`). Never invent figures, test results,
certifications, personas or launch dates. Do not override a brand's own `CLAUDE.md` from the group layer. This repo
does not write into `cinema-platform`, into engine, or into `c-ats-shopify` — it specs and hands over. Scattering never
diffusion on a product name. No competitor named on a public page.*

---

## Also queued, not Pro-Fi

**Parked deliberately:** *the AVForums brief (`group-strategy/avforums-brief.md`) until B2C is the active lane; CPD
accreditation until the full six-brand sweep completes and a training list exists (`D-09`).*

**Group-level and open:** *`Q39` is Ben still involved · `Q40` what is `srnd-os` · `Q43`/`Q44` two ADR decisions
belonging to `cinema-platform`'s owner · `Q38` commercialising Probata · `FACT-5` the targets table · the partner
programme's four.*

**One structural note.** *`brands/_template/the-brand-run.md` is what every remaining brand inherits, and the C-ATS run
changed what it should say. Its § "Four findings about the method" is worth re-reading against what actually happened
before Pro-Fi repeats it.*
