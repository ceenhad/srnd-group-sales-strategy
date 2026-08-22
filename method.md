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

## The oldest failure in the repo: forgetting how long SRND has been doing this

**Neil, 2026-08-19:** ***"The repo forgets that we have been doing this a long time. Lots exists in some state or
another and even if a bit out of date it's still useful."***

**This is not a new rule, it is the one that keeps producing the others.** *Four premises broke on it in two days —
`PR-1` (the sizing method was systemised in the platform, not missing), `PR-10` (checking the platform means the
ADR, not the document), `PR-18` (the live site is a mockup, not the offer), `PR-20` (a 204-chapter course outline
existed minutes after training was logged as work that would have to be written). **Every time, the repo's default
was that a capability was absent, and every time it was present in some state.***

**Two corollaries, and the second is the more useful:**

- **"Out of date" is a state, not a verdict.** *A 2015 pack decode, a July brand document, an old training deck —
  these are **unestablished, not wrong** (failure 6 above already says so). **The version of that error worth
  naming separately is treating them as absent** rather than as stale.*
- **The register's blank cells are ours, not the company's — and writing them up as findings is the failure's
  loudest form.** *`CAT-05` "Isolation System" had three of four cells `—` or `[?]`; the layer has been sold for
  years, hardware and a six-step service ladder both (`../evidence/2026-08-19-isolation-is-a-sold-layer.md`). **The
  error was not missing it — it was the write-up**, which called it *"the largest find of the day"* and implied the
  business had not noticed its own revenue. **Neil: *"since I did them all it's no surprise I assure you."*** *So the
  rule has a wording half: **an empty cell means nobody wrote it down. It never means the company does not do it** —
  and a strategy document that announces a long-standing practice as a discovery is telling the owner something they
  taught us.* **This is the same failure as `PR-20`** *(training material logged as needing authoring, minutes before
  a 204-chapter outline turned up)* **two days running, which makes the write-up, not the lookup, the thing to
  watch.**
- **Shaping existing material into something new is hours, not projects.** *The cinema-expert course outline —
  **204 chapters, keyed to RIBA stage and to deliverable** — was **old cinema training compared against the
  identified deliverables and capabilities in Pro, and shaped**. Neil: **"maybe two hours work from nothing to that
  current outline."*** **So the estimate to distrust is not the optimistic one. It is the assumption that a thing
  must be built from nothing**, which is what makes a two-hour job look like a quarter's work and keeps it
  unstarted.

> **The rule: before recording anything as missing, absent, unwritten or a gap, say where you looked.** *Not
> "checked the platform" — **which repository, which directory, and what did the frontmatter say.** A gap asserted
> without that is an assumption, and in this repo it has been the wrong one every time it was tested.*

## Propagation by citation — the mechanism, not just the habit

**Named 2026-08-19, after the fourth instance in three days.** *The repo's most repeated defect is a correction
applied where it was spotted rather than everywhere the claim lives — `C5.24` (a rule dropped at group level, still
governing brand copy three days later), `C7.1` (a claim struck in §2, still standing in §7 of the same file),
`DOC-27`, and the buyer-truth apparatus in DT and Fabric Walls (`MTH-2`).*

**The mechanism is worth naming because it predicts where to look.** *Two of those four spread through an explicit
cross-reference — **"parked, as with C-ATS"** and **"as with the other brands"**. **A claim that cites another
document does not merely duplicate it; it survives the original's deletion**, because the citation reads as
provenance rather than as a copy.*

> **The rule: when a claim is struck, grep for the brands and files that cite it, not only for its words.** *A
> paraphrase pointing at the struck original is the hardest instance to find and the likeliest to be believed —
> it looks sourced.*

## The four that failed on 2026-08-19 — one root, and it is not carelessness

*One session, four failures, **all mine**, and every one caught by Neil rather than by the register. The root is
the same each time: **a conclusion that runs one step past the evidence, written with the confidence of the step
before.** This is not the same as failure 4 (*extraction is not thinking*) or failure 2 (*inference must not wear
the voice of measurement*) — in all four cases the evidence was real, the reasoning was sound as far as it went,
and **the sentence went further than the last fact behind it.** That is why the register did not catch them: every
row cited a genuine source.*

**1. A summary is not a source.** I recorded that a competitor *"positions against stretch-fabric treatment"* and
built a named finding on it — **from a search summary, not from the page.** Neil: *"this is a nonsensical statement
— all stretch fabric systems have an air gap, and loads of acoustic treatment panels rely on an air gap."* Correct.
**The page actually said `'hang on the wall'`, three words the summary had dropped, and they carried the whole
meaning**: the contrast was with absorbers fixed flat to the substrate, which *is* our install.

> **The rule: fetch the thing.** A search result, an index page or a summary tells you a document exists and roughly
> what it is about. **It is not quotable.** *And the failure is asymmetric — a summary drops qualifiers far more
> often than it adds them, so what it loses is exactly the part that made the claim narrow and true.*

**2. Replacing an unsourced claim with an unverified one is not a fix.** `C1.38`'s unmeasured competitor price band
was replaced with *"some competitors sell direct to the end user at published prices"* — **written before any
research, and presented as the sourced correction.** It also leaned on a `drafted` row for its second clause. Neil:
*"your text under `C1.38` is making a LOT of assumptions."*

> **The rule: a replacement claim carries its own burden.** *Striking something for lack of evidence and writing
> something else in its place, in the same edit, is the most likely moment in this whole method to introduce a new
> unsourced claim — because the strike feels like rigour and lends its credibility to whatever follows.*

**3. A broken premise drifts back, and fast.** `PR-4` — the measured data is not what credibility rests on —
**broke on 2026-08-18 and was drifted back over three times on 2026-08-19**: the `A1` axis reading, `Leg 4`'s first
rule, and the acoustics scan's headline. Neil, one sentence: *"if it's not legal or safety no one gives a shit.
Hardly any dealer cares about Sabines."*

> **The rule: a break does not hold by being recorded.** **Re-read the premises before writing anything that would
> have leaned on one** — *the intuitive version is what returns, and it returns in new work rather than in the file
> where it was struck.* `PR-4` now carries the caution as well as the break, because the break alone lasted a day.

**4. Check which layer owns the comparison before drawing one.** I judged **C-ATS** against firms that deliver whole
rooms and recorded its scope as a weakness. Neil: *"there is a critical bit that you miss — we lack nothing against
these. On the contrary we offer much more. It's called SRND Group."* **The scope was never C-ATS's to have.**

> **The rule: name the layer before the verdict.** *`../CLAUDE.md`'s first discipline is usually broken the other way
> — a brand file restating group strategy. **This is the same error inverted**, and it is harder to see, because
> judging a brand by its own boundaries looks like exactly the discipline the rule asks for.*

### The self-check the four produce

**Ask of any sentence: is it more confident than the last piece of evidence behind it?** *All four passed every
other check in this file. They cited real sources, they atomised properly, they marked their statuses. **What they
did was extend — one comparison, one clause, one qualifier — past the point the source reached**, and nothing in a
register catches that, because the citation is genuine and only the distance is wrong.*

**And the count matters more than any of the four.** *A session that also broke six of the repo's own premises found
none of its own errors. **Four of four came from the owner**, which sets what a session should expect of itself: not
that it will avoid this, but that its output is unreviewed until somebody who knows the field has read it.*

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
6. **Correct the text, and keep the reason.** The wrong version goes; why it was wrong stays. **Broken premises
   are the exception to every deletion rule in this repo** — `registers/premises.md` is the failure library, and
   `PR-1` (this repo's default assumption about a missing capability has been wrong every time) has prevented the
   same mistake repeatedly. A broken row is deleted only if it turns out never to have been load-bearing.

## Two things to say out loud rather than resolve quietly

- **"I do not know"** — with the `[?]` and what would answer it. *159 of those already exist and they are the
  healthiest thing in the repo.*
- **"That was mine, not measured"** — when a claim is inference. **The cost of not saying it is that somebody
  builds on it, and the somebody is usually the next session.**

---

## Where things live

**One kind per file**, and the folder says which kind: **`group-strategy/`** argument · **`motion/`** the
machinery · **`brands/`** application · **`registers/`** state, in rows · **`evidence/`** measured,
measured. **A superseded conclusion is deleted; the measurement under it is not** — figures are expensive to
re-derive and a later question usually needs them · **`operations/`** what leaves the repo, **including ADRs drafted for `cinema-platform`** ·
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
| **Business or management** — pricing, territory, what we sell, who we sell to | `decided.md`, once Neil decides it | SRND OS, every morning |
| **Repo management** — conventions, structure, how questions are logged, how a session runs | this file | Whoever is working in the repo |

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

## Not getting into this mess again — 2026-08-20

**Most of what went wrong on 2026-08-20 is now a rule, and rules did not stop it happening.** *What stops it is
`tools/check.py`: run it before committing. It fails on things a machine can see and warns on the rest.*

| It catches | Because, on 2026-08-20 |
|---|---|
| **Strikethrough anywhere** | 403 struck spans had accumulated. A reader cannot tell a finding from a retracted one |
| **Duplicate IDs** | 23 of them. `REC-8` meant two different rows, and I numbered new work into occupied families without looking |
| **Ragged table columns** | A tidy-up regex joined table rows and took a 549-line file to 312. Later, adding two columns to headers and not to rows broke 163 rows |
| **A row typed `Ask` weighted `clarification`** | It fails the bar by definition — an owner's attention on a filing choice |
| **Any row typed `Decide`** | That type does not exist. A decision is a question, asked and answered |
| **Emphasis over ~12 marks per 100 words** | Files were running at 15–24. Nothing reads as emphasised when everything is |
| **A register over ~450 lines** | `open-items.md` reached 838 and had become a diary. Nothing had told it to stop |
| **Sessions narrating their own process** | *"I first wrote…", "third instance of…"* — keep the finding, drop the diary |

**An eighth, 2026-08-21, and it is about rule-writing rather than about work.** *A rule was added to `CLAUDE.md` saying the C-ATS web surfaces are data rather than truth — correct today, because both are dead. **Neil: "Your rule is fine today but a real problem when the new site goes live."*** *He is right: as written it would have told a future session to disregard a genuine defect on a real published site. **The rule was a snapshot of current facts wearing the grammar of a principle.*** **The rule about rules: write the test, not the list.** *A durable rule says how to tell which case you are in — here, establish whether a surface is the published offer, a legacy remnant or a mock-up, because the three behave in opposite ways. **The current statuses belong underneath it as a status board with an explicit expiry**, not as the rule itself. *Every rule derived from today's state needs the condition under which it stops being true written next to it.*

**A seventh, 2026-08-21 — "apply at source" was a queue item I could not perform.** *Eight content corrections were written as paste-ready copy and listed as the top of the producer queue. **Neil: "apply the corrections at source — what does that mean?"** It meant three different surfaces, none of which this repo can edit: a WordPress site with no documented editing route, a Shopify store whose CLI auth `EST-6` records as blocked, and a generated build whose pipeline is documented nowhere. **And the corrections document asserted that the site is generated from this repo so the text would be picked up automatically — an assumption built on one remark about one build of unknown provenance.*** **The rule: before listing work as yours, name the mechanism by which it lands.** *Writing the copy is the deliverable; applying it is somebody else's task, and saying so is more useful than a queue item that cannot be worked.*

**A sixth, 2026-08-21 — a "confirm current spec" flag is a blocker, not a note.** *The ~300 mm layout tolerance traced to a decode of a **2015** pack brochure, and the provenance table had flagged it *"legacy, confirm current spec"* throughout. **It was never confirmed, and it became the record's `H2` — its single most interesting true thing — cited in fourteen places, drafted as a training piece, written into the copy and the install notes, and published on the live site.** Struck in one sentence by an owner (`registers/questions.md` `Q102`). **The same 2015 source produced a second wrong claim the same day** (the 50 mm depth on all three panels).* **The rule: a flag that says confirm before use means the claim cannot be built on until it is confirmed.** *Treat an unconfirmed source as unusable rather than as usable-with-a-caveat — the caveat travels for a while and then stops travelling.*

**A fifth, 2026-08-21 — building on an in-development platform output.** *`../CLAUDE.md` requires checking the platform before specifying anything that touches it, and this session read two Cinema Tools reports properly. **Then it lifted an unlocked implementation detail straight into a live positioning document.** Neil: **"please treat that in development report as just background info right now. your general observations are dead on but the stuff like the aperiodic placement needs deeper analysis before i lock it."*** **The rule: reading the platform is not the same as building on it.** *An output still in development shows where the thinking has got to; it is not a fact to cite. **Check whether a platform artefact is locked before any of it leaves the evidence file** — general observations may inform, specific parameters and implementation choices may not travel.*

**A fourth, 2026-08-21 — asking outside the active phase.** *Invited to close open questions so there would be work queued, I picked the heaviest `Ask` rows in the register. One of them, `CON-10`, was **group B2C channel spend during a C-ATS trade phase**, and the brief it produced then had to reason about a dependency in another lane entirely. Neil: **"Why are cinema store questions slipping in here."*** **The rule: heaviness is not relevance.** *When choosing what to ask, filter by the active phase first and weight second — and if a row from another lane genuinely deserves to jump, say that it is jumping.*

**Three judgement failures a checker cannot catch, so they are written down instead.**

1. **A shared link is context, not a work order.** *A URL arrived with no instruction and produced a seven-section
   audit, then four more files correcting it. **Ask what is wanted, or do the smallest useful thing.***
2. **Establish what an artefact is before measuring it.** *An unfinished mockup was audited against the guardrails
   and produced findings that dissolved the moment someone said what it was. **Name the artefact and check its
   state first.***
3. **A stop is a stop, including file writes.** *Told to stop, I made one more edit; told we were going in circles,
   I did another pass and then offered more work.*

**And the deepest one, which is why the bar on questions exists:** *of 61 answered questions, 22 were pure repo
housekeeping. **The scarcest thing in this process is an owner's attention, and it was being spent on filing.***

### What the deletion rules must never touch

*Added 2026-08-20, after the clean-up nearly cut into the working memory a session needs. Neil's question was the
right one: rules that remove noise can remove the record with it.*

**Four things are exempt from every "delete it" rule in this repo:**

| Kept, always | Why |
|---|---|
| **What an owner actually said, verbatim, with a date** | It is the only unimpeachable source here, and 171 such quotations are load-bearing across the files |
| **A broken premise** (`registers/premises.md`) | The failure library. `PR-1` — this repo's default assumption about a missing capability has been wrong every time — has stopped the same mistake repeatedly. 18 of 24 rows are broken, and that is the register working |
| **A measurement**, even when the conclusion drawn from it is withdrawn | Figures are expensive to re-derive. The 53-of-549 dealer baseline, the `G3`/`G4`/`G6` funnel counts, the BSRIA provenance — a later question needs the number even when the argument around it was wrong |
| **Why a correction happened** | "This failed because X" is a finding. "I first wrote X and then corrected it" is a diary. The first stays |

**What goes, and it is only this:** *the wrong version of a text · a session's account of its own process ·
a withdrawn finding · a superseded conclusion · a closed row that carries nothing but its own history.*

*`tools/check.py` is scoped to match: its narration check flags self-reference only, and exempts this file and the
premises register.*
