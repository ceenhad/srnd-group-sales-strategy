# Engine as the hub — the three questions, worked through

**Status: §1 is agreed — worked through with Neil question by question, 2026-08-14.** The KPI framework below is
his, arrived at in discussion, with the open decisions named where they sit. §2 (the reconciliation map) remains a
proposal row by row. §3 records the goal as Neil hardened it in the same session. Where the first draft of this
file was corrected, the correction is visible in place.

This file exists because `open-items.md` § "the direction set 2026-08-14" names three things to establish, in
order: a KPI set, a reconciliation map, and a consolidation shape.

## Why the three are one question

*Quoting the argument already made in `open-items.md`, not re-deriving it:* **a KPI is only real if it has one
uncontested definition and a system that computes it** — and four dealer counts were found differing five-fold
(340 engine-approved, 266 Monday-approved, 104 ever purchased, 62 current). **Reconciliation is that same problem
priced** — 40 approved dealers cannot see a price, Monday's per-brand flags never reached Mailchimp, 6% of revenue
sits unclassified. **Both are symptoms of the sprawl**: every one of those failures happens at a boundary between
systems, not inside one. So a KPI, a reconciliation, and a consolidation decision are three views of the same
fact, and this file treats them as one piece of work rather than three.

---

## §1 — The KPI framework (agreed 2026-08-14)

*An earlier draft of this section was headed ~~"definitions first, dashboards never"~~ — a misreading of
sequencing as doctrine, struck 2026-08-14. **The dashboard, in engine, is the destination.** The definitions
below are what gate it, so it is never built on contested numbers. And the frame matters more than any row: in an
organisation where **the content is the rep** (`group/08-sales-motion.md`), this framework is sales management —
reach, inbound-per-output and questions-retired are the rep's performance review.*

### The rule

**Nothing ships without a metric, a benchmark, and a place the number lands — and the place is engine.**
Everything output — websites, social, newsletters, campaigns, YouTube — is tracked and benchmarked. Three
corollaries:

- **Benchmarks are our own baselines, never industry figures.** The benchmark question is always: better than our
  last one?
- **Every link published anywhere carries a campaign tag.** Full attribution machinery is a trap at this size;
  tagged links plus per-stage conversion is the whole discipline, and it is a habit, not a build.
- **Each third-party replacement inherits the old system's baseline as its acceptance test.** When engine-owned
  mail replaces Mailchimp, the 63% open baseline is what proves the migration didn't cost deliverability.

### The funnel spine

**published → reached → inbound → account → first order → active → multi-line → loop**

**"Engaged" was deliberately reset to active inbound communication** (Neil). The ~2,000-contact mail list is warm
but passive — 29 campaigns produced 6 C-ATS clicks, and opens are inflated by mail privacy proxies — so passive
metrics are not a rung. Clicks, opens and tool sessions stay measured as **diagnostics** (they decide which
content formats earn their keep); they no longer count as funnel progress. The inbound rung is also where the
designed sales motion pivots — content does the reach and proof, and *very few people ask* — so the funnel is
measured at the joint the business actually turns on. Boundary calls, settled: **a completed design-tool
submission counts as inbound** (it is a project handed to us); **a booking counts when completed, not when
clicked.** Calls run over Zoom, so **calls are countable interactions too** — logs into engine, and transcripts
of owner answers feed the recurring-question list (`current-state.md`).

**Inbound is currently uncountable** — it lands in mailboxes, calls and heads. So this rung creates one capture
requirement in engine: an inbound log, one field on a screen people already use. The same log serves the
recurring-question list (the publishing schedule) and sits beside the three-line spec-conversation capture
(`adjacency-map.md`) — one mechanism, three of the plan's wants.

### The primitive: the account × brand signal matrix

**"Sales" is not revenue — revenue is the last signal in a ladder** (Neil). Per account × brand, the cell holds
the highest signal tier reached in the period, with revenue as the value attached:

**browsed → quoted → spec'd → ordered → repeat**

- The *spec'd* tier sits between quote and order: a quote is routine, being written into the project's spec is
  commitment. For specifier-type accounts, spec'd is the terminal success tier.
- **The store is fully gated, so every browse is a logged-in, identified account** — a dealer reading Fabric
  Walls pages who has only ever bought DT is a named cross-sell signal months before revenue could show it.
  Neil: knowing what people are looking at is *"100% a lost opportunity right now."* Owning the store is what
  makes this stream land in engine rather than in a third party's data model.

### Account types — because cross-sell is only expected where cross-sell applies

**A flat multi-brand metric fails** (Neil): the group wants accounts outside the cinema niche — a fit-out company
buying only Fabric Walls is a beyond-cinema win, not a cross-sell failure. So a **type field is set at account
approval** (a screen already in use), and every type has three parts: **a qualifying rule** (one sentence,
judgement-based), **an expectation profile** (which KPI views apply — breadth for whole-room, depth for
single-brand, influence for specifiers), and **a review trigger** (behaviour outside the profile flags a re-type
review for a human — never an auto-change). The type list, agreed: **whole-room integrator · single-brand trade ·
specifier/consultant · distributor · consumer.**

### The six questions and their KPIs

**Q1 — are we winning dealers?**
Reach per output (diagnostic, per format, own baselines) · **inbound contacts per period** (the new rung; needs
the inbound log; new-name inbound is funnel, existing-account inbound is a service/cross-sell signal) ·
**accounts created per period** (live in engine; 4–14/month baseline) · **first-order conversion and
time-to-first-order** (live; the 348 → 104 gap is the sales problem in one line).

**Q2 — are they buying across the group?**
Per-brand active accounts and revenue per period (the health line — also delivers active-dealers-per-year, the
metric a rising-revenue, falling-breadth year cannot flatter; DT 2026 is the case in point) · **white space on
signals, whole-room accounts only** — "quoted in brand A, browsing brand B" is a live moment, not a statistical
window · **depth for single-brand accounts** (repeat and growth within their brand) · Leyard-entry → own-made
conversion (the number that answers the open Leyard on-ramp question with data) · second-line interval as the
lagging gauge of the cross-sell motion (baseline: median 246 days, 74% later than first order). The headline
cross-brand count is **own-made brands only**; carried entry is tracked as the door it is.

**Q3 — are we keeping them?**
Detection is deliberately simple (Neil): **days since last interaction + interactions in a sliding window**, flat
tunable thresholds — no per-account behavioural modelling. Any signal counts as an interaction, which separates
*between projects* (revenue-quiet, signal-alive) from *going quiet* (no signal at all) for free. Plus: retention
rate (last year's actives active again) · reactivations against the 50-dealer/£2.33m list (`MON-6`) · top-5
concentration per brand (the Apex 31.5% lesson; distribution's 5.3% is what healthy looked like). *The quiet
list's owner rides on the open roles decision (`NEXT.md` step 1).*

**Q4 — is the pipeline healthy?**
Open value per brand (engine is pipeline truth; Monday is a stale snapshot) · **stalled = no status confirmation
past N days** — not deal age, because proposal-to-order can run past a year · win rate (~⅓ base rate) ·
time-to-close (median 153 days won; lost dies at 105) · pipeline by expected-land quarter · status-confirmation
coverage · poke response rate.

> **The one-tap deal-status email (Neil's design).** The mechanical status call — *rep calls dealer to ask what's
> happening* — spends relationship capital for nothing. Replace it: per open deal, a signed link, no login,
> airport-style one-tap options — *still live / on hold / expect to land [date] / not happening / **I need
> something from you*** (the last routes to a human, flipping extraction into service) — plus an optional free-text
> box. Self-reported land dates are dealer optimism, weighted by the ⅓ base rate. Discipline: one question, one
> tap, a cadence cap per deal, a named sender, honest copy ("one click saves us both a phone call"); two ignores →
> a human call, now justified spend. Non-response is itself signal. **This is the first use of engine-owned mail**
> — transactional, tiny volume, negligible deliverability risk: the cheap rehearsal before the newsletter
> migration. Open at build time: option wording, N, sender.

**Q5 — is the mix improving?**
Per-brand revenue and trend, **with carried revenue counted as a good number** — the strategy holds the carried
lines deliberately as revenue that funds the own lines, and Neil is plain: *"every Leyard sale is a good number…
the revenue matters greatly and leads to attachment sales."* So: **own-made share is watched, not maximised**
(34% in 2025; the right way for it to rise is attach and Pro-Fi shipping, never Leyard shrinking) · **own-made
attach rate on carried sales** — the bridge metric; every Komodo sale is a room being built, and the £472,320 /
£38,452 Komodo-to-Screen-Wall split says the door is currently walked through rarely. High proves the on-ramp
thesis; low names the accounts with an open door. Whether attach has historically followed is checkable in the
archive but needs the careful `MON-7` join — a dedicated pass, not a quick query · gross margin per brand
**later**, via the accounting ingest (accounting stays third-party by rule). **Staged payments are normal on
big-ticket carried lines** (the Komodo runs at 60% received, and that is the ordinary state of a live project —
`current-state.md`): no exposure or collections alarm belongs in this set; at most a payments-on-schedule flag
per project milestone, living in accounting.

**Q6 — is the motion running?**
Publications per period against **the floor** (the floor is undecided — see below) · sends per period and
brand-segmented share of sends (currently zero; the best send ever was the last one sent) · reach per output vs
own baseline (63% open; explainers ~9,500 views; mechanisms 600–1,500; catalogue 1–26) · clicks by destination
(store 946 · bookings 226 · c-ats.co.uk 6 · top single link a carried projector at 219, with no own-made
equivalent offered) · **inbound generated per output** (the motion's real conversion, attributed via tags) ·
**questions retired** (a published answer measurably stops arriving; the same question arriving twice after
publication is a findability problem, which is cheaper) · record coverage (% of live products with the record
filled — `product-register.md` counts the gaps) · and the stall signal, which needs no instrumentation: a month
with no publication.

### Open decisions in §1

1. **The floor rate, and who owns publication** — Neil and Olivier only (`open-items.md`). The lane does not
   start without them.
2. **Threshold values** — the quiet-detection window and N days for status confirmation: set as starting
   hypotheses, tuned against the first quarter's false positives.
3. **The poke email's wording, cadence cap and named sender** — settled at build time.
4. **Whether "approved dealer" (266) is ever reported as a headline count** — the ladder proposal stands
   (accounts created and active dealers are the two figures said out loud); Neil to confirm.

---

## §2 — The reconciliation map: every documented boundary, and what leaks at it

Built from the boundaries `archive-findings.md` and `backlog.md` document. Figures below are only ones that
appear in the findings — no new arithmetic.

| Boundary | What leaks | Measured price | Disappears under consolidation? |
|---|---|---|---|
| **Engine ↔ Monday — deal/pipeline state** | The two systems disagree on which deals are open; Monday is a snapshot of the migration moment, engine is live (finding 26). Engine holds 58 projects to Monday's 34 `In Engine` deals; several deals Monday shows open are won or lost in engine; values disagree (The Shard £1.0m vs £0.8m; Galileo £187k vs £93k). | Values named above; no single £ total given. | **Yes** — the boundary exists only because two systems both claim pipeline state. `MON-12`. |
| **Engine ↔ Monday — account population** | 40 of 265 Monday-approved dealers absent from engine entirely — no engine account, no pricing access. 80 engine accounts absent from Monday. | **40 dealers cannot see a price.** | **Needs fixing regardless** — flagged in `MON-13` as neither disappearing nor waiting: **a fault to fix today**, because forty partners cannot buy right now, independent of any future architecture. |
| **Monday ↔ Mailchimp — per-brand subscribe flags** | Monday holds real per-brand subscribe flags (DT 926, C-ATS 191, Fabric Walls 193, Light Walls 195, Pro-Fi 193 — finding 21); Mailchimp's brand tags carry **one member each**. The flags never reached the sending system (finding 28). Result: everyone gets the group newsletter, nobody gets a brand proposition. | 189 signed accounts never sold to; brand tags at n=1 each. | **Yes** — this is precisely the class of failure the direction argues consolidation removes: a flag set in one system with no route to the system that acts on it. `MON-15`. |
| **Xero exports ↔ classification — two report formats, half the detail each** | Sales Analysis (GTUK, DT) carries item code and quantity but no description; Account Transactions (C-ATS, SRND, Light Walls) carries description but no item code or quantity. Store items had to be keyword-classified (`data/classify_store_items.py`) rather than read directly. | **~£1.05m of £1.27m unclassified revenue** would resolve from re-exporting GTUK and DT in Account Transactions format (GTUK `OTHERS` £509,343; DT `Others` £234,135; DT store rows with no SKU £306,647). | **Needs fixing regardless** — this is a source-system export choice, not an integration boundary that consolidation removes. `MON-11`. |
| **Shopify ↔ the group's own sales analysis — nominal-account posting** | Shopify's store integration posts every order to a single nominal account, with no product category attached. Over half of SRND Group's revenue (**£1,385,960**) arrived this way and had to be reconstructed from item descriptions by keyword rule. | **£1,385,960**, over half of SRND Group's revenue (`open-items.md` § "the direction set 2026-08-14," citing finding 23's margin-ladder argument applied to Shopify). | **Yes, if Shopify's checkout is retired** — this is exactly the "storefront cheap, checkout expensive" case: the categorisation loss is a consequence of not owning the transaction record, which consolidation would fix; but it is coupled to the hardest half of the Shopify question (see §3). |
| **Shopify — the distribution 2024–25 gap** | Distribution sales after the swap into SRND sit between the GTUK archive (stops 2023-12-04) and engine (starts 2026-05-28), with no source obtained yet. | Not yet obtained — `MON-8`, still open. | **[?]** — cannot classify until the export lands and the gap is measured. |
| **Xero/GTUK/DT ↔ engine — dealer identity join** | Dealer identity is an unnormalised `Contact` string in the historic exports; any join to engine accounts is fuzzy, so every carry-over rate is a floor, not a real number (e.g. missed matches like "The Next Level" vs "TNL Systems Ltd T/a The Next Level"). | Finding 6's 26% carry-over rate is confirmed as a floor, not the true rate (`MON-7`). | **Needs fixing regardless** — a data-hygiene join problem inside the historic record, independent of where future systems live. |
| **Approved-dealer status ↔ what it is used to mean** | "Approved dealer" (266, Monday) is read informally as "our dealers," overstating the trading relationship roughly 4× against the 62 actually current (finding 25). | 266 vs 62 — a 4× overstatement if conflated. | **Partly disappears** — the ladder in §1 removes the ambiguity once adopted as reporting practice, independent of any system move; it is a definition fix, not a plumbing fix. |
| **▲ `cinema-tools.com` ↔ engine — the front door captures nothing** *(added 2026-08-15)* | The seven free calculators each produce an A4 PDF and have **no form and no email field**, so the PDF downloads unconditionally — against ADR 020, which specifies lead capture on PDF download landing in engine's `leads` table, and against `07-tools.md`'s *"on-ramp hinge in product form."* Both enquiry forms — `/project-support/` and `/introduction/` — are **`mailto:`**, so the best-qualified inbound the group generates arrives **in a mailbox**. | **No £ figure, and that is the point: the volume is unmeasurable because nothing is captured.** The leads are for the group's **highest-margin product** (finding 31, ≈100 %). | **Yes** — this is the archetype of the class. A lead-magnet whose leads never reach the system that would act on them, on the one page built to generate them. **And it is the concrete instance of §1's "inbound is currently uncountable."** |
| **Engine's own age vs the business's age** | Engine's transaction history is eleven weeks, not years, so anything read "from engine's pipeline" (e.g. win/loss reasons, `X6`) is not actually available yet, even though the business has fourteen years of history sitting in Monday and the Xero archives. | No £ figure — a capability gap, not a revenue leak. | **[?]** — this narrows as engine accrues history regardless of consolidation; whether the historic Monday/Xero record should be backfilled into engine is part of the §3 sequencing fork below. |

**MON-13 sits outside the disappears/needs-fixing split by design, per the brief:** it is neither a leak that
consolidation would incidentally close nor a structural fix to schedule — it is **a fault to fix today**, because
forty partners cannot currently buy.

---

## §3 — The consolidation shape (hardened 2026-08-14)

**The goal, as Neil set it in the KPI session, is harder than the first draft recorded: no third-party
applications in business operations.** Not "coupled" — replaced. No Mailchimp, no Monday, no heropost; Shopify
goes too, in favour of Cloudflare + Supabase. *"Every one of those softwares is a roadblock to efficiency and
management that costs far, far more than the cost of developing our own replacements."* Two exclusions, named:
**formal accounting software**, and **ambient tools like Google Analytics** that don't need replacing (Zoom sits
here too — a utility to ingest from, not a roadblock to replace).

Three distinctions that keep the goal crisp:

- **Operations software goes** — the tools that hold a step of the chain (mail sender, CRM, scheduler,
  storefront).
- **Audiences stay** — YouTube, the social platforms, trade press are channels, not tools; the scheduler that
  posts to them goes, the platform stays, and **engine ingests the platform-native metrics**, because "the place
  the number lands" holds even for surfaces we don't own.
- **Ambient measurement and accounting stay** — and feed engine by ingest (gross margin per brand arrives this
  way).

**Sequencing is unchanged by the harder goal** — it still follows *"does it ride on something already
happening?"* and *storefront cheap, checkout expensive* (payments, PCI scope, multi-territory tax, fraud, and the
338 `customer_shopify_company_refs` B2B mappings are the hard half). Two sequencing facts from the KPI session:
**each replacement inherits the old system's baseline as its acceptance test**, and **the first use of
engine-owned mail is the one-tap deal-status email** — transactional, tiny, low-risk: the rehearsal before the
newsletter migration carries the 63%-open baseline.

### The decisions only Neil can make

1. **The sequencing fork: does the product record (group 04, this repo's step 3) get filled directly into
   engine's `knowledge_topics` → `knowledge_questions` → `knowledge_answers` → `knowledge_gaps` mechanism**
   (`engine-audit.md` §2 — confirmed to exist) **rather than into files that later migrate?** Worth resolving
   before more of the record is written.
2. **`decided.md` S29 — the canonical home for answers.** S29 settled that answers live on each brand's own site,
   assuming the site was separate from engine. Under the replacement goal the sites become engine-coupled
   properties, so S29 needs re-reading. **Flagged, not resolved** — it may not need reversing, but it was decided
   under an assumption this direction changes.
3. **Which §2 boundaries get worked now versus wait on consolidation** — proposed per row above; the **[?]** rows
   had no basis to classify.
4. **The replacement order itself** — mail (poke first, newsletter second) and reporting look first; Monday's
   remaining content migrates as part of the historic-record question; storefront before checkout; social
   scheduling whenever convenient. A proposal, not a plan.

---

## The finding-30 warning

A platform programme is a building activity — the mode the group is already strongest in — and it must not
absorb the hours while **189 signed partners still receive no brand proposition and 40 still cannot see a price.**
The architecture is not in question; what must not happen is for it to become the ninth entry in finding 30's
table of things built and never said. Consolidation and the audience work draw on different hours and different
people, and neither should wait on the other.
