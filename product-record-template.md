# The product record — the form

*Why this file exists, in one sentence: **`product-data-schema.md` says what to capture and why; nothing said what
shape it is captured in**, so every fill has been bespoke, nothing can be counted, and nothing downstream can be
generated from it reliably.*

The schema is the argument. This is the **form** — a fixed set of fields, in a fixed order, with stable IDs, so that
a record can be filled by anyone, diffed, scored for completeness, and read by a person or a machine without
interpretation. Same discipline as `backlog.md`: **IDs are stable and rows are regular** so the whole set can be
lifted into engine when the process gets a system home.

**Three rules carried down from the schema, unchanged:**

- **Engine owns the mechanical record.** SKU, name, weight, dimensions, stock, price. Not here, not duplicated
  here. A record that restates engine is a record that will go stale against it.
- **Every field has a stated consumer.** The generation gates at the bottom of this file are that stated consumer,
  made concrete. A field no output needs should be struck from the form, not filled in.
- **Definition before pitch.** Group A gets filled first. You cannot honestly say what problem a product solves
  until you have said what it is.

---

## Fill states — and the point of them

Every field carries one of four states. **This is what turns "the documentation is poor" into a number.**

| State | Written as | Means | Counts as |
|---|---|---|---|
| **Filled** | the answer | Known, sourced, current | Complete |
| **Gap** | `[?]` *(with what is missing)* | We know we don't know. **A named gap is progress** — it is a question someone can be sent to answer | Not complete, but **identified** |
| **Not applicable** | `n/a — reason` | Genuinely does not apply. The reason is mandatory; without it `n/a` is just a blank with confidence | Out of the denominator |
| **Untouched** | blank | Nobody has looked | Not complete, **not identified** — the worst state, and the one the form exists to eliminate |

**Two meters, and they measure different things.** Keep them apart:

- **Record completeness** = filled ÷ (applicable fields). The sales-and-marketing layer.
- **Asset completeness** = assets `current` ÷ applicable assets (group G). What a dealer can actually be given.

A product can be 100 % record-complete and 20 % asset-complete. That is a normal and useful state: it means we know
exactly what to make.

## Scope of a record — per mechanism, not per SKU

**One record per thing that behaves differently**, not per line item. Nine Dynamic masking screens that differ only
in size are **one** record with the sizes in D8; a Hush Box and a port hole are two records because they solve
different problems and fail differently. This is `decided.md` S11a applied to the form: DT's fifty-odd SKUs collapse
into roughly a dozen records, and the variant list lives in D8 where it belongs.

**The test:** if two items would produce the same install manual and the same failure modes, they are one record.

---

## The form

Copy the block at the bottom. Fields in order; **do not reorder or renumber** — downstream generation refers to IDs.

### A. What it actually is — `D1`–`D10`

*The foundation. Filled before anything below it.*

| ID | Field | Fill rule |
|---|---|---|
| `D1` | **What it is** | One sentence. Category, not pitch. This is the sentence every other asset inherits |
| `D2` | **What it does** | Its function, plainly. Not the benefit, not the mechanism |
| `D3` | **How it works** | The mechanism. The field that lets documentation be written per mechanism rather than per SKU |
| `D4` | **What it is for** | The intended applications, stated not implied |
| `D5` | **What it is *not* for** | Where it does not apply. **Misapplication is expensive** and nobody writes this down |
| `D6` | **Scope of supply** | What is actually in the box, including quantity/coverage rules |
| `D7` | **What it requires from others** | Power, data, structure, fixings, clearances, site conditions, adjacent products. The biggest single source of site pain |
| `D8` | **Configuration space** | Variants, sizes, options — and precisely what varies between them |
| `D9` | **Limits** | Maximum and minimum sizes, loads, environmental range. The honest edge of the envelope |
| `D10` | **Where it sits** | The layer of the room or system it belongs to, and what it meets |

### B. Why to buy it — `O1`–`O5`

*The on-ramp. Nothing operational needs these, which is exactly why they are missing everywhere.*

| ID | Field | Fill rule |
|---|---|---|
| `O1` | **The problem it solves, in the dealer's words** | Their phrasing, not ours — it is what gets searched and what an AI answer matches against. If it has not been heard from a dealer, mark `[?]`, do not compose one |
| `O2` | **The time or labour it saves** | Quantified where possible. The most under-used argument we have |
| `O3` | **The opportunity it opens** | What job it helps the dealer *win*, not merely fit |
| `O4` | **What it replaces or avoids** | Including doing nothing, which is the commonest alternative |
| `O5` | **Entry or flagship** | One of: `entry` · `flagship` · `neither`. Every brand needs a door-opener distinct from its showpiece |

### C. The doubt it has to remove — `R1`–`R4`

*The most valuable group here, and the one no operational system would ever hold.*

| ID | Field | Fill rule |
|---|---|---|
| `R1` | **The doubt it meets** | The specific objection, in the words it arrives in. Usually a question |
| `R2` | **The load-bearing asset** | Which single asset removes that doubt. **Decides what to make first** — the rest is documented equally only when there is time |
| `R3` | **The questions it generates** | Pre-sale and on site. The same question at different moments. This is the content backlog, per product |
| `R4` | **What goes wrong on site** | The installer's real fear, and what peer reputation is made of |

### D. Who decides on it — `W1`–`W2`

*Engine knows who bought it. It does not know who specified it, and those are different people.*

| ID | Field | Fill rule |
|---|---|---|
| `W1` | **Purchaser vs specifier** | Who buys, who specifies, and whether they are the same. Names roles, never companies |
| `W2` | **Who signs it off, and what convinces them** | Different parties are reassured by different things — a finish sample, a measured report, an install time |

### E. What we may and may not say — `G1`–`G4`

*Governance, and it belongs in the record rather than in someone's memory.*

| ID | Field | Fill rule |
|---|---|---|
| `G1` | **Claims supported** | Each with its test standard and report reference. No superlative without a measurement behind it |
| `G2` | **Claims deliberately not made** | The credibility boundary, written down so a writer cannot cross it without knowing it exists |
| `G3` | **Marketing status** | One of: `pre-release` · `demonstrable, undocumented` · `current` · `discontinued`. **Build it, then say it** |
| `G4` | **Proof available, and publishable?** | What exists, and whether it may be shown. At this tier the best jobs are the least publishable |

### F. Where it is sold — `C1`–`C2`

| ID | Field | Fill rule |
|---|---|---|
| `C1` | **Channel** | One of: `srnd.store` (trade) · `Cinema Store` · `trade-only, not listed` · `embedded — not sold separately`. **No product exists in two places** |
| `C2` | **Territory availability** | Any restriction or exclusivity. A vacated territory should be visibly open |

### G. The asset audit — `A1`–`A11`

*Each carries a state: **`current`** · **`exists — stale`** · **`missing`** · **`n/a — reason`**. This group is what
makes the debt countable.*

| ID | Asset | Primarily for |
|---|---|---|
| `A1` | Datasheet | Specifier, dealer evaluating |
| `A2` | Dimensioned drawings | Specifier, installer |
| `A3` | CAD | Specifier — *publish-versus-gate decision outstanding (`backlog.md` DEC-5)* |
| `A4` | BIM / Revit object | Architect |
| `A5` | NBS clause | Spec writer |
| `A6` | Install manual | Installer on site — the highest-intent reader we will ever have |
| `A7` | Commissioning / calibration guide | Installer, integrator |
| `A8` | Fault-finding guide | Installer, support |
| `A9` | "How do you do X" video | Installer — the atom of the corpus |
| `A10` | Training module | Certification — assembled from the above, never authored separately |
| `A11` | Spares and service instructions | Installer, support |

### H. Record keeping — `K1`–`K3`

| ID | Field | Fill rule |
|---|---|---|
| `K1` | **Record owner** | A role, never a name (`decided.md` S27) |
| `K2` | **Last reviewed** | Date |
| `K3` | **Review interval** | **A record with no review date is not complete** — a stale answer is worse than no answer, because a dealer acts on it |

---

## What the filled record produces — the generation gates

**This is the half that makes filling it worth anyone's time.** Each output below names the fields it needs. Two
consequences, both deliberate:

1. **You can tell what is generatable today.** If the fields are filled, the piece can be drafted; if not, the
   missing field is the blocker, and it is a specific question rather than "we should do some marketing."
2. **You fill against demand, not alphabetically.** Filling `O1`, `R1` and `R3` across a whole range unlocks the
   hooks and the content backlog for every product in it. Filling one product to 100 % unlocks one product.

| Output | Fields required | Notes |
|---|---|---|
| **Hook / campaign silo** | `O1` `R1` `R3` | Wording set by an owner, never generic (`backlog.md` JNY-4) |
| **Site on-ramp block** (S15) | `D1` `O1` `O2` `O3` | The on-ramp half of the information architecture |
| **Product page — technical depth** (S15) | `D1`–`D10` `G1` `G2` | The depth half. There to remove doubt, not to persuade |
| **Store listing** | `D1` `D6` `D8` `C1` `G3` | `G3` gates it: nothing `pre-release` gets listed |
| **Datasheet** | `D1`–`D9` `G1` `G2` `G3` `A2` | The first doubt-removal document anyone opens |
| **Install manual** | `D6` `D7` `D8` `R4` | Organised by moment, not by product structure |
| **"How do you do X" video** | `R4` `R3` | One failure mode per piece. The cheapest thing we make |
| **Fault-finding guide** | `R4` `R3` `D7` | Most support volume, answered once |
| **Comparison / objection content** | `O4` `R1` `G1` `G2` | The dealer is choosing between options, including doing nothing |
| **Cross-sell prompt** (`backlog.md` XS-1) | `D10` `D7` `O3` | The physical adjacency is what justifies the prompt |
| **Specifier pack decision** | `W1` `W2` `A3`–`A5` | Whether this product needs NBS/Revit/samples at all, or only an install guide |
| **Case study** | `G4` | Publishability is the gate, and it is checked before writing, not after |
| **Training module** | `A6`–`A9` | Assembled from the corpus (`decided.md` S12), never authored separately |

**Two hard gates, and they are not stylistic.**

- **`G3` gates publication of anything.** A product that is `pre-release` or `demonstrable, undocumented` generates
  internal material only. This one field would have caught three live errors: the Screen Wall, the C-ATS commercial
  range, and REV-CP-12.
- **`G2` gates every claim.** A writer working from a record with `G2` filled cannot cross a credibility boundary
  without seeing it first. That is the entire mechanism — *scattering, never diffusion* only survives if it is
  written next to the product it applies to.

---

## The blank form

```markdown
## <Product or mechanism family> — `<ID>`

**Record:** __ / __ fields · **Assets:** __ / __ current · **Status (G3):** ___

### A. What it actually is
| ID | Field | Value |
|---|---|---|
| D1 | What it is | |
| D2 | What it does | |
| D3 | How it works | |
| D4 | What it is for | |
| D5 | What it is *not* for | |
| D6 | Scope of supply | |
| D7 | What it requires from others | |
| D8 | Configuration space | |
| D9 | Limits | |
| D10 | Where it sits | |

### B. Why to buy it
| ID | Field | Value |
|---|---|---|
| O1 | Problem, in the dealer's words | |
| O2 | Time or labour saved | |
| O3 | Opportunity it opens | |
| O4 | What it replaces or avoids | |
| O5 | Entry or flagship | |

### C. The doubt it removes
| ID | Field | Value |
|---|---|---|
| R1 | The doubt it meets | |
| R2 | Load-bearing asset | |
| R3 | Questions it generates | |
| R4 | What goes wrong on site | |

### D. Who decides
| ID | Field | Value |
|---|---|---|
| W1 | Purchaser vs specifier | |
| W2 | Who signs off, and what convinces them | |

### E. What we may and may not say
| ID | Field | Value |
|---|---|---|
| G1 | Claims supported | |
| G2 | Claims not made | |
| G3 | Marketing status | |
| G4 | Proof, and publishable? | |

### F. Where it is sold
| ID | Field | Value |
|---|---|---|
| C1 | Channel | |
| C2 | Territory | |

### G. Assets
| A1 datasheet | A2 drawings | A3 CAD | A4 BIM | A5 NBS | A6 install | A7 commissioning | A8 fault-finding | A9 video | A10 training | A11 spares |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

### H. Record keeping
**Owner:** — · **Last reviewed:** — · **Review interval:** —
```

---

## How this gets used

1. **The roster is `product-register.md`.** Every product in the group, its record status and its meters. Start
   there; it is what says which record to open next.
2. **Records live with the brand** — `brands/<brand>/product-records.md`. The form is group; the fill is brand
   (`CLAUDE.md`, group ≠ brand).
3. **Rank by `R3`, not alphabetically.** The questions-generated field, cross-checked against what the sent-mail
   archive says actually recurs (`backlog.md` CON-3), is the order to work in.
4. **Fill a field group across a range before filling one product deeply**, unless a specific output is waiting on
   it. The gates above say which unlocks most.
5. **Completeness gates new products** (`decided.md` S16). A product without `D1`–`D10` and `G3` does not get a
   store listing. That is the only version of this that stops the debt returning.

*First cut, for correction. Every field is a claim that some output needs it — a field no output needs should be
struck, and a missing field that an output needs should be added.*
