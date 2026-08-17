# The QA session — the run sheet

**Three questions, asked one at a time over the same 46 tasks. Then a fourth pass for what is missing.**

> ## ▶ CLOSED — the session is complete, 2026-08-08
>
> **All four passes and the reading are done.** This sheet is the historical record of the run; nothing in it
> is live. The outcome lives in `NEXT.md` § "What the QA produced"; the shapes it directed are in
> `task-shapes.md`; the decisions it surfaced are in `standards.md`. *(Banner updated
> 2026-08-14 — it previously read "RESUME HERE", which made a finished run look in-progress.)*
>
> | | State |
> |---|---|
> | **Pass 1 sweep A** — is it the same every time? | **Done.** All 46. `from scratch` 21 · `varies` 19 · `standard` 6 |
> | **Pass 1 sweep B** — the reasons | **Done.** Two tags survived of six proposed: `no template`, `no standard` |
> | **Pass 2 sweep A** — what starts it? | **Done.** All 46. `remembered` 29 · `asked` 10 · `a system` 7 |
> | **Pass 2 sweep B** — what would have to fire it? | **Done.** 29 rows. **An owner is needed for all 29** (Neil, on review); the split is *automatable event exists* (11) vs *not* (18); 3 of the 18 also need a destination |
> | **Pass 3 sweep A** — where does the output land? | **Done.** All 46. `a file` 17 · `a system` 14 · `a head` 10 · `nowhere` 5 |
> | **Pass 3 sweep B** — what is lost? | **Done.** 15 rows (`a head`/`nowhere`) — this is the `record` build list; 3 are duplication rows |
> | **Pass 4** — what is missing? | **Done.** Two additions, both reactive triggers — inbound mail, a colleague's question; no tasks struck |
>
> **How to run it.** Ask with question boxes (`AskUserQuestion`), **four tasks per box**, one word each from the
> pass's fixed list. That format is working — any unanswered box in the history was a timeout while the answerer
> was elsewhere, not a problem with the method. Do not switch to prose and do not re-ask what is already
> answered above.
>
> **Two things deliberately parked, not forgotten:**
>
> 1. **The pass 1 tag spread.** Whether `no template` and `no standard` split across the 40 rows or apply to
>    nearly all of them. Deferred to after pass 3, which may settle it without asking.
> 2. **No cross-pass interpretation yet**, by this sheet's own rule. Reading waits for all four passes. The
>    pattern flagged at eight rows now has all 46 behind it and it mostly held: of the 7 rows that fire on their
>    own (`a system`), five are downstream of a dealer already in contact — qualify the dealer, technical selling,
>    produce a quote, negotiate terms, onboard the account. The two exceptions are both marketing housekeeping,
>    not sales motion — events/exhibitions and CRM/data hygiene — things a calendar or a database fires
>    regardless of any dealer. So the sales machine still only starts once somebody else has; the only
>    self-starting parts of the whole register are the two that run on a clock. Watch, don't act.
> 3. **A texture behind the `remembered` answers, from Neil (2026-08-06).** These tasks aren't unknown —
>    everyone's aware of them — but none is a specific person's job and nothing routes them. Example: research the
>    masking-screen market and you now *know* it, but nothing feeds that back; for all you know someone else
>    researched the same thing — the least efficient case, effort spent, re-spent, retained nowhere. Two things to
>    carry forward, not act on: **(a)** for the research-type rows (`T-M01`, `T-S23`, `T-S24`) the
>    `remembered` → `a system` fix reads less like a trigger and more like *an owner and a destination* — pass 2
>    sweep B should frame those that way rather than hunting for a firing event. **(a) — confirmed and broader
>    than expected (sweep B, 2026-08-06):** not 3 rows but 18 of the 29 `remembered` rows had no firing event and
>    were answered *needs an owner*; the trigger question misframed most of them. The owner gap, not the trigger
>    gap, is the through-line of pass 2. **(b)** *Duplication / re-work* is
>    a cost this sheet can't yet name: pass 3 asks "what is lost", but the sharper loss here is the same work done
>    twice by people blind to each other — worse than lost, negative. And it is not hypothetical. Given the work
>    provably happens and (a) says nothing owns or routes it, *some* duplication is arithmetically forced — the
>    only duplication-free world is one with a single owner or one shared destination, and pass 2 says we have
>    neither. What's forced is its **existence**, not its **size**: this sheet can name the mechanism, it can't
>    measure how often or how dear (that needs watching real work). It strengthens the reading table's
>    `… · nowhere → record first` — it does not reopen it. Watch for it in pass 3 sweep B and pass 4.

## The two rules that make it work

**1. One question at a time — go down a column, never across a row.** A row asks three different questions at
once, so answering row-wise means switching between them 46 times and the standard drifts. The instrument
measuring consistency ends up inconsistent itself. Hold one question, answer it 46 times, then pick up the next.

**2. Answer first, detail second.** Each pass is two sweeps. **Sweep A** is the answer alone, all 46, fast, one
word each. **Sweep B** goes back for detail — and only over the rows whose answer earned it. Asking for the
answer and the reason together is two questions again, and it is what turns an hour into an afternoon.

## How to answer sweep A

- **Record what happens now, never what should happen.** This is a baseline. A task that is *meant* to be
  standard but which everyone does their own way is **`varies`** — the intention is not the answer. Answered
  aspirationally the sheet measures nothing and the build list it produces aims at problems that do not exist.
  **Intent has exactly one home: pass 2's sweep B**, which asks what would have to happen for something to fire
  on its own.
- **One word from the list. Never a sentence.** Fixed words are comparable; prose is where the consistency goes.
  The sentences belong in sweep B.
- **First instinct.** If a row takes more than a few seconds, mark it `?` and move on. A row that needs
  discussion is telling you the task as written isn't one real thing — that is an answer, not a delay.
- **No discussion during a sweep.** Mark disagreement, resolve it after.
- **If more than one person answers: answer independently, compare afterwards.** Two people giving different
  answers for the same task is not a problem to iron out — **it is the finding.** The task varies by who does
  it, which is pass 1's answer arriving from a different direction.

---

# Pass 1 — Is it the same every time?

**`standard`** same way each time · **`varies`** depends who does it · **`from scratch`** rebuilt each time

*Only this: when it gets done, does it follow a shape, or is it made up on the spot?*

### Sweep A — the answer, all 46 — **done 2026-08-04 (Neil)**

| ID | Task | |
|---|---|---|
| `T-S01` | Build the target list | **`from scratch`** |
| `T-S02` | Reach a dealer who has never heard of us | **`from scratch`** |
| `T-S03` | Qualify the dealer | **`varies`** |
| `T-S04` | Qualify the project | **`varies`** |
| `T-S05` | Present the range | **`varies`** |
| `T-S06` | Discover | **`from scratch`** |
| `T-S07` | Technical selling | **`varies`** |
| `T-S08` | Produce a quote | **`standard`** |
| `T-S09` | Follow up through the project's lead time | **`varies`** |
| `T-S10` | Handle objections | **`from scratch`** |
| `T-S11` | Defend against a named competitor | **`from scratch`** |
| `T-S12` | Negotiate terms | **`standard`** |
| `T-S13` | Close | **`varies`** |
| `T-S14` | Onboard the account | **`from scratch`** |
| `T-S15` | Make the first install succeed | **`from scratch`** |
| `T-S16` | Post-delivery follow-up | **`from scratch`** |
| `T-S17` | Account management | **`from scratch`** |
| `T-S18` | Cross-sell the rest of the group | **`from scratch`** |
| `T-S19` | Prompt the reorder | **`from scratch`** |
| `T-S20` | Recover a failure | **`from scratch`** |
| `T-S21` | Train the dealer's staff | **`from scratch`** |
| `T-S22` | Pipeline and forecast | **`standard`** |
| `T-S23` | Bring back market intelligence | **`varies`** |
| `T-S24` | Feed product development | **`varies`** |
| `T-S25` | Events and keeping relationships warm | **`varies`** |
| `T-S26` | Territory planning | **`from scratch`** |
| `T-S27` | The novel problem | **`varies`** |
| `T-S28` | Recognition and thanks | **`varies`** |
| `T-M01` | Market and segment research | **`from scratch`** |
| `T-M02` | Competitor tracking | **`varies`** |
| `T-M03` | Positioning and messaging | **`varies`** |
| `T-M04` | Campaign planning | **`from scratch`** |
| `T-M05` | Content production | **`from scratch`** |
| `T-M06` | Editorial calendar and cadence | **`varies`** |
| `T-M07` | Channel management | **`varies`** |
| `T-M08` | Discoverability | **`from scratch`** |
| `T-M09` | Lead capture and nurture | **`varies`** |
| `T-M10` | Collateral | **`varies`** |
| `T-M11` | Brand consistency | **`standard`** |
| `T-M12` | Dealer marketing support | **`from scratch`** |
| `T-M13` | Events and exhibitions | **`standard`** |
| `T-M14` | Trade press and PR | **`varies`** |
| `T-M15` | Measurement and reporting | **`varies`** |
| `T-M16` | CRM and data hygiene | **`standard`** |
| `T-M17` | Product launch | **`from scratch`** |
| `T-M18` | Budget and spend allocation | **`from scratch`** |

### Sweep B — the reasons, named cold — **done 2026-08-04 (Neil)**

**Which rows:** the 40 answered `varies` or `from scratch`.

**Method:** the reasons were named before any row was looked at, so the vocabulary is the answerer's and not
the sheet's. Six were proposed for correction; **two survived.**

| Tag | Means | The fix it implies |
|---|---|---|
| **`no template`** | Nothing to copy from. No template, and last time's version wasn't kept, so you start from a blank page having already done it before | Make the template — or keep the last one |
| **`no standard`** | Nobody decided what good looks like, so there is nothing to be consistent with | Decide what done means, once |

**What was struck, and it matters more than what survived:**

- ~~Depends who picks it up~~ — **not a people problem.** Inconsistency is not coming from who does the work.
- ~~The facts aren't in one place~~ — **not a data-assembly problem**, at least not at this altitude.
- ~~Too infrequent to have a habit~~ — **not a frequency problem.**
- ~~**Genuinely different each time**~~ — **struck, and this is the finding.** The escape hatch was offered and
  refused: **none of the 40 is legitimate variation.** There is no row here where doing it the same way would be
  wrong. All of it is fixable.

**So the whole of pass 1 reduces to two missing artefacts per task — a template and a definition of done.**
Both are written, not built. That is a materially cheaper conclusion than the primitives build, and it lands
before any of it.

| ID | Answer | Tag |
|---|---|---|

*To fill: the 40 rows tagged `no template`, `no standard`, or both.*

---

# Pass 2 — What starts it?

**`a system`** something fires it · **`remembered`** someone thinks of it · **`asked`** only when a customer prompts

*Only this: what causes it to happen at all? Not who does it, and not how well.*

### Sweep A — the answer, all 46 — **done 2026-08-06 (Neil)**

**Spread:** `remembered` 29 · `asked` 10 · `a system` 7.

| ID | Task | |
|---|---|---|
| `T-S01` | Build the target list | **`remembered`** |
| `T-S02` | Reach a dealer who has never heard of us | **`remembered`** |
| `T-S03` | Qualify the dealer | **`a system`** |
| `T-S04` | Qualify the project | **`remembered`** |
| `T-S05` | Present the range | **`remembered`** |
| `T-S06` | Discover | **`asked`** |
| `T-S07` | Technical selling | **`a system`** |
| `T-S08` | Produce a quote | **`a system`** |
| `T-S09` | Follow up through the project's lead time | **`remembered`** |
| `T-S10` | Handle objections | **`asked`** |
| `T-S11` | Defend against a named competitor | **`asked`** |
| `T-S12` | Negotiate terms | **`a system`** |
| `T-S13` | Close | **`remembered`** |
| `T-S14` | Onboard the account | **`a system`** |
| `T-S15` | Make the first install succeed | **`asked`** |
| `T-S16` | Post-delivery follow-up | **`asked`** |
| `T-S17` | Account management | **`remembered`** |
| `T-S18` | Cross-sell the rest of the group | **`remembered`** |
| `T-S19` | Prompt the reorder | **`asked`** |
| `T-S20` | Recover a failure | **`asked`** |
| `T-S21` | Train the dealer's staff | **`asked`** |
| `T-S22` | Pipeline and forecast | **`remembered`** |
| `T-S23` | Bring back market intelligence | **`remembered`** |
| `T-S24` | Feed product development | **`asked`** |
| `T-S25` | Events and keeping relationships warm | **`remembered`** |
| `T-S26` | Territory planning | **`remembered`** |
| `T-S27` | The novel problem | **`asked`** |
| `T-S28` | Recognition and thanks | **`remembered`** |
| `T-M01` | Market and segment research | **`remembered`** |
| `T-M02` | Competitor tracking | **`remembered`** |
| `T-M03` | Positioning and messaging | **`remembered`** |
| `T-M04` | Campaign planning | **`remembered`** |
| `T-M05` | Content production | **`remembered`** |
| `T-M06` | Editorial calendar and cadence | **`remembered`** |
| `T-M07` | Channel management | **`remembered`** |
| `T-M08` | Discoverability | **`remembered`** |
| `T-M09` | Lead capture and nurture | **`remembered`** |
| `T-M10` | Collateral | **`remembered`** |
| `T-M11` | Brand consistency | **`remembered`** |
| `T-M12` | Dealer marketing support | **`remembered`** |
| `T-M13` | Events and exhibitions | **`a system`** |
| `T-M14` | Trade press and PR | **`remembered`** |
| `T-M15` | Measurement and reporting | **`remembered`** |
| `T-M16` | CRM and data hygiene | **`a system`** |
| `T-M17` | Product launch | **`remembered`** |
| `T-M18` | Budget and spend allocation | **`remembered`** |

### Sweep B — back over the answers, for detail — **done 2026-08-06 (Neil)**

**Which rows:** Every row answered **`remembered`** (29).

**What to add:** **What would have to happen for it to fire on its own?** Name the trigger, not the build — *"when a quote passes 30 days"*, not *"a reminder system"*.

**Method note:** candidate triggers were drafted per row and confirmed or overwritten one at a time. A recurring option was offered — *"no natural event, needs an owner"* — because for many rows the honest answer to "what fires it" is "nothing does."

**Spread:** of 29, **18 have no firing event** — the answer was *needs an owner on a cadence*, not a trigger; **11 have a genuine event**. Of the 18, **3 also need a shared destination** (`T-S23`, `T-M01`, `T-M02`) — the duplication rows from parked note 3(b). Recorded as a spread only; the reading waits for all four passes.

**On review (Neil, 2026-08-06):** *needs an owner* is arguably true for **all 29** — the 11 "event" rows have a trigger available, but nothing acts on it without someone owning it; the event fires into the void otherwise. So the split is not *owner vs. not* (an owner is universal across the `remembered` class) — it is *whether an automatable event exists (11) or not (18)*. The owner gap is the whole class; the event, where present, is only what could later let **a system** stand in for the owner. The 11 can graduate toward `a system`; the 18 can only ever be an owned cadence. Answers left as recorded — this sharpens the reading, it does not rewrite the rows. The Pass 2 primitive it points at is **assign owners**, not add triggers.

| ID | Sweep A | The trigger — or why there isn't one |
|---|---|---|
| `T-S01` | `remembered` | **No event — needs an owner** on a cadence |
| `T-S02` | `remembered` | **No event — needs an owner** (standing outreach) |
| `T-S04` | `remembered` | When discovery starts on an opportunity |
| `T-S05` | `remembered` | When a dealer engages a brand they haven't bought |
| `T-S09` | `remembered` | **No event — needs an owner** working live projects on a cadence |
| `T-S13` | `remembered` | As the decision / install date approaches |
| `T-S17` | `remembered` | **No event — needs an owner** holding accounts on a cadence |
| `T-S18` | `remembered` | **No event — needs an owner** watching each account's brand coverage |
| `T-S22` | `remembered` | When opportunities move stage or value |
| `T-S23` | `remembered` | **No event — needs an owner + a shared destination** (duplication row) |
| `T-S25` | `remembered` | **No event — needs an owner** keeping relationships warm on a cadence |
| `T-S26` | `remembered` | When a territory's shape, coverage or ownership changes |
| `T-S28` | `remembered` | **No event — needs an owner** deciding who to thank on a cadence |
| `T-M01` | `remembered` | **No event — needs an owner + a shared destination** (duplication row) |
| `T-M02` | `remembered` | **No event — needs an owner + a shared destination** (duplication row) |
| `T-M03` | `remembered` | **No event — needs an owner** on a cadence |
| `T-M04` | `remembered` | **No event — needs an owner** planning on a cadence |
| `T-M05` | `remembered` | When a campaign is approved |
| `T-M06` | `remembered` | At the start of each planning cycle |
| `T-M07` | `remembered` | When a channel's performance drops below its norm |
| `T-M08` | `remembered` | **No event — needs an owner** on a cadence |
| `T-M09` | `remembered` | When a lead is captured (form fill, event scan) |
| `T-M10` | `remembered` | **No event — needs an owner** maintaining the set |
| `T-M11` | `remembered` | **No event — needs an owner** holding the standard |
| `T-M12` | `remembered` | **No event — needs an owner** supporting dealers on a cadence |
| `T-M14` | `remembered` | **No event — needs an owner** working press on a cadence |
| `T-M15` | `remembered` | **No event — needs an owner** producing reports on a cadence |
| `T-M17` | `remembered` | When a product reaches launch-ready |
| `T-M18` | `remembered` | When spend hits a threshold and needs reallocation |

---

# Pass 3 — Where does the output land?

**`a system`** engine, the store, the record · **`a file`** somewhere findable · **`a head`** one person's memory or inbox · **`nowhere`**

*Only this: when it is done, what is left behind that makes the next one cheaper?*

### Sweep A — the answer, all 46 — **done 2026-08-06 (Neil)**

**Spread:** `a file` 17 · `a system` 14 · `a head` 10 · `nowhere` 5. The `a head` + `nowhere` rows (15) go to sweep B.

| ID | Task | |
|---|---|---|
| `T-S01` | Build the target list | **`a system`** |
| `T-S02` | Reach a dealer who has never heard of us | **`a system`** |
| `T-S03` | Qualify the dealer | **`a system`** |
| `T-S04` | Qualify the project | **`a system`** |
| `T-S05` | Present the range | **`a system`** |
| `T-S06` | Discover | **`a system`** |
| `T-S07` | Technical selling | **`a file`** |
| `T-S08` | Produce a quote | **`a system`** |
| `T-S09` | Follow up through the project's lead time | **`a file`** |
| `T-S10` | Handle objections | **`a head`** |
| `T-S11` | Defend against a named competitor | **`a head`** |
| `T-S12` | Negotiate terms | **`a system`** |
| `T-S13` | Close | **`a system`** |
| `T-S14` | Onboard the account | **`a head`** |
| `T-S15` | Make the first install succeed | **`nowhere`** |
| `T-S16` | Post-delivery follow-up | **`nowhere`** |
| `T-S17` | Account management | **`a system`** |
| `T-S18` | Cross-sell the rest of the group | **`a head`** |
| `T-S19` | Prompt the reorder | **`nowhere`** |
| `T-S20` | Recover a failure | **`a head`** |
| `T-S21` | Train the dealer's staff | **`a file`** |
| `T-S22` | Pipeline and forecast | **`a system`** |
| `T-S23` | Bring back market intelligence | **`nowhere`** |
| `T-S24` | Feed product development | **`a head`** |
| `T-S25` | Events and keeping relationships warm | **`a file`** |
| `T-S26` | Territory planning | **`a file`** |
| `T-S27` | The novel problem | **`a file`** |
| `T-S28` | Recognition and thanks | **`a head`** |
| `T-M01` | Market and segment research | **`a head`** |
| `T-M02` | Competitor tracking | **`a head`** |
| `T-M03` | Positioning and messaging | **`a file`** |
| `T-M04` | Campaign planning | **`a file`** |
| `T-M05` | Content production | **`a file`** |
| `T-M06` | Editorial calendar and cadence | **`a file`** |
| `T-M07` | Channel management | **`a system`** |
| `T-M08` | Discoverability | **`nowhere`** |
| `T-M09` | Lead capture and nurture | **`a system`** |
| `T-M10` | Collateral | **`a file`** |
| `T-M11` | Brand consistency | **`a file`** |
| `T-M12` | Dealer marketing support | **`a file`** |
| `T-M13` | Events and exhibitions | **`a file`** |
| `T-M14` | Trade press and PR | **`a file`** |
| `T-M15` | Measurement and reporting | **`a file`** |
| `T-M16` | CRM and data hygiene | **`a system`** |
| `T-M17` | Product launch | **`a file`** |
| `T-M18` | Budget and spend allocation | **`a head`** |

### Sweep B — back over the answers, for detail — **done 2026-08-06 (Neil)**

**Which rows:** Every row answered **`a head`** or **`nowhere`** (15).

**What to add:** **What exactly is lost?** The thing itself, in a few words — *"which competitor they were comparing against"*, *"the answer we gave"*. This sweep writes the `record` build list directly.

**This table is the `record` build list.** 15 items — the specific thing each task should leave behind and currently doesn't. The three marked **(duplication)** are the rows from parked note 3(b) whose loss is not just "gone" but "redone".

| ID | Sweep A | What is lost — the thing to capture |
|---|---|---|
| `T-S10` | `a head` | Which objections recur across dealers, and the answer that worked |
| `T-S11` | `a head` | Where we win and lose against each named competitor |
| `T-S14` | `a head` | What was agreed, set up and promised at onboarding |
| `T-S15` | `nowhere` | What went right and wrong on the first install |
| `T-S16` | `nowhere` | The relationship state after delivery |
| `T-S18` | `a head` | Cross-sell attempts and how the account responded |
| `T-S19` | `nowhere` | Each account's reorder cadence |
| `T-S20` | `a head` | What failed, the root cause, and the fix |
| `T-S23` | `nowhere` | What the field learned about the market — **(duplication)** |
| `T-S24` | `a head` | The feature and gap requests coming back from the field |
| `T-S28` | `a head` | Which accounts are owed recognition |
| `T-M01` | `a head` | Who researched what — **(duplication)** |
| `T-M02` | `a head` | The competitor picture over time — **(duplication)** |
| `T-M08` | `nowhere` | What was tried for discoverability, and what worked |
| `T-M18` | `a head` | The spend decisions and their rationale |

---

# Pass 4 — What is missing?

**Its own pass, deliberately.** Asked during passes 1–3 it becomes an interruption and gets skipped; tacked onto
the end it gets rushed. It is the only pass that can find what the other three cannot.

*Only this: **what do you do that isn't on this list?***

These 46 rows were assembled from the documents in this repo, not from watching anyone work — so the list
contains only what somebody thought of. Anything named here is a genuine addition. Anything above that turns out
not to be one real thing gets struck. Both are worth more than a filled cell.

### Answered 2026-08-08 (Neil) — only two, and both reactive

| # | The task, in your words | Closest existing row, if any |
|---|---|---|
| 1 | **Inbound mail** from a project lead, customer or support — it triggers the work, and is where the same work gets done again and again | No clean match. Pieces touch `T-M09` (lead capture), `T-S04`/`T-S06` (qualify/discover), `T-S17` (account mgmt), `T-S20` (recover, for support). **Genuine addition** — no row for triaging inbound, and none for support at all |
| 2 | **A colleague asking a question** — a price, a lead time, a competitive analysis — which exposes a knowledge or process gap that could be closed | Subjects map to `T-S11`/`T-M02` (competitive), `T-S08`/`T-S09` (lead time); price has no row (policy, gated). **Genuine addition** — no row for the internal question itself |

**What pass 4 found — and what it didn't.** It found no missing *tasks*: the 46 rows hold up, nothing struck. It found the two **reactive triggers** the register was built without — one external, one internal — and both are where the earlier findings bite:

- **Inbound mail** is the general trigger behind the whole `asked` class in pass 2 (`T-S06`, `T-S10`, `T-S11`, `T-S15`, `T-S16`, `T-S19`, `T-S24`, `T-S27`). Neil named its defining feature unprompted — *"the same work done multiple times"* — the duplication finding (note 3(b)) arriving a third time, now from the front door.
- **A colleague's question** is the internal face of pass 3's `a head`/`nowhere`: when the answer to *"what's the price, the lead time, the competitive picture"* lives in a head and not a record, the only way to get it is to ask — and re-ask. The question *is* the missing record, made audible.

---

# Reading the result

**After all four passes, not during.** Each task now carries three words and, where it earned one, a line of
detail.

| Pattern | What it means | What follows |
|---|---|---|
| **`from scratch` · `remembered` · `nowhere`** | Done well and lost every time — rebuilt from zero next month by whoever is around | **The build list.** Highest value regardless of automation verdict |
| **anything · anything · `nowhere`** | The work evaporates | `record` first. It is the cheapest primitive and does not need the task automated to pay — pass 3's sweep B says exactly what to capture |
| **`varies`** anywhere | A habit, not a process | Nothing can be automated until there is a shape. Pass 1's sweep B usually shows the shape is already there and simply unwritten |
| **`standard` · `a system` · `a system`** | Already handled | Skip it, and skip every work item beneath it |
| **`?`** | The row isn't one real thing | Split it or strike it. Do not build against it |
| **Two people disagreeing** | The task varies by person | Pass 1's answer, arriving from a different direction |

---

## The result — read 2026-08-08

**One root, found four ways.** Every pass pointed at the same mechanism from a different side:
**no owner → nothing kept → nowhere → the work redone.** Pass 2 found the *owner* gap (an owner is needed for
all 29 `remembered` rows; 18 have no firing event at all). Pass 3 found the *landing* gap (15 rows end in
`a head` or `nowhere`). The three duplication rows and both pass-4 triggers are that same mechanism again. It is
not five findings — it is one. And it is **cheaper than the primitives build assumed**, because the fix is
mostly *write it down and give it an owner*, not *build a system*.

**In cost order — what to do:**

1. **`record` — build first; it pays before anything is automated.** Capture the 15 things pass 3 sweep B
   named. The 5 acute ones (`nowhere`) are `T-S15`, `T-S16`, `T-S19`, `T-S23`, `T-M08`. This one primitive kills
   the duplication and answers *both* pass-4 triggers — inbound work stops being redone, and the colleague's
   question has somewhere to look before it's asked.
2. **Write the shape — a template and a definition of done.** The 19 `varies` rows are habits, not processes;
   pass 1 says the shape is already there and merely unwritten. Written, not built.
3. **Assign owners — not triggers.** All 29 `remembered` rows need an owner. Only the **11** with a real firing
   event can later graduate to `a system`: `T-S04`, `T-S05`, `T-S13`, `T-S22`, `T-S26`, `T-M05`, `T-M06`,
   `T-M07`, `T-M09`, `T-M17`, `T-M18`. The other 18 will always need a person on a cadence.
4. **Skip — already handled.** `T-S08`, `T-S12`, `T-M16` read `standard · a system · a system`. Build nothing,
   and strike every work item beneath them.

**The two registers then resolve by block.** In `work-items.md`, the items beneath the three skip-tasks
(#4) need nothing built. In `registers/backlog.md`, no task was struck in pass 4, so all 46 survive — the by-block strike
applies only to backlog rows that map to *no* surviving task, which is a single read of backlog against the 46,
not 115 individual judgements.

**What this is not.** Not an automation programme. The moves are mostly writing — a captured record, a template.
Automation is the *last* mile and only for the 11 event-triggered rows. "Build it, then say it" applies: the
record comes first; the system, if ever, comes after it exists.

**Two cautions from Neil (2026-08-08), which govern how the result is used:**
- **Read the shape, not the cell.** Many sweep-A answers had two or three equally defensible options, so the
  aggregate carries the signal and no single row's word should bear weight on its own.
- **Owners are the roles decision, not a task to allocate now.** The owner gap (pass 2) is a real finding, but
  allocating a role to each task at this stage would be spurious. It feeds step 1 / `PAR-3` and waits there — it
  is not one of the moves. Accordingly the carry into `NEXT.md` is framed forward — *tasks → result → plan
  section → automation* — not as a verdict on lost work.

**Then the other two registers resolve by block.** A work item in `work-items.md` beneath a task reading
`standard / a system / a system` needs nothing built. A row in `registers/backlog.md` mapping to no surviving task is
struck as a group, unread — which is how 115 unreviewed rows get resolved without anyone reading 115 rows.
