# The C-ATS segment cut — measured, 2026-08-18

*The third leg of the C-ATS template run (`../NEXT.md` item 2: "its segments cut from the database"). **Facts
only.** Produced by `../data/cats_segments.py` from `../data/derived/all-transactions.csv`; the per-account table it
writes is `../data/derived/cats-segments.csv`. What the numbers mean, and which segment gets which pathway, is
`../brands/c-ats/segments.md` — per `../method.md`, evidence does not argue. Re-run the script to reproduce every
figure below.*

## Method, and the one correction it required

Rows filtered to `category = "Acoustic treatment"`, `is_product_revenue = 1`, `is_intra_group = 0`. That is C-ATS
product wherever it was invoiced from — the C-ATS entity's own ledger, GTUK's `CATS` line, and SRND Group's store
rows — not the C-ATS company's accounts, which hold only part of it.

**Account identity had to be normalised further than the ledger does.** `contact_canonical` collapses only the
Apex USA/LLC pair (`../data/README.md`), and on this question that is not enough: **35 clusters covering 74 names
are one dealer written two or three ways.** `Meridian Audio Ltd` bought C-ATS and `Meridian Audio Limited` did not —
the same dealer, landing in opposite segments. The script strips legal-form words before grouping. The effect:

| | Names | Dealers |
|---|---|---|
| `contact_canonical` as the ledger carries it | 588 | — |
| After legal-suffix normalisation | — | 549 |

**Both counts are still upper bounds.** Suffix stripping catches `Ltd`/`Limited`, not `Cornflake` versus a
differently-worded trading name, and not a dealer who changed name. One source row also carries a mojibake
contact name (`Plafond S<?>bastien Dhennin EIRL`) — a source encoding fault, unfixed here.

## What the ledger holds

| | |
|---|---|
| C-ATS external product revenue, all entities, 2015 → 2026 | £495,106 |
| External accounts that have ever bought it | 53 |
| External accounts in the group ledger, 2012 → 2026 | 549 |
| So: share of the group's dealer base that has ever bought C-ATS | 9.7 % |
| Of the 53, bought in more than one year | 17 |
| Of the 53, also bought some other category from the group | 43 |

### By year

| Year | Net | Rows | Accounts |
|---|---|---|---|
| 2015 | £21,250 | 11 | 5 |
| 2016 | £50,045 | 8 | 2 |
| 2017 | £69,834 | 22 | 6 |
| 2018 | £39,583 | 19 | 11 |
| 2019 | £20,646 | 9 | 5 |
| 2020 | £52,556 | 43 | 9 |
| 2021 | £46,144 | 37 | 11 |
| 2022 | £23,065 | 26 | 5 |
| 2023 | £13,328 | 11 | 3 |
| 2024 | £73,092 | 41 | 15 |
| 2025 | £67,667 | 53 | 16 |
| 2026 (part) | £17,898 | 12 | 6 |

*Account counts are per year on the un-normalised name, so they run slightly high against the 53.*

### By recency segment

*Recency is measured against the ledger's own last year (2026), not against a rolling window.*

| Segment | Definition | Accounts | C-ATS net |
|---|---|---|---|
| C-ATS active | last C-ATS order 2025 or 2026 | 18 | £276,726 |
| C-ATS recent | last C-ATS order 2024 | 7 | £41,837 |
| C-ATS lapsed | last C-ATS order 2020–2023 | 16 | £140,108 |
| C-ATS dormant | last C-ATS order before 2020 | 12 | £36,435 |
| Never bought C-ATS, active elsewhere 2024–26 | no C-ATS row; some other category in 2024–26 | 142 | £0 (**£4,002,157** spent with the group on everything else) |

### By panel

*Attributed from the line's own product line or item description; nothing inferred.*

| Line | Net |
|---|---|
| Unattributed (GTUK `CATS`, some store rows) | £165,147 |
| Reflection | £89,831 |
| Reverberation | £83,399 |
| Packs (legacy) | £79,222 |
| Complete (legacy) | £39,024 |
| Resonance | £38,484 |

**A third of the revenue cannot be attributed to a panel** — the GTUK Sales Analysis export carries an item code
and no description (`../data/README.md`, MON-11). The re-export that would fix it is already a backlog item.

## What the CRM holds, against the same question

From `../data/derived/monday-accounts.csv` (1,658 accounts) and `../data/derived/monday-contacts.csv` (1,371 contacts):

| Field | Value | Count |
|---|---|---|
| `CATS Status` | Not Customer | 1,568 |
| | Presented | 49 |
| | Approached | 16 |
| | Current Customer | 16 |
| | Not Interested | 4 |
| | Historic Customer | 4 |
| | Demonstrated | 1 |
| `C-ATS Relationship` (contacts) | Dealer | 9 |
| | None | 1,254 |
| `Subscribe C-ATS` (contacts) | Yes | 191 |
| | No | 32 |
| | (blank) | 1,148 |
| `Subscribe SRND` (contacts) | Yes | 985 |

**The CRM and the ledger disagree by a factor of two and a half.** The CRM marks 20 accounts as current or historic
C-ATS customers; the ledger shows 53 that have paid for C-ATS product. Neither source has been reconciled against
the other before now. The ledger is the harder evidence — an invoice happened — but the CRM holds the only
*status* field, and it is the only place `Presented` and `Approached` exist at all.

## Four facts this cut establishes

1. **£495,106 over eleven years, 53 dealers, 9.7 % of the group's dealer base.**
2. **142 dealers bought from the group in 2024–26 and have never bought a C-ATS panel**, spending £4,002,157 on
   everything else in that window.
3. **43 of the 53 C-ATS buyers already buy another category** — for most of them C-ATS was not the first thing
   they bought from us.
4. **17 of 53 bought C-ATS in more than one year.** Thirty-six bought once.

## What this cut does not establish

- **Why the 142 have not bought.** Nothing here says whether they were asked, whether they buy acoustics
  elsewhere, or whether their work does not call for it. That is `../registers/backlog.md` CON-3 territory and it
  is not answered by a ledger.
- **Whether `Presented` means presented.** The 49 rows are a CRM field with no dated event behind them in this
  export.
- **Unit volumes.** The C-ATS and store rows carry no quantity (`../data/README.md`), so panels-per-job is unknown.
- **Anything about the 2015–2018 period's account identity.** GTUK-era names are the least normalised.
