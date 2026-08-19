# The brand run — the shape every brand inherits

*What a brand run produces, in the order it produces it. **Derived from the C-ATS run** (`../c-ats/`, 2026-08-18),
which was done first precisely so the shape would be set by a real one rather than designed in the abstract
(`../../NEXT.md` item 2; `../../group-strategy/strategy.md`, "Then the brands"). **This file is shape, not
substance** — it says what to produce and what each piece must contain, never what a brand should say.*

**The run is four legs.** Three are named in the strategy — *pathways built stage by stage from the brand's
material · hooks written from its products · segments cut from the database* — and the fourth was added on
2026-08-19: **training opportunities, identified per brand.** *Everything else the brand needs is already
group-level and is not re-derived.*

> **Note the departure.** `../../group-strategy/strategy.md` names **three** legs. Leg 4 is Neil's instruction of
> 2026-08-19 — *"training and education is one of the most beneficial marketing types… a critical deliverable on
> all"* — and **the strategy document has not yet been updated to match** (`../../registers/backlog.md` `DOC-30`).
> *Recorded here rather than left implicit: a correction applied in one place and not the other is this repo's
> most repeated defect.*

## The precondition

**Check the platform first, then the record.** The brand folder is not the whole material — `cinema-platform`
holds engines, design rules and ADRs that move faster than this repo, and on the C-ATS run the single most
important answer in the brand (*how many panels do I need*) turned out to live there, fully systemised, while the
brand's own record said it was written down nowhere. **A brand run that reads only `brands/<brand>/` will find
gaps that are not gaps** — and `../../CLAUDE.md` already requires the platform check in as many words.

**Brand truth has to be confirmed before anything is built on it, and confirmation means a name and a date.**
C-ATS's `positioning.md` — what the brand is, who it is for, the promise, why it is credible — ran for months
with **no attribution to an owner anywhere in it**, and three pathways, a hook set and a content plan were built
on top. Drill each section into rows first (`../../method.md` § The drill-down) and record the answers in
`claims.md`. **An unconfirmed brand document is not a weaker source than a confirmed one; it is a different kind
of thing, and the run cannot tell them apart unless the rows say so.**

**The product record has to be filled first.** All three legs read from it — the hooks trace to its fields, the
pathway slots cite its assets, the segments join to its products. A brand run against an empty record produces
invention, which is the one thing the production line is not for (`../../motion/motion-design.md`, component 2).
`../../registers/record-form.md` is the form; `../c-ats/product-records.md` is the worked example.

**A record with `[?]` in it is fine and is not a blocker.** The pathways carry a gap forward as a flag rather
than filling it. **A named gap is progress; a composed answer is not.**

**But check the gap is real before honouring it.** C-ATS carried "who specifies, who signs off, why they really
choose" as *deliberately parked pending real recent jobs* across two files and eleven record fields. **Half of it
was answered in one sentence the first time anyone asked an owner** (Q55), and the rest is a question, not a
research project. Neil, 2026-08-18, on the parking language: *"what trash and bullshit — just needs cleaned out."*
**A `[?]` that nobody has tried to answer is not a parked decision, it is an unasked question**, and dressing it
as the former makes it permanent.

## Leg 1 — one pathway per door

**One file per entry door: `pathway-<problem>.md`.** A door is a product and the problem it answers, never a
brand or a campaign (`../../group-strategy/buyer-journey.md`).

Each pathway carries, in this order:

1. **The door.** The problem *in the dealer's words* — and if that phrasing has not come from real questions, it
   is marked `[?]` and flagged, not drafted into place.
2. **Eight slots, always the same eight**, as a table of *piece · its one job · state today · the handoff*:

   | Slot | Gateway | What sits here |
   |---|---|---|
   | 1 | **G1** | The hook set for this door (a set, not a piece) |
   | 2 | **G1→G2** | The fuller answer on the canonical home |
   | 3 | **G2** | The proposition — range and possibility |
   | 4 | **G2→G3** | The proof |
   | 5 | **G3** | Registration — **the hinge** |
   | 6 | **G4** | The listing and the first order |
   | 7 | **G5** | The install layer |
   | 8 | **G6** | The adjacency, and which brand's stage 2 it exits onto |

3. **The hook matrix** for this door — appeal × angle × the record field behind it. Terse; provenance lives in
   `hooks.md`.
4. **What writing it down shows** — including the register items the pathway consumes, in order.
5. **Guardrails**, from the brand's own `CLAUDE.md`.

**Three things the C-ATS run established about slot behaviour**, worth knowing before writing three of them:

- **Slot 5 is shared. A brand has one G3 piece, not one per door.** Registration does not vary by product, and
  three pathways each specifying their own registration piece is three copies of one thing.
- **A door's centre of gravity is not always slot 1.** One C-ATS door's most valuable piece is an install
  one-pager at slot 7. A door can be worth opening for what happens after the order.
- **Slot 8 can have more than one exit**, depending on what is being built. Take the exits from
  `../../motion/adjacency-map.md` rather than deciding them per pathway.

## Leg 2 — `hooks.md`, the brand's hook set

The group designs the hook layer (S23, `../../motion/motion-design.md`); the brand fills it. The file holds the
whole candidate set across every door, and it carries four things the per-pathway matrices do not:

- **Provenance per candidate** — the record field or published figure behind it. A candidate with no source is
  not a candidate.
- **The three tests, applied and visible.** The **stranger test** (would someone who hasn't bought stop for
  this?), **evidenced and positive** (a search hook claims people type those words), and **the professional bar**
  (does it teach a good integrator something they would respect us for?). On the C-ATS run the third test
  rejected the most, and what it rejected was true, useful, and filler.
- **The rejections, with reasons.** This is the half that is usually lost. A rejected angle that is not written
  down comes back next quarter.
- **Blocked hooks, named as blocked.** An angle that passes every test and is not yet *true* is recorded, not
  quietly dropped — **build it, then say it** (`../../CLAUDE.md`). It becomes castable the day the thing exists.

**States:** `live` · `candidate` (passes, uncast) · `blocked` (passes, something must be true first) · rejected
(in the rejection table, never in the candidate table).

Placement follows the settled channel roster (Q49) and is not re-decided per brand. **Search placement stays
provisional until the archive count confirms the wording** (CON-3); until then a "problem named" angle is cast on
social, where wording costs nothing to change.

## Leg 3 — `segments.md`, plus the measured cut

**Two files, deliberately.** `../../evidence/<date>-<brand>-segment-cut.md` holds the numbers and does not argue;
`segments.md` says what each segment is and **where it enters the journey**. Per `../../method.md`, a conclusion
and the data behind it live in different places.

The cut is produced by a script into `../../data/derived/`, so it is reproducible rather than remembered. Method:

- **Filter the consolidated ledger to the brand's category**, across every entity that ever invoiced it — not to
  the brand company's own accounts, which usually hold only part of the history.
- **Normalise account identity before counting anything.** `contact_canonical` is not sufficient: on the C-ATS
  run, 35 clusters covering 74 names were one dealer written two or three ways, and the same dealer landed in
  opposite segments. State the residual over-count rather than implying the number is exact.
- **Segment on recency against the ledger's own last year**, crossed with **what the account buys elsewhere in
  the group.** The second axis is what produces the *group-active, never bought this brand* segment.
- **Map each segment to a journey stage, not to a mailing list.** The rule that decides most of it: an existing
  dealer crossing to a second brand **re-enters at stage 2, not stage 1** — they have already seen the group, so
  they do not need the hook.
- **Do not rank the segments, and do not order work by what an account has spent** (Neil, 2026-08-18,
  `../../registers/questions.md` Q51): *"we are treating every relationship as day 1 startup."* A segment says
  what a dealer has already been shown — a fact about their state, not a measure of their worth. **A segment cut
  that turns into a league table has been misused.**
- **Read the CRM against the ledger and report the disagreement** rather than picking one. Both were wrong in
  different directions on the C-ATS run.

Segments are internal. They inform which pathway a dealer is offered; they are never described back to a dealer,
and no piece of content refers to one.

## Leg 4 — `training.md`, the brand's training opportunities

**Added 2026-08-19 on Neil's instruction:** ***"Training and education is one of the most beneficial marketing
types. We should add that as a critical deliverable on all — identifying training opportunities."*** *So every brand
run produces a training file, and it is a leg rather than a line inside another one.*

**Why it is a leg.** `../../group-strategy/the-group-play.md` already says **the route in is the specifier**, and
`../../group-strategy/buyer-journey.md` already names **RIBA-approved CPD** as the standard route to architects in
the UK. **In this channel teaching is not adjacent to the route to market — it is the route**, which the competitor
work established from the other side: the people who filled the void SRND left now hold the standard, the
certification and the distributor training academies (`../../group-strategy/competitors.md` § the education layer,
`EDU-1`).

**One row per opportunity. Each row states:**

| Field | What it holds |
|---|---|
| **Audience** | **Which actor** — architect · interior designer · AV consultant · integrator. *From the confirmed cast (`../c-ats/claims.md` `C2.27`); **the end user is not an audience for this** (`C2.29`, B2C runs only through the defined Cinema Store channels)* |
| **Route** | Where it would run: a CEDIA/CTA committee or session · RIBA-approved CPD · a distributor's academy · our own class · a show programme · recorded and published |
| **Subject** | **Traced to a record field or a confirmed claim, never invented** — the same provenance rule the hook set runs under (Leg 2). *A subject with no trace is not a training opportunity, it is a topic* |
| **What it needs to run** | The honest precondition — a written module, a room, an accreditation, an owner's time, a piece of measured data |
| **Publication limit** | **What may not be shown.** *Where the subject touches a black-boxed method, the row cites the decision that gates it — for C-ATS, `../../operations/decision-request-q52-cats-rules-publication.md`* |
| **State** | Runnable today · needs the module written · needs a decision · blocked, with the blocker named |

**Four rules the first run's evidence produces.**

1. **Teach from measured data, because the tier that competes on rooms does not publish any.** The acoustics scan
   found **no coefficients, standard or report** on the design-led competitors' pages — a proprietary scorecard, or
   nothing (`../../evidence/2026-08-19-acoustics-competitor-scan.md`). **Where a brand holds published third-party
   measurement, teaching from it is available to us and not to them.**
2. **A training subject and a proof asset fail in the same way.** Leg 1's finding 2 — a proof asset can be net
   negative until its teaching piece exists — **is a training opportunity stated backwards.** Read the pathway's
   proof slots first: *the pieces that make a weak-looking asset legible are usually the best training subjects.*
3. **Do not teach what the brand does not do.** `../../CLAUDE.md`'s build-it-then-say-it applies to a syllabus as
   much as to a claim — **with one exception this leg exists because of**: where the *capability* is long-held and
   only the *activity* lapsed, the rule does not bite. **That is `EDU-1`'s whole point, and it is the one place in
   this repo where the reverse failure applies.**
4. **Name the competitor's session, not the competitor.** Training programmes are public, so who teaches what is
   observable — and `../../CLAUDE.md` permits criticising the category in public while naming a rival only behind
   the partner gate, measured. **An internal training row may name anyone; a published syllabus names nobody.**

**Training is not content, and the distinction matters for who owns it.** A piece of content is produced by the
line (`../../motion/motion-design.md`); **a class is delivered by a person, and `Q25` recorded that Neil and Simon
cover every role.** *So a training row's *"what it needs to run"* field is usually an owner's calendar, which makes
this the leg most likely to produce an honest **no** — and a named no is worth more than an unscheduled yes.*

## Four findings from the first run that are about the method, not about C-ATS

1. **A door's material may not be in the brand folder.** Two C-ATS doors assembled from brand material; the third
   read as unassemblable until the platform was checked, and then turned out to be the best-documented of the
   three. **The failure mode is finding a gap that is really a boundary** — the answer exists, in another
   product, with no route from it to the dealer. Lay all the doors out the same way, then check every apparent
   gap against the platform before calling it one.
2. **A proof asset can be net negative until its teaching piece exists.** Published, free, third-party measured
   data argued *against* one C-ATS product, because the figures read as weak to anyone who does not know what the
   product does. Check every proof slot for this before counting it as an asset.
3. **How well a problem is understood says nothing about how well it is served.** The C-ATS door with the most
   complete measured evidence behind it has the emptiest pathway. Do not infer readiness from depth of knowledge,
   in either direction.
4. **The fixed shape is what makes emptiness visible.** Nothing in the run was discovered by thinking harder about
   the brand; it was discovered by three doors having the same eight rows, so a blank cell had nowhere to hide.

## What a completed run looks like

- `pathway-<door>.md` per entry door, every slot stated with its honest state and its handoff.
- `hooks.md` — candidates with provenance, rejections with reasons, blocked hooks named.
- `../../evidence/<date>-<brand>-segment-cut.md` and `segments.md`, with the script that reproduces the cut.
- `training.md` — one row per training opportunity, each with its audience, route, traced subject, precondition,
  publication limit and state.
- The register items each pathway consumes, listed in order, so the run ends as a work queue rather than as a
  document.

**And what it does not include:** copy, a campaign, a launch date, or any claim that was not already true in the
record.
