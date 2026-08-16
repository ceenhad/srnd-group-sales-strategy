# A cleaned-up structure — proposal

**Proposal only. Nothing moves without approval.** *Written 2026-08-16 after a complete read of the repo:
68 markdown files, 16,356 lines.* **This file is disposable** — it gets executed or rejected, then deleted.

---

## 1 · What is actually wrong

**Not size. Five different kinds of thing are mixed together with nothing marking which is which.**

| Kind | Example | How it should behave | What actually happens |
|---|---|---|---|
| **Argument** — why | `00-strategy.md`, `08-sales-motion.md` | Stable. Rarely changes. Re-argued never | Correct |
| **Design** — the machinery | `09-motion-design.md`, `10-tasks.md`, `11-work-items.md` | Changes when the design changes | Correct |
| **Evidence** — what is measured | `archive-findings.md`, `engine-audit.md`, `current-state.md` | **Append-only. Never carries argument** | **Broken — `archive-findings.md` is 2,083 lines and its last two findings argue group strategy** |
| **Ledgers** — open, asked, proposed | `open-items.md`, `questions.md`, `backlog.md` | High churn. Short rows, no prose | **Broken — `open-items.md` is 840 lines and holds four different documents** |
| **Application** — per brand | `brands/` | Inherits, never forks | Correct |

**And two more faults on top of that:**

- **Closed things sit in the live set.** `10-tasks-qa-sheet.md` (448 lines, a run that closed on 2026-08-08)
  and `2023-buyer-journey-archive.md` (evidence recovered from Dropbox) are numbered alongside live design
  documents. **A banner saying CLOSED is not a structure.**
- **The numbering implies a reading order that does not exist.** `00`–`15` looks like a sequence. It is not:
  `10`–`13` are one chain, `02`/`04`/`08`/`09` are four views of the same motion, `14` and `15` are session
  outputs, and `15` is younger than `13` but supersedes parts of it.

> **The measurable consequence, from today:** four settled positions were re-argued in a day, a rung was
> invented in a ladder, and two questions were put to Neil about things that did not exist — **by a reader
> who had the whole repo available and could not see its shape.**

---

## 1a · The bigger answer: this repo should use ADRs, and the group already has them

*Added after Neil asked: "are we not using ADR in this repo yet?" **No. And the convention exists, works, and
was written to counter exactly the failure this repo just had.***

**`cinema-platform` runs ADRs 001–079** with frontmatter (`id · status · version · revised · supersedes ·
superseded_by`), permanent numbers, content-based areas, and — the part that matters most here — **a
generated catalogue** (`adr_catalogue.py`), not a hand-maintained index.

**And `ADR 079` exists because of a diagnosis Neil made on 2026-08-13:**

> *"You love to make an ADR a locked document which makes sense from version control but automatically leads
> to a sprawl… **Trying to retire ADR docs doesn't work, you like to grep and thus miss any rules at the start
> of docs** etc. Finally there is no content-based organisation of the documents."*

**That is a description of this session.** I grepped, missed the rules at the tops of documents, and re-argued
four settled positions.

### What ADRs fix that today's scaffolding does not

| Fault seen today | `decided.md` / `proposals.md` | An ADR |
|---|---|---|
| **Nothing was ratified** | An entry saying *"Neil's decision"* written by a session | **`status: proposed` → `accepted`, with a decision-maker and a date.** This *is* the "nothing without my approval" mechanism |
| **The floor rate was struck invisibly** | A reversal buried in a list at the foot of a file | **`superseded_by: 0yy`** in the frontmatter, and in the catalogue |
| **~142 citations now dangle** | IDs that vanished when the file was emptied | **A number is permanent and its content is versioned** — `ADR 017` still resolves at v2 |
| **~350 inline flags nobody can track** | `▲ ⚑ ⚠ ▶`, "struck", "retired" scattered through prose | **A generated catalogue with a status column** |
| **Two repos, two conventions** | Strategy decisions look nothing like platform decisions | **One convention across the group**, so they cross-cite |

### What it means concretely

- **`proposals.md`'s ~60 entries become candidate ADRs.** Each is proposed, and becomes `accepted` only when
  Neil says so — which is the ratification pass, given a mechanism instead of a promise.
- **`decided.md` stays empty and dies.** SRND OS holds what is decided; ADRs are how a decision gets *made*
  and recorded here before it goes there.
- **Most inline flags disappear.** A `▲` in prose is either an ADR, a `questions.md` row, or noise. *The 159
  `[?]` markers are different — those are evidence gaps and stay in `current-state.md`.*
- **The catalogue is generated, never hand-written.** A hand-maintained index is the thing that rots; the
  platform already proved that with a script.

**Adopting it is coherence, not invention** — the group's own convention, already working, already Neil's.

## 2 · The proposed structure

**Folders by *kind*, because kind determines how a file is read, how fast it goes stale, and what may be
written in it.**

```
README.md              the front door — what this is, how to read it, where to start
CLAUDE.md              the constitution
NEXT.md                the plan — what happens next

strategy/              WHY. Stable, argued once, re-argued never.
  the-group-play.md        (00-strategy)
  commercial-model.md      (01)
  buyer-journey.md         (02)
  partner-programme.md     (03)
  competitors.md           (06)
  channels.md              (05)

design/                HOW. The machinery. Changes when the design changes.
  sales-motion.md          (08)
  motion-design.md         (09)   ← the master; 02/04/08 feed it
  content.md               (04)
  tools.md                 (07)
  tasks.md                 (10)
  work-items.md            (11)
  task-shapes.md           (12)
  standards.md             (13)
  engine-as-hub.md         (14)

record/                THE PRODUCT LAYER. Unchanged — it already works.
  schema.md · template.md · register.md

evidence/              WHAT IS TRUE. Append-only. No argument, ever.
  current-state.md         the baseline
  archive-findings.md      the measured findings — findings only
  engine-audit.md
  direction.md             (15 — the group read; see §4, it may not survive)

decisions/             ADRs — the group's existing convention (see §1a)
  CATALOGUE.md             GENERATED, never hand-edited
  0001-….md                one decision per file; number permanent, content versioned
  …                        proposals.md's ~60 entries enter here as `status: proposed`

ledgers/               WHAT IS OPEN. Short rows. No prose.
  open-items.md            open items that are not yet decision-shaped
  questions.md             the asking surface
  backlog.md               the action register

brands/                unchanged
data/                  unchanged
archive/               CLOSED AND SUPERSEDED. Dated. Never cited as live.
  2026-08-08-tasks-qa-sheet.md
  2023-buyer-journey-archive.md
  2026-08-14-store-split-worklist.md
  adjacency-map.md → moves to design/ if live, here if not
```

**Numbering goes.** A filename says what a document is; the folder says what kind it is. Nothing else is
needed, and the false sequence disappears.

---

## 3 · The rules that make it hold

**A structure without rules degrades back to a pile in a month.** Five, and each one is a fault seen today:

1. **One kind per file.** **Evidence may not argue; ledgers may not narrate; strategy may not hold work
   items.** *`archive-findings.md` findings 31 and 32 broke this — measured evidence carrying group-level
   strategy — and that is why they were mistaken for settled positions.*
2. **A ledger row is a row.** If an `open-items.md` entry runs to three paragraphs it is a document; move it
   to `strategy/` or `design/` and leave a one-line row pointing at it. *`open-items.md` is 840 lines and
   contains a stress test, an engine-direction essay, a sessions list and a decision ledger.*
3. **Closed goes to `archive/` the day it closes.** Not a banner.
4. **Every document carries a status line at the top** — *live · superseded by X · closed on DATE* — so it is
   visible in the first line, not inferred from a date somewhere in the middle.
5. **Nothing enters `decided.md`, ever, without Neil.** SRND OS is the source of record. *This one is
   already stated; it belongs in the list because it is the one that matters most.*

---

## 4 · Three things to decide, not just move

**Moving files is mechanical. These are judgements, and I would rather ask than assume.**

- **`archive-findings.md` is 2,083 lines and doing two jobs.** The 30 measured findings are evidence;
  findings 31 and 32 — the service-revenue read and the LWCP review — are argument that happens to cite
  evidence. **Split them, or accept that the evidence file argues?** *My view: split. It is what let me
  treat my own reasoning as measured fact.*
- **`group/15-direction.md` may not deserve to exist.** It was written this morning, then corrected three
  times in a day — priority-one demoted, single-brand dealers qualified, personal authority added. **It reads
  as a session transcript rather than a document.** *My view: fold its measured content into
  `evidence/current-state.md`, fold its conclusions into `NEXT.md`, delete the file.*
- **The four motion documents overlap heavily.** `02-buyer-journey`, `04-content`, `08-sales-motion` and
  `09-motion-design` say related things at four altitudes, and `09` explicitly assembles the other three
  (*"the assembly is what was missing"*). **Merge into one, or keep four and make `09` the entry point?**
  *My view: keep four — each is genuinely a different altitude — but say so at the top of each, which they
  currently do not.*

---

## 5 · What it costs

**The moves are half a day and mostly mechanical** — `git mv`, then fix the cross-references.

**The cross-references are the real work**, and they are already broken: **~142 references to `decided.md`
across 28 files** point at an emptied file (`DOC-28`), and every relative link between group documents changes
when the folder does. **Doing the folder move and the citation reconciliation as one pass is cheaper than two**,
because both touch the same 28 files.

**What I would not do:** rewrite content while moving it. *Move first, verify nothing broke, then correct.
Mixing the two is how a reorganisation becomes an unreviewable diff.*

---

## 6 · What to do first, if any of it

**The ADRs matter more than the folders**, and they can start without the move:

1. **Adopt the ADR convention** — copy the platform's frontmatter, meta-rules and catalogue script. *Half a
   day, and it makes everything after it cheaper.*
2. **Run `proposals.md` through it** — each entry proposed, then accepted or dropped by Neil, one at a time,
   the way the register already works. **That is the ratification pass, with a mechanism instead of a
   promise.**
3. **Then the folders and the citation reconciliation**, as one pass over the same 28 files.

*Doing 3 first would move ~350 flags and 142 dangling citations into a tidier arrangement of the same mess.*

## 7 · The one-line version

**Use the group's own ADRs for decisions; sort everything else by kind; archive what is closed; keep ledgers
to rows; and let no file both measure and argue.**
