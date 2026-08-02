# The product record — the form

*Why this file exists, in one sentence: **`product-data-schema.md` says what to capture and why; nothing said what
shape it is captured in**, so every fill has been bespoke, nothing can be counted, and nothing downstream can be
generated from it reliably.*

The schema is the argument. This is the **form** — a fixed set of fields, in a fixed order, with stable IDs, so that
a record can be filled by anyone, diffed, scored for completeness, and read by a person or a machine without
interpretation. Same discipline as `backlog.md`: **IDs are stable and rows are regular** so the whole set can be
lifted into engine when the process gets a system home.

> **Corrected 2026-08-02, and it changes what the record is for.** The first cut treated this as *product data*.
> But **content is the sales rep** (`decided.md` S1–S9), and the production line's step 1 is *"substance in — the
> atoms that already exist: **the product records**, the measured data, the archive…"* with the standing rule that
> Claude *"multiplies pieces from that substance; it never invents claims"* (`group/09-motion-design.md`,
> component 2). **So the record is not a specification. It is the database the rep speaks from** — and a record
> holding only definition and an index of questions gives the line nothing to multiply but the definition. Hence
> **group D, the knowledge layer**, below. It is the half that was missing, and it is the half that matters.

**Three rules carried down from the schema, unchanged:**

- **Engine owns the mechanical record.** SKU, name, weight, dimensions, stock, price. Not here, not duplicated
  here. A record that restates engine is a record that will go stale against it.
- **Every field has a stated consumer.** The generation gates at the bottom of this file are that stated consumer,
  made concrete. A field no output needs should be struck from the form, not filled in.
- **Definition before pitch.** Group A gets filled first. You cannot honestly say what problem a product solves
  until you have said what it is.
- **And knowledge before content.** Group D is what a rep carries. Nothing downstream of it can be produced
  without it, and no amount of production capacity substitutes for it.

---

## Fill states — and the point of them

Every field carries one of four states. **This is what turns "the documentation is poor" into a number.**

| State | Written as | Means | Counts as |
|---|---|---|---|
| **Filled** | the answer | Known, sourced, current | Complete |
| **Gap** | `[?]` *(with what is missing)* | We know we don't know. **A named gap is progress** — it is a question someone can be sent to answer | Not complete, but **identified** |
| **Not applicable** | `n/a — reason` | Genuinely does not apply. The reason is mandatory; without it `n/a` is just a blank with confidence | Out of the denominator |
| **Untouched** | blank | Nobody has looked | Not complete, **not identified** — the worst state, and the one the form exists to eliminate |

**Three meters, and they measure different things.** Keep them apart:

- **Record completeness** = filled ÷ applicable fields. The sales-and-marketing layer.
- **Knowledge completeness** = group D filled ÷ 9, plus **`R3` questions answered ÷ `R3` questions named**. What the
  rep can actually say.
- **Asset completeness** = assets `current` ÷ applicable assets (group H). What a dealer can be given.

A product can be 100 % record-complete and 20 % asset-complete: normal and useful — it means we know what to make.
**But a product that is record-complete and knowledge-empty is the dangerous state**, because it looks finished. It
has a definition, an on-ramp and a list of the questions it provokes, and it still cannot hold a conversation.
**Report the knowledge meter first.**

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

*The index of what the product has to overcome. **It names the questions; group D holds the answers**, and the two
are only useful together — `R3` without `N3` is a list of things we are known to be asked and known not to answer.*

| ID | Field | Fill rule |
|---|---|---|
| `R1` | **The doubt it meets** | The specific objection, in the words it arrives in. Usually a question |
| `R2` | **The load-bearing asset** | Which single asset removes that doubt. **Decides what to make first** — the rest is documented equally only when there is time |
| `R3` | **The questions it generates** | Pre-sale and on site. The same question at different moments. This is the content backlog, per product |
| `R4` | **What goes wrong on site** | The installer's real fear, and what peer reputation is made of |

### D. The knowledge layer — `N1`–`N9`

***This is the group the whole exercise exists for.*** Group C names the questions; **this group holds the
answers**, plus everything else a good rep carries in their head. It is the substance the production line runs on,
and **it is the only group that cannot be derived from any other** — engine does not hold it, the website does not
hold it, and it is currently distributed across two or three people's memories and a decade of sent mail.

**The test for whether a record is worth anything: could someone who has never seen the product hold a competent
conversation with a dealer using only group D?** Today, for every product in the group, the answer is no.

| ID | Field | Fill rule |
|---|---|---|
| `N1` | **Selection logic** | How you choose it, and how many. The rule stated so a dealer can apply it themselves — quantity per room size, placement rule, the "it depends" made explicit. **The single commonest live question in every brand** |
| `N2` | **The worked example** | One real room, start to finish, with the numbers shown. Not a case study — an arithmetic demonstration. C-ATS has already *decided* this is the self-serve route in place of a public calculator (`brands/c-ats/positioning.md` §1) |
| `N3` | **The answers** | **One row per question in `R3`**: the question, the answer in the owner's words, its source, and where it is published. An unanswered `R3` entry is a question we are known to receive and known not to answer |
| `N4` | **Comparison** | Versus the named alternatives (`group/06-competitors.md`), dimension by dimension. What we genuinely do better, **and where a competitor is genuinely better** — a rep who cannot say that is not trusted twice |
| `N5` | **Compatibility & pairing** | What it works with, ours and other people's; what it must never be paired with; the physical adjacency that justifies the cross-sell |
| `N6` | **Project timing** | When in a project this is decided, what it blocks if decided late, and who is in the room at that moment. **A rep's real value is knowing when to be there** |
| `N7` | **What the dealer tells their client** | The non-technical explanation the dealer repeats to someone who is paying and cannot judge it. **Depth spent on the dealer's customer reads as generosity** (`CLAUDE.md`) — this field is that principle made into a deliverable, and it is empty for every product in the group |
| `N8` | **Field learning** | What real jobs have taught since launch. Accumulates; never rewritten, only added to. The record of a product actually being used |
| `N9` | **What we are asked and cannot answer** | The honest edge. **Every entry is a decision waiting**: commission the test, or stop being asked by saying plainly that we do not claim it |

**Two rules specific to this group, because it is the one that can go wrong.**

- **`N3` is transcription, not authorship.** The answer comes from whoever actually knows it — recorded, not
  composed. *"Ten minutes of an owner talking, once"* (`NEXT.md` lane 6) fills more of this group than a week of
  writing, and it is the only version that is true.
- **`N9` is filled honestly or not at all.** A record that claims no unanswerable questions is a record nobody has
  tested against a real dealer.

### E. Who decides on it — `W1`–`W2`

*Engine knows who bought it. It does not know who specified it, and those are different people.*

| ID | Field | Fill rule |
|---|---|---|
| `W1` | **Purchaser vs specifier** | Who buys, who specifies, and whether they are the same. Names roles, never companies |
| `W2` | **Who signs it off, and what convinces them** | Different parties are reassured by different things — a finish sample, a measured report, an install time |

### F. What we may and may not say — `G1`–`G4`

*Governance, and it belongs in the record rather than in someone's memory.*

| ID | Field | Fill rule |
|---|---|---|
| `G1` | **Claims supported** | Each with its test standard and report reference. No superlative without a measurement behind it |
| `G2` | **Claims deliberately not made** | The credibility boundary, written down so a writer cannot cross it without knowing it exists |
| `G3` | **Marketing status** | One of: `pre-release` · `demonstrable, undocumented` · `current` · `discontinued`. **Build it, then say it** |
| `G4` | **Proof available, and publishable?** | What exists, and whether it may be shown. At this tier the best jobs are the least publishable |

### G. Where it is sold — `C1`–`C2`

| ID | Field | Fill rule |
|---|---|---|
| `C1` | **Channel** | One of: `srnd.store` (trade) · `Cinema Store` · `trade-only, not listed` · `embedded — not sold separately`. **No product exists in two places** |
| `C2` | **Territory availability** | Any restriction or exclusivity. A vacated territory should be visibly open |

### H. The asset audit — `A1`–`A11`

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

### I. Record keeping — `K1`–`K3`

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

**The table is ordered deliberately, and the divider in it is the finding.**

| Output | Fields required | Notes |
|---|---|---|
| **Store listing** | `D1` `D6` `D8` `C1` `G3` | `G3` gates it: nothing `pre-release` gets listed |
| **Datasheet** | `D1`–`D9` `G1` `G2` `G3` `A2` | The first doubt-removal document anyone opens |
| **Product page — technical depth** (S15) | `D1`–`D10` `G1` `G2` | The depth half. There to remove doubt, not to persuade |
| **Site on-ramp block** (S15) | `D1` `O1` `O2` `O3` | The on-ramp half of the information architecture |
| **Install manual** | `D6` `D7` `D8` `R4` **`N1`** | Organised by moment, not by product structure. `N1` is why it is installed *right*, not merely installed |
| **Specifier pack decision** | `W1` `W2` `A3`–`A5` | Whether this needs NBS/Revit/samples at all, or only an install guide |
| **Case study** | `G4` **`N8`** | Publishability is the gate, checked before writing. `N8` is what the job actually taught |
| — *the line above generates from definition; below, nothing generates without group D* — | | |
| **The knowledge base** — the corpus itself | **`N3`** `R3` | **One article per answered question.** This is the whole content estate, and it is one field |
| **Hook / campaign silo** | `O1` `R1` `R3` **`N3`** | A hook with no answer behind it sends a dealer to a dead end (`backlog.md` CON-8) |
| **"How do you do X" video** | `R4` `R3` **`N3`** | One failure mode per piece. The cheapest thing we make — and it is a *person answering*, so `N3` is the script |
| **Fault-finding guide** | `R4` `D7` **`N3`** | Most support volume, answered once |
| **"How many do I need" / selection guide** | **`N1` `N2`** | The commonest live question in every brand, and there is no output for it today |
| **Design tool / calculator spec** (`group/07-tools.md`) | **`N1` `N2`** `D9` | A tool is `N1` made executable. Building one without `N1` written down is how a tool contradicts the design service |
| **Comparison / objection content** | `O4` `R1` `G1` `G2` **`N4`** | The dealer is choosing between options, including doing nothing |
| **Cross-sell prompt** (`backlog.md` XS-1) | `D10` `D7` `O3` **`N5` `N6`** | Physical adjacency justifies it; **`N6` says when to say it**, which is the whole trick |
| **The spec-conversation prompt list** | **`N5` `N6`** | Our only discovery channel, and it runs on timing knowledge (`NEXT.md` lane 4) |
| **Dealer-facing sales material** — what they tell their client | **`N7`** | **Nothing in the estate produces this today.** It is the moat expressed as a deliverable |
| **Training module** | `A6`–`A9` **`N1`–`N4`** | Assembled from the corpus (`decided.md` S12), never authored separately |
| **The testing / commissioning decisions** | **`N9`** | Each unanswerable is either a test to buy or a claim to stop making. Not content — a spending decision |

**Read that table as one fact:** everything above the divider can be produced from the record as it stands today, and
**every one of those outputs is a document.** Everything below the divider is what a *rep* does — answering, sizing,
comparing, timing, arming the dealer — and none of it can be produced at all. **The estate can currently generate
paperwork and cannot generate a salesperson**, which is precisely the thing content was supposed to replace.

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

**Record:** __ / 39 fields · **Knowledge:** __ / 9 + __ of __ questions answered · **Assets:** __ / 11 current · **Status (G3):** ___

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

### D. The knowledge layer
| ID | Field | Value |
|---|---|---|
| N1 | Selection logic — which, and how many | |
| N2 | The worked example | |
| N4 | Comparison, versus named alternatives | |
| N5 | Compatibility & pairing | |
| N6 | Project timing — when it is decided | |
| N7 | What the dealer tells their client | |
| N8 | Field learning | |
| N9 | What we are asked and cannot answer | |

**N3 — the answers.** One row per `R3` question. *State: `answered` (written down) · `known` (in someone's head,
unrecorded) · `unanswered`.*

| Question (from `R3`) | Answer | Source / whose words | State | Published where |
|---|---|---|---|---|
| | | | | |

### E. Who decides
| ID | Field | Value |
|---|---|---|
| W1 | Purchaser vs specifier | |
| W2 | Who signs off, and what convinces them | |

### F. What we may and may not say
| ID | Field | Value |
|---|---|---|
| G1 | Claims supported | |
| G2 | Claims not made | |
| G3 | Marketing status | |
| G4 | Proof, and publishable? | |

### G. Where it is sold
| ID | Field | Value |
|---|---|---|
| C1 | Channel | |
| C2 | Territory | |

### H. Assets
| A1 datasheet | A2 drawings | A3 CAD | A4 BIM | A5 NBS | A6 install | A7 commissioning | A8 fault-finding | A9 video | A10 training | A11 spares |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

### I. Record keeping
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
5. **`N3` is filled by recording, not by writing.** Take the ranked `R3` list into a session, ask the questions, and
   transcribe. **Ten minutes of an owner talking fills more of group D than a week of drafting**, and it is the only
   version that carries the authority — the substance stays human, the multiplication does not
   (`group/09-motion-design.md` component 2). Filling `N3` by composition would be inventing claims, which the line
   forbids.
5. **Completeness gates new products** (`decided.md` S16). A product without `D1`–`D10` and `G3` does not get a
   store listing. That is the only version of this that stops the debt returning.

*First cut, for correction. Every field is a claim that some output needs it — a field no output needs should be
struck, and a missing field that an output needs should be added.*
