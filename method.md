# How the work is done

**Status: proposed** — written 2026-08-17, not yet accepted. *What good looks like in this repo, drawn from
two days in which six things failed and five worked. It is method, not strategy: nothing here says what to
decide, only how to arrive at it.*

---

## The five that worked — keep doing these

**1. One question at a time, with a proposed default.**
A default means *"yes, that"* is a complete answer, and only the ones worth changing need thought. **9 of the
first 16 standards were straight accepts.** The ones that mattered were overrides, and they arrived fast
because the rest were cheap.

**2. Questions in the box, never scattered through prose.**
State them in the reply, then present them for capture. *Multiples in the box are fine. Questions embedded
across paragraphs are not — the answer lands against the wrong point, or takes a novel to give.*

**3. Every question carries its source, and the categories are unflattering.**
**Platform** (an ADR — authoritative) · **Engine** (read from the live system) · **Observed** (in the accounts
or the field) · **Repo** (this repo says so, which is weaker) · **Proposed here** (mine — you are ratifying a
suggestion, not confirming a fact) · **Unknown**. *A reader can see before answering whether they are
confirming reality or approving an invention.*

**4. Stable IDs, and the answer recorded verbatim.**
`Q17` is `Q17` forever. The answer goes in in the words it was given, because the wording usually carries the
correction — *"you are conflating"*, *"too far down the track"*, *"the concept is right"* each did more work
than the decision they came with.

**5. A status that says what is needed, not what is wrong.**
**`unestablished`** — a claim this project exists to establish · **`established`** — measured or confirmed,
with the evidence named · **`rule`** — binds, and cites what made it. **Default `unestablished`**, and anything
unestablished carries one line: *what would establish it.* **That line is what turns a marker into a work
item.**

---

## The six that failed — the rules exist because of these

**1. Grep is not reading.**
A grep returns the sentence that matched, never the argument around it. Four settled positions were re-argued
in a day by a reader who had every document available and had read none of them end to end. **If a document
governs the work, read it. If there is no time to read it, say so rather than cite it.**

**2. Inference must not wear the voice of measurement.**
~500 lines of my own reasoning went into an evidence file and became citable as fact — by me, the next day.
**Evidence may not argue. Where a conclusion is drawn from data, the conclusion and the data live in different
places.**

**3. A document existing is not evidence that anyone holds it.**
A July brand document's launch plan was read as current; a charter for a background experiment was read as
commercially load-bearing; a rung invented in this repo's own ladder was put to Neil as a question. **Ask what
a document is *for* before building on it** — the same check already applied to competitors' marketing sites.

**4. Extraction is not thinking.**
59 ADRs were generated from a template in a single script run: frontmatter, a boilerplate line, one bolded
sentence. **The source documents already held the reasoning; the extraction kept the slogan and threw the
reasoning away.** *If it can be produced by a loop, it is not a record of a decision.*

**5. Flagging is not doing.**
A banner reading *"this cites a superseded ADR"* was written, and the citation left in place. **A flag with an
obvious fix is a fix not yet made.** *~350 inline markers across the live files are the accumulated form of
this.*

**6. Old thoughts are not stale — they are the agenda.**
> *"Much of the point of this project is to establish these facts."*

**The July material is unestablished, not wrong.** Marking it *discount this* is as bad as treating it as a
rule. **The status vocabulary above exists to say which it is.**

---

## The three that failed on 2026-08-18 — and the rules they produced

*One session, one brand run, three failures with the same root: **filling a structure is not thinking.** Twenty-four
pathway cells got filled, each with a citation, each defensible alone — and a contradiction between two of the
sources never surfaced, because a contradiction has nowhere to appear when the job is populating cells. This is
failure 4 above (*extraction is not thinking*) wearing different clothes, so it gets its own rules rather than a
cross-reference.*

**1. A premise carried the work and was never stated.**
The C-ATS run stood on *nobody can size a room without ringing us*. It was false — the method is systemised and
running in Cinema Tools — and it sat inside a product record for sixteen days. **It was never available to be
broken, because it was never stated as a premise**; it was a sentence in a table that other work quietly leaned on.
It surfaced because Neil read one line of a 640-line output and said four words.

> **The rule: load-bearing premises are stated as rows before they carry anything** — `registers/premises.md`,
> with a source, what rests on it, and **what would break it**. A premise buried in a deliverable can only be
> caught by reading the deliverable. *And the corollary for asking: put premises to be broken, not options to be
> chosen. Options smuggle the framing in — two questions were asked that day, both as multiple choice, and both
> framings were wrong.*

**2. An apparent gap was declared without checking the platform.**
`CLAUDE.md` already required the platform check and it had no teeth, because it never said what *checked* means.
The repo even held the contradiction: `brands/c-ats/positioning.md` §1 named the partner-gated tool in a sentence that was
read, cited, and half-used.

> **The rule: an apparent gap is not a gap until the relevant ADRs have been read and named in the artefact that
> claims it.** Name them, or write `[?] platform not checked`. **And ask where the answer would live if it
> existed** — a calculation lives in an engine, not in a marketing folder, and that one question resolves it in a
> step. **Two documents disagreeing is the finding**, not an obstacle to filling a cell.

**3a. The platform was then checked by reading its documents, and that was the same mistake again.**
Hours after rule 2 was written, the correction built on it cited **ADR 043** (superseded by 042) and rested half
its argument on `03-c-ats-partner-tool.md` — a 24 May product document framed throughout on **ADR 019**, which
ADR 017 superseded on 13 August, describing a Level 2 surface **ADR 017 v2 decision 5 withdrew outright.** Three
files then asserted a "Tier-0 free sizing route" that had been cancelled, not deferred. `CLAUDE.md` warned this
had happened once before; it has now happened three times in one day, each time one layer deeper.

> **The rule: the ADR is the check, not the document.** A document inside the platform is evidence of what
> someone once planned, not of what is decided — `docs/` drifts, `docs/decisions/` is the record. **Before citing
> any platform document, resolve its governing ADR and read that ADR's `status` and `superseded_by`.** A
> superseded ADR is not a weaker source, it is the wrong one. *And this is failure 3 above — a document existing
> is not evidence that anyone holds it — which the platform's own frontmatter can settle in one grep.*

**3. The output was a pile of documents.**
Neil, 2026-08-18: *"we are trying to create materials that are of a quality to share but even the data share must
be of proper structured data not piles of documents. the ADRs need to manage that."*

> **The rule is in "What the work produces" below.**

## What the work produces

**Rows with stable IDs, not prose.** The point is not tidiness — it is that **more than one person has to be able
to work this process and be sure they are doing the same thing.** A narrative document cannot give that
assurance: it cannot be diffed meaningfully, queried, checked for completeness, or lifted into engine. A register
can.

- **Default to a register.** `registers/` is state in rows. If the thing being produced has instances — pieces,
  premises, questions, products, segments — it is rows, and prose is at most its preamble.
- **Data leaves as data.** A measured cut is a script and a CSV (`data/derived/`), with the reading of it kept
  separate. **Never a table typed into a document**, which is a copy that immediately starts drifting.
- **Prose is for argument only** — `group-strategy/` and `motion/`. An argument is the one thing rows cannot hold.
- **The test: could a second person work from this and be certain they were doing what the first did?** If the
  answer needs them to have read a document end to end and taken the same reading from it, it is the wrong shape.

**Decisions that bind the platform are ADRs, and this repo does not write them.** `cinema-platform` runs a real
ADR set — `docs/decisions/` at platform level (0001–0016), `products/<product>/docs/decisions/` per product
(cinema-tools: 87 files, all `scope: cinema-tools`) — governed by `docs/conventions.md` and by ADR 079, which
versions rather than amends.

**What leaves here is a decision request, not an ADR.** An ADR is a *record of a decision*, numbered in the repo
that owns it. A file in `operations/` with a placeholder number and borrowed frontmatter is neither — it is a
document in ADR costume, and it fails the same test as any other pile of prose. So:

- **It carries an ID in this repo's namespace** (`DR-<question-id>`), keyed to its row in `registers/questions.md`.
- **It never guesses the destination's number**, its frontmatter, or whether it supersedes anything. Whether it
  lands as a new ADR or as a new *version* of an existing one is the owner's call under ADR 079.
- **It states the contradiction, the proposed decision and the consequences as tables**, because that is what a
  second person can act on without reading it end to end.
- **If accepted, the owner creates the ADR in their repo.** That is the moment it becomes an ADR, and not before.

*(First instance: `operations/decision-request-q52-cats-rules-publication.md`, 2026-08-18 — and it took a
correction from Neil to get its shape right, having first been drafted as a fake ADR numbered `<n>`.)*

**And the standing rule that survives all of this unchanged:** no `decisions/` folder in this repo, ever. Tried
twice, deleted twice — see below. **Somebody else's ADR set is not this repo growing one.**

## The drill-down — how a claim gets confirmed

*Added 2026-08-18, from the C-ATS brand-truth run. **The method that produced more correction in twenty minutes
than the preceding six hours of building.** Neil: "1 paragraph became 15 data points! …this is exactly the power
of drilling down."*

**The problem it solves:** a paragraph can be read, nodded at and marked settled while carrying a wrong claim
inside it. `brands/c-ats/positioning.md` is 249 lines describing what the brand is, who it is for, what it
promises and why it is credible — with **zero attributions to Neil in the whole file.** It was drafted by a
session, never checked, and then cited as settled strategy by every piece of work that followed, including mine.
**Nobody lied. The confirmation step was simply never performed, and prose is where that is invisible.**

**The five steps:**

1. **Take one section. Not a file, not a brand — a section.**
2. **Atomise it.** Split until every row is a single claim that could be true or false on its own. One paragraph
   of C-ATS positioning gave **fifteen**. The count being surprising is the point; that surprise is the measure
   of how much was riding on an unexamined passage.
3. **Sort each row by who owns it** — is this a **brand** claim, a **product** fact, a **service**, or a **gap**?
   **This is where the duplication surfaces.** Five of C-ATS's fifteen were `product-records.md` reproduced word
   for word, which means the strategy document was not standing on the record but copying it — two files free to
   drift apart, and nobody would see it until they disagreed.
4. **Put the rows to the owner, and record the words back.** Confirmed rows carry a date and a name. **A row is
   not confirmed because the paragraph containing it was** — anything singled out keeps its own status.
5. **Regroup only after confirming.** Grouping is safe once each atom is checked; grouping first is how fifteen
   claims hide inside one sentence again.

**Where the rows live:** `brands/<brand>/claims.md`, one register per brand. **The prose file stays** — it is
where the argument lives, and rows cannot hold an argument — **but the register is what says which parts of it
anyone has actually agreed to.**

**Two things the first run showed, likely to repeat:**

- **The real brand story is one or two rows.** Thirteen of C-ATS's sixteen were product facts, restatements, or
  gaps. **The row that said why the brand exists was a single sentence** — and it had never been confirmed.
- **Atomising finds holes, not just errors.** "A design service specifies them; verification proves they worked"
  passed as ordinary prose. As rows it is immediate: both are named in every C-ATS document and **described in
  none.**

## The shape of a working session

1. **Read what governs it, end to end.** The owning area document, this file — **and the platform's ADRs where
   the work touches them.**
2. **State the premises.** What is this about to stand on, and what would break each one — rows in
   `registers/premises.md` before a line of the deliverable is written.
3. **Work in the register.** Questions get IDs before they get asked.
4. **Ask, apply, ask.** No essay between the answer and the next question. **Premises to break, not options to
   pick.**
5. **Record the answer verbatim, and what it changed.** If it changed nothing, say so.
6. **Correct in place and visibly.** A struck line with its reason is worth more than a clean one that hides a
   reversal — **and a broken premise is kept, never deleted**, because the work built on it has to be findable.

## Two things to say out loud rather than resolve quietly

- **"I do not know"** — with the `[?]` and what would answer it. *159 of those already exist and they are the
  healthiest thing in the repo.*
- **"That was mine, not measured"** — when a claim is inference. **The cost of not saying it is that somebody
  builds on it, and the somebody is usually the next session.**

---

## Where things live

**One kind per file**, and the folder says which kind: **`group-strategy/`** argument · **`motion/`** the
machinery · **`brands/`** application · **`registers/`** state, in rows · **`evidence/`** measured,
append-only · **`operations/`** what leaves the repo, **including ADRs drafted for `cinema-platform`** ·
**`data/`** the source, as scripts and derived files rather than as tables typed into documents.

## `decided.md` is a machine input, not a record

**Neil, 2026-08-17: SRND OS reads `decided.md` every morning and tries to react to it.** That single fact
governs everything about the file:

- **It holds business process and management decisions only** — things the OS should act on.
- **Repo management never goes in it.** How ADRs work, where files live, how questions are logged: **none of
  that is the OS's business**, and putting it there makes a machine try to act on a filing convention. *That is
  what the ~60 mixed entries were doing, and it is why they were mess.*
- **Nothing enters it without Neil's explicit approval**, and nothing about the business has been decided yet,
  so **it is empty and stays empty until something genuinely is.**
- **SRND OS is the source of record for what is decided.** This repo is where a decision is *worked out*, not
  where it is kept.

**So there are two kinds of decision here and only one of them is the OS's:**

| | Where it goes | Who acts on it |
|---|---|---|
| **Business or management** — pricing, territory, what we sell, who we sell to | `decided.md`, once Neil decides it | **SRND OS, every morning** |
| **Repo management** — conventions, structure, how questions are logged, how a session runs | **this file** | Whoever is working in the repo |

***ADRs were tried twice and the answer is settled: no `decisions/` folder, ever.*** *The first attempt
(2026-08-16) scraped 59 stubs and was deleted entire. The second (2026-08-17) wrote three proper ADRs and was
removed the same day, on Neil's challenge, for being a third copy of what the repo already holds. The decision
record is what exists:* **`registers/questions.md` holds the act of deciding** *(permanent Q-ids, the answer
verbatim, dated),* **the owning area or brand document states the current position** *(rewritten wholesale when
it changes, organised by level — never a separate file per decision),* *and* **`decided.md` is the machine
interface for SRND OS.** *A future session that finds itself creating a decisions folder is repeating a
mistake made twice.*

### The three rules the deleted convention was worth keeping for

- **A number is permanent; content is versioned.** A decision that changes is rewritten in place — no
  amendment notes, no "see also" chains. *This is why `ADR 017` still resolves at version 2 while
  `decided.md`'s IDs vanished the moment the file was emptied.*
- **A decision is written when it is made, by the person making it** — never scraped out of a pile afterwards.
  *59 were, by script, and all 59 were deleted.*
- **An index of decisions is generated, never hand-maintained.** *The platform's hand-written one drifted to
  covering 41 of 70 in three months, with nine rows disagreeing with their own files.*
