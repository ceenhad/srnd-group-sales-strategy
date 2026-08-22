# Decision records: the method, and the lessons that produced it

*A portable working method for a repository whose decision records have got out of control. **Written from
experience, not theory** — every rule below exists because the failure it prevents actually happened, twice in
some cases. Self-contained: nothing here depends on the repo it came from.*

**Two audiences.** *Someone cleaning up an existing set, and anyone writing a new record afterwards. **Start with
the diagnostics** — they tell you the size of the problem before you decide how to fix it.*

---

## Part 1 — The eight rules

### 1. A number is permanent; content is versioned

**A decision that changes is rewritten in place under the same number, at a new version.** *No amendment notes, no
"see also" chains, no `ADR-014b`.* **`ADR 017 version 2` still resolves; `ADR 017 (amended)` would not.**

**Why it matters more than it looks:** *a reader who finds the number finds the current decision. The moment you
allow amendment chains, "what is decided" becomes a research task and everyone stops doing it.*

### 2. The status field is the check — not the document, and not the date

**Before citing any decision, read its `status` and `superseded_by`.** *A superseded record is **not a weaker
source. It is the wrong one.***

**This is the rule that gets broken most, and it breaks in a way that feels rigorous.** *In our case a correction
was written that cited a record superseded three weeks earlier, and rested half its argument on a product
document framed on a record superseded two months earlier — which described a product surface a later decision had
**withdrawn outright**. Three separate documents then asserted a feature that had been cancelled, not deferred.
**Every author had checked something. None had checked the status field.***

### 3. Frontmatter must make one grep sufficient

Every record carries, machine-readably: **`id` · `status` · `version` · `revised` · `supersedes` ·
`superseded_by`**. *If answering "is this current?" requires opening the file and reading prose, the check will not
happen at scale.*

### 4. A decision is written when it is made, by the person making it

**Never scraped out of a pile afterwards.** *We generated 59 records from a template in a single script run —
frontmatter, a boilerplate line, one bolded sentence each. All 59 were deleted. **The source documents already held
the reasoning; the extraction kept the slogan and threw the reasoning away.***

> **The test: if it could have been produced by a loop, it is not a record of a decision.**

### 5. The index is generated, never hand-maintained

*A hand-written index drifted to covering **41 of 70** records in three months, with **nine rows disagreeing with
their own files**. **A stale index is worse than no index**, because it is consulted.*

### 6. One set of decision records, in the repository that owns the decision

**Do not grow a second set alongside someone else's.** *We tried twice — the first attempt scraped 59 stubs and was
deleted entire; the second wrote three good records and was removed the same day for being a third copy of what the
repo already held.* **If a decision binds another repository, it is not your record to write.**

### 7. What leaves is a decision *request*, not a decision record

*A file with a placeholder number and borrowed frontmatter is neither a record nor a proposal — it is a decision
record in costume, and it will be mistaken for one.* **A request carries an ID in the requesting repo's own
namespace**, states the contradiction, the proposed decision and the consequences **as tables**, and **never
guesses the destination's number** or whether it supersedes anything. **If accepted, the owner creates the record
in their repo.** *That is the moment it becomes a decision, and not before.*

### 8. Product documents outlive their decisions — plan for it

**`docs/` drifts; the decision set is the record.** *We found two product documents in one day still describing
things their governing records had withdrawn, and both read as perfectly current. **Neither was wrong when
written.*** *Any document that leans on a decision should name the record it leans on, so the pair can be checked
mechanically.*

---

## Part 2 — Diagnostics for a set already out of control

*Run these before deciding anything. **Numbers first**: a set with three broken links needs a different response
from one with thirty.* *(Commands assume records in `docs/decisions/` with YAML frontmatter. Adjust the paths.)*

**1. Records with no status at all** — *the ones nobody can check:*
```sh
for f in docs/decisions/*.md; do grep -q '^status:' "$f" || echo "NO STATUS: $f"; done
```

**2. Non-reciprocal supersession** — *`A` says it supersedes `B`, but `B` does not point back. **The commonest
corruption, and it silently resurrects dead decisions:***
```sh
grep -H '^\(id\|supersedes\|superseded_by\):' docs/decisions/*.md
# then check every pair both ways — a one-directional link is a bug, not a shorthand
```

**3. Documents citing a superseded record** — *the highest-value check in the list:*
```sh
# list superseded ids first
grep -l '^status: superseded' docs/decisions/*.md
# then find every document that cites one
grep -rn 'ADR[- ]0*<id>' --include=*.md . | grep -v '^docs/decisions/'
```

**4. The index against reality:**
```sh
# count records vs index rows, then diff the id lists — do not eyeball it
ls docs/decisions/*.md | wc -l
grep -c '^|' docs/decisions/README.md
```

**5. Scraped records** — *find the ones a loop produced:*
```sh
# near-identical length and structure is the tell
wc -l docs/decisions/*.md | sort -n | head -40
```
*A cluster of records within a line or two of each other, all created the same day, is an extraction rather than a
decision history.*

**6. Reused or missing numbers:**
```sh
grep -h '^id:' docs/decisions/*.md | sort -n | uniq -d   # reused
```

**7. The same decision in two places** — *no command for this one. It needs reading, and it is why the count
matters: you cannot read 300 records, so fix the mechanical faults first and let the set shrink.*

---

## Part 3 — Lessons that apply to the cleanup itself

*These are not about decision records. They are about how a cleanup goes wrong, and each one cost us something.*

**Grep is not reading.** *Four settled positions were re-argued in a day by someone who had every document
available and had read none end to end. **A grep returns the sentence that matched, never the argument around
it.** If a document governs the work, read it; if there is no time, say so rather than cite it.*

**Flagging is not doing.** *A banner reading "this cites a superseded record" was written, and the citation left in
place. **A flag with an obvious fix is a fix not yet made** — and roughly 350 inline markers are what that habit
looks like after a year.*

**Propagation by citation.** *When you strike a claim, **grep for the documents that cite it, not only for its
words.** Two of our four worst instances spread through an explicit cross-reference — "as with X", "parked, as
with Y" — and **a paraphrase pointing at a deleted original survives the deletion**, because the citation reads as
provenance rather than as a copy. It is the hardest instance to find and the likeliest to be believed.*

**A summary is not a source.** *Search results, index pages and generated summaries tell you a document exists.
**They are not quotable.** We built a finding on a summary that had dropped three words, and those three words
carried the whole meaning. **The loss is asymmetric**: summaries drop qualifiers far more often than they add
them, so what goes missing is exactly the part that made the claim narrow and true.*

**A replacement claim carries its own burden.** *Striking something for lack of evidence and writing its
replacement **in the same edit** is the likeliest moment in any cleanup to introduce a fresh unsourced claim —
because the strike feels like rigour and lends its credibility to whatever follows.*

**Old is unestablished, not wrong.** *A superseded record, a legacy document, a five-year-old spec: these are
**unestablished, not false**. Marking them "discount this" is as damaging as treating them as binding, and it is
how genuinely useful material gets thrown away during a tidy-up. **Say which it is.***

**Before recording anything as missing, say where you looked.** *Not "checked the repo" — **which directory, and
what did the frontmatter say.** Every time we recorded a capability as absent and someone checked, it was present
in some state.*

**And the self-check that catches most of it:** *is the sentence more confident than the last piece of evidence
behind it?* **Every one of our worst errors cited something real and then went one step further than the source
reached.** *Nothing mechanical catches that, because the citation is genuine and only the distance is wrong.*

---

## Part 4 — The order to do it in

1. **Run the diagnostics. Write down the numbers.** *Decide scale before method.*
2. **Fix the mechanical faults first** — missing statuses, non-reciprocal supersession, the generated index.
   *These need no judgement and they shrink the set you have to read.*
3. **Find every document citing a superseded record.** *Fix the citation, do not flag it.*
4. **Delete the scraped records.** *They contain no reasoning to lose. Check the source documents still exist
   first.*
5. **Only then read what is left.** *Duplicated decisions and genuine contradictions need judgement, and by now
   there will be far fewer of them.*
6. **Write down the rule you broke as you fix each class.** *A cleanup that does not change how records are written
   will be needed again within the year.*

> **The one-line version:** *the number is permanent, the status field is the check, the index is generated, and a
> decision is written by the person making it — everything else in this document is a consequence of one of those
> four.*
