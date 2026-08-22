# The Cinema Partners accounts — what the ledger holds, 2021–2023

*Written 2026-08-19 because Neil pointed at them: **"in the accounts you will find entries under cinema
partners?"** — asked while I was claiming the cinema design-and-materials layer had no record.*

> **Framing, stated once.** *This is the repo loading history it had not loaded. **None of it is news to the
> business** — these are Neil's own invoices. What follows is only what the ledger shows and what it means for the
> **model this repo has been building**, which has been underweighting the half of the business that turns out to be
> the larger half.*

---

## 1. What is there

**Two GTUK sales accounts** — `Sales - CINEMA PARTNERS MATERIALS` and `Sales - CINEMA PARTNERS SERVICES` — in
**GTUK / Apex Tech Scotland Ltd**, running **2021 to 2023**.

| | Lines | Positive | Credits | Net |
|---|---|---|---|---|
| Materials | 36 | £249,575 | −£113,977 | £135,598 |
| Services | 34 | £154,618 | −£571 | £154,047 |
| Total | 70 | £404,193 | −£114,548 | £289,645 |

**31 distinct invoices** — 2 in 2021, 15 in 2022, 14 in 2023. *The account pair stops after 2023, which is when
SRND Group was formed.*

## 2. The finding that matters to the model: services were the larger half

**£154,047 of services against £135,598 net of materials — and on positive lines, £154,618 against £249,575.** *Take
the credit at face value and services are **53%** of the total; ignore it and they are **38%**. **Either way this is
not a product business with a design service attached to it.***

**That is the thing this repo has been getting wrong in shape rather than in fact.** *The C-ATS work here treats the
design service as an adjunct — a **£2,400 median** engagement whose price is argued from how long a design takes
(`Q45`). **The ledger says the design half of cinema work has historically carried comparable weight to the
materials half**, across three years and seven trade customers.* **Consistent with everything Neil has said this
week** — `C1.43` (three parties, none of whom will do the acoustic design), `C1.44` (*"even with guides, someone gets
paid to design it"*), and the isolation service ladder — **but this is the first place the repo can see the
proportion rather than infer it.**

## 3. Seven trade customers, and four of them still trade with SRND

| Cinema Partners-era customer (GTUK) | Also trades with | Same dealer, different spelling |
|---|---|---|
| HiFi Corner (Edinburgh) Ltd | SRND Group Ltd | as *"Hifi Corner"* |
| Holburn (Scotland) Ltd | SRND Group Ltd | as *"Holburn (Scotland) Limited"*, and *"Holburn HiFi Ltd"* |
| Sysco Productions | SRND Group Ltd | as *"Sysco Productions Ltd"* |
| INT3 Ltd | **SRND Group Ltd**, Display Technologies, Light Walls | as *"INT3 Limited"* on DT |
| TwentyTwo Integration | GTUK only | — |
| Robin Arora | GTUK only | — |
| London AV Solutions | GTUK only | *`[?]` distinct from "West London AV Solutions" and "London AV Setup Ltd", both also in GTUK — **do not merge without checking*** |

**This is the repo's own core idea in evidence** *(`../group-strategy/the-group-play.md`: the dealer relationship
counted across brands and over years)*: **four dealers who bought cinema materials *and* cinema design from Neil in
2021–23 are still buying from SRND**, and one of them — INT3 — appears across four entities.

## 4. A defect this exposes, and `MON-7` predicted it

**`contact_canonical` is not canonical.** *It equals `contact_raw` in every case above. So the join that measures
dealer carry-over splits the same dealer across entities on spelling alone:*

- *`HiFi Corner (Edinburgh) Ltd` ≠ `Hifi Corner`*
- *`Holburn (Scotland) Ltd` ≠ `Holburn (Scotland) Limited` ≠ `Holburn HiFi Ltd`*
- *`Sysco Productions` ≠ `Sysco Productions Ltd`*
- *`INT3 Ltd` ≠ `INT3 Limited`*

**`MON-7` already says the 26% carry-over figure is a floor for exactly this reason**, citing *"The Next Level"*
against engine's *"TNL Systems"*. **This adds four more instances in one seven-customer sample**, which is a rate
worth stating: *in this sample, **every dealer that continued was mis-joined**.* **`MON-7` should be re-run, and the
canonicaliser is the fix, not a manual list.**

## 5. What the ledger cannot tell us

- **No line descriptions.** *The GTUK export carries account, quantity, contact, date and net — **and no description
  field**. So **what was actually sold under these accounts is not recoverable from this data**: not the isolation
  content, not the deliverable names, not the split between drawings and site work. **The account names are the only
  description.***
- **One £113,977 credit sits inside the materials figure**, on `INV-2022/1844` to HiFi Corner, dated the same day as
  £138,473 of positive materials lines to the same customer on `INV-2022/1843`. *Whether that is a re-invoicing, a
  deposit offset or a correction **is not visible here**. Both the gross and net figures are given above for that
  reason.*
- **`[?]` What "Cinema Partners" actually was.** *The name is **both** a GTUK revenue stream **and** a Light Walls
  customer — `Cinema Partners` bought **£63,567** of LED lighting and control from Light Walls in 2022
  (`archive-findings.md` finding 13 records it as Light Walls' second-largest counterparty, 12.6% of external
  revenue). **A trading identity, a partnership, a separate company, or all three at different times — the ledger
  does not say**, and it changes what the £289,645 means.* `../registers/questions.md` `Q80`.

## Sources

- `../data/derived/all-transactions.csv`, `../data/derived/gtuk-invoice-lines.csv` — the account lines
- `archive-findings.md` finding 13 — Cinema Partners as a Light Walls counterparty
- `../registers/backlog.md` `MON-7` — the carry-over floor and why
