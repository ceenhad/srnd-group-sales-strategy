# Premises — what the work is standing on

*One premise per row. **A premise is a claim being built on, not a question waiting for an answer** — that is what
separates this file from `questions.md`. A question blocks; a premise is assumed true and carries weight until
somebody breaks it. **Stable IDs, never reused.***

**Why this file exists** (Neil, 2026-08-18): the C-ATS run rested on a premise that was wrong — *nobody can size a
C-ATS room without ringing us* — and it was wrong for sixteen days inside a product record before anyone was
asked. It was never stated as a premise, so it was never available to be broken. It surfaced only because Neil
happened to read one line of a 640-line output. **A premise buried inside a deliverable can only be caught by
reading the deliverable. A premise in a row can be broken in seconds.**

## How it runs

- **Stated before the work, not after it.** Anything load-bearing goes in a row before it carries anything.
- **Source, in the unflattering categories** (`../method.md`): **Platform** (an ADR — authoritative) · **Engine**
  (read from the live system) · **Observed** (the accounts or the field) · **Repo** (this repo says so, which is
  weaker) · **Proposed here** (mine — you are ratifying a suggestion, not confirming a fact) · **Unknown**.
- **Every row names what would break it.** A premise with no falsifier is not a premise, it is a belief.
- **Status:** `holding` · `challenged` (evidence against it, not yet resolved) · `qualified` (true within stated
  limits) · `broken` (with the date and what broke it — **kept, never deleted**, because the work built on it
  has to be findable).
- **A broken premise is not a failure, it is the point.** The register earns its place by how often rows break.

## The register

| # | The premise | Source | What rests on it | What would break it | Status |
|---|---|---|---|---|---|
| **PR-1** | The brand's material is in `brands/<brand>/` | Proposed here | The whole brand-run method; every "missing" verdict in the three C-ATS pathways | Finding the answer in another repo | **broken 2026-08-18** — the C-ATS sizing method is systemised in `cinema-platform` `products/cinema-tools/`. Fix folded into `../brands/_template/the-brand-run.md` |
| **PR-2** | What C-ATS is short of is **content** | Repo (`../group-strategy/strategy.md`) | The entire run; `../brands/c-ats/content-plan.md`; the case for a production line | Counting the blocked items and finding most are not authoring jobs | **challenged** — see the count below |
| **PR-3** | The dealer's own words for each problem must come from the sent-mail archive (CON-3) and may not be drafted | Repo → Proposed here | The `[?]` at the head of all three pathways; every "problem named" hook's wording; `O1` on all three records | An owner simply saying the words — which costs minutes against days of mining | **broken 2026-08-18.** Neil: *"all of that shit about real recent jobs etc — what trash and bullshit. Just needs cleaned out regardless."* **The parking was ceremony, not caution.** `W2`'s *who* was answered in one sentence the first time it was asked (Q55). Cleaned out of `../brands/c-ats/` and `../brands/_template/`; still present in DT and Fabric Walls |
| **PR-4** | The BSRIA measured data is C-ATS's strongest proof asset | Repo (`../brands/c-ats/positioning.md`) | Slot 4 on all three pathways; the proof-first ordering of the content plan | A stronger asset existing — and the design rules look like one | **broken 2026-08-18** (Q61). Neil: the credibility is *"the systemised method — that's the real answer."* **The data stays real, published and free; it is not what credibility rests on.** Consequences: slot 4 on all three pathways leads with the wrong asset, and **C-ATS's credibility claim is currently unpublishable** — the method is black-boxed, which makes DR-Q52 this brand's central question rather than a content one |
| **PR-5** | The consolidated ledger describes C-ATS's addressable field | Observed | `../brands/c-ats/segments.md`; the 53-of-549 finding; every segment count | The missing sources landing | **qualified** — Shopify (MON-8) covers the 2023→2026 middle and is absent; engine is not extracted; account identity is normalised to a floor, not to exactness |
| **PR-6** | A dealer who already buys from the group re-enters C-ATS at stage 2, not stage 1 | Repo (`../motion/motion-design.md`) | The 142-account reading in `../brands/c-ats/segments.md` | Evidence that group trust does not transfer across brands | **qualified** by Q51 — it says what a dealer has *seen*, and must not become a ranking |
| **PR-7** | Three problems means three doors | Repo (`../group-strategy/buyer-journey.md`) | Three pathway files; the hook set's structure | Q50 taken to its conclusion: if the **system** is the product, the door may be the **room**, not the panel | **broken 2026-08-19** (Neil): **one way in — the room.** *Follows from `Q50` (the system is the product, no panel leads) and `Q70` (the 3 Rs **is** the design system): a dealer is sold the room's acoustics, not a panel for a symptom.* **Consequence: the three `pathway-*.md` files collapse into one**, and the hook set's structure goes with them. **This merges with `MTH-1`** — the pathways were already owed a rewrite from prose into rows, deliberately queued behind the drill-down *because the drill-down might change what they say.* **It did.** One rebuild, not two |
| **PR-8** | Hooks cannot be cast without an owner authoring the wording | Repo (S8 — authorship is not scaled) | Nothing in `../brands/c-ats/hooks.md` being castable today; the whole set waiting on Neil | An owner correcting a draft rather than authoring from blank — which is what the production line says everywhere else (`../motion/motion-design.md` component 2, step 3) | **challenged** — the rest of the method says *correct a draft*; only the hooks were held to *author from blank*, and I did not notice the inconsistency |
| **PR-10** | Checking the platform means reading its documents | Proposed here | The 2026-08-18 correction to PR-1; DR-Q52's first draft; the "Tier-0 route exists" claim in three files | A document in the platform being built on a superseded ADR | **broken 2026-08-18, hours after PR-1** — `03-c-ats-partner-tool.md` (24 May) is framed on ADR 019, superseded by 017 on 13 Aug, and describes a Level 2 surface 017 v2 §5 withdrew. **Checking the platform is not enough; the ADR status is the check** |
| **PR-11** | `positioning.md` states settled brand truth | Repo | Every hook's justification; all three pathways' propositions; `content-plan.md`; the whole C-ATS run | Checking who confirmed it | **broken 2026-08-18** — **zero attributions to Neil in 249 lines.** Drafted by a session, never confirmed, cited as settled by everything since. Atomising §1 gave 16 claims, of which 5 were `product-records.md` verbatim and 2 were open questions nobody had asked. Fix: `../brands/c-ats/claims.md` and `../method.md` § The drill-down |
| **PR-13** | The REF-CP `A`/`B` install-type difference is a **commercial risk to manage** — an installer screws it, skips the glue, the room misbehaves and we get blamed | Proposed here (`../brands/c-ats/product-records.md`, "the install trap — the most important thing in this record") | `install-critical-notes.md` page 1 and its "highest-return documentation" status; `../brands/c-ats/pathway-reflection.md` slot 7 (first job) and half of slot 4; `content-plan.md` item 40's framing; `DOC-1`; the `C2.20` qualification | An owner saying how they actually handle it | **broken 2026-08-19** (Neil): *"the whole A/B trap hand-waving fire-breathing dragon of a problem… no one cares. I just use bonded numbers in the design and that's it."* **A/B is a design input, settled by always designing on the bonded figures.** *The two published curves are a measurement configuration, not a field hazard.* **Nothing was mis-measured — a risk narrative was invented around a real technical detail and then rated the most important thing in a 640-line record.** Page 2 (the cold-room adhesive failure) is unaffected and is the range's real predictable failure (`R4`) |
| **PR-12** | All three C-ATS panels are 50 mm deep | Repo (`../brands/c-ats/product-records.md` line 62), sourced from `c-ats-shopify:data/panels.json` | The shared `Depth` field; `C1.8` (**confirmed** 2026-08-18); RES-CP's scope of supply, `O4` and `R1`; the whole depth-and-floorspace commercial argument; `Q63`'s own framing | An owner stating the dimensions | **broken 2026-08-19** (Neil, `Q63`): *"the Ref and Rev panels are 50mm and the Res is 43mm."* **The canonical dataset is wrong, or was, and the store sells on it** → `DAT-1`. *Two things worth keeping: it is the **first `confirmed` claim row to turn out false**, and it was confirmed *because* it was a verbatim duplicate of the record — the duplication propagated the error and doubled the apparent confidence in it. And it broke while answering a question that had assumed it* |
| **PR-9** | The unit of output is a document | Proposed here | Everything produced this session — ~640 lines of prose across seven files | Neil, 2026-08-18: *"even the data share must be of proper structured data not piles of documents"* | **broken 2026-08-18** — see `../method.md` § "What the work produces" |

## PR-2, counted

*The premise says the shortage is content. The three pathways name what they consume. Classified by what the work
actually is:*

| Kind | Items | Count |
|---|---|---|
| **Publish something already written** | DOC-1 (both one-pagers), the staged KB articles (items 3–20), EST-5 (surface the BSRIA report) | 3 |
| **Wire something already published** | CON-8 (the handoffs — every live piece ends dead) | 1 |
| **Fix or build a surface** | EST-4 (the £0.00 presentation, product order, marine demotion), EST-6 (CLI re-auth and deploy), a sizing route (undesigned — DR-Q52) | 3 |
| **Fetch a fact** | DOC-4 (read the A/B values off the published chart) | 1 |
| **Record** | DOC-2 (three "how do you do X", one session) | 1 |
| **Actually write something new** | DOC-3 (guides by moment), item 37 (corner placement), item 42 (fault-finding), item 45 (adjacency) | **4** |

**Four of thirteen are authoring.** The rest is publishing, wiring, fixing and one fetch. **The strategy's claim
that content does the selling is untouched by this** — but the working assumption that *producing* content is the
bottleneck does not survive its own plan. On the evidence of this run, C-ATS's journey is blocked mainly on
things that are already written and not reachable.

*Stated as a finding, not a conclusion: this is one brand, and the count comes from a plan I drafted, so it
inherits whatever is wrong in the plan.*
