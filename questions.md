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
| **Q3** ⚑ | Services | The **Pro-Fi recipe pack** — three reference room classes from `recipe_generator.py`, which the platform calls *"the customer-facing source of truth"*, with any specific install getting its own. **Does a per-install recipe get bought, or come with the speakers?** | Comes with the speakers | **Platform** — `cinema-tools/docs/validation/tier1-briefs/recipe_pack.md` |
| **Q4** | Services | Do **Partner-tier dealers get an allowance of free design time**? | No — training and Experience Centre hosting are the depth already spent | **Repo** — `group/03-partner-programme.md` *(the tier is designed here, not observed)* |
| **Q5** ⚑ | Credit | On **staged-payment projects** (shipped part-paid), who assesses ability to pay, and against what? | *No default* | **Observed** — the Komodo at 60 % received, `current-state.md` |
| **Q6** | Dealer bar | Does the qualification record carry a **decline** at all, or admit + priority with discretionary refusals logged separately? | Admit + priority; discretion logged apart | **Proposed here** — session 1 |
| **Q7** | Dealer bar | Can the **priority band be overridden by hand**, and is the override recorded? | Yes, and yes | **Proposed here** — session 1 |
| **Q8** | Proposal | **One document, or core plus appendix?** | One document | **Proposed here** — session 3 |
| **Q9** ⌕ | Proposal | **What goes out today** — a store quote, or something else? | *Fetch, not a decision* | **Unknown** — nothing in any repo says |
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

---

**Not yet done, and it is the point of the file:** the flags, banners and "still open" lists scattered through
`open-items.md`, `NEXT.md`, `backlog.md`, `current-state.md`, `archive-findings.md` and
`group/13-standards-decision-sheet.md` **should become pointers to these IDs rather than free-standing prose.**
That is a mechanical pass over six documents, and it should shrink the repo rather than grow it.
