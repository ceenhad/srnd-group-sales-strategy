# Questions — the asking surface

*One question per row. **Stable IDs, never reused, never renumbered** — that is what stops an answer being
logged against the wrong point. Answers land in the row, verbatim and dated.*

**Why this file exists** (Neil, 2026-08-16): *"The flags and flaps and little docs are an untenable way of
running this repo. Store questions to be asked one at a time so that I can answer sensibly without having to
write a novel every time or risking feedback being logged against the wrong point."*

## How it runs

- **Asked one at a time.** Never a batch, unless you ask for one.
- **A proposed default wherever one is defensible**, so *"yes, that"* is a complete answer. Overriding it is
  also a complete answer.
- **One line is enough.** Detail is optional and only worth giving where the default is wrong.
- **If a question cannot be answered in a line, it is not a question** — it is a session, and it belongs in
  `open-items.md` § "Sessions needed" instead.
- **This is the only place open questions live.** Other documents point at an ID; they do not restate the
  question. *Converting the existing flags to pointers is a mechanical pass, not yet done — see the note at the
  foot.*
- **`⚑` marks a question only Neil can answer** — business or brand truth, where a guess would be worse than
  the gap. **`⌕` marks a fetch** — a fact to look up, not a decision.
- **Every question carries its source**, and the categories are deliberately unflattering:
  **Platform** (an ADR or product doc — authoritative) · **Engine** (read from the live system) ·
  **Observed** (seen in the accounts or the field) · **Repo** (this repo says so, which is weaker) ·
  **Proposed here** (mine — you are ratifying a suggestion, not confirming a fact) · **Unknown**.
  ***Added after Q2 was struck: it was built on a rung of the tools ladder that this repo invented, and asking
  it cost Neil a turn on something that does not exist. A source column makes that visible before the question
  is asked, not after.***

---

## Open

| # | Area | Question | Proposed default | Source |
|---|---|---|---|---|
| **Q10** | Proposal | Should the **layer list be fixed per room type**? | Yes — it makes the completeness rule checkable | **Proposed here** — session 3 |
| **Q11** | Proposal | Where a layer is offered but its **record is empty** — price it, or drop to *named, ask*? | Named, ask | **Proposed here** — session 3 |
| **Q12** ⚑ | Content | **The floor, in beat-sheet briefs per period.** *(Neil and Olivier)* | *No default — yours to set* | **Repo** — `NEXT.md` lane 6; unit reset by Neil 2026-08-15 |
| **Q13** ⚑ | Content | **Who owns publication?** *(Neil and Olivier)* | The producer role | **Repo** — `group/04-content.md` |
| **Q14** | Content | Do **machine-derived pieces publish under a brand's name**, and does that change the gate? | Yes, and no | **Proposed here** — session 4 |
| **Q15** ⚑ | Competitors | **C-ATS** — who do we actually meet, behind the GIK / RPG / Artnovion price band? | *No default* | **Repo** — `brands/c-ats/positioning.md` names the band only |
| **Q16** ⚑ | Competitors | **Fabric Walls** — who, beyond Cinema Build Systems and on-site fabric track? | *No default* | **Repo** — `group/06-competitors.md` |
| **Q17** ⚑ | Competitors | **Pro-Fi** — who? | *No default* | **Nothing researched anywhere** |
| **Q18** ⚑ | Competitors | Which of the **currently named** competitors are wrong — in the document but not met? | *No default* | **Neil, 2026-08-14** — *"different roster"* |
| **Q19** | Competitors | Confirm the **cadence**: quarterly, plus on any surface change | Yes | **Proposed here** — standard 5 |
| **Q20** ⚑ | `G2` | **Anything missing** from the six `G2` lists? | Nothing missing | **Repo** — assembled from brand documents, session 6 |
| **Q21** | `G2` | Are the `G2` lists **published to dealers or held internally**? | Internal | **Proposed here** — session 6 |
| **Q22** ⚑ | Sensing | Is sensing **a line of its own, or a layer of LWCP**? | *No default* | **Neil, 2026-08-15** + LWCP ADRs 0044–0047 |
| **Q23** ⚑ | Sensing | How does it relate to **SRND Solutions** — same, adjacent, or one inside the other? | *No default* | **Repo** — `group/01-commercial-model.md` names the line |
| **Q24** ⚑ | Sensing | Does it **carry a brand**, and whose? | *No default* | **Follows from Q22** |
| **Q25** ⚑ | Roles | **Who fills owner · producer · trade view?** | *No default* | **Repo** — `NEXT.md` step 1, `decided.md` S27 |
| **Q26** ⚑ | C-ATS | The **canonical name** — "C-ATS", "Cinema", or the expansion? | "C-ATS" | **Repo** — C-ATS brand truth flags it unresolved |
| **Q27** | Record | The **`C1` dual-listing wording** — is a brand store *plus* the group store intended? | Yes — narrow the rule to say so | **Engine** — 13 DT codes on both stores, `engine-audit.md` |
| **Q28** ⚑ | Record | Does **Fabric Walls take the second record pass**? | Yes | **Repo** — `NEXT.md` §B, `DOC-20` |
| **Q29** ⚑ | Steering | The proposed **`CLAUDE.md` refinement** — accept, reword, or reject? | Accept as drafted | **Proposed here** — `open-items.md`, 2026-08-14 |
| **Q30** | Training | Pending — **what is being introduced** that bears on training being free to partners? | *Held* | **Neil, 2026-08-15** |
| **Q31** ⚑ | Meta | **Which other repos hold commercial thinking** this one should read? `dt-platform`, `pro-fi-design`, `pro-fi-pantheon`, `cinema-design-process`, `lustre`, `business-finance` are visible and unread | *No default* | **Three for three so far** — `cinema-platform`, `lwcp` |
| **Q32** ⚑ | Meta | **Is anything else background with no commercial value**, as Auctor turned out to be? | *No default* | **Neil, 2026-08-15** |

## Answered

*Answers land here with their date and the exact words, so the reasoning survives the decision. Nothing yet —
the register opens 2026-08-16.*

| # | Question | Answer | Date |
|---|---|---|---|
| **Q1** | Is fit-out something the group does deliberately? | **Only for our own rooms.** Fit-out where SRND product is the substance of the room; never a general contracting service. **A boundary, not a yes or no** — so it enters the service offer as a bounded line, and `XS-7` is answered for this row: not a gap in the strategy, a scope limit that was never written down | 2026-08-16 |
| **Q2** | ~~What is "partner-network escalation" commercially?~~ | **STRUCK — the premise was invented.** Neil: *"this is something you have invented so the question lacks much info for me to answer usefully."* Confirmed: the phrase appears nowhere in the platform documentation. The rung is removed from `group/07-tools.md`'s ladder. **A question asked about something that does not exist** | 2026-08-16 |
| **Q3** | Pro-Fi recipe pack — bought, or comes with the speakers? | **Answered in part, and it opened the real question.** *"Cinema Tools Pro gives us choice… but what if they asked to use Pro-Fi processors on a job with other speakers? Should they pay then? **This is where the pre-sales vs paid services layer often bites.**"* Continued as Q33 | 2026-08-16 |
| **Q8** | One document, or core plus appendix? | **Neither — two artefacts at two stages.** *"The quote is an important mechanic document which allows a customer to formally accept our offer before it goes to invoice. That mechanical quote can also contain **optional 'have you also considered' type line items** that would be added to the invoice. That quote can perhaps be seen as **distinct from the proposal stage which is much more sales based**. Engine stores sales interactions by project so it would be possible to have a separate proposal which when accepted moves to formal quote then to invoice."* **Plus a hard constraint and a failed precedent:** *"The process of making the proposal has to be **quick and easy** and is a loop we have [been] round a dozen times. At one time we even had **three graphic designers on staff producing per-product blocks to drop into design-based proposals. Doesn't work.** **Speed of delivery of proposals is just as important as content** quite often."* **▲ Refined same day, and it reverses the strike:** *"The content blocks thing works… **if you have the content blocks!** All of our products and services are going to have to be listed in there. To add a block seems achievable but that **then needs a document template that can use it**."* — so the failure was **authoring blocks per proposal**, not assembling them. Two deliverables: **a block library covering every product and service** (rides on the record), and **a template that consumes it**. And a dependency it exposes: **a service cannot have a block until it is defined and costed**, so session 1 gates the proposal build | 2026-08-16 |
| **Q9** | What goes out to a dealer today when a room is quoted? | **A store quote.** *So the proposal is a new artefact and session 3 is a **build, not a template**. It also explains the attach problem measured in finding 31: a store quote is a list of the line items asked for, and it has no place to put a layer nobody requested — £472,320 of Komodo against £38,452 of Screen Wall is what a quoting mechanism with no room in it produces* | 2026-08-16 |
| **Q7** | Can the priority band be overridden by hand, and is the override recorded? | **Yes, and recorded.** *An unrecorded override turns a computed ranking back into a gut call with a table around it, and nobody can tell later which it was. With the override logged, the band stays evidence — and a pattern of overrides is itself a signal that the rule needs fixing* | 2026-08-16 |
| **Q6** | Does the qualification record carry a decline value? | **No — admit + priority only**, with discretionary refusals logged separately as discretion. *Keeps the record automatable and stops a judgement call hiding inside a verdict field, which is what the reframe existed to separate* | 2026-08-16 |
| **Q5** | On staged-payment projects, who assesses ability to pay, and against what? | **Against the schedule, not the dealer.** What matters is whether the payment stages cover our outlay at each point — **a project structured so we are never out of pocket needs no assessment at all.** *So there is no second credit test anywhere: the dealer is covered by checkout and Iwoca, the project by its own schedule. `T-S04` keeps "every project is worth the time" without a hidden solvency judgement underneath it, and the residue session 1 left open is closed* | 2026-08-16 |
| **Q35** | Where does the product sweep live? | **A field on the record.** Rides on step 3 rather than beside it — one pass, not two. **Added as `N10` — "the design work this needs to succeed"** — in the knowledge layer, distinct from `N1` (selection) and from true services. *The form is now 59 fields; every "of 58" elsewhere is one short, logged as a single mechanical pass rather than scattered now* | 2026-08-16 |
| **Q4** | Do Partner-tier dealers get an allowance of free design time? | **WITHDRAWN as a question — it is session work now.** Q34 settled that free is legitimate but only from *"a clearly defined policy of what is and is not allowed on free things"*, and only on a costed service. **An allowance is one line of that policy, and the policy is written in session 1**, not decided in isolation here | 2026-08-16 |
| **Q34** | Is the principle: services price like products, no cross-line subsidy, free only as pre-sales or a published partner grant? | **Close, and corrected in the important place.** *"Published partner grant is too strong. **A clearly defined policy of what is and is not allowed on free things.** Cross-selling with a free service incentive is real. **An incentive can only work though where the service is defined and costed — otherwise in the customer mind it's just work you needed to do as part of their sale.**"* → **so free is legitimate, but only from a defined policy, and only where the thing given already has a price.** Plus a second category split: *"products should be swept to identify clearly what specific project-specific design is needed for [each] to be successful — then can it be automated, can a tool be created, or is it really labour which does need paying for. **That's separate to true services like a sound isolation design.**"* | 2026-08-16 |
| **Q33** | What decides free vs paid on a design deliverable — whose product is in the room? | **DISSOLVED — the question was malformed, and Neil said why:** *"You are conflating. **What makes it our room? What makes a service sale have different rules to a product sale?** If they [buy] brand x does that entitle them to a discount on the costs of brand y."* **All four options offered were versions of "when do we give it away", which assumed giving away was the default state.** *And it was the second time: crediting the fee against the order was rejected on 2026-08-15, and "free because they're buying hardware" is the same cross-subsidy in a different costume.* Reformulated as **Q34** | 2026-08-16 |

---

**Not yet done, and it is the point of the file:** the flags, banners and "still open" lists scattered through
`open-items.md`, `NEXT.md`, `backlog.md`, `current-state.md`, `archive-findings.md` and
`group/13-standards-decision-sheet.md` **should become pointers to these IDs rather than free-standing prose.**
That is a mechanical pass over six documents, and it should shrink the repo rather than grow it.
