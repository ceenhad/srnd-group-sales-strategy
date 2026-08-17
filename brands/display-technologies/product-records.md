# Display Technologies — product records (skeleton)

*The form in `../../registers/record-form.md`, applied to the DT range **by mechanism rather than by SKU**
(S11a, `../../motion/sales-motion.md`). Fifty-two live catalogue lines resolve into **twelve record scopes**, of which nine are
sellable families documented below.*

**What this file is: the definitional layer, filled from what the repo already holds — and every other field
counted as a gap.** The counted gaps are the deliverable. DT's documentation debt has been described for months;
this states it as **~13 of 58 fields per family**, with the definitional gaps named individually so each is a
question someone can be sent to answer rather than a project someone has to scope.

> **Scope of the gap lists.** The `Gaps:` lists under each family enumerate the *definitional* gaps only. The
> front half of the form — competitive (`X1`–`X6`), commercial (`M1`–`M5`), lifecycle (`L1`–`L5`) and hook
> material (`H1`–`H3`) — is **empty for every DT family**. Filling it is `../../registers/backlog.md` SYS-3.

**Provenance — read before using anything here.**

| Content | Source |
|---|---|
| Range, families, SKU counts, variant lists | `product-line.md` (live Shopify catalogue, captured 2026-07-26) |
| Identity, what may and may not be claimed, the control rule, sizing basis | `positioning.md` §1, §5 |
| The Commanders and their jobs | `brand-data.md`, `dt-commander-v5.md` |

> **Nothing below is new research.** Where the repo does not hold an answer the field says `[?]`, and **no field has
> been filled by inference.** The point of the skeleton is that it is honest about its own emptiness — a plausible
> guess in `D7` would be worse than the blank, because someone would build a drawing on it.

---

## Shared across the DT range

*Filled once, inherited by every family below. Same principle as the C-ATS record's shared block.*

| ID | Field | Value |
|---|---|---|
| `W1` | **Purchaser vs specifier** | The **AV integrator** buys. Where the room's *look* is at stake the **architect or designer** specifies, which widens the audience beyond the integrator (`positioning.md` §2) |
| `W2` | **Who signs off, and what convinces them** | `[?]` — **deliberately parked.** The real split (integrator vs specialist cinema contractor vs architect/designer) comes from real jobs, not invention |
| `G2` | **The claims we refuse to make** | No *"engineered to your exact projector"* — products are **size-driven, not per-model bespoke**. No lab regime or certifications DT does not hold. No claim that DT's element is *the* most complex part of a project. Forward/LED claims are **capability, not track record**. FA-copied-CAD is internal and attributed, never public |
| `G3` | **Marketing status** | `current` for `DT-01`–`DT-08` and `DT-12`; see the individual rows for the exceptions |
| `C1` | **Channel** | `srnd.store`, trade. **DT is trade-only** — the former Enthusiast tier has left the brand for the Cinema Store DIY range (`../../group-strategy/commercial-model.md`) |
| `C2` | **Territory** | Direct to dealer globally through the store; distributor appointments are case-by-case exceptions. **The US is currently unrepresented** — Apex-Tech has resigned and the Screen Innovations arrangement is white label (`../../evidence/current-state.md`) |
| `K1` | **Record owner** | `[?]` — unassigned |
| `K2` | **Last reviewed** | 2026-08-02 (first capture) |
| `K3` | **Review interval** | `[?]` |

**Shared: 6 of 9 filled.**

**The asset audit (`A1`–`A11`) is `[?]` for every family.** It has not been done, and it should not be guessed:
manuals are known to be poor (S11, `../../motion/sales-motion.md`) but "poor" is not a state the form accepts. **Auditing the
current documentation folder against the eleven asset types is perhaps an hour**, and it is the natural companion to
confirming the family grouping below — same session, same person.

---

## `DT-01` — Dynamic masking screens

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | A motorised masking projection screen whose borders move to fit the image being shown |
| `D2` | What it does | Changes the screen's active area to match the source aspect ratio, so the image is always framed rather than letterboxed onto unused white |
| `D3` | How it works | Motorised masking borders driven by the **Dynamic Commander**, which ships inside the screen — 5-edge aspect masking including **Mask Position Logic**, driving the screen by aspect ratio rather than by fixed presets |
| `D4` | What it is for | The premium moving product: high-end cinema and screening rooms where more than one aspect ratio is watched |
| `D5` | What it is *not* for | `[?]` — **and this is the range's most conspicuous blank.** See the note below |
| `D6` | Scope of supply | `[?]` — does the screen ship with a surface, or is the surface specified separately from `DT-03`? |
| `D7` | What it requires from others | `[?]` — power, control connection, structural support, wall or ceiling clearance, and what the builder must leave |
| `D8` | Configuration space | Three masking types × three sizes: **2S / 2S-L / 2S-XL** (side), **2TB / 2TB-L / 2TB-XL** (top-and-bottom), **4 / 4-L / 4-XL** (four-way). Nine SKUs, one mechanism. Tension bands are a spare, not a variant |
| `D9` | Limits | `[?]` — maximum screen size per family, load, throw and mounting constraints |
| `D10` | Where it sits | The front of room, in or on the front wall. Meets the image surface (`DT-03`), the front-wall structure, and — with an acoustically transparent surface — the speakers and treatment behind it |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D5`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

**`D5` is the one to fill first, and the reason is commercial.** DT's products are **size-driven** — what determines
the product is the dimensions of the unit and the room. So the characteristic DT misapplication is not "wrong
product" but **"right product, wrong size"**, which is expensive, discovered on site, and entirely preventable by a
sentence. Nowhere in the DT estate is that sentence written down.

## `DT-02` — Fixed-frame screens

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | A rigid, fixed-size projection screen frame carrying a tensioned surface |
| `D2` | What it does | Holds a screen surface flat and square at one fixed aspect ratio |
| `D3` | How it works | Tensioned surface on a fixed perimeter frame. No motion, no control layer |
| `D4` | What it is for | **Contempo** and **Frontier** — acoustic-transparent fixed-frame, tagged for home cinema, commercial AV and meeting rooms |
| `D5` | What it is *not* for | Multi-aspect-ratio rooms — that is `DT-01`'s job. `[?]` beyond that |
| `D6` | Scope of supply | `[?]` — frame only, or frame plus surface |
| `D7` | What it requires from others | `[?]` — fixings, wall structure, flatness |
| `D8` | Configuration space | Two lines, made to size. **The Outline Fixed range is no longer DT** — it left with the Enthusiast tier |
| `D9` | Limits | `[?]` — maximum span |
| `D10` | Where it sits | Front of room, on the front wall or within the Screen Wall (`DT-10`) |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

## `DT-03` — Image surfaces

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | The screen material itself, specified and sold separately from the frame |
| `D2` | What it does | Reflects the projected image — and, in the acoustically transparent grades, lets speaker sound pass through it |
| `D3` | How it works | Two mechanisms in one family, and **they should probably be two records**: acoustic transparency (perforation or weave) and ambient-light rejection (optical structure). See the note |
| `D4` | What it is for | Acoustic-transparent: **ATPro · ATRef · ATStudio · AT ALR**, where speakers sit behind the screen. Solid: **Image ALR · Image Ref**, where they do not |
| `D5` | What it is *not* for | `[?]` |
| `D6` | Scope of supply | `[?]` — supplied cut to size, on a roll, or fitted |
| `D7` | What it requires from others | `[?]` — and for the AT grades this is the whole speaker-placement conversation |
| `D8` | Configuration space | **The largest variant count in the range** — ATPro alone has 31 size/gain variants. Six surfaces × sizes × gains |
| `D9` | Limits | `[?]` — maximum width before seaming, gain and viewing-angle envelope |
| `D10` | Where it sits | On `DT-01` or `DT-02`, and it is **the direct C-ATS and Pro-Fi link** — the acoustically transparent grades put speakers and acoustic treatment behind the image |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D5`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

**Two notes, and the first is a scoping decision:**

- **This row may be two records.** *Acoustically transparent* and *ambient-light-rejecting* are different mechanisms
  answering different doubts, and by the template's own test — same manual, same failure modes — they are not one
  record. Split when someone confirms the grouping.
- **`D8` is where DT's variant problem actually lives.** Thirty-one variants of one surface is a configurator
  question, not a documentation question. Getting `D8` right here is what keeps the manual set from multiplying.

## `DT-04` — Ceiling & vertical projector mounts

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | An engineered mount that carries a projector in a fixed or vertically adjustable position |
| `D2` | What it does | Holds a heavy projector rigidly and precisely where the room needs it |
| `D3` | How it works | `[?]` for the vertical range — whether adjustment is manual, motorised, or Commander-driven, and how it is locked off |
| `D4` | What it is for | **Ceiling Mount / — XL** and **Vertical Projector Mount / — XL / — XXL**, sized to the projector |
| `D5` | What it is *not* for | `[?]` — and **the size-driven caveat applies hardest here** |
| `D6` | Scope of supply | `[?]` — fixings, adaptor plates, drop poles |
| `D7` | What it requires from others | `[?]` — structural fixing, load path, clearance, and power where motorised |
| `D8` | Configuration space | Two mount types × three size bands. **Projector-model tags are a sizing aid, never a claim of per-model engineering** (`positioning.md` §1) |
| `D9` | Limits | `[?]` — **and this is a load-bearing product, so the load figure is not optional** |
| `D10` | Where it sits | Above or behind the audience, in the ceiling void or on the rear wall. Pairs with `DT-06` and `DT-07` |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D3`, `D5`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

## `DT-05` — Mirror concealment

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | A motorised or fixed mirror assembly that folds the projector's optical path so the projector can be hidden |
| `D2` | What it does | Reflects the image to the screen from a projector placed out of sight, and — in the drop variants — reveals and conceals on demand |
| `D3` | How it works | Motorised motion driven by the **Actuator Commander**, which ships inside the product and is not sold separately |
| `D4` | What it is for | **Motorised Mirror Drop** (+ Short Throw, Small, Large) and **Side Mirror / — XL**, where the projector must not be visible in the finished room |
| `D5` | What it is *not* for | `[?]` |
| `D6` | Scope of supply | `[?]` |
| `D7` | What it requires from others | `[?]` — **the coordination case in the range**: ceiling void, aperture, structure, power, control, and the geometry the optical path demands |
| `D8` | Configuration space | Drop variants by size and by throw; side mirrors in two sizes |
| `D9` | Limits | `[?]` — throw range, projector size and weight |
| `D10` | Where it sits | Ceiling void or side wall, ahead of the projector, behind the finished surface — typically a Fabric Walls one |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D5`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

## `DT-06` — Hush Box enclosures

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | A ventilated acoustic enclosure that houses a projector inside the room |
| `D2` | What it does | Contains the projector's noise while keeping it cool enough to run |
| `D3` | How it works | Sealed enclosure with managed airflow; cooling is handled by the Mistral layer (`DT-08`) |
| `D4` | What it is for | Rooms where the projector must sit in the space rather than a projection room, and its fan noise would be audible |
| `D5` | What it is *not* for | `[?]` |
| `D6` | Scope of supply | `[?]` — whether fans, controller and glass are included or specified alongside |
| `D7` | What it requires from others | `[?]` — **power, airflow path, extract route, service access, and structural support.** The single most under-documented dependency set in the range |
| `D8` | Configuration space | Five size bands: Small · Medium · Medium Plus · Large · Large Plus, chosen by projector dimensions |
| `D9` | Limits | `[?]` — **thermal capacity by projector heat load, which is the figure that decides whether the box works** |
| `D10` | Where it sits | In the room, usually within or behind the finished surface; meets `DT-04`, `DT-07` and `DT-08` |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D5`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

**`D9` here is a genuine commercial risk, not a documentation nicety.** A hush box specified against a projector it
cannot cool is a failure discovered after the room is finished. **The store's de-duplication of this line is already
a live worklist item** (`../../operations/store-split-worklist.md`), so the range is being touched anyway — the thermal
envelope should be captured in the same pass.

## `DT-07` — Projector port holes

**Record: 13 / 58 · Assets: not audited · `G3`: current**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | A glazed aperture assembly set into a wall for a projector to shoot through |
| `D2` | What it does | Lets the image pass cleanly from a projection room into the cinema while keeping the wall's acoustic and visual separation |
| `D3` | How it works | Single or double optical glazing in a framed aperture |
| `D4` | What it is for | Rooms with a separate projection room or equipment space |
| `D5` | What it is *not* for | `[?]` |
| `D6` | Scope of supply | `[?]` — frame, glass, trim, and which side is finished |
| `D7` | What it requires from others | `[?]` — **the builder's opening, and it must be right before the wall is closed.** The definitive example of a field that belongs in a drawing, not in marketing |
| `D8` | Configuration space | Single Glazed · Double Glazed, each with **Custom Size**; plus a Small single-glazed |
| `D9` | Limits | `[?]` — aperture range, wall thickness, angle |
| `D10` | Where it sits | In the projection-room wall. Meets the building fabric more directly than anything else DT makes |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D5`, `D6`, `D7`, `D9`, `W2`, `K1`, `K3`.**

## `DT-08` — Airflow (Mistral)

**Record: 12 / 58 · Assets: not audited · `G3`: current · `C1`: `[?]` — see below**

| ID | Field | Value |
|---|---|---|
| `D1` | What it is | A fan and fan-control layer for projector and enclosure cooling |
| `D2` | What it does | Moves air through an enclosure or void at a controlled rate, and holds the projector within its thermal envelope quietly |
| `D3` | How it works | **Mistral Commander**, a two-zone fan controller, driving **inline fans** at 150 / 200 / 250 |
| `D4` | What it is for | Hush boxes (`DT-06`), projector voids, and equipment spaces |
| `D5` | What it is *not* for | `[?]` |
| `D6` | Scope of supply | `[?]` |
| `D7` | What it requires from others | `[?]` — power, ducting, intake and extract routes, and an acoustic path that does not undo the enclosure |
| `D8` | Configuration space | One controller, three fan sizes |
| `D9` | Limits | `[?]` — flow rate per fan, and the heat load each combination can carry |
| `D10` | Where it sits | Inside or adjacent to `DT-06`; part of the control layer rather than the visible room |

**Gaps: `O1`–`O5`, `R1`–`R4`, `G1`, `G4`, `D5`, `D6`, `D7`, `D9`, `C1`, `W2`, `K1`, `K3`.**

> **`C1` is `[?]` for a reason, and it is a decision rather than a lookup.** The rule is *"control stays embedded —
> never a line item, no exceptions"* (`positioning.md` §5), and the Actuator Commander is being withdrawn from the
> store to make it hold without exception. **The Mistral Commander is a live standalone line item.** So either
> airflow control is an unstated exception to the rule, or it follows the Actuator Commander off the store. Nobody
> has said which. Recorded in `../../registers/product-register.md` and worth a minute of the owner's time, not a project.

## `DT-09` — The Commanders

**`n/a — embedded`.** The Dynamic, Actuator and Mistral Commanders are **the control layer, not a product line**:
they ship inside DT products and are never sold as components. The Dynamic Commander has never been a purchasable
SKU; the Actuator Commander is being withdrawn as one.

**The distinction is purpose, not part.** A Commander may be supplied as a **service replacement** against an
existing DT product — we have to be able to support our own installed base — but never as a component to design into
someone else's mechanism. **That sentence belongs in `A11` (spares and service instructions), not in a product
record**, and it is the cleanest example in the estate of a governance rule that only survives if it is written next
to the thing it governs.

## `DT-10` — The Screen Wall

**Record: 0 / 58 · `G3`: `demonstrable, undocumented`**

**No record, deliberately not skeletoned here.** The flagship — a modular front-wall carrying screen, speakers,
acoustics and structure as one product, in projection and LED variants, demonstrable since **ISE 2023** and with no
page and no datasheet.

**The `G3` gate applies in full: it generates internal material only until it has a record.** Writing that record is
`registers/backlog.md` SW-1 and it is a description of what already exists, not an engineering job. **It is also the best
possible argument for this whole exercise** — three years of a finished flagship being commercially invisible is
what the absence of a product record costs.

## `DT-11` — Artmask

**Record: 0 / 58 · `G3`: `[?]`**

Appears on the DT site but **not in the product feed**. Whether it is a product, a category or an intention is
unresolved, as is how it sits against Screen Research's art masking (`positioning.md` §7). `[?]` throughout, and the
first question is not a field — it is whether this row should exist at all.

## `DT-12` — Spares & components

**Record: 13 / 58 · Assets: not audited · `G3`: current**

Tension bands · linear actuator 200 mm · 1500 mm draw-wire sensor · AC→12 V DC 8 A power supply.

`D1`–`D4` are self-evident and `D8` is the list above; the fields that matter for this row are **`A11`** (service
instructions) and **`O3`** — *the opportunity it opens* — because **buying a part instead of replacing an assembly
is a form of backing a dealer**, and that is the whole reason the row is worth keeping.

**One question, noted rather than pressed:** a draw-wire sensor as a general line item sits slightly against *"DT is
not a components/OEM supplier."* Spares for our own installed base are obviously right. The general components are
worth a look when someone is in the store data anyway.

---

## The knowledge layer — `N1`–`N9` — and why DT's version is a different problem

*Group 04 across the whole DT range: **0 of 9, and `R3` is unfilled on every family**, which is worse than it
sounds.*

**C-ATS is short of answers. DT is short of the questions.** The C-ATS record names thirteen questions and answers
two; a content backlog exists there and is merely thin. **For DT there is no list at all** — nothing says what a
dealer asks about a hush box, a port hole or a masking screen, so nothing can be ranked, and the production line
has nothing to draft from but the catalogue description. That is the same catalogue content that already failed:
two dozen competent product films at between 1 and 26 views (`../../motion/content.md`).

**And DT owns the audience.** Three-quarters of the estate's viewers are on DT's channel, running since 2018 with
~41,000 views. **The brand with the audience is the brand with no question list** — which is the most consequential
sentence on this page.

| ID | Field | State | Note |
|---|---|---|---|
| `N1` | Selection logic | **`[?]` — and it is DT's central question** | The whole range is **size-driven**: what determines a mount, an enclosure or a port hole is the dimensions of the unit and the room. **So "which one do I need?" is *the* DT question**, the site answers it today with projector-model tags, and `positioning.md` §1 explicitly says those tags are a sizing aid and **not** a claim of per-model engineering. There is no written sizing rule to replace them with |
| `N2` | The worked example | **`missing`** | No worked sizing example exists for any family |
| `N3` | The answers | **`missing` — no questions to answer** | `R3` unfilled on all nine families. **This is the first thing to fix, and it is an hour of listening rather than an hour of writing** |
| `N4` | Comparison | **`[?]`** | Future Automation and Screen Research are named in the strategy; nothing per product. Note the standing rule — position by capability, never disparagement, and **FA-copied-CAD is internal only** |
| `N5` | Compatibility & pairing | **partly derivable** | The cross-brand links are real and stated: acoustically transparent surfaces put C-ATS treatment and Pro-Fi speakers behind the image; concealment sits behind the Fabric Walls surface; the Screen Wall contains four brands. **Never written as pairing guidance a dealer could use** |
| `N6` | Project timing | **`[?]`, and it is DT's strongest unclaimed argument** | A port hole is an opening the builder must leave; a mount is a load path; a hush box is an extract route. **These are decided before the wall is closed** — far earlier than the AV order. Knowing that is exactly what a rep is for, and it is written nowhere |
| `N7` | What the dealer tells their client | **`missing`** | And DT is the brand where it matters most, because `positioning.md` §2 says the audience widens to **the architect and designer** — people the *dealer* has to persuade, in the dealer's own meeting, without us there |
| `N8` | Field learning | **`[?]`** | Prestigious installs exist; nothing captured |
| `N9` | What we are asked and cannot answer | **`[?]`** | Two candidates already visible: how far DT's remote diagnostics actually goes (`../../registers/backlog.md` US-6, capability assumed rather than known), and what the LED variant of the Screen Wall can be claimed to do |

**The cheapest thing on this page, and it is not writing.** `R3` and `N3` for nine families is **one conversation
with whoever answers DT support calls**, transcribed. It produces the DT content backlog, the fault-finding
priorities and the manual set's running order in a single pass — and until it happens, `DOC-14` (write the DT manual
set, *"large, finite"*) has no ranking to work to.

---

## What building the skeleton produced

**Four findings, none of which needed new research** — only somewhere to put what the repo already held:

1. **The Mistral Commander contradicts the control-stays-embedded rule**, and it is live on the store today. Either
   an unstated exception or an oversight; a minute to settle, and it would have gone on being invisible because
   nobody was looking at the range as a set.
2. **`D5` — what it is *not* for — is empty across the entire range**, and DT's products are size-driven, which
   makes **"right product, wrong size"** the characteristic and expensive DT failure. A sentence per family, and it
   does not exist anywhere.
3. **`D7` — what it requires from others — is the range's defining gap.** These are heavy, powered, ventilated
   things set into building fabric: an aperture the builder must leave, a load path, an extract route, a service
   access. **For DT this field is not documentation, it is the product's coordination story** — the thing the
   specifier needs before the wall is closed and the thing nobody can currently be sent.
4. **`DT-03` and possibly `FW-02` are mis-scoped**, which is the grouping doing its job: acoustic transparency and
   ambient-light rejection are different mechanisms, and the template's own test separates them.

**And the number that matters: ~13 of 58 fields, before anyone did any work.** The definitional layer was already
sitting in the repo, unassembled. What remains is genuinely unknown here and genuinely known by the people who build
these things — which is exactly the shape the record was designed to convert into questions.

**A fifth finding, from adding the knowledge layer:** the definitional gaps above are real but ordinary — they get
filled by someone who knows the products writing down what they know. **The knowledge gap is different in kind.**
`R3` and `N3` cannot be filled from the building; they are filled from *what dealers ask*, which means listening to
support and mining sent mail (`../../registers/backlog.md` CON-3), not consulting the engineering. **Those are two different
people and two different sessions**, and treating DT documentation as one job is why it has never started.
