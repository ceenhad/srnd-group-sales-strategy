# C-ATS product records — the sales and marketing layer, filled

*The schema in `../../product-data-schema.md`, applied to the three C-ATS treatment panels. First worked example,
so it sets the standard for the rest of the group.*

**Sources:** `c-ats-shopify` — `data/panels.json`, `data/c-ats-acoustic-data.json`, `data/c-ats-pack-rules-2026.md`,
the knowledge-base articles, and the C-ATS install guides. Performance figures are from **BSRIA Report 100241/1**,
BS EN ISO 354:2003, BSRIA Bracknell, 210 m³ chamber, tested 24 July 2019, reported 3 March 2020.

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
| **Who specifies** | The integrator, typically with our help. Acoustic consultants write pre-tender specs on larger projects and are **not** a non-audience — the product is optimised for the integrator, which is a different question from who influences specification |

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

### Performance (BSRIA, free/unfixed, design-stage reference)

Surface absorption coefficient by octave band, **install Type A (default)**:

| 125 Hz | 250 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz |
|---|---|---|---|---|---|
| 0.01 | 0.08 | 0.28 | 0.11 | 0.01 | 0.06 |

Deliberately low, and that is the point — it is a scatterer, not an absorber.

### The install trap — the most important thing in this record

- **Type A, adhesive-bonded (recommended, and the default in the data):** the adhesive bonds the panel centre and
  **damps its resonance**, so it absorbs less and works as a clean scatterer.
- **Type B, screw-only:** the panel is free to resonate, adding an absorption peak. **Higher absorption, which is
  not what the design assumed.**

**Why it matters commercially:** an installer following instinct will screw it and skip the glue. The room then
behaves differently from the design, and the fault will be attributed to the product or to us. **This is a
one-page manual fix and a sixty-second video**, and it is the single highest-return piece of documentation in the
C-ATS range.

### The doubt it removes, and the questions it generates

| Field | Value |
|---|---|
| **The doubt it meets** | *"Will this actually change what I hear, or is it a decorative panel?"* — and, from consultants, *"is this a real acoustic device?"* |
| **Load-bearing asset** | The install guide (Type A versus B) and the measured data. Not the datasheet's appearance |
| **Questions it generates** | Bond or screw; how far off the designed position is acceptable; whether it can go behind fabric; why the absorption figures look low |
| **What goes wrong on site** | Screwed without bonding; placed by eye rather than at the reflection point; expected to do a reverberation job |

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

Per-panel equivalent absorption area, **from Test 4 (corner placement — the intended use)**, m² per panel:

| 125 Hz | 250 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz |
|---|---|---|---|---|---|
| 0.38 | 0.35 | 0.32 | 0.25 | 0.15 | 0.14 |

**Design note that must travel with the figure:** these values **already embody corner loading**, so a design tool
must not also apply a corner factor — that double-counts. A caveat living in a JSON comment today, and it belongs
in the published data note.

### The doubt it removes, and the questions it generates

| Field | Value |
|---|---|
| **The doubt it meets** | *"Can 50 mm do anything at low frequency?"* — the objection the whole depth argument exists to answer, and the one where measured data does the work |
| **Load-bearing asset** | The measured per-panel Sabines with the test configuration stated. This product cannot be sold on description |
| **Questions it generates** | How many, and where; whether it replaces bass traps; why it is bigger than the others; can it go anywhere other than a corner |
| **What goes wrong on site** | Placed away from corners; too few for the room volume; expected to fix a subwoofer-placement problem |

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

### The doubt it removes, and the questions it generates

| Field | Value |
|---|---|
| **The doubt it meets** | *"Is this just foam?"* — the objection that matters most, because commodity foam is the competitor. The answer is measured performance and a system that says how much to use and where, not the material |
| **Load-bearing asset** | The measured absorption table, and the fire certificate. A specifier will ask for both |
| **Questions it generates** | How much coverage; checkerboard or continuous; will the adhesive hold; is it fire rated; can it be painted or covered |
| **What goes wrong on site** | Installed in a cold room and the adhesive lets go — **the most predictable and preventable failure in the range**; over-coverage making a dead room; used where resonance was the problem |

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

## What filling this in produced

Six findings, none of which needed new research — only somewhere to put what we already knew:

1. **The REF-CP bond-versus-screw trap.** Highest-return documentation in the range, and currently buried.
2. **The REV-CP cold-adhesive failure.** The most predictable site failure we have, and a one-line fix in a manual.
3. **The corner-factor double-count warning** on RES-CP data, currently living in a code comment.
4. **"Faceted ABS diffuser"** in our own legacy source — a wording violation the record now catches.
5. **The marine panel has no acoustic data**, which matters more for a compliance product than a standard one.
6. **~300 mm layout tolerance is a genuine selling point that appears in no marketing.** It says the system is
   forgiving on site — exactly what an integrator wants to hear, and exactly the kind of thing that gets lost
   when nobody owns the definitional layer.
