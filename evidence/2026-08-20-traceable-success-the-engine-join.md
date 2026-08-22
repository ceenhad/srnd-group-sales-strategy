# Traceable success: the journey, the activities, and where the join breaks

*Written 2026-08-20 in answer to Neil's three questions: **what does traceable success look like as we move each
brand through the buyer journey · how do these connect back to our activities and what exactly are those activities ·
how are we implementing those activities.*** **This closes `JNY-1`**, which asked for exactly this map and could not
be finished before because nobody had read what engine holds.

*Measured directly against engine, read-only, 2026-08-20. **Nothing is proposed into engine here.***

---

## 1. Traceable success, gateway by gateway — and the funnel counts for the first time

*The gateways are `motion/motion-design.md`'s, unchanged. The unit is `group-strategy/buyer-journey.md`'s: **the
dealer relationship, across the group, over time** — which is why the dealer number is a group measure and the brand
split sits underneath it.*

| Gateway | What success is | Where it lives in engine | Countable today | The number now |
|---|---|---|---|---|
| **G1** (1→2) | A stranger with a problem found us | **Nowhere.** *Engine cannot see a visit; it sees only what becomes a lead. `leads.source_brand_site` and `customers.source_brand_website` record **which brand's site**, never how many looked* | No | — |
| **G2** (2→3) | The proposition landed — worth their time | `leads` (`enquiry_type`, `product_id`, `source_brand_site`); `knowledge_topics` **257** with questions, answers and gaps | Partly | 4 leads in total |
| **G3** (3→4) | Registered, **with marketing permission given willingly** | `customers.approved_at` · `terms_accepted_at` · **`marketing_opt_in_company`** | Yes | **17** approved · **13** terms accepted · **6** with marketing permission — *and on the gateway's own wording, **G3 is 6*** |
| **G4** (4→5) | First order placed | `sales_orders.ordered_at` | Yes | 35 customers have ordered |
| **G5** (5→6) | The first job succeeded | **`support_tickets` exists** — with statuses and priorities defined and **0 rows**. `projects.status_id` carries `won`/`lost`, which is a *project* outcome, not an install one | **No — still needs defining**, exactly as `motion-design.md` said | — |
| **G6** (6→loop) | A second brand followed | `sales_order_lines` → `products.brand_id`, per customer — `FACT-1`'s query | Yes | 2 customers have ordered across more than one brand |

**So the funnel, as far as it is instrumented: 6 → 35 → 2.** *Read it as a first reading of a young system, **not as
performance** — engine's order history is weeks old, not years (`engine-audit.md` §0).*

**And the shape is the finding: the back half of the journey is instrumented and the front half is not.**
*Everything from registration onward is countable today. **Everything that generates the interest is invisible.***
*For a business whose plan is content-as-rep, that is precisely the wrong way round — **the activities we are
investing in are the ones we cannot measure**.*

## 2. The chain exists end to end — and it is broken at three joins

**Engine already models the whole path from an activity to a room to an order to a brand.** *This was not known here
before today, and it is better than the repo assumed:*

```
leads (lead_source_id, source, source_brand_site, enquiry_type, product_id)
  → projects (source_lead_id, brand_id, expected_value, probability, status: potential/active/won/lost)
    → quotes (project_id, project_stage_id, won_at)
      → sales_orders (project_id, ordered_at)
        → sales_order_lines → products.brand_id
```

| Join | State | |
|---|---|---|
| `quotes.project_id` | 10 of 13 | ✅ *working* |
| `products.brand_id` | 163 of 166 | ✅ *working* |
| `customers.source_brand_website` | 329 of 350 | ✅ *populated and unread* |
| `projects.source_lead_id` | 0 of 50 | ❌ **the link from an activity to a room** |
| `projects.brand_id` | 0 of 50 | ❌ **the link from a room to a brand** |
| `sales_orders.project_id` | 1 of 74 | ❌ **the link from a room to the money** |
| `customers.customer_type_id` | 17 of 350 | ❌ *the dealer/distributor split — `ENG-20`* |

**None of these is a build. All four are fields that exist and are not being filled.** *Which is the same finding as
`ENG-20`, one layer wider: **engine's capture is ahead of engine's use.***

## 3. How activities connect back — and this is the real gap

**The activities are already defined**, in `motion/content.md` § The map: **fourteen content types placed against the
six stages**, plus the two owned assets — *the studio* and *the Experience Centre, virtualised*. **The list is not
missing.** *What is missing is a way to tell one of them from another once a lead arrives.*

**`lead_sources` holds five codes: `website` · `referral` · `trade_show` · `manual` · `import`.**

**That is the entire activity vocabulary, and it cannot answer `JNY-1`'s own question — *which hook caught which
dealer*.** *A CPD seminar, an AI answer, a press piece, a podcast episode, a virtual case study and a data card all
arrive as **`website`**. There is **no campaign, UTM, attribution or channel table anywhere in engine** — checked.*

**Mapped against the fourteen activities, the honest position:**

| The activity | Stage | Traceable today? |
|---|---|---|
| Off-site hooks — social, trade press, events, search/AI · always-on presence (podcast, YouTube) | 1 | **No.** *Invisible until a lead exists, and then indistinguishable* |
| Group-site intro and campaign landing pages | 1 | No |
| Brand-site range, data cards, virtual case studies, knowledge base, recorded demos | 2–3 | **Brand only** — `source_brand_site` says which site, never which piece |
| Sample kit | 3 | **Possible now** — `leads.enquiry_type` could carry it |
| Registration and partner pricing | 4 | **Yes** — G3 |
| Purchase | 4 | **Yes** — G4 |
| Install, verification, support | 5 | **No** — `support_tickets` empty, no verification event |
| Reorder and cross-brand prompts | 6 | **Yes** — G6 |
| Evergreen collateral (brochure) | ongoing | No |

**One field closes most of this: a specific source carried from the piece into the lead.** *`lead_sources.meta` is
already a `jsonb` column, so **a campaign or piece identifier has somewhere to go without a schema change** — but
nothing writes one, and the five parent codes would still need a child. **That is the decision, and it is small.***

## 4. How they are implemented — and the honest gap

**The implementing machinery is real and documented:** *`motion/sales-motion.md` (the operating loop, what stays
human), `motion/content.md` (the standard, the map, the campaign template), `motion/work-items.md` and
`task-shapes.md` (the work as `detect` / `record` / `route` / `assemble` shapes), and engine hosts an agent layer with
budgets and an audit trail (`engine-audit.md` §2).*

**What is not implemented is the one step that would make any of it measurable: nothing emits a traceable source.**
*A content piece is published, a seminar is delivered, an answer is written — and **no identifier travels with it into
the lead that follows.*** **So the operating loop can produce work and cannot yet learn from it**, which is the
difference between an activity list and a plan.

---

## What this says to do, in order

1. **`ENG-20`** — populate `customer_type_id`. *Without it, dealer and distribution cannot be separated at all.*
2. **`JNY-10`** — decide the source vocabulary: **what identifies a piece, and where it is carried.** *`lead_sources.meta`
   already accepts it. **This is the whole of "which hook caught which dealer."***
3. **`JNY-11`** — fill the three project joins going forward: `source_lead_id`, `brand_id`, `sales_orders.project_id`.
   *A room becomes the traceable unit the moment these are populated — and **the room is the unit the business
   actually works in**.*
4. **`JNY-6`** — define `G5`. *`support_tickets` exists and is empty; the absence of a ticket is a signal only once
   tickets are being raised.*
5. **Then, and only then, the target.** *Two numbers against a working instrument: a **group** number on dealer
   relationships and a **brand** number on distribution — `ENG-21`.*

**What not to do:** *design a new tracker. **Engine already models the chain**; four fields are unpopulated and one
vocabulary is too coarse. That is the whole gap.*
