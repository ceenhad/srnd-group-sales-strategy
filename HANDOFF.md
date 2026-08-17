# Handoff — read this first if you are a new session

*Written 2026-08-14 at the close of a two-day working session, for a session starting cold with no prior context and
no access to the previous session's memory. **Everything you need is in this repo.** Read this, then
`CLAUDE.md`, then `NEXT.md`.*

---

## 1. What just happened

**Two days of measurement.** Before this, the repo held strategy and a plan but almost no facts about the present. It
now holds the sales history of the whole group, the platform audited field by field, and thirty numbered findings —
and the plan has been amended against them **without re-arguing any settled decision.**

Three deliverables landed:

| File | What it is |
|---|---|
| **`evidence/engine-audit.md`** | Engine (the operations platform) audited against the 58-field product record. Closes `TSK-5`, `DOC-12`, `REC-0` |
| **`evidence/archive-findings.md`** | **The main artefact.** 30 findings from six data sources, fifteen years. Starts with a **source register** — read that first |
| **`data/`** | The data itself, stored not referenced: nine source files verbatim, lossless extracts, and the loaders as code |

**Everything is merged to `main`.** PRs #17 and #18.

---

## 2. The five things that matter most

**If you read nothing else, read these. Each is measured, not argued.**

1. **The work stops one step before anybody hears about it.** Nine measured instances of *built, and never said*:
   C-ATS has its record filled, copy written and a BSRIA report published, and drew **6 clicks in 29 email
   campaigns**; the best campaign ever sent **was the last one sent**, four months ago; **348 partners hold signed
   T&Cs and pricing access and 189 have never bought anything**; **40 approved dealers cannot see a price at all.**
   *(Finding 30. Note this runs **opposite** to the failure mode `CLAUDE.md` names — a refinement is proposed in
   `registers/open-items.md` for Neil, not applied.)*
2. **The growth target is already inside the building.** 10–20 % on 2025's £1.44m is £144–288k, which is **10 to 64
   first orders from the 189 who already signed.** No new capture, content or system needed. *(Finding 27.)*
3. **Own-made revenue is worth two to three times carried revenue.** Each step of the chain the group holds is a
   margin it keeps: own-made direct to a dealer earns manufacture **and** distribution (47–64 %); a carried line can
   only ever earn the distribution step (**Leyard 20 %, a structural ceiling**). This explains make-not-buy, the 2×
   distributor test and why Cinema Store exists. *(Findings 22–23.)*
4. **Audio was the group's largest category and is now absent.** 38.7 % of the distribution era — and **£779,979 of
   it was audio over IP, exactly where Pro-Fi aims.** Pro-Fi is pre-revenue with no shipping speaker line, and
   `Audio` appears in eight live deals. *(Findings 17, 24.)*
5. **The founding premise holds, in a prohibitive form.** First-order size predicts nothing: sub-£5k starters
   produced **61 % of twelve years' revenue**, and the result replicates in a second business. So *"we don't triage
   dealers by order size"* is not optimism — **nothing in a first order tells you which half you are looking at.**
   *(Findings 3, 11.)*

---

## 3. The current direction — and it is a change of scope

**Read `registers/open-items.md` § "the direction set 2026-08-14" in full before proposing work.** In short, Neil's position:

> Not ready to start executing. Three things come first — **KPIs** (never discussed), **data reconciliation**
> (*"could win us a LOT"*), and **the doing question**: how to act when the work is *"basted over 100 tools and apps
> and files."* **The answer: extend engine so social media, mail campaigns, websites and reporting are either in
> engine or closely coupled to it.** Willing to invest the time and tokens.

**The argument that those three are one question:** a KPI is only real with one uncontested definition and a system
that computes it — and **four dealer counts were found differing five-fold.** Reconciliation is that same problem
priced. **Every failure found this week sits at a boundary *between* systems, not inside one.**

**Behind it is a thesis**, recorded in the same section: the transformation is AI-driven top and bottom; Shopify gives
little against a Claude-powered Cloudflare + Supabase combination; glue apps die as MCP makes them irrelevant; and
the business is simple enough to own outright. **The evidence for and the reservations against are both written up —
read both.** The headline reservation: *storefront cheap, checkout expensive*, and a platform programme is a
*building* activity, which is the mode the group is already strongest in and the one finding 30 warns about.

**This reverses a deliberate parking** in `NEXT.md`'s "deliberately not now" — the fragmentation fix was explicitly
*"not this repo's."* The flag is recorded in both files.

---

## 4. What is open, in priority order

| | Item | Why |
|---|---|---|
| **1** | **`MON-13` — 40 approved dealers with no engine account** | The account is a strict gate: **no account, no pricing.** Neil believes these are key people. **A fault to fix today, not a session's work** |
| **2** | The **active price list** is the 8-entry `Scenario 04/06/2026` with **no Leyard or SRND row**, while a fuller 12-entry version sits archived | A live pricing control in what looks like the wrong state |
| **3** | **`MON-15` / `MON-16` / `MON-17`** — segment the list by brand, restart the cadence, point some mail at C-ATS | All cheap, all already paid for. Reach is solved; **targeting does not exist** |
| **4** | **KPI definitions · the reconciliation map · the consolidation shape** | The next session's substance. See §3 |
| **5** | `MON-8` Shopify · `MON-11` two Xero re-exports · `MON-12` Monday↔engine reconciliation | Remaining data gaps. `MON-11` would resolve ~£1.05m of unclassified revenue |
| **6** | Decisions only Neil can make | The `CLAUDE.md` refinement; the `C1` dual-listing wording (13 DT codes on two stores); whether **Fabric Walls** takes the second record pass; **roles** (`NEXT.md` step 1, still undone) |

**One fork worth resolving early:** does the product record get filled **into engine's knowledge mechanism** — which
`evidence/engine-audit.md` §2 found already exists, pointed at engine's own UI — rather than into files that later migrate?

---

## 5. How to work in here

**Read `CLAUDE.md` — it binds.** The house rules that matter most in practice:

- **Check the live system before specifying anything that touches it.** This repo assumed an engine gap **three
  times** and was wrong every time, always in the same direction: engine holds more than the plan credits.
- **Evidence, not re-argument.** New facts land as evidence against a row or an open item. They do **not** reopen a
  closed decision — that is a dated reversal and Neil's to make. Prefer amending the plan to re-arguing the strategy.
- **Flag, don't guess.** Several findings this week were held open (`[?]`) rather than filled with a plausible answer,
  and in two cases the guess would have been wrong.
- **Corrections go in place, visibly.** Where a finding was revised, the original reasoning is struck through rather
  than deleted, because knowing *why* something looked different matters.

### The data gotchas that cost real time to rediscover

- **Start any group-level question from `data/derived/all-transactions.csv`** — 10,360 rows, five entities, one
  harmonised category vocabulary, reconciled to the pound. The per-entity extracts are for single-company work.
- **Two Xero report shapes.** *Sales Analysis* has item code and quantity but **no description**; *Account
  Transactions* has description but no item code, puts the **contact in a group header row**, and gives amounts as
  debit/credit so `net = credit − debit`. **The `Raw Data` sheet reaches further back than the pivot sheets** —
  GTUK's pivots start 2019, its data starts 2012.
- **Monday exports are grouped boards, not tables.** On the Deals board sub-item blocks sit *between* parent rows, so
  **column A is the discriminator**. The board group is the only win/loss signal in the export.
- **Join Mailchimp to engine on email domain, never on `COMPANY`** — weak coverage there produced the opposite answer
  on a live question.
- **Separate intra-group counterparties before counting dealers, and re-run every source after adding one**, because
  a newly recognised group entity may have been a customer of an already-loaded one.
- **Engine access** is a read-only Supabase MCP pinned to project `vzgdhfsmxteoxxsuexyg` (`SRND Engine`, eu-west-2).
  The testbed is `bpsaxuwitlycubnvmfrr`. **`zgwkyswychtqfmuvsuvt` is the separate Cinema Platform project — not
  engine.**
- **Mailchimp** is pulled by `data/fetch_mailchimp.py`, reading `MAILCHIMP_API_KEY` from the environment. **The key is
  never in the repo, a file, or a command argument.** `setx` will not reach an already-running process — read the
  persisted value with `[Environment]::GetEnvironmentVariable('MAILCHIMP_API_KEY','User')`. **The key is
  full-access; it may already have been revoked.**

### Sensitivity

`data/` holds **invoice-level revenue, named dealer relationships, and 2,845 named contacts with email addresses**
(the last retained at Neil's instruction, flagged in `data/README.md`). The repo is private. **Treat any decision to
share, clone or grant access as a decision about commercial and personal data.**

---

## 6. What was deliberately not done

So you do not mistake absence for oversight:

- **No new strategy documents.** The repo is supposed to stop growing; every addition here has a stated reason.
- **Nothing in `group/` was re-argued.** Two single-line evidence citations were added — `the-group-play.md` (the
  measured "no long tail" claim) and `commercial-model.md` (the 2× distributor test) — and nothing else.
- **`CLAUDE.md` was not edited.** A refinement is proposed in `registers/open-items.md` for Neil to accept, reword or reject.
- **No pricing was published anywhere**, and no supplier or OEM relationship was named in anything public-facing.
- **The engine price-list state was not corrected**, despite looking wrong — access is read-only and it is a live
  commercial control.
