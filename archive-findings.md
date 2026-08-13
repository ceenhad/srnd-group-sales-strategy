# What the archive says — measured findings

*The counted output of `backlog.md` `MON-1`/`MON-2`/`MON-3`. **Evidence, not argument** — this file holds what the
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
| 4 | **Shopify — distribution after the swap into SRND** | **Not yet obtained** — `backlog.md` `MON-8` | The distribution 2024–25 gap between sources 1 and 3 | ~2024 → 2026 |
| 5 | **Old Monday.com CRM logs** | **Not yet handed over** — `backlog.md` `MON-1` | Historic pipeline: quotes, stages, win/loss | Pre-engine |
| 6 | **Sent-mail archive** | Not yet worked — `backlog.md` `CON-3` | Which questions recur, for `R3`/`N3` ranking | Years |

> **▶ The data itself is now stored in the repo, not just pointed at — `data/`** (2026-08-13, at Neil's
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
template, but **`product_speaker_technical` holds zero rows** (`engine-audit.md` §1). Two consequences for anyone
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
July 2021) → SRND Distribution** (`group/01-commercial-model.md`; `group/2023-buyer-journey-archive.md`).
**So this is one of the six brands' own twelve-year trading record**, not an analogue borrowed from elsewhere —
and it is *distinct from the US Apex-Tech* recorded in `current-state.md` as the resigned DT distributor. Two
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
territories (`current-state.md`) — is **not** in this file. Three consequences: the **£11.75m is a UK figure**, not
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

`current-state.md` asked *"what share the top five accounts represent."* Over the twelve years:

| | Share of net |
|---|---|
| Top 5 customers | **22.3 %** |
| Top 10 | 36.2 % |
| Top 20 | **49.8 %** |
| Top 50 | 71.0 % |

**Half the revenue sits in twenty accounts, and the tail is long and real** — 354 paying external dealers, of whom about 200
bought a single line. Note the top account here reached **£623,422 over nine years**; that is *not* the
"£500,000 in a year" dealer in `current-state.md`, which is a current SRND account. **Different eras, different
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

**The `group/00-strategy.md` claim under test:** *"There is no long tail to service cheaply. A small order in one
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
(`engine-audit.md` §2), needing no new capture at all.

### Finding 5 — the own-brand lines behaved differently from each other

| | Dealers | Net | Was it the dealer's **entry** line? |
|---|---|---|---|
| **DT SCREENS** | 85 | £1,165,218 | **Entry for 45; arrived later for 40** |
| **CATS** | 23 | £141,844 | Entry for **7**; arrived later for **16** |

**DT was a genuine front door** — over half its dealers met the business through it. **C-ATS mostly arrived
second**, after a dealer was already buying something else.

**This bears on an open item without settling it.** `open-items.md` asks for entry products per brand, and
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
`group/00-strategy.md`'s third consequence — *"an asset taken for granted leaks"* — measured for the first time
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

**This is the same argument `decided.md` C1j already makes about the US, applied at home:** *"a resigned
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
  `X6`/`REC-2` remain uncaptured (`engine-audit.md` §3). The archive proves the *shape* of relationships, never the
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
broadening** — which is precisely what `group/00-strategy.md` says the group exists *not* to do: the asset is
*"valuable dealer relationships, counted across every brand, over years,"* and the count is still going the wrong
way. **Good news on the revenue line, unchanged news on the asset.**

**This is `group/00-strategy.md`'s second consequence, measured on DT itself:** *"Direct is asset-building, not
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
orders** inside its eleven weeks of history (`engine-audit.md`).

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

**The repo says something different.** `current-state.md` records Apex-Tech as having **resigned from DT**;
`decided.md` **C1f** treats the US as *"open and unencumbered"* because of it; **C1j** calls the Apex dealer base
*"unserved"* and *"the fastest revenue in the strategy"*; `NEXT.md` lane 7 opens on *"the largest market in the
world is unrepresented."* **Workstream W2 (`US-1`–`US-6`) rests on that reading.**

**The size of the dependency is still worth stating plainly: 31.5 % of DT's external revenue over seven years was one
counterparty, and it was the only dealer that ever bought the whole range.** `decided.md` C1j describes that dealer
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
- **No why.** No loss reasons, no competitors, no lead source — `X6`/`REC-2` remain uncaptured (`engine-audit.md`).
- **No territory.** No country field in any source; dealer names imply geography but that is inference.
- **Uneven scope.** GTUK is **UK-only**; the others include international. So the pre-2024 series understates the
  group's true geography while the post-2024 series does not.
- **2024–25 distribution is thinner than it looks**, pending `MON-8` (Shopify).

---

## Finding 17 — audio was the group's second business, and it is now absent

*Measured at Neil's prompt (2026-08-13): "look at how much of our historic revenue was speakers, amps and
processing to see why we see [Pro-Fi] as such an important gap to fill."*

**In the distribution era, audio was 30.8 % of revenue — £3,613,784 of GTUK's £11,742,315.**

| | Net | Share of GTUK |
|---|---|---|
| **Speakers** (Stealth, Leon, Wisdom, Phase Technology, SolidDrive, Quested, Aerial) | **£2,620,620** | **22.3 %** |
| Amplifiers (ADA, Acurus, Storm Audio, Aragon, Integra) | £485,334 | 4.1 % |
| Audio processing (Datasat) | £187,105 | 1.6 % |
| `PRO AUDIO` — a generic line, unclassified | £320,725 | 2.7 % |
| **Audio subtotal** | **£3,613,784** | **30.8 %** |
| Video processing (madVR, Lumagen) | £280,357 | 2.4 % |

**Speakers alone were the second-largest thing the group ever sold** — behind Barco projection at £2,976,976
(25.4 %) and ahead of its own DT screens at £1,165,218 (9.9 %).

**Today that business is 9.3 % and carried.** SRND's audio is £254,151 — speakers £188,465 (MAG Theatron,
PhaseTech, DCB Flyte, all third-party) and amplifiers £65,686. **No own speaker line is shipping** (Neil).

**Across both eras: audio is £3,867,935, 19.9 % of all group external revenue — 21.8 % with video processing.**

**So the Pro-Fi bet is sized by history rather than by hope.** The group sold roughly £3.6m of other people's audio,
knows the dealers who bought it, and now has no own line in the category. *That is a measured gap, not a
speculative one — and it is the largest single category the group has vacated.*

*Classification caveat: these are my groupings of carried-brand account names and are reviewable. `PRO AUDIO`
(£320,725) is generic and could be any of the three; `SolidDrive` is a transducer rather than a conventional
speaker; `Aerial` is assumed to be Aerial Acoustics.*

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
