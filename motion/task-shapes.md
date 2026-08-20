# Task shapes — a template and a definition of done for the `varies` tasks

*From the QA (`evidence/2026-08-08-tasks-qa-run.md`), the "write the shape" move. Pass 1 found **19 tasks that vary by
whoever does them** — a habit, not a process — and pass 1's sweep B reduced the cause to two missing artefacts
per task: **`no template`** (nothing to copy from) and **`no standard`** (nobody decided what good looks like).
This file writes both. It needs no engine and builds nothing — it surfaces the shape pass 1 said is "already
there and merely unwritten."*

> **The `Direction (2026-08-14)` markers below are first-pass directions, not qualified decisions** — Neil ran
> all 16 `[decide]` calls in one sitting (`standards.md`) and was explicit that the
> substantial ones each need their own session. Treat a direction as the working answer until its session
> refines it; treat nothing below as closed.
>
> **Six of those sessions have since been worked** — `T-S03`, `T-S04`, `T-S05`, `T-M02`, `T-M03`, `T-M06`. Each
> shape below carries a **▶ Session** pointer into `standards.md` § "The worked sessions,"
> where the proposal and the questions only Neil can answer both sit. **The sessions propose; they do not
> settle** — nothing has entered `registers/questions.md` § Answered.

## What a shape is — and the depth test

**A list of steps is not a shape; steps written down are still a habit.** A shape has depth only when it
specifies the **output** tightly enough that the same result comes out regardless of who produces it — and,
where the work-items mark a step machine-side, tightly enough to build. The depth lives in the output's
structure, not in the instructions. So each shape names five things:

- **For** — what it is for, in one line.
- **Output** — the artefact produced and its required structure: the fields, the matrix, the ranked list. **This
 is the heart.** It is where a property like *comparative* is enforced by the form of the thing, not left to
 the person.
- **Rules the output must satisfy** — the non-negotiable properties (*comparative*, *sourced*, *ranked*,
 *complete*…). A shallow template omits these; they are what hold the output consistent and what an automated
 check would test.
- **Steps — each time** — how the output gets produced (the work-items, in service of the output).
- **Definition of done** — a checkable standard: the output exists and satisfies the rules. **`[decide]`** marks
 a standard nobody has set yet (pass 1's `no standard`) — the owner's one-time call, not a guess.

> **The test to apply to every shape:** *could someone produce the correct output from this alone, without the
> tacit knowledge — and could the machine-side steps be built from it?* If not, it lacks depth (Neil,
> 2026-08-09).

**Three disciplines still hold.** *Surface, don't invent* — the output and steps are drawn from what the repo
already says (`motion/work-items.md`, `sales-motion.md`, `motion-design.md`); silence is `[?]`, not
filled. *Definition of done is often a decision* — `[decide]`, once. *Read the shape, not the cell* — the 19 are
the aggregate; several share a shape and will be grouped.

**And don't gold-plate the tracking.** Where a shape needs to show currency, that is a **last-updated date** —
not a version history or a change-log (Neil, 2026-08-09).

**The 19 `varies` tasks:** `T-S03`, `T-S04`, `T-S05`, `T-S07`, `T-S09`, `T-S13`, `T-S23`, `T-S24`, `T-S25`,
`T-S27`, `T-S28`, `T-M02`, `T-M03`, `T-M06`, `T-M07`, `T-M09`, `T-M10`, `T-M14`, `T-M15`.

> **Status — 2026-08-09: all 19 written, at depth, grouped by shared shape.** The `[decide]` calls are collected
> at the end — the one-time decisions that turn a template into a standard. Owners are not assigned here — that
> is the roles decision (`PAR-3`).

---

## `T-M02` — Competitor tracking

**For:** a standing, comparative picture of each competitor that accretes over time, so any rep can defend or
position without rebuilding it from memory.

**Output:** a **comparison matrix** — rows are the fixed dimensions a dealer actually weighs (measured
performance, integration/control, support model, lead time, price posture, …); columns are **us + each named
competitor**. Every populated cell carries the claim **and its source** — a measured figure, an `X1`–`X5`
field, a pipeline win/loss. Each record carries a **last-updated date** — that is the whole of the tracking.

**Rules the output must satisfy:**
- **Comparative, never absolute.** Every entry is *us vs a named competitor on a named dimension* —
 "on lead time, us 6–8 wks vs them 12+." A bare "they're weaker" is not a permitted entry; the form has no cell
 for it.
- **Sourced.** No cell without its evidence. An unsourced claim is a marked gap, not an assertion.
- **Current and dated.** Each record carries a last-updated date — no version history or change-log to maintain.

**Steps — each time a competitor is looked at:** detect the change on their surfaces → enter it against the
fixed dimensions, sourced, into `X1`–`X4` → judge one-off vs pattern → stamp the last-updated date.

**Definition of done:** the matrix is current as of the look; every populated cell is comparative and sourced;
last-updated date stamped. **Direction (2026-08-14):** the fixed dimensions are performance and features ·
integration/control · support model · lead time · price posture · reference/credibility — amended from the
proposed default because measured performance is a hard metric to claim. **Open:** which competitors are
tracked — the current roster is wrong and the real one is pending from Neil; cadence (quarterly + on any surface
change) stands once it is named. *(Where the record lands: the engine audit — `REC-13` / `REC-0`.)*
**▶ Session 5** (`standards.md`): the roster is the only thing still gating this shape, and it
**cannot be derived** — no loss reason exists in any system, so it is name-them or nothing. What the repo holds
is tabulated by front and the gap named per brand: **DT is covered and `brands/display-technologies/competition-matrix.md`
is already this shape half-built** — the model to copy; **C-ATS has a price band (GIK, RPG, Artnovion) but no
roster**, which `product-records.md` `N4` already flags as *"a commercial position, not a comparison"*;
**Fabric Walls appears only through Cinema Build Systems; Pro-Fi has nothing.** The ask is five questions.

---

## `T-S03` — Qualify the dealer

**For:** a repeatable pursue / hold / decline decision, and on which brand, that does not depend on who takes the
enquiry.

**Output:** a **qualification record** per dealer, fixed fields: buy-history (brands, recency, value band —
pulled from engine), build profile (room types, tier), fit signals, and the **verdict** — pursue / hold /
decline — with brand and the reason that follows from the fields.

**Rules the output must satisfy:**
- **Scored against a fixed bar, not a gut call.** The same inputs yield the same verdict whoever runs it — which
 is exactly what makes it automatable once the bar exists.
- **Sourced from engine, not memory.** Buy-history fields are pulled, never recalled.

**Steps — each time:** retrieve engine history → populate the fixed fields → apply the bar → record verdict +
brand + reason.

**Definition of done:** a complete qualification record with a verdict traceable to the criteria.
**Direction (2026-08-14) — reframed:** the bar is ability to pay, not size or build-type — "much of our best
projects have come from smaller dealers that get max value from our combined product and service offer."
Pursue any dealer with the means to pay; small is fine; the disqualifier is inability to pay, not scale.
**▶ Session 1, answered 2026-08-15** (`standards.md`): **the verdict field splits in two — an
admit test and a priority band for attention**, recomputed from engine signals, with first-order value and any
size-derived band as **prohibited inputs** (measured twice). The admit test is **objective and already
running**: VAT registration and company identity verified against supplied IDs, plus ability to pay enforced at
checkout — **and credit is available via Iwoca Pay, from a third party rather than from us**, so there is no
bad-debt exposure to underwrite. Two named exclusions on top: **a competitor buying to copy**, and a
**discretionary refusal** — *"if we simply decide not to"* — which is **logged as discretion, never written as
a rule.** The priority band is the automatable half.

---

## `T-S05` — Present the range

**For:** every dealer sees the same substance for their room, generated from the record rather than recalled, so
the presentation does not vary by rep.

**Output:** a **tailored range pack** — for the room's product set, the on-ramp fields (`D1`, `O1`–`O4`, `H2`)
assembled per brand in a fixed order, covering the minimum set every presentation must include.

**Rules the output must satisfy:**
- **Complete against the room.** Every brand relevant to the room is represented; a brand with missing fields is
 a **flagged gap**, never a silent omission.
- **Generated from the record.** Assembled from fields, not composed ad hoc, so it is identical whoever builds
 it.

**Steps — each time:** identify the room's product set → pull the on-ramp fields per brand → assemble in the
fixed order → flag any brand whose fields are missing.

**Definition of done:** a pack covering the minimum set for every relevant brand, generated from the record,
with gaps flagged not hidden. **Direction (2026-08-14) — reframed, build item:** not a minimum-set rule; the
standard to build is how the proposal should be presented to maximise the upsell — a proposal design/template
task, working with `motion/adjacency-map.md`. Not yet built. *(Depends on the on-ramp fields being filled —
`DOC-13`, `KNW-*`.)*
**▶ Session 3** (`standards.md`): designed — **the unit is the room, not the enquiry**;
sections are the room's layers in build order; **every layer carries one of four statuses** (specified ·
offered · not applicable · not ours) so the form has no blank cell; the justification is **physical, never
commercial**, quoted from `adjacency-map.md`; the increment is priced **inside the same document**. Its
acceptance test is Q5's **own-made attach rate on carried sales**, baselined at **£472,320 Komodo against
£38,452 Screen Wall**. Note the timing distinction the session draws: finding 4's 246-day lag governs
*dealer-level* cross-sell, **not** the room in front of you.
**Answered 2026-08-15:** an unrequested layer is shown as a **priced increment** — so *offered* carries a
number, in the same document. **Which couples this shape to the record's fill state:** pricing an increment for
a layer whose record is empty is a number we cannot stand behind, so `registers/product-register.md`'s gaps now bear
directly on the proposal.

---

## `T-S04` — Qualify the project *(shares the qualification shape with `T-S03`)*

**For:** deciding whether a live project is real, live and worth the time — consistently, not on instinct.

**Output:** a **project qualification record** — fixed fields: the room and requirement (from the tool use or
enquiry that flagged it), stage, value band, the dealer it sits with, and a **verdict** (pursue / watch / pass)
with the reason that follows from the fields.

**Rules the output must satisfy:**
- **Scored against a fixed bar** — as `T-S03`: same inputs, same verdict.
- **Linked, never floating** — it ties to the qualified dealer (`T-S03`) and the room's product set.

**Steps — each time:** detect the signal of a live project → pull what it captured about room and requirement →
apply the bar → record verdict + reason.

**Definition of done:** a project record with a verdict traceable to the criteria, linked to its dealer.
**Direction (2026-08-14) — reframed:** every project is worth the time — "always." The bar to define is not this
one but the boundary between pre-sales (free) and consulting (paid): "consulting needs to be paid." That
boundary is a new open decision, not yet set. (Answers backlog `XS-4` in principle: spec help beyond pre-sales
is chargeable.)
**▶ Session 2, answered 2026-08-15** (`standards.md`): the test is **free pre-sales is work
that becomes content; consulting is work that cannot** — standard 7's reusable-versus-one-off cut, doing double
duty as the price line — with three tie-breakers (bespoke · accountable · sustained). **Charged · fixed fee ·
not credited against the order · published to dealers.** `XS-4` is closed and the answer is the problem: today
it varies and is not deliberate. **What remains is the paid-services list**, assembled in that session —
**one priced service in the whole group, four real and unpriced** (`XS-5`), and of five unclassified rungs
**three now settled free** (training · Experience Centre hosting · standard drawings) **with two left**
(`XS-6`). Also
flagged here: the one place payment risk is genuinely ours is the **staged-payment project**, which belongs to
this shape rather than to `T-S03`.

---

## `T-S23` — Bring back market intelligence *(shares the comparison-matrix shape with `T-M02`)*

**For:** turning what the pipeline and the field reveal into the same standing picture `T-M02` holds — so
intelligence is pooled, not carried in one head. *(Duplication row; record side `REC-9`.)*

**Output:** entries into the **same comparison matrix** as `T-M02` — which rival, which dimension, at which stage
we won or lost — sourced from the pipeline (`X1`–`X5`), plus a market-level note where it is a pattern and not a
single deal.

**Rules the output must satisfy:**
- **Comparative and sourced** — as `T-M02`; each datum enters against a named dimension with its source.
- **Pattern vs one-off is marked** — a single loss is a data point; a repeated one is a finding, and the shape
 distinguishes them.

**Steps — each time:** retrieve win/loss from the pipeline → enter against the matrix dimensions, sourced →
judge pattern vs one-off → stamp last-updated.

**Definition of done:** the matrix reflects the latest pipeline evidence, comparative and sourced, patterns
flagged. **Direction (2026-08-14) — struck:** no threshold rule; unmeasurable — "people don't reply with the
actual list they did buy when you lose a bid." Replacement standard: record a competitor only when one is
actually named in the deal; the picture accretes slowly; no pretence of systematic loss attribution (consistent
with the `X6` finding that no loss reason exists in any system). *(Record home: `REC-9` / `REC-0`.)*

---

## `T-S07`, `T-S24`, `T-S27` — the learning-capture shape

*Their output is two things: the answer or action now, **and** what it taught, captured back into the record so
the next person starts from it. The capture is the half that currently evaporates — so in this shape it is not
optional.*

**`T-S07` — Technical selling (help specify a live job)**
- **Output:** a specification for the room, assembled from the product records (`N1`, `N2`, the definition
 fields), **plus** the new answer captured back — into `N3` (the answer) and `N8` (what it taught).
- **Rules:** *from the record where it exists* (don't re-derive what's held); *the novel answer is captured, not
 just given* — an answer that leaves only in an email is the gap.
- **Steps:** retrieve the room's product records → assemble the spec → answer the part the record doesn't hold →
 record that answer into `N3`/`N8`.
- **Done:** the dealer has the spec, and any answer the record didn't hold is now in it. **Settled
 (2026-08-14):** capture into `N3` any answer that isn't already in the record and could recur (a general
 technical point) — not one-off project arithmetic.

**`T-S24` — Feed product development**
- **Output:** a **ranked list of product gaps and requests**, aggregated across the range from `X4`, `X6`,
 `N9`, ordered by how often each one costs us.
- **Rules:** *ranked by cost/frequency, not recency or loudest voice*; *sourced* — each item cites the deals or
 answers it aggregates.
- **Steps:** retrieve `X4`/`X6`/`N9` across the range → assemble → order by frequency/cost → hand to the
 `decide`.
- **Done:** a current ranked list, each item sourced. **`[decide]`** what to change or commission — the owner's
 call; the shape prepares it, it does not make it.

**`T-S27` — The novel problem**
- **Output:** the answer to the one-off, **plus** what it taught, captured into `N8` (what it taught) and `N9`
 (what we still can't answer).
- **Rules:** *the capture is mandatory* — the whole value of a novel problem is what it teaches; an uncaptured
 one is paid for and lost.
- **Steps:** answer the problem → record the lesson into `N8`/`N9`.
- **Done:** answer given, lesson recorded. No `[decide]` — the shape is simply "always capture."

---

## `T-M03`, `T-M10`, `T-M14` — the draft-from-the-record shape

*Each produces a written artefact from record fields, against the brand gates, truth-checked before it ships.
Same shape, different output and gate.*

**Shared Output:** a draft **generated from named record fields**, carrying its **source tags** and a
**review/approval stamp**.
**Shared Rules:** *generated from fields, not composed from scratch* (consistent, and regenerable when a field
changes); *gated before publication* — nothing ships without the truth-check against `G1`/`G2`/`G4` and the
brand's hard don'ts; *sourced* — every claim traces to a field or a measurement.

- **`T-M03` — Positioning and messaging** · Output: the brand/product positioning, from the `D` and `O` fields
 plus the brand's own truth. Added rule: obeys `G2` — what the brand will and will not say. **Settled
 (2026-08-14) — confirmed in principle, build item:** inherit each brand's `CLAUDE.md` hard don'ts plus the
 group rule (no superlative without a measurement) — but the actual per-brand `G2` lists don't exist yet;
 "none of this is done." Done: positioning stated, `G2`-obedient, sourced.
 **▶ Session 6** (`standards.md`): **built — six lists** (group floor, C-ATS, DT, Fabric
 Walls, Pro-Fi, Light Walls, Distribution), surfaced from rules the repo already holds rather than authored.
 Two by-products: **no `brands/*/CLAUDE.md` exists in this repo**, so the standard points at a file that isn't
 there; and applied to what is published today the lists catch **five live breaches** already logged in
 `registers/open-items.md`. Needs only Neil's "nothing missing" confirmation.
- **`T-M10` — Collateral** · Output: datasheet / case study from the generation-gate fields, versioned with a
 review date. Done: draft approved against `G1`/`G2`, versioned. **Direction (2026-08-14):** re-review on change
 (a product or data change triggers it), with an annual backstop.
- **`T-M14` — Trade press and PR** · Output: the piece + the pitch to the outlet, from `H2` (the most
 interesting true thing) and `G4` (what may be shown). Added rule: **nothing NDA'd or unpublishable passes
 `G4`**. Done: piece and pitch ready, `G4`-cleared.

---

## `T-M06`, `T-M07` — the cadence shape

*Both run on a rhythm (their trigger is a clock — pass 2): order a queue by a rule, place items, log what went
where. The shape is a schedule plus a log.*

**Shared Output:** a **scheduled queue** (what goes out, when, where) and a **log** of what actually published
where, last-updated dated.
**Shared Rules:** *ordered by a stated rule, not by whim*; *logged* — the record of what is live where is what
stops duplication and orphaning.

- **`T-M06` — Editorial calendar and cadence** · Output: the ranked queue + schedule + published log. Rule:
 ranked by *what recurs and what is blocking* (the archive-derived demand, `CON-3`). Done: a current queue and
 a log of what published. **Direction (2026-08-14) — reset:** the actual demand is daily per brand — "if you
 take all the content needed it's daily per brand" — servable only by the record + AI production line; the
 owner's batch model is unchanged (owner minutes stay at the answer step), daily-per-brand is the production
 system's target, not an owner promise.
 **▶ Session 4** (`standards.md`): sized — four viable brands at a weekday piece each is
 **20 a week, ~1,000 a year, against 109 videos in eight years**, so it is a different machine rather than a
 faster cadence. Decomposed as **answers per period × derivatives per answer**, which makes it reachable at
 roughly **two owner recording sessions a month** (both figures marked hypothesis). Two rules the line needs:
 **every piece makes an argument** (the catalogue's 1–26 views is what a line without that rule produces at
 speed), and **the answer carries the face, the derivative carries the pointer.**
 **Answered 2026-08-15 — scope is the four viable brands, and the floor's unit was rejected, rightly.** Neil:
 *"I'm pretty efficient at the making part — it's the planning that makes videos difficult. With a plan and
 script you can bash out loads in a day."* **The owner's output is not the constraint; the planning upstream of
 him is.** So **the floor belongs to the production line and its unit is scripted briefs delivered**, while the
 owner's commitment is a booked slot rather than a quantity. This is `content.md`'s *"never faces a blank
 page"* rule confirmed by the owner rather than argued at him — **and it re-points the whole build: the hard
 part is producing briefs good enough to record from, which is step 3 again.**
- **`T-M07` — Channel management** · Output: a map of what is live on which channel + the routing rule. Rule:
 *right piece to the right channel* against a stated fit (brand channel vs group; the estate rules in
 `04`/`05`). Done: current live-where map, routing rule applied. **Direction (2026-08-14):** publish to brand
 channels, not the group one; short argument-making pieces to video, method/data to the knowledge base; the
 group channel stays group-level only.

---

## `T-S09`, `T-S13`, `T-S25`, `T-S28` — the contact-and-record shape

*Human contact whose outcome must be recorded or it evaporates. `T-S09` can run as a scheduled sequence
(`automatable` — it is build item `TSK-3`); the other three are human in the contact, machine-recordable in the
outcome.*

- **`T-S09` — Follow up through the project's lead time** · Output: a **scheduled sequence of touches** across
 the quote-to-order window, each relevant to *this* project, with sent/opened/replied logged and a
 hand-to-a-person rule. Rules: *fires on elapsed time, not memory*; *relevant, not a generic nudge*; *logged*.
 Done: touches firing on schedule, logged, escalating when the rule says. **Direction (2026-08-14):** a 30-day
 default via the one-tap status email (`operations/engine-as-hub.md` §1 Q4), and the receiver adjusts their own
 next-contact interval; two ignored pokes escalate to a human call; stop at order or explicit no. *(This is
 `TSK-3`.)*
- **`T-S13` — Close** · Output: the ask made, and **the answer recorded either way** against the opportunity.
 Rule: *a "no" and its reason is recorded, not just a "yes"*. Done: outcome recorded. The detect-side (gone
 quiet / past window) is buildable; the ask is human.
- **`T-S25` — Events and keeping relationships warm** · Output: **who was met and what was said**, recorded
 against the account. Rule: *the contact is captured* — an event whose conversations aren't recorded is a cost
 with no asset. Done: contacts logged against accounts. **Direction (2026-08-14):** per contact — who, which
 account, what they were unsure about, what they were afraid of, the next step.
- **`T-S28` — Recognition and thanks** · Output: the thanks given, triggered by a **milestone the record can
 detect** (first order, Nth, anniversary, £ threshold). Rule: *triggered by a signal, not a calendar* (`S28`).
 Done: milestones surfaced and acted on. **Direction (2026-08-14):** first order · a big-£ threshold (the
 £500k-dealer class) · an Nth-order or anniversary mark · a standout project. *(Record side: `REC-11`.)*

---

## `T-M09` — Lead capture and nurture

**For:** a captured lead never sits in an inbox — it enters the record and routes onward. *(Largely `automated`
already.)*

**Output:** a **lead record** in engine — source, what they did (tool use, download, form), and the route taken
(nurture sequence, or a person).
**Rules:** *captured on the event, not later*; *source-tagged* — which hook caught them (`JNY-1` attribution);
*routed, never parked*.
**Steps:** detect the capture event → record into engine → route to nurture or to a person.
**Definition of done:** every lead in the record, source-tagged, with a route assigned. **Settled
(2026-08-14):** an explicit ask, a qualified high-value lead, or a live project routes to a person; everything
else to the nurture sequence.

---

## `T-M15` — Measurement and reporting

**For:** the same view of what moved each period, from the gateway signals, so trends are readable rather than
re-derived.

**Output:** a **period report** from the gateway signals `G1`–`G6`: what moved, what didn't, against the prior
period.
**Rules:** *the same signals every period* — so periods are comparable, the measurement form of "comparative";
*sourced to the gateways*, not hand-assembled; *dated to the period*.
**Steps:** detect the `G1`–`G6` signals → assemble the what-moved view → record against the period.
**Definition of done:** a report on the fixed signals, comparable to prior periods. **Direction (2026-08-14) —
amended:** live anytime and emailed on a Monday morning — the KPI dashboard (`operations/engine-as-hub.md` §1)
live in engine at any time, plus a Monday-morning email digest; headline content is the six-question KPI set
(Q1–Q6), not `G1`–`G6`/`FACT-1`. The digest is another engine-owned-mail use case.

---

## The standards to set — the `[decide]` calls, collected

*Pass 1's `no standard` in one place: the small, one-time decisions that turn these templates into standards.
Each is minutes, and each makes a task consistent whoever does it. The owner's to set — not guessed here.*

> **First pass run 2026-08-14 — directions set, not settled.** All 16 taken; outcomes are inline above and in
> full in `motion/standards.md` (9 accepted/amended, 3 reframed, 1 struck, 2 left as build
> items, 1 still pending a roster from Neil — and per Neil's caveat, the substantial ones each still need their
> own session). The bullets below are the original asks, kept for reference.

- **Qualify (`T-S03` / `T-S04`):** the bar — what makes a *dealer*, and a *project*, worth pursuing.
- **Present the range (`T-S05`):** the minimum set every presentation must include, per room type.
- **Competitor / intelligence (`T-M02` / `T-S23`):** the fixed dimension list per category (the axes every
 comparison uses); which competitors are tracked and how often; the threshold at which a run of losses is a
 "pattern."
- **Technical selling (`T-S07`):** what counts as "worth capturing" into `N3`, vs a one-off.
- **Positioning (`T-M03`):** `G2` — what each brand will and will not say.
- **Collateral (`T-M10`):** the re-review cadence.
- **Cadence (`T-M06` / `T-M07`):** the floor rate (sustainable minimum publish rate); the channel-fit rules.
- **Follow-up (`T-S09`):** the touch interval, and the stop / hand-to-a-person rule.
- **Events (`T-S25`):** the minimum a post-event note must capture.
- **Recognition (`T-S28`):** which milestones warrant a thank-you.
- **Lead routing (`T-M09`):** what goes to nurture vs to a person.
- **Measurement (`T-M15`):** the reporting period, and which of `G1`–`G6` are the headline measures.

*Not a standard but a standing decision: `T-S24` — what to change or commission — is the owner's recurring call
the ranked list feeds, not a one-time bar.*
