# The product record — the form

*Why this file exists, in one sentence: **`registers/record-schema.md` says what to capture and why; nothing said what
shape it is captured in**, so every fill has been bespoke, nothing can be counted, and nothing downstream can be
generated from it reliably.*

The schema is the argument. This is the **form** — a fixed set of fields, in a fixed order, with stable IDs, so that
a record can be filled by anyone, diffed, scored for completeness, and read by a person or a machine without
interpretation. Same discipline as `registers/backlog.md`: **IDs are stable and rows are regular** so the whole set can be
lifted into engine when the process gets a system home.

> **What the record is for.** **Content is the sales rep** (`decided.md` S1–S9), and the production line's step 1
> is *"substance in — the atoms that already exist: **the product records**, the measured data, the archive…"*
> with the standing rule that Claude *"multiplies pieces from that substance; it never invents claims"*
> (`motion/motion-design.md`, component 2). **So the record is not a specification. It is the database the rep
> speaks from.**

**The form is built against the rep test** (`registers/record-schema.md`, part one — which also maps a rep's and a
marketing executive's actual weekly tasks onto the fields each one consumes and feeds). A rep does four jobs; the
record is done when it can do all four without them:

| Job | Test | Groups that serve it |
|---|---|---|
| **1 · Attract** — make it as attractive as it honestly is | Can you start a conversation a dealer wants to have? **Every hook comes from here** | **08** hook · 02 on-ramp · 04 knowledge |
| **2 · Defend** — hold it against the alternatives | Can you win the comparison, including against the incumbent and against doing nothing? | **05** competitive · 04 knowledge · 10 claims |
| **3 · Build trust** | Can you be believed? The proof, the honest limits, **and the claims we refuse to make** | 03 doubt · 10 claims · 04 knowledge |
| **4 · Deliver** — every question answered, through to a working install | Can a dealer reach a working room without asking us anything? | 01 definition · **07** lifecycle · 04 knowledge · 12 assets |

**Jobs 1 and 2 are one piece of work.** A claim you cannot defend is a hook that costs you the dealer the moment
it meets a competitor's answer. **Groups 05–08 carry the front half** — the competitive comparison, the dealer's
business case, and what a product can honestly be hooked on.

**Three rules carried down from the schema, unchanged:**

- **Engine owns the mechanical record.** SKU, name, weight, dimensions, stock, price. Not here, not duplicated
  here. A record that restates engine is a record that will go stale against it.
- **Every field has a stated consumer.** The generation gates at the bottom of this file are that stated consumer,
  made concrete. A field no output needs should be struck from the form, not filled in.
- **Definition before pitch.** Group **01** gets filled first. You cannot honestly say what problem a product
  solves until you have said what it is.
- **And knowledge before content.** Group **04** is what a rep carries. Nothing downstream of it can be produced
  without it, and no amount of production capacity substitutes for it.
- **Four identifier sets, none of them overlapping.** Groups are numbered `01`–`13`; **fields are lettered**
  (`D1`, `X6`, `N3`); capture routes are `RT1`–`RT6`; tasks are `T-S…` / `T-M…` (`motion/tasks.md`). Jobs are
  plain ordinals 1–4, and **domains carry no identifier at all** — the dealer's question names them. Keep the
  sets apart: any new identifier goes in one of these shapes or it collides with an existing one.

---

## Fill states — and the point of them

Every field carries one of four states. **This is what turns "the documentation is poor" into a number.**

| State | Written as | Means | Counts as |
|---|---|---|---|
| **Filled** | the answer | Known, sourced, current | Complete |
| **Gap** | `[?]` *(with what is missing)* | We know we don't know. **A named gap is progress** — it is a question someone can be sent to answer | Not complete, but **identified** |
| **Not applicable** | `n/a — reason` | Genuinely does not apply. The reason is mandatory; without it `n/a` is just a blank with confidence | Out of the denominator |
| **Untouched** | blank | Nobody has looked | Not complete, **not identified** — the worst state, and the one the form exists to eliminate |

**Four meters, and they measure different things.** Keep them apart, and **report them in this order**:

- **Rep-test coverage** — can it attract · defend · be believed · deliver? **Four yes/no answers, and the only
  measure that matters.** A record can be most of the way full and fail three of them. **Whoever owns the record
  answers these, not whoever built the form** — a coverage verdict is a judgement about the business, not an
  arithmetic result.
- **Knowledge completeness** = group 04 filled ÷ 9, plus **`R3` questions answered ÷ `R3` questions named**. What
  the rep can actually say.
- **Record completeness** = filled ÷ applicable fields (58 in total). The breadth measure — **of the form, not of
  what is known about the product.** See below.
- **Asset completeness** = assets `current` ÷ applicable assets (group 12). What a dealer can be given.

A product can be 100 % record-complete and 20 % asset-complete: normal and useful — it means we know what to make.
**The dangerous states are the ones that look finished:** record-complete and knowledge-empty (it has a definition,
an on-ramp and a list of the questions it provokes, and cannot hold a conversation), or well-filled on the back
half and empty on the front (it can answer a dealer who already wants it, and cannot get one).

## What the meters can and cannot tell you

**A database confirms what you know. It cannot report what you do not know** (Neil, 2026-08-02). Three
consequences, and they bind every count in this repo:

- **A filled field confirms something.** An empty one confirms nothing — it means the answer does not exist, or
  nobody has looked, **or the field is the wrong question.** The record cannot tell you which, so a blank is a
  prompt to go and ask, never a finding in itself.
- **The denominator is a claim.** *28 of 58* assumes 58 is the right list of things to know about a product. It is
  the list this form currently proposes. **Completeness measures the form, not the knowledge** — a record at 100 %
  against a wrong field list is complete and useless.
- **Only contact with the world finds the missing fields.** The capture routes are the only input that can
  introduce something the form did not anticipate — **and only if they are open-ended.** A route that records
  solely against known fields returns only known things.

**So every route carries an overflow.** Alongside the fields it fills, one free line: *what came up that no field
covers.* That line is where new fields come from, and it is the only part of this system that can grow the form
rather than fill it. The clearest case is `R3`: the questions dealers actually ask will include ones no field
anticipated, and those are the valuable ones.

## Scope of a record — per mechanism, not per SKU

**One record per thing that behaves differently**, not per line item. Nine Dynamic masking screens that differ only
in size are **one** record with the sizes in D8; a Hush Box and a port hole are two records because they solve
different problems and fail differently. This is `decided.md` S11a applied to the form: DT's fifty-odd SKUs collapse
into roughly a dozen records, and the variant list lives in D8 where it belongs.

**The test:** if two items would produce the same install manual and the same failure modes, they are one record.

---

## The form

Copy the block at the bottom. Fields in order; **do not reorder or renumber** — downstream generation refers to IDs.

### 01 · What it actually is — `D1`–`D10`

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

### 02 · Why to buy it — `O1`–`O5`

*The on-ramp. Nothing operational needs these, which is exactly why they are missing everywhere.*

| ID | Field | Fill rule |
|---|---|---|
| `O1` | **The problem it solves, in the dealer's words** | Their phrasing, not ours — it is what gets searched and what an AI answer matches against. If it has not been heard from a dealer, mark `[?]`, do not compose one |
| `O2` | **The time or labour it saves** | Quantified where possible. The most under-used argument we have |
| `O3` | **The opportunity it opens** | What job it helps the dealer *win*, not merely fit |
| `O4` | **What it replaces or avoids** | Including doing nothing, which is the commonest alternative |
| `O5` | **Entry or flagship** | One of: `entry` · `flagship` · `neither`. Every brand needs a door-opener distinct from its showpiece |

### 03 · The doubt it has to remove — `R1`–`R4`

*The index of what the product has to overcome. **It names the questions; group 04 holds the answers**, and the two
are only useful together — `R3` without `N3` is a list of things we are known to be asked and known not to answer.*

| ID | Field | Fill rule |
|---|---|---|
| `R1` | **The doubt it meets** | The specific objection, in the words it arrives in. Usually a question |
| `R2` | **The load-bearing asset** | Which single asset removes that doubt. **Decides what to make first** — the rest is documented equally only when there is time |
| `R3` | **The questions it generates** | Pre-sale and on site. The same question at different moments. This is the content backlog, per product |
| `R4` | **What goes wrong on site** | The installer's real fear, and what peer reputation is made of |

### 04 · The knowledge layer — `N1`–`N9`

***This is the group the whole exercise exists for.*** Group 03 names the questions; **this group holds the
answers**, plus everything else a good rep carries in their head. It is the substance the production line runs on,
and **it is the only group that cannot be derived from any other** — engine does not hold it, the website does not
hold it, and it is currently distributed across two or three people's memories and a decade of sent mail.

**The test for whether a record is worth anything: could someone who has never seen the product hold a competent
conversation with a dealer using only group 04?** Today, for every product in the group, the answer is no.

| ID | Field | Fill rule |
|---|---|---|
| `N1` | **Selection logic** | How you choose it, and how many. The rule stated so a dealer can apply it themselves — quantity per room size, placement rule, the "it depends" made explicit. **The single commonest live question in every brand** |
| `N2` | **The worked example** | One real room, start to finish, with the numbers shown. Not a case study — an arithmetic demonstration. C-ATS has already *decided* this is the self-serve route in place of a public calculator (`brands/c-ats/positioning.md` §1) |
| `N3` | **The answers** | **One row per question in `R3`**: the question, the answer in the owner's words, its source, and where it is published. An unanswered `R3` entry is a question we are known to receive and known not to answer |
| `N4` | **Comparison** | Versus the named alternatives (`group-strategy/competitors.md`), dimension by dimension. What we genuinely do better, **and where a competitor is genuinely better** — a rep who cannot say that is not trusted twice |
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

### 05 · Competitive — how it is defended — `X1`–`X6`

*Rep job 2. **The record previously did this whole job with one field.** Making something attractive and defending
it are the same work: a claim that cannot survive a competitor's answer is a hook that costs you the dealer.
Governed hardest by the standing discipline — **position by capability, never disparagement**, and never in public
copy as an attack.*

| ID | Field | Fill rule |
|---|---|---|
| `X1` | **The named alternatives** | What the dealer is actually choosing between, including **the one they already buy** and doing nothing |
| `X2` | **The dimensions it turns on** | The two or three that decide it in this category. Arguing the others is noise |
| `X3` | **Where we win** | Dimension by dimension, **with the measurement behind it or it is not a claim** |
| `X4` | **Where they win** | **The field that makes the other three believable.** The dealer already knows the answer; a rep who concedes nothing is not trusted twice. Also the honest input to product development |
| `X5` | **The switch argument** | What to say to a dealer who already buys the alternative — an incumbent relationship, not a cold pitch |
| `X6` | **Why deals are lost** | One line per loss, accumulating: which competitor, which dimension, which stage. **The only outside view we have, and it ranks everything above it** |

### 06 · Commercial — the dealer's business case — `M1`–`M5`

*Rep job 1 and 4. **Not price.** Price is engine's, is partner-gated and is never published. This is the argument
around it — and group commercial policy (terms, credit, territory) is not product data and stays in `decided.md`.*

| ID | Field | Fill rule |
|---|---|---|
| `M1` | **Order unit and minimum** | Boxes not panels, sheets not metres. After scope of supply, the commonest cause of a wrong first order |
| `M2` | **Lead time, and what changes it** | The question that decides whether we are specified on a live project at all |
| `M3` | **Availability posture** | `stocked` · `made to order` · `made to size`. Different products want different promises |
| `M4` | **The dealer's business case** | Margin position against the alternative, **plus what it costs them in labour** to install and support. *A cheaper product that takes two more days on site is not cheaper* |
| `M5` | **What not specifying it costs them** | The callback, the room that underperforms, the unhappy client. The honest version of urgency |

### 07 · Lifecycle & support — the way to install, and after — `L1`–`L5`

*Rep job 4. The asset audit (group 12) records whether the **documents** exist; this group holds the **facts** — and
a dealer on the way to install asks for the facts.*

| ID | Field | Fill rule |
|---|---|---|
| `L1` | **Order to site** | What arrives, when, in what state, and what must be ready for it |
| `L2` | **Install sequence, and who does it** | Where it sits in the build order; whether it needs a specialist. **Fabric Walls' entire proposition is an answer to this field** |
| `L3` | **Commissioning & verification** | Where a good product still becomes a bad room. Also the G5 signal |
| `L4` | **Serviceability** | What can be replaced without pulling the assembly. A purchasing argument as much as a support one |
| `L5` | **What we support, and for how long** | The substance behind *"support is part of the sales proposition, not a cost behind it"* |

### 08 · Hook material — `H1`–`H3`

*Rep job 1, and **the source the hook machinery does not currently have.** `motion/motion-design.md` designs many
hooks per door by appeal category; volume is deliberate. **Volume without a source means hooks get invented per
campaign**, which the production line forbids. This group holds the material; **the matrix holds the wording**
(`registers/backlog.md` JNY-4) — keeping them apart is what stops the record turning into copy.*

| ID | Field | Fill rule |
|---|---|---|
| `H1` | **Which appeals it can honestly carry** | Against the five: *more revenue · time saved · easier to do · better results · the problem named*. Each marked `carries — substance` or `empty`. **Marking one empty is as useful as filling it** — it stops a hook being stretched into a claim we cannot defend |
| `H2` | **The single most interesting true thing about it** | Every product has one, and it is rarely what the datasheet leads with. C-ATS's ~300 mm tolerance sat unused for years |
| `H3` | **What has actually bitten** | Hooks issued and which caught, source-tagged (`decided.md` S23). Turns hook volume from guesswork into evidence |

### 09 · Who decides on it — `W1`–`W2`

*Engine knows who bought it. It does not know who specified it, and those are different people.*

| ID | Field | Fill rule |
|---|---|---|
| `W1` | **Purchaser vs specifier** | Who buys, who specifies, and whether they are the same. Names roles, never companies |
| `W2` | **Who signs it off, and what convinces them** | Different parties are reassured by different things — a finish sample, a measured report, an install time |

### 10 · What we may and may not say — `G1`–`G4`

*Governance, and it belongs in the record rather than in someone's memory.*

| ID | Field | Fill rule |
|---|---|---|
| `G1` | **Claims supported** | Each with its test standard and report reference. No superlative without a measurement behind it |
| `G2` | **The claims we refuse to make** | **A wording boundary, not modesty.** These are claims that would be untrue or unsupported — written next to the product so a writer cannot cross the line without seeing it. C-ATS never says *diffusion*, because the mechanism is scattering. DT never says *engineered to your exact projector*, because the products are size-driven |
| `G3` | **Marketing status** | One of: `pre-release` · `demonstrable, undocumented` · `current` · `discontinued`. **Build it, then say it** |
| `G4` | **Proof available, and publishable?** | What exists, and whether it may be shown. At this tier the best jobs are the least publishable |

### 11 · Where it is sold — `C1`–`C2`

| ID | Field | Fill rule |
|---|---|---|
| `C1` | **Channel** | One of: `srnd.store` (trade) · `Cinema Store` · `trade-only, not listed` · `embedded — not sold separately`. **No product exists in two places** |
| `C2` | **Territory availability** | Any restriction or exclusivity. A vacated territory should be visibly open |

### 12 · The asset audit — `A1`–`A11`

*Each carries a state: **`current`** · **`exists — stale`** · **`missing`** · **`n/a — reason`**. This group is what
makes the debt countable.*

> **This group has a system home, found 2026-08-13 (`evidence/engine-audit.md` §1, group 12).** Engine's `doc_document`
> already carries `status`, **`stale`** and `last_published_at` — this group's state vocabulary, implemented — with
> templates that *generate* `A1` and `A6` (a Pro-Fi speaker datasheet, a DT screen manual), a `content_snapshot`
> freezing the fields that produced each PDF, and `coverage_rule` + `coverage_snapshot` computing the completeness
> meter. **So this group is read from engine, not maintained by hand**, and `A4`, `A5` and `A7`–`A11` are new
> `doc_kind`s rather than a new system.

| ID | Asset | Primarily for |
|---|---|---|
| `A1` | Datasheet | Specifier, dealer evaluating |
| `A2` | Dimensioned drawings | Specifier, installer |
| `A3` | CAD | Specifier — *publish-versus-gate decision outstanding (`registers/backlog.md` DEC-5)* |
| `A4` | BIM / Revit object | Architect |
| `A5` | NBS clause | Spec writer |
| `A6` | Install manual | Installer on site — the highest-intent reader we will ever have |
| `A7` | Commissioning / calibration guide | Installer, integrator |
| `A8` | Fault-finding guide | Installer, support |
| `A9` | "How do you do X" video | Installer — the atom of the corpus |
| `A10` | Training module | Certification — assembled from the above, never authored separately |
| `A11` | Spares and service instructions | Installer, support |

### 13 · Record keeping — `K1`–`K3`

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
| — *the line above generates from definition; below, nothing generates without group 04* — | | |
| **The knowledge base** — the corpus itself | **`N3`** `R3` | **One article per answered question.** This is the whole content estate, and it is one field |
| **Hook / campaign silo** | `O1` `R1` `R3` **`N3`** | A hook with no answer behind it sends a dealer to a dead end (`registers/backlog.md` CON-8) |
| **"How do you do X" video** | `R4` `R3` **`N3`** | One failure mode per piece. The cheapest thing we make — and it is a *person answering*, so `N3` is the script |
| **Fault-finding guide** | `R4` `D7` **`N3`** | Most support volume, answered once |
| **"How many do I need" / selection guide** | **`N1` `N2`** | The commonest live question in every brand, and there is no output for it today |
| **Design tool / calculator spec** (`motion/tools.md`) | **`N1` `N2`** `D9` | A tool is `N1` made executable. Building one without `N1` written down is how a tool contradicts the design service |
| **Comparison / objection content** | `O4` `R1` `G1` `G2` **`N4`** | The dealer is choosing between options, including doing nothing |
| **Cross-sell prompt** (`registers/backlog.md` XS-1) | `D10` `D7` `O3` **`N5` `N6`** | Physical adjacency justifies it; **`N6` says when to say it**, which is the whole trick |
| **The spec-conversation prompt list** | **`N5` `N6`** | Our only discovery channel, and it runs on timing knowledge (`NEXT.md` lane 4) |
| **Dealer-facing sales material** — what they tell their client | **`N7`** | **Nothing in the estate produces this today.** It is the moat expressed as a deliverable |
| **Training module** | `A6`–`A9` **`N1`–`N4`** | Assembled from the corpus (`decided.md` S12), never authored separately |
| **The hook matrix per door** (`registers/backlog.md` JNY-4) | **`H1` `H2`** `O1` `R1` | `H1` says which of the five appeals this product can honestly carry; **the matrix must not invent one it cannot** |
| **Comparison content, per named rival** | **`X1`–`X5`** `G1` `G2` | `X4` (where they win) is what makes the other four believable |
| **The switch approach** — a rival's dealer, a vacated territory | **`X5` `X1`** `M4` | The conversation that is not a cold pitch, because there is an incumbent |
| **The business-case argument** | **`M4` `M5` `M2`** `O2` | *A cheaper product that takes two more days on site is not cheaper* |
| **Delivery & availability answers** | **`M1`–`M3` `L1`** | The questions that decide whether we are specified on a live project |
| **Commissioning / verification material** | **`L3`** `R4` | Where a good product still becomes a bad room — and the G5 signal |
| **Spares & service proposition** | **`L4` `L5`** | Backing a dealer, expressed as something they can buy |
| **The testing / commissioning decisions** | **`N9`** | Each unanswerable is either a test to buy or a claim to stop making. Not content — a spending decision |
| **What to fix in the product** | **`X4` `X6`** `N9` | The record's one output that is not content. Where we lose, and why |

**Read that table as one fact:** everything above the divider can be produced from the record as it stands today, and
**every one of those outputs is a document.** Everything below the divider is what a *rep* does — answering, sizing,
comparing, arming the dealer, defending the choice — and none of it can be produced at all. **The estate can
currently generate paperwork and cannot generate a salesperson**, which is precisely the thing content was supposed
to replace.

**And the last row is not content.** `X4`, `X6` and `N9` — where competitors beat us, why deals are lost, what we
are asked and cannot answer — feed the product and the testing budget, not the corpus. ~~**`X6` is largely a read
from engine's pipeline rather than something to capture afresh.**~~ **Struck 2026-08-13 against engine itself
(`evidence/engine-audit.md` §1, group 05): a quote carries `won_at` and nothing else — no loss reason, no competitor, no
dimension — and there is no loss history to read regardless. `X6` must be captured, not read.** **A database built
to sell the thing also tells you what to fix about it**, and that is a reason to keep it honest rather than
flattering.

**Two hard gates, and they are not stylistic.**

- **`G3` gates publication of anything.** A product that is `pre-release` or `demonstrable, undocumented` generates
  internal material only. This one field would have caught three live errors: the Screen Wall, the C-ATS commercial
  range, and REV-CP-12.
- **`G2` gates every claim.** A writer working from a record with `G2` filled cannot cross the wording boundary
  without seeing it first. That is the entire mechanism — *scattering, never diffusion* only survives if it is
  written next to the product it applies to.

---

## The blank form

```markdown
## <Product or mechanism family> — `<ID>`

**Rep test:** attract __ · defend __ · trust __ · deliver __
**Knowledge:** __ / 9 + __ of __ questions answered · **Record:** __ / 58 · **Assets:** __ / 11 · **Status (G3):** ___

### 01 · What it actually is
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

### 02 · Why to buy it
| ID | Field | Value |
|---|---|---|
| O1 | Problem, in the dealer's words | |
| O2 | Time or labour saved | |
| O3 | Opportunity it opens | |
| O4 | What it replaces or avoids | |
| O5 | Entry or flagship | |

### 03 · The doubt it removes
| ID | Field | Value |
|---|---|---|
| R1 | The doubt it meets | |
| R2 | Load-bearing asset | |
| R3 | Questions it generates | |
| R4 | What goes wrong on site | |

### 04 · The knowledge layer
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

### 05 · Competitive
| ID | Field | Value |
|---|---|---|
| X1 | The named alternatives | |
| X2 | The dimensions it turns on | |
| X3 | Where we win | |
| X4 | Where they win | |
| X5 | The switch argument | |
| X6 | Why deals are lost *(append one line per loss)* | |

### 06 · Commercial
| ID | Field | Value |
|---|---|---|
| M1 | Order unit and minimum | |
| M2 | Lead time, and what changes it | |
| M3 | Availability posture | |
| M4 | The dealer's business case | |
| M5 | What not specifying it costs them | |

### 07 · Lifecycle & support
| ID | Field | Value |
|---|---|---|
| L1 | Order to site | |
| L2 | Install sequence, and who does it | |
| L3 | Commissioning & verification | |
| L4 | Serviceability | |
| L5 | What we support, and for how long | |

### 08 · Hook material
| Appeal | Carries? | The substance behind it |
|---|---|---|
| More revenue | | |
| Time saved | | |
| Easier to do | | |
| Better results | | |
| The problem named | | |

**H2 — the most interesting true thing:**
**H3 — what has bitten:**

### 09 · Who decides
| ID | Field | Value |
|---|---|---|
| W1 | Purchaser vs specifier | |
| W2 | Who signs off, and what convinces them | |

### 10 · What we may and may not say
| ID | Field | Value |
|---|---|---|
| G1 | Claims supported | |
| G2 | The claims we refuse to make | |
| G3 | Marketing status | |
| G4 | Proof, and publishable? | |

### 11 · Where it is sold
| ID | Field | Value |
|---|---|---|
| C1 | Channel | |
| C2 | Territory | |

### 12 · Assets
| A1 datasheet | A2 drawings | A3 CAD | A4 BIM | A5 NBS | A6 install | A7 commissioning | A8 fault-finding | A9 video | A10 training | A11 spares |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

### 13 · Record keeping
**Owner:** — · **Last reviewed:** — · **Review interval:** —
```

---

## How it gets filled — the six routes

***The system half, and it decides whether any of the above ever happens.*** **A route is a rule: *when this
happens, this gets written down.*** Fifty-eight fields is not twelve projects and not one documentation push — it
is six triggers, five of which already fire every week (`registers/record-schema.md`, part one).

| # | When this happens… | …this gets written down | How often |
|---|---|---|---|
| **RT1** | A product is made or changed | `D1`–`D10` · `L1` `L2` | Per change |
| **RT2** | A test result or report arrives | `D9` · `G1` · `G4` | Rarely |
| **RT3** | We help specify a job | `N1` `N2` `N5` · `D4` `D5` | **Daily** |
| **RT4** | We answer a question, pre-sale or on site | `R3` `R4` `N3` · `L3` `L4` | **Daily** |
| **RT5** | We quote, and when we win or lose | `X1`–`X6` · `M1`–`M5` · `O1` | Per quote — **already runs in engine's CRM** |
| **RT6** | A position is settled or reviewed | `H1`–`H3` · `G2` `G3` · `K1`–`K3` | The one new habit |

**Three consequences worth stating plainly.**

1. **A running route fills its fields forever; a field filled by a push starts decaying the day it is written.**
   Stand the routes up before filling more fields — otherwise this becomes another documentation project, and the
   reason those fail is that they ask one person to hold everything.
2. **RT5 already runs — engine's CRM is classic pipeline management**, so win/loss is captured today. ~~The live
   question is whether the recorded loss reason carries **which competitor, on which dimension**~~ — **answered
   2026-08-13 (`evidence/engine-audit.md` §3, REC-2): neither. Only the fact of a loss has a home** (`project_statuses.lost`,
   an unused `rejected` quote status); there is no loss-reason, competitor or dimension field anywhere in engine.
   **RT5 fills `M1`–`M5` and `O1` from live quoting, but `X1`–`X6` needs capture built.**
3. **The two daily triggers already produce this and throw it away.** Every spec conversation fills the
   application fields; every support answer fills the knowledge fields. Both happen anyway, both get written into
   an email and lost. The archive is the proof (`registers/backlog.md` CON-3) — **the knowledge exists, it has just never
   had anywhere to land.**

## How this gets used

1. **The roster is `registers/product-register.md`.** Every product in the group, its record status and its meters. Start
   there; it is what says which record to open next.
2. **Records live with the brand** — `brands/<brand>/product-records.md`. The form is group; the fill is brand
   (`CLAUDE.md`, group ≠ brand).
3. **Rank by `R3`, not alphabetically.** The questions-generated field, cross-checked against what the sent-mail
   archive says actually recurs (`registers/backlog.md` CON-3), is the order to work in.
4. **Fill a field group across a range before filling one product deeply**, unless a specific output is waiting on
   it. The gates above say which unlocks most.
5. **`N3` is filled by recording, not by writing.** Take the ranked `R3` list into a session, ask the questions, and
   transcribe. **Ten minutes of an owner talking fills more of group 04 than a week of drafting**, and it is the only
   version that carries the authority — the substance stays human, the multiplication does not
   (`motion/motion-design.md` component 2). Filling `N3` by composition would be inventing claims, which the line
   forbids.
6. **Completeness gates new products** (`decided.md` S16). A product without `D1`–`D10` and `G3` does not get a
   store listing. That is the only version of this that stops the debt returning.

*Every field is a claim that some output needs it — a field no output needs should be struck, and a missing field
that an output needs should be added.*
