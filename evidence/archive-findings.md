# What the archive says — measured findings

*The counted output of `registers/backlog.md` `MON-1`/`MON-2`/`MON-3`. **Evidence, not argument** — this file holds what the
historical data actually shows, tranche by tranche, and nothing else. It accumulates; each tranche is appended with
its own scope and caveats. **Internal. Dealer names are not for publication** in any form.*

---

## The source register — read this before hunting for anything

**The point of this section is that nobody goes looking twice.** Every dataset behind the findings below, where it
lives, what it covers, and what it cannot answer.

| # | Source | Where it lives | Covers | Period |
|---|---|---|---|---|
| 1 | **GTUK / Apex Tech Scotland sales analysis** | Dropbox — `/GTUK Staff/Sales/Reports/GTUK - Sales Analysis Report - All.xlsx` · file id `id:F15NlnKOA1AAAAAAAAAo8w` | SRND Distribution's forerunner. **UK dealers only** | 2012-01-11 → 2023-12-04 |
| 2 | **DT sales analysis** | Dropbox — `/DT Management/Sales/DT - Sales Analysis Report - All.xlsx` · file id `id:F15NlnKOA1AAAAAAAAAo-Q` | Display Technologies, incl. international dealers and intra-group | 2016-07-12 → 2026-08-12 |
| 2b | **C-ATS account transactions** — *different report type, see below* | `data/source/C-ATS - Account Transactions.xlsx` (supplied locally, 2026-08-13) | Cinema Acoustic Treatment Systems Limited, incl. intra-group | stated 2016-01-01 → 2026-08-31 |
| 2c | **SRND Group account transactions** | `data/source/SRND Group - Account Transactions.xlsx` (supplied locally, 2026-08-13) | SRND Group Ltd — **the current trading entity, from when it took over from the Apex businesses.** Hybrid distributor/manufacturer selling to distributors and dealers globally (Neil) | stated 2020-01-01 → 2026-08-31; data 2023 → 2026 |
| 2d | **Light Walls account transactions** | `data/source/Light Walls - Account Transactions.xlsx` (supplied locally, 2026-08-13) | Light Walls Ltd, incl. intra-group | stated 2016-08-01 → 2026-08-31; data 2020 → 2026 |
| 3 | **Engine** *(live, not an extract)* | Supabase project **`vzgdhfsmxteoxxsuexyg`** (`SRND Engine`, eu-west-2). Testbed is `bpsaxuwitlycubnvmfrr`. Read-only MCP is pinned to the production ref | Current accounts, quotes, orders, products, documents | Accounts migrated; transactions from **2026-05-28** |
| — | **Pro-Fi** | **No source, because there are no sales** (Neil, 2026-08-13). Nothing to obtain | — | — |
| 4 | **Shopify — distribution after the swap into SRND** | **Not yet obtained** — `registers/backlog.md` `MON-8` | The distribution 2024–25 gap between sources 1 and 3 | ~2024 → 2026 |
| 5 | **Monday.com CRM — four board exports** ✔ | `data/source/Monday - {SRND Deals, SRND Accounts, Leads, SRND Contacts}.xlsx` (supplied 2026-08-13) | **Deals 155** + 226 sub-deals, **Accounts 1,658** with per-brand status, **Leads 1,233**, **Contacts 1,371**. See tranche 4 | **Deals 2025 → 2026 only** — eighteen months, not years |
| 6 | **Mailchimp** ✔ *(API, not an export)* | `data/source/mailchimp-{lists,members-a9c4508863,campaigns}.json`, pulled by `data/fetch_mailchimp.py`. **Key read from the `MAILCHIMP_API_KEY` environment variable — never in the repo, a file, or an argument** | **One audience, ~2,028 subscribed** (2,845 records); **29 campaigns**; **416 click-detail URL records** | list built 2025; sends 2025-06-30 → 2026-04-16 |
| 7 | **Sent-mail archive** | Not yet worked — `registers/backlog.md` `CON-3` | Which questions recur, for `R3`/`N3` ranking | Years |

> **▶ One consolidated table now sits above all of it — `data/derived/all-transactions.csv`** (2026-08-13).
> **10,360 rows, five entities, fifteen years, one harmonised category vocabulary**, reconciled to the pound against
> every per-entity file. **Use it for any group-level question**; the per-entity extracts remain for single-company
> work. It is built by `data/consolidate.py`, which maps GTUK's third-party *brand* lines and DT's store SKUs onto
> the same categories the other sources use, and adds `supply` (own-made / carried / services) and `carried_brand`.
> **6.0 % of product revenue stays `Unclassified` by design** — six lines that cannot be read from an account name
> are listed in `data/derived/consolidation-review.csv` instead of guessed at. See `data/README.md`.
>
> **▶ The data itself is stored in the repo, not just pointed at — `data/`** (2026-08-13, at Neil's
> instruction). Sources 1 and 2 are held verbatim in `data/source/`, **verified byte-identical to Dropbox**, with
> lossless analysis-ready extracts in `data/derived/` and the column contract in `data/README.md`. **A moved,
> renamed or deleted Dropbox file can no longer cost us the history.** When the outstanding sources arrive they land
> the same way: received file, lossless extract, a row in this register.

**Prefer the Dropbox path and file id over a share link.** Both files arrived as `dropbox.com/scl/...?rlkey=...`
links; those carry an access token, expire, and are revocable, so they are **deliberately not recorded here.** The
file id is stable across renames and moves and resolves directly through the Dropbox tooling.

**A note on what these files are.** Sources 1 and 2 are the same Xero-derived **Sales Analysis Report** run for two
entities: one row per invoice line, twelve columns, with a `Raw Data` sheet plus pivot sheets. **The `Raw Data` sheet
always reaches further back than the pivots** — GTUK's pivots start at 2019 while its raw data starts at 2012 — so
**work from `Raw Data`, never from the pivots.**

**Source 2b is a different Xero report — Account Transactions — and needs different handling.** Three differences
that will silently produce wrong numbers if missed:

1. **The contact is a group header row, not a column.** Transactions sit under a bare row naming the contact, closed
 by a `Total <contact>` row. Parsing row-wise without tracking the current group loses the dealer entirely.
2. **Amounts are `Debit (GBP)` / `Credit (GBP)`, not `Net`.** Revenue is a **credit**; reversals, write-offs and
 credit notes are debits. **Net = credit − debit.**
3. **No item code or quantity**, and the `Reference` column carries the invoice number — sometimes a real one
 (`INV-0013`), sometimes free text (`Stock Catchup`, `Jay Demo Pack`). Treat it as a label, not a key.

Both report types are normalised to the same column contract in `data/derived/` — see `data/README.md`.

### Pro-Fi — no sales, and no source

**Pro-Fi has no sales and therefore no report to load** (Neil, 2026-08-13). What appears across the four sources is
**£13,156 of Pro-Fi-branded product invoiced through SRND Group**, five lines in 2025, and **neither part of it is
ordinary revenue:**

| Date | Dealer | Lines | Net | What it is |
|---|---|---|---|---|
| 2025-04-29 | De Opera Domotica | Dot 1, Dash 2, Boxer 1 surface-mount | **£8,128** | **A very early prototype system** (Neil) — not a product sale |
| 2025-11-11 | Cornflake | `PF-A-16-700D`, `PF-A-4-350D` amplifiers | £5,029 | Amplifiers |

**So the brand is pre-revenue**, which matches engine: Pro-Fi has a brand, a store and a `profi_speaker_datasheet`
template, but **`product_speaker_technical` holds zero rows** (`evidence/engine-audit.md` §1). Two consequences for anyone
using this data: **do not read £13,156 as a product-revenue baseline** — most of it is one prototype — and any
per-brand analysis of Pro-Fi will be noise at this scale.

*Search caution for anyone repeating this:* a regex of `pro-?fi` also matches "**profi**le", so LED-profile lines
count as Pro-Fi and inflate the total roughly threefold. Use `pro-fi|\bprofi\b|\bpf-a-`.

### Method, so the numbers reproduce

Anyone re-running these needs the same five decisions, or the figures will not match:

1. **Measure is the `Net` column.** Not `Unit Price (ex)`, which appears to hold list prices and is inconsistent with
 the rest of the row. Credit notes carry negative `Net` and are **left in** so they net off.
2. **Exclude non-revenue accounts:** postage, freight, shipping, warehousing, payroll, VAT, accounts receivable,
 cost-of-sales, motor vehicle, advertising, inter-company postings, and `Other Revenue`.
3. **Exclude `Deleted` and `Draft` status**; keep `Paid` and `Approved`.
4. **Separate intra-group counterparties before counting dealers.** For DT these are **Apex Tech Scotland Ltd**,
 **SRND Group Ltd**, **Apex Tech International Ltd**, Dzyn Ltd and Display Technologies Ltd. Missing this
 overstates the external dealer base and understates concentration.
5. **Canonicalise `Apex Technologies USA` and `Apex Technologies USA LLC` to one account** — same counterparty,
 re-registered April 2024 (Neil, 2026-08-13).

**Dealer identity is an unnormalised `Contact` string** in both files, so any join against engine is fuzzy and every
carry-over rate is a **floor** (`MON-7`).

---

## Tranche 1 — GTUK sales analysis, 2012–2023

**Source.** `GTUK - Sales Analysis Report - All.xlsx` (Neil, 2026-08-13), a Xero-derived invoice-line export:
**4,992 raw lines, 2012-01-11 to 2023-12-04**. The workbook's own pivot sheets only cover 2019–2023 — **the raw
sheet goes back seven years further than the analysis anyone had built on it.**

**Whose history this is — and it is not a third party's.** The trading entity is **Apex Tech Scotland Ltd**
(Neil, 2026-08-13), the company behind the lineage the repo already resolved: **GT → Apex-Tech UK (rebranded
July 2021) → SRND Distribution** (`group-strategy/commercial-model.md`; `evidence/2023-buyer-journey-archive.md`).
**So this is one of the six brands' own twelve-year trading record**, not an analogue borrowed from elsewhere —
and it is *distinct from the US Apex-Tech* recorded in `evidence/current-state.md` as the resigned DT distributor. Two
things follow:

- **It puts numbers on a claim the repo makes in prose.** *"Twenty years spent distributing other companies'
 brands"* and *"we have been doing this a long time"* now read as **£11.7m across 367 dealers and 55 lines**.
 The moat's first half — understanding the dealer's job — has a measured provenance.
- **The dealer base is the group's own inheritance**, which makes it joinable to engine's current accounts. That
 join is findings 6 and 7, and it is where the commercial value of this tranche actually sits.

**Method.** 4,909 usable lines after excluding `Deleted`/`Draft` status and non-revenue accounts (postage, freight,
travel, bank fees, cost-of-sales, accounts receivable). Measure is the **`Net`** column; credit notes carry negative
values and are left in so they net off. 619 lines carry no account code — kept in revenue totals, excluded from
per-line breadth counts. **Dealer identity is the `Contact` field**, unnormalised, so a company appearing under two
spellings counts twice; the effect on the aggregates below is small but non-zero.

**Scale.** **£11,745,315 net over twelve years** (£11,742,315 external), across **367 customers** (354 external with positive net) and **55 revenue
lines**.

| Year | Net | | Year | Net |
|---|---|---|---|---|
| 2012 | £1,369,480 | | 2018 | £740,106 |
| 2013 | £1,101,397 | | 2019 | £1,019,659 |
| 2014 | £1,044,627 | | 2020 | £876,115 |
| 2015 | £506,174 | | 2021 | **£1,884,000** |
| 2016 | £515,402 | | 2022 | £1,245,364 |
| 2017 | £559,460 | | 2023 | £883,531 |

**Scope: UK dealers only** (Neil, 2026-08-13). The international network — 21 appointments across 20-odd
territories (`evidence/current-state.md`) — is **not** in this file. Three consequences: the **£11.75m is a UK figure**, not
the group's historic total; every behavioural finding below is **UK dealer behaviour** and should not be
generalised to the territories without testing; and it sharpens finding 6 rather than weakening it — the 262
unmatched dealers are **UK** accounts absent from engine, so the gap cannot be explained away as international
accounts sitting outside the comparison.

**A second caveat that governs every reading below.** Most of those 55 lines are third-party brands the business
carried; only two are ancestors of the group's own-made brands — **DT SCREENS** (£1,165,218 across 85 dealers) and
**CATS** (£141,844 across 23). **So this is SRND Distribution's own history in full, and a cross-*line* measurement
within it — not cross-*brand* behaviour across the six own brands.** Same dealer base, same room, same buying
moment, and now known to be the same company, so the direction is solid evidence; the magnitudes stay indicative
for the six-brand question until engine's own history is long enough to answer it directly.

### Finding 1 — concentration, which closes a standing `[?]`

`evidence/current-state.md` asked *"what share the top five accounts represent."* Over the twelve years:

| | Share of net |
|---|---|
| Top 5 customers | **22.3 %** |
| Top 10 | 36.2 % |
| Top 20 | **49.8 %** |
| Top 50 | 71.0 % |

**Half the revenue sits in twenty accounts, and the tail is long and real** — 354 paying external dealers, of whom about 200
bought a single line. Note the top account here reached **£623,422 over nine years**; that is *not* the
"£500,000 in a year" dealer in `evidence/current-state.md`, which is a current SRND account. **Different eras, different
businesses — do not conflate the two figures.**

### Finding 2 — breadth tracks value, strongly and monotonically

| Lines bought | Dealers | Median lifetime | Mean lifetime |
|---|---|---|---|
| 1 | 199 | £3,000 | £7,249 |
| 2–3 | 86 | £16,788 | £24,590 |
| 4–6 | 46 | £44,328 | £77,850 |
| 7+ | 24 | **£109,781** | £191,959 |

**The 44 % of dealers who bought more than one line produced 87.7 % of all revenue** (£10,302,847 of £11,745,315).
Single-line dealers — 56 % of the base — produced 12.3 %.

**Read this cautiously.** Breadth and value are *mechanically* correlated: a dealer who spends more has more chances
to touch another line. **This table on its own does not prove cross-sell causes value.** Finding 3 is the test that
does not have that confound.

### Finding 3 — first-order size carries no signal, and this is the important one

**The `group-strategy/the-group-play.md` claim under test:** *"There is no long tail to service cheaply. A small order in one
brand isn't a low-value account; it's the opening of a group relationship. We don't triage dealers by any single
brand's order size."*

Banding every dealer by the value of their **first invoice**, then measuring only what came **after** it:

| First order | Dealers | Reordered | Median later revenue | **Mean later revenue** | New lines added later |
|---|---|---|---|---|---|
| < £1k | 91 | 52 % | £0 | £12,477 | 0.8 |
| **£1–5k** | **161** | 62 % | £2,235 | **£37,143** | **1.7** |
| £5–20k | 77 | 51 % | £0 | £13,011 | 0.6 |
| £20–50k | 20 | 70 % | £3,131 | £30,915 | 0.9 |
| £50k+ | 5 | 80 % | £12,200 | £27,618 | 1.4 |

**The £1–5k cohort went on to earn more than the £50k+ cohort — £37,143 against £27,618 in mean later revenue.**
The relationship between first-order size and everything that follows is not weak; it is absent.

Three numbers make it concrete:

- **252 of 354 dealers — 71 % — started with a first order under £5,000.**
- **40 of those (16 %) went on to exceed £50,000 lifetime.**
- **They generated £7,115,374 after that first order — 61 % of all revenue in the file.**
- **The single largest account in twelve years began with a first order under £5,000.**

**Verdict: the premise is confirmed, and the honest form of it is a prohibition rather than a promise.** Roughly
half of small first orders never reorder at all — so the finding is *not* "small orders grow." It is
**"nothing in a first order tells you which half you are looking at,"** which is a stronger argument against triage
than optimism would be. **Triage by first-order size is provably discarding £7m of revenue signal you do not have.**

### Finding 4 — cross-sell is real, and it is slow

Of the 156 multi-line dealers, **115 (74 %) bought their second line on a later date**, not in the opening basket.

| Lag from first line to second | Dealers |
|---|---|
| Under 3 months | 30 |
| 3–12 months | 42 |
| 1–3 years | 26 |
| **Over 3 years** | **17** |

**Median lag: 246 days — a little over eight months.**

**This is the most directly actionable finding in the tranche.** `NEXT.md` lane 4 puts the cross-sell prompt in the
specification conversation, which is right — but the data says **the adjacency lands months after the first order,
not at it.** A prompt fired at point-of-first-order is aimed at the wrong moment for three-quarters of the cases,
and 43 dealers took more than a year. **So the cross-sell trigger is a dormancy-and-adjacency prompt on an
established account, not a basket suggestion** — and that is a `detect` rule engine can compute from order history
(`evidence/engine-audit.md` §2), needing no new capture at all.

### Finding 5 — the own-brand lines behaved differently from each other

| | Dealers | Net | Was it the dealer's **entry** line? |
|---|---|---|---|
| **DT SCREENS** | 85 | £1,165,218 | **Entry for 45; arrived later for 40** |
| **CATS** | 23 | £141,844 | Entry for **7**; arrived later for **16** |

**DT was a genuine front door** — over half its dealers met the business through it. **C-ATS mostly arrived
second**, after a dealer was already buying something else.

**This bears on an open item without settling it.** `registers/open-items.md` asks for entry products per brand, and
`NEXT.md` §B puts C-ATS first in the record-filling order — *for a different reason* (its data already exists, so
the standard gets set cheaply). **Those two are compatible**, but the evidence says C-ATS historically converted as
a **follow-on to an existing relationship**, not as a door for strangers. Worth weighing before C-ATS is asked to
carry a cold-entry pathway. **Recorded as evidence; the entry-product decision remains open and Neil's.**

### Finding 6 — how much of the inheritance carried over, joined against engine

Because the entity is the group's own, the historic dealer list can be matched against engine's **348 registered
accounts** (read 2026-08-13). Matching is on normalised company names — trading-as tails stripped, suffixes
ignored — so **treat every number here as a floor**: the method certainly misses re-registrations under changed
names. Confirmed misses already spotted include *"The Next Level"* against engine's *"TNL Systems Ltd T/a The Next
Level"*, and *"Glo Audio Visual Ltd."* against *"GLO AV Ltd"*.

| | Dealers | Share |
|---|---|---|
| Historic dealers **found in engine** | **93** | 26 % of the base — **but 45 % of historic revenue (£5,262,007)** |
| Historic dealers **not found** | 261 | 74 % of the base, 55 % of revenue |
| Of the **top 50** historic dealers | **24 in engine** | Just under half |

**Read together, those two lines are the finding.** A quarter of the base carried across, and it is
disproportionately **the valuable quarter** — retention was weighted toward value rather than random. **But
just under half the top fifty accounts of twelve years have no account in the current system**, which is
`group-strategy/the-group-play.md`'s third consequence — *"an asset taken for granted leaks"* — measured for the first time
rather than asserted.

### Finding 7 — the reactivation list, and it is the commercial headline

Filtering the unmatched to those still trading in **the last three years of the file (2021 or later)**:

**50 dealers, £2,326,987 of historic net between them, with no account in engine.**

The largest ten, with their last recorded order:

| Dealer | Historic net | Last order | Lines bought |
|---|---|---|---|
| Sensory International Ltd | £458,664 | 2022-01-13 | 5 |
| SMC | £354,634 | **2023-07-28** | 5 |
| TwentyTwo Integration | £326,191 | **2023-09-26** | 5 |
| Audio Alpha Ltd | £183,970 | 2023-01-16 | 4 |
| AT&C Professional Systems Ltd | £108,172 | 2021-10-26 | 2 |
| KJ West One | £107,895 | 2023-01-18 | 6 |
| AT&C Audio Technology & Communications Ltd | £87,087 | 2021-03-22 | 2 |
| Pericom PLC | £82,509 | 2021-10-22 | 1 |
| LiveSmarter Ltd | £69,060 | 2022-02-17 | 4 |
| BATH CI | £58,043 | 2022-06-02 | 6 |

**This is the same argument C1j (`../group-strategy/commercial-model.md`) already makes about the US, applied at home:** *"a resigned
distributor's dealers become unserved, not absent."* These are dealers who bought from this business — several of
them across five or six lines — and who have no route to it now. **`C1j` calls that pattern "the fastest revenue in
the strategy" and "not dependent on the content programme."** The same reasoning holds here, and unlike the US list
this one requires no territory decision.

**Three cautions before anyone picks up a phone.**

1. **It is a screening list, not a verdict.** Fuzzy matching, and the two AT&C rows are probably one group counted
 twice. Every row needs a human check against engine before contact.
2. **Some rows are not dealers.** Individuals appear (two of the fifty), as do contractors — Bam Construction,
 Quinn London — which is a different relationship from an integrator.
3. **`MON-5` bites here.** The file ends 2023-12-04 and engine starts May 2026. A dealer whose "last order" reads
 2023 may have traded through 2024–25 in a system nobody has shown me. **Close that gap before treating any of
 these as lapsed.**

### What this tranche does not answer

- **Nothing about *why*.** No loss reasons, no competitor, no dimension — this is invoiced revenue only, so
 `X6`/`REC-2` remain uncaptured (`evidence/engine-audit.md` §3). The archive proves the *shape* of relationships, never the
 reasoning inside them.
- **Nothing about questions asked.** `MON-2`'s second question — which questions recur across fourteen years — needs
 the mail archive (`CON-3`), not this file.
- **Nothing post-2023.** The file stops at 2023-12-04, and engine starts in May 2026. **There is a gap between
 them** worth naming: whatever ran 2024–2025 is in neither source yet.
- **Cross-*brand* across SRND's six**, as opposed to cross-line in distribution — still unmeasured, and only
 engine's own history will eventually answer it directly.

---

## Tranche 2 — Display Technologies, 2016–2026

**Source.** `DT - Sales Analysis Report - All.xlsx` (Neil, 2026-08-13). Same Xero-derived shape: **3,952 raw lines,
2016-07-12 to 2026-08-12 — yesterday.** Method as tranche 1, excluding non-product accounts (shipping, freight,
warehousing, payroll, VAT, cost-of-sales, inter-company postings) leaving 3,460 product-revenue lines.

> **This closes `MON-5`.** DT's record runs continuously through 2024, 2025 and into 2026, so the archive and engine
> are no longer two disconnected windows — **for DT.** The distribution side still has the 2024–25 hole, and Neil
> has named the source that fills it: **Shopify, from when distribution sales swapped into SRND** (`MON-8`).

**One structural difference from tranche 1 that must be handled, not averaged away.** DT sold heavily **to its own
group**: of £5,620,592 total product revenue, **£1,381,762 (24.6 %) went to intra-group entities** — Apex Tech
Scotland Ltd £782,537, SRND Group Ltd £470,031 and Apex Tech International Ltd £129,194. **Every figure below is
external-only (£4,219,271)** unless it says otherwise.

> **Two entity corrections from Neil, 2026-08-13, applied throughout.** *"Apex Technologies USA"* and *"Apex
> Technologies USA LLC"* are **the same counterparty** — the April 2024 split is a re-registration in the books, not
> a new relationship — so they are merged into one account below. And **Apex Tech International Ltd was a group
> company, not a dealer**: it served Europe and was *"pointless as a third company, so we just rolled it into
> SRND."* It has therefore moved from external revenue into the intra-group line. Both corrections revise figures
> first written from the raw file alone.

**The intra-group line is itself a finding.** It runs at a fifth to a quarter of DT's output consistently, and 2025
was its largest year at £222,124. **That is the consolidation Neil describes** — first International folded into
SRND, then distribution sales swapped across — visible from DT's side of the invoice.

**And the account dimension is product category, which is a third opinion on a live question.** DT's thirteen
revenue categories — Motorised / Non-Motorised On Wall Screens, Image Surfaces, Port Hole Glass, Motorised /
Non-Motorised Mount Solutions, Mistral, Bespoke Solutions, Other Screens, Mechanics, Hush Boxes, Others, DT Store
Sales — **already group DT by mechanism.** `NEXT.md` treats "group the range by mechanism" as an hour of owner
knowledge still to be spent; there are now **three independent groupings** to reconcile instead of inventing one:
this revenue set, engine's 14 `product_families`, and the twelve record scopes drafted in
`brands/display-technologies/product-records.md`.

### Finding 8 — DT is a concentrated, distributor-led business, and distribution was not

| | DT (2016–2026) | SRND Distribution (2012–2023) |
|---|---|---|
| External dealers, ever | **76** | 354 |
| Active in a typical year | **11–27** | — |
| Top 1 account | **31.5 %** | — |
| Top 5 accounts | **61.0 %** | 22.3 % |
| Top 10 accounts | **76.8 %** | 36.2 % |

**These are two different businesses wearing one group's clothes.** Distribution was a broad dealer base where the
top five held a fifth of revenue; **DT is one account holding nearly a third, five holding over sixty per cent, and
ten holding three-quarters.** For scale, the top account is **2.8× the second** (£1,329,564 against £478,249).

**This matters for how the group strategy reads.** *"Valuable dealer relationships, counted across every brand, over
years"* describes distribution's shape well and DT's poorly — DT's asset has been a handful of accounts, mostly
distributors. **Not a contradiction of the strategy; a measurement of the distance between the strategy and DT's
actual history**, and an argument that the direct-dealer model is something DT has to *build*, not resume.

### Finding 9 — the erosion behind the headline, and it runs the other way from the assumption

External revenue by year, split by whether it came from an Apex-named account:

| Year | External total | Apex USA | **Everyone else** |
|---|---|---|---|
| 2019 | £447,241 | — | £447,241 |
| 2020 | £592,272 | £107,868 | **£484,405** ← peak |
| 2021 | £560,016 | £232,385 | £327,630 |
| 2022 | £610,247 | £257,325 | £352,922 |
| 2023 | £530,378 | £273,044 | £257,335 |
| 2024 | £439,770 | £194,456 | £245,314 |
| 2025 | £386,918 | £201,987 | £184,931 |
| 2026 *(to 12 Aug)* | £219,539 | £62,499 | £157,040 |

**DT's non-Apex dealer revenue peaked in 2020 at £484,405 and has fallen every year since to £184,931 in 2025 — a
62 % decline.** Apex's growth masked it through 2021–23; when Apex flattened, the underlying erosion became the
headline.

**New-dealer acquisition tells the same story from the other end:** 14 new dealers in 2024 — the best year on
record — then **5 in 2025 and 2 so far in 2026.**

**But the full-year view above misleads on 2026, and like-for-like corrects it.** Comparing 1 January to 12 August
in each year — the period 2026 actually covers:

| YTD to 12 Aug | Apex USA | **non-Apex** | Total | non-Apex dealers active |
|---|---|---|---|---|
| 2022 | £170,285 | £220,806 | £391,091 | 19 |
| 2023 | £198,891 | £179,067 | £377,957 | 20 |
| 2024 | £129,064 | £165,499 | £294,563 | 19 |
| 2025 | £143,463 | £98,222 | £241,685 | 13 |
| **2026** | £62,499 | **£157,040** | £219,539 | **10** |

**The five-year slide has broken: non-Apex revenue is up 60 % year-on-year YTD** (£98,222 → £157,040), while Apex
is down 56 % as the grace period runs. **That is a much better position than the full-year table suggests**, and it
is the number to watch rather than the annual one until 2026 closes.

**The caution is in the last column, and it is the strategically important half.** That 60 % recovery came from
**ten dealers, against thirteen last year and nineteen or twenty in 2022–24.** Revenue per non-Apex dealer has
roughly doubled while the count keeps thinning. **So DT's revenue is recovering by concentrating, not by
broadening** — which is precisely what `group-strategy/the-group-play.md` says the group exists *not* to do: the asset is
*"valuable dealer relationships, counted across every brand, over years,"* and the count is still going the wrong
way. **Good news on the revenue line, unchanged news on the asset.**

**This is `group-strategy/the-group-play.md`'s second consequence, measured on DT itself:** *"Direct is asset-building, not
cost-saving. A distributor owns the relationship instead of us."* The years DT leaned hardest on a distributor are
the years its own dealer base thinned. **The strategy already argues this; DT's own numbers now evidence it.**

### Finding 10 — **the Apex-Tech position: asked, answered, and the repo was right**

**Merged as Neil confirms — one counterparty across both account names — Apex USA is £1,329,564: 31.5 % of DT's
entire external revenue, over seven unbroken years, and 2.8× the next largest account.** It bought **13 of the 13
product lines**, which no other dealer did.

| Year | Apex USA |
|---|---|
| 2020 | £107,868 |
| 2021 | £232,385 |
| 2022 | £257,325 |
| 2023 | **£273,044** ← peak |
| 2024 | £194,456 |
| 2025 | £201,987 |
| 2026 *(to 12 Aug)* | £62,499 |

**Still buying four weeks ago — last order 2026-07-16** — and engine independently shows the account with **11 sales
orders** inside its eleven weeks of history (`evidence/engine-audit.md`).

> **▶ Resolved (Neil, 2026-08-13). The agreement officially ended 1 July 2026.** The resignation is in effect, *"but
> it's not a brickwall filter as they have projects in play and it is common to give 90 days grace for them to tidy
> that up while we are starting our own push."* **So the repo was right and this finding raised a false alarm** —
> `C1f` and `C1j` stand unchanged, and the trading that looked like a live relationship was notice and grace.

**And the data says the grace is already spent.** Splitting 2026 at the 1 July end date:

| 2026 | Apex USA |
|---|---|
| 1 Jan – 30 Jun *(agreement live)* | £62,143 |
| **From 1 July *(grace)*** | **£356** — one order, 2026-07-16, one mount line |

**Apex is effectively at zero already.** Grace nominally runs to about 29 September, but £356 in six weeks says there
is nothing material left to come. **The cliff is behind us, not ahead of us** — which also means the wind-down began
well before the formal end: H1 2026 ran £62,143 against £143,463 in the same period of 2025, a 57 % fall while the
agreement was still live.

**The consequence is the good news in this tranche.** DT absorbed the loss of a third of its external revenue *and*
its total YTD is down only 9 % (£241,685 → £219,539), because non-Apex revenue grew 60 % over the same period
(finding 9). **The replacement is already happening.** What has not recovered is the dealer *count* — ten active
non-Apex dealers against nineteen or twenty in 2022–24 — so the exposure now is breadth, not the missing distributor.

**The repo says something different.** `evidence/current-state.md` records Apex-Tech as having **resigned from DT**;
**C1f** (`../group-strategy/commercial-model.md`) treats the US as *"open and unencumbered"* because of it; **C1j** calls the Apex dealer base
*"unserved"* and *"the fastest revenue in the strategy"*; `NEXT.md` lane 7 opens on *"the largest market in the
world is unrepresented."* **Workstream W2 (`US-1`–`US-6`) rests on that reading.**

**The size of the dependency is still worth stating plainly: 31.5 % of DT's external revenue over seven years was one
counterparty, and it was the only dealer that ever bought the whole range.** C1j describes that dealer
base as *"warm"* and its recovery as *"the fastest revenue in the strategy"* — **on these numbers that is right about
the prize, and the window is now open rather than closing.** Those dealers lost their supply route on 1 July and are
being tidied up by a departing distributor as we speak.

**A method note worth keeping, because it nearly produced a wrong conclusion.** Two account names for one
counterparty, a partial current year, and an annual table together made a completed departure look like a live
relationship. **Splitting on the date the arrangement actually ended — and comparing like-for-like YTD rather than
annualising — reversed the reading.** Neither correction was available from the spreadsheet alone; both came from
asking. **Flagging rather than concluding was the right call, and the flag is now cleared.**

### Finding 11 — the first-order result replicates

| First order | Dealers | Reordered | Mean later revenue |
|---|---|---|---|
| < £1k | 18 | 56 % | £18,027 |
| £1–5k | 33 | 64 % | **£49,783** |
| £5–20k | 25 | 56 % | **£63,170** |
| £20k+ | 1 | — | — |

Small numbers, so this is corroboration rather than proof. **But it points the same way as tranche 1 in a completely
separate business and a different decade:** sub-£5k first orders went on to average £49,783 afterwards. **Two
independent datasets now say first-order size does not predict relationship value.**

### What tranche 2 does not answer

- **Still nothing about why** — no loss reasons, no competitors. Invoiced revenue only.
- **The distribution 2024–25 gap remains** (`MON-8`, Shopify).
- **Territory is inferable but not stated** — dealer names imply geography (USA, India, Spain, Canada) but there is
 no country field, so any international split is inference, not data.

---

## Tranche 3 — Light Walls, 2020–2026

**Source.** `Light Walls - Account Transactions.xlsx` (Neil, 2026-08-13). Account Transactions format, as C-ATS and
SRND. Stated period 2016-08-01 → 2026-08-31; **the data begins in 2020.** 418 rows, 380 product-revenue,
**£574,683 = £502,855 external + £71,828 intra-group**, 26 counterparties.

### Finding 12 — the shape: three good years, then a stop

| Year | Total | External |
|---|---|---|
| 2020 | £9,178 | £9,178 |
| 2021 | £199,313 | £174,263 |
| **2022** | **£250,859** | **£236,222** ← peak |
| 2023 | £96,870 | £83,191 |
| 2024 | — | — |
| 2025 | — | — |
| 2026 | £18,463 | **£0** (intra-group only) |

**External trading stops after 2023.** The 2024–26 rows are not trade at all: a £35,750 inter-company journal, a
pair of offsetting Protopixel journals, and a single **£18,463 invoice to SRND Group Ltd in March 2026** which moves
the residual Protopixel position into SRND. **So the brand's commercial life in this data is 2021–2023, with 2022 its
best year.**

**The reason is on the record and is not in this file** (Neil, 2026-08-13): *"it was going so well but the pain of
the protopixel nodes all breaking and needing replaced left us gun shy."* The invoice ledger shows the stop; it does
not show the replacement cost, which would sit in purchases and warranty rather than in sales.

### Finding 13 — two concentrations, and one of them is the same account as DT's

| Counterparty | Net | Share of external |
|---|---|---|
| **Apex Technologies USA** | **£273,866** | **54.5 %** |
| Cinema Partners | £63,567 | 12.6 % |
| INT3 Ltd | £35,325 | 7.0 % |
| Wakefields Smarter Home Technology | £33,570 | 6.7 % |
| Chevalier | £22,252 | 4.4 % |

**Over half of Light Walls' external revenue went through Apex USA** — the same counterparty that carried 31.5 % of
DT's. Recorded as a fact about channel structure, not a claim about cause: Light Walls stopped in 2023, the Apex
agreement ended 1 July 2026, and nothing here connects them.

**And a quarter of revenue was the bought-in component.** By account line: `Light Walls` £350,912, **`Protopixel`
£144,515** (25 %), generic `Sales` £79,256. Protopixel ran £21,855 (2021) → £68,448 (2022) → £34,221 (2023), then
the journal reversals. **`ProtoPixel SL` appears as both customer and supplier** — five sales invoices to them in
2020, then payable invoices and negative postings against the Protopixel sales account — so the relationship was
two-way in the books.

### What tranche 3 changed elsewhere — two figures I had published

**Light Walls Ltd is itself a group entity**, so adding it to the intra-group list reclassified revenue in two
already-loaded sources. Both corrected in place:

| | Was | Now | Moved |
|---|---|---|---|
| DT external | £4,238,830 | **£4,219,271** | £19,559 of DT→Light Walls sales (2021–23) |
| GTUK external | £11,745,315 | **£11,742,315** | £3,000 |

Knock-on: DT's dealer count 77 → **76**, top-1 share 31.4 % → **31.5 %**, top-5 60.7 % → **61.0 %**, top-10 76.4 % →
**76.8 %**, and 2022's non-Apex YTD £229,706 → £220,806. GTUK's dealer count 355 → **354**, its cohort counts by one
dealer, and its concentration percentages are unchanged at one decimal place. **No finding reverses; the £1–5k
cohort's mean later revenue moves from £36,914 to £37,143 and still exceeds the £50k+ cohort's £27,618.**

**The lesson for the remaining tranches:** each new group entity can reclassify earlier ones, because it may have
been a *customer* of them. The loader holds one shared intra-group list for exactly this reason, and **all sources
are regenerated together** after any addition to it.

### Loose ends in this tranche

- **`Complete-ATS` is unresolved but immaterial — £222.** It is left external. "Complete ATS" is the C-ATS vendor
 name on the store, which suggests a group entity, but the C-ATS company is *Cinema Acoustic Treatment Systems
 Limited*. Flagged in `data/normalise.py` (`UNRESOLVED_ENTITIES`); at this value it changes nothing either way.
- **`UNKNOWN_CONTACT`** appears as a literal placeholder on one £12 `Other Revenue` row — excluded from revenue.
- **Three new spellings of group entities** were introduced by this file and are now canonicalised in the loader:
 `Apex Tech Scotland Ltd / Apex-Tech UK`, `Display Technologies Limited`, and a lower-case `apex Tech
 International Ltd`.
- **Neil notes work in progress on the lighting side** — *"something special… that can really help us get back into
 that lighting business."* Recorded as a pointer only; there is nothing about it in the data.

---

## Fabric Walls — no separate source; it is inside SRND Group

**Fabric Walls has no entity report to load: its sales are already under SRND Group Ltd** (Neil, 2026-08-13). So it
is a *slice* of tranche 2c rather than a tranche of its own, and it is recoverable because the store-item
classification (`data/classify_store_items.py`) split the store blob into categories.

**The product is three components — "metal frame and fabric… and fabric track"** (Neil) — and the accounts separate
them:

| Component | Categories | Net | % of SRND | Dealers |
|---|---|---|---|---|
| Fabric track | `Metal Fabric Track`, `Plastic Fabric Track`, `Fabric track` | **£197,476** | 7.2 % | 21 |
| Metal frame | `Fabric wall frames & panels` | £62,729 | 2.3 % | 8 |
| Fabric | `Fabrics`, `Fabric samples` (Ultrasuede, Showtex, Aura Flex) | £15,136 | 0.6 % | 8 |
| Installation tools | `Tools` | £1,128 | 0.0 % | 4 |
| **Product total** | | **£276,470** | **10.1 %** | **32 distinct** |

Plus, sitting in other categories: **£19,548** of Fabric Walls design services (the Seattle and Madrid room designs)
and a **£9,000** downpayment on the Mexico City showroom — **£305,018 in total, 11.2 % of SRND's product revenue.**

**Revenue is flat and current:** £107,991 (2024), £108,206 (2025), £60,273 (2026 part-year). **Thirty-two dealers
have bought it** — the broadest dealer base of any own-made line in the loaded data, against DT's 76 across ten years
and C-ATS's 16.

**Antecedent confirmed, and it is older than the group** (Neil, 2026-08-13). GTUK's **£46,761 across 5 lines of
`Sales - BARRISOL COUTURE`** is the tail of real prior work: **Simon worked for Neil then and led Barrisol Couture
and High Tech Couture.** So stretch-fabric wall and ceiling work is not a new competence — *"it's not new work."*
The same holds across the range: the group sold **third-party acoustic systems** exactly as it sold other companies'
projector screens, which is what GTUK's `STEALTH`, `LEON`, `AGATH`, `ADA`, `WISDOM`, `ACURUS`, `DATASAT`, `STEWART`
and `PHASE TECHNOLOGY` lines are. **Own-made C-ATS and DT products grew out of distributing the third-party
equivalents first.**

> **Neil's caveat, and it governs how this is used:** *"all just history to be aware of but not plan around too
> much."* **Recorded as provenance only.** It explains why the competences are deeper than the brands' ages suggest;
> it is not a basis for planning, and the £46,761 is not counted in the Fabric Walls figures above.

*Method note: a regex for fabric-wall terms also catches DT image-surface lines described as "no silicon edge". One
such line (£601) was excluded by hand. Any repeat of this slice should filter on `category`, not on description text.*

---

## The consolidated view — fifteen years in one series

*All tranches joined. **This is the artefact the per-tranche sections could not give**: one group-level series, with
intra-group flows excluded on the selling side so nothing is double-counted (a DT→SRND sale is dropped from DT and
picked up when SRND sells it onward). Still pure numbers — revenue only, no margin.*

### Finding 14 — group external revenue, 2012–2026

| Year | UK distribution | DT | C-ATS | Light Walls | SRND Group | **Group** |
|---|---|---|---|---|---|---|
| 2012 | £1,369,480 | — | — | — | — | **£1,369,480** |
| 2013 | £1,101,397 | — | — | — | — | £1,101,397 |
| 2014 | £1,044,627 | — | — | — | — | £1,044,627 |
| 2015 | £506,174 | — | — | — | — | £506,174 |
| 2016 | £515,402 | £23,221 | £3,520 | — | — | £542,142 |
| 2017 | £559,460 | £147,004 | £71,244 | — | — | £777,708 |
| 2018 | £740,106 | £282,224 | £33,148 | — | — | £1,055,479 |
| 2019 | £1,019,659 | £447,241 | £11,960 | — | — | £1,478,860 |
| 2020 | £876,115 | £592,272 | £36,153 | £9,178 | — | £1,513,719 |
| **2021** | £1,884,000 | £549,357 | £22,978 | £174,263 | — | **£2,630,599** ← peak |
| 2022 | £1,242,364 | £601,347 | £24,385 | £236,222 | — | £2,104,317 |
| 2023 | £883,531 | £530,378 | £6,338 | £83,191 | £10,670 | £1,514,108 |
| 2024 | — | £439,770 | £40,507 | — | £790,971 | £1,271,247 |
| 2025 | — | £386,918 | £3,978 | — | £1,048,315 | £1,439,211 |
| 2026 *(part)* | — | £219,539 | — | — | £875,327 | £1,094,866 |
| **All** | **£11,742,315** | **£4,219,271** | **£254,210** | **£502,855** | **£2,725,282** | **£19,443,934** |

**Three phases, and the numbers date them.** Pure UK distribution to 2015, and declining. Own brands appear in 2016
(DT and C-ATS in the same year) and grow alongside distribution to a **2021 group peak of £2.63m**. The handover runs
through 2023 — GTUK's last invoice 2023-12-04, SRND's first revenue that same year — and from 2024 the group is
SRND-led.

**On 2026: it is running ahead, but on lumpy revenue.** £1,094,866 to mid-August is roughly 7.5 months, which
annualises near **£1.7m against 2025's £1.44m**. Treat that with care: **three Leyard Komodo LED-wall lines alone are
£472,320 — 54 % of SRND's 2026** — so the annualisation rests on a handful of large orders rather than a broad rate.
*(Source cut-offs differ slightly: DT 2026-08-12, SRND 2026-08-10, C-ATS 2026-07-31, Light Walls 2026-03-31.)*

### Finding 15 — the own-brand shift is real and incomplete

**GTUK's own-brand share of its own revenue was 11.1 %** (`DT SCREENS` + `CATS`, £1,307,062 of £11,742,315). For the
current entity, classifying SRND's categories into own-made, carried and services:

| | Net | Share |
|---|---|---|
| Carried / third-party | £1,381,327 | **50.7 %** |
| Own-made | £936,980 | **34.4 %** |
| Services | £246,276 | 9.0 % |
| Other (shipping, surcharges, adjustments) | £160,700 | 5.9 % |

**So own-brand share roughly tripled — 11 % to 34 % — and the current entity is still majority carried.** By year,
own-made was £260,162 (2024) → £401,532 (2025) → £275,286 (2026 part), while carried was £443,818 → £386,441 →
£551,068. **2026 is more carried than 2025, not less**, because of the Leyard orders. *"Hybrid distributor/
manufacturer" is exactly right as a description of today; "manufacturer" is not yet true of the revenue.*

*This split is my classification of category names and is reviewable — the own/carried lists are at the top of the
query, and `Fabrics` (Ultrasuede) is counted as carried even though it is consumed inside a Fabric Walls product.*

### Finding 16 — dealer breadth, side by side, is the one consistent weakness

| Entity | Period | External dealers | Top 1 | Top 5 |
|---|---|---|---|---|
| GTUK / UK distribution | 2012–23 | **354** | 5.3 % | 22.3 % |
| SRND Group | 2023–26 | **147** | 22.4 % | 45.2 % |
| DT | 2016–26 | 76 | 31.5 % | 61.0 % |
| Light Walls | 2020–26 | 19 | 54.5 % | 85.2 % |
| C-ATS | 2016–26 | 12 | 25.3 % | 85.9 % |

**The distribution business was broad and the own-brand businesses are narrow.** GTUK's largest account was 5.3 % of
its revenue; every own-brand entity has a single account at a quarter to a half. **SRND is rebuilding breadth
fastest** — 147 dealers in three years, the widest of the own-brand era — and is the least concentrated of them.

**Fabric Walls is the broadest own-made line at 32 dealers** (as a slice of SRND), against DT's 76 across ten years
and C-ATS's 12.

### What the consolidated view still cannot answer

Worth stating plainly before any of it is used for planning:

- **No margin.** Revenue only. A carried LED wall and an own-made screen at the same revenue are not the same
 business, and nothing here says which is worth more.
- **No why.** No loss reasons, no competitors, no lead source — `X6`/`REC-2` remain uncaptured (`evidence/engine-audit.md`).
- **No territory.** No country field in any source; dealer names imply geography but that is inference.
- **Uneven scope.** GTUK is **UK-only**; the others include international. So the pre-2024 series understates the
 group's true geography while the post-2024 series does not.
- **2024–25 distribution is thinner than it looks**, pending `MON-8` (Shopify).

---

## Finding 17 — audio was the group's largest business, and it is now absent

*Measured at Neil's prompt (2026-08-13): "look at how much of our historic revenue was speakers, amps and
processing to see why we see [Pro-Fi] as such an important gap to fill." **Revised upward the same day** once Neil
identified four carried lines the account names did not explain — `NEXTGENTECH`, `PRO AUDIO`, `TPI Cinema` and
`AGATH`. The first estimate of 30.8 % was too low.*

**In the distribution era, audio was 38.7 % of revenue — £4,548,710 of GTUK's £11,742,315.** That makes it the
group's **largest** business by category, ahead of projection.

**Across the whole group, 2012–2026: £4,802,861 — 24.7 % of all external revenue.**

| Category | Group net | Share | Carried brands |
|---|---|---|---|
| **Speakers** | **£2,809,085** | 14.4 % | Stealth, Leon, Wisdom, Phase Technology, SolidDrive, Quested, Aerial |
| **Audio over IP** | **£779,979** | **4.0 %** | NextGen Tech |
| Amplifiers | £548,019 | 2.8 % | ADA, Acurus, Aragon, Integra, StormAudio |
| Speakers & amplifiers *(mixed lines, unsplittable)* | £475,672 | 2.4 % | Pro Audio, TPI |
| Audio processing | £190,105 | 1.0 % | Datasat |
| **Audio total** | **£4,802,861** | **24.7 %** | |

**Today it is 9.3 % of SRND and entirely carried** — £254,151, all third-party (MAG Theatron, PhaseTech, DCB Flyte).
**No own speaker line is shipping** (Neil).

**The strongest single number for the Pro-Fi case is the second row.** `NEXTGENTECH` is **audio over IP, and that is
exactly where Pro-Fi is aiming** (Neil). So the group has already sold **£779,979 into the specific category the big
bet targets** — not an adjacent one — to dealers it can still name. **That is a matched precedent rather than a
hopeful analogy**, and it is the difference between entering a category and returning to one.

*Two classification notes. `Speakers & amplifiers` exists because Pro Audio and TPI were each "speakers and amps"
and cannot be split — it rolls into audio but must never be read as speakers alone. `AGATH` turned out to be
**mirror TVs** (£216,342), so it is not audio at all and is excluded here.*

## Finding 18 — margin changes the LED reading, and margin is the data we do not have

**LED video walls carry 20 % margin** (Neil, 2026-08-13). Applied to the £610,885 of LED wall revenue in SRND, that
is **roughly £122,000 of gross margin** — against **22.4 % of revenue.**

**This is the first hard evidence that the revenue tables in findings 14–16 overstate the carried lines' importance
to the business**, and it cannot be corrected further because **no margin data has been loaded for any other line.**
The consequence is specific and worth stating before anyone ranks work by revenue:

- **A carried line at 20 % needs five times the revenue of a 100 %-margin service, and roughly double that of a
 50 %-margin own-made product, to contribute the same money.**
- On that basis **Fabric Walls (£276,470 product revenue) may already out-earn LED walls (£610,885)** in margin
 terms — *may*, because the own-made margin is unknown. **This is a hypothesis the data cannot yet test.**
- **Neil's framing is the right one and the numbers support it:** LED walls are *"a very nice revenue that supports
 our own lines"* — infrastructure for the P&L, not the strategic centre, and *"an impossible category to get into as
 a manufacturer"* so the carried relationship with the industry number one is the only way to hold the category.

**`MON-10` is therefore the highest-value missing dataset now** — a margin or cost column against these lines would
re-rank every priority the revenue view suggests.

---

## Tranche 4 — the Monday.com CRM boards (`MON-1`)

**Source.** Four board exports supplied 2026-08-13, held in `data/source/Monday - *.xlsx`, flattened by
`data/normalise_monday.py` into `data/derived/monday-{deals,deal-subitems,accounts,leads,contacts}.csv`.

| Board | Items | Columns |
|---|---|---|
| Deals | **155** + 226 sub-deals | 18 |
| Accounts | **1,658** | 29 |
| Leads | **1,233** | 39 |
| Contacts | **1,371** | 31 |

**Format note, because it bites hard.** Monday exports grouped boards, so the sheet is not a table: a group name
row, then a *repeated* column-header row, then items — and on the Deals board **sub-item blocks sit between parent
rows.** A latching parser produced 6 deals instead of 155. **Column A is the discriminator** — parents populate it,
sub-items start at column B. The group name is kept as `board_group` because on Deals **it is the only win/loss
signal in the export.** Row counts reconcile exactly (Deals: 462 source rows = 2 title + 4 groups + 4 headers +
67 sub-item headers + 155 items + 226 sub-items + 4 blank).

### Finding 19 — the pipeline exists, is 18 months old, and still has no loss reason

**Correcting what this repo expected of `MON-1`.** `evidence/current-state.md` recorded that *"the historical pipeline is in
the old Monday.com CRM logs"* and that this was where "the years" were. **The deals board runs 2025–2026 only** — 93
deals created in 2025, 62 in 2026. **It is eighteen months of pipeline, not years.**

> **And that is a retention practice, not an export limit** (Neil, 2026-08-13): *"I don't have older records of deals.
> Once they are lost there seems little point keeping them."* So the eighteen months is all there is, and older lost
> deals were discarded rather than archived. **Recorded because it changes what `X6` can ever be:** it can only be
> built forward, never recovered, and every lost deal removed takes with it the one thing
> `registers/record-form.md` calls *"the only outside view we have."* **The fix is close to free and belongs in the
> capture routes, not in a policy argument — keep the closed-lost record with a reason on it rather than deleting the
> row.** At 74 lost deals in eighteen months that is a few seconds each, and it is the difference between `X6`
> existing in a year and this same finding being written again.

| Group | Deals | Value |
|---|---|---|
| Active | 47 | £4,133,340 |
| **Closed Lost** | **74** | **£5,994,922** |
| Closed Won | 9 | £1,004,875 |
| Complete | 25 | £194,882 |

**This is the first win/loss data the group has ever had**, and it is sobering: **74 lost against 34 won-or-complete**
by count, **£6.0m lost against £1.2m won.** Treat the values as *stated deal value* — aspirational on lost deals and
never invoiced — so the ratio is a signal about pipeline hygiene and qualification, not a lost-revenue figure.

**And `X6` is still not answered.** There is **no loss-reason and no competitor field.** `Description` is populated on
67 of 74 lost deals but describes **what the deal was**, not why it went — *"VDS and Komodo options"*, *"Basement
cinema project"*, *"Acoustic isolation + FW + C-ATS"*. A keyword sweep for reasons or rivals hit 7 of 74, and every
hit was a product mention (Barco, Sony) rather than a competitive loss.

> **So the answer to `REC-2`/`X6` is now definitive across all three systems.** Engine records `won_at` and no
> counterpart; Monday records the *fact* of loss as a board group and no reason; the invoice archive records only what
> was sold. **Nothing anywhere holds why a deal was lost, to whom, on what dimension. `X6` must be captured going
> forward — there is nothing to mine.** `SYS-2`'s original premise was right all along.

### Finding 20 — the Accounts board holds a per-brand awareness funnel, and nobody has used it

**This is the most valuable thing in the tranche.** Every one of the 1,658 accounts carries a status for **each of six
brands** — `Barco Status`, `DT Status`, `Fabric Walls Status`, `Mag Status`, `CATS Status`, `Leyard Status` — on a
vocabulary that *is* an awareness funnel: **Not Customer → Approached → Presented → Demonstrated → Current Customer**
(plus `Historic Customer`, `Not Interested`, `Out of Territory`).

| Brand | Current | Historic | Demonstrated | Presented | Approached | Not Customer |
|---|---|---|---|---|---|---|
| **DT** | **52** | 14 | 2 | 53 | 20 | 1,493 |
| Fabric Walls | 16 | — | 3 | **73** | 19 | 1,544 |
| C-ATS | 16 | 4 | 1 | 49 | 16 | 1,568 |
| Barco | 14 | — | — | 24 | 15 | 1,504 |
| MAG | 3 | — | — | 26 | 18 | 1,573 |
| Leyard | 2 | — | 1 | 17 | 15 | 1,612 |

**Read the last column, then Neil's diagnosis** — *"no one can buy what they don't even know exists."* **Between
1,493 and 1,612 of 1,658 accounts are `Not Customer` for every brand**, and the funnel says why: only 24–73 accounts
have ever been *presented* any given brand. **The undersold claim is not an impression; it is recorded, per brand, per
account, and has been all along.**

**Two specifics worth carrying into the plan.** **Fabric Walls has been presented to more accounts (73) than any
other brand** — the widest active selling effort, consistent with it being the broadest own-made line in the invoice
data. And **all 266 Approved Dealers carry a status for all six brands**, so cross-brand coverage per dealer is
directly countable — which is `FACT-1`, answerable now without building anything.

### Finding 21 — reach is five times narrower for the own brands than for DT

The Contacts board holds per-brand subscribe flags across 1,371 contacts:

| List | Subscribers |
|---|---|
| SRND | 985 |
| **DT** | **926** |
| Pro-Fi | 193 |
| Light Walls | 195 |
| Fabric Walls | 193 |
| C-ATS | 191 |

**C-ATS can reach 191 people; DT can reach 926.** The same asymmetry shows in declared relationships — SRND `Dealer`
104, DT `Dealer` 42 plus `Distributor` 29, then Fabric Walls 8, C-ATS 9, Light Walls 5, Pro-Fi 4. **This is the
"massively undersold" problem expressed as a distribution list**, and it is the cheapest thing on this page to change:
the audience exists and is already consented.

**And the Leads board points at the US.** Of 1,233 leads, **348 are United States** — the largest single country
by a wide margin, ahead of Italy (53), Spain (46) and France (44), with 647 blank. **901 leads carry an email.**
Set against `US-4`, that is a warm-ish list already in hand, though **908 of the 1,233 are flagged `Not Active`** and
only 39 have any call logged.

### Two things this tranche adds that were not in the repo

- **Two people in sales who are not in `evidence/current-state.md`.** `Primary Sales` on the Accounts board is **Olivier
 Dedek (298 accounts), Mark Franks (225), Erica Johnson (19), Neil (4)**, and Mark Franks also owns a lead. The
 people list records Neil, Olivier, Ben and Simon. **Worth correcting — a 225-account owner is not a detail.**
- **Segment data for the beyond-cinema question.** `Enviroments` is populated on 355 accounts with combinations of
 **Home Cinema and Media Rooms, Luxury Living, Commercial, Outdoor, DCI Screening Rooms** — and `Work Areas` on the
 Leads board carries Residential AV, Commercial AV, Hospitality, Office Spaces. **`group-strategy/channels.md` is
 cinema-shaped and notes non-cinema needs evidence; this is the first structured non-cinema segmentation the repo
 has seen.** Sparse (355 of 1,658) but real.

---

## Finding 22 — the margin policy is in engine; the costs to apply it to are not

*Read from engine 2026-08-13 at Neil's direction ("margin data for our brands in engine"). Partly answers
`MON-10`. **Note the timestamps: `brand_tier_margins` was written at 16:44 the same day**, so this is fresh policy,
not settled history.*

### What is there

Engine models pricing two ways, and both are populated:

**`brand_tier_margins` — a margin per brand per tier**, versioned through `price_lists` as named scenarios:

| Brand | Dealer | Distributor | |
|---|---|---|---|
| C-ATS | 0.40 | 0.40 | |
| Pro-Fi | 0.40 | 0.40 | |
| DT | 0.35 | 0.40 | |
| Fabric Walls | 0.30 | 0.25 | |
| **Leyard** | **0.20** | **0.20** | *archived scenario only — see the flag below* |
| SRND | 0.40 | 0.40 | *archived scenario only* |

**`brand_tier_cost_multipliers` — cost × multiplier = price**, for the own-made brands: **distributor 1.6 ·
dealer 2.1 · 3.0 with no tier** (read as RRP). Present for Fabric Walls, Pro-Fi and SRND; absent for DT and C-ATS.

### The ambiguity, and it is material — **resolved below**

**Is `margin` *our* margin or the *channel's*?** Both readings are supported and they give different answers:

- **Reading A — it is the channel's resale margin.** The Fabric Walls arithmetic fits almost exactly: if RRP is
 cost × 3.0 and a dealer buys at cost × 2.1, the dealer's margin is (3.0 − 2.1)/3.0 = **30 %**, matching
 `fabricwalls dealer 0.30`; a distributor buying at 1.6 and selling on at 2.1 earns (2.1 − 1.6)/2.1 = **23.8 %**,
 near `0.25`. **Under A our own margin comes from the multipliers: 52.4 % selling to a dealer, 37.5 % to a
 distributor.**
- **Reading B — it is our margin at that tier.** Supported by the thing that matters most: **Neil states LED walls
 earn us 20 %, and engine's Leyard rows are exactly 0.20/0.20.** Under B, own-made earns us 30–40 %.

**Reading A cannot be reconciled with Neil's 20 % unless Leyard is a special case; reading B cannot be reconciled
with the cost multipliers.** Flagged rather than resolved — one sentence from Neil settles it.

### What survives the ambiguity, which is the decision-relevant part

**Finding 18's open hypothesis is now answered, and the answer holds under both readings.**

| | Revenue | Margin under A | Margin under B |
|---|---|---|---|
| LED video walls *(carried, Leyard)* | £610,885 | £122,177 *(20 %)* | £122,177 *(20 %)* |
| **Fabric Walls** *(own-made)* | **£276,470** | **£144,870** *(52.4 %)* | £82,941 *(30 %)* |

*(Superseded by the resolution below: the answer is the A-shaped one, arrived at differently.)* Under reading A, Fabric Walls out-earns LED walls on under half the revenue; under B it does not, but the gap
narrows from 2.2× on revenue to 1.5× on margin. **Either way the revenue tables in findings 14–16 overstate the
carried lines**, and Neil's framing — LED as *"revenue that supports our own lines"* — is what the numbers support.

### The limitation that keeps `MON-10` open

**Engine holds the policy but almost none of the inputs. Of 165 live products, 6 carry a cost:**

| Brand | Products | With cost | With RRP |
|---|---|---|---|
| DT | 85 | **0** | 4 |
| Fabric Walls | 37 | **0** | 0 |
| SRND | 10 | 3 | 0 |
| Light Walls | 6 | 0 | 0 |
| Pro-Fi | 5 | 1 | 0 |
| C-ATS | 4 | 0 | 0 |

**So per-line realised margin still cannot be computed** — only policy margins applied to revenue, which assumes
every sale went at list. **`MON-10` moves from "no margin data" to "policy yes, actuals no", and what would close it
is a cost column on the Xero exports** (`MON-11` covers the same re-export) **or costs populated in engine.**

### ▲ And an operational flag worth ten seconds of someone's time

**Two price-list scenarios were activated today; the one left `active` looks like the wrong one.**

- **Active: `Scenario 04/06/2026`** — 8 entries. **No Leyard row and no SRND row**, so the two carried-heavy lines
 have no active margin policy at all.
- **Archived: `Scenario 13/08/2026`** — 12 entries, the same brands **plus Leyard 0.20 and SRND 0.40**.

**And DT's tiers are inverted between them:** active says dealer 0.35 / distributor 0.40; the archived one says
dealer 0.40 / distributor 0.35. **Every other brand gives the dealer the higher figure**, so the active list is the
odd one out on DT as well as being incomplete. **Not corrected here — read-only access, and it is a live pricing
control.**

### ▶ Resolved (Neil, 2026-08-13) — the margins are per-step and they stack

Two sentences settled it: *"we don't sell Leyard to another distributor so that's not a case that could ever
happen"* and **"a DT screen sold direct to dealer nets us both margins."**

**So `margin` is the margin earned at each step of the chain — manufacture → distribution → dealer — and because the
group owns both the manufacturing and the distribution arm, a direct-to-dealer sale earns both steps.** Neither
Reading A nor Reading B above was right on its own; the structure is stacking, not either/or.

| What we sell | Steps we occupy | Our margin |
|---|---|---|
| **Own-made, direct to dealer** | manufacture **and** distribution | **both margins stack** |
| Own-made, through a distributor | manufacture only | the manufacturing step alone |
| **Carried (Leyard)** | distribution only — we do not make it | **one step: 20 %** |

**Worked from the stored figures**, compounding the two steps (1 − (1 − m₁)(1 − m₂)):

| Brand | Distributor step | Dealer step | **Direct-to-dealer margin** |
|---|---|---|---|
| DT | 0.40 | 0.35 | **≈ 61 %** |
| C-ATS · Pro-Fi | 0.40 | 0.40 | **64 %** |
| Fabric Walls | 0.25 | 0.30 | **≈ 47 %** |
| **Leyard** | *n/a — never happens* | 0.20 | **20 %** |

**Sense-checked against the other mechanism:** the own-made cost multipliers give 1 − 1/2.1 = **52.4 %** at the
dealer tier, which sits inside the 47–64 % range the stacked margins imply. **The two mechanisms agree.**

**And this is why the carried lines are structurally different, not just lower-margin.** On Leyard the group can only
ever occupy one step, because it does not manufacture the product — so **20 % is not a negotiating outcome, it is the
ceiling of the position.** Neil's framing follows directly: *"a very nice revenue that supports our own lines."*

### The comparison, now settled

| | Revenue | Margin rate | **Margin** |
|---|---|---|---|
| LED video walls *(carried)* | £610,885 | 20 % | £122,177 |
| **Fabric Walls** *(own-made, direct)* | **£276,470** | **≈ 47 %** | **≈ £131,000** |

**Fabric Walls out-earns LED walls on less than half the revenue** — finding 18's hypothesis confirmed, and the
strongest single argument in this file for ranking work by margin rather than by revenue. **On the same arithmetic,
£100k of own-made revenue is worth roughly £47–64k, against £20k carried** — a factor of two to three.

**These rates are owner-supplied and are treated as authoritative** (Neil, 2026-08-13). That is the same standing as
every other commercial fact in this repo — the pricing gate, the terms, the territory positions — and it needs no
corroboration from the ledger. **`MON-10` is closed on that basis:** the question it existed to answer, *can work be
ranked by margin rather than revenue*, is answered.

*A cost column on the exports (`MON-11`) would still add something, but it is a smaller thing than the row implied:
per-line realised margin, showing where discounting moved an actual sale away from these rates. It would refine the
picture, not correct these figures.*

---

## Finding 23 — the margin ladder, and it explains the group's shape

*Neil, 2026-08-13, drawing the consequence out of finding 22: "the margin illustrates why we started to make not just
buy. It illustrates why a distributor has to add at least 2x to be worth considering. It shows why the cinema store
exists."*

**Three settled positions in this repo were arguments. The margin ladder makes them arithmetic.** Each step of the
chain the group occupies is a margin it keeps, so the question is always *how many steps do we hold?*

| Route | Price to the buyer | Steps we hold | Our margin | Per £1 of cost |
|---|---|---|---|---|
| Through a distributor | cost × **1.6** | manufacture | **37.5 %** | £0.60 |
| **Direct to a dealer** | cost × **2.1** | manufacture + distribution | **52.4 %** | **£1.10** |
| **Direct to a consumer** (RRP) | cost × **3.0** | all three | **66.7 %** | **£2.00** |
| **Carried line** (Leyard) | — | distribution only | **20 %** | *ceiling of the position* |

*(Multipliers are engine's own `brand_tier_cost_multipliers` for the own-made brands; the tier margins compound to the
same place — finding 22.)*

### 1. Why make and not just buy

**Making adds a step that buying cannot.** A carried line lets the group hold **one** step at 20 %; an own-made line
sold to the same dealer holds **two**, at ~52 %. **That is the whole economic case for the 2016 shift**, and the
consolidated series shows it happening: own-brand share went from **11.1 % of the distribution era to 34.4 % today**
(finding 15). **The evolution was not a change of taste — it was a move up the ladder.**

### 2. Why a distributor must add at least 2×

**Selling through a distributor gives away the distribution step**: £0.60 of margin per £1 of cost instead of £1.10.
**£1.10 ÷ £0.60 = 1.83, so a distributor must deliver roughly twice the volume to leave the group no worse off** —
before any allowance for the relationship being theirs rather than ours. **Neil's "at least 2x" is the arithmetic,
and it is conservative.**

> **And the 2× test was already in the repo, as a lived rule rather than a calculation.** `registers/open-items.md`, from
> Neil's account of the distribution history: *"The 2× test kills most candidates instantly, and that is the
> intent"* — alongside the two UK distributors appointed for the group's own brands that both failed. **So this
> finding did not discover the rule; it supplied its arithmetic.** The judgement came first and the numbers agree
> with it, which is the strongest form of corroboration available here.

**This puts a number on two positions that were previously stated as judgement.** `group-strategy/commercial-model.md`
holds that distributors are *"a deliberate case-by-case exception (scale or language barrier only), never the
default"* — **the test for that exception is now quantified: does this distributor plausibly double the volume?**
And `group-strategy/the-group-play.md`'s *"direct is asset-building, not cost-saving"* gains its cost side: **the asset argument
and the margin argument point the same way, which is not something the repo had established.**

**It also explains the DT history in finding 9 without needing a story.** DT leaned on a distributor for a third of
its revenue while its own dealer base thinned — that is the low rung of the ladder taken for volume, and the
measured erosion is what it cost.

### 3. Why the Cinema Store exists

**Direct to a consumer holds all three steps — 66.7 %, £2.00 per £1 of cost, more than three times the distributor
route.** That is the answer to a question the repo describes structurally but never economically: the group play keeps
the consumer proposition as DIY home cinema deliberately, and `group-strategy/commercial-model.md` gives Cinema Store its
own product list — *"a Cinema Store product is a specific product for that channel"*, with the DIY range and plastic
track exclusive to it.

**So the channel split is not merely tidy, it is the top rung.** And the constraint on it follows from the same
arithmetic: **the store can only hold the third step on products a consumer can actually buy and fit alone**, which
is exactly why the trade range is not simply listed there — and why *"no product exists in two places"* protects
margin as well as clarity.

### What this changes, and what it does not

**Nothing here reverses anything.** Three positions already decided — make rather than buy, direct rather than
distributor, a separate consumer store — now share **one measured explanation** instead of three separate arguments.
That is coherence in the sense `CLAUDE.md` means it: the substance was already there; this draws it out.

**The one thing it adds that is genuinely new is a test.** *How many steps does this route let us hold?* It ranks
channel decisions, it prices the distributor exception at 2× volume, and it explains why £100k of own-made revenue is
worth two to three times £100k of carried (finding 22). **Worth carrying into `group-strategy/commercial-model.md` as the
reason behind the exception rule rather than leaving it here as a finding.**

---

## Finding 24 — the deals board, worked properly

*The first pass counted the groups and stopped. This is what the 155 deals and 226 sub-deals actually contain.*

### The live pipeline is £4,133,340 across 47 deals — and it is stacked in one stage

| Stage | Deals | Value |
|---|---|---|
| **In Engine** | **34** | **£3,480,152** |
| Discussion | 4 | £441,075 |
| Proposal | 6 | £202,594 |
| Discovery | 3 | £9,520 |

**Three-quarters of the deals and 84 % of the value sit in `In Engine`.Answered in finding 26: it
means migrated into engine, not a sales stage — so this is not deep-funnel pipeline.** The original question, kept
because the reasoning holds: **the stage name needed one word of explanation** — whether it means *in engineering* (being designed) or *moved into engine* (the platform). It changes
the reading completely: the first is a genuine pipeline stage, the second is a holding pen for everything migrated
into the new system. **The sub-deals suggest the second: 216 of 226 sit at `Proposal` with only 4 `Agreed`.**

### The sales cycle now has a number, and `TSK-3` is what it is for

| Outcome | Deals | Median days, creation → last interaction |
|---|---|---|
| **Closed Won** | 9 | **153** |
| Complete | 25 | 126 |
| Closed Lost | 74 | **105** |
| Active *(so far)* | 47 | 66 |

**A won deal takes about five months; a lost one dies at three and a half.** `NEXT.md` puts `TSK-3` — the lead-time
follow-up — outside the sequence because *"projects run for months, so quote-to-order is a long stage nobody runs
systematically."* **That is now measured rather than asserted, and it gives the follow-up its interval:** a deal
quiet past ~105 days is behaving like a lost one, and the median winner needs another seven weeks of attention after
that point. **The active deals sit at a median of 66 days, so most of the current pipeline has not yet reached the
age at which deals start dying.**

### Win rate, by the person who owned it

| Owner | Active | Won + complete | Lost | Win rate |
|---|---|---|---|---|
| Olivier Dedek | 45 | 26 | 54 | **32 %** |
| Mark Franks *(left)* | 0 | 6 | 18 | 25 % |
| Neil Davidson | 2 | 2 | 2 | *50 %, n=4* |

**About a third of qualified deals close.** Read it as a base rate to plan against rather than a judgement on anyone
— and note that **Mark Franks holds no active deals, consistent with having left**, so 24 of his closed deals are in
the denominator with nothing in flight behind them.

### The deals are multi-brand already, and more so than history

**67 of 155 deals carry a component list, and 52 of those — 78 % — name more than one line.** Against the twelve-year
invoice record, where **44 % of dealers ever bought more than one line** (finding 2), **the current pipeline is
markedly more cross-brand than the historic base.** Whole-room selling is happening now, in the deals as written.

**What the deals are made of**, by component frequency:

| Component | Deals | | Component | Deals |
|---|---|---|---|---|
| Video | 14 | | Screen Wall | 5 |
| Acoustic treatment | 9 | | C-ATS | 4 |
| Screen | 9 | | Video processor | 2 |
| **Audio** | **8** | | Projector | 2 |
| Room fit-out | 6 | | Gold install | 2 |

> **`Audio` appears in eight live deals and the group has no own speaker line to put in them** (finding 17,
> `evidence/current-state.md`). **That is the Pro-Fi gap showing up as present demand rather than as history** — the strongest
> argument yet for the viability tier that puts Pro-Fi in step 3 before launch rather than after it.

## Finding 25 — 266 approved dealers, 62 current, 162 who never bought anything

Joining the Accounts board to the fifteen-year transaction record, on the same fuzzy name matching used in finding 6:

| | Count | Share |
|---|---|---|
| **Approved Dealers on the board** | **266** | |
| Matched to any purchase, ever | **104** | 39 % |
| **Flagged `Current Customer` on ≥1 brand** | **62** | **23 %** |
| Never matched to any purchase | **162** | 61 % |

Those 104 who did trade are worth **£4,583,030** of lifetime spend between them.

**Two things follow, and they point in opposite directions.**

**The approved network is three times larger than the trading one.** *"Approved dealer"* is an administrative state —
262 hold a signed SRND Group agreement — and **it has come loose from commercial reality.** Any count of "our
dealers" that uses 266 is overstating by about 4×. **§D's dealer-count metric should use `Current Customer` or a
purchase in the period, never the approved list.**

**But 162 approved dealers who have never bought are not a failure — they are a list.** They were qualified enough to
be approved and to sign an agreement; they have simply never been sold to. **Set beside finding 20 — that only 24–73
accounts have ever been *presented* any given brand — this is the same story from the other end**, and it is a
second reactivation list sitting alongside the 50 lapsed historic dealers of finding 7. **These ones have already
said yes to the relationship.**

*Matching caveat as before: fuzzy name joins, so 104 is a floor and 162 a ceiling.*

---

## Finding 26 — `In Engine` confirmed, and the two systems have drifted apart

*Checked against engine directly, at Neil's suggestion.*

### The stage name means what Neil expected

**`In Engine` means the deal has been migrated into engine as a project — it is not a sales stage.** Of the 34
deals in that stage, nearly all appear in engine's `projects` table by name, account and often exact value: *Evermore*
(Cornflake, £1,245,000 in both), *Komodo 4K* (£304,000 in both), *Cinema Hungary*, *Project LA*, *ABE6516 Hush Box*,
*JOLO fit-out*, *MMD-S NZ900*, *Skeisvang VGS*, *Project Stenton* and the rest.

**So the £3,480,152 sitting in `In Engine` is not deep-funnel pipeline — it is "everything we moved across."** The
sub-deals confirm it: **216 of 226 remain at `Proposal`**, because the sub-item statuses were never worked after the
migration. **Read the active pipeline as £4.13m of mixed maturity, not as £3.5m near the line.**

### But engine and Monday now disagree, and engine is the one that moved on

**Engine holds 58 projects; Monday holds 34 `In Engine` deals.** The gap is not migration lag — **engine contains
live work that never went back into Monday**: *Harehope* (£100,000), *Oman outdoor LED wall* (£175,000), *Voisins —
LED wall window display* (£162,800), *45 Park Lane — The Dorchester* (£50,000), *5880 Chalet Balagan* (£100,000),
*G12 Cinema* (£100,000), *Leadenhall projector replacement* (£59,000), *Pro-Fi project* (£60,000), *DYN-4-XXL*,
*Project Ziggy*, *Creed Farm*, *23Q Cinema fit-out* and more.

**And several deals Monday still shows as open are closed in engine:**

| Deal | Monday | Engine |
|---|---|---|
| The Grove Cinema | Active · In Engine | **won** |
| Ballroom project | Active · In Engine | **won** |
| Showroom | Active · In Engine | **lost** |
| Sylvox Cinema Pro 75" *(Tokyo TV)* | Active · In Engine | **lost** |
| Cinema Pro 75" *(Potters Home Digital)* | Active · In Engine | **lost** |

**Values disagree too:** The Shard £1,000,000 in Monday against £800,000 in engine; Galileo £187,000 against
£93,000; Focal demo Joppa £17,380 against £2,500.

> **The consequence is simple and worth acting on: the answer to "what is in the pipeline?" depends on which system
> you open, and Monday is the stale one.** Everyone works in engine now (`evidence/current-state.md`), so **engine is the
> live record and the Monday boards are a snapshot of the moment of migration.** Every pipeline figure in finding 24
> should be read that way — the win/loss counts and cycle times are sound as *history*, but the £4.13m "active"
> is not a current number.

### The accounts comparison — and "approved" means two different things

| | Count |
|---|---|
| Monday accounts, all groups | 1,658 |
| **Monday `Approved Dealers`** | **266** |
| Engine accounts | 348 |
| **Engine accounts with status `approved`** | **340** |
| Monday approved dealers **found in engine** | **225 of 265 — 85 %** |
| Monday approved dealers **absent from engine** | 40 |
| Engine accounts **absent from Monday entirely** | 80 |

**The carry-over is good — 85 % of approved dealers made it across.** The 40 that did not are a concrete list
(1install Group, AV6, Amplified Lifestyles, Boca Theater & Automation, Cinema Lusso, Genesis AV, Glo Audio Visual,
Holburn Hi-Fi, Heag Soluções and 31 more) and are worth a migration check rather than an assumption.

**But the two systems do not count the same population, and that is the thing to hold on to.**

> **▶ Corrected by Neil, 2026-08-14 — the account is the milestone, and it is a strict one.** *"No one can access
> pricing until they have an account. Literally signed and agreeing T&Cs. It's exactly the sort of unambiguous
> milestone we want. Note there are lots of potential states for accounts as that is where we try to track
> progress."*
>
> **My framing above was wrong in a way worth naming.** I read *"340 of 348 approved"* as evidence that `approved`
> had come loose from commercial reality. **It is the reverse.** Engine holds **only** accounts, an account exists
> **only** after signed terms, and signed terms are what unlock pricing — so **every one of the 348 is a partner who
> has agreed T&Cs.** That is not a soft category; it is the cleanest gateway in the business, and it is exactly the
> unambiguous milestone `motion/motion-design.md` asks the gateway signals to be built on (`JNY-1`).
>
> **And the many statuses are a feature, not drift** — they are where progress is tracked *after* the milestone, in
> both systems: engine's `pending → approved → active → suspended → non_trading`, and Monday's per-brand
> `Not Customer → Approached → Presented → Demonstrated → Current Customer` (finding 20).

**So the counts are not competing definitions of one thing. They are sequential milestones on one journey**, and the
right move is to report the whole ladder rather than pick a number:

| Milestone | Count | What it means |
|---|---|---|
| **Has an account** | **348** *(engine)* | **Signed T&Cs; can see pricing.** The unambiguous gate |
| Curated as an approved dealer | 266 *(Monday)* | A judgement laid over the gate |
| Has ever purchased | 104 | Converted at least once |
| Currently purchasing | 62 | Live trading relationship |

**Read that way it is a funnel with a clear diagnosis: the gate is passed 348 times and converts 104 times.** The
drop from *signed and able to see prices* to *ever bought* is the sales problem stated in one line — and it is the
same gap finding 20 shows from the presentation side.

### The milestone is dated in engine, but only from June 2026

| | Accounts |
|---|---|
| Accounts | 348 |
| With `terms_accepted_at` | **12** — all between 2026-06-09 and 2026-08-11 |
| With `approved_at` | 17 |
| With a signed terms document and signature image | 12 |
| With a pricing tier set | 18 |

**The signature exists for all 348** — it is how they got a record at all, via the Shopify form
(`evidence/current-state.md`) — **but the date of it only lives in engine for those who registered through engine's own flow
since June.** New-account creation is countable per month regardless (roughly 4–14, back to at least March 2025).

> **So the metric §D needs is already running and needs no new capture: accounts created per period, and of those,
> how many convert to a first purchase.** Both sides are in engine today. **The only thing missing is the signing
> date on the 336 migrated accounts**, which matters for cohort analysis and not for the forward count.

### The reconciliation that follows

**225 of 265 Monday approved dealers are in engine — 85 %.** The 40 that are not (1install Group, AV6, Amplified
Lifestyles, Boca Theater & Automation, Cinema Lusso, Genesis AV, Glo Audio Visual, Holburn Hi-Fi, Heag Soluções and
31 more) are **worth checking precisely because the account is a strict gate**: if they hold signed terms and no
engine account, they cannot see pricing. That is `MON-12`.

---

## Finding 27 — the growth is already inside the building

*Neil, 2026-08-14: "Key is that we just expose again how easily we could grow by simply actively working this
audience we have." This is that, costed.*

### The audience

| | Accounts |
|---|---|
| **Hold an engine account** — signed T&Cs, can see pricing | **348** |
| Matched to any purchase across fifteen years | 159 |
| **Signed, able to buy, and never bought** | **189** |

**189 partners have completed the hardest step in the whole funnel — agreeing terms — and then bought nothing.**
They are not prospects. They are not cold. They have signed.

### What one converted dealer is worth

From the fifteen-year record, 518 dealers with positive net:

| | Median | Mean | Upper quartile |
|---|---|---|---|
| **First twelve months** | **£4,470** | **£14,559** | — |
| Lifetime | £6,652 | £37,537 | £27,696 |

*The mean is pulled by the large accounts and the median by the long tail of one-order dealers; the truth for any
particular conversion sits between them, which is why both are carried below.*

### What 10–20 % growth actually requires

**Target: 10–20 % of 2025's £1,439,211 = £143,921 to £287,842.**

| Assumption | Conversions needed | As a share of the 189 |
|---|---|---|
| Each converts at the **mean** first year (£14,559) | **10 – 20** | **5 – 11 %** |
| Each converts at the **median** first year (£4,470) | 32 – 64 | 17 – 34 % |

> **So the whole growth target is between ten and sixty-four first orders, from a pool of 189 who have already
> signed.** On the pessimistic reading it needs a third of them; on the optimistic, one in twenty. **Neither is a
> campaign. Both are a list and a reason to call.**

### And it is not the only pool

Three other audiences the archive has already named, none of them cold:

| Pool | Size | Evidence |
|---|---|---|
| Signed accounts that never bought | **189** | this finding |
| Lapsed dealers still trading in 2021–23, no engine account | **50**, £2.33m historic net | finding 7 |
| Monday approved dealers never matched to a purchase | 162 *(overlaps the 189)* | finding 25 |
| **Approved dealers with signed terms and no engine account** | **40** | finding 26 |

**Set against finding 20 — only 24 to 73 accounts have ever been *presented* any given brand — these pools are not
a mystery.** The reason 189 signed partners have not bought is visible in the same CRM: **most of them were never
shown anything.** *"No one can buy what they don't even know exists"* (Neil) is not a metaphor here; it is the
recorded state of the account base.

### ▲ And the 40 are urgent, not tidy-up

**Neil, 2026-08-14: "Those 40 are probably some of our key people so some gap has appeared we need to address."**

Because the account is a strict gate (finding 26), **an approved dealer with no engine account cannot see pricing at
all.** If they are key people, the gap is not administrative — **it is a live inability to buy**, sitting quietly
across a migration boundary. `MON-12` carries the list; this raises it from a reconciliation to a fix.

### What this changes in the plan

**Nothing in the strategy, and one thing in the ordering.** `NEXT.md` already puts the record and the corpus first
because content is the rep. **This finding does not dispute that — it prices the alternative.** The record work
compounds and is the durable answer; **working the existing audience is the fastest £150–300k available**, needs no
new capture, no new content and no new system, and the plan's own test — *does this ride on something already
happening?* — it passes outright, because the accounts, the pricing access and the CRM statuses all exist.

**The honest statement of the trade-off:** the audience work buys time and revenue; the record work buys the ability
to do it at scale and without the owners in the room. **They are not competing for the same hours** — one is sales
activity, the other is documentation — **which is precisely why both can run, and why `MON-6` sits in the plan
already.**

---

## Finding 28 — Mailchimp: reach is solved, targeting does not exist

*Pulled from the Mailchimp API 2026-08-14 (`data/fetch_mailchimp.py`; datacentre us7). Source files in
`data/source/mailchimp-*.json`.*

### What is there

**One audience, not six.** `SRND Group Ltd` — **2,027 subscribed**, plus 446 transactional, 244 cleaned and 126
unsubscribed: **2,844 records.** Opt-in dates are **2025 (2,513) and 2026 (323) only**, so the list was built in
2025 and carries no older history.

**29 campaigns sent, 2025-06-30 to 2026-04-16.** Mean **723 recipients** per send, though the newsletters reach
1,600–1,982 and a `DT Distributor Highlights` segment reaches exactly 23.

| | Mean | Median |
|---|---|---|
| Open rate | **56.4 %** | 54.1 % |
| Click rate | **3.1 %** | 2.9 % |

**Read the click rate, not the open rate.** A consistent 50–55 % open across every single campaign is the signature of
**Apple Mail Privacy Protection auto-opening messages**, which has inflated open rates industry-wide since 2021. The
**3.1 % click rate is the honest engagement number, and it is ordinary for B2B** — neither a triumph nor a problem.

### The question this was pulled to answer

**Have the signed-and-never-bought accounts ever actually been emailed? Yes — almost all of them.**

Joining engine's 348 accounts to Mailchimp on **email domain** (338 accounts carry an identifiable business domain;
free-mail domains excluded):

| Engine accounts | On the mailing list |
|---|---|
| **No order in engine** — 301 | **295 — 98 %** |
| Ordered in engine — 37 | 33 — 89 % |

**Only six accounts are absent from the list entirely** (Adeo Group, Consult Acustic, Delta Pelio, IAC Acoustic, LCG
Intégration, Zene Private Theaters).

> **A correction to my own first pass, because it gave the opposite answer.** Matching on the `COMPANY` merge field
> suggested only 13 % of never-bought accounts were on the list. **That join was too weak to use** — just 1,233 of
> 2,844 members have a company recorded at all — and matching on email domain, where coverage is near-complete,
> reverses it. **The lesson is worth keeping: on this dataset, join on domain, never on company name.**

### So the diagnosis changes — and sharpens

**The problem is not that the audience has never been contacted. It is that it has never been *targeted*.**

**There is no working brand segmentation in Mailchimp.** The brand tags exist and are used on **one member each**:

| Tag | Members |
|---|---|
| B2B | 277 |
| show restricted pricing | 238 |
| Login with Shop / Shop | 164 |
| ISE2026 | 156 |
| No Barco | 117 |
| **CATS · DT · FWALLS · LWALLS · SRND** | **1 each** |

**So Monday's per-brand subscribe flags — DT 926, C-ATS 191, Fabric Walls 193, Light Walls 195, Pro-Fi 193
(finding 21) — have no counterpart in the system that actually sends the mail.** Everyone gets the group newsletter;
nobody gets a brand proposition.

**Set against finding 20, the two sources now agree from opposite directions.** Monday says only 24–73 accounts have
ever been *presented* any given brand. Mailchimp says 98 % of accounts receive the general mailing. **Broadcast reach
is solved; brand-specific presentation does not happen.** That is a much more tractable problem than an
uncontacted audience, and it reframes `MON-14`: the 189 do not need finding, they need **segmenting and presenting**.

### Two things worth acting on

**1. Nothing has been sent since 2026-04-16 — four months.** `NEXT.md` lane 6 names its stall signal as *"a month
with no publication."* **This is four**, on a list of 2,027 with a 54 % open rate. The audience is warm and idle.

**2. ▲ A brand-truth breach, dated and sized.** Two campaigns in January and February 2026 went out as
**"ISE 2026: Introducing Pro-Fi Spatial Audio Series"** (1,633 recipients) and **"Pro-Fi Spatial Audio Series -
Small Speakers…"** (1,622), plus **"Pro-Fi Speakers Impress at ISE 2026"** (1,581 + 287). `registers/open-items.md` already
records *"Pro-Fi described as SRND Group's dedicated spatial audio brand"* as a **live contradiction that Pro-Fi's own
voice code forbids** — the phrasing was flagged from the group site. **It also went to the mailing list, three times,
to roughly 1,600 people each.** The flag stands; this gives it dates and reach.

*Also visible and consistent with the archive: Pro-Fi has had more campaign airtime than any other brand while being
pre-revenue with no shipping speaker line (finding 17).*

---

## Finding 29 — the click detail, which is the first real demand signal in the repo

*Pulled 2026-08-14: `data/source/mailchimp-click-details.json`, **416 URL records across all 29 sent campaigns.**
Aggregate open and click rates say how many people engaged; **these say what they engaged with**, and that is the
question `motion/content.md` and lane 6 have never had an answer to.*

### Where the clicks went, by destination

| Destination | Unique clicks |
|---|---|
| **srnd.store** | **946** |
| **tidycal.com** — booking a call or a factory visit | **226** |
| fabricwalls.uk | 195 |
| **YouTube** (`youtu.be` + `youtube.com`) | **231** |
| displaytechnologies.co.uk | 191 |
| srnd.group | 170 |
| pro-fi.uk | 86 |
| facebook.com · linkedin.com | 88 · 54 |
| **c-ats.co.uk** | **6** |

### The most-clicked individual links

| Unique | Total | Link |
|---|---|---|
| **219** | 258 | `srnd.store/collections/barco-heimdall` |
| **179** | **652** | `fabricwalls.uk` — the new-site announcement |
| **82** | 345 | **`tidycal.com/srnd-neil/srnd-group-factory-visit`** |
| 71 + 60 | 163 | ISE 2026 booking calendars |
| 65 | 70 | `pro-fi.uk` |
| 57 · 34 · 33 | | three YouTube videos |
| **53** | 55 | **`srnd.store/pages/trade-account-partner-application`** |
| 43 | 115 | `srnd.store/pages/immersive-environments` |
| 40 | 42 | `srnd.store/products/dynamic-2s-side-masking-projection-screen` |

### Five things this says

**1. C-ATS received six clicks in twenty-nine campaigns.** Against 946 to the store, 195 to Fabric Walls and 191 to
DT. **This is the "massively undersold" diagnosis with a mechanism attached** — not that the audience rejected C-ATS,
but that **almost no email ever pointed at it.** Finding 20 said only 49 accounts were ever *presented* C-ATS;
finding 28 said the brand tag carries one member. **All three sources now say the same thing, and this is the
cheapest of them to fix.**

**2. The single most-clicked link in the whole dataset is a carried projector** — Barco Heimdall, 219 unique. **The
audience pulls hardest on 20 %-margin product** (finding 22), which is the demand-side face of the margin ladder. It
does not mean stop selling Barco; it means **the pull that exists is currently aimed at the least profitable rung**,
and no equivalent own-made hook has been offered.

**3. Booking links are the second-biggest destination — 226 clicks, of which 82 unique for a factory visit.**
`NEXT.md` lane 1 calls the Experience Centre *"disproportionately important… the one room we can show, film and
measure freely."* **This is the first evidence for that claim rather than argument** — a link to book a visit
out-pulls every product page except one. **High-intent, and it costs nothing to include.**

**4. YouTube drew 231 clicks across a handful of videos.** Lane 6's *"record, don't write"* rests on the eight-year
channel history and the ~9,500-view C-ATS explainer. **Emails that point at video get clicked**, which supports the
cheapest content format the group has.

**5. The trade-account application drew 53 unique clicks.** That is the strict gate from finding 26 — signed T&Cs,
pricing access — **being clicked 53 times from email alone.** Worth reconciling against how many accounts were
actually created in the same window: **engine shows 4–14 new accounts a month**, so the application link is
plausibly a material share of new-account origin, and it is the one link that directly advances the milestone
`NEXT.md` §D now measures.

### And the best-performing campaign was a website launch

*"The New Fabric Walls Website Is Now Live"* (2026-04-16) reached **1,982 recipients** — the widest send — at a
**63 % open rate, the highest of the 29**, and produced **652 total clicks to fabricwalls.uk, the highest of any
link.** It is also **the last campaign sent.** `MON-16` already flags the four months of silence since; this says the
silence began immediately after the best result the list has produced.

*Caveat carried from finding 28: open rates are inflated by Apple Mail Privacy Protection, so compare campaigns on
clicks. The click figures above are unaffected.*

---

## Finding 30 — the pattern, and it runs the opposite way to the one the repo names

*Not new data. The same shape, counted across everything measured on 13–14 August 2026, because eight instances of
one thing is a finding and eight separate findings are a list.*

**`CLAUDE.md` names the group's characteristic failure mode as "build it, then say it"** — announcing something not
yet practised — and records it surfacing three times: dealer appreciation, the partner programme, and the whole room
being genuinely easier to buy.

**Everything measured this week is the same gap running the other way: built, and never said.**

| Built | Never said | Evidence |
|---|---|---|
| C-ATS record filled, copy written, **BSRIA report published** | **6 clicks in 29 campaigns**; 49 accounts ever presented it; brand tag on one member | findings 20, 28, 29 |
| A mailing list of 2,027 at a 54 % open rate | **Best campaign ever sent was the last one sent** — four months of silence | findings 28, 29 |
| **348 partners with signed T&Cs and pricing access** | **189 never sold anything**; 24–73 accounts ever presented any brand | findings 20, 27 |
| 266 approved dealers, 262 with signed agreements | **62 currently trading**; 162 never bought | findings 25, 26 |
| Engine's document-generation layer, staleness flags, coverage rules | **Not mentioned anywhere in the plan** until it was audited | `evidence/engine-audit.md` |
| Engine's question → answer → gap mechanism, 257 topics | Pointed at engine's own UI, never at products | `evidence/engine-audit.md` §2 |
| A new Fabric Walls website | Announced once, brilliantly, then nothing | finding 29 |
| **40 approved dealers** | **Cannot see a price at all** | finding 26 |
| Monday's per-brand subscribe flags — DT 926, C-ATS 191 | **Never reached the system that sends the mail** | finding 28 |

**So the failure mode is not over-claiming. It is under-telling** — and the two are opposites with the same root: a
gap between what is true and what has been said. **`CLAUDE.md`'s rule guards one direction and the measured evidence
runs the other**, which is worth a line in the steering document rather than a finding buried here. *Flagged in
`registers/open-items.md`; not edited unilaterally.*

**Why it matters more than a tidy observation.** Every entry in that table is **cheap to fix and already paid for.**
Nothing needs building, buying or hiring: the record exists, the list exists, the accounts exist, the mechanism
exists, the report is published. **This is the arithmetic behind finding 27** — the growth target is 10 to 64 first
orders from people who already signed — **and behind Neil's own diagnosis: *"no one can buy what they don't even know
exists."***

> **The one-line version, for whoever reads this file next: the group's problem is not capability and it is not
> demand. It is that the work stops one step before anybody hears about it.**

---

> **Restored 2026-08-17.** Findings 31 and 32 below were deleted entire in the 2026-08-17 restructure
> under the evidence-may-not-argue rule; the cut removed the measured content along with the argument, and the
> repo still cited both. Restored verbatim from git history on Neil's challenge; internal file paths within
> them predate the six-area restructure.

## Finding 31 — service revenue was identified but never opened, and the prices were in it all along

*Asked by Neil, 2026-08-15: was service revenue identified in the revenue work? **Yes — and only as a bucket.***
*No new source; this is the loaded data queried a second time, prompted by a live decision it turns out to
answer.*

**The consolidated file has carried a `services` value in its `supply` column since it was built**, and finding
15 used it — but only to report **one number for one entity**: services at 9.0 % of SRND Group. **The group
total was never stated, and the bucket was never broken down.**

**The group total is £672,915 across fifteen years, on 153 invoice lines:**

| Kind | GTUK | SRND Group | C-ATS | Total |
|---|---:|---:|---:|---:|
| **Unlabelled** — nominal says only *"Services"* | £376,977 | £45,000 | — | **£421,977** |
| **Design** | — | £96,076 | £49,662 | **£145,738** |
| **Fit-out** | — | £62,495 | — | £62,495 |
| **Install / commissioning** | — | £39,005 | — | £39,005 |
| **Project management** | — | £8,750 | — | £8,750 |
| Payment mechanics (advances, reversals) | — | −£5,050 | — | −£5,050 |
| **Total** | **£376,977** | **£246,276** | **£49,662** | **£672,915** |

**DT and Light Walls carry no service lines at all**, so services are a GTUK, SRND and C-ATS phenomenon.

**63 % of it cannot be read, and it is almost entirely the distribution era.** GTUK's export shape carries no
description, and its nominals say only `Sales - SERVICES` and `Sales - CINEMA PARTNERS SERVICES`. **So
£376,977 of service revenue is opaque without a re-export — the `MON-11` problem again, in a different
account.** *(C-ATS's lines carry no description either, but its nominal is specific — `Sales - Design Services`
— so they classify on the account name alone.)*

### What the readable 37 % contains, and it changes a decision that was open this morning

**Named services, already invoiced, at real prices:**

| Service | Invoiced | Year |
|---|---|---|
| **Acoustic Treatment Design Service — Basic** | **£3,000** | 2026 |
| **Sound Isolation Design Project** | **£7,500** | 2025 |
| Fabric Walls room design — Seattle | £13,068 | 2025 |
| Fabric Walls room design — Madrid | £6,480 | 2026 |
| Light Walls pixel layout, one rectangular room | £750 · £505 | 2025 |
| Installation support, **per day** | £4,800 | 2025 |
| Commissioning support, SRND display products | £1,000 | 2025 |
| Reference audio calibration | £838 | 2025 |
| Leyard Gold tier — commissioning, assisted install, on-site | £6,000 · £5,040 | 2026 |
| Cinema fit-out (Kildrummy) | £45,450, plus £12,500 interim and £4,545 of design | 2024–25 |
| Consulting — project design phase | £5,000 | 2023 |
| System design and schematic layouts, CAD/PDF | quoted **per hour** | 2025 |

**Forty-one design engagements: median £2,400, mean £3,580, range £260 to £29,195.** C-ATS's own twenty-two run
at a **median of £1,560**, almost all to Apex-Tech.

### Three consequences, all landing on items open right now

1. **Over-claimed, and corrected by Neil, 2026-08-16:*"Other than C-ATS the service was all
 ad hoc. We have a pretty good idea what a service offer should be overall, but documenting it and pricing it
 is a dedicated session."***
 **So the accounts are precedent, not a price list.** The C-ATS exception is visible in the data and is the
 one that proves the rule — a dedicated `Sales - Design Services` nominal running from 2019, **22 engagements
 at a median of £1,560**, which is a repeated service. **Everything else — the Fabric Walls room designs, the
 fit-out, install support by the day, commissioning, calibration, project management — was priced job by
 job.** What the history gives the pricing session is **a range and a set of real precedents**; what it
 cannot give is an offer, because there wasn't one.
 **This makes the underlying finding stronger, not weaker.** **£672,915 was earned with no service offer,
 no published price and no promotion** — ad hoc, on demand that arrived anyway. *And it explains
 `XS-4`'s answer exactly: "terrible at working out what is paid work and what is free" is what necessarily
 happens when there is a boundary but no offer to apply it to.*
 **Re-scoped: `XS-5` is a dedicated session, not a small read-and-ratify.**
2. **The group sells more services than the strategy describes.** Fit-out, installation support by the day,
 commissioning, calibration and project management are all real invoiced revenue and **none appears in the
 paid-services list** — because that list was assembled from strategy documents and this is the accounts.
 **Fit-out is the striking one: £62,495 of it, and the repo does not describe the group as doing fit-out at
 all.**
3. **Services are not marginal, and 2025 was the biggest year on record.** £149,284 (2022) · £74,774 (2023) ·
 £34,925 (2024) · **£178,472 (2025)** · £37,876 (2026 part-year). **In the current entity services are the
 third-largest revenue class after carried and own-made** — which puts a number behind `current-state.md`'s
 *"design work is real revenue and expected to grow with verification attached."*

**Two caveats on the totals.** The bucket has noise — **at least one product sits in it** (a £6,646 video
processor, inside SRND's unlabelled £45,000) — and the kind-splitting above is keyword classification of
descriptions and nominals, reviewable and not authoritative. **Neither affects the conclusion**, which is about
what exists rather than about the last few thousand pounds.

> **And the shape of this is familiar.** The number was in the file, correctly classified, and used once for a
> percentage. **A smaller instance of finding 30** — not built and never said, but *measured and never read* —
> and worth noticing because the fix was one query prompted by somebody asking a live question of the data.

### The margin ladder was missing its top rung — Neil, 2026-08-15

*"Services are 100% margin effectively — think on that."* **So finding 23's ladder is incomplete**, and the rung
it is missing is the highest one:

| Route | Steps held | Margin |
|---|---|---|
| Carried line (Leyard) | distribution only | 20 % |
| Own-made through a distributor | manufacture | 37.5 % |
| Own-made direct to a dealer | manufacture + distribution | 52.4 % |
| Own-made direct to a consumer | all three | 66.7 % |
| **Services** | **no goods to make, buy, hold or ship** | **≈ 100 %** |

**The equivalences are the part worth sitting with:**

- **£672,915 of services is the margin of £3.36m of carried revenue**, or £1.28m of own-made sold direct.
- **One median design engagement — £2,400 — earns what a £12,000 Leyard order earns.**
- And in the current entity, **2025**: services **£178,472** against carried **£385,652** and own-made
 **£485,754**. At the ladder's rates that is **£178,472 of margin from services, £77,130 from carried,
 £254,535 from own-made** — so **services were 35 % of the group's gross margin on 17 % of its revenue, and
 earned more than twice what the entire carried book earned.**

**Which reframes several things that were argued on other grounds:**

1. **The free/paid boundary is now the most expensive open item in this repo.** Free pre-sales is not
 generosity — **it is the group's highest-margin product, given away.** Every median engagement done free
 forgoes the margin of a £12,000 order. *How many happen is unknown* (`current-state.md` **[?]**), and it has
 just become the most valuable unknown on that page.
2. **It vindicates the no-credit-against-the-order call** (2026-08-15) **with arithmetic the session did not
 have.** Crediting a £3,000 fee converts 100 %-margin revenue into revenue at 52.4 %, so the credit must win
 roughly **£5,700 of incremental own-made order just to break even.** *The recommendation to credit it was
 wrong, and the instinct that overruled it was right.*
3. **The attach metric is aimed one rung too low.** Q5 measures own-made attach on carried sales — but
 **service attach earns about twice as much per pound and needs no product to exist**, and it already
 happens: Leyard Gold-tier commissioning at **£5,040–£6,000** against Komodo orders. On a £472,320 Komodo
 year, **the best attach is not a Screen Wall; it is commissioning and calibration on every one.**
4. **It is the strongest business case yet for filling the record.** The record turns a repeated answer into a
 published one — **which converts hours from unpaid answering into paid design.** Not "fewer support calls":
 *the highest-margin capacity in the business, freed.*
5. **Acoustic verification is the un-sold service with the best economics.** It is the only one of the four
 never invoiced, and it attaches to every design, is measurement-based (so repeatable and tool-supported),
 carries no goods, and is the thing that proves the product worked.

**Three honest qualifications, because the number invites over-reading:**

- **100 % is gross, and the input is the binding constraint.** Services consume owner and engineer hours — the
 exact resource the whole strategy is short of. **So services are simultaneously the highest-margin and the
 least scalable revenue**, and the useful conclusion is not *sell more services* but **an hour of design is the
 most valuable hour in the business, so anything else competing for it must clear that bar.** That is an
 argument for the record and the tooling, which are what make an hour of design produce more design.
- **Split the rung: desk services are near-100 %, on-site services are not.** £4,800-a-day installation support
 carries a person and their travel; a design produced against a tooled engine carries almost nothing.
- **The n is small and the years are lumpy.** Forty-one design engagements across fifteen years is about three
 a year, and **2025's £178,472 is substantially one job** — Kildrummy at £57,950 including the interim. Read
 it as *what a service pound is worth*, not as a trend.

### Checked against the live site — `cinema-tools.com`, 2026-08-15

*Neil pointed at it. Per `CLAUDE.md`'s check-the-platform rule, and it corrects this finding as well as the
strategy.*

> **▲ Context that changes how everything below should be read, and it arrived after the observations were
> written: the site went live two days ago, forced — the old one was hacked** (Neil, 2026-08-15). **So this is
> a two-day-old emergency rebuild, not a settled surface**, and the gaps listed further down are a launch
> punch-list rather than decisions anyone made. *Recorded as a correction to my own framing, and as an instance
> of the error `06-competitors.md` opens by warning about: reading a published surface as though it reflected
> settled intent.*
>
> **Two things follow, and they pull opposite ways.**
>
> - **The service architecture is now more impressive, not less.** Four coherent tiers were articulated under
> emergency conditions in two days, and they are **better than the version this repo derived deliberately
> over weeks.** Where the strategy documents produced a C-ATS-shaped list, the forced rebuild produced the
> right group-level one. **That is worth noticing about where the truth actually lives.**
> - **But it is live now, so the capture gap is costing from today.** Every day the seven PDFs download without
> an email and both forms post to a mailbox, leads for the group's **highest-margin product** arrive
> uncounted. **Not a criticism of the launch — a reason the punch-list is urgent rather than tidy.**
>
> **And one question the hack raises that is not in the list below: what happened to the discoverability?**
> `NEXT.md` lane 8's firm rule is *restart the presentation, never discard the discoverability* — URLs, indexed
> pages, accumulated search position. **A forced rebuild is exactly the circumstance in which that gets lost by
> accident.** Worth establishing whether the old URLs still resolve and what, if anything, went with the old
> site. *(The group already carries one estate loss of this kind — the locked YouTube account.)*

**The service is already articulated publicly, at group level, and better than this repo's version of it.**
`cinema-tools.com/project-support/` sells **four named tiers, individually or as a full sequence**:

| Tier | What the site says it is |
|---|---|
| **Design review** | A remote review of a room, drawings, or a space the client is considering — what the room needs to meet, where it stands, what it would take |
| **Performance design** | A full specification: audio, video, acoustic treatment, finishes, lighting, seating and services |
| **Calibration** | Levels, delays, EQ and bass management; brightness, colour and gamma |
| **Verification** | Measuring the finished room against the targets it was designed to, and documenting the result |

**Three corrections to what is written above and in `group/13-standards-decision-sheet.md` session 2:**

1. **The service architecture is whole-room and group-level, not C-ATS-shaped.** The paid-services list was
 assembled from strategy documents and came out as acoustic design / acoustic verification / isolation
 design / isolation verification. **The live one is the better model** and the strategy should adopt it.
2. **Verification is offered, and has still never been invoiced.** *"The un-sold service with the best
 economics"* is right and the sharper form is: **it is on sale, publicly, and has never sold once.**
3. **"Design review" is the missing first rung** — a low-commitment paid entry that is the direct paid
 equivalent of the free spec help the boundary decision is about. **It already exists; nobody knew.**

**And three gaps at the same joint — a launch punch-list, not a set of decisions** (see the context note
above; the site is two days old and was forced by a hack).

- **The free calculators capture nothing.** Seven tools, each producing an A4 PDF, and **no form and no email
 field anywhere on the page** — the PDF downloads unconditionally. **ADR 020 specifies lead capture on PDF
 download landing in engine's `leads` table, and `07-tools.md` calls that trade "the on-ramp hinge in product
 form." It is not happening.**
- **Both enquiry forms are `mailto:`** — *"This opens a completed email in your own mail client."* So the
 group's own lead-magnet front door delivers its best-qualified leads **into a mailbox, not into engine.**
 That is `14-engine-as-hub.md` §1's *"inbound is currently uncountable"* made concrete on the one page
 designed to generate it.
- **No prices, on any tier.** Consistent with the gated-pricing rule for products — but the boundary decision
 of 2026-08-15 was **published**, and a dealer currently cannot tell what a design review costs. **The service
 invoice history is the answer** (`XS-5`).

**The site itself is good, and the bounded-tool discipline is being kept.** The Room Resonances calculator
states its own limits plainly — *"assumes a rigid rectangular room… surface treatments, damping and RT60 need
physics-grade material data that this calculator does not ask for"* and *"optimising sub placement numerically
is design work"* — which is exactly `07-tools.md`'s three tests, passed. **Under emergency conditions, and
that is the more impressive version of it.** So the shop window for the highest-margin product in the group is
well built and honest; **what it does not yet have is prices, capture, or a form that posts anywhere but a
mailbox** — and those are finishing work on a two-day-old build.

*Two smaller observations, recorded rather than actioned: the reflection-point calculator `07-tools.md` names
as the obvious gap is **still missing** from the set of seven; and the site is attributed personally —
"Cinema Tools was created by Neil Davidson, one of the owners of SRND Group" — which is a credibility choice
worth being deliberate about against the master-brand rule.*

### And the platform repo already holds most of this — checked 2026-08-15

*Neil: "now you can look into the cinema platform repo at cinema tools pro." **The check-the-platform rule
earning its place again** — and this time what it finds is not a gap but a duplication.*

**`ADR 017` was revised to version 2 on 2026-08-13, five days ago, consolidating five ADRs into one — 001, 014,
019 and 073 all fold into it.** `group/07-tools.md` cites **ADR 019**, which no longer exists as a separate
rule. *That document's own header warns it once "leaned on ADR 014, whose substance had been retired." **It has
happened again**, which suggests the citation should be to 017 alone and re-read rather than pinned.*

**Five decisions in the current ADR 017 that this repo either does not hold or contradicts:**

| ADR 017 v2 | What it says | What this repo says |
|---|---|---|
| **Decision 4** | **Cinema Tools Pro is internal tooling.** No external user logs into it; **its purpose is "to make the method reproducible by fewer people in less time."** | Nothing. Pro appears nowhere in the group strategy |
| **Decision 10** | **"Four revenue lines carry the business — training, design services, the partner channel, product."** | Product is the business; services are a `[?]` in `current-state.md` |
| **Decision 9** | The free calculators exist to put qualified people in the funnel, **"which makes lead capture launch-blocking"** (mechanism: ADR 011) | `07-tools.md` calls capture the on-ramp hinge, but not a launch gate |
| **Decision 3** | *"Commercial cinema is the **lead market**"* — **the ranking is rejected, not the market** (Neil, 2026-08-15). See the note below | High-end **residential** cinema is the heartland and day 1; commercial cinema is real upside, later |
| **Decision 12** | **Demand is measured before the curriculum or the partner programme is built** — calculator traffic first, then one module published to see who buys | The partner programme is designed and awaiting build; no measure-first gate |

**On decision 3 — it is the ranking that is wrong, not the market.** Neil, 2026-08-15: *"There is a lot of
business opportunity in commercial cinema. It's just not the day 1 target above all other things."* **So this
is a sequencing correction, and it should not be recorded as a scope one.**

- **The archive cannot speak to opportunity, only to history.** It carries no market-type field and shows no
 commercial cinema revenue in fifteen years — **but absence of past revenue is not absence of a market**, and
 reading it that way would be precisely the inference error `06-competitors.md` opens by warning about.
- **What the archive does settle is where day 1 is, and it is not a market at all.** **348 partners hold signed
 T&Cs and pricing access; 189 have never bought** (finding 27), and the 10–20 % growth target is 10 to 64
 first orders from inside that base. **Day 1 is the base already signed** — which beats any new market on
 cost, certainty and speed, commercial cinema included.
- **And the group's existing position already has a slot for it.** `NEXT.md` is explicit that the group will
 not remain a cinema-only trade supplier, that the adjacent markets are larger, and — lane 1 — that
 **commercial and hospitality clients often want the publicity**, so a first commercial room *"may be worth
 more as a showable reference than as revenue."* **In a market where the best residential work is unshowable,
 that is not a small thing.** Commercial cinema belongs in that upside, not in the day-1 slot.
- **The capability is already being built toward it**, and correctly: commercial-Atmos reach, the cabinet
 catalogue, the CLA layouts, the full RP22 scorecard. **Building the engine ahead of the market is fine.
 Sequencing the go-to-market ahead of the signed base is not.**

*So a reissued ADR 017 does not need to lose the commercial ambition — it needs to demote "lead market" to a
named future market, which also leaves ADR 021's engine work standing on its own competitive argument.*

**What it touches, checked rather than assumed — and it is nearly nothing.** The phrase *"lead market"* appears
**exactly once in the whole platform documentation set**: ADR 017 §3 itself. Nothing cites it. **One
dependency exists and it is live:** **ADR 021** — the commercial-Atmos engine, revised to **version 3 on
2026-08-14** — opens *"Implements: ADR 017, **which promoted the commercial-Atmos / DARDT-replacement path to
the primary product surface**."* **So one actively-worked ADR hangs its priority off the struck line.**

**The engineering does not move at all.** Commercial-Atmos reach, the cabinet catalogue and the CLA layouts are
**engine depth**, and their justification is competitive — **replacing DARDT** — not market-size. **What
changes is the sentence explaining why 021 is first, not the value of anything it built**, and the capability
is what makes the commercial upside reachable when it is wanted. *Whether ADR 017 is reissued at version 3 with
§3 demoted, and whether 021's "Implements" line is restated, is Neil's call in the platform repo — ADR 079 says
ADRs are versioned, not amended, and neither file has been touched from here.*

**And decision 4 is the answer to the constraint this finding raised.** The margin note above concluded that
services are the highest-margin and least scalable revenue, so the useful move is *making an hour of design
produce more design.* **That is Cinema Tools Pro's stated purpose, already built and running.** The lever was
identified from the accounts this afternoon and has existed as a platform decision since at least June.

**Which is the real headline of this check.** `docs/product/08-service-lines.md`, **proposed 2026-06-03**,
already says what finding 31 derived from fifteen years of invoices today:

> *"Boutique design services — the cashflow and the wedge… **Highest margin, lowest infrastructure risk,
> near-zero customer-acquisition cost.**"* And: *"**the design fee is the smallest number in the deal**"* — the
> recurring lifecycle tail is the prize the design buys.

*(That document names a specific product chain for the tail. **One of the three named carries no commercial
value** — Neil, 2026-08-15 — so the chain is not reproduced here; **the argument survives it**, since
configuration and commissioning are real and recurring on their own. See the correction in
`group/07-tools.md`.)*

It also settles a boundary the group repo has never stated: **SRND owns the design, the IP and the client
relationship; partners own the install** — *"the design authority at the top of the market, with the partner
network as the delivery arm, not a competitor."*

**So the two repos reached the same place from opposite directions** — the platform from strategy in June, this
one from the accounts in August — **and neither knew.** *That is not a contradiction to resolve; it is
corroboration, and the strongest kind, because the methods were independent.* **The action is to stop
re-deriving: `group/07-tools.md` should read from the current ADR 017 and `docs/product/` rather than restate
them.**

**One thing all three sources agree on by omission: there is no price list anywhere.** Strategy repo, platform
docs and live site all carry exactly one price — **the £500 Pro Design escalation**, which
`docs/product/08-service-lines.md` is careful to define narrowly as *"a review of a partner's tool design"*,
not a design service. **`XS-5` therefore stands, and the invoice history remains the only source of prices the
group has.**

**And one live tension, flagged for Neil rather than resolved.** ADR 017 decision 10 makes **training a revenue
line**; the standards run on 2026-08-15 set training as **free to registered partners**. Those do not
obviously agree. *Neil noted at the time that he would be "introducing another later tomorrow that impacts on
this" — ADR 073's superseded text, folded into 017, is about **Cinema Expert**, an independently accredited
cinema credential reoccupying ground CEDIA abandoned. That is very likely the thing, and it would resolve the
tension by making training a product with a partner-facing tier rather than either/or.*

---

## Finding 32 — the future the archive cannot see: LWCP, reviewed 2026-08-15

*Neil: "one more for you to fill the future gap as well as history. Please review the LWCP repo." **The archive
measures fifteen years of what was sold. This is the only thing in the group large enough to change what gets
sold next, and the strategy repo currently records it as dormant.** Read-only review of `d:/dev/lwcp` — README,
`docs/STRATEGY.md`, `docs/PRODUCT-TIERS.md`, ADR summaries and the git history. No files were modified.*

### 1. It is not dormant, and it is not a fixture brand

`NEXT.md` places Light Walls in the **Hold** tier — *"stopped in 2023 pending the replacement approach"* — and
"Deliberately not now" says **"nothing to plan here until that lands."** **It has landed.** Architecture and
commercial strategy are settled, the software layer is end-to-end exercisable, **freedom-to-operate is cleared
on the two patents that threatened the moat**, and the git history runs to **2026-08-02** — a fortnight ago,
with a whole dynamic-content workstream (`F1`–`F4`, `G1`) merged after the README's own "parked" note.

**But the more important correction is what it became.** A posture update dated **2026-07-17** re-weights the
whole thing:

- **Per-pixel demotes from headline to feature.** *"~98 % of the professional lighting market is non-pixel and
 mostly white."* **Calibrated white is the volume P&L; pixel — Light Walls — is the halo that proves the
 colour science.**
- **The unit of product is the driver plus its measured profile, not the fixture.** Own light demotes to a
 reference engine.
- **LWCP is a lighting control system**, competing with **Lutron, Rako, Crestron, Control4** — not with tape
 vendors.

**So "Light Walls" is now one tier of a platform, not a brand being restarted.** Tier 1 retrofit/event · Tier 2
DT8 architectural luminaire · **Tier 3 full system, which is where the Light Walls name lives.** Same hardware
throughout; tiers separated by firmware flags and licensing.

### 2. Three things the group strategy has no account of at all

**a. A fourth revenue shape — licensing.** Finding 31 put services at ≈100 % margin above product. LWCP adds
**software licensing**: the design tool seat- or project-licensed, Path B enablement licensed per install, tier
gating by firmware flag. **Same hardware, three price points, differentiated in software** — and Tier 3 ships
**commissioning and calibration as part of the deliverable**, which is precisely the lifecycle service tail
`cinema-platform`'s `08-service-lines.md` calls the recurring prize. *The group repo has no concept of licence
revenue anywhere.*

**b. Prices, written down.** *"There is no price list anywhere"* was the conclusion three sources ago. **LWCP
has indicative pricing**: master receiver **£150–300**, coordinator **£800–2,500** by SKU, and a typical
high-end residential cove install at **£4,000–8,000** — positioned below Ketra and against Color Kinetics and
Lumaris. **Which sharpens the pattern rather than contradicting it: the numbers live in the product repos, and
the strategy repo is the only place that doesn't have them.**

**c. A competitor set that does not appear in `06-competitors.md`.** Lutron (Lumaris and Ketra), Color
Kinetics, Traxon, Anolis, Lumenpulse, Saco, Advatek, Pharos, ENTTEC, Madrix, Dresden Elektronik, Philips Hue —
each assessed for what it does well. **Session 5's roster ask did not even list Light Walls as a brand needing
names.** *It needs them least of all: it already has the best competitor document in the group.*

### 3. The group-level consequence, and it is the largest thing in this review

**LWCP is the group's most credible route out of cinema, and the strategy has been looking for one.**
`NEXT.md` is explicit that the group will not remain a cinema-only trade supplier and that the adjacent markets
— **commercial fit-out, hospitality, premium residential** — are larger; lane 1 adds that **those clients often
want the publicity**, which is the answer to a proof problem the cinema work structurally cannot solve.
**LWCP's three tiers aim at exactly those buyers**, through the **architectural specifier and BMS-integrator
channel** — which is also the pre-tender specification route `open-items.md` has had staged since Stage 2 and
never started. **One product line addresses the beyond-cinema gap, the specifier gap and the publishable-proof
gap simultaneously.** *Nothing else in the group does that.*

### 4. And the pattern across three repos is now unmistakable

- **DT** — the Commander control platform, *"the un-copyable half"*, mechanisms plus control.
- **Cinema Tools** — engine depth as the IP; Pro is **internal tooling** whose purpose is to make the method
 reproducible by fewer people (ADR 017 §4).
- **LWCP** — *"every driver measures the light it powers and holds it calibrated for life."*

**Three brands, three measurement-and-control platforms, each behind a thin brand front.** The group's stated
moat is technical depth; **the specific form that depth takes is measurement and control**, and it is the same
form three times. *That is a group-level statement `group/00-strategy.md` does not make, and it also explains
why this repo keeps discovering the product repos are ahead of it: the depth is being built where the
engineering is, and the strategy layer is downstream of it.*

### 5. Two hard constraints that must survive into any commercial decision

**Freedom-to-operate rests on two design invariants**, and they are cheap to honour and expensive to
rediscover:

1. **No optical sensing element** — no photodetector, no LED-as-sensor, no optical feedback at runtime. This is
 what clears the **Ketra/Lutron** portfolio, including a patent **in force to 2034**.
2. **Single RGB triangle plus free W** — never tessellate the gamut into three-coordinate mixing zones.

**Colour correction runs open-loop from a stored measured profile.** *These belong in Light Walls' `G2`
(session 6) as hard don'ts the moment the brand says anything public — a marketing claim about "sensing" or
"closed-loop" colour would be a patent problem, not a tone problem.* **Counsel review is still outstanding on
three narrow items and is named as gating the premium-driver certification spend.**

### 6. Two staleness notes inside LWCP itself, flagged not fixed

- **The README's status line is two weeks behind its own repository** — *"work parked ~1 week"* dated
 2026-07-20, with substantial work merged on 2026-08-02.
- **`docs/STRATEGY.md` contradicts itself.** Its posture box says ADR 0039 supersedes ADR 0005 so that **DALI
 and Matter coexist by tier**; its "What LWCP is not" section still says *"not running DT8 and Matter on the
 same coordinator: each coordinator is one or the other per ADR 0005."* **Same file, superseded rule.** *The
 same class of error as `07-tools.md` citing ADR 019 — a superseded citation left standing inside a document
 that elsewhere knows better.*

### 7. LWCP's spatial sensing — missed on the first pass, and it corrects a guardrail

*Neil: "did you also note the sensing in LWCP?" **No — the sensing documents were in the tree and were not
opened, and the omission produced a wrong rule.** The first draft of Light Walls' `G2` said "never claim
optical sensing," which would have denied a real capability. **The freedom-to-operate ban is narrow: optical
feedback on the luminaire's own output, inside the colour loop.** Corrected in place in
`group/13-standards-decision-sheet.md`.*

**LWCP has a spatial-sensing layer, ratified.** ADRs **0044** (the category and its allocation), **0045** (the
sensing head), **0046** (a UWB anchor fabric) and **0047** (the embedded platform), all accepted 2026-07-26.
The stack is **mmWave, time-of-flight depth, UWB, audio events and environment** — and **camera-free by
ratified privacy posture**, which is a saleable position in itself for residential and hospitality work.

**The claim it makes is a category claim, and it has the shape of the group's best ones.** *"Nobody has made
position computational; sensors report **what**, never **where**."* Spatial sensing is defined as **measurement
resolved into the installation's shared coordinate frame and computed against its authored model**, laddered
L0 (positioned telemetry — any scalar reading gains its node's pose and becomes an environment field over the
room) through L3. **The coordinator is the spatial computer and the fixture never learns its position**
(ADR 0015 Principle 2), which is the same allocation the colour pipeline uses.

**It also sharpens LWCP as a control system.** Against Lutron, Rako, Crestron and Control4 the differentiator
is depth of exactly this kind: **lighting that responds to where people actually are in a modelled room**, not
to which zone a PIR covers.

### 8. But sensing is not a feature of the lighting — Neil, 2026-08-15

> *"Sensing is a potential giant market in its own right."*

**Recorded as the owner's position, because this repo holds nothing else on it and would otherwise file a
market under a feature.** *An earlier draft of this finding did exactly that — demoted sensing to a capability
of the lighting platform — and it was wrong in the opposite direction to the draft before it. Both errors are
kept visible here because the shape matters: the first over-read a document, the second over-corrected from a
single instruction.*

**What the LWCP work supplies that supports a market rather than a feature:**

- **A category claim, and it is the kind this group is good at.** *"Nobody has made position computational;
 sensors report **what**, never **where**."* **That is a named absence with a ladder over it** — L0 positioned
 telemetry through L3 — structurally the same move as C-ATS's 3 Rs or measured colour. **The group's best
 positions have all been of this form.**
- **Camera-free by ratified posture.** In residential, hospitality and workplace, *knowing where people are
 without watching them* is a saleable position on its own, and it is a choice competitors using vision cannot
 reverse cheaply.
- **The architecture is already allocated.** The coordinator is the spatial computer; the device never learns
 its position (ADR 0015 Principle 2). **That is a platform shape, not a product feature** — the same shape as
 DT's Commander and Cinema Tools' engines (§4).
- **And it is the least cinema-shaped thing the group has.** Presence and position in a modelled room serve
 **commercial fit-out, hospitality and workplace** — the markets `NEXT.md` says the group wants and cannot yet
 prove. **LWCP at least carries a lighting heritage; sensing carries none, which is an advantage here.**

**What is not known, and must not be filled in:** the size of the market **[?]**, who buys **[?]**, through
which channel **[?]**, against whom **[?]**, at what price **[?]**, and on what timing **[?]**. **None of that
is in any repo**, and a plausible answer would be worse than the gap.

**Three decisions this creates, none of them takeable here** — recorded in `open-items.md`:

1. **Is sensing a line of its own, or a layer of LWCP?** The engineering is currently inside LWCP; the market
 claim is not lighting-shaped. *These can both be true and the answer is a commercial choice, not an
 architectural one.*
2. **How does it relate to `SRND Solutions`** — the own-made *"sensors and interfaces"* line
 `group/01-commercial-model.md` already names as in development and `open-items.md` still records as an
 unanswered go-to-market question? **Same thing, adjacent things, or one inside the other is undetermined**,
 and the repo currently describes SRND Solutions in words that could equally describe this.
3. **Does it get a brand, and whose?** The six-brand roster has no slot for it, and the group model makes
 brands the marketing surface.

> **What this finding is for.** The archive answered *what has been sold*. This answers *what could be sold
> next*, and it turns up **two** forward positions rather than one: **LWCP, filed under "Hold" for a 2023 stop
> the work has since overtaken — and sensing, which the plan does not mention at all.** *One is
> mis-prioritised; the other is missing.*

> **A withdrawal, recorded because the reasoning is the useful part.** This finding first carried two further
> sections, drawing group-level conclusions — about SRND Solutions' go-to-market and about the cross-sell
> thesis being engineered rather than asserted — **from a platform document that also governs a separate
> background project with no commercial value** (Neil, 2026-08-15). **The premise was wrong and the sections
> are removed rather than struck**, along with the `open-items.md` note they produced. *The error is the one
> `06-competitors.md` opens by warning about, in a new place: **a document's existence and its ratification
> were read as commercial weight**, and nobody had said it carried any. **Ask what a document is for before
> building on it** — the same check this repo already applies to competitors' marketing sites.*
