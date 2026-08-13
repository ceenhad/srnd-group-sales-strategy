# What engine already does — the audit

*Read against engine directly on **2026-08-13** (Supabase project `vzgdhfsmxteoxxsuexyg`, read-only, 200-odd tables
in `public`). **This file exists because three ready rows name the same deliverable — a gap list**: `TSK-5`
(does engine already do `detect`/`record`/`route`), `DOC-12` (what engine models against the record's fields), and
`REC-0` (the 15 operational-capture rows). It is evidence, not argument. Where it contradicts a belief in this repo,
**engine is right and the repo is wrong** — the same rule `product-register.md` already applies.*

> **S16a discipline, and it earned its keep again.** This repo has assumed an engine gap twice and been wrong both
> times. **It has now been wrong a third time, in the same direction** — engine holds considerably more than the plan
> credits, including a document-generation layer and a question-and-answer mechanism nobody here knew existed.
> **But it was right about the one thing that matters most:** group 04, the knowledge layer, has no home in engine
> and no home anywhere else either.

---

## 0 · First, a correction that changes how to read every count below

`current-state.md` records **"Engine is the CRM — years of real project and prospect data."** The account data
supports that; **the transactional history does not.**

| What | Actually in engine | Reading |
|---|---|---|
| Customers · contacts | **348** · **591** | Real depth — **migrated** (every core table carries a `monday_legacy_id`; `lead_sources` includes `import`) |
| Sales orders | **77**, first **2026-05-28**, last **2026-08-12** | **Eleven weeks**, not years |
| Quotes | **12** — 2 won, **0 rejected** | The pipeline is newly live |
| Sales activities | **78**, first **2026-06-11** | Nine weeks |
| Projects | **58** | Includes historic entries |

**So engine is a young system holding migrated accounts, not an archive of years of pipeline.** The consequence
lands hardest on group 05: `product-record-template.md` says **"`X6` is largely a read from engine's pipeline
rather than something to capture afresh."** **That is not available *from engine* today** — there is no won/loss
reason structure (§3, REC-2) and no loss history in it to read even if there were.

> **Refined the same day, from Neil — and it improves the position.** The eleven weeks is **engine's** history, not
> the business's. Two things sit outside it. The accounts came from **Shopify, where a record only exists once a
> customer has signed a form** — so those 348 accounts are about as clean as this data gets, and can be trusted
> accordingly rather than treated as an import of unknown quality. And **the old Monday.com CRM logs still hold the
> historical pipeline**; they have not been handed over yet. **So the archive exists — it is simply not in engine.**
> `X6` becomes *capture forward, and possibly backfill backwards*, which is materially better than capturing from
> zero, and it makes the Monday logs a named asset rather than a loose end (`MON-1`).

**Where the repo expected to mine engine, it must capture forward and mine Monday backwards.** A plan correction,
not a new argument.

### Why the gaps fall where they do — and why it is not a defect

**Engine was written by Simon, who thinks operations-first.** That one fact explains the shape of §1 better than any
per-field reasoning: what a product *is*, what it *costs*, how it is *configured, priced, built, shipped and
documented* is modelled thoroughly and in places elegantly. What a rep *says* is absent. **The system is complete
against the frame it was built in.**

**Two consequences, neither of them a criticism.**

1. **The gap is predictable, so stop rediscovering it.** Any future *"does engine hold this?"* resolves to *is this
   operational, or is it selling?* Operational — assume engine has it and check. Selling — assume it does not.
   That is a cheaper rule than three audit rows.
2. **It names the standing risk.** Nobody's default frame is the knowledge layer, which is why group 04 is empty in
   a system modelling 200-odd tables of everything else. **That is the roles decision (`PAR-3`) restated as a system
   fact:** the knowledge half needs an owner or it will keep not happening, however good the platform gets.

**And the opportunity is the actual headline.** The whole company now works in engine and the group owns the
platform outright — so a capture route is not a new habit bolted onto a system, it is **a field on a screen people
are already using every day**, which is the difference between a documentation push and a route that runs forever
(`SYS-1`). **That is why the `knowledge_topics` mechanism (§2) matters out of proportion to its size:** it is
existing proof the platform extends into exactly this territory, built by the people who own it.

---

## 1 · The 58 fields — which have a system home

**Verdicts:** `canonical` = engine is the source of truth · `partial` = adjacent or half of it ·
`built, empty` = the structure exists and is unused · `none` = no home in engine.

**Headline: 13 of 58 canonical or near, 12 partial, 4 built-but-empty, 29 with no home at all** — and the 29 are
almost exactly the front half plus the knowledge layer. **Engine holds what a product *is* and how it is *sold and
shipped*. It holds nothing of what a rep *says*.**

### 01 · What it actually is — the definitional layer

| Field | Verdict | Where in engine |
|---|---|---|
| `D1` What it is | **partial** | `products.marketing_description` (93 of 164), `quote_description` (2), `seo_title`/`seo_description` (**0**) — one prose blob, not a category sentence |
| `D2` What it does | **none** | — |
| `D3` How it works | **partial — and better than expected** | No prose field, but **the mechanism grouping already exists**: `product_families` (14) and `products.product_type` (12 values) |
| `D4` What it is for | **none** | — |
| `D5` What it is *not* for | **none** | — |
| `D6` Scope of supply | **partial** | `boms` (8) · `bom_lines` (43) · `kit_lists` (**0**) — the production view of what's in the box, not the dealer-facing statement |
| `D7` What it requires from others | **none** | `product_technical.voltage_options` touches power only |
| `D8` Configuration space | **canonical** | `product_variants` (**821**) · `option_types`/`option_type_values` · `product_default_configurations` · `available_aspects`/`available_surfaces` · `width_formula`/`height_formula` · `sku_token_registry` · `configurator_sessions` |
| `D9` Limits | **partial → canonical for dimensions** | `product_technical.min/max_viewable_width_mm`, `max_height_overrides`, `depth_mm`, `bezel_mm`. **Environmental limits: none** (an `operating_conditions` spec category is defined but carries no fields) |
| `D10` Where it sits | **none** | `product_categories` (17) is adjacent, not the room layer |

### 02 · Why to buy it — `O1`–`O5`

**All five: `none`.** Nothing in engine holds a problem in the dealer's words, labour saved, opportunity opened,
what it replaces, or entry-versus-flagship. `marketing_description` is the only text field in the vicinity and it is
an undifferentiated blob. **This is the on-ramp half of S15 and it has no system home anywhere.**

### 03 · The doubt it removes

| Field | Verdict | Where |
|---|---|---|
| `R1` The doubt it meets | **none** | — |
| `R2` Load-bearing asset | **none** | — |
| `R3` The questions it generates | **none for products** — **but the mechanism exists** | See §2: `knowledge_questions`/`knowledge_gaps` do exactly this shape, pointed at engine's own UI |
| `R4` What goes wrong on site | **built, empty** | `support_tickets` (**0**) · `rmas.reason`/`inspection_notes` (**0**) · `qc_fail_reasons` (7 defined) · `eco_categories.defect`. **The structure is there and nothing has been filed** |

### 04 · The knowledge layer — `N1`–`N9`

**All nine: `none`.** Verified, not assumed. The template's claim — *"engine does not hold it, the website does not
hold it"* — **is correct**, and this is the group the whole exercise exists for.

One partial: `N5` compatibility has fragments (`position_templates` + 47 slots, `fabric_stretch_bands`,
`cnc_tool_material_compat`) but these are **internal build compatibility, not product pairing for a dealer**.

**And the finding that saves real work — see §2.** Engine already runs a question → answer → gap → summary
mechanism with answer state and attribution. **`N3` should extend it, not duplicate it.**

### 05 · Competitive — `X1`–`X6`

**All six: `none`** — and `X6` specifically corrects the plan. `quotes` carries `won_at`; there is **no `lost_at`,
no loss reason, no competitor field, and no dimension**. `quote_statuses` offers `rejected` (0 quotes in it) and
`project_statuses` offers `lost` — so **the *fact* of a loss has a home; the *reason* has none.** The only `reason`
fields nearby are `discount_reason` and `approval_denial_reason`, neither of which is this.

### 06 · Commercial

| Field | Verdict | Where |
|---|---|---|
| `M1` Order unit and minimum | **none** | `reorder_point`/`reorder_quantity` are internal stock policy, not the dealer's order unit |
| `M2` Lead time, and what changes it | **canonical** | `products.default_lead_time_days` (57 of 164) · `product_technical.lead_time_days` · **`quote_lines.lead_time_days_at_quote_time`** — a snapshot per quoted line, which is more than the record asked for |
| `M3` Availability posture | **partial** | `products.source_type` (**164 of 164**) plus `parts_mode` and `product_statuses` — close to `stocked`/`made to order`/`made to size` without being it |
| `M4` The dealer's business case | **none** | `brand_tier_margins` / `*_cost_multipliers` hold **our** margin, not the dealer's case |
| `M5` What not specifying it costs | **none** | — |

### 07 · Lifecycle & support

| Field | Verdict | Where |
|---|---|---|
| `L1` Order to site | **built, empty** | `sales_order_statuses` models 10 stages through `delivered`; `sales_order_boxes`, `shipments`, `carriers` all **0** |
| `L2` Install sequence, and who does it | **none** | `sub_task_templates` (82) are **manufacturing** steps, not install |
| `L3` Commissioning & verification | **none** | `qc_templates` (7) / `qc_checks` (3) are factory QC, not site commissioning |
| `L4` Serviceability | **none** | the RMA flow is adjacent |
| `L5` What we support, and for how long | **built, empty** | `products.warranty_months` — **1 of 164 filled**; one authored `doc_block` holds warranty terms for one brand |

### 08 · Hook material — `H1`–`H3`

`H1`, `H2`: **none**. `H3` *(what has actually bitten)*: **partial** — `leads` carries `source`,
`enquiry_type`, `source_brand_site` and `product_id`, so an enquiry **can** be attributed to a product and a site
(4 leads so far). That is the raw signal for source-tagged hooks (S23); the hook-to-catch link itself is unmodelled.

### 09 · Who decides — `W1`–`W2`

**`W1`: partial.** `contacts` (591) · `contact_role_types` (**buyer, technical, installer, finance, logistics,
sales**) · `contact_role_assignments` (47), and `customer_types` includes **`specifier`** at account level.
**So "buyer" is modelled per contact and "specifier" only per account** — the distinction the field exists to draw
is half there. **`W2`: none.**

### 10 · What we may and may not say

| Field | Verdict | Where |
|---|---|---|
| `G1` Claims supported | **none — but the mechanism is exemplary** | `product_field_specs.provenance` marks a value `predicted_measured` vs `none`, with `risk_tier`. **That is claim provenance per field, already built** — just only over 35 spec fields for screens and speakers |
| `G2` The claims we refuse to make | **none** | The template calls this a hard gate. Nothing in engine expresses a wording boundary |
| `G3` Marketing status | **canonical** | `product_statuses` (`draft` · `pre_release` · `released` · `active` · `superseded` · `cancelled`) + `product_generation_statuses` + `product_store_listings.is_published`. **Maps onto G3's four values almost exactly** |
| `G4` Proof available, and publishable? | **none** | `product_images.usage` (an array) is the nearest thing to a permission concept |

### 11 · Where it is sold

**`C1` Channel: canonical** — `product_store_listings` (106) × `stores` (`dt`, `profi`, `srnd_store`) ×
`is_published`.

> **But it returns live evidence against the rule.** `C1` states **"No product exists in two places."**
> **Thirteen DT product codes are currently listed on both `dt` and `srnd_store`** — DT-DYN, DT-HB, DT-MMD,
> DT-VMM, DT-PHG and eight others. Either the rule means something narrower than it says (a brand store plus the
> group store is the intended arrangement) or 13 listings contradict it. **Logged as evidence for
> `open-items.md`; not a reversal, and not mine to settle.**

**`C2` Territory: partial** — `product_field_specs.required_by_market` and `doc_block.market_scope` exist as arrays,
`customers.country` per account. No per-product territory restriction.

### 12 · The asset audit — `A1`–`A11`: **the biggest find in the audit**

**Engine has a document generation layer, and this repo's plan does not mention it.**

- `doc_document` (7 live): `doc_kind` · `status` (draft/released) · `origin` (**generated** vs **external**) ·
  `revision` · `supersedes_id` · **`stale`** · `last_published_at` · `pdf_url` · **`content_snapshot`**, which
  *"freezes the field values + template hash that produced the PDF"*
- `doc_template` (3): a **Pro-Fi speaker datasheet**, a **DT screen manual**, and a test
- `doc_template_slot` (16): `spec_table` by group, `variant_table`, `block_ref`, `cover_page`, `universal_info`
- `doc_block` (2): reusable authored blocks, versioned, with `status` and `approved_by`
- `doc_generation_log` + **`coverage_rule`** and a **`coverage_snapshot`** per generation

| Asset | Verdict |
|---|---|
| `A1` Datasheet | **canonical mechanism** — a template exists and generates; also holds suppliers' own PDFs for distributed lines as `origin=external` |
| `A2` Dimensioned drawings | **partial** — `fabricwalls_drawings` (9) |
| `A3` CAD | **partial** — `material_cad_files` (103), `cnc_files` (3), `cnc_file_distributions` |
| `A4` BIM · `A5` NBS | **none** — `doc_kind` could carry them |
| `A6` Install manual | **canonical mechanism** — the DT screen manual template generates, versions and flags stale |
| `A7`–`A11` commissioning · fault-finding · video · training · spares | **none** |

**Two consequences.** The asset-state vocabulary the record defines (`current` / `exists — stale` / `missing`) is
**already implemented** as `status` + `stale` + `last_published_at`. And `coverage_rule` +
`doc_generation_log.coverage_snapshot` **is the completeness meter** — which means `DOC-15` (*operationalise the
completeness gate*) has a host and is not a from-scratch build.

### 13 · Record keeping

`K1` owner: **partial** — `roles` (17, including `salesperson`, `sales_director`, `designer`) and
`role_memberships` give a role vocabulary, but nothing owns a *record*. `K2` last reviewed / `K3` review interval:
**none** for a marketing record — though `doc_document.stale` and `last_published_at` are the same idea, already
working, one layer down.

---

## 2 · `TSK-5` proper — `detect`, `record`, `route`

**The verdict: build the rules, not the plumbing.** All three primitives have a spine in engine. `TSK-6` is
smaller than the register implies for two of them, and unchanged for the third.

**`detect` — appears in 20 tasks. Verdict: the signals exist; nothing fires on them.**
`activity_log` (310) · `shopify_webhook_events` (72) · `customer_shopify_company_refs` (338) ·
`notifications` (20) · `counters` (22) · `leads` with source and product attribution · quote and order state
machines. Brand coverage per account is derivable today (`sales_order_lines` → `products.brand_id`), which is
`FACT-1`. **What is missing is computation, not capture:** nothing derives reorder cadence, nothing computes a
recognition trigger, nothing watches a quote ageing between sent and won — which is exactly `TSK-3`'s
lead-time follow-up, and it has a data spine waiting for it.

**`record` — appears in 30 tasks. Verdict: it splits, cleanly, and the split is the whole finding.**
The **operational** record is engine's and largely built (§1: config, lead time, channel, status, documents).
The **knowledge** record — group 04, plus `O`, `X`, `H` — has no home in engine and none anywhere else.
**So `record` is not one build. It is "use engine" for two-thirds and "the genuine gap" for the third that
carries the selling.**

**`route` — appears in 11 tasks. Verdict: more built than assumed.**
`notifications` · `tasks` (23) with `task_watchers` and `task_activity` · `chat_threads` (264) /
`chat_messages` (114) · `quote_approvals` (4) with `profile_approval_limits` · and notably
**`leads.referred_to_customer_id` + `referral_status`** — routing an enquiry out to a dealer is already modelled,
which is the partner-programme referral mechanic in embryo.

**And an unexpected fourth.** Engine already hosts an agent layer: `agents` (2), `agent_runs` (62),
`agent_tasks` (97), `agent_proposals` (2), `agent_url_fetches` (9), `agent_budgets` (2), `engine_ai_audit` (6),
plus `automation_types` (10). **`assemble` has a host with budgets and an audit trail.** Anything this repo
proposes to automate should be proposed *into* that, not beside it.

### The reusable mechanism nobody here knew about

`knowledge_topics` (**257**) → `knowledge_questions` → `knowledge_answers` → `knowledge_gaps` →
`knowledge_summaries`.

**Read the subject before celebrating.** The 257 topics are engine's **own interface**, not products — kinds are
`action` (106), `screen` (73), `status_transition` (39), `field` (39), keyed to routes like `/admin/customers`.
**It is engine documenting itself. It is not a product knowledge base and must not be reported as one.**

**But the shape is `N3` exactly:**

| The record's `N3` column | The engine table that already holds it |
|---|---|
| The question (from `R3`) | `knowledge_questions.prompt`, with `status` and an approver |
| The answer | `knowledge_answers.free_text` / `selected_options` |
| Source / whose words | `knowledge_answers.user_id` + `role` |
| State — `answered` · `known` · `unanswered` | `knowledge_answers.state` |
| — | **`knowledge_gaps`**: a question asked that nothing answered, with `routed_to_question_id` — **`N9`'s mechanism, already running** |
| — | `knowledge_summaries`, generated from cited `source_answer_ids` |

**So the recommendation for step 3 is concrete: extend this to `subject_kind = product` rather than build a
knowledge store.** `N9` — *what we are asked and cannot answer* — is `knowledge_gaps` with a different subject, and
the routing from an unanswered question to a question needing an owner is already implemented.

---

## 3 · `REC-0` — the 15 audit questions, answered

*Prior beliefs from `backlog.md`. **Nine of fifteen priors were right; four understated engine; two were wrong.***

| Row | Answer | Verdict vs prior |
|---|---|---|
| **REC-1** objections + response | **Free-text only.** `sales_activities` (78) has `subject`/`body` with types call/email/meeting/note/task. No structured objection field | prior right — **gap** |
| **REC-2** win/loss with competitor + dimension | **Neither.** No loss reason at all: `won_at` only, `rejected` status unused, no competitor or dimension anywhere. **And no history to mine** (§0) | prior **understated the gap** — this was the open question and the answer is "less than assumed" |
| **REC-3** onboarding promises | **Partial and better than assumed.** `customers` carries `pricing_tier`, `terms_accepted_at`, `terms_doc_url`, `approval_notes`, approval/denial trail, `has_demo_facilities`, `marketing_opt_in_company`, tax registrations, resale certificate | prior right ("may be partial") — **thinner gap than feared** |
| **REC-4** install outcome | **No home.** `projects` has value/probability/close date, no outcome. Factory QC ≠ install snags | prior right — **gap** |
| **REC-5** post-delivery health | **Account status only** (`active`/`suspended`/`non_trading`/…) — a trading state, not a relationship state | prior right — **gap** |
| **REC-6** cross-sell attempts + response | **Orders only.** Coverage derivable; attempts and responses nowhere. The `G6` signal has no capture | prior right — **gap** |
| **REC-7** reorder cadence | **Derivable, not derived** — 77 orders over 11 weeks is too little history to establish cadence yet. `notifications` + `tasks` could carry the prompt | prior right, **plus a data-depth caveat** |
| **REC-8** failure root cause + fix | **Structure built, zero rows.** `rmas` (reason, inspection/resolution notes, 5 resolutions incl. `no_fault_found`), `support_tickets` (6 statuses, priorities, messages), `eco_requests` with 7 categories and severities — **all empty** | prior **wrong**: not a gap in the schema, a gap in *use* |
| **REC-9** field/market intelligence | **No home.** Correct that engine is not the place | prior right — **gap** |
| **REC-10** feature/gap requests | **`eco_requests` is exactly this** — categories include `improvement` and `documentation`, with severity, affected items, events, attachments and 5 resolutions. **0 rows** | prior **wrong** — built, unused |
| **REC-11** recognition triggers | **Computable, not computed.** Order history + `notifications` exist; nothing surfaces a threshold or anniversary | prior right |
| **REC-12** research register | **No home** — and correctly not a CRM concept | prior right — **gap** |
| **REC-13** standing competitor profile | **Nothing, at either level** — no per-deal fragments either (REC-2). The standing record stays `X1`–`X4` in the product record | prior right, **and the per-deal half is emptier than assumed** |
| **REC-14** discoverability performance | **Not in engine.** No analytics tables. Real home is site/store/GA/YouTube | prior right — confirmed outside |
| **REC-15** spend and rationale | **Not in engine.** `products.xero_account_code` shows finance is Xero. Rationale nowhere | prior right — confirmed outside |

**The shape of it, not the cells.** Three of the fifteen (**REC-8**, **REC-10**, and half of **REC-3**) are
**not build work at all — they are unused structure**, and the cheapest possible action is to start filing into
what exists. Nine are genuine gaps and all nine are conversational residue — objections, snags, attempts,
learning, intel — which is precisely what the six capture routes (`SYS-1`) are for. Two live outside engine and
should stop being tracked as engine work.

---

## 4 · What this changes in the plan

**Nothing in `group/` needs reopening.** Four amendments, all to plan and record files:

1. **`current-state.md`** — the "years of pipeline data" line needs the §0 correction. **Done** (this session).
2. **`NEXT.md` step 2** — done; and step 5 (`TSK-6`, build the four primitives) is **smaller for `detect` and
   `route`, unchanged for `record`'s knowledge half**, which is where it always mattered.
3. **`product-record-template.md`** — RT5's open question is answered (no competitor/dimension structure), and the
   claim that `X6` is *"largely a read from engine's pipeline"* should be struck. **Done** (this session).
4. **`backlog.md`** — `TSK-5`, `DOC-12`, `REC-0` close; `REC-8` and `REC-10` change from *build capture* to
   *use what exists*; `DOC-15`'s completeness gate has a host in `coverage_rule`. **Done** (this session).

**And the one thing to carry into step 3 unchanged:** the knowledge layer is confirmed homeless. Every field
`N1`–`N9` is `none`, in the system that holds everything else about these products. **The record is still the
cheapest, highest-leverage thing on the plan** — and it now has a specific system destination
(`knowledge_topics` extended to products) instead of "engine, somewhere."
