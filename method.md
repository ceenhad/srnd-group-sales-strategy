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

## The shape of a working session

1. **Read what governs it, end to end.** Check `decisions/CATALOGUE.md` and the owning area document first.
2. **Work in the register.** Questions get IDs before they get asked.
3. **Ask, apply, ask.** No essay between the answer and the next question.
4. **Record the answer verbatim, and what it changed.** If it changed nothing, say so.
5. **Correct in place and visibly.** A struck line with its reason is worth more than a clean one that hides a
   reversal.

## Two things to say out loud rather than resolve quietly

- **"I do not know"** — with the `[?]` and what would answer it. *159 of those already exist and they are the
  healthiest thing in the repo.*
- **"That was mine, not measured"** — when a claim is inference. **The cost of not saying it is that somebody
  builds on it, and the somebody is usually the next session.**

---

## Where things live

**One kind per file**, and the folder says which kind: **`group-strategy/`** argument · **`motion/`** the
machinery · **`brands/`** application · **`registers/`** state, in rows · **`evidence/`** measured,
append-only · **`operations/`** what leaves the repo · **`decisions/`** ADRs · **`data/`** the source.

**SRND OS is the source of record for what is decided.** `decided.md` is empty and nothing enters it without
Neil. An ADR belongs to one area and is written when a decision is made in it — **never scraped out of a pile
afterwards** (`decisions/0001` §6).
