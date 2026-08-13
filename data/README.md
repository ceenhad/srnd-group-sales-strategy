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

**Both verified byte-identical to Dropbox** on 2026-08-13 using Dropbox's own block-hash algorithm (SHA-256 per
4 MiB block, then SHA-256 of the concatenated digests). Re-verify any time with that method rather than a plain
file hash, which will not match what the Dropbox API reports.

**Treat these as read-only.** They are the received artefacts. Corrections belong in the derived extracts or in the
findings, never by editing a source file — otherwise provenance is gone.

## `derived/` — analysis-ready, and lossless

| File | Rows | Source report type |
|---|---|---|
| `gtuk-invoice-lines.csv` | 4,992 | Sales Analysis (`Raw Data` sheet) |
| `dt-invoice-lines.csv` | 3,952 | Sales Analysis (`Raw Data` sheet) |
| `cats-account-transactions.csv` | 268 | **Account Transactions** — different shape, normalised to the same columns |

One row per transaction, UTF-8 CSV, **all three on the same column contract below.** Every row from the source is
present. The cleaning decisions are carried as *columns* rather than applied as deletions, so nothing is silently
dropped and anyone can disagree with a decision without re-deriving the file.

**The C-ATS report is a different Xero export and was normalised, not merely converted.** Three things to know:
its **contact is a group header row** rather than a column (parsing row-wise without tracking the group loses the
dealer); amounts arrive as **`Debit (GBP)` / `Credit (GBP)`**, so `net` here is **credit − debit** with revenue as
the credit; and there is **no item code or quantity**, while `Reference` holds an invoice number only sometimes —
elsewhere free text like `Stock Catchup`. Treat `invoice_number` from this source as a label, not a key.

**Three no-contact manual journals** in the C-ATS file (a sales accrual, its reversal, and a suspense write-off,
netting **−£815**) are preserved with `is_product_revenue = 0`, since they carry no dealer and would otherwise
distort per-dealer figures.

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

> **One classification unconfirmed — `[?]`.** The C-ATS file contains **Genesis Technologies AG** (£13,083) and
> **Genesis Technologies AG (Deutschland)** (£64,398), together **£77,481 — 30 % of what is currently counted as
> C-ATS external revenue.** They are treated as **external** pending confirmation. The lineage note in
> `group/01-commercial-model.md` has *GT* as the forerunner of Apex-Tech UK / SRND Distribution, and C-ATS invoices to
> Apex Tech Scotland carry the description "Genesis Technologies Ltd" — so the name is used for a group entity
> somewhere. Whether these two AG companies are group entities or independent distributors changes the external
> figure materially. **Ask before relying on C-ATS external totals.**

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
