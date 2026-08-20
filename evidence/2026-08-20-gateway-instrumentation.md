# Traceable success — the six gateways mapped to engine, measured 2026-08-20

*`JNY-1` completed: **"map the six gateway signals against what engine, the store and the tools already capture —
the gap list is the deliverable."*** *Read directly from engine (`SRND Engine`, project `vzgdhfsmxteoxxsuexyg`),
read-only. **Answering Neil's three questions: what traceable success looks like per brand through the journey, how
it connects back to activities, and how those activities are implemented.***

**And the framing correction that made this possible** *(Neil, 2026-08-20)*: ***"remember it's our platform and we can
do what's needed on it."*** **Earlier notes in this repo treated engine as a fixed constraint to work around. It
isn't.** *It is under active migration — the latest is `20260820120000_duplicate_product`, applied today — so a
missing field is a decision not yet taken, not a wall.*

---

## 1 · What traceable success looks like — the funnel, measured for the first time

*The unit is the one `buyer-journey.md` already states: **the dealer relationship, across the group, over time.**
Brand detail sits underneath it.*

| Gateway | The state change | What engine holds | Count today |
|---|---|---|---|
| **G1** (1→2) | The hook landed — someone with a problem found us | **Not in engine.** *Engine sees a visitor only once they become a lead. **Which brand's site they arrived at is recorded** — `customers.source_brand_website`* | **Needs web analytics.** *Brand-of-entry known for **329 of 350** customers, and unread* |
| **G2** (2→3) | The proposition landed — worth their time | `leads.enquiry_type`, `leads.product_id`, `leads.source_brand_site`; `knowledge_topics` (**257**) with questions, answers and gaps | **4 leads.** *The instrument is built and essentially unused* |
| **G3** (3→4) | **Registration, the hinge** — with marketing permission given willingly | `customers.approved_at`, `terms_accepted_at`, **`marketing_opt_in_company`** | **6** *(marketing opt-in — the gateway's own definition)*. 17 approved · 13 terms accepted |
| **G4** (4→5) | The first order placed | `sales_orders.ordered_at` | **35 customers have ordered** |
| **G5** (5→6) | The first job succeeded | **`support_tickets` exists** with statuses and priorities — *so "no escalation" is definable*. `projects.status_id` gives `won`/`lost`, which is a **project outcome, not an install outcome** | **0 tickets. Still needs defining**, exactly as `motion-design.md` said |
| **G6** (6→loop) | A second layer of the room is ours | `sales_order_lines` → `products.brand_id` per customer — `FACT-1`'s query | **2 customers across 2+ brands** |

**So the funnel today is 6 → 35 → 2**, and **the shape of it is the first finding.**

> **⚠ `G4` is five times `G3`, which means G3 is not the gate the journey assumes.** *35 customers have ordered;
> **6** gave marketing permission and 17 are approved. **So ordering does not currently require crossing the
> registration hinge** — and `buyer-journey.md` §"The on-ramp: registration is the hinge" is describing an intended
> policy, not the observed system.* **That is either a gap to close or a claim to soften, and it is not a
> measurement problem.**

## 2 · How success connects back to activities — the chain, and where it breaks

**The full chain already exists in engine**, and it is better than this repo assumed:

`leads` *(source, brand site, enquiry type, product)* → **`projects.source_lead_id`** → `projects.brand_id` →
`quotes.project_id` → `sales_orders.project_id` → `sales_order_lines` → `products.brand_id`

**Four links are empty or too coarse. That is the entire gap list.**

| # | Link | Field | State | What it costs |
|---|---|---|---|---|
| **B1** | **Which activity generated the interest** | `leads.lead_source_id` → `lead_sources` | **5 codes: `website` · `referral` · `trade_show` · `manual` · `import`** | ***"Website" cannot tell a CPD seminar from an AI answer from a press piece from a hook.*** **No campaign, UTM, content or activity table exists anywhere in engine.** *So **no marketing activity is individually traceable** — which is precisely the question being asked* |
| **B2** | Lead → room | `projects.source_lead_id` | **0 of 50** | *A project cannot be traced back to what caused it* |
| **B3** | Room → brand | `projects.brand_id` | **0 of 50** | *Per-brand pipeline is unavailable, though the column exists* |
| **B4** | Room → order | `sales_orders.project_id` | **1 of 74** | *Revenue cannot be attributed to the project it came from.* `quotes.project_id` is **10 of 13**, so **quotes are linked and orders are not** |
| — | Dealer vs distributor | `customers.customer_type_id` | **17 of 350** | *The dual target cannot be split at all (`ENG-1`)* |

**`B1` is the one that needs a schema change. `B2`–`B4` are population and app workflow, not database design** —
*the columns are there and nothing is filling them, which is a question about the app's forms rather than about the
model.*

## 3 · What the activities are, and how they are implemented

**The activity layer exists in this repo, in `../motion/`** — *the content operation (`content.md`), the sales motion
(`sales-motion.md`), the work items and task shapes. And the hook layer is defined in `motion-design.md`: **many
hooks per door, categorised by appeal** — more revenue · time saved · easier to do · better results · the problem
named.*

**The implementation gap is not that the activities are undefined. It is that none of them emits anything engine can
count.** *A hook, a seminar, an AI answer and a press piece all arrive as `lead_source = website`, if they arrive at
all. **So the activity list and the measurement system have no common vocabulary**, and no amount of reporting will
create one.*

**Which makes the sequence unavoidable:** *name the activities as rows with codes → carry the code from the activity
into the lead → then the funnel above splits by activity, per brand.* **Without the first two steps, "which of our
activities works" is unanswerable no matter what is measured.**

---

> **⚠ Two corrections to this file, both 2026-08-20, and the first matters more.**
>
> **1. There is an agreed KPI framework and `G1`–`G6` is not it.** *`../operations/engine-as-hub.md` §1 — **agreed
> with Neil on 2026-08-14 and hardened on the 17th** — sets the funnel spine as **published → reached → inbound →
> account → first order → active → multi-line → loop**, with the primitive being the **account × brand signal
> matrix**: **browsed → quoted → spec'd → ordered → repeat**. **That is the authority.** The gateway mapping above
> stands as a valid read of engine, but **it must not become a third vocabulary** — the implementation gaps are now
> specified against the agreed framework in `../operations/engine-measurement-spec.md`, which found **two tiers
> engine cannot see at all** (`browsed`, and **`spec'd` — the commitment signal, and the terminal success tier for
> specifier accounts**).*
>
> **2. Nothing is applied to engine from here.** *Neil, 2026-08-20: **"we are not directly writing anything to engine
> right now. We can design anything we want and let them see it. The dev team are monitoring this repo."*** *The
> design below is right; **the "apply it, testbed first" framing was wrong** and is replaced by a specification the
> dev team can read.*

## The change proposal — designed here, built by the dev team

**Engine is ours and under daily migration, so a missing field is a decision not yet taken — but this repo specifies
rather than applies.** *House convention:
`YYYYMMDDHHMMSS_snake_case_name`; lookups carry `id, code, label, sort_order, meta, archived_at, created_at,
updated_at`.*

**`B1` — the marketing-activity dimension.** *One new lookup, matching house shape, plus two nullable FKs:*

- **`marketing_activities`** — *`code`, `label`, `activity_type` (hook · article · seminar · case study · press ·
  AI answer · email · social · event), `brand_id` (nullable — group activities exist), `gateway` (`G1`–`G6`), `url`,
  `starts_on`, `ends_on`, plus the standard lookup columns.*
- **`leads.marketing_activity_id`** → the activity that produced this lead.
- **`customers.first_marketing_activity_id`** → *so attribution survives conversion; `customers.lead_source_id`
  already sets the precedent for carrying source onto the customer.*

*Additive and nullable, so nothing existing breaks. **`lead_sources` stays as the coarse channel; this is the piece
underneath it**, which is the right split rather than exploding a five-row lookup into fifty.*

**Then, and these are not schema:** *populate `customer_type_id` (`ENG-1`, 333 rows) · make the app set
`projects.source_lead_id`, `projects.brand_id` and `sales_orders.project_id` · define `G5` before instrumenting it ·
and decide whether registration really is the gate, given `G4` is five times `G3`.*

**One sequencing note, for whoever builds it.** *There is an **`SRND Engine Testbed`** project alongside production —
a live system with 74 orders in it deserves a rehearsal. **Not this repo's call to make, and not this repo's hand on
the migration.***

## Sources

- `SRND Engine` (`vzgdhfsmxteoxxsuexyg`), read-only queries, 2026-08-20
- `../motion/motion-design.md` § the gateway table — the `G1`–`G6` definitions this maps
- `../group-strategy/buyer-journey.md` § Metrics — the unit, and *"progress (not yet instrumented)"*
- `../registers/backlog.md` `JNY-1` — the task this completes
