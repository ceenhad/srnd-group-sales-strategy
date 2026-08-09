# Task shapes — a template and a definition of done for the `varies` tasks

*From the QA (`group/10-tasks-qa-sheet.md`), the "write the shape" move. Pass 1 found **19 tasks that vary by
whoever does them** — a habit, not a process — and pass 1's sweep B reduced the cause to two missing artefacts
per task: **`no template`** (nothing to copy from) and **`no standard`** (nobody decided what good looks like).
This file writes both. It needs no engine and builds nothing — it surfaces the shape pass 1 said is "already
there and merely unwritten."*

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
already says (`group/11-work-items.md`, `08-sales-motion.md`, `09-motion-design.md`); silence is `[?]`, not
filled. *Definition of done is often a decision* — `[decide]`, once. *Read the shape, not the cell* — the 19 are
the aggregate; several share a shape and will be grouped.

**The 19 `varies` tasks:** `T-S03`, `T-S04`, `T-S05`, `T-S07`, `T-S09`, `T-S13`, `T-S23`, `T-S24`, `T-S25`,
`T-S27`, `T-S28`, `T-M02`, `T-M03`, `T-M06`, `T-M07`, `T-M09`, `T-M10`, `T-M14`, `T-M15`.

> **Status — 2026-08-09: format + first tranche (3 of 19), rebuilt for depth.** The remaining 16 follow once the
> depth is confirmed. Owners are not assigned here — that is the roles decision (`PAR-3`).

---

## `T-M02` — Competitor tracking

**For:** a standing, comparative picture of each competitor that accretes over time, so any rep can defend or
position without rebuilding it from memory.

**Output:** a **comparison matrix** — rows are the fixed dimensions a dealer actually weighs (measured
performance, integration/control, support model, lead time, price posture, …); columns are **us + each named
competitor**. Every populated cell carries the claim **and its source** — a measured figure, an `X1`–`X5`
field, a pipeline win/loss. Plus a dated change-log line whenever a competitor's public surface moves.

**Rules the output must satisfy:**
- **Comparative, never absolute.** Every entry is *us vs a named competitor on a named dimension* —
  "on lead time, us 6–8 wks vs them 12+." A bare "they're weaker" is not a permitted entry; the form has no cell
  for it.
- **Sourced.** No cell without its evidence. An unsourced claim is a marked gap, not an assertion.
- **Accretes.** The prior state is retained, so change is visible rather than overwritten.

**Steps — each time a competitor is looked at:** detect the change on their surfaces → enter it against the
fixed dimensions, sourced, into `X1`–`X4` → judge one-off vs pattern → date it.

**Definition of done:** the matrix is current as of the look; every populated cell is comparative and sourced;
prior state retained. **`[decide]`** the fixed dimension list per product category (so every competitor is
compared on the *same* axes — this is what makes the analysis comparable across deals) and which competitors are
tracked. *(Where the record lands: the engine audit — `REC-13` / `REC-0`.)*

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

**Definition of done:** a complete qualification record with a verdict traceable to the criteria. **`[decide]`**
the bar itself — the criteria and thresholds that turn the fields into a verdict (this is the `no standard`;
once set, the scoring is a rule a machine can run).

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
with gaps flagged not hidden. **`[decide]`** the minimum set a "presentation" must always include, per room
type. *(Depends on the on-ramp fields being filled — `DOC-13`, `KNW-*`.)*

---

## Still to write — the other 16

`T-S04` qualify the project · `T-S07` technical selling · `T-S09` follow up through lead time · `T-S13` close ·
`T-S23` bring back market intelligence · `T-S24` feed product development · `T-S25` events and keeping
relationships warm · `T-S27` the novel problem · `T-S28` recognition and thanks · `T-M03` positioning and
messaging · `T-M06` editorial calendar and cadence · `T-M07` channel management · `T-M09` lead capture and
nurture · `T-M10` collateral · `T-M14` trade press and PR · `T-M15` measurement and reporting.

*Shared shapes to group: the two "qualify" tasks (`T-S03`/`T-S04`); the intelligence tasks
(`T-S23`/`T-M02`) — both comparison-matrix-shaped; the cadence tasks (`T-M06`/`T-M07`); the
draft-from-the-record tasks (`T-M03`/`T-M10`/`T-M14`).*
