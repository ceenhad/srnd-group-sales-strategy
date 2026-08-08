# The work items beneath each task

*Why this document exists, in one sentence: **a task is too big to automate.** `T-S09` — follow up through the
project's lead time — is one row in the register and six separate pieces of work, four of which a machine does and
two of which it cannot. **The work item is the unit automation is actually built at.***

`10-tasks.md` lists 46 tasks and gives each an automation verdict. That verdict is a summary — a task reads
`assisted` because *some* of the work beneath it needs a person, not because all of it does. This document opens
each task up.

**Same standing caution as the task register.** These are decompositions proposed from the tasks and the strategy
documents. They have not been checked against anyone doing the work. **Strike what is wrong.**

**And the harder half: this list can only contain work items somebody thought of.** A decomposition confirms what
is in it; it says nothing about steps nobody wrote down. So `108 of 168` is a real ratio of *this list* and not a
measure of the work. Read the counts as a shape, never as a coverage figure — **the items missing from here are
invisible from here.**

> **Resolved by block after the QA (2026-08-08).** The QA graded all 46 tasks (`group/10-tasks-qa-sheet.md`).
> Three read `standard · a system · a system` — **already handled** — so every work item beneath them needs
> nothing built: **`T-S08`, `T-S12`, `T-M16`** (marked in place below). No task was struck, so nothing else
> resolves out of this register by block; the remaining correction (strike what's wrong, add what's missing) is
> still the row-by-row pass `TSK-4`, done with whoever does the work.

---

## What a work item is

**The smallest step that is wholly machine or wholly human.** If a step contains both, it is two work items. That
is the whole test, and it is what makes the layer useful: the moment you split them, you can see which half is
buildable.

## The thirteen primitives

Every work item below is one of thirteen verbs. **Eight are machine-side, five are human-side.** The set is small
because the same operations recur across quite different tasks — which turns out to be the point.

| Primitive | Side | What it is | Work items | Tasks that need it |
|---|---|---|---|---|
| **`detect`** | machine | Notice that something has happened or changed — a quote issued, a registration, a dealer gone quiet, a rival's page altered | 20 | 20 |
| **`retrieve`** | machine | Pull the right fields for this product, dealer or project. **Almost always from the product record** | 29 | 28 |
| **`assemble`** | machine | Build the thing from those fields — a draft, a page, a pack, a list, a comparison | 29 | 29 |
| **`send`** | machine | Deliver it to a named person | 7 | 7 |
| **`record`** | machine | Write the outcome back so the next pass starts from it | 30 | 30 |
| **`route`** | machine | Put it in the right place, or in front of the right person, at the right moment | 11 | 11 |
| **`rank`** | machine | Order a list by a stated rule — what recurs, what blocks, what earns | 3 | 3 |
| **`schedule`** | machine | Fire at a time, or at an interval | 4 | 4 |
| **`judge`** | human | Is this real, is this right, does it apply here | 12 | 12 |
| **`relate`** | human | The human contact itself — asking, thanking, negotiating, recovering | 9 | 9 |
| **`decide`** | human | A call only an owner makes | 7 | 7 |
| **`answer`** | human | Substance only the person who knows it can supply | 3 | 3 |
| **`word`** | human | The phrasing, where the wording carries the weight | 3 | 3 |

**168 work items across the 46 tasks. 133 are machine-side and 34 are human-side.**

## What the counts say

**1. Four primitives carry most of the work.** `record` (30 tasks), `assemble` (29),
`retrieve` (28) and `detect` (20) account for
108 of the 168 work items. **Build those four well and you have
addressed most of the machine side of nearly every task.** That is a different build plan from automating tasks one
at a time, and a much shorter one.

**2. `retrieve` retrieves from the product record.** 28 of 46 tasks need it, and in almost every case
what they need is a field: the on-ramp fields to present the range, `L1`–`L3` and `R4` to make an install succeed,
`X1`–`X5` to defend against a rival, `N7` to arm a dealer for their own client. **This is the same conclusion the
domain map reached, now with a count against it: the record is what the automation reads from.**

**3. The human side is 34 items and it is specific.** `judge` — is this real, is this right. `relate` — the
contact itself. `decide` — an owner's call. `answer` — substance only the person holds. `word` — the phrasing.
Nothing on that list is administrative, which is the test of whether the split has been drawn in the right place.

**4. A `manual` task is not automation-proof.** `T-S13`, asking for the order, is irreducibly human in the asking —
but *noticing* that a dealer has gone quiet is a `detect`, and it is buildable. Same with `T-S20` recovering a
failure, and `T-S28` recognition. **The verdict describes the task; the work items describe what you can build.**

---

## The build order this implies

Not task by task. **Primitive by primitive**, because each one unlocks work in dozens of tasks at once:

| Order | Build | Unlocks |
|---|---|---|
| 1 | **`detect`** — a way to notice state changes and fire on them | 20 tasks. Most of the signals sit in engine already; the question is what can be subscribed to |
| 2 | **`retrieve`** — the record, queryable by product, dealer and project | 28 tasks. **Blocked on the record being filled**, which is why that comes first |
| 3 | **`assemble`** — generation from fields, against the generation gates | 29 tasks |
| 4 | **`record`** — somewhere every outcome lands | 30 tasks. The capture routes, from the other side |

`route`, `send`, `schedule` and `rank` are smaller and mostly follow from the four above.

---

## The decomposition, task by task

*Verdict shown is the task's, from `10-tasks.md`. Primitives are marked `machine` or `human` by the table above.*


### `T-S01` — Build the target list

**Task verdict: `automatable`** · 5 work items

| Primitive | Work item |
|---|---|
| `retrieve` | Pull the accounts already known — who buys, what, how recently |
| `retrieve` | Establish which brands each one already buys and which they do not |
| `rank` | Order by cross-sell headroom, or by whatever rule the owner sets |
| `judge` | Is this dealer worth approaching, and on which brand |
| `[?]` | Where a list of dealers we do *not* already know comes from — a question for engine, not an assumption |

### `T-S02` — Reach a dealer who has never heard of us

**Task verdict: `automated`** · 4 work items

| Primitive | Work item |
|---|---|
| `assemble` | Publish the answer against the problem, in the dealer's words |
| `route` | Place it where strangers look — search, AI answers, social, press |
| `detect` | A visit arriving from a hook |
| `record` | Which hook caught which dealer — source tagging |

### `T-S03` — Qualify the dealer

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | What engine already holds on them |
| `assemble` | A short profile — what they buy, what they build, who they are |
| `judge` | Are they real, and are they the kind of dealer this suits |

### `T-S04` — Qualify the project

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `detect` | A tool use or enquiry that indicates a live project |
| `retrieve` | What the tool captured about the room and the requirement |
| `judge` | Is the project real, is it live, is it worth the time |

### `T-S05` — Present the range

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | The on-ramp fields for the products in play — D1, O1–O4, H2 |
| `assemble` | The material for this dealer and this room |
| `relate` | The conversation itself, and reading the room |

### `T-S06` — Discover — their business, their fears, last job's failure

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `relate` | The spec conversation itself |
| `record` | The project, what they were unsure about, what they were afraid of |
| `route` | Into the record — O1, N1, N5, R3, W2 |
| `rank` | What recurs across conversations, so the content queue orders itself |

### `T-S07` — Technical selling — help specify a live job

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | The product records for everything in the room |
| `assemble` | A specification from N1, N2 and the definition fields |
| `answer` | The part the record does not hold |
| `record` | That new answer back into N3, and what it taught into N8 |

### `T-S08` — Produce a quote

**Task verdict: `automated`** · 4 work items · **QA: `standard · a system · a system` — already handled; skip these work items.**

| Primitive | Work item |
|---|---|
| `retrieve` | Products, quantities, partner pricing |
| `assemble` | The quote |
| `send` | To the dealer |
| `record` | Into the pipeline |

### `T-S09` — Follow up through the project's lead time

**Task verdict: `automatable`** · 7 work items

| Primitive | Work item |
|---|---|
| `detect` | Quote issued, no order, time elapsed |
| `schedule` | The next touch, at an interval matched to how long the project runs |
| `retrieve` | Something relevant to *this* project rather than a generic nudge |
| `assemble` | The touch |
| `send` | To the dealer |
| `record` | Sent, opened, replied |
| `judge` | When to stop, and when to hand it to a person |

### `T-S10` — Handle objections

**Task verdict: `automatable`** · 5 work items

| Primitive | Work item |
|---|---|
| `detect` | Which objection this is, against R1 and R3 |
| `retrieve` | The answer from N3 and the claim that supports it from G1 |
| `assemble` | The response |
| `send` | Or publish, if it recurs |
| `record` | Whether it settled the point |

### `T-S11` — Defend against a named competitor

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | X1–X5 for the product, and the loss history from engine's pipeline |
| `assemble` | The comparison, dimension by dimension |
| `judge` | What is fair to say to this dealer about this rival |
| `record` | The outcome — X6 reads from the pipeline |

### `T-S12` — Negotiate terms

**Task verdict: `manual`** · 3 work items · **QA: `standard · a system · a system` — already handled; skip these work items.**

| Primitive | Work item |
|---|---|
| `relate` | The negotiation |
| `decide` | What may be conceded |
| `record` | What was agreed |

### `T-S13` — Close — want the order and ask for it

**Task verdict: `manual`** · 3 work items

| Primitive | Work item |
|---|---|
| `detect` | A dealer who has gone quiet, or a quote sitting past its window |
| `relate` | Asking for the order |
| `record` | The answer, either way |

### `T-S14` — Onboard the account

**Task verdict: `automated`** · 4 work items

| Primitive | Work item |
|---|---|
| `detect` | A registration |
| `assemble` | The welcome and what registration grants |
| `send` | To the new partner |
| `record` | Account state |

### `T-S15` — Make the first install succeed

**Task verdict: `assisted`** · 6 work items

| Primitive | Work item |
|---|---|
| `detect` | An order placed, and for what |
| `retrieve` | L1–L3, R4 and N3 for those products |
| `assemble` | The install pack — what arrives, what must be ready, what goes wrong |
| `send` | Ahead of delivery, not with it |
| `answer` | The live question from site |
| `record` | What went wrong, into R4 and N8 |

### `T-S16` — Post-delivery follow-up

**Task verdict: `automatable`** · 6 work items

| Primitive | Work item |
|---|---|
| `detect` | Delivery, or completion |
| `schedule` | The touch, far enough after to be useful |
| `assemble` | The check-in |
| `send` | To the dealer |
| `record` | The response |
| `route` | Escalate a problem to a person |

### `T-S17` — Account management — stay recalled

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `detect` | Gone quiet, or a change in what they buy |
| `retrieve` | What they buy and what they have never bought |
| `assemble` | A reason to make contact that is not a nag |
| `relate` | The contact |

### `T-S18` — Cross-sell the rest of the group

**Task verdict: `automatable`** · 5 work items

| Primitive | Work item |
|---|---|
| `detect` | A spec conversation or an order in progress |
| `retrieve` | The adjacency — D10, N5, N6 for what they are already buying |
| `assemble` | The prompt, with the physical reason it belongs |
| `route` | To whoever is in the conversation, at the moment it is relevant |
| `record` | Whether a second brand followed — the G6 signal |

### `T-S19` — Prompt the reorder

**Task verdict: `automatable`** · 4 work items

| Primitive | Work item |
|---|---|
| `detect` | The reorder interval, or a consumption pattern |
| `assemble` | The prompt |
| `send` | To the dealer |
| `record` | Whether it converted |

### `T-S20` — Recover a failure

**Task verdict: `manual`** · 3 work items

| Primitive | Work item |
|---|---|
| `detect` | An escalation |
| `relate` | The recovery |
| `record` | What actually failed, into N8 and X6 |

### `T-S21` — Train the dealer's staff

**Task verdict: `automatable`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | A6–A9 and N1–N4 for the range |
| `assemble` | The module from material that already exists |
| `route` | To registered partners |
| `record` | Completion, and certification |

### `T-S22` — Pipeline and forecast

**Task verdict: `automated`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | Open quotes, stages, values |
| `assemble` | The view |
| `record` | Movement |

### `T-S23` — Bring back market intelligence

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | Win/loss from engine's pipeline |
| `assemble` | The picture — which rival, which dimension, which stage |
| `judge` | What it means, and whether it is a pattern or a one-off |
| `record` | Into X1–X5 |

### `T-S24` — Feed product development

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | X4, X6 and N9 aggregated across the range |
| `assemble` | The list, ordered by how often each thing costs us |
| `decide` | What to change, and what to commission |

### `T-S25` — Events and keeping relationships warm

**Task verdict: `manual`** · 2 work items

| Primitive | Work item |
|---|---|
| `relate` | The event itself |
| `record` | Who was met, and what was said |

### `T-S26` — Territory planning

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | Where dealers are, where orders come from, where they do not |
| `assemble` | The coverage picture |
| `decide` | Where to push, and where to leave alone |

### `T-S27` — The novel problem

**Task verdict: `manual`** · 2 work items

| Primitive | Work item |
|---|---|
| `answer` | The impossible project |
| `record` | What it taught, into N8 and N9 |

### `T-S28` — Recognition and thanks

**Task verdict: `manual`** · 2 work items

| Primitive | Work item |
|---|---|
| `detect` | A milestone worth marking |
| `relate` | The thanks itself |

### `T-M01` — Market and segment research

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | What we sell, where, and to whom |
| `assemble` | The segment picture |
| `judge` | What it means for where to aim |

### `T-M02` — Competitor tracking

**Task verdict: `automatable`** · 4 work items

| Primitive | Work item |
|---|---|
| `detect` | A change on a rival's public surfaces — range, claims, pricing posture |
| `retrieve` | What changed against what we held before |
| `record` | Into X1–X4 |
| `judge` | Whether the change matters |

### `T-M03` — Positioning and messaging

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `retrieve` | The record's D and O fields, and the brand's own truth |
| `word` | The positioning itself |
| `decide` | What the brand will and will not say — G2 |

### `T-M04` — Campaign planning

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | H1 — which appeals each product can honestly carry |
| `assemble` | The hook matrix per door: appeal by placement |
| `word` | The hooks themselves |
| `schedule` | The run |

### `T-M05` — Content production

**Task verdict: `assisted`** · 5 work items

| Primitive | Work item |
|---|---|
| `retrieve` | The substance — the record, the measured data, the archive |
| `assemble` | The derivative set from each atom |
| `judge` | The truth-check: is it true today, may it be published |
| `route` | To the canonical home, then the placements |
| `record` | What went out, tagged to its source |

### `T-M06` — Editorial calendar and cadence

**Task verdict: `automatable`** · 4 work items

| Primitive | Work item |
|---|---|
| `rank` | The queue, by what recurs and what is blocking |
| `schedule` | What goes out when |
| `detect` | What actually published |
| `record` | The log |

### `T-M07` — Channel management

**Task verdict: `assisted`** · 3 work items

| Primitive | Work item |
|---|---|
| `route` | The right piece to the right channel |
| `record` | What is live where |
| `judge` | What suits a channel and what does not |

### `T-M08` — Discoverability — search and AI answers

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | O1 and N3 — the dealer's words, and our answers to them |
| `assemble` | Published answers in the form an engine can cite |
| `detect` | What is being found, and for what |
| `judge` | Where we are absent and should not be |

### `T-M09` — Lead capture and nurture

**Task verdict: `automated`** · 3 work items

| Primitive | Work item |
|---|---|
| `detect` | A tool used, a download taken, a form completed |
| `record` | Into engine |
| `route` | To the nurture sequence, or to a person |

### `T-M10` — Collateral — datasheets, case studies

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | The fields each output needs — the generation gates |
| `assemble` | The draft |
| `judge` | Approval, against G1 and G2 |
| `record` | Version and review date |

### `T-M11` — Brand consistency

**Task verdict: `automated`** · 2 work items

| Primitive | Work item |
|---|---|
| `retrieve` | G2 for the product, and the brand's hard don'ts |
| `assemble` | Applied at drafting time, not policed afterwards |

### `T-M12` — Dealer marketing support

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | N7 — what the dealer tells their own client |
| `assemble` | Material the partner can hand over, in their name not ours |
| `route` | To registered partners |
| `record` | What gets used |

### `T-M13` — Events and exhibitions

**Task verdict: `manual`** · 2 work items

| Primitive | Work item |
|---|---|
| `relate` | The stand, and the conversations on it |
| `decide` | Which shows, and what to show |

### `T-M14` — Trade press and PR

**Task verdict: `assisted`** · 4 work items

| Primitive | Work item |
|---|---|
| `retrieve` | H2 — the most interesting true thing — and G4, what may be shown |
| `assemble` | The piece |
| `word` | The pitch to the title |
| `route` | To the outlet |

### `T-M15` — Measurement and reporting

**Task verdict: `automatable`** · 3 work items

| Primitive | Work item |
|---|---|
| `detect` | The gateway signals — G1 to G6 |
| `assemble` | The view: what moved, what did not |
| `record` | Against the period |

### `T-M16` — CRM and data hygiene

**Task verdict: `automated`** · 2 work items · **QA: `standard · a system · a system` — already handled; skip these work items.**

| Primitive | Work item |
|---|---|
| `record` | Account, contact and project state |
| `detect` | Duplicates, staleness, missing fields |

### `T-M17` — Product launch

**Task verdict: `assisted`** · 6 work items

| Primitive | Work item |
|---|---|
| `detect` | G3 changing from pre-release to current |
| `retrieve` | The full record, and the asset audit |
| `assemble` | The launch set — page, datasheet, hooks, announcement |
| `decide` | That it is ready to be said |
| `route` | To every placement at once |
| `record` | What went out |

### `T-M18` — Budget and spend allocation

**Task verdict: `manual`** · 1 work items

| Primitive | Work item |
|---|---|
| `decide` | Where the money goes |

---

## What to do with this

1. **Correct it first.** A work item that does not exist generates a build that serves nobody. The people who do
   these tasks will strike rows and add ones I have missed.
2. **Then build primitives, not tasks.** `detect` and `record` are shared plumbing. Building them for one task and
   again for the next is how this gets expensive.
3. **`retrieve` waits on the record.** 28 tasks need to read fields that are largely unfilled. Filling the record
   is not a documentation chore sitting alongside the automation — it is the automation's input.
4. **Check engine before building any of it.** Most of `detect`, `record` and `route` may already exist there in
   some form. That check comes before design, not after.
