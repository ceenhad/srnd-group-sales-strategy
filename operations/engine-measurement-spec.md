# Engine — the measurement build, specified

**Status: design only. Nothing in this file has been written to engine, and nothing here was applied.**
*Neil, 2026-08-20: **"we are not directly writing anything to engine right now. We can design anything we want and
let them see it. The dev team are monitoring this repo."*** **So this is a specification for the dev team, not a
migration.**

**What it is.** *The gap between the KPI framework **already agreed** in `engine-as-hub.md` §1 (with Neil,
2026-08-14, hardened 2026-08-17) and **what engine actually holds**, measured read-only on 2026-08-20.* **The
framework is not reopened here** — *`engine-as-hub.md` is the authority and this file only says what is missing to
run it.*

**Why it is worth reading before building anything.** *Engine is under daily migration
(`20260820120000_duplicate_product` went in on the 20th). **Five of the six gaps below are one column or one lookup
each**, and the sixth is a decision rather than a build.*

---

## The measured state, 2026-08-20

| | |
|---|---|
| Live customers · typed | **350** · **17** |
| Customers carrying `source_brand_website` | **329** — *which brand's site brought them in, already recorded* |
| Leads | **4** *(the model is complete; the table is empty)* |
| Sales orders · linked to a project | **74** · **1** |
| Quotes · linked to a project | 13 · **10** |
| Projects · with `brand_id` · with `source_lead_id` | **50** · **0** · **0** |
| Products carrying `brand_id` | 163 of 166 |
| `sales_activities` | 78 |
| `support_tickets` | **0**, *with statuses and priorities defined* |
| Customers approved · terms accepted · marketing opt-in | 17 · 13 · **6** |
| Customers with an order · with 2+ brands | **35** · **2** |

---

## The six deltas

### `D1` — The account types in engine are not the agreed five

**Agreed** (`engine-as-hub.md` §1, *"account types — because cross-sell is only expected where cross-sell
applies"*): **whole-room integrator · single-brand trade · specifier/consultant · distributor · consumer**, *set at
account approval, on a screen already in use.*

**In engine:** `customer_types` holds **`dealer` · `distributor` · `end_user` · `specifier`**.

**So `dealer` is a merge of the two types the framework most needs to keep apart** — *a whole-room integrator is
measured on **breadth**, a single-brand trade account on **depth**, and the agreed reason for the split is that
**"a fit-out company buying only Fabric Walls is a beyond-cinema win, not a cross-sell failure."*** **Reporting
breadth against a merged `dealer` type produces exactly the false negative the framework was designed to avoid.**

**Change:** *add the two missing codes (`whole_room_integrator`, `single_brand_trade`), align `end_user` → `consumer`
naming, and **retire `dealer` once existing rows are re-typed** — 12 rows.* **And each type carries three parts the
lookup has no room for**: *a **qualifying rule** (one sentence), an **expectation profile** (which KPI views apply),
and a **review trigger** (behaviour outside the profile flags a human re-type, never an auto-change).* **`meta`
already exists on the lookup and is the natural home**, or three columns if they should be first-class.

*Then the population job: **333 of 350 customers are untyped**, and until they are, dealer and distribution cannot
be separated at all — which is the basis Neil named for **dual targets: a group target on dealer sales, a brand
target on distribution sales** (2026-08-19).*

### `D2` — "Every link carries a campaign tag" has nowhere to land

**Agreed:** ***"every link published anywhere carries a campaign tag. Full attribution machinery is a trap at this
size; tagged links plus per-stage conversion is the whole discipline, and it is a habit, not a build."***

**In engine:** *`lead_sources` holds **five** codes — `website` · `referral` · `trade_show` · `manual` · `import`.*
**There is no campaign, UTM, content or activity table anywhere in the schema.** *So a CPD seminar, an AI answer, a
press piece and a hook all arrive as `website`, and **no marketing activity is individually traceable** — which
makes `Q6`'s **"inbound generated per output, attributed via tags"** uncomputable today.*

**Change — one lookup and two nullable foreign keys, in house shape:**

- **`marketing_activities`** — `code`, `label`, `activity_type` *(hook · article · seminar · case study · press ·
  AI answer · email · social · event)*, `brand_id` *(nullable — group activities exist)*, `funnel_rung`, `url`,
  `starts_on`, `ends_on`, plus the standard `sort_order, meta, archived_at, created_at, updated_at`.
- **`leads.marketing_activity_id`** — the activity that produced this lead.
- **`customers.first_marketing_activity_id`** — *so attribution survives conversion.* `customers.lead_source_id`
  already sets the precedent for carrying source onto the customer.

**`lead_sources` stays as the coarse channel above it.** *Exploding a five-row lookup into fifty would lose the
channel view; this is the level underneath.* **Additive and nullable throughout, so nothing existing breaks.**

### `D3` — The inbound log is one column, not a new table

**Agreed:** ***"inbound is currently uncountable — it lands in mailboxes, calls and heads. So this rung creates one
capture requirement in engine: an inbound log, one field on a screen people already use."***

**In engine:** **`sales_activities` already is that screen** — *78 rows, polymorphic `entity_type`/`entity_id`,
`activity_type_id` (**call · email · meeting · note · task**), `subject`, `body`, `owner_id`, `follow_up_at`,
`completed_at`.* **What it cannot say is which way the contact went.**

**Change:** *a **`direction`** column on `sales_activities` (`inbound` / `outbound`).* **That is the whole inbound
log** — *the agreed framework's prediction of "one field" is literally correct.* *New-name versus existing-account
inbound is then derivable from `entity_type` (a `lead` versus a `customer`), which the framework distinguishes:
**new-name inbound is funnel, existing-account inbound is a service or cross-sell signal.***

*Not `activity_log` — that is the **system audit trail** (`entity_type, entity_id, actor_id, action, detail`, 391
rows) and must not be repurposed as a CRM log.*

### `D4` — The signal matrix is missing its first and middle tiers

**Agreed primitive:** *per **account × brand**, the highest signal tier reached in the period —*
**browsed → quoted → spec'd → ordered → repeat.**

| Tier | In engine |
|---|---|
| browsed | **Nothing.** *`shopify_webhook_events` exists (72 rows, raw payloads) but carries orders, not page views.* **The agreed point stands unbuilt: *"the store is fully gated, so every browse is a logged-in, identified account"*** — and Neil: knowing what people look at is *"100 % a lost opportunity right now"* |
| quoted | ✅ `quotes` |
| spec'd | **No field at all** — *and it is the tier Neil singled out: **"a quote is routine, being written into the project's spec is commitment"**, and it is the **terminal success tier for specifier accounts.*** Without it, specifier-type accounts have no success measure |
| ordered | ✅ `sales_orders.ordered_at` |
| repeat | ✅ derivable |

**Change:** *`spec'd` needs one state — the cleanest home is a nullable **`quotes.spec_confirmed_at`** or a stage on
`projects`, since being written into a spec is a fact about the project, not the quote. **The design decision is
which, and it is small.*** *`browsed` needs a store event stream landing in engine; that is a bigger piece and
should be scoped separately rather than bundled here.*

### `D5` — Three existing columns are not being filled

*No schema change. The model is right and the app is not writing to it.*

| Column | State | What it costs |
|---|---|---|
| `projects.source_lead_id` | 0 of 50 | A project cannot be traced to what caused it |
| `projects.brand_id` | 0 of 50 | Per-brand pipeline unavailable, though the column exists |
| `sales_orders.project_id` | 1 of 74 | Revenue cannot be attributed to the project it came from |

**And the asymmetry is the clue: `quotes.project_id` is 10 of 13.** *Quotes are being linked to projects and orders
are not — so this is a form-and-flow question in the app, most likely the order-from-quote path dropping the
reference.*

### `D6` — `G5`, "the first job succeeded", is a definition not a build

*`motion/motion-design.md` has called this the weakest signal since it was written.* **`support_tickets` now exists**
*(0 rows, statuses and priorities defined)*, **so *"an order with no support escalation within N days"* is definable
today.** *`projects.status_id` gives `won`/`lost`, which is a **project outcome, not an install outcome**, and should
not be used for this.*

**Change:** *none, until the definition is chosen. **Then it is an afternoon.***

---

## What needs no change — computable today

*Worth stating so the build is not overscoped:* **per-brand active accounts and revenue per period** *(`Q2`'s health
line)* · **accounts created per period** *(`Q1`)* · **first-order conversion and time-to-first-order** · **open
pipeline value per brand, win rate, time-to-close** *(`Q4`)* · **second-line interval** · **cross-brand account
count** *(`FACT-1`: `sales_order_lines` → `products.brand_id`, and it returns **2** today)*.

## Four things for Neil, not for the dev team

1. **The `spec'd` tier's home** — *on the quote, or on the project?* **It decides how specifier accounts are
   measured at all.**
2. **`G5`'s definition** — *"no escalation within N days", a completed verification, or a reorder?*
3. **Is registration the gate?** *Measured: **35 customers have ordered, 17 are approved, 6 gave marketing
   permission.** So `buyer-journey.md`'s *"registration is the hinge"* describes intended policy, not the observed
   system. **Close the gate or soften the claim** — it is not a data problem.*
4. **The qualifying rule, expectation profile and review trigger for each of the five account types** — *the
   framework says every type has all three, and none is written down yet.* **Without them `D1` cannot be populated
   consistently.**

## Sources

- `engine-as-hub.md` §1 — **the agreed framework this specifies against.** Not reopened here
- `SRND Engine` (`vzgdhfsmxteoxxsuexyg`) — read-only queries, 2026-08-20
- `../evidence/2026-08-20-gateway-instrumentation.md` — the same engine read against the `G1`–`G6` gateways
- `../motion/motion-design.md` — the gateway definitions; `../group-strategy/buyer-journey.md` — the journey and its unit
