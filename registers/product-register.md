# The product register — what the group sells, and what is captured about it

*Why this file exists, in one sentence: **there was no single list of what the group sells**, so "which products have
no record, and which of those are being marketed anyway" could not be answered — only argued about.*

The roster, one row per **record scope** (a mechanism family, not a SKU — `registers/record-form.md`), across all
six brands plus the one in development. It is deliberately thin per row: identity, record state, marketing status,
channel. **The substance lives in the brand records**; this file only says what exists and what is captured.

**Read it as three questions:**

1. **What do we sell?** Nobody could previously answer this in one place, and two of the brands still cannot answer
   it without going to their website.
2. **What is captured about it?** Record state per row, so the documentation debt is counted rather than described.
3. **What are we marketing that we have not captured?** The rows where `G3 = current` and record = `none`. **That
   combination is the actual risk** — a live product being sold and described with no canonical account of what it
   is.

**Sources:** the brand `brand-data.md` files and `brands/display-technologies/product-line.md` (a capture of the live
Shopify catalogue, 2026-07-26). This is a capture of the **public catalogues**, not of engine. Where engine's roster
differs, engine is right and this file is wrong — reconciling the two is `registers/backlog.md` DOC-12.

---

## Record states

| State | Means |
|---|---|
| **filled** | Every applicable field has a value or a named `[?]` |
| **skeleton** | Definition group (`D1`–`D10`) attempted; the rest is a counted gap |
| **none** | No record exists. A catalogue line and a brand page, and nothing behind them |
| **n/a** | Not a product — a service, an embedded component, or a line that has left the brand |

## Where it stands

| Brand | Record scopes | filled | skeleton | none | n/a | Public catalogue |
|---|---|---|---|---|---|---|
| **C-ATS** | 8 | 3 | 0 | 5 | 0 | `c-ats.co.uk` + store |
| **Display Technologies** | 12 | 0 | 9 | 2 | 1 | 52 live SKUs |
| **Fabric Walls** | 6 | 0 | 0 | 6 | 0 | `fabricwalls.uk` |
| **Light Walls** | 4 | 0 | 0 | 4 | 0 | `lightwalls.co.uk` |
| **Pro-Fi** | 5 | 0 | 0 | 5 | 0 | `pro-fi.uk` (thin, out of date) |
| **SRND Distribution** | 2 | 0 | 0 | 2 | 0 | `srnd.store` |
| **SRND Solutions** | 1 | 0 | 0 | 1 | 0 | none — in development |
| **Total** | **38** | **3** | **9** | **25** | **1** | |

**Three reads worth taking from that table before anything else:**

- **Three records out of thirty-eight.** The debt was known to be large; it is now a number, and the number is the
  argument for the mechanism-not-SKU rule — thirty-eight is finite, fifty-plus DT SKUs plus everything else is not.
- **The debt is concentrated exactly where S11a (`../motion/sales-motion.md`) said it was.** C-ATS is the only brand with anything
  filled; DT carries the volume; Fabric Walls, Light Walls and Pro-Fi have nothing at all.
- **Fifteen rows are `current` *and* `none`** — sold today, described on a live site, with no canonical account of
  what they are. **That combination is the gap doing the damage**, and it is why every page describes the same
  product slightly differently. Six of the fifteen are Fabric Walls and four are Light Walls, which is where the
  next fill should go after DT.

---

## C-ATS — `brands/c-ats/product-records.md`

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `CAT-01` | **Reflection Control Panel** | `C-ATS-REF-CP` | **filled** | current | `srnd.store` |
| `CAT-02` | **Resonance Control Panel** | `C-ATS-RES-CP` | **filled** | current | `srnd.store` |
| `CAT-03` | **Reverberation Control Panel** | `C-ATS-REV-CP-50` | **filled** | current | `srnd.store` |
| `CAT-04` | **Marine Reflection Control Panel** | `C-ATS-REF-CP-MAR` | none | current | `srnd.store` |
| `CAT-05` | **Isolation System** | — | none | `[?]` | `[?]` |
| `CAT-06` | **Design service** | — | none | current | trade, by enquiry |
| `CAT-07` | **Verification service** | — | none | current | trade, by enquiry |
| `CAT-08` | **Commercial / large-format range** | — | none | **pre-release** | not listed |

**Notes, and two of them are live risks:**

- `CAT-04` is a **compliance product with no acoustic data of its own** (`registers/backlog.md` DOC-8). Being sold, being
  specified for Lloyd's heat-load limits, and unable to answer a coefficient question. Worst combination on this
  page.
- `CAT-08` is `pre-release` and **must not be written up as shipping** — the `G3` gate exists for exactly this row.
- **`C-ATS-REV-CP-12` is discontinued and still listed.** Not given a row, because it is not a product; recorded
  here so the delisting is not forgotten (`operations/store-split-worklist.md`).
- `CAT-06` and `CAT-07` are services, so groups 01 and 07 apply only in part — but `O1`–`O4` and `R1`–`R4` apply in
  full, and are the reason they are on this list rather than excluded from it.

## Display Technologies — `brands/display-technologies/product-records.md`

*Grouped by mechanism, which is `registers/backlog.md` DOC-11. **The grouping below is proposed from the catalogue and needs an
hour of the owner's knowledge to confirm** — that hour is what converts DT from a year of writing into a finite
list.*

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `DT-01` | **Dynamic masking screens** | 2S · 2S-L · 2S-XL · 2TB · 2TB-L · 2TB-XL · 4 · 4-L · 4-XL (9 SKUs) | skeleton | current | `srnd.store` |
| `DT-02` | **Fixed-frame screens** | Contempo · Frontier | skeleton | current | `srnd.store` |
| `DT-03` | **Image surfaces** | ATPro · ATRef · ATStudio · AT ALR · Image ALR · Image Ref (many size/gain variants) | skeleton | current | `srnd.store` |
| `DT-04` | **Ceiling & vertical projector mounts** | Ceiling ± XL · Vertical ± XL/XXL | skeleton | current | `srnd.store` |
| `DT-05` | **Mirror concealment** | Motorised Mirror Drop (+ Short Throw, Small, Large) · Side Mirror ± XL | skeleton | current | `srnd.store` |
| `DT-06` | **Hush Box enclosures** | Small · Medium · Medium Plus · Large · Large Plus | skeleton | current | `srnd.store` |
| `DT-07` | **Projector port holes** | Single Glazed · Double Glazed · Custom Size · Small | skeleton | current | `srnd.store` |
| `DT-08` | **Airflow — Mistral** | Mistral Commander (2-zone) · inline fans 150/200/250 | skeleton | current | `srnd.store` `[?]` |
| `DT-09` | **The Commanders** | Dynamic · Actuator · Mistral | n/a — embedded | n/a | **embedded, never a line item** |
| `DT-10` | **The Screen Wall** | projection + LED variants | none | **demonstrable, undocumented** | not listed |
| `DT-11` | **Artmask** | `[?]` | none | `[?]` | on site, **not in the product feed** |
| `DT-12` | **Spares & components** | tension bands · linear actuator · draw-wire sensor · PSU | skeleton | current | `srnd.store` |

**Notes, and the first is a genuine contradiction the register surfaced:**

- **`DT-08` versus `DT-09`.** The rule is *"control stays embedded — never a line item, no exceptions"*
  (`brands/display-technologies/positioning.md` §5), and the Actuator Commander is being withdrawn to make it hold.
  **But the Mistral Commander is a live standalone line item and nobody has said whether it is an exception or an
  oversight.** Either the rule
  has an unstated exception for airflow control, or the Mistral Commander follows the Actuator Commander off the
  store. **A decision, not a project — `[?]`.**
- **`DT-10` is the flagship and has no record, no page and no datasheet** — demonstrable since ISE 2023. The `G3`
  gate says it generates internal material only until that changes (`registers/backlog.md` SW-1).
- **The Enthusiast tier has left DT** — Mask 2s, Mask2TB and Outline Fixed are a Cinema Store DIY range and are no
  longer DT products (`group-strategy/commercial-model.md`). They carry no DT row. **They were still in the DT catalogue
  at capture**, which is a store-split job (`registers/backlog.md` EST-1), not a record job.
- **The projector-model tags across `DT-04`–`DT-08` are a sizing aid, not per-model engineering.** Products are
  driven by physical size (`brands/display-technologies/positioning.md` §1). That belongs in `D8`, and getting it
  wrong there would harden a claim the brand has explicitly ruled out.
- `DT-12` sits slightly awkwardly against *"DT is not a components/OEM supplier"*. Spares for our own installed base
  are clearly right; a draw-wire sensor as a general line item is worth a look. Not urgent, noted.

## Fabric Walls — no records

*The brand with the clearest internal structure and nothing captured behind it. Its **Method** — Panels → Elements →
Kits → Levels — is already a record scope hierarchy; it has simply never been filled.*

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `FW-01` | **Fabric Panels** | Rectangle · Angled Rectangle · Angled | none | current | `srnd.store` |
| `FW-02` | **Fabric Wall Elements** | Acoustic Core · Column · Divider · External Corner · Inset Column · Inset Divider · LED Divider · Mounting Solution · Porthole & Vent · Slats · Staggered Slats · Halo LED (12) | none | current | `srnd.store` |
| `FW-03` | **Fabric** | fabric options; Camira and others | none | current | `[?]` — see store split |
| `FW-04` | **Star Ceiling** | — | none | current | `srnd.store` |
| `FW-05` | **Interior Kits** | Levels 1–4 · named city schemes · Cinema / Media Wall / Office families | none | current | `srnd.store` |
| `FW-06` | **Services** | Design & Technical Planning · Supply-Only · Approved Partner Installation · Commercial Fit-Out · Aftercare & Refitting | none | current | by enquiry |

**Notes:**

- **`FW-02` is twelve Elements in one row, and that is almost certainly wrong** — an Acoustic Core and a Halo LED
  fail differently and install differently, so they are not one record by the template's own test. Split it when
  someone who knows the range looks; the row is a placeholder, not a judgement.
- **The Acoustic Treatment Design Service is not listed above** because it comes off the site — design belongs to
  C-ATS (`registers/backlog.md` EST-7). Recorded here so the removal is not silently reversed by whoever rebuilds the page.
- **`O2` is already known for this brand and nowhere in a record.** Factory-assembled, CNC-cut, no specialist
  upholsterers, predictable install times, no on-site measurement errors — the strongest `O2` answer in the group,
  and the brand's best-performing film is built on it. It has never been written down as product data.

## Light Walls — no records

*Deferred as a brand (B7, `../group-strategy/the-group-play.md`), and the roster is recorded so the deferral is a choice with a known scope
rather than a blank.*

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `LW-01` | **Down Light** | Module (RGBW) · System Kit (RGBW, 20 W, 70 mm) | none | current | `srnd.store` |
| `LW-02` | **Linear** | Linear 1×10 (RGBW, 16-bit) | none | current | `srnd.store` |
| `LW-03` | **Matrix** | 5×5 · 1×5 · 1×1 (RGBW, 16-bit) | none | current | `srnd.store` |
| `LW-04` | **System Kits** | — | none | current | `srnd.store` |

**Note:** the measured-per-unit colour work (LWCP) is the brand's real depth and sits in `brands/light-walls/opportunity.md`. It is
`G1` material — a supported claim with a measurement behind it — and it is currently invisible in every public
surface. When the brand wakes up, that is the first field to fill.

## Pro-Fi — no records

*The public site and the engineered range do not describe the same brand. **The register records both**, because the
gap between them is the work.*

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `PF-01` | **Spatial** | BMR satellites — dot / dash / cube | none | `[?]` | not listed — gated |
| `PF-02` | **Cinema** | 2-way LCR; Reference coax point-source | none | `[?]` | not listed — gated |
| `PF-03` | **Modular** | stackable line-array blocks | none | `[?]` | not listed — gated |
| `PF-04` | **Stage** | BMR 2-way LCR | none | `[?]` | not listed — gated |
| `PF-05` | **LFE** | sealed subs 5 / 8 / 12 / 15 · infra_21 | none | `[?]` | not listed — gated |

**Notes:**

- **Every `G3` is `[?]`, and that is the finding.** The store listing is gated on range and platform readiness
  (`registers/backlog.md` BR-7), which means nobody can currently say per product whether it is `pre-release` or `current`.
  Until that is answered, **no Pro-Fi product should generate public material** — the gate does its job.
- The live site's three-way split (full-range speakers · subwoofers · amplifiers) is the *shop* structure, not the
  record structure. The five above are the engineered range. **The amplifiers have no row yet** — `[?]`, and they
  are a real product line.

## SRND Distribution — no records

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `DIS-01` | **Leyard** | LED — the only genuine third-party brand | none | current | `srnd.store` |
| `DIS-02` | **Carried lines & components** | — | none | current | `srnd.store` |

**Note:** a carried line needs `D1`–`D9` least (the manufacturer supplies them) and needs `O1`, `R1` and `C2` most —
why a dealer should buy it *from us*, what doubt that raises, and where we may sell it. That is the opposite fill
order from an own-made product, and it is why `DEC-2` (Leyard's role) is a record question as much as a strategy
one. **Ultrasuede is not a row** — it is a fabric used within Fabric Walls, not a standalone brand.

## SRND Solutions — no records, deliberately

| ID | Record scope | Covers | Record | `G3` status | Channel |
|---|---|---|---|---|---|
| `SOL-01` | **Sensors & interfaces** | — | none | **pre-release** | not listed |

**Note:** in development, and go-to-market is parked until nearer shipping. **Build it, then say it** — but the
record can be filled *before* it ships, and should be. `D1`–`D10` and `G2` written during development is the cheapest
they will ever be, and it is what the Screen Wall shows the cost of skipping.

---

## The knowledge gap — what the record shows the moment you look

*Added 2026-08-02. **Content is the sales rep** (S1–S9, `../motion/sales-motion.md`), and the production line's step 1 is
*"substance in — the atoms that already exist: **the product records**…"* with Claude multiplying pieces from that
substance and never inventing claims (`motion/motion-design.md` component 2). **So the line's fuel tank is this
register.** Reading it as fuel rather than as inventory is what this section does, and the picture is worse than the
record counts suggest.*

### Three tiers of ignorance, not one gap

| Tier | Scopes | State | What the line can do with it |
|---|---|---|---|
| **1 — questions indexed, answers missing** | **3** (the C-ATS panels) | 28/58 fields, **knowledge 2/9**, **2 of 13 questions answered in writing**; front half (`X`/`M`/`L`/`H`) empty | Multiply the two answers we have. Six more are a paragraph each away. The rest is not there |
| **2 — definition only, questions not even asked** | **9** (the DT families) | ~13/58 fields, **`R3` unfilled throughout**; front half empty | **Nothing.** With no question list there is no content backlog for DT at all — and DT owns the channel with 8 years and ~41,000 views |
| **3 — nothing** | **25** | No record | Nothing |

### What that means, stated plainly

- **The production line has fuel for three products out of thirty-eight**, and on those three it can multiply two
  answers. **Volume of pieces was never the constraint; substance is**, and the constraint is now measured rather
  than suspected.
- **DT is the sharper problem, and it is not the one that looks urgent.** C-ATS is short of *answers*; DT is short
  of the *questions* — `R3` is unfilled across every family, so nobody can rank a DT content backlog, because there
  is no list to rank. **And DT has the audience.** Three-quarters of the estate's viewers are on a channel we
  cannot currently feed with anything but product descriptions — which is precisely the catalogue content that
  already failed at 1 to 26 views a piece (`motion/content.md`).
- **`N7` — what the dealer tells their client — is empty for all 38.** The group's stated advantage is depth spent
  on the dealer's behalf, and *"the dealer is the hero, always"* (`CLAUDE.md`). **There is not one artefact in the
  estate that a dealer can hand to their own client.** Of everything on this page, this is the gap most directly
  opposite to what the strategy says the group is.
- **`N1`/`N2` — how many do I need, and show me — is the commonest question in every brand and answered in none.**
  In C-ATS three of four unanswered questions reduce to it; in DT it is the sizing question the whole range turns
  on; in Fabric Walls it is the kit level; in Light Walls it is the module count. **One field shape, five brands,
  zero answers.**
- **The C-ATS content plan cannot be copied to another brand yet.** It says *"other brands copy the shape after
  their pathways"* (`brands/c-ats/content-plan.md`) — but its ~48 items derive from three filled records, and no
  other brand has one. **The blocker on a second brand's content plan is upstream of its pathway: it is the record.**

### The one that should be uncomfortable

**Every question in a `R3` field is a question we already receive.** Naming it does not create work — the work is
already happening, one email at a time, uncounted. A `known`-but-unwritten answer means **someone here answers it
repeatedly and it has never been made findable**; an `unanswered` one means **a dealer asks and we improvise.**
Thirteen questions on the best-documented product in the group, two of them answered in writing. **That ratio, not
the record count, is the size of the job** — and mining the sent-mail archive (`registers/backlog.md` CON-3) is the cheapest
way to find out how much bigger thirteen becomes when it is counted from real traffic instead of from our own
reading of the products.

---

## What this register is for next

0. **It says what the content operation can actually be fed.** Read the knowledge gap above first; the record
   counts below it are the lesser number.
1. **It orders the work.** The `current` + `none` rows are the queue, ranked by `R3` once the sent-mail archive says
   what actually recurs (`registers/backlog.md` CON-3) — not alphabetically, and not by whichever product is loudest this
   week.
2. **It is the input to reconciliation with engine** (`registers/backlog.md` DOC-12). A roster to hold up against engine's,
   rather than a conversation about whether one exists.
3. **It says what cannot be generated yet, and why.** Every `none` row is a brand page, a store listing and a
   campaign that currently has no canonical source — which is S19 (`../motion/content.md`) restated as a list.
4. **It is amended, not re-argued.** New products get a row when they get a SKU; a filled record changes its state
   here and nowhere else.

*Drawn from the public catalogues. **The roster itself needs checking against engine** before anyone treats a
count on this page as final.*
