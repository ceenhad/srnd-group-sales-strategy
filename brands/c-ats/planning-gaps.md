# C-ATS — the planning gaps

Written 2026-08-20 on Neil's instruction: *"the risk is that we are going too deep into building. Are there planning
gaps in C-ATS that we need to look at?"*

Not a backlog, not a content plan, and not another thing to build. Every gap below closes with a decision, a number
or one fetch — none of them closes with a document.

## The structural finding: the brand run produces a work queue, never a plan

Four legs — pathways, hooks, segments, training — and not one of them asks for a number, a price, a date or whose
time it takes. `../_template/the-brand-run.md` says so itself: "the run ends as a work queue rather than as a
document." A work queue with no target cannot be prioritised, so the natural next move after a run is always to
write the next piece. That is the drift Neil spotted: four drafts in a day, and no plan they answer to.

Proposed, not adopted: the run needs a plan check. One page, before Leg 1 or after Leg 4 — the number we are trying
to move, from what baseline, by when, at what price, whose hours. Offered as `MTH-3`; the template is not edited
from here.

## The gaps

### `P1` — a measured baseline with no target against it

The baseline is good (`../../evidence/2026-08-18-cats-segment-cut.md`): 53 external accounts have ever bought C-ATS
out of 549 in the group ledger, 9.7%. Of those 53, **18 active** (2025–26, £276,726), 7 recent, 16 lapsed
(£140,108). External product revenue 2015→2026: £495,106.

The objective is a direction with no quantity — `claims.md` `C2.15`, Neil's own words and the only confirmed
statement of the job: "we need to engage with more AV integrators."

**What `P1` needs, settled 2026-08-19/20.** The measure comes before the number. Engine already models
`customers.customer_type_id` (`dealer` · `distributor` · `end_user` · `specifier`) and `products.brand_id`, so the
structure is a **group** target on dealer sales and a **brand** target on distribution sales, never netted together,
counted at `ordered_at` rather than at the invoice. 333 of 350 live customers are untyped, and until that field is
filled the two cannot be separated at all (`ENG-20`).

Two constraints on how it is set. There is **one motion, not three** — Neil: "treating all of them as new is the
most efficient approach", so the recency segments are measurement and not a segmentation of the pitch. And the
**historical ledger is not the instrument**: invoices are outstanding for work already sold, so what matters is
`leads` by source through to conversion, going forward.

### `P2` — isolation is a sold layer with one clause of plan behind it

Confirmed C-ATS's (`Q79`): it has always been sold, fits no other brand, and belongs with C-ATS because it is the
acoustic consultant's work. Commercially it is a Sound Isolation store category of ten items — compound, proprietary
clip, five bracket variants, a mount, a penetration back box — plus a six-step service ladder: discovery, design,
drawings, details, BOM, build guide.

In the plan it appears once: `growth-levers.md` says "Isolation and Verification travel well" to pro install. No
record, no claim rows, no pathway, no price position, no content.

And the planning point is larger than the missing record. Per `claims.md` `C1.40`, the isolation layer is the
earliest of the three — it sets the room's structural dimensions and travels with the architectural design. So the
layer we have never planned is the one that reaches a project first.

Closes with a decision on whether isolation is a line to sell or a way in. `KNW-10` fills the record either way.

### `P3` — the most profitable line has no commercial shape

`Q45` has been open since 2026-08-17: no price, and no structure — per room, banded by project size, or staged by
deliverable. Three things now point at the answer and none has been used:

- the platform calls design services "the margin engine — and the only line that can earn now";
- the isolation ladder next door is already staged by deliverable, and Neil built it;
- the store carries an `Acoustic Treatment Design Service - Basic` line at 5 rows / £17,000, alongside the £2,400
  median across 41 invoiced engagements.

Closes with one decision. `Q45`'s framing is the thing to drop: pricing a design off how long it now takes is the
wrong axis when the customer is buying hours they will not spend (`C1.44`).

### `P4` — capacity is the binding constraint and nothing states it

Every runnable item traces to an owner's hours. `Q25` says Neil and Simon cover all three roles; `Q39` asks whether
Ben is still involved and has never been answered. Four drafts wait on one person's truth-check, and the training
rows' "needs to run" column is largely an owner's calendar.

Closes with a statement of who does what and roughly how much time exists. Without it every plan here is costed at
zero, which is why the queue keeps growing.

### `P5` — a channel is gated behind a product with no date

`growth-levers.md` lever 2 points at commercial cinema and says plainly that the product opens the channel. The
commercial range is in development and must not be written up as shipping. So a named growth channel depends on
something with no owner, no date and no gate recorded here. Closes with a date, or an explicit "not this year".

### `P6` — lever 2 has no validation step, so it is a permanent maybe

`growth-levers.md` says each new channel needs its own validation before spend. Nothing schedules that validation
for pro install, commercial cinema or fit-out. A lever that cannot be started is not a lever. Closes by picking one
channel and defining what would count as validation — or by saying lever 2 is not this year's work.

### `P7` — withdrawn

Verification is an offer, not an unsold capability. It is listed as a service on the C-ATS store alongside Isolation
System and Isolation Verification, and `copy.md` carried all three all along; this file was written without reading
it. What survives sits with `P2`: verification is listed and not priced, and isolation is listed with no plan behind
it.

## Not a gap, so it does not get re-audited

- **Buyer truth.** `W1`/`W2` and `C2.17`–`C2.23`: who specifies, who signs off, why they buy. Answered.
- **The quantity question.** `N1`/`N2` — how many panels — is systemised in the platform. Publication is the open
  part, and it is `DR-Q52`'s.
- **The retention motion.** `sequences.md` A/B/C covers welcome, install and adjacency.
- **The content queue.** `content-plan.md` has five tranches ordered by cost. It does not need more items; it needs
  a target to be ordered against, which is `P1`.
