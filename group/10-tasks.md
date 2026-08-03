# The tasks — what a sales person and a marketing person actually do

*Why this document exists, in one sentence: **"content is the sales rep" is a claim about tasks, and the tasks had
never been listed** — so nobody could say which of them the system performs, which it assists, and which stay
irreducibly human.*

`08-sales-motion.md` divides a rep's work into what content takes, what substitutes, and what stays human — but
selectively, naming the interesting cases rather than enumerating the job. `09-motion-design.md` component 5 gives
the named substitutes a mechanism. **This document is the exhaustive version**, and it adds the column both were
missing: **for each task, can it be automated, and if not, why not.**

Four things per task, and the order matters:

1. **Listed** — the whole job, not the interesting parts of it.
2. **Verified** — every row is a **claim about how SRND works today** until someone who does the work confirms it.
   Nothing here is verified yet. That is the point of the column, not an apology for it.
3. **Automation verdict** — one of four, defined below.
4. **Where it fits** — the journey stage or motion component it serves, and the record fields it consumes and
   feeds.

> **Read the verification column first.** This was assembled from the repo, not from watching anyone work. A wrong
> row is cheap to strike and expensive to build on — and *"we don't do that"* or *"that isn't how it happens"* is
> the most valuable thing this document can produce.

---

## The four verdicts

| Verdict | Means | The test |
|---|---|---|
| **`automated`** | Runs today with no person in the loop — engine, the store, the tools, published content | It happens whether or not anyone is at their desk |
| **`automatable`** | Could run with no person, given the record filled and engine's existing capability. **Not built** | The blocker is build or data, not judgement |
| **`assisted`** | A person is required, but the system carries most of the labour. **The judgement stays; the work moves** | Minutes of a person, not hours — the production-line split (`../decided.md` S5, S24) |
| **`manual`** | Irreducibly human. No amount of system removes it | Automating it would destroy the thing that makes it work |

**`assisted` is not a halfway house — it is the design.** The whole model rests on separating the judgement from
the labour: an owner's ten minutes of answers becomes an article, a video, a hook set and a datasheet paragraph.
A task marked `assisted` is one where that split works. A task marked `manual` is one where it does not.

---

## The sales person's tasks

*Performer today: `content` · `store/engine` · `tools` · `person` · **`nobody`**.*

**Renumbered once, at the first verification pass (2026-08-02), so the sequence follows the actual order of work.
Nothing cited these IDs yet; from here they are stable.**

| ID | Task | Verdict | Performer today | Where it fits | Record fields | Verified? |
|---|---|---|---|---|---|---|
| `T-S01` | Build the target list | `automatable` | `content` inbound; `person` for cold | Stage 1 | `O1` `H1` | claim |
| `T-S02` | **Reach a dealer who has never heard of us** — be findable when they search the problem, and be the answer an AI engine returns | **`automated`** | `content` — search, AI answers, social, press | Stage 1 · G1 | `H1` `H2` `O1` `R1` | claim |
| `T-S03` | Qualify the dealer | **`assisted`** | `store/engine` for the record; **a person for the read** | Stage 4 · G3 | — | **confirmed — instinct and rapport (Neil)** |
| `T-S04` | Qualify the project | **`assisted`** | `tools` surface it; **a person judges whether it is real** | Stage 2 · G2 | `D4` `N1` | **confirmed — instinct and rapport (Neil)** |
| `T-S05` | Present the range | **`assisted`** | `content` carries it; **a person reads the room** | Stage 2 | `D1` `O1`–`O4` `H2` | **confirmed — instinct and rapport (Neil)** |
| `T-S06` | **Discover** — their business, their fears, last job's failure | `assisted` — the conversation is human, **the capture is not** | the spec conversation | Stage 2–3 · **our only discovery channel** | feeds `O1` `N1` `N5` `R3` `W2` | **confirmed** |
| `T-S07` | Technical selling — help specify a live job | `assisted` | the design desk + `content` | Stage 3 | `D1`–`D10` `N1` `N2` `N5` | **confirmed** |
| `T-S08` | Produce a quote | **`automated`** | `store/engine` | Stage 4 · G4 | `M1`–`M3` | claim |
| `T-S09` | **Follow up through the project's lead time** — projects run long, so quote to order is often months of staying present without nagging | **`automatable`** | **`nobody` systematically** | Stage 4 · **the gap between G4's quote and its order** | `M2` `N6` `O3` | **added by Neil, 2026-08-02** |
| `T-S10` | Handle objections | `automatable` **once group 05 is filled** | `content` | Stage 3 · G3 | `R1` `X1`–`X5` `G1` | claim |
| `T-S11` | **Defend against a named competitor** | `assisted` — no comparison material exists to defend with | **`nobody`** | Stage 3 · G3 | `X1`–`X5`; **`X6` reads from engine's pipeline** | claim |
| `T-S12` | Negotiate terms | `manual` | `person` | Stage 4 | `M4` | claim — *largely settled: pricing gated, no dealer credit (`../decided.md` C8)* |
| `T-S13` | **Close — want the order and ask for it** | **`manual`** | `person` — **unnamed** (component 5) | Stage 4 · G4 | `M4` `O3` | claim |
| `T-S14` | Onboard the account | **`automated`** + assisted welcome | `store/engine` | G3→G4 | `M1` `L1` | claim |
| `T-S15` | Make the first install succeed | `assisted` | `content` — manuals, how-do-you-do-X | Stage 5 · G5 | `L1`–`L3` `R4` `N3` | claim |
| `T-S16` | Post-delivery follow-up | `automatable` | the post-hinge touch set | Stage 5–6 | `L3` `N8` | claim |
| `T-S17` | Account management — stay recalled | `assisted` | `content` always-on + `person` | Stage 6 | `N5` `N6` | claim |
| `T-S18` | Cross-sell the rest of the group | **`automatable`** | the adjacency prompt at the spec moment | Stage 6 · G6 | `D10` `N5` `N6` `O3` | **confirmed (Neil)** |
| `T-S19` | Prompt the reorder | `automatable` | `store/engine` triggers | Stage 6 | `M1` `M2` | claim |
| `T-S20` | Recover a failure | **`manual`** | `person`, thinly covered | Stage 5 | `R4` `L4` `L5` → `N8` `X6` | claim |
| `T-S21` | Train the dealer's staff | `automatable` | `content` — assembled from the corpus (`../decided.md` S12) | Stage 5–6 | `A6`–`A9` `N1`–`N4` | claim — *parked with the training programme* |
| `T-S22` | Pipeline and forecast | **`automated`** | `store/engine` | — | — | claim |
| `T-S23` | **Bring back market intelligence** | **`assisted`** — *possibly `automatable`; no worse than assisted* | **`nobody`** | — | feeds `X1`–`X5`; **win/loss already in engine** | **confirmed (Neil)** |
| `T-S24` | **Feed product development** | `assisted` — capture manual, aggregation automatic | **`nobody`** | — | feeds `X4` `N9` | claim |
| `T-S25` | Events and keeping relationships warm | `manual` | `person` | Stage 1–2, 6 | `H2` | claim — *ISE booked; CEDIA out (`../decided.md` E1–E3)* |
| `T-S26` | Territory planning | **`assisted`** | `person` | — | `C2` | **confirmed (Neil)** |
| `T-S27` | **The novel problem** — *"can you do this impossible project?"* | **`manual`** | the authority | Stage 3 | feeds `N8` `N9` | claim — *the business's best work* |
| `T-S28` | Recognition and thanks | **`manual`** | `person` | Stage 6 | — | claim — *acts, not publications* |

## The marketing person's tasks

*Never inventoried before. SRND has no marketing department, so the point of the list is to see which tasks have a
performer and which have simply never been assigned.*

| ID | Task | Verdict | Performer today | Where it fits | Record fields | Verified? |
|---|---|---|---|---|---|---|
| `T-M01` | Market and segment research | **`assisted`** | `person`, thin | — | — | **confirmed (Neil)** |
| `T-M02` | **Competitor tracking** | `automatable` in part — public sources | **`nobody`** | Component 5 | feeds `X1`–`X4` | claim |
| `T-M03` | Positioning and messaging | **`assisted`** | the owner — done, in `brands/<brand>/positioning.md` | — | `D1` `O1`–`O4` → `G2` | **confirmed (Neil)** |
| `T-M04` | Campaign planning | `assisted` | the pathways + hook matrix | Component 1 | `H1` `O1` `R1` | claim |
| `T-M05` | **Content production** | **`assisted`** — drafting automated, truth-check never | **the production line** (component 2) | Every stage | **the whole record** | **confirmed** (`../decided.md` S24) |
| `T-M06` | Editorial calendar and cadence | `automatable` | the churn queue | Component 2 | `R3` `N3` | claim |
| `T-M07` | Channel management | `assisted` | per brand | Component 4 | — | claim |
| `T-M08` | **Discoverability — search *and* AI answers** | `assisted` | `content`, **owner unclear** | Stage 1 · G1 | **`O1` `N3`** | claim |
| `T-M09` | Lead capture and nurture | **`automated`** | `tools` + `store/engine` | G2 · G3 | `N1` | claim |
| `T-M10` | Collateral — datasheets, case studies | `assisted` | the generation gates | Stage 2–3 | `D`/`G`/`A` groups | claim |
| `T-M11` | Brand consistency | **`automated` at drafting time** | guardrails baked into the line | Component 2 | `G2` | claim |
| `T-M12` | **Dealer marketing support** — material a partner uses with their own client | `assisted` | **`nobody`** | Stage 6 | **`N7`** | claim |
| `T-M13` | Events and exhibitions | `manual` | `person` | Stage 1 | — | claim |
| `T-M14` | Trade press and PR | `assisted` | thin — the EI microsite runs near-empty | Stage 1–2 | `H2` `G4` | claim |
| `T-M15` | Measurement and reporting | `automatable` | defined; **instrumentation partly unowned** (`../backlog.md` W8) | Every gateway | `H3` | claim |
| `T-M16` | CRM and data hygiene | **`automated`** | `store/engine` | — | — | claim |
| `T-M17` | **Product launch** | `assisted` | **`nobody`** | Stage 2 | `G3` `D1`–`D10` `H2` | claim |
| `T-M18` | Budget and spend allocation | `manual` | the owner | — | — | claim |

---

## What the register says

### The shape of the answer to "can content be the rep?"

*Counts as at verification pass 1 (2026-08-02). **Nine verdicts changed in that pass** and the shape moved
noticeably — see the note below.*

| Verdict | Sales | Marketing | Total | Share |
|---|---|---|---|---|
| **`automated`** — runs today with nobody | 4 | 3 | **7** | 15 % |
| **`automatable`** — could, not built | 7 | 3 | **10** | 22 % |
| **`assisted`** — judgement stays, labour moves | 11 | 10 | **21** | 46 % |
| **`manual`** — irreducibly human | 6 | 2 | **8** | 17 % |
| | **28** | **18** | **46** | |

**What the first verification pass changed, and it is worth reading as a finding in itself.**

- **The front of the funnel is more human than the desk version assumed.** Qualifying a dealer, qualifying a
  project and presenting the range all moved from `automated`/`automatable` to **`assisted`** — *"human instinct
  and rapport are needed there"* (Neil). The system supplies the record and the reach; **a person still reads the
  room.**
- **A whole task was missing, and it sits in the most expensive gap in the funnel.** `T-S09`: **projects run
  long**, so quote-to-order is often months. There is a lengthy follow-up stage between producing the quote and
  asking for the order, **nobody runs it systematically, and it is automatable.** That is the clearest
  build-it-and-it-pays item the register has produced.
- **The middle and back moved the other way.** Cross-sell is `automatable`, not assisted. Market intelligence is
  **at worst `assisted`, possibly `automatable`** — which reduces the "no substitute exists" hole from a wall to a
  build. Territory planning, market research and positioning are all `assisted` rather than irreducibly manual.
- **Net effect: `assisted` is now 46 % and `manual` is down to 8 tasks.** The irreducible residue is
  **negotiating · asking for the order · recovering a failure · events (sales and marketing) · the novel problem ·
  recognition · budget.** Every one of them is relationship or judgement, which is a coherent list rather than an
  arbitrary one — and it is a smaller residue than the desk version claimed.
- **Every `assisted` task depends on the record.** Assisted work is a person reviewing what the system drafted, and
  the system can only draft from the record. **An empty record silently reverts every assisted task to manual** —
  and with `assisted` now the largest category by some way, that dependency got stronger, not weaker.

### The unowned tasks, in one place

**Seven tasks have no performer at all**, and they split three ways:

| | Task | Kind |
|---|---|---|
| `T-S09` | **Follow up through the project's lead time** | execution — **and automatable** |
| `T-S11` | Defend against a named competitor | outward-sensing |
| `T-S23` | Bring back market intelligence | outward-sensing |
| `T-S24` | Feed product development | outward-sensing |
| `T-M02` | Competitor tracking | outward-sensing |
| `T-M12` | **Dealer marketing support** | execution |
| `T-M17` | **Product launch** | execution |

**The four sensing tasks are one job, not four gaps.** Nobody is looking at the market or at rivals. **Not "at why
we lose" — that was wrong**: engine's CRM does classic pipeline management and already records win/loss (Neil,
2026-08-02). The gap is that nothing *reads* it into the competitive group. Recorded as evidence that component 5's *"market intelligence: no substitute exists"* hole is wider than the
one line it was logged as — **and, per the first verification pass, shallower than it was logged as too**: market
intelligence is at worst `assisted` and possibly `automatable`, so it is a build rather than a wall. Role, standing
habit, or accepted hole is `../backlog.md` SYS-6.

**The three execution tasks are ordinary work nobody was assigned**, and one of them is new:

- **`T-S09` follow-up through the lead time.** Projects run for months; the quote goes out and then the stage that
  decides whether it converts belongs to nobody. **Automatable, unbuilt, and sitting directly on the revenue
  path** — the strongest candidate on this page for building something.
- **`T-M17` product launch. The Screen Wall is the invoice** — engineered, demonstrable since ISE 2023,
  commercially invisible for three years. Not a content failure, an unassigned task (`../backlog.md` SYS-8).
- **`T-M12` dealer marketing support** — material a partner hands their own client. No performer, no artefact, and
  its record field (`N7`) empty for all 38 record scopes. In a group whose stated advantage is *depth spent on the
  dealer's behalf*, **the sharpest gap on this page between what the strategy says and what exists.**

---

## What to do with this document

1. **Verify it.** Every row is `claim`. Sit with whoever does the work and mark each `confirmed`, `wrong` or
   `we don't do that`. **Expect to strike rows** — an invented task is worse than a missing one because it
   generates work that serves nobody.
2. **Then re-read the verdicts.** An automation verdict on an unverified task is a guess about a guess.
3. **Then decide the unowned five** (`SYS-6`, `SYS-8`).
4. **Do not treat `automatable` as a build list.** Nine tasks could run without a person; that does not mean nine
   things should be built. Most wait on the record being filled, which is cheaper and comes first.
5. **Keep it in step with the record.** When a group of the form changes, the fields columns here change with it.
   The task register and `../product-record-template.md` are two views of one system.
