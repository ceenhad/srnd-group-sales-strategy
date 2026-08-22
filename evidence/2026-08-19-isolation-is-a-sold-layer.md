# Isolation is a sold layer, and this repo had no record of it — 2026-08-19

*Written after `Q79`, which asked which of two contradicting documents was right. **The answer was that the group
layer was right.** *This file then records what the layer actually consists of, because **no document in this repo
said** — the register carried it as an empty row.*

> **⚠ Read the framing correctly.** *None of this is news to the business. Neil, 2026-08-19: ***"since I did them
> all it's no surprise I assure you."*** **The gap was documentary, not commercial.** *An earlier draft of this file
> and of `../NEXT.md` wrote it up as a discovery — *"the largest find of the day"* — which is the failure
> `../method.md` already names as **the oldest one in the repo: forgetting how long SRND has been doing this**. It is
> recorded here rather than quietly rewritten, because it is the second instance in two days.*

**Neil, 2026-08-19 (`../registers/questions.md` `Q79`):** ***"We have always sold isolation but it didn't fit into
any other brand. It's part of the work of the acoustic consultant so the correct place for it to live contextually is
under C-ATS. I am pretty sure that the draft Shopify website has it."***

---

## 1. It is sold, and the invoices say so

**Ten distinct isolation items appear as invoiced store lines** (`../data/derived/srnd-store-item-categories.csv`):

| Item | Net |
|---|---|
| MP5A — rubber elastomer compound mixed with barite | 4,234 |
| Akustik + Sylomer® channel clip 15 | 3,685 |
| CS6 · CS44 · M12 · H12 · S6 custom isolation brackets | 1,000 · 1,000 · 750 · 750 · 500 |
| S-110 custom isolation mount | 500 |
| EP 500 + Sylomer s35 | 664 |
| Penetration isolation back box, 270 × 400 mm | 378 |
| Total | £13,461 across 10 lines |

**So the question was never whether we sell it — only what the sold thing is, which nothing here recorded.** *A
compound, a proprietary clip, five bracket variants, a mount and a penetration back box is **a small hardware system
for decoupling a structure**, and the bracket variants are the tell that it was engineered against real conditions
rather than bought in once. **That is the sentence `CAT-05` should have carried and didn't.***

## 2. The part no document here carried: a six-step service ladder, priced well above the treatment design

**Six separately invoiced isolation *services*, all under the store's services category:**

| Service | Net |
|---|---|
| Sound Isolation **Project Drawings** | 20,000 |
| Sound Isolation **Design Project** | 7,500 |
| Sound Isolation **Build Guide** | 6,500 |
| Sound Isolation **Details** | 5,000 |
| Sound Isolation **Project Discovery** | 3,750 |
| Sound Isolation **BOM** | 3,750 |
| Total | £46,500 across 6 lines |

**Set that against the acoustic treatment design service: a £2,400 median across 41 engagements** (`Q45`). *The
isolation lines average **£7,750**, and the largest single one is **£20,000** — for drawings.*

**Three things follow, and the third is the important one.**

1. **The layer sells for multiples of the layer beside it**, for work of the same kind — discovery, design,
   drawings, details, a bill of materials, a build guide.
2. **It is sold as a ladder of named deliverables, not as one fee.** *Each step is separately priced and separately
   invoiceable.* **That is a live, in-house precedent for exactly the question `Q45` is stuck on** — *whether the
   treatment design fee should be per room, banded, or something else. **It is already answered next door: it is
   staged by deliverable.***
3. **It puts a number on `Q77`, which is all it adds.** *Neil's account of why the acoustic layer stalls — the
   consultant does not want it, the designer lacks the knowledge, the integrator will not spend the time, so
   **someone gets paid to design it** — **is his own practice, not a hypothesis this file confirmed.** *What the data
   contributes is the **rate**: £7,750 a step in the adjacent layer.* **The business has known this since it started
   invoicing it; the strategy documents did not.***

## 3. What the contradiction actually was

**The group layer said C-ATS covers *"reflection, resonance and reverberation, plus isolation"*. The C-ATS record
said *"not isolation — resonance is a treatment problem, isolation is a different one entirely."*** **Both are
correct, at different scopes**, and the repo had collapsed them:

- **The record's line is a *product* boundary.** *It sits in the **resonance panel's** record and says a corner
  absorber is not an isolation device. **True, and it must stay** — it guards against the commonest
  misapplication.*
- **The group's line is a *brand* boundary**, and it is right: **isolation lives under C-ATS.** *Neil's reason is
  contextual rather than technical — **it is part of the acoustic consultant's work**, and it fits no other brand in
  the roster.*

**So the fix is not to edit either sentence. It is to stop reading a panel-level exclusion as a brand-level one.**
*`../brands/c-ats/claims.md` `C1.46`.*

## 4. What this does to the three-layer account, one day old

**`C1.40`'s three layers were: isolation (architectural) · treatment (nominally the acoustic consultant's) ·
interior finish (interior design).** *Written yesterday's way, C-ATS was **the middle layer** and the other two
belonged to other people.*

**That is wrong in our favour. Two of the three layers are C-ATS's own scope, and the third is Fabric Walls'.**

| Layer | Whose decision it is | Whose product it is |
|---|---|---|
| Sound isolation | Architectural design | C-ATS |
| Acoustic treatment | Nominally the acoustic consultant | C-ATS |
| Interior finish | Interior design | Fabric Walls |

**So *"SRND is often involved in all three"* is not a claim about reach — it is a description of the product
range.** *Two brands out of six cover the entire acoustic-and-finish stack of a room. **The layer ownership stays
with three different disciplines; the supply does not.*** *That distinction is the whole point: **we are not
claiming to own their decisions, only to be the one supplier standing behind all three of them.***

## 5. Honest limits on the numbers above

- **The category assignment is derived by rule in this repo, not the business's own** — `../data/README.md` says so
  in terms, and lists the categories file as being *"for review and correction."* **The item descriptions are real
  invoice lines; the grouping into "Sound Isolation" is ours.**
- **These are invoice *lines*, not projects.** *Six isolation service lines is not six jobs, and the £46,500 is not
  an annual figure. **Do not restate it as either.***
- **Store rows only.** *Isolation sold through other routes, if any, is not in this file.*
- **`[?]` Whether the draft Shopify site lists isolation**, which Neil believes it does. *Not checked — and the
  invoice evidence is stronger than the site's, so it does not gate anything here.*

## Sources

- `../data/derived/srnd-store-item-categories.csv` — every distinct store item, its assigned category, line count
  and net
- `../data/README.md` § the classifier's three caveats
- `../registers/questions.md` `Q79` (Neil, 2026-08-19), `Q77`, `Q45`
