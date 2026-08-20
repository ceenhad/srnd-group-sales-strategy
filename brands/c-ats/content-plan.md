# C-ATS — the filled content plan (the churn queue)

*The thing that has always been missing, in Neil's words: "a filled out plan of content per brand and the
mechanical means to churn through it, record the outputs and then apply them." The machinery exists
(S24 — the production line, `../../motion/motion-design.md`) and the tracking is designed (S23). **This is the filled
plan for the first brand**: every content piece C-ATS needs, enumerated against the journey, with its
source atom, its state, its stage-grid row and its target — the thing it points at, written into the piece
(`../../motion/motion-design.md`, "the actions at each stage"). The line works this queue top to bottom;
nothing here requires ideation. Drafted for correction — states and targets are claims, strike wrong ones.
Other brands copy the shape.*

## How the queue is ordered

Cheapest truth first: **(1) publish what is already written → (2) surface what is already published →
(3) draft derivatives from existing atoms → (4) create the genuinely missing → (5) hooks scale only after
the archive count says what to multiply.** The dead ends (handoffs) get wired as each piece lands.

## The queue

*State: `live` · `staged` (written, unpublished) · `written` (in repo, no home yet) · `buried` (published,
unfindable) · `draft` (Claude-drafted, awaiting truth-check) · `missing`. Stage = journey stage / grid row.
Target = what the piece points at — its gateway's threshold action, written into the piece.*

> **Added 2026-08-18, by the template run.** All three doors now have a pathway — `pathway-reverberation.md`,
> `pathway-reflection.md`, `pathway-resonance.md` — so every item below can be read against a slot rather than
> only against a stage. **Two things the run changed about this queue.** The reflection pathway's proof slot needs
> item 40 *before* EST-5 lands, not after, because the raw data argues against the panel until the reading is
> explained. And **— struck 2026-08-18. Both exist**, systemised and running in
> Cinema Tools (`pathway-resonance.md`). **The queue's real missing item is a front door onto them** — and there is
> currently no design for one: ADR 017 v2 withdrew Level 2 and made Cinema Tools Pro internal. What C-ATS's
> self-serve sizing route should be is `../../registers/questions.md` Q52 / `../../operations/decision-request-q52-cats-rules-publication.md`.

### Tranche 1 — already written: publish (days of churn, no authoring)

| # | Piece | Stage | Target | Source atom | State |
|---|---|---|---|---|---|
| 1 | REV-CP warm-room instruction page ("the warm-room rule") | 5 | Verification offer → REV-CP product page | `install-critical-notes.md` p2 | written + derivative set in `content-batch-001.md` (draft) |
| 2 | REF-CP bond-vs-screw instruction page | 5 | Verification offer → REF-CP product page | `install-critical-notes.md` p1 | written — next through the line |
| 3–20 | The 18 knowledge-base articles across 8 pillars (RT60, first reflections, panel thickness, slim-vs-deep, absorbers/diffusers/bass, checkerboard placement, reading an absorption table, BSRIA results, fire ratings, mounting, spec mistakes, concealment → Fabric Walls, verification, + the rest — inventory the full list from `c-ats-shopify`) | 2–3 | Each → its product's on-ramp; the proof articles → registration; concealment → Fabric Walls stage 2 | staged KB, `c-ats-shopify` | staged |
| 21–31 | The paste-ready site blocks: hero, 3 Rs block, depth argument, proof block, the two routes, three product on-ramps, four services | 2 | The depth layer: knowledge base, measured data, the design service | `copy.md` | written (deploy = EST-4/EST-6) |

### Tranche 2 — already published: surface and wire (hours)

| # | Piece | Stage | Target | Source atom | State |
|---|---|---|---|---|---|
| 32 | BSRIA report + five coefficient sheets, surfaced and linked from product pages and proof block | 3 | Registration ("see partner pricing") + a Zoom for the doubtful | live `c-ats.co.uk` PDFs | buried (EST-5) |
| 33 | The reverberation explainer — description + end-card handoff | 1 | The RT60 article (the fuller answer) | live, ~9,500 views | live, ends dead (CON-8) |
| 34 | The 3 Rs explainer set — same handoff wiring | 1 | Each → its fuller KB answer | live `@Complete_ATS` | live, ends dead |
| 35 | Pre-planned reference layouts (three 7.1.4 rooms) | 2–3 | The design service enquiry | built in `c-ats-shopify` | staged (blocked: CLI re-auth, EST-6) |

### Tranche 3 — derivatives from existing atoms (the line drafts; owner truth-checks)

| # | Piece | Stage | Target | Source atom | State |
|---|---|---|---|---|---|
| 36 | REF-CP derivative set (article frame, stage-2/3 pieces, site-conditions paragraph, email item) — batch 002 | 2–5 | Per piece, per its row | item 2 + `product-records.md` | queued |
| 37 | RES-CP corner-placement instruction + derivative set | 5 | Verification offer → RES-CP product page | `product-records.md` | missing (the third predictable question) |
| 38 | Site-conditions paragraphs for all three panels, into the product records (schema group 1) | 5 (+3 reassurance) | The install manual | batches 001/002 | draft (REV-CP only) |
| 39 | Three "how do you do X" recordings: bond-vs-screw, warm room, corner placement — prompts ready | 5 | Embedded in items 1, 2, 37; each → its product page | batch prompts | missing (one session, DOC-2) |
| 40 | "Reading the Reflection A/B chart" — the two-install-types story as proof | 3 | Registration | S21 + published chart (and Q46, 2026-08-17) | queued (check DOC-4 first) |
| 41 | Three rewritten install guides, organised by moment | 5 | Verification offer; fault-finding | existing guides + records | missing (DOC-3) |
| 42 | Fault-finding one-pagers per panel | 5 | Support contact ("tell us before commissioning") | `product-records.md` §doubt | missing |
| 43 | Virtual case studies — room stories around renders, C-ATS-led | 2–3 | The product on-ramps; the design service | render library | missing (CON-11; renders exist) |
| 44 | "Hear the difference" Experience Centre demo film | 3 | The sample kit; a visit; registration | the facility | missing (CON-12) |

### Tranche 4 — genuinely missing, small

| # | Piece | Stage | Target | Source atom | State |
|---|---|---|---|---|---|
| 45 | The adjacency prompt page (treatment → fabric → front-of-room) | 6 | **Fabric Walls stage 2** — the loop | XS-1, one page | missing — the only authored gap in the reverberation pathway |
| 46 | Registration-worth-crossing copy (what a partner account grants, honestly — no unbuilt promises) | 3→4 | Registration completed → the store | `partner-programme.md` | missing |
| 49 | The registered-welcome sequence — several small useful touches, not one email (S26): what the account grants, the entry product, how to buy, who to ask; the offer of a Zoom. Direct, permissioned | 4 | The first order | `partner-programme.md` + store | drafted — `sequences.md` A |
| 50 | The install pack and post-delivery check-in — order-confirmation email + in-box sheet, assembled from items 1, 2, 37–39 | 5 | A first job that succeeds, and telling us | items 1–2, 37–39 | drafted — `sequences.md` B |
| 51 | The adjacency-aware partner email set — timed to what was bought, never a blast; includes reorder ease | 6 | The next layer — Fabric Walls stage 2 | item 45 + purchase data | drafted — `sequences.md` C (C2 blocked: item 45) |

### Tranche 5 — hooks, after evidence

| # | Piece | Stage | Target | Source atom | State |
|---|---|---|---|---|---|
| 47 | **The uncast hook angles, worded by an owner.** Now the full set across all three doors, not four from one: 19 angles, 2 live, 2 blocked, **15 castable** — each with the record field behind it, and the rejections recorded so they stay rejected | 1 | Each → its fuller answer (items 3–20) | `hooks.md` (2026-08-18), the three `pathway-*.md` | candidates — **waiting only on wording** |
| 48+ | Hook variants multiplied per what the archive count ranks and what the bites show | 1 | Each → its fuller answer | CON-3 + published-piece log | waits on evidence |

## The grid check — items counted per row

*The point of the fill: a stage with an empty or all-unpublished row is a visible break. Counted from the
queue above.*

| Grid row | Items | Live today | Verdict |
|---|---|---|---|
| **1 — Unaware** | 33, 34, 47, 48+ | 2 (both end dead) | Seeded by the explainers; hooks correctly wait on evidence. Wire the handoffs first |
| **2 — Interested** | 3–20 (part), 21–31, 35, 43 | **0** | The fullest row on paper and nothing is live — the stage-2 break is a publishing job, not a writing job |
| **3 — Evaluating** | 3–20 (part), 32, 35, 40, 44 | 1 (buried) | Strong material; the proof exists and is invisible. Surface before making anything new |
| **4 — Registered** | 46, 49 (+ store listing fixes, EST-4) | mechanism live | The direct welcome now planned (49). The store's listing copy has no plan item beyond the fix list; decide if it needs one |
| **5 — First job** | 1, 2, 37–42, 50 | **0** | The deepest row once published — and today an installer finds none of it. The install pack (50) assembles it into the order itself |
| **6 — Next order** | 45, 51 | 0 | The loop's two pieces now planned — the adjacency page and the permissioned partner email. Always-on formats still have no C-ATS items |
| *Specifier (parked)* | — | — | Empty, correctly — parked by choice, visible by design |

**What the check says:** stages 2 and 5 break on publishing, not writing; stages 4 and 6 now have their
direct, permissioned pieces planned (49–51) and nothing live. Nothing anywhere needs a campaign.

## Record the outputs — the apply loop

The half that was always skipped. Zero infrastructure to start:

- **Every published piece gets a row in the log below**: date, canonical home, source tag, destination slot.
- **Read monthly, in minutes:** which hooks got bites (source-tagged arrivals), which questions stopped
 arriving (an owner notices), what the estate's numbers moved.
- **Apply:** multiply the winning appeal categories (S23); fix findability where a published question is
 still being asked; retire dead angles; feed the next tranche ordering. Results move the queue — the queue
 does not re-argue the strategy.

### Published-piece log

| Date | Piece (# above) | Canonical home | Tag | Notes |
|---|---|---|---|---|
| — | *(starts when the first piece lands)* | | | |

## Guardrails

Brand truth binds hardest here: C-ATS naming (never the expansion), scattering never diffusion, no invented
figures, problem-named products, no teasing the commercial range, the design service is a choice never a
rescue — and per the hook rules: hooks evidenced and positive, install detail is never a hook.
