# C-ATS — the planning gaps

*Written 2026-08-19 on Neil's instruction: **"the risk is that we are going too deep into building. Are there
planning gaps in C-ATS that we need to look at?"*** **He is right, and the audit below found a reason it happened
rather than just a list.**

**What this file is not:** *a backlog (that is `../../registers/backlog.md`), a content plan (`content-plan.md`), or
another thing to build. **Every gap below closes with a decision, a number or one fetch — none of them closes with a
document.***

---

## The structural finding: the brand run produces a work queue, never a plan

**Four legs — pathways, hooks, segments, training — and *not one of them asks for a number, a price, a date or
whose time it takes.*** *`../_template/the-brand-run.md` says so itself: **"the run ends as a work queue rather than
as a document."*** **A work queue with no target cannot be prioritised, so the natural next move after a run is
always to write the next piece.** *Which is exactly the drift Neil spotted: **four drafts in a day, and no plan
they answer to.***

**Proposed, not adopted: the run needs a plan check.** *One page, before Leg 1 or after Leg 4: **the number we are
trying to move · from what baseline · by when · at what price · whose hours.** `../_template/the-brand-run.md` is not
edited here — this is offered as `MTH-3` and belongs to whoever owns the method.*

---

## The gaps, in the order that they block things

### `P1` — There is a measured baseline and no target against it

**The baseline exists and is good** *(`../../evidence/2026-08-18-cats-segment-cut.md`)*: **53 external accounts have
ever bought C-ATS out of 549 in the group ledger — 9.7%.** *Of those 53: **18 active** (ordered 2025–26, £276,726),
**7 recent** (2024), **16 lapsed** (2020–23, £140,108). Total external product revenue 2015→2026: **£495,106**.*

**The objective is a direction with no quantity.** *`claims.md` `C2.15`, Neil's own words and the only confirmed
statement of the job: **"we need to engage with more AV integrators."*No number and no horizon.** * **That framing was withdrawn
the same day — see below. One motion, everybody treated as new.***

> **What `P1` needs, settled 2026-08-19/20.** *The **measure comes before the number**: engine already models
> `customers.customer_type_id` (`dealer` · `distributor` · `end_user` · `specifier`) and `products.brand_id`, so the
> structure is **a group target on dealer sales and a brand target on distribution sales, never netted together**,
> counted at `ordered_at` rather than at the invoice. **333 of 350 live customers are untyped, and until that is
> filled the two cannot be separated** (`ENG-20`).* **And there is one motion, not three** — *Neil: "treating all of
> them as new is the most efficient approach", so the recency segments are measurement, not a segmentation of the
> pitch.* **The historical ledger is not the instrument**: *invoices are outstanding for work already sold, and what
> matters is `leads` by source through to conversion.*

### `P2` — Isolation is a sold C-ATS layer with no plan at all

**Confirmed C-ATS's** *(Neil, `Q79`: it has always been sold, it fits no other brand, and it belongs with C-ATS
because it is the acoustic consultant's work)*. **What exists commercially:** *a **Sound Isolation** store category
of ten items — compound, proprietary clip, five bracket variants, a mount, a penetration back box — plus a
**six-step service ladder** (discovery, design, drawings, details, BOM, build guide).*

**What exists in the plan: one clause.** *`growth-levers.md` says *"Isolation and Verification travel well"* to pro
install. **That is the only place it appears** — no record, no claims, no pathway, no price position, no content.*

**And the planning point is bigger than the missing record.** *Per `claims.md` `C1.40`, **the isolation layer is the
earliest of the three** — it sets the room's structural dimensions and travels with the architectural design. **So
the layer we have never planned is the one that reaches a project first**, ahead of the treatment we plan
constantly.*

> **Closes with:** *a decision on whether isolation is **a line to sell** or **a way in** — those imply different
> work. `KNW-10` fills the record either way.*

### `P3` — The most profitable line has no commercial shape

**`Q45` has been open since 2026-08-17.** *No price, and no structure — per room, banded by project size, or staged
by deliverable.* **Three things now point at the answer and none of them has been used:**

- *The platform calls design services ***"the margin engine — and the only line that can earn now"***.*
- *The isolation ladder next door **is already staged by deliverable**, and Neil built it.*
- *The store carries an **`Acoustic Treatment Design Service - Basic`** line with **5 rows at £17,000** — so there is
 a real average to price from, alongside the £2,400 median across 41 invoiced engagements.*

> **Closes with:** *one decision. **`Q45`'s framing is the thing to drop** — pricing a design off how long it now
> takes is the wrong axis when the customer is buying hours they will not spend (`C1.44`).*

### `P4` — Capacity is the binding constraint and nothing states it

**Every runnable item traces to an owner's hours.** *`Q25` says Neil and Simon cover all three roles; `Q39` asks
whether Ben is still involved and **has never been answered**.* **Four drafts now wait on one person's truth-check,
and the training rows' *"needs to run"* column is largely an owner's calendar.**

> **Closes with:** *a statement of who does what, and roughly how much time exists. **Without it every plan here is
> costed at zero**, which is why the queue keeps growing.*

### `P5` — A channel is gated behind a product with no date

**`growth-levers.md` lever 2 points at commercial cinema and says plainly that *the product opens the channel*.**
*The commercial/large-format range is in development and **must not be written up as shipping** (brand
`CLAUDE.md`).* **So a named growth channel depends on something with no owner, no date and no gate recorded here.**

> **Closes with:** *a date or an explicit *"not this year"*. **Either is a plan; silence is not.***

### `P6` — Lever 2 has no validation step, so it is a permanent maybe

*`growth-levers.md`: each new channel *"needs its own validation before spend"*. **Nothing schedules that
validation** for pro install, commercial cinema or fit-out.* **A lever that cannot be started is not a lever.**

> **Closes with:** *pick **one** channel and define what would count as validation — or say lever 2 is not this
> year's work. **Both are decisions; holding three unvalidated channels open is not.***

### — not a gap

**Verification is an offer, not an unsold capability.** *Listed as a service on the C-ATS store alongside Isolation
System and Isolation Verification, and `copy.md` carried all three all along — this file was written without reading
it.* **What survives sits with `P2`: verification is listed and not priced, and isolation is listed with no plan
behind it.**

## What is *not* a gap, so it does not get re-audited

- **Buyer truth.** *`W1`/`W2`, `C2.17`–`C2.23`: who specifies, who signs off, why they buy. Answered.*
- **The quantity question.** *`N1`/`N2` — how many panels — is systemised in the platform. **Publication is the open
 part, and it is `DR-Q52`'s, not ours.***
- **The retention motion.** *`sequences.md` A/B/C covers welcome, install and adjacency.*
- **The content queue.** *`content-plan.md` has five tranches ordered by cost. **It does not need more items; it
 needs a target to be ordered against**, which is `P1`.*
