---
id: 1
scope: srnd-group-strategy
slug: adrs-in-this-repo
area: governance
title: "ADRs in this repo: proposed until Neil accepts, versioned not amended, catalogue generated"
status: accepted
version: 1
revised: 2026-08-16
supersedes: []
superseded_by: null
---

# ADR 0001 — ADRs in this repo: proposed until Neil accepts, versioned not amended, catalogue generated

- **Status:** **Accepted** — 2026-08-16, Neil. *The first ADR ratified under its own decision 3.*
- **Adopts:** the convention already running in `ceenhad/cinema-platform` — ADRs 001–079, frontmatter,
  permanent numbers, generated catalogue — and in particular **Cinema Tools ADR 079**, *"ADRs are versioned,
  not amended."*

## Context

**This repo has never used ADRs.** It used `decided.md` — sixty-odd entries written by working sessions
summarising conversations, never ratified entry by entry — plus roughly **350 inline status markers**
(`▲ ⚑ ⚠ ▶`, "struck", "retired", "reframed") scattered through prose in fourteen files.

**On 2026-08-16 that failed measurably.** In one working day a session re-argued four settled positions,
invented a rung in a documented ladder and put two questions to Neil about things that did not exist. The
same day, `decided.md` was emptied on Neil's instruction — *"that is being monitored by SRND OS and all this
shit is just mess now"* — and its contents moved to `proposals.md` as unratified.

**The failure mode was diagnosed three days earlier, in another repo, by the same decision-maker**
(Cinema Tools ADR 079, 2026-08-13):

> *"Trying to retire ADR docs doesn't work, **you like to grep and thus miss any rules at the start of docs**
> etc. Finally there is no content-based organisation of the documents."*

That is a description of what happened here. **The counter-measure already exists and this repo does not use
it.**

## Decision

**1. Decisions in this repo are recorded as ADRs**, in `decisions/`, one per file, named
`NNNN-slug.md`.

**2. The frontmatter is the platform's**, so the two repos are readable by the same eye and can cross-cite:
`id · scope · slug · area · title · status · version · revised · supersedes · superseded_by`.
**`scope: srnd-group-strategy`** distinguishes these from Cinema Tools and platform ADRs.

**3. `status: proposed` is the default, and only Neil moves it to `accepted`.** This is the mechanism behind
*"nothing goes in decided.md without my explicit approval"* — a proposal is written freely, and ratification
is a separate, explicit, dated act. **A `proposed` ADR binds nothing and may not be cited as settled.**
Statuses: `proposed · accepted · superseded · rejected`.

**4. A number is permanent; content is versioned.** A decision that changes is **rewritten in place** —
`version` and `revised` move, the number every citation depends on stays still. **No amendment notes, no
"see also" chains, no partial supersession.** *This is ADR 079's core rule and the reason `ADR 017` still
resolves at version 2 while `decided.md`'s IDs vanished the moment the file was emptied.*

**5. The catalogue is generated, never hand-edited** — `decisions/CATALOGUE.md`, built from the frontmatter
by `scripts/adr_catalogue.py`. *The hand-maintained equivalent in the platform drifted to covering 41 of 70
in three months, with nine rows disagreeing with their own files. A hand-maintained index here would rot
faster, because this repo has fewer readers.*

**6. An ADR belongs to one functional area, and is written when a decision is made in it — never scraped out
of a pile afterwards.** The areas are **Group · Motion · Brand · Registers · Evidence · Operations** (Neil,
2026-08-17).

> **⚠ This decision is written from a failure, on 2026-08-16.** `proposals.md`'s ~60 entries were extracted
> into 18 ADRs, then split into 59, **by script, from a template**. Each was frontmatter, a boilerplate status
> line, one bolded sentence and a provenance footer — **no context, no consequences, no reasoning.** Neil:
> *"rarely did I see a worse interpretation."* **All 58 were deleted; only this ADR survives.**
>
> **What went wrong is worth keeping:** the source documents already held the reasoning, and the extraction
> threw it away and kept the slogan. **An ADR is a document — the context that made the decision necessary,
> the decision, and what follows.** A one-line restatement of something already written better elsewhere is
> not an ADR; it is a worse copy with a number on it.
>
> **So: no retrospective ADR sweeps.** Where a position already lives in a group document, it stays there. An
> ADR is written when something is actually decided, by the person deciding it.

**7. SRND OS remains the source of record for what is decided.** ADRs are how a decision is **made and
recorded here**; what is accepted belongs in SRND OS. **This repo is not a second decision database**, which
is the mistake `decided.md` became.

**8. Inline flags are not decisions.** A `▲` or a "struck" in prose is either an ADR, a `questions.md` row,
or noise. **The `[?]` markers are different** — they are evidence gaps in `current-state.md` and stay exactly
where they are.

**9. Every document carries a status line, because the corpus is mostly old thinking and nothing says so.**
*Neil, 2026-08-16: **"It's pulling old thoughts and treating them as hard rules."*** That is the failure
underneath every other failure of that day, and the dates make it plain:

| | Last touched | What it is |
|---|---|---|
| All nine `brands/*/positioning.md`, `brand-data.md`, `opportunity.md` | **2026-07-24 → 07-28** | Written in the first strategy pass |
| `02-buyer-journey`, `03-partner-programme`, `05-channels`, `06-competitors` | **2026-07-28 → 07-31** | Same pass |
| `archive-findings`, `engine-audit`, `data/` | **2026-08-13 →** | **The measured layer, three weeks later** |

**So the corpus has two eras and no marker between them.** A July claim and an August measurement read
identically, and a reader gives them equal weight — which is how *"v1 launch market: commercial cinema"* in a
July brand document became a live plan in a working session, and how the July `decided.md` entries became a
ratchet.

> **⚠ And the obvious correction is the wrong one — Neil, 2026-08-16:**
> ***"Much of the point of this project is to establish these facts."***
>
> **The July material is not stale and must not be marked as such.** It is **the agenda** — the claims this
> project exists to establish. A first draft of this decision called the default `thinking`, which reads as
> *discount it*; that is precisely backwards. **An unestablished claim is not noise. It is the work.**

**Therefore: the first line of every document states what it is, and the vocabulary says what is *needed*
rather than what is wrong with it.**

> **`Status:`** **`unestablished`** — a claim this project exists to establish · **`established`** — measured,
> or confirmed by Neil, with the evidence named · **`rule`** — binds, and cites the ADR that made it ·
> **`superseded by X`** · **`closed DATE`**
>
> **Plus, for anything `unestablished`: what would establish it.** *One line. A measurement, a fetch, a
> question, a conversation with a dealer.* **That line is the difference between a status marker and a work
> item**, and it is what turns the brand layer from a pile of assertions into a backlog with a method.

**The default is `unestablished`.** *Nothing here binds unless it says it does* — the only default that fails
safe, and the honest description of most of the repo.

**Two consequences worth naming.**

- **Most of the brand layer will carry `unestablished`, and that is not a criticism of it** — it is the state
  a first strategy pass leaves things in, and naming it is what makes the second pass possible.
- **This is what `GRP-2`, the per-brand question sweep, is *for*.** Not to re-write the brand documents, but
  to walk each claim from `unestablished` to `established` or struck. **The sweep and the status vocabulary
  are the same mechanism**: the status says what is needed, the sweep is how it gets got.

*And the `[?]` markers in `current-state.md` are this idea already working at field level — a named unknown
with a place to land. **They are the model, not the exception.***

## Consequences

- **`decided.md` stays empty and is deleted once the citations are reconciled** (`DOC-28`).
- **`proposals.md` is worked through into ADRs**, each `proposed`, then accepted or rejected one at a time —
  the ratification pass, with a mechanism instead of a promise.
- **~142 dangling `decided.md` citations** get repointed at ADR numbers as each is written, which is why the
  citation reconciliation and the ADR pass should run together rather than twice.
- **The repo gets a `scripts/` directory** for the first time, holding the catalogue generator.

## What this ADR does not do

It does not decide the folder restructure proposed in `structure-proposal.md` — **that is separate and can
wait.** Adopting ADRs does not require moving anything else, and doing the folders first would move the same
mess into a tidier arrangement.
