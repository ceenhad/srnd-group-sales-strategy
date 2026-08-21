# C-ATS — what closes this phase

Written 2026-08-21 on Neil's question: is the work to complete this phase of the C-ATS run actually captured, after
a session that lost its way. Tested against the run's own definition in `../_template/the-brand-run.md`
§ "What a completed run looks like" rather than against a new list.

## Against the template's five deliverables

| The template requires | State |
|---|---|
| A pathway per entry door, every slot with its honest state and handoff | **Done, and re-keyed.** `pathways.md` is the row form; the three `pathway-*.md` files hold the per-door argument. Entry is `M1`–`M3`, the three project moments Neil confirmed |
| `hooks.md` — candidates with provenance, rejections with reasons, blocked hooks named | **Done, and thin by admission.** `S1` is empty on two doors and dead on the third. The hook wording is an owner's, not a session's |
| The segment cut and `segments.md`, with the script | **Done.** `../../evidence/2026-08-18-cats-segment-cut.md`, reproducible |
| `training.md` — a row per opportunity with audience, route, traced subject, precondition, limit, state | **Done.** Five rows, three rejections with reasons. `T2` and `T5` drafted; `T1` blocked on one classification |
| The run ends as a work queue, not a document | **Done, and now weighted.** The queue is in `../../registers/backlog.md` with weight and scope on every live row |

**So the run is structurally complete.** What is open is not the run — it is four things the run surfaced.

## The four things that close the phase

### 1. Four drafts need a truth-check, and one needs reading first

`draft-t2-decide-before-the-wall.md` · `draft-t5-layout-tolerance.md` · `draft-answers.md` ·
`draft-n7-client-leave-behind.md`.

Read `draft-answers.md` against the published knowledge base before correcting it: it re-derived answers that were
already live on the site. That is the one place this phase produced waste.

### 2. One rule violation, and it is on a published page

`SIT-9` — an article files the Reflection Control Panel under a "Diffusers" heading. `C5.15` forbids the word on the
product, and the record had already caught the legacy brochure doing the same thing.

### 3. Three fetches, each one input, each unblocking more than itself

- **`DAT-3` / `DOC-7`** — the current EN 13501-1 classification. It blocks `T1`, which is the strongest training row
  because it is the only subject a dealer cannot finish the job without.
- **`DOC-8`** — marine provenance, now answerable from the published BSRIA report: one commission, "3 materials in 8
  configurations", and the marine sheet in the same April 2023 batch.
- **`DOC-17`** — `O1`, `O3` and `W2`'s remainder in the dealer's own words. One input unblocks eleven record fields.

### 4. Two decisions with a brand scope

`KNW-4` (commission the remaining tests, or declare the current data the limit) and `KNW-7` (whether the treatment
design service adopts the staged-deliverable shape the isolation ladder already runs). `DEC-1` — the canonical name —
is a third if the legal form matters for copy.

## What is explicitly not part of closing this phase

- **`P2`, isolation.** A sold layer with one clause of plan behind it, and per `C1.40` the layer that reaches a
  project first. That is a phase of its own, not a loose end of this one.
- **`EST-20`, standard rooms with layouts.** Half done — geometry from the platform's own sweep, no finish schedule
  per room, and the model needs tuning. It waits on Neil, not on this run.
- **`DR-Q52`.** Answered by publication rather than by decision. Closing it formally is the platform owner's, and
  doing so probably un-gates `T4`.
- **The prose-to-rows rewrite** of the three `pathway-*.md` files, `hooks.md` and `segments.md` (`PR-9`). Real debt,
  but it is a reshaping of finished work.

## The engine thread, which did not drop

It is in `../../operations/engine-measurement-spec.md` — six deltas between the KPI framework agreed with Neil on
2026-08-14 and what engine measurably holds, written as a specification for the dev team because we do not write to
engine from here.

`D1` the account types · `D2` nowhere for a campaign tag to land · `D3` the inbound log as one column, not a table ·
`D4` the signal matrix missing its first and middle tiers · `D5` three existing columns nobody fills · `D6` `G5` is a
definition, not a build. Plus what is computable today, and four things that are Neil's rather than the dev team's.

The queue for it is `ENG-20` → `ENG-24` → `JNY-10` → `ENG-21`/`ENG-22`, and the order matters: nothing measures
until `customers.customer_type_id` is populated.

## The repo access boundary — tested 2026-08-21, do not retry

**A session on this repo cannot read `SRND-Group/srnd-engine` or `SRND-Group/srnd-os` by any route.** Three were
tried:

| Route | Result |
|---|---|
| `add_repo` | Refused: cross-tier adds unsupported; this session's sources are under `ceenhad` |
| `git clone` | No credentials for `github.com` in this session |
| GitHub API | *"Access denied: not configured for this session. Allowed repositories: `ceenhad/srnd-group-sales-strategy`, `ceenhad/cinema-platform`"* |

**It is not a rights problem** — the account has push on both SRND repos. The session's repo allowlist is fixed at
launch and holds only the two `ceenhad` repos, which is why `cinema-platform`'s ADRs are readable and the SRND ones
are not.

**Neil's intent, 2026-08-21:** read-only both ways, *"as those are where our internal tooling comes from just as they
don't want to write here… to not mix our work."* **The current boundary already enforces that** — nothing here can
write there and nothing there can write here. What it costs is that no single session reads across.

**So the working arrangement is the one already in use:** engine work that needs the application code happens in a
session opened on the SRND repos, and what lands here is a specification —
`../../operations/engine-measurement-spec.md` is exactly that. **Any answer to `Q40` ("what is `srnd-os`?") has to
come from such a session, or from Neil.**

*The alternative, if one session ever needs all four: an org owner adds the `SRND-Group` repos to this workspace's
allowed set in the Claude GitHub settings.*
