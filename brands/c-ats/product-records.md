# C-ATS product records — the sales and marketing layer, filled

*The schema in `../../registers/record-schema.md`, on the form in `../../registers/record-form.md`, applied to the
three C-ATS treatment panels. First worked example, so it sets the standard for the rest of the group. Field IDs
below (`D1`, `O2`, `R4`…) are the form's; they are what downstream generation refers to.*

**Knowledge: 2 of 9 fields · 2 of 13 questions answered · Record: 28 of 58 · Assets: 5 of 11 states known · `G3` current.**

*The form gained the front half on 2026-08-02 — competitive (`X`), commercial (`M`), lifecycle (`L`) and hook
material (`H`). **Those four groups are unfilled here**, which is why the front half is unanswered. Only `M1`
(whole boxes of 1.44 m²) and `H2` (the ~300 mm tolerance — the most interesting true thing about the range) are
already answered above. Filling the rest is `registers/backlog.md` SYS-3.*

Two findings sit behind those numbers, and the second is the serious one:

- The six unfilled *record* fields are the same six on all three panels — **not per-product gaps but one missing
  input** (`O1`, `O3`, `W2`), one unmade decision (`O5`), and record ownership.
- **The knowledge layer is nearly empty on the group's best-documented product.** These records can produce a
  datasheet and cannot hold a conversation. See "the knowledge layer" below — it is the half that content-as-the-rep
  actually runs on.

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

> **Two provenance warnings on the source data.**
>
> 1. **`panels.json` is marked "DRAFT — generated from BSRIA data; pending review."** Nothing here should reach a
>    datasheet before that review happens.
> 2. **Not every figure in it is BSRIA.** The REF-CP default surface coefficient is sourced from the **legacy CATS
>    Calculator (catalogue entry 3084)**, not from the report. Both figures are given below, labelled. **Mixing the
>    two sources under one label is exactly the failure the record exists to prevent** — every figure carries its
>    source here for that reason.

**Two things this record surfaced on the first product, which is the argument for filling the rest:**

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
| **Depth** | ~~**50 mm** on all three.~~ **CORRECTED 2026-08-19 (Neil): REF-CP and REV-CP are 50 mm; RES-CP is 43 mm.** *The dimensions in this record are sourced from `c-ats-shopify:data/panels.json`, which gives 50 mm for RES-CP — **so the canonical dataset is wrong, or was, and the store is selling on it.** Verify and correct at source: `../../registers/backlog.md` `DAT-1`.* **And minimum depth is a stated design goal of the system, not a spec detail** (Neil, 2026-08-19) — it feeds the commercial argument directly: at this tier the floor area a deeper system consumes costs far more than the treatment itself |
| **Box rule** | Every box covers **1.44 m²**. Quantities round **up** to whole boxes — a dealer buys full boxes |
| **Layout tolerance** | Panels may move **~300 mm** from the designed position without material performance impact. Forgiving on site, and a genuine selling point that is nowhere in the marketing |
| **Where they sit** | Behind a stretch-fabric finish, concealed. Any fabric system works; Fabric Walls pairs well and is not a dependency |
| **Channel** | **Trade only — `srnd.store`.** No C-ATS on Cinema Store (C5, `../../group-strategy/commercial-model.md`) |
| **Test basis** | BSRIA, BS EN ISO 354:2003, **free/unfixed mounting** — design-stage reference figures, not installed-effective values |
| **Marketing status** | Current. REV-CP-12 is discontinued and must not be listed. The commercial cinema range is in development and must not be written up as shipping |
| **Who specifies** (`W1`) | The integrator, typically with our help. Acoustic consultants write pre-tender specs on larger projects and are **not** a non-audience — the product is optimised for the integrator, which is a different question from who influences specification |
| **Who signs off** (`W2`) | **Half answered 2026-08-18 (Neil, `../../registers/questions.md` Q55): *"the AV integrator in our case signs off the job."*** ~~`[?]` — deliberately parked~~ for the *who*. **What convinces them — answered in substance 2026-08-19, and deliberately left open** (Neil): *"That's an open item but more because it's the fundamental question that really deserves being picked at."* **Six reasons, his words:** *"it works well and reliably · they trust us to do a good job · it's efficient to transport and easy to install · it doesn't use up loads of space · and they can make money."* **And the answer he thinks may actually be true:** ***"the true answer in a lot of cases may simply be that it is simply the option we gave them."*** *All six were already in this record, distributed — reliability in `C2.14`, transport in the 1.44 m² box quantum, install in the `A`/`B` trap and the ~300 mm tolerance, space in the depth argument, margin in §1's channel economics. **None had ever been assembled as the answer to why they buy.*** See `claims.md` `C2.17`–`C2.23`. Consistent with `W1`: the integrator specifies **and** signs off, so it is one person, not a specifier-and-approver pair |
| **Territory** (`C2`) | Direct to dealer globally through the store; distributor appointments are case-by-case exceptions. **The live constraint is distribution, not territory** — C-ATS is widely deployed and thinly distributed, which `positioning.md` §7 calls the headline problem |
| **Proof, and publishable?** (`G4`) | **Strong and unusually unencumbered.** The full BSRIA report is published as a public PDF with five per-panel coefficient sheets beside it — specifier-grade third-party proof, freely available (`../../NEXT.md` lane 8). Install photography is thin; the Cornflake IMAX private cinema is public and easy to find, though years old |
| **Record keeping** (`K1`–`K3`) | Owner **`[?]` — unassigned** · last reviewed **2026-08-02** · review interval **`[?]`** |

**Known data gaps, shared — the authoritative-figures question is answered** (Neil, 2026-08-17,
`../../registers/questions.md` Q46): *"both options are used in our modelling tools with the glued style as
default. in test they literally just lay them loose on the floor which is not reality in any case."* So the
modelling tools carry both series (glued/Reflection A and free/Reflection B), **glued is the default for quotes
and design**, and the loose-lay lab condition is not representative of a real install.

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

### The install types — and there is no trap

~~**The install trap — the most important thing in this record.**~~ **DEFLATED 2026-08-19 (Neil):** *"The whole
A/B trap hand-waving fire-breathing dragon of a problem… no one cares. I just use bonded numbers in the design and
that's it."*

- **Type A, adhesive-bonded:** the adhesive bonds the panel centre and **damps its resonance**, so it absorbs less
  and works as a clean scatterer. **These are the numbers the design uses. Always.**
- **Type B, screw-only:** the panel is free to resonate, adding an absorption peak. *This is what BSRIA measured,
  which is why the two curves exist — it is a measurement configuration, not a field risk to manage.*

**So it is a design input, already settled by always designing on the bonded figures** — not a commercial exposure,
not a documentation priority, and not the most important thing in this record. ~~*An installer following instinct
will screw it and skip the glue; the room then behaves differently from the design and the fault is attributed to
us. A one-page manual fix and a sixty-second video, the single highest-return documentation in the range.*~~
**Struck — this was inference, and it invented a field failure to be worried about.** *The premise it rested on is
`../../registers/premises.md` `PR-13`.*

### Why to buy it — the on-ramp

| ID | Field | Value |
|---|---|---|
| `O1` | Problem, in the dealer's words | **`[?]` — unasked, not blocked.** Drafted phrasing exists in `copy.md` (*"the sound arriving off the side walls competes with the sound from the speakers; detail smears"*), and it is ours rather than a dealer's. **An owner can settle this in a sentence** |
| `O2` | Time or labour saved | **The ~300 mm layout tolerance** — panels can move that far from the designed position without material performance impact, so the install does not need set-out precision. Plus whole-box quantities (1.44 m²) making take-off arithmetic trivial. **Neither appears in any marketing** |
| `O3` | Opportunity it opens | **`[?]`** — not established at product level. The group-level answer exists (acoustics is a strong way in, `positioning.md` §6); what job this panel helps a dealer *win* does not |
| `O4` | What it replaces or avoids | Deeper competing scatterers that cost floor area; commodity foam used at reflection points, which is the wrong device for the problem; and doing nothing, which is the commonest alternative. C-ATS exists because competitors were awkward to handle, awkward to cut on site, supplied in unsuitable volumes, and too deep (`positioning.md` §1) |
| `O5` | Entry or flagship | ~~**`[?]`** — DEC-3~~ **ANSWERED 2026-08-18 (Q50): the question does not apply to C-ATS.** *"C-ATS is an acoustic treatment system… it's not that one panel is more or less important. The 3 Rs of acoustics is what defines the product"* (Neil). **No entry product, no flagship — the system is the product.** |

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
| **How it works** | Corner loading — placed where modal pressure is highest, so a **43 mm** panel does work that would otherwise need far greater depth |
| **What it is for** | Room corners and wall–ceiling junctions. The bass problem, which is the one dealers most often cannot solve |
| **What it is *not* for** | Reflection control or general reverberation. Not isolation — resonance is a treatment problem, isolation is a different one entirely. **↻ Scope note, 2026-08-19 (`Q79`): this is a *product* boundary and it stays. It is **not** a statement that C-ATS does not do isolation** — *the brand has always sold it, and it lives under C-ATS because isolation is part of the acoustic consultant's work (`claims.md` `C1.46`). **The repo had been reading this cell as a brand-level exclusion**, which put the group layer and this record in false conflict* |
| **Scope of supply** | 600 × 600 × **43 mm** panel, 0.36 m² each; **4 per box = 1.44 m²**; moulded countersunk fixing holes *(depth corrected 2026-08-19 — see the shared `Depth` field)* |
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
| `O1` | Problem, in the dealer's words | **`[?]` — unasked.** The bass problem is the one dealers most often cannot solve, but that is our reading of it, not their phrasing |
| `O2` | Time or labour saved | Whole-box quantities (4 per box, 1.44 m²). **The ~300 mm tolerance does not transfer here** — this panel's effectiveness depends on corner placement, so it is the one product in the range where position is not forgiving. Worth stating rather than inheriting |
| `O3` | Opportunity it opens | **`[?]`** — not established at product level |
| `O4` | What it replaces or avoids | Deep bass traps that consume corner volume the room cannot spare. Corner loading is what lets **43 mm** do work that would otherwise need far greater depth — **the depth argument made concrete**, and the product where it is most defensible. **Neil, 2026-08-19: *"a very, very unusual product delivering results much deeper panels would be proud of — and those results are lab verified, which is probably about the most important result and discussion point in the BSRIA results pack."*** So this is not merely the most defensible depth argument, it is **the strongest single proof point in the measured data** |
| `O5` | Entry or flagship | ~~**`[?]`** — DEC-3~~ **ANSWERED 2026-08-18 (Q50): the question does not apply to C-ATS.** *"C-ATS is an acoustic treatment system… it's not that one panel is more or less important. The 3 Rs of acoustics is what defines the product"* (Neil). **No entry product, no flagship — the system is the product.** ~~*Candidate flagship on the evidence*~~ — that line was inference, and it is struck |

### The doubt it removes, and the questions it generates

| ID | Field | Value |
|---|---|---|
| `R1` | **The doubt it meets** | *"Can **43 mm** do anything at low frequency?"* — the objection the whole depth argument exists to answer, and the one where measured data does the work. **Sharper than the record had it**: the panel is shallower than the 50 mm this field assumed, and the lab-verified answer is correspondingly more surprising (Neil, 2026-08-19) |
| `R2` | **Load-bearing asset** | The measured per-panel Sabines with the test configuration stated. This product cannot be sold on description |
| `R3` | **Questions it generates** | How many, and where; whether it replaces bass traps; why it is bigger than the others; can it go anywhere other than a corner |
| `R4` | **What goes wrong on site** | Placed away from corners; too few for the room volume; expected to fix a subwoofer-placement problem |

### What we may and may not say

- **Supported:** measured per-panel absorption, corner configuration stated; BSRIA-tested 2019; **43 mm** depth.
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
| `O1` | Problem, in the dealer's words | **`[?]` — unasked** |
| `O2` | Time or labour saved | **Pre-applied adhesive backing** — peel and stick, no fixings and no cutting on site, against a competing set that was awkward to handle and awkward to cut (`positioning.md` §1). Whole-box coverage at 1.44 m². **The strongest `O2` in the range, and it carries a condition** — the 18 °C rule below, which must travel with the claim |
| `O3` | Opportunity it opens | **`[?]`** — not established at product level |
| `O4` | What it replaces or avoids | **Commodity foam bought by the sheet**, which is the real competitor. The difference is not the material — it is measured performance plus a system that says how much to use and where |
| `O5` | Entry or flagship | ~~**`[?]`** — DEC-3~~ **ANSWERED 2026-08-18 (Q50): the question does not apply to C-ATS.** *"C-ATS is an acoustic treatment system… it's not that one panel is more or less important. The 3 Rs of acoustics is what defines the product"* (Neil). **No entry product, no flagship — the system is the product.** ~~*Candidate entry product on the evidence*~~ — that line was inference, and it is struck |

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

## The knowledge layer — `N1`–`N9`

*Added 2026-08-02 with the form's group 04. **This is the substance the production line runs on**
(`../../motion/motion-design.md` component 2, step 1: "the atoms that already exist: the product records…").
Filled across the three panels together, because most of it is range-level. **Knowledge: 2 of 9 fields · 2 of the 13
questions answered in writing.***

| ID | Field | Value |
|---|---|---|
| `N1` | **Selection logic** | ~~**`[?]` — partial…** *Quantity* is not written anywhere — it lives inside the legacy CATS Calculator and the design service~~ **WRONG, corrected 2026-08-18 (Neil: *"how many panels — please see Cinema Tools Pro"*).** **The selection logic is fully systemised and encoded.** `cinema-platform` `products/cinema-tools/``docs/product/c-ats-system-design-rules.md` (captured 2026-06 with Neil) holds the design hierarchy, per-axis Fitzroy flatness, the surface-palette rule, reflection triage with a binding budget, install-type effects, corner-straddle placement and the 1.44 m² box quantum; `engines/modal_analysis/treatment_systems.cats_system()` and `acoustic_treatment.py` implement it, sizing in whole boxes off the BSRIA catalogue. **The legacy calculator was reverse-engineered for parity in 2026-05 and its SKUs are explicitly historic** (`docs/validation/cats-calculator-reference.md`) — it is a source that was superseded, not the place the answer is trapped. **What is `[?]` is not the answer but its publishable form** — see `N2` and Q52 |
| `N2` | **The worked example** | **`exists — unpublished`, corrected 2026-08-18.** ~~`missing`~~ A worked reference is carried in `cinema-platform` `products/cinema-tools/``docs/product/c-ats-system-design-rules.md`: **Joppa Road, 7.05 × 4.95 × 2.6 m, 7.1.4, 7 seats over two rows — Gold on carpet = 11 boxes (REF 6 + REV 1 + RES 4)**, per-axis x 0.35 / y 0.20 / z 0.11, and the wood-walkway variant that flattens z to 0.30. **So the commitment in `positioning.md` §1 is one step from being met, not unstarted.** What is unresolved is **how much of the derivation may be shown** — the platform black-boxes the methodology while positioning promises examples showing how quantities are *derived*. **That is Q52 and it gates this field.** Also still true: the three pre-planned 7.1.4 layouts are built and blocked on a CLI re-auth (EST-6) |
| `N3` | **The answers** | **2 of 13 written.** Table below |
| `N4` | **Comparison** | **PARTLY FILLED 2026-08-19 — the eight axes are applied to acoustics in `../../group-strategy/competitors.md`, C-ATS column complete, competitor columns empty by design.** *The price band is replaced by the `A5` posture claim (`claims.md` `C1.38`): direct-sell-at-published-prices versus trade-only-and-gated, which is observable rather than measured.* ~~**`[?]` — price band only.**~~ `positioning.md` §1 places C-ATS above direct-sell GIK, comparable to RPG, slightly below Artnovion. **That is a commercial position, not a comparison** — nothing says what a dealer gets or gives up choosing one over another, per panel, per dimension |
| `N5` | **Compatibility & pairing** | **Filled.** Sits behind any stretch-fabric finish — **Fabric Walls pairs naturally and is never a dependency**. Works behind acoustically transparent projection screens, which puts DT's image surface, Pro-Fi's speakers and the treatment in one wall. The commercial/large-format range is likely built on Fabric Walls Acoustic Core PET. **Never paired with:** isolation as a substitute — resonance is a treatment problem, isolation is a different one |
| `N6` | **Project timing** | **`[?]`, with one thing derivable and load-bearing.** The panels are concealed behind the fabric layer, so **the treatment must be decided before the wall is built** — which makes it *earlier* in the project than the fabric, the lighting or the screen. That is the cross-sell moment and the argument for being in the spec conversation, and it has never been stated. When the acoustic decision actually gets made on a real job is `[?]`. **↻ First stated 2026-08-19** — `draft-t2-decide-before-the-wall.md` is built on this derivation and nothing else, with three further consequences drawn from records already here: **the treatment depth is part of the wall build-up, so it feeds the architect's finished dimensions**; the corner absorber needs corners that have not yet been committed; and an acoustic design is drawn *from* the finish schedule (`Q68`). **`Q75` answered 2026-08-19, and it corrected me.** *The sequence holds. **The dimensions do not belong to us** — Neil: *"they are separate things. The sound isolation design which determines the structural dimensions of the room is one part of the project… the interior design of the room likely includes the fabric wall design which is what the client will see. **C-ATS fits nicely physically and metaphorically between the two** and SRND is often involved in all three."* **So this field's real content is a three-layer account with three owners** (`claims.md` `C1.40`), and the load-bearing derivation is now a different one: **the treatment is the only layer with no natural owner, which is why it waits** (`C1.41`, open as `Q77`). `PR-21` broken |
| `N7` | **What the dealer tells their client** | ~~**`missing`, for all three panels.**~~ **DRAFTED 2026-08-19 — `draft-n7-client-leave-behind.md`**, the first `N7` artefact in the repo (`KNW-5`). The raw material was one sentence away — `positioning.md` §4: *"acoustics is usually the one part of a room nobody can see or prove; C-ATS makes it the part you can"* — **and the piece is built to deliver exactly that line.** *It covers all three panels as one system, because that is what a client sees. **It makes no measured claim at all**, so it needs nothing from `DOC-4`, `DOC-7` or `DR-Q52` — `PR-4` used as a design constraint rather than fought.* **Two decisions are Neil's, on `Q76`:** whether client-facing words should exist at all given `C2.29`, and **whose name is on it** — the dealer-brandable version is the one a dealer would actually hand over |
| `N8` | **Field learning** | **`[?]`.** A decade of cinema work and the Cornflake IMAX install; nothing captured as learning. The two failure modes in `install-critical-notes.md` *are* field learning, and they are the only entries that exist |
| `N9` | **What we are asked and cannot answer** | **Filled — and see the note.** (1) ISO 17497 scattering coefficient for the REF-CP: never measured. (2) Resonance performance below 125 Hz: outside the report; the design tool is blind below ~80 Hz. (3) Marine panel absorption: no data of its own. (4) Current EN 13501-1 classification for the REV-CP foam. (5) ~~Installed-effective versus raw lab figures: both in circulation, neither declared authoritative~~ **Answered 2026-08-17** — both are used in the modelling tools, glued default (Q46; note above the record) |

> **`N9` was already in the repo as five separate backlog rows** (DOC-6 to DOC-10) and had never been read as one
> list. As a set it says something the rows individually do not: **four of the five are measurement gaps, so one
> decision — commission the further testing, or declare the current data the limit and say so plainly — closes most
> of them.** `positioning.md` §4 already frames expanded testing as *"an option for later."* This is what makes it a
> decision rather than an option: it is the answer to five live questions, not a nice-to-have.

### `N3` — the answers, against the 13 questions the record says we get asked

*State: **`answered`** (written down somewhere a dealer could reach it) · **`known`** (the answer is in this record
or in someone's head, and has never been turned into an answer) · **`unanswered`**.*

| # | Question (from `R3`) | Panel | State | Where the answer is, or why not |
|---|---|---|---|---|
| 1 | Bond or screw? | REF-CP | **`answered`** | `install-critical-notes.md` p1 — written, unpublished (`../../registers/backlog.md` DOC-1) |
| 2 | How far off the designed position is acceptable? | REF-CP | **`known` → DRAFTED 2026-08-19** | ~300 mm, in this record. Also the brand's best unused `O2`. **Now its own piece — `draft-t5-layout-tolerance.md`**, carrying two pre-publication confirmations |
| 3 | Can it go behind fabric? | REF-CP | **`known` → DRAFTED 2026-08-19** | Yes, any stretch fabric — `N5`. ~~Never stated as an answer~~ **Written in `draft-answers.md`**, with `N6`'s consequence attached: the treatment is decided before the wall that conceals it |
| 4 | Why do the absorption figures look low? | REF-CP | **`known` → DRAFTED 2026-08-19** | Because it is a scatterer, not an absorber — plus the Reflection A/B install-type story. ~~Blocked on DOC-4~~ **`DOC-4` blocks tabulating the values, not explaining them** — the explanation is written in `draft-answers.md` and quotes no coefficient |
| 5 | **How many, and where?** | RES-CP | **`known`, not `unanswered`** *(corrected 2026-08-18)* | Both are answered in the platform's design rules and encoded in the engine — `N1`. **The gap is publication, not knowledge**, and its boundary is Q52 |
| 6 | Does it replace bass traps? | RES-CP | **`unanswered`** | A comparison question with no `N4` behind it |
| 7 | Why is it bigger than the others? | RES-CP | **`known` → DRAFTED 2026-08-19** | Corner loading needs area — in `D8`. ~~Never stated as an answer~~ **Written in `draft-answers.md`** as the trade it actually offers: area on a corner instead of depth into the room |
| 8 | Can it go anywhere other than a corner? | RES-CP | **`known` → DRAFTED 2026-08-19** | Much weaker away from a corner — in `D9`. **Written in `draft-answers.md`**, plainly: it is the one place in the range where position is not forgiving |
| 9 | **How much coverage?** | REV-CP | **`unanswered`** | The same quantity question as 5 |
| 10 | Checkerboard or continuous? | REV-CP | **`known` → DRAFTED 2026-08-19** | Checkerboarded toward the rear — in `D4`. **Written in `draft-answers.md`** with the *over-use dulls a room* limit attached, and **one gate flagged**: pattern is stated as intended use, quantity stays behind `DR-Q52` |
| 11 | Will the adhesive hold? | REV-CP | **`answered`** | The warm-room rule — written, derivative set drafted (`content-batch-001.md`) |
| 12 | Is it fire rated? | REV-CP | `known`, partly | Class 0 core is known; **the current EN 13501-1 classification is `[?]`** (DOC-7) |
| 13 | Can it be painted or covered? | REV-CP | **`unanswered`** | Nobody has answered this |

**Three things this table says that nothing else in the repo did:**

1. **Two of thirteen are written down.** The brand with the best data in the group, three SKUs, a decade of
   deployment — and a dealer can find our answer to two of the thirteen questions we know we get asked.
2. ~~**Six are `known` and unwritten — and they are the cheap ones.**~~ **DONE 2026-08-19 — and the claim held.**
   The answers were already in this file, in the definitional fields. **Turning a `known` into an `answered` is a
   paragraph, not research** — *five are written in `draft-answers.md` and the sixth (row 2) became its own piece,
   **and not one of them needed a fetch, a decision or an owner's answer.*** *`12` was left deliberately at half an
   answer, because a partial fire answer is the one that could get a dealer refused on site.* **They are drafted,
   not published: the count moves from 2 of 13 to 8 of 13 on approval, not on writing.**
3. ~~**Three of the four unanswered questions are the same question: *how many do I need?*** (5, 6, 9). **The
   commonest question in the range has no answer, no worked example, and no owner.**~~ **Corrected 2026-08-18.**
   *How many do I need* **is answered** — systemised with Neil in 2026-06 and running in the Cinema Tools engine
   (`N1`, `N2`). **It has an answer, a worked reference and an owner; what it does not have is a public form.**
   *The original line was written from this file alone and never checked against the platform, which
   `../../CLAUDE.md` requires in as many words. That is the second time a position here has been built on a stale
   in-repo reading rather than the live system.*

---

## The asset audit — `A1`–`A11`

*Shared across the three panels; states are **`current` · `exists — stale` · `missing` · `n/a`**. **Two of eleven are
known**, which is the honest position: the audit itself has not been done, and it should not be guessed.*

| ID | Asset | State | Note |
|---|---|---|---|
| `A1` | Datasheet | `[?]` | Per-panel absorption coefficient sheets are published; whether a datasheet proper exists per panel is unverified |
| `A2` | Dimensioned drawings | `[?]` | |
| `A3` | CAD | `[?]` | Publish-versus-gate is an open decision (`../../registers/backlog.md` DEC-5) |
| `A4` | BIM / Revit | **`missing`** | Pre-tender specifier machinery is parked group-wide, so this is a choice rather than a debt |
| `A5` | NBS clause | **`missing`** | Same |
| `A6` | Install manual | **`exists — stale`** | Three guides exist and are to be rewritten by moment rather than by product structure (`../../registers/backlog.md` DOC-3) |
| `A7` | Commissioning guide | `[?]` | Arguably `n/a` for passive panels — but the *design* is what needs verifying, and that is `CAT-07` |
| `A8` | Fault-finding guide | `[?]` | The two known failure modes are documented in `install-critical-notes.md` but not as a guide |
| `A9` | "How do you do X" video | **`missing`** | Three are specified and unrecorded (`../../registers/backlog.md` DOC-2). The 52-second reverberation explainer is brand content, not product documentation |
| `A10` | Training module | **`missing`** | The programme is parked; manuals are its raw material (S12, `../../motion/sales-motion.md`) |
| `A11` | Spares & service | `[?]` | |

**Filling this table is perhaps twenty minutes with the documentation folder open**, and it converts every "the
manuals are poor" conversation into a list. It is the cheapest unstarted thing in this file.

## What is still missing, and why it is the same six

Six fields are unfilled on all three panels, and **the pattern matters more than the count**:

| Missing | On | Why |
|---|---|---|
| `O1` — the problem in the dealer's words | all three | **Unasked.** Drafted phrasing exists in `copy.md`, but it is ours. One question to an owner |
| `O3` — the opportunity it opens | all three | Never established at product level; the group-level version exists and does not substitute |
| `W2` — who signs off, and what convinces them | all three | **Who: answered** (the AV integrator, Q55). **What convinces them: answered in substance 2026-08-19** — six reasons plus the hypothesis that it may be *"simply the option we gave them"*. **Kept open by Neil as the fundamental question** |
| ~~`O5` — entry or flagship~~ | ~~all three~~ | **Closed 2026-08-18 (Q50) — the question does not apply.** No longer a gap on any of the three; the counts in the header were not recomputed |
| `K1`, `K3` — record owner and review interval | all three | Unassigned |

**Three consequences, and the first one changes a backlog item.**

- **`../../registers/backlog.md` DOC-13 cannot complete as written.** It asks for schema groups 1 and 2 filled so site copy
  generates from the record (S19, `../../motion/content.md`). **Group 1 is done; group 2's `O1`/`O3` are
  unasked, not blocked.** That is not a reason to compose the missing half — it is the reason the field exists. The honest
  move is to generate the copy that `O2` and `O4` support and leave the `O1` slot empty until a dealer fills it.
- **One input unblocks eleven fields across three products.** `O1`, `O3` and `W2` are the same question asked three
  times. **The cheapest source is the one already identified** — what dealers actually ask, from the sent-mail
  archive and from spec conversations already happening (`../../registers/backlog.md` CON-3).
- ~~**`O5` is a five-minute decision holding up the on-ramp for a whole brand.** The record even suggests its own
  answer: the REV-CP is the likeliest entry product and the RES-CP the likeliest flagship, on the evidence above.~~
  **Struck 2026-08-18 (Q50).** The decision was never C-ATS's to make: *"it's not that one panel is more or less
  important. The 3 Rs of acoustics is what defines the product."* **The record proposing its own answer here is
  exactly the failure `../../method.md` names — inference wearing the voice of measurement**, and it stood in the
  file for sixteen days before anyone was asked.

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
   are the same unasked question three times. ~~Already being sourced (CON-3)~~ — **struck 2026-08-18: it was never
   being sourced, and it does not need an archive. It needs asking.**
   Before the form, that read as "group 2 is unfilled"; it now reads as one question with a known source.
