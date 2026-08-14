# Engine as the hub — the three questions, drafted for decision

**Status: DRAFT — proposals for decision, none of this is decided.** Every numbered choice below is Neil's to
make, confirm, reword or reject. Nothing here is a design; `open-items.md` § "the direction set 2026-08-14" is
explicit that the next session establishes decisions, not a build.

This file exists because that section names three things the next session should establish, in order: a KPI set,
a reconciliation map, and a consolidation shape. It answers those three, in that order, as proposals.

## Why the three are one question

*Quoting the argument already made in `open-items.md`, not re-deriving it:* **a KPI is only real if it has one
uncontested definition and a system that computes it** — and four dealer counts were found differing five-fold
(340 engine-approved, 266 Monday-approved, 104 ever purchased, 62 current). **Reconciliation is that same problem
priced** — 40 approved dealers cannot see a price, Monday's per-brand flags never reached Mailchimp, 6% of revenue
sits unclassified. **Both are symptoms of the sprawl**: every one of those failures happens at a boundary between
systems, not inside one. So a KPI, a reconciliation, and a consolidation decision are three views of the same
fact, and this file treats them as one piece of work rather than three.

---

## §1 — The KPI set: definitions first, dashboards never

No target numbers are proposed here — `CLAUDE.md` rules that out and the brief asks for definitions, not
dashboards. The account ladder (`archive-findings.md` findings 25–26) is the spine: **has an account 348 →
curated as an approved dealer 266 → ever purchased 104 → currently purchasing 62.** Each arrow is a sequential
milestone on one journey, not a competing definition of the same thing (Neil, 2026-08-14, correcting an earlier
reading in finding 26) — so the ladder should be reported whole, not as one headline number.

| Candidate KPI | Definition (proposed) | System of record | Computable today? |
|---|---|---|---|
| **Accounts created per period** | New engine `customers` rows per month/quarter — the gate itself: signed T&Cs, pricing unlocked. | Engine | **Yes.** Live; roughly 4–14/month back to at least March 2025 (`archive-findings.md` finding 26). |
| **First-order conversion** | Share of accounts created in a period that reach a first `sales_order` (any brand). | Engine | **Yes.** Both sides of the ratio are in engine now; no new capture. |
| Curated / approved status | Monday's `Approved Dealer` flag — a judgement layered over the account gate, not a gate itself. | Monday | Yes, but Monday is confirmed stale against engine for pipeline state (finding 26) — **[?] whether "approved" should keep being tracked in Monday at all once engine's own status ladder (`pending → approved → active → suspended → non_trading`) covers the same ground.** |
| Ever purchased / currently purchasing | Distinct accounts with ≥1 order, ever / in the current period. | Engine | Yes, from `sales_order` history — thin (11 weeks native), so cohort trend reads better than a point-in-time count until more history accrues. |
| **Active dealers per year** | Distinct dealers placing ≥1 order in a trailing 12 months, per own-made entity. | Engine (order history) | **Yes.** Has a measured baseline already: distribution ran 354 dealers (largest at 5.3% of revenue); DT ran 76 across ten years, only 10 non-Apex active by mid-2026 against 19–20 in 2022–24; SRND rebuilt to 147 in three years (`archive-findings.md` finding 16, `NEXT.md` §D). Proposed because it is the one metric a rising-revenue, falling-breadth year cannot flatter — DT 2026 is the case in point. |

**The contested definition, flagged per findings 25–26: what does "our dealer count" mean?** Four candidates
exist and they are five-fold apart. The finding's own conclusion — and this file's proposal — is that **"approved
dealer" (266) should never be reported alone as "our dealers"**; it overstates the trading relationship by roughly
4×. The two proposed headline figures are **accounts created** (the gate, unambiguous) and **active dealers per
year** (the trading reality). **This is Neil's to confirm** — the finding argues for it but does not settle group
policy on which number gets said out loud.

**One thing this table deliberately does not do: propose a dashboard, a cadence of reporting, or a target.**
Those are downstream of confirming the definitions above.

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
| **Engine's own age vs the business's age** | Engine's transaction history is eleven weeks, not years, so anything read "from engine's pipeline" (e.g. win/loss reasons, `X6`) is not actually available yet, even though the business has fourteen years of history sitting in Monday and the Xero archives. | No £ figure — a capability gap, not a revenue leak. | **[?]** — this narrows as engine accrues history regardless of consolidation; whether the historic Monday/Xero record should be backfilled into engine is part of the §3 sequencing fork below. |

**MON-13 sits outside the disappears/needs-fixing split by design, per the brief:** it is neither a leak that
consolidation would incidentally close nor a structural fix to schedule — it is **a fault to fix today**, because
forty partners cannot currently buy.

---

## §3 — The consolidation shape: what moves, what couples, what stays out

**The test already stated in `open-items.md`: does it ride on something already happening?** Applied here as a
proposal, not a decision.

| Candidate | Proposed treatment | Reasoning |
|---|---|---|
| **Mail (Mailchimp)** | Couples to engine. | The whole pull is one ~120-line script (`data/fetch_mailchimp.py`); the failure that matters (Monday's flags not reaching Mailchimp) is a plumbing gap, not a platform gap, and closing it rides on work already scheduled (`MON-15`). |
| **Reporting** | Couples to engine. | Same shape as mail — the reconciliation problems in §2 are boundary problems between systems that already exist; coupling reduces the boundaries without requiring the reporting layer itself to move. |
| **Websites** | A bigger question — not resolved here. | `decided.md` S29 put the canonical home for answers on each brand's own site, assuming the site was a separate system. If sites become engine-coupled, that assumption needs re-reading (see decision list below). |
| **Social** | Least certain of the three named. | No finding in this session measured social's boundaries the way mail and reporting were measured; flagged as open rather than assessed. **[?]** |
| **Shopify — catalogue, pricing tiers, product data** | Storefront half: cheap, and arguably already redundant. | This half already lives in engine (`engine-audit.md` §1); genuinely low-risk to take back. |
| **Shopify — checkout, payments, company accounts** | Checkout half: expensive, and the honest reservation stands. | Payments, PCI scope, multi-territory tax, fraud and B2B company accounts are the hard half, and the group uses the last of those: `customer_shopify_company_refs` holds **338 mappings**. The framing from `open-items.md` — "storefront cheap, checkout expensive" — should govern sequencing, not enthusiasm for the thesis. |

### The decisions only Neil can make

1. **The KPI definitions in §1** — specifically, whether "approved dealer" keeps being reported as a headline
   figure, and whether accounts-created and active-dealers-per-year become the two figures said out loud.
2. **Which boundaries in §2 get worked now versus wait on consolidation** — the brief's split (disappears under
   consolidation / needs fixing regardless) is proposed per row above; several rows are marked **[?]** where the
   session had no basis to classify them.
3. **The sequencing fork: does the product record (group 04, this repo's own step 3) get filled directly into
   engine's `knowledge_topics` → `knowledge_questions` → `knowledge_answers` → `knowledge_gaps` mechanism**
   (`engine-audit.md` §2 — confirmed to exist, currently pointed at engine's own UI, never at products) **rather
   than into files that later migrate?** This is a fork worth resolving before more of the record is written, not
   after.
4. **`decided.md` S29 — the canonical home for answers.** S29 settled that answers live on each brand's own site,
   assuming the site was separate from engine. If websites move to being engine-coupled (§3, still an open
   question itself), S29 needs re-reading. **Flagged, not resolved here** — it may not need reversing, but it was
   decided under an assumption that this direction changes.
5. **Social's treatment** — no basis in this session's findings to propose coupled, in, or out.
6. **The website question generally** — named as "a bigger question" in the direction section; this file does not
   attempt to answer it.

---

## The finding-30 warning

A platform programme is a building activity — the mode the group is already strongest in — and it must not
absorb the hours while **189 signed partners still receive no brand proposition and 40 still cannot see a price.**
The architecture proposed here is not in question; what must not happen is for it to become the ninth entry in
finding 30's table of things built and never said. Consolidation and the audience work draw on different hours
and different people, and neither should wait on the other.
