# data — the stored sales history

**The data itself, not links to it.** `archive-findings.md` holds what the numbers *mean*; this folder holds the
numbers, so a moved Dropbox file or a closed account cannot cost us the history. The register in
`archive-findings.md` remains the index — scope, period and caveats per source live there, not here.

## `source/` — the files exactly as received

| File | From | Size | Dropbox content hash |
|---|---|---|---|
| `GTUK - Sales Analysis Report - All.xlsx` | `/GTUK Staff/Sales/Reports/` · `id:F15NlnKOA1AAAAAAAAAo8w` | 1,043,526 b | `ab9ead0e0ef338c2b750d66099a660dfe6fd0f9689f558fa2febb19f8945c08e` |
| `DT - Sales Analysis Report - All.xlsx` | `/DT Management/Sales/` · `id:F15NlnKOA1AAAAAAAAAo-Q` | 881,262 b | `9c9df2b93d5f3be812eeff64efc83a686fc90d7d3ada8f0e6691bff921fbbcad` |
| `C-ATS - Account Transactions.xlsx` | supplied locally 2026-08-13 (`Cinema_Acoustic_Treatment_Systems_Limited_-_Account_Transactions.xlsx`) | 22,551 b | `1c630431b99daef6fd1cfe0f53b3ba235845643f6db86a3058b3fc4203bba02a` |
| `SRND Group - Account Transactions.xlsx` | supplied locally 2026-08-13 (`SRND_Group_Ltd_-_Account_Transactions.xlsx`) | 71,112 b | `07d0233f1d535d17536d84ebe380d1c8792dca61e44bef8b179eac64c6233891` |
| `Light Walls - Account Transactions.xlsx` | supplied locally 2026-08-13 (`Light_Walls_Ltd_-_Account_Transactions.xlsx`) | 36,314 b | `4d667a97ea1cd7eba526f8669ebfe6870c3394b205f0fc752b20e1f8ebeccb92` |

**Both verified byte-identical to Dropbox** on 2026-08-13 using Dropbox's own block-hash algorithm (SHA-256 per
4 MiB block, then SHA-256 of the concatenated digests). Re-verify any time with that method rather than a plain
file hash, which will not match what the Dropbox API reports.

**Treat these as read-only.** They are the received artefacts. Corrections belong in the derived extracts or in the
findings, never by editing a source file — otherwise provenance is gone.

## `derived/` — analysis-ready, and lossless

| File | Rows | Source report type | Period |
|---|---|---|---|
| `gtuk-invoice-lines.csv` | 4,992 | Sales Analysis (`Raw Data` sheet) | 2012 → 2023 |
| `dt-invoice-lines.csv` | 3,952 | Sales Analysis (`Raw Data` sheet) | 2016 → 2026 |
| `cats-account-transactions.csv` | 268 | **Account Transactions** | 2016 → 2026 |
| `srnd-account-transactions.csv` | 730 | **Account Transactions** | 2023 → 2026 |
| `lightwalls-account-transactions.csv` | 418 | **Account Transactions** | 2020 → 2026 |

**All four are produced by `data/normalise.py`** — one command per source, so the contract below is enforced by code
rather than by hand:

```bash
python data/normalise.py account-txns "data/source/SRND Group - Account Transactions.xlsx" data/derived/srnd-account-transactions.csv
```

Regenerating all four reproduces the published totals to the pound. The script carries the settled intra-group list
and the account-exclusion rules, so **a new tranche is one line, not a fresh set of judgements.**

One row per transaction, UTF-8 CSV, **all three on the same column contract below.** Every row from the source is
present. The cleaning decisions are carried as *columns* rather than applied as deletions, so nothing is silently
dropped and anyone can disagree with a decision without re-deriving the file.

**The C-ATS report is a different Xero export and was normalised, not merely converted.** Three things to know:
its **contact is a group header row** rather than a column (parsing row-wise without tracking the group loses the
dealer); amounts arrive as **`Debit (GBP)` / `Credit (GBP)`**, so `net` here is **credit − debit** with revenue as
the credit; and there is **no item code or quantity**, while `Reference` holds an invoice number only sometimes —
elsewhere free text like `Stock Catchup`. Treat `invoice_number` from this source as a label, not a key.

### The `SRND Store Sales` problem, and how it is fixed

**The Shopify integration posts every store order to a single nominal account,
`SRND Store Sales`** — 416 rows and **£1,385,960, just over half of SRND Group's revenue**, arriving with no product
category at all. It is a chart-of-accounts mapping failure at source, not a data problem: **the item description
survives**, in the form `<Contact> - <Item>`.

`data/classify_store_items.py` recovers the category by ordered keyword rule and adds four columns:

| Column | Meaning |
|---|---|
| `description` | The raw `Description` cell, as received |
| `item_description` | The same with the contact-name prefix stripped — the item alone |
| `category` | **Product category.** For store rows, derived from `item_description`; for every other row, the account's own line |
| `category_source` | `account` · `description-rule` · `unclassified` — always visible which is which |

**All 416 store rows classify; nothing is left unmatched**, across 266 distinct item descriptions. Two needed rules
added after a first pass (a `DYN4XL` model prefix with no word boundary, and a named cinema-interior supply), and
both are commented in the script.

**Three things to know before relying on `category`:**

1. **It is a derived classification, assigned by rule here — not the business's own.**
   `data/derived/srnd-store-item-categories.csv` lists every distinct item against its assigned category with row
   count and value, **for review and correction.** Corrections belong in the rules, then re-run.
2. **Rule order matters and encodes real decisions.** Logistics, refunds and surcharges are matched *first* because
   they name products without being product sales; services precede the goods they mention; `Fabric Walls Tool` is a
   tool, not a fabric wall; an Ultrasuede *sample* is a sample, not fabric revenue; a Leyard *services* line is a
   service, not an LED wall.
3. **Some store categories are deliberately finer than the Xero account set** — masking screens, fixed and
   specialist screens, image surfaces, screen accessories, port holes, hush boxes and fabric wall frames have no
   account line of their own, or are lumped into `Projection Screens`. Recovering that detail is the point, so it is
   kept rather than flattened. Pure case and synonym collisions between rule names and account names **are**
   harmonised onto the account name (`CANONICAL` in the script) so no category appears twice in an aggregate.

**One thing to fix at source:** the Xero account is spelled **`Sales - Materials - Audio Amplfiers`**. The
classifier corrects it to `Audio Amplifiers`; the account itself still has the typo.

### What the exclusions actually cost — quantified, so no one has to wonder

`is_product_revenue = 0` rows are kept in the files. Their weight:

| Source | Excluded rows | Net effect | Made up of |
|---|---|---|---|
| C-ATS | 5 | **+£968** | 2 `Other Revenue` (+£1,782); 3 no-contact journals (−£815: an accrual, its reversal, a suspense write-off) |
| SRND | 43 | **−£28,021** | 15 `Payable Invoice` postings to revenue accounts (−£42,358); 4 `Other Revenue` (+£15,126); 2 `Spend Money` (−£789); **22 no-contact manual journals netting exactly £0** — accrual/reversal pairs, so nothing is lost by dropping them |

**One of these is a judgement rather than a rule, and it is the largest single item.** The 15 SRND `Payable Invoice`
rows sit in revenue accounts and net **−£42,358**, about 1.6 % of SRND's total. They are excluded as not-a-sale-to-a-
customer, which is right if they are supplier-side postings or miscodings, and **overstates revenue by that amount if
they are genuine reductions** such as distributor rebates. Flip `NON_SALE_SOURCES` in `normalise.py` to test the
other reading.

| Column | Meaning |
|---|---|
| `entity` | Which trading company the row belongs to |
| `invoice_number` · `invoice_date` · `year` | As received; `year` is derived for convenience |
| `item_code` · `quantity` | As received |
| `contact_raw` | The `Contact` string exactly as in the workbook — unnormalised |
| `contact_canonical` | `Apex Technologies USA` / `USA LLC` merged to one account (Neil, 2026-08-13); otherwise identical to `contact_raw` |
| `status` | `Paid` · `Approved` · `Draft` · `Deleted` |
| `account_raw` · `product_line` | The account code, and the same with the `Sales - ` prefix stripped |
| `net` | **The measure.** Credit notes are negative and net off. `Unit Price (ex)` is *not* carried — it holds list prices and is inconsistent with the rest of the row |
| `is_product_revenue` | `1` if the row counts toward product revenue: a sales account, status not `Deleted`/`Draft`, with a net, date and contact. **GTUK 4,909 of 4,992 · DT 3,460 of 3,952** |
| `is_intra_group` | `1` for Apex Tech Scotland Ltd, SRND Group Ltd, Apex Tech International Ltd / Apex Technologies International, Dzyn Ltd, Display Technologies Ltd. **Filter these out before counting dealers** — missing it overstates the dealer base and understates concentration |

> **Confirmed external, do not re-ask (Neil, 2026-08-13): Genesis Technologies AG** (£13,083) and **Genesis
> Technologies AG (Deutschland)** (£64,398) **are not group entities.** Together £77,481 of genuine external C-ATS
> revenue. The name is easy to misread because *GT* was the forerunner of Apex-Tech UK / SRND Distribution
> (`group/01-commercial-model.md`) and C-ATS invoices to Apex Tech Scotland carry "Genesis Technologies Ltd" in the
> description — **the description is not the counterparty.** Likewise `Genesis Home Technologies SL` is external
> (it appears in DT's file as a Spanish dealer).
>
> **The intra-group list, as it stands:** Apex Tech Scotland Ltd (incl. the `/ Apex-Tech UK` spelling), Apex Tech
> International Ltd / Apex Technologies International, SRND Group Ltd, Dzyn Ltd, Display Technologies Ltd (incl.
> `Limited`), Light Walls Ltd, Cinema Acoustic Treatment Systems Limited. **Everything else is external**, and
> `Complete-ATS` (£222, Light Walls only) is the one unresolved case — see `UNRESOLVED_ENTITIES` in `normalise.py`.

> **Each new entity can reclassify earlier sources, so regenerate them all.** A newly-recognised group company may
> have been a *customer* of an already-loaded one. Adding Light Walls Ltd moved £19,559 out of DT's external revenue
> and £3,000 out of GTUK's. The loader therefore holds **one shared intra-group list**, and every source is
> regenerated together after any addition to it:
>
> ```bash
> for f in data/source/*.xlsx; do echo "$f"; done   # then re-run normalise.py per source, and classify_store_items.py
> ```

**To reproduce any figure in `archive-findings.md`:** filter `is_product_revenue = 1`, then split on `is_intra_group`,
then group by `contact_canonical`, `product_line` and `year`, summing `net`.

## What is not here

Engine is live and not extracted — read it directly (project ref in the register). The three outstanding sources —
Shopify, the Monday.com CRM logs, the sent-mail archive — are not obtained yet and have backlog rows (`MON-8`,
`MON-1`, `CON-3`). **When they arrive, they land here the same way: the received file in `source/`, a lossless
extract in `derived/`, a row in the register.**

## Sensitivity

**Internal only.** Invoice-level revenue and named dealer relationships. Nothing in here goes into public content,
and dealer names are not for publication in any form.
