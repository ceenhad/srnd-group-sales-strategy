# What happens next

*Rev 3, 2026-08-17. The strategy lives in `group-strategy/strategy.md`; this file holds only the current
position and what's next. The order is Neil's: lock the group level, drive down through the brands, then
generate and track.*

**Where we are:** the top-level strategy is drafted and landed; corrections fold in as Neil makes them.
Nothing is generating yet and engagement is at an all-time low — that is the problem the whole system
exists to fix. **The C-ATS template run is drafted (2026-08-18)** — three pathways, the hook set, the segment cut,
and the inherited shape written up in `brands/_template/the-brand-run.md`. It is drafted for correction, not
adopted.

**Next, in order:**

1. **Settle the strategy** — Neil's corrections into `strategy.md` until it says what he means.
2. **The template brand run: C-ATS.** Pathways built stage by stage from its material, hooks from its
 products, segments cut from the database. This run defines the shape every brand inherits — and because
 C-ATS is the most basic brand, the run proves the machine, not the money: the template is validated
 against one unlike brand before the shape is called settled.
 **Drafted 2026-08-18** (`brands/c-ats/`: three pathways, `hooks.md`, `segments.md`;
 `brands/_template/the-brand-run.md`). **Two framings were put to Neil and both were rejected** — the
 entry-product/flagship split (Q50: C-ATS is a system, the 3 Rs defines it, no panel leads) and using the
 segment cut as a league table (Q51: every relationship is treated as day 1). Both are corrected in place and
 folded into the template, so no other brand inherits them. **The drill-down is the live thread** — §1–§5 of
 `positioning.md` are atomised into `brands/c-ats/claims.md`, §6–§7 remain, and it has broken or qualified more
 than the building did. **What it still leaves for Neil:** the hook
 wording, which is an owner's, and whether the shape is right before another brand copies it. **What it leaves
 as work:** the run ends as a queue of register items rather than as a document — CON-8 and EST-5 first, then
 DOC-1 to DOC-4 and EST-4. **— struck 2026-08-18 on Neil's correction: both exist in Cinema Tools.** What
 replaces it is **Q52**, the publication boundary between the design rules and the engine, which gates the
 C-ATS self-serve route and six of the strongest hook candidates found in the run.
3. **The launch brands get the same treatment** — Pro-Fi and Light Walls launch *into* the system, not
 beside it.
4. **Switch on generation and tracking** — the production line running, the daily drumbeat per live brand,
 the inbound counted in engine, the funnel numbers arriving weekly. Operational readiness items (dealer
 accounts, list segmentation, tool capture) done as the running machine needs them.

---

## Session state — 2026-08-20, resume here

*Written so a session in a different account can pick up cold. Everything points at a register; nothing is restated.*

### Resume here, in this order

1. **`ENG-20`** — populate `customers.customer_type_id`. 333 of 350 live customers are untyped, and until that field
 is filled dealer sales and distribution sales cannot be separated at all.
2. **`ENG-24`** — the app should fill three columns that already exist: `projects.source_lead_id` (0/50),
 `projects.brand_id` (0/50), `sales_orders.project_id` (1/74). `quotes.project_id` is 10/13, so quotes link to
 projects and orders do not.
3. **`JNY-10` / `ENG-23`** — spec the marketing-activity dimension. `lead_sources` has five codes, so a CPD seminar,
 an AI answer, a press piece and a hook all arrive as "website". Design it here and hand it over; we do not write to
 engine (Neil, 2026-08-20).
4. **`ENG-21` / `ENG-22`** — then the two target reports and the interest measure, which need the data above.

The target is settled in structure, not in number: a **group** target on dealer sales, a **brand** target on
distribution sales, never netted together, counted at `ordered_at` rather than at the invoice. A dealer is one
relationship across every brand; a distributor is appointed brand by brand.

### Waiting on Neil

**23 questions, typed `Ask` in `registers/backlog.md`** with a weight and a scope. Every one is money, a commitment,
or what we sell. The heaviest: `KNW-4` (commission the remaining tests or declare the data the limit) · `XS-5` (price
the service offer) · `CON-10` (spend the £10k AVForums credit) · `US-2`/`US-3` (US terms, and who moves it) ·
`PAR-2`–`PAR-5` (the partner programme's four) · `DEC-3`/`DEC-4`/`DEC-5` · `FACT-5` (the targets table) · `EDU-1`
(re-enter education).

**Four C-ATS drafts await a truth-check** — `draft-t2-decide-before-the-wall.md`,
`draft-t5-layout-tolerance.md`, `draft-answers.md`, `draft-n7-client-leave-behind.md`. Read `draft-answers.md`
against the published knowledge base first: it re-derived answers that were already live.

**One rule violation to fix: `SIT-9`.** A published article files the Reflection Control Panel under a "Diffusers"
heading, and `C5.15` forbids the word on the product.

### What changed today, and what it means for how you work

Six rules are new, in `CLAUDE.md` and `method.md`:

- **Fix the text; do not annotate it.** Corrections delete the wrong version — 403 strikethrough markers were swept.
- **A thing is decided only when it went through the question box and a human answered it.**
 `registers/questions.md` is the record; `decided.md` is the SRND OS feed and takes business decisions only.
- **A question earns the box only if the answer is a decision the business acts on.** Of 61 answered questions, 22
 were pure repo housekeeping.
- **No `Decide` type.** `Do`/`Fetch` is work, `Ask` is a question not yet put to Neil, `Flag` is another repo's.
- **Weight and scope on every live row** — `strategy` · `capability` · `clarification`, and `group` · a brand ·
 `platform`.
- **Run `python3 tools/check.py` before committing.** It found three defects on its first run, including five
 premise rows that had been invisible for days.

### Warnings that still apply

- **Name the artefact before measuring it.** C-ATS has four web presences — the live site, the Shopify mockup, an
 Astro build of unknown provenance, and `copy.md`. Confusing them cost most of a session.
- **Do not audit a mockup against the guardrails.** The findings dissolve when someone says what it is.
- **Check the published site before recording anything as unpublished.** One fetch; `PR-24` records the cost.
- **A blanket find-and-replace across many references produces text that is well-formed and false.** It rewrote
 `method.md`'s statement of what SRND OS reads.
- **Do not do regex surgery on markdown emphasis.** Three attempts, three lots of damage: joined table rows, eaten
 leading characters, broken pairing. Reducing emphasis is a rewrite, not a substitution.

### Where the C-ATS work stands

**`brands/c-ats/phase-closure.md` is the answer to "what finishes this phase"** — tested against the run's own
definition in `../_template/the-brand-run.md`, not against a new list. The run is structurally complete on all five
deliverables; four things close the phase: the four drafts' truth-check (read `draft-answers.md` against the
published knowledge base first), `SIT-9`, three fetches (`DAT-3`/`DOC-7`, `DOC-8`, `DOC-17`), and two brand-scoped
decisions (`KNW-4`, `KNW-7`). Explicitly not in this phase: isolation (`P2`), standard rooms (`EST-20`), `DR-Q52`'s
formal closure, and the prose-to-rows rewrite.

**The engine thread did not drop** — `operations/engine-measurement-spec.md` holds six deltas `D1`–`D6` between the
KPI framework agreed 2026-08-14 and what engine measurably holds, written as a dev-team specification because we do
not write to engine from here.

**Access boundary, tested three ways on 2026-08-21 — do not retry.** `SRND-Group/srnd-engine` and `srnd-os` cannot
be read from a session on this repo: `add_repo` refuses cross-owner, `git clone` has no credentials, and the GitHub
API names the allowlist as `ceenhad/srnd-group-sales-strategy` and `ceenhad/cinema-platform` only. Not a rights
problem — the account has push on both. **Engine application work, and any answer to `Q40`, needs a session opened on
those repos; what comes back here is a spec.** Detail in `brands/c-ats/phase-closure.md`.

The drill-down is done end to end — `positioning.md` §1–§7 atomised into **76 claim rows** in
`brands/c-ats/claims.md`, and `Q63`–`Q81` are answered and applied.

**`DR-Q52` has been answered by publication**, not by decision: five items from its own proposed-publishable column
are live on the C-ATS site and nothing from the proposed-not column is. So `T4` can probably be un-gated and the
request closed — Neil's call.

**`brands/c-ats/planning-gaps.md` holds `P1`–`P7`.** `P1` (the target) is the engine work above. `P7` (verification)
is withdrawn — it is a listed service. `P2` stands: isolation is a sold layer with one clause of plan behind it, and
per `C1.40` it is the layer that reaches a project first.

**Known debt:** the three `pathway-*.md` files, `hooks.md` and `segments.md` are prose-with-tables and owe a rewrite
into rows (`PR-9`). Emphasis density is over the warning threshold in most brand and evidence files — a rewrite job,
not a substitution.

### Read first

`method.md` (§ The drill-down · § What the work produces · § Not getting into this mess again) · `CLAUDE.md` ·
`registers/premises.md` — 24 premises, and the broken ones say what this repo assumes wrongly by default.

---

**The standing rule:** execution doesn't jump the queue, and nothing is announced before it's real.
