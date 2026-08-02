# C-ATS product records — the sales and marketing layer, filled

*The schema in `../../product-data-schema.md`, on the form in `../../product-record-template.md`, applied to the
three C-ATS treatment panels. First worked example, so it sets the standard for the rest of the group. Field IDs
below (`D1`, `O2`, `R4`…) are the form's; they are what downstream generation refers to.*

**Where the three panels stand: 24 of 30 fields each · assets 2 of 11 known · `G3` current.**

The six unfilled fields are the same six on all three, which is itself the finding — **they are not per-product
gaps, they are one missing input** (`O1`, `O3`, `W2`) and one unmade decision (`O5`), plus record ownership. See
"what is still missing, and why it is the same six" at the end.

## Provenance — read this before using any figure

| Content | Source file |
|---|---|
| SKUs, dimensions, box rules, mounting specifications, absorption tables, test metadata, data gaps | `c-ats-shopify:data/panels.json` |
| Materials (ABS, foam), ~500 Hz, Class 0, layout rules, 30 % height rule, ~300 mm tolerance, RES-CP as a 2019 addition | `c-ats-shopify:data/c-ats-pack-rules-2026.md` (a decode of the 2015 pack brochure — **legacy, confirm current spec**) |
| Class 0 / EN 13501-1 / IMO SOLAS and the certificate caveat | `c-ats-shopify:content/article-fire-ratings.html` |
| Range, discontinued items, marine scope, services, tooling separation | `brands/c-ats/brand-data.md`, `measured-acoustics.md`, `product-pricing.md` |
| Wording guardrails | the C-ATS `CLAUDE.md` |

**Test basis:** BSRIA Report 100241/1, BS EN ISO 354:2003, BSRIA Bracknell, 210 m³ chamber, tested 24 July 2019,
reported 3 March 2020, **free/unfixed mounting** — design-stage reference, not installed-effective.

> **Two provenance warnings, and the first one is a correction to an earlier draft of this file.**
>
> 1. **`panels.json` is marked "DRAFT — generated from BSRIA data; pending review."** Nothing here should reach a
>    datasheet before that review happens.
> 2. **Not every figure in it is BSRIA.** The REF-CP default surface coefficient is sourced from the **legacy CATS
>    Calculator (catalogue entry 3084)**, not from the report — an earlier version of this file wrongly attributed
>    it to BSRIA. Both figures are given below, labelled. **This is precisely the failure the record exists to
>    prevent**, and it happened on the first attempt, which is the strongest argument for the exercise.

**Two things this exercise proved immediately, which is the argument for doing it:**

1. **It found a real and expensive gap** — the REF-CP performs differently depending on how it is fixed, and the
   *recommended* method deliberately gives **less** absorption. An installer who screws it without bonding gets
   acoustics the design did not assume. That belongs in the manual in bold and currently isn't prominent anywhere.
2. **It caught a wording violation in our own source data.** The legacy pack brochure calls the REF-CP a "faceted
   ABS diffuser." We do not claim diffusion. The record is where that gets fixed once rather than caught
   repeatedly.

---

## Shared across all three panels

*Documenting the common layer once — the mechanism-not-SKU principle in practice.*

| Field | Value |
|---|---|
| **What they are, collectively** | A three-panel acoustic treatment system, one panel per acoustic problem — reflection, resonance, reverberation |
| **Depth** | **50 mm** on all three. The commercial argument is space: at this tier the floor area a deeper system consumes costs far more than the treatment itself |
| **Box rule** | Every box covers **1.44 m²**. Quantities round **up** to whole boxes — a dealer buys full boxes |
| **Layout tolerance** | Panels may move **~300 mm** from the designed position without material performance impact. Forgiving on site, and a genuine selling point that is nowhere in the marketing |
| **Where they sit** | Behind a stretch-fabric finish, concealed. Any fabric system works; Fabric Walls pairs well and is not a dependency |
| **Channel** | **Trade only — `srnd.store`.** No C-ATS on Cinema Store (`../../decided.md` C5) |
| **Test basis** | BSRIA, BS EN ISO 354:2003, **free/unfixed mounting** — design-stage reference figures, not installed-effective values |
| **Marketing status** | Current. REV-CP-12 is discontinued and must not be listed. The commercial cinema range is in development and must not be written up as shipping |
| **Who specifies** (`W1`) | The integrator, typically with our help. Acoustic consultants write pre-tender specs on larger projects and are **not** a non-audience — the product is optimised for the integrator, which is a different question from who influences specification |
| **Who signs off** (`W2`) | **`[?]` — deliberately parked.** Who signs off and what convinces them comes from real recent jobs in the owners' words, not personas or file archaeology (`positioning.md` §2, §7) |
| **Territory** (`C2`) | Direct to dealer globally through the store; distributor appointments are case-by-case exceptions. **The live constraint is distribution, not territory** — C-ATS is widely deployed and thinly distributed, which `positioning.md` §7 calls the headline problem |
| **Proof, and publishable?** (`G4`) | **Strong and unusually unencumbered.** The full BSRIA report is published as a public PDF with five per-panel coefficient sheets beside it — specifier-grade third-party proof, freely available (`../../NEXT.md` lane 8). Install photography is thin; the Cornflake IMAX private cinema is public and easy to find, though years old |
| **Record keeping** (`K1`–`K3`) | Owner **`[?]` — unassigned** · last reviewed **2026-08-02** · review interval **`[?]`** |

**Known data gaps, shared:** installed-effective (derated) values may exist in the legacy calculator and need
reconciling against the raw lab figures, with a decision on which are authoritative for quotes and design. **[?]**

---

## 1. Reflection Control Panel — `C-ATS-REF-CP`

### What it actually is

| Field | Value |
|---|---|
| **What it is** | A faceted, injection-moulded panel that redirects reflected sound away from the listening position |
| **What it does** | **Scatters** — redirects reflected energy off-axis. **It does not diffuse**, and the word is not to be used: diffusion has a specific meaning under ISO 17497 that this does not claim |
| **How it works** | Rigid faceted surface geometry, most active around **500 Hz**, breaking up the specular reflection from side walls, rear wall and ceiling |
| **What it is for** | First-reflection points — side walls between screen and prime seat, rear wall behind the heads, ceiling |
| **What it is *not* for** | Absorption. It is a reflector, and treating it as an absorber is the misapplication to guard against. Not a bass or reverberation solution |
| **Scope of supply** | 300 × 300 × 50 mm panel, 0.09 m² each; **16 per box = 1.44 m²**; 3 mm injection-moulded ABS; moulded countersunk fixing holes |
| **What it requires from others** | A flat substrate; **4 × 3.5 × 25 mm bugle-head black drywall screws** per panel; builder's adhesive if bonding (see below); a concealing fabric layer if the room is finished |
| **Configuration space** | One size. **Two install types, and they are acoustically different** |
| **Limits** | Lowest panel in a block should sit no higher than **30 % of room height** off the floor; rooms over 3 m tall need proportionally more |

### Performance — and the two sources do not agree

Surface absorption coefficient by octave band:

| Source | 125 Hz | 250 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz |
|---|---|---|---|---|---|---|
| **Legacy CATS Calculator** (entry 3084; the current default in `panels.json`, Type A glued) | 0.01 | 0.08 | 0.28 | 0.11 | 0.01 | 0.06 |
| **BSRIA test 6** — plane absorber, 16 tiles, 1.44 m², centre of room (the intended-use configuration) | 0.01 | 0.20 | 0.54 | 0.12 | 0.04 | 0.09 |

**Resolved, and there was no disagreement.** The published absorption chart for the REF-CP plots **two curves,
labelled "Reflection A" and "Reflection B"** — so the install-type distinction has been public for years. The two
figures are **the two install types, not two versions of one number**: A is the glued, damped case (the lower set);
B is free/unfixed, which is what BSRIA measured (the higher set).

**Authoritative source: the absorption coefficient sheets published on `c-ats.co.uk`** — the numbers that have
been out for years. Everything downstream cites those. *One check still outstanding: the chart is a vector plot, so
the exact plotted values could not be read from the file. Confirm the A and B series against the chart before they
go into a datasheet table.*

Either way the values are deliberately low, and that is the point — this is a scatterer, not an absorber.

### The install trap — the most important thing in this record

- **Type A, adhesive-bonded (recommended, and the default in the data):** the adhesive bonds the panel centre and
  **damps its resonance**, so it absorbs less and works as a clean scatterer.
- **Type B, screw-only:** the panel is free to resonate, adding an absorption peak. **Higher absorption, which is
  not what the design assumed.**

**Why it matters commercially:** an installer following instinct will screw it and skip the glue. The room then
behaves differently from the design, and the fault will be attributed to the product or to us. **This is a
one-page manual fix and a sixty-second video**, and it is the single highest-return piece of documentation in the
C-ATS range.

### Why to buy it — the on-ramp

| ID | Field | Value |
|---|---|---|
| `O1` | Problem, in the dealer's words | **`[?]`** — drafted phrasing exists in `copy.md` (*"the sound arriving off the side walls competes with the sound from the speakers; detail smears"*), but **it is ours, not a dealer's.** Buyer-truth is parked until it comes from real jobs |
| `O2` | Time or labour saved | **The ~300 mm layout tolerance** — panels can move that far from the designed position without material performance impact, so the install does not need set-out precision. Plus whole-box quantities (1.44 m²) making take-off arithmetic trivial. **Neither appears in any marketing** |
| `O3` | Opportunity it opens | **`[?]`** — not established at product level. The group-level answer exists (acoustics is a strong way in, `positioning.md` §6); what job this panel helps a dealer *win* does not |
| `O4` | What it replaces or avoids | Deeper competing scatterers that cost floor area; commodity foam used at reflection points, which is the wrong device for the problem; and doing nothing, which is the commonest alternative. C-ATS exists because competitors were awkward to handle, awkward to cut on site, supplied in unsuitable volumes, and too deep (`positioning.md` §1) |
| `O5` | Entry or flagship | **`[?]`** — the entry product per brand is an open decision (`../../backlog.md` DEC-3) |

### The doubt it removes, and the questions it generates

| ID | Field | Value |
|---|---|---|
| `R1` | **The doubt it meets** | *"Will this actually change what I hear, or is it a decorative panel?"* — and, from consultants, *"is this a real acoustic device?"* |
| `R2` | **Load-bearing asset** | The install guide (Type A versus B) and the measured data. Not the datasheet's appearance |
| `R3` | **Questions it generates** | Bond or screw; how far off the designed position is acceptable; whether it can go behind fabric; why the absorption figures look low |
| `R4` | **What goes wrong on site** | Screwed without bonding; placed by eye rather than at the reflection point; expected to do a reverberation job |

### What we may and may not say

- **Supported:** measured absorption per BSRIA Report 100241/1, BS EN ISO 354:2003; 50 mm depth; ~300 mm layout
  tolerance; scattering at first-reflection points.
- **Not claimed, ever:** **diffusion.** Also no scattering-coefficient claim — ISO 17497 scattering data has not
  been measured. **[?]** whether to commission it.
- **Fix in source:** the legacy pack brochure's "faceted ABS diffuser" wording.

---

## 2. Resonance Control Panel — `C-ATS-RES-CP`

### What it actually is

| Field | Value |
|---|---|
| **What it is** | A corner-loaded low-frequency absorber for room resonance |
| **What it does** | Absorbs at low frequencies, where room modes make bass uneven from seat to seat |
| **How it works** | Corner loading — placed where modal pressure is highest, so a 50 mm panel does work that would otherwise need far greater depth |
| **What it is for** | Room corners and wall–ceiling junctions. The bass problem, which is the one dealers most often cannot solve |
| **What it is *not* for** | Reflection control or general reverberation. Not isolation — resonance is a treatment problem, isolation is a different one entirely |
| **Scope of supply** | 600 × 600 × 50 mm panel, 0.36 m² each; **4 per box = 1.44 m²**; moulded countersunk fixing holes |
| **What it requires from others** | **4 × 3.5 × 60 mm bugle-head black drywall screws with threadless shank** per panel; corner access; a fabric layer if concealed |
| **Configuration space** | One size. The larger 600 mm format is deliberate — corner loading needs area |
| **Limits** | Effectiveness depends on corner placement; away from a corner it is a much weaker device |

### Performance (BSRIA, design-stage reference)

Per-panel equivalent absorption area, **BSRIA test 4 — three items in corners against two walls, the
manufacturer's intended configuration**, m² per panel:

| 125 Hz | 250 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz |
|---|---|---|---|---|---|
| 0.38 | 0.35 | 0.32 | 0.25 | 0.15 | 0.14 |

*For completeness, and to be used with care:* the report also holds test 5 (edges against one wall — 0.28 / 0.28 /
0.31 / 0.27 / 0.18 / 0.15), test 3 (discrete around the room — 0.15 / 0.18 / 0.30 / 0.30 / 0.25 / 0.21) and test 8
(as a plane absorber in the centre of the room). **Only test 4 is the intended use.** The surface coefficient
carried in `panels.json` comes from test 8, which is explicitly *not* the intended configuration — worth knowing
before anyone quotes it.

**Design note that must travel with the figure:** these values **already embody corner loading**, so a design tool
must not also apply a corner factor — that double-counts. A caveat living in a JSON comment today, and it belongs
in the published data note.

### Why to buy it — the on-ramp

| ID | Field | Value |
|---|---|---|
| `O1` | Problem, in the dealer's words | **`[?]`** — same parked buyer-truth. The bass problem is the one dealers most often cannot solve, but that is our reading of it, not their phrasing |
| `O2` | Time or labour saved | Whole-box quantities (4 per box, 1.44 m²). **The ~300 mm tolerance does not transfer here** — this panel's effectiveness depends on corner placement, so it is the one product in the range where position is not forgiving. Worth stating rather than inheriting |
| `O3` | Opportunity it opens | **`[?]`** — not established at product level |
| `O4` | What it replaces or avoids | Deep bass traps that consume corner volume the room cannot spare. Corner loading is what lets 50 mm do work that would otherwise need far greater depth — **the depth argument made concrete**, and the product where it is most defensible |
| `O5` | Entry or flagship | **`[?]`** — `../../backlog.md` DEC-3. *Candidate flagship on the evidence:* it is the product with the strongest measured case and the hardest problem, which is what a flagship is for |

### The doubt it removes, and the questions it generates

| ID | Field | Value |
|---|---|---|
| `R1` | **The doubt it meets** | *"Can 50 mm do anything at low frequency?"* — the objection the whole depth argument exists to answer, and the one where measured data does the work |
| `R2` | **Load-bearing asset** | The measured per-panel Sabines with the test configuration stated. This product cannot be sold on description |
| `R3` | **Questions it generates** | How many, and where; whether it replaces bass traps; why it is bigger than the others; can it go anywhere other than a corner |
| `R4` | **What goes wrong on site** | Placed away from corners; too few for the room volume; expected to fix a subwoofer-placement problem |

### What we may and may not say

- **Supported:** measured per-panel absorption, corner configuration stated; BSRIA-tested 2019; 50 mm depth.
- **Not claimed:** any modal-region figure below 125 Hz — the report does not extend there. **The design tooling's
  resonance sizing has a known blind spot below ~80 Hz**, so no resonance numbers from that tool.
- **[?]** Whether a below-125 Hz measurement is worth commissioning. It is the obvious next test and would
  strengthen the strongest product.

---

## 3. Reverberation Control Panel — `C-ATS-REV-CP-50`

### What it actually is

| Field | Value |
|---|---|
| **What it is** | A broadband foam absorber that controls reverberation time |
| **What it does** | Absorbs across the mid and high band, bringing decay time to the target for a small room |
| **How it works** | Dense open-cell foam, 50 mm, working by flow resistance across a wide band above roughly 200 Hz |
| **What it is for** | Broad wall and ceiling coverage, checkerboarded toward the rear; around surround speakers |
| **What it is *not* for** | Bass. It has a weak low-frequency tail and is not the resonance answer — that is what the RES-CP exists for |
| **Scope of supply** | 300 × 300 × 50 mm panel, 0.09 m² each; **16 per box = 1.44 m²**; **pre-applied adhesive backing** |
| **What it requires from others** | A clean, dry substrate; **a room conditioned above 18 °C for 24 hours before installation** — the adhesive is temperature-sensitive; optionally one 25 mm screw per panel as permanent insurance |
| **Configuration space** | One size at 50 mm. **REV-CP-12 is discontinued — do not list it** |
| **Limits** | Above ~200 Hz is where it works; over-use dulls a room, which is a design question rather than a product limit |

### Performance (BSRIA, plane/surface, design-stage reference)

Surface absorption coefficient by octave band:

| 125 Hz | 250 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz |
|---|---|---|---|---|---|
| 0.25 | 0.51 | 0.88 | 1.09 | 1.07 | 1.18 |

### Fire

**Class 0 foam core.** Specified projects will ask for reaction-to-fire evidence — Class 0 in the UK, EN 13501-1
in Europe, IMO/SOLAS at sea. **Always confirm the certificate for the exact product and finish**, and **[?]** the
current EN 13501-1 classification, which should be in the record rather than looked up each time.

### Why to buy it — the on-ramp

| ID | Field | Value |
|---|---|---|
| `O1` | Problem, in the dealer's words | **`[?]`** — same parked buyer-truth |
| `O2` | Time or labour saved | **Pre-applied adhesive backing** — peel and stick, no fixings and no cutting on site, against a competing set that was awkward to handle and awkward to cut (`positioning.md` §1). Whole-box coverage at 1.44 m². **The strongest `O2` in the range, and it carries a condition** — the 18 °C rule below, which must travel with the claim |
| `O3` | Opportunity it opens | **`[?]`** — not established at product level |
| `O4` | What it replaces or avoids | **Commodity foam bought by the sheet**, which is the real competitor. The difference is not the material — it is measured performance plus a system that says how much to use and where |
| `O5` | Entry or flagship | **`[?]`** — `../../backlog.md` DEC-3. *Candidate entry product on the evidence:* the simplest to specify, the easiest to install, and the one a dealer is likeliest to try first |

### The doubt it removes, and the questions it generates

| ID | Field | Value |
|---|---|---|
| `R1` | **The doubt it meets** | *"Is this just foam?"* — the objection that matters most, because commodity foam is the competitor. The answer is measured performance and a system that says how much to use and where, not the material |
| `R2` | **Load-bearing asset** | The measured absorption table, and the fire certificate. A specifier will ask for both |
| `R3` | **Questions it generates** | How much coverage; checkerboard or continuous; will the adhesive hold; is it fire rated; can it be painted or covered |
| `R4` | **What goes wrong on site** | Installed in a cold room and the adhesive lets go — **the most predictable and preventable failure in the range**; over-coverage making a dead room; used where resonance was the problem |

### What we may and may not say

- **Supported:** measured absorption; Class 0 core; 50 mm depth; peel-and-stick with the temperature condition
  stated.
- **Not claimed:** bass performance; a specific RT60 outcome without a design behind it.

---

## Also in the range, deliberately not developed here

- **`C-ATS-REF-CP-MAR`** — marine Reflection Control Panel. **A narrow compliance edge case for superyacht work
  where Lloyd's requires specific heat-load limits.** Not a segment and not to be given segment-level prominence.
  **[?] It has no absorption data of its own** — the BSRIA report does not cover it, and it needs establishing
  whether it is acoustically identical to the REF-CP with a marine-grade finish or requires its own test. That is
  a real gap for a compliance product.
- **Isolation System** — a different test class entirely (sound reduction / transmissibility, not absorption) and
  needs its own report. **[?]**
- **Design service and Verification** — services, so most of the schema does not apply. But the doubt-removal and
  questions-generated fields do, and they are worth filling.

---

## The asset audit — `A1`–`A11`

*Shared across the three panels; states are **`current` · `exists — stale` · `missing` · `n/a`**. **Two of eleven are
known**, which is the honest position: the audit itself has not been done, and it should not be guessed.*

| ID | Asset | State | Note |
|---|---|---|---|
| `A1` | Datasheet | `[?]` | Per-panel absorption coefficient sheets are published; whether a datasheet proper exists per panel is unverified |
| `A2` | Dimensioned drawings | `[?]` | |
| `A3` | CAD | `[?]` | Publish-versus-gate is an open decision (`../../backlog.md` DEC-5) |
| `A4` | BIM / Revit | **`missing`** | Pre-tender specifier machinery is parked group-wide, so this is a choice rather than a debt |
| `A5` | NBS clause | **`missing`** | Same |
| `A6` | Install manual | **`exists — stale`** | Three guides exist and are to be rewritten by moment rather than by product structure (`../../backlog.md` DOC-3) |
| `A7` | Commissioning guide | `[?]` | Arguably `n/a` for passive panels — but the *design* is what needs verifying, and that is `CAT-07` |
| `A8` | Fault-finding guide | `[?]` | The two known failure modes are documented in `install-critical-notes.md` but not as a guide |
| `A9` | "How do you do X" video | **`missing`** | Three are specified and unrecorded (`../../backlog.md` DOC-2). The 52-second reverberation explainer is brand content, not product documentation |
| `A10` | Training module | **`missing`** | The programme is parked; manuals are its raw material (`../../decided.md` S12) |
| `A11` | Spares & service | `[?]` | |

**Filling this table is perhaps twenty minutes with the documentation folder open**, and it converts every "the
manuals are poor" conversation into a list. It is the cheapest unstarted thing in this file.

## What is still missing, and why it is the same six

Six fields are unfilled on all three panels, and **the pattern matters more than the count**:

| Missing | On | Why |
|---|---|---|
| `O1` — the problem in the dealer's words | all three | **Buyer-truth is parked by decision**, not by neglect (`positioning.md` §2, §7). Drafted phrasing exists in `copy.md`, but it is ours |
| `O3` — the opportunity it opens | all three | Never established at product level; the group-level version exists and does not substitute |
| `W2` — who signs off, and what convinces them | all three | Same parked buyer-truth |
| `O5` — entry or flagship | all three | An unmade decision, not a missing fact (`../../backlog.md` DEC-3) |
| `K1`, `K3` — record owner and review interval | all three | Unassigned |

**Three consequences, and the first one changes a backlog item.**

- **`../../backlog.md` DOC-13 cannot complete as written.** It asks for schema groups 1 and 2 filled so site copy
  generates from the record (`../../decided.md` S19). **Group 1 is done; group 2 is half-blocked on parked
  buyer-truth.** That is not a reason to compose the missing half — it is the reason the field exists. The honest
  move is to generate the copy that `O2` and `O4` support and leave the `O1` slot empty until a dealer fills it.
- **One input unblocks eleven fields across three products.** `O1`, `O3` and `W2` are the same question asked three
  times. **The cheapest source is the one already identified** — what dealers actually ask, from the sent-mail
  archive and from spec conversations already happening (`../../backlog.md` CON-3).
- **`O5` is a five-minute decision holding up the on-ramp for a whole brand.** The record even suggests its own
  answer: the REV-CP is the likeliest entry product and the RES-CP the likeliest flagship, on the evidence above.

---

## What filling this in produced

Seven findings, none of which needed new research — only somewhere to put what we already knew:

1. **The REF-CP bond-versus-screw trap.** Highest-return documentation in the range, and currently buried.
2. **The REV-CP cold-adhesive failure.** The most predictable site failure we have, and a one-line fix in a manual.
3. **The corner-factor double-count warning** on RES-CP data, currently living in a code comment.
4. **"Faceted ABS diffuser"** in our own legacy source — a wording violation the record now catches.
5. **The marine panel has no acoustic data**, which matters more for a compliance product than a standard one.
6. **A live figure disagreement on the REF-CP** — legacy-calculator against BSRIA test 6, roughly double at 250
   and 500 Hz — which nobody had noticed because the two numbers lived in different places.
7. **~300 mm layout tolerance is a genuine selling point that appears in no marketing.** It says the system is
   forgiving on site — exactly what an integrator wants to hear, and exactly the kind of thing that gets lost
   when nobody owns the definitional layer.

**And two more from putting it on the form** (2026-08-02):

8. **The tolerance does not transfer to the RES-CP.** Corner placement is what makes that panel work, so it is the
   one product in the range where position is *not* forgiving. Inheriting the shared claim onto all three would have
   been a wrong statement in a datasheet — caught only because `O2` had to be answered per product rather than once.
9. **The on-ramp is half-blocked on one parked input, not on three products' worth of work.** `O1`, `O3` and `W2`
   are the same missing buyer-truth asked three times, and it is already being sourced (`../../backlog.md` CON-3).
   Before the form, that read as "group 2 is unfilled"; it now reads as one question with a known source.
