# Decided — the ratchet

*Why this file exists: the repo had documents for the **argument** (`group/`), the **plan** (`NEXT.md`) and what
is **open** (`open-items.md`), but nothing recording what is **closed**. So every new fact reopened the argument
and the work spiralled instead of advancing. This is the ratchet: one line per settled decision, the evidence
behind it, and the date. **A decision here is not re-argued.** New evidence either supports it — in which case
add the evidence and move on — or overturns it, which has to be stated explicitly and dated as a reversal.*

## How to use it

1. **New data from real work lands as evidence**, against a decision here or against an open item. It does not
   trigger a rewrite of the reasoning that produced the decision.
2. **A decision changes only when someone says it changes.** "This new fact means X is now wrong" — recorded as
   a reversal with the date, not absorbed silently into a document.
3. **If a fact touches nothing here and nothing open, it is context.** Note it in the relevant document once and
   stop.
4. **The plan moves, the argument stays put.** After recording evidence, the next step is `NEXT.md`, not another
   pass through `group/`.

---

## Commercial model

| # | Decision | Evidence / basis | Date |
|---|---|---|---|
| C1 | **Direct is the default for new territories and appointments.** Distributors only on a 2× scale case or a genuine language barrier, and never at the cost of the direct relationship. | Twenty years inside distribution; and now 21 live appointments where 6 of 18 DT distributors produce nothing, 6 are low, and 3 of the 5 that work are high maintenance. | 2026-07 |
| C1a | **Scope correction, dated 2026-07:** C1 was written as "direct to dealer, globally," which described an intention rather than the operating model. **The model today is direct in the UK and distributor-led internationally.** C1 governs new appointments and the UK; it does not describe the existing network. | The distributor roster (`current-state.md`). | 2026-07 |
| C1b | **Selection criterion, from the roster:** appoint cinema specialists with complete portfolios, not Hi-Fi-rooted distributors. | Hi-Fi-background appointments are consistently no- or low-business; the producing accounts are all cinema specialists. | 2026-07 |
| C1c | **Dead appointments, and any that fail the 2× test, are removed.** A dormant distributor is not neutral — it occupies a territory and blocks the direct approach, so it is a **barrier**. | Neil's decision; the roster shows six DT appointments producing nothing. | 2026-07 |
| C1d | **Most appointments are really dealer-distributors, and are treated as dealers** — the partner programme, the content, no exclusivity. "Distributor" is reserved for the rare case that genuinely multiplies. | Neil's account. Explains both the high-maintenance producers and why the 2× test bites: a hybrid multiplies nothing while still holding the territory. | 2026-07 |
| C1e | **Screen Innovations is white label, not a route to market.** They own the relationship; we supply product. DT has no brand presence in the US through it. | Neil's clarification. Internal only — OEM relationships are not named publicly. | 2026-07 |
| C1f | **The US is the priority territory and is approached directly, with the whole group.** Apex-Tech has resigned from DT and the white-label deal gives us nothing in market, so the largest market is open and unencumbered. | Neil's decision. | 2026-07 |
| S13 | **One content estate, not a marketing estate and a support estate.** The same material does four jobs: hook, de-risk, install support, next order. The support question and the pre-purchase doubt are the same question at different times. | Neil's synthesis. Also explains why documentation was underfunded — marketing didn't own it because it looked like support, and support didn't invest because it looked like marketing. | 2026-07 |
| S14 | **The unit of work is one question, answered well, published where it can be found** — not a campaign and not a manual. "How do you do X" is the atom: support, sales enablement and marketing simultaneously. | Follows from S13; endorsed by the estate's own numbers, where utility rather than production value separated what worked. | 2026-07 |
| S15 | **Site structure per brand and product: marketing on-ramp → technical depth → easy contact.** The on-ramp states the problem solved, the opportunity opened, the time or labour saved; the depth removes doubt; the contact route is explicit. | Neil's synthesis — and it is the information architecture for the rebuild (S10). | 2026-07 |
| S11 | **Support is a documentation problem, not a staffing one.** It reduces to two things: the dealer being trained, and the answer being available when they need it. Manuals and instructions are therefore the priority content class, ahead of everything else in the corpus. | Neil's account: manuals are currently poor and it costs us more than it should. | 2026-07 |
| S11a | **Correction: the documentation gap is concentrated, not group-wide.** C-ATS has the data — three SKUs, documented — and the debt sits mostly with DT, then Fabric Walls and Pro-Fi. **Set the standard on C-ATS, then apply it to DT by mechanism rather than by SKU**, since the range is variant-heavy and fifty-odd products collapse into far fewer manuals. | Neil's correction; C-ATS's own datasheets and BSRIA data. | 2026-07 |
| S16 | **A product data schema comes before any documentation work.** Capturing what *needs* to be documented precedes what is and will be documented; without it, the gap is an opinion rather than a measurable one. Field list in `../product-data-schema.md`. **Completeness becomes a gate on new products.** | Neil's proposal. The Screen Wall — demonstrable since ISE 2023 with no page and no datasheet — is what its absence looks like. | 2026-07 |
| S16a | **Engine owns the mechanical record; this repo specifies the sales and marketing layer above it.** Engine handles SKU, name, weight, dimensions, stock and pricing because that is what an operational system is built for; it was never designed to hold why a product sells, what doubt it must remove, who specifies it, or what we may claim. **That layer is the opportunity, and the deliverable is three answers per field — what data, why, and how it will be used.** A field with no stated consumer never gets filled in. | Neil's framing. | 2026-07 |
| S16b | **Definition comes before everything else.** You cannot state what problem a product solves until you have stated what it is and what it does — and definition is not SKU, name and weight either. The definitional layer is **missing in the middle**: Engine holds the object, marketing holds the pitch, and nothing holds the canonical account of what the thing is. Without one, every datasheet, page, listing and email describes it slightly differently. | Neil's correction. | 2026-07 |
| S21 | **The published absorption sheets on `c-ats.co.uk` are authoritative** — the figures that have been out for years. And the apparent conflict dissolves: the REF-CP chart already plots **Reflection A and Reflection B**, so the two number sets are the two install types (A glued/damped, B free/unfixed as BSRIA measured), not rival versions of one figure. | Neil's decision; confirmed by the published chart carrying both series. | 2026-07 |
| S20 | **The roles are fitted in, not swapped out.** Ben keeps visualisation and adds editorial ownership; the same applies to everyone. So the publishing rate is a **floor set to what the work allows**, not a target requiring reallocation. | Neil, 2026-07-31. | 2026-07 |
| S19 | **Website copy is generated from the product record, not written per page.** The C-ATS Shopify site kept its theme placeholder hero — *"this signature bestseller exceeds all expectations"* — because there was no canonical source for what belongs there, and the 3 Rs vanished from the homepage for the same reason. Fill groups 1 and 2 of the schema and the pages inherit; write page copy first and it drifts again. | Observed 2026-07-31 comparing `c-ats.co.uk` and `c-ats.myshopify.com` (`brands/c-ats/brand-data.md`). | 2026-07 |
| S18 | **C-ATS is the worked example and sets the standard** — `brands/c-ats/product-records.md`. It validated the exercise: six actionable findings from data we already held, including two site-failure modes that belong in a manual in bold. | Filled 2026-07 from BSRIA Report 100241/1 and the C-ATS source repo. | 2026-07 |
| S17 | **The archive seeds the corpus; it does not close it.** Correction of an overstatement: frequency data proposes a ranked list, and that is all it does. The schema defines the required set, and the answers still have to be written. | Neil's correction. | 2026-07 |
| S12 | **Manuals and training are one corpus, differently packaged** — the manual is the reference version, training the structured version. So manuals come first and become the raw material for the training programme rather than competing with it. | Follows from S11. | 2026-07 |
| C1g | **US logistics are solved** — goods move as if we were located there, and a warehouse and logistics partner handles spares. **The binding constraint on US entry is therefore support, not fulfilment.** | Neil's account. | 2026-07 |
| C1h | **Two US entries, not one.** DT recovers the existing dealer base — warm, immediate, no campaign needed. C-ATS is the wide door for dealers we have never met: smallest first order, only brand documented to a standard, only content with demonstrated search pull, ships economically. Different jobs; neither waits for the other. | Revised 2026-07-31 after C1i — the earlier version had C-ATS leading because DT was thought blocked. | 2026-07 |
| C1i | **No conflict: DT enters the US directly regardless of the white label.** It coexisted with Apex-Tech as DT distributor in the same market, so this is the arrangement that has always operated. Whether it continues is SI's decision. *(Supersedes an earlier reading of this as a fork to resolve first.)* | Neil, 2026-07-31. | 2026-07 |
| C1k | **US entry is a conversion problem, not an acquisition problem.** We already know plenty of US dealers; the contacts exist, the direct relationships do not. So marketing is not the constraint — the offer and the trade terms are, and the work is personal rather than campaign-shaped. | Neil, 2026-07-31. | 2026-07 |
| C1j | **The Apex-Tech dealer base is the priority in US entry, and it is warm.** A resigned distributor's dealers become unserved, not absent — they already specify DT and have lost their supply route. Fastest revenue in the strategy, a closing window, and **not dependent on the content programme.** | Follows from C1i. | 2026-07 |
| C2 | **SRND Distribution is the sales arm for our own brands**, not an attempt to become a multi-brand distributor. | Same. | 2026-07 |
| C3 | **The UK is representative of the global market structure** — large distributors, a long tail of small and dealer-distributors, regional manufacturers. So C1 and the competitor analysis travel. | Neil's account. | 2026-07 |
| C4 | **Pricing is registered-partner-only, including end users.** No public prices in the trade channel. | Settled. | 2026-07 |
| C5 | **Two stores, split by the self-evidence test.** If a buyer already knows what it is, Cinema Store; if it must be explained, specified or commissioned, `srnd.store`. **No product exists in both.** | Settled; AVshop.no as the DIY reference. | 2026-07 |
| C6 | **Carried lines are Leyard, MadVR (as a Leyard accessory) and Advatek.** Nothing that competes with our own brands. | Settled. | 2026-07 |
| C7 | **Beyond cinema in trade; B2C stays cinema.** | Settled. | 2026-07 |

## Events

| # | Decision | Evidence / basis | Date |
|---|---|---|---|
| E1 | **ISE is the show, and we are booked.** | The largest European AV-integration show. | 2026-07 |
| E2 | **CEDIA Expo is out** — a dying show, and too late in the year to consider. | Neil's judgement. | 2026-07 |
| E3 | **InfoComm US is a possibility for next year**, not this one. | Open, not committed. | 2026-07 |

## The sales motion

| # | Decision | Evidence / basis | Date |
|---|---|---|---|
| S1 | **There is no field force and we have stopped looking for one.** | Very limited success with sales people over many years; the owner-driven model loads the scarce resource rather than relieving it; three bases (Glasgow, Yorkshire, Marbella). | 2026-07 |
| S2 | **Content does the rep's job** — reach, recall, the technical answer, teaching, and the whole specifier route. | `group/08-sales-motion.md`. | 2026-07 |
| S3 | **Content cannot qualify, discover, close or gather intelligence.** Substitutes: the tools qualify, the spec conversation discovers, Zoom and the store close. Market intelligence has no substitute — an open hole. | Same. | 2026-07 |
| S4 | **An owner's primary sales output becomes authoring on camera**, scheduled like a customer meeting. | Neil's acceptance. | 2026-07 |
| S5 | **Planning splits into judgement and labour; only the labour moves.** The owner never faces a blank page — the editorial output is a ranked proposal to correct, not a schedule handed down. | Neil's correction. | 2026-07 |
| S6 | **The operating loop:** archive → ranked question list → batch recording → edited and published. | Same. | 2026-07 |
| S7 | **The corpus is the asset, not the channel.** Publish canonically to owned properties, syndicate to platforms. | The locked YouTube account demonstrated platform and personnel risk in one incident. | 2026-07 |
| S8 | **Authorship is never scaled.** No bulk or generic content; volume is not the goal. The archive is legitimate because it is our own authored answers. | `group/08-sales-motion.md`. | 2026-07 |
| S9 | **Show what can be shown; explain what cannot.** Short pieces that make an argument. The catalogue fails. | ~9,500 views on a 52-second reverberation explainer; DT's mechanisms-in-motion at 600–1,500; two dozen product films at 1–26. | 2026-07 |
| S10 | **Websites and social restart; URLs, indexed pages and channel history are kept.** The rebuild must not gate the content cadence. | Neil's acceptance, plus the compounding argument. | 2026-07 |
| S22 | **The journey runs as a process.** The buyer journey is defined with **gateways** between its stages; content is generated as **pathways** that move a dealer through each gateway, start to finish and back round the loop. Most of a rep's job is pure mechanics, and the mechanics become process; the judgement residue stays human. | Neil's proposition, 2026-07-31. Design: `group/09-motion-design.md`. **Ancestor evidence (2026-08-01):** the March 2023 programme — nine "bridges", explicit stage-end definitions, "get each CRM company to the next bridge" — `group/2023-buyer-journey-archive.md`. | 2026-07 |
| S23 | **Hooks are multiplied and categorised; every piece has a roadmap position; the funnel tracks like e-commerce; elevation is engineered early.** G1 is a *set* of hooks per product — categorised by appeal (more revenue, time saved, easier to do, better results, the problem named), placed indirectly, each the head of a pathway with a named destination. The journey reads as an e-commerce funnel because every gateway lives in systems — hook-level attribution turns the hook matrix into evidence. Elevation runs product → brand → group as early as the dealer's state allows: brand at the proposition, group at the hinge — never at the cold open, and cross-sell prompts still wait for the first job. | Neil's articulation, 2026-07-31. Design: `group/09-motion-design.md`. **Ancestor evidence (2026-08-01):** the appeal categories appear near-verbatim in Neil's 2023 *Purchase Events* map — solve a problem, save time, earn more revenue, a good experience (`group/2023-buyer-journey-archive.md`). | 2026-07 |
| S24 | **Content is produced at volume on a Claude-assisted line.** The substance is human and never scaled (S8 stands): the records, the measured data, the archive, the decided positions. From each substance atom Claude drafts the derivative set — canonical article, hook variants, recording prompts, datasheet copy, email items — an owner truth-checks in minutes, and distribution is batched, source-tagged and efficient. **No cadence ceremony:** no set floor rate, no formal role confirmations. Volume of pieces, never volume of assertions; nothing needs to be fancy — no fresh ten-minute video every day. | Neil, 2026-07-31. Completes S5: the labour moves — to Claude. Design: `group/09-motion-design.md` component 2. | 2026-07 |

## Partner programme

| # | Decision | Evidence / basis | Date |
|---|---|---|---|
| P1 | **Spend the depth, not the margin. No ledgers** — every element is a discrete act. | `group/03-partner-programme.md`. | 2026-07 |
| P2 | **Distributor services are our baseline, not our differentiator.** We have been a distributor for twenty years; credit, logistics, reps, demo rooms and training are the day job. | Correction of an earlier misjudgement. | 2026-07 |
| P3 | **The differentiator is owning the brands, the factory and what the products do** — changing the product is the thing no distributor can do. | Same. | 2026-07 |
| P4 | **The named technical contact is bounded**, or it rebuilds the trap that made field sales fail. | Same. | 2026-07 |

## Brands and alignment

| # | Decision | Evidence / basis | Date |
|---|---|---|---|
| B1 | **Acoustic treatment design belongs to C-ATS.** Others cross-sell it; none duplicates it. | `group/00-strategy.md`. | 2026-07 |
| B2 | **No brand claims to be the most complex or critical part of the project.** | Neil's rule. | 2026-07 |
| B3 | **DT is solutions for the architectural integration of technology** — deliberately not the projection company. | `brands/display-technologies/positioning.md`. | 2026-07 |
| B4 | **Control is embedded in DT products, never a line item.** | Same. | 2026-07 |
| B5 | **The Scandinavian register applies group-wide.** No superlative without a measurement behind it. | Neil's rule. | 2026-07 |
| B6 | **Never insinuate the dealer can't.** The design service is their choice, never a rescue. | Neil's rule. | 2026-07 |
| B7 | **Light Walls is deferred and worked separately.** | Neil's decision. | 2026-07 |
| B8 | **Tools are never built around our own products**, and the report is the deliverable rather than tool access. | `group/07-tools.md`, ADR 017/019/020/036. | 2026-07 |

---

## Reversals

*When a decision above is overturned, it is recorded here with the date and the fact that did it — never
edited away silently.*

- **2026-07-31 — S20, partially reversed (Neil).** The ceremony half of S20 — a formally set floor rate and
  a formal confirmation of editorial ownership — is struck as "spurious dross": decisions the documents
  invented, not ones anybody needed. Production volume comes from the Claude-assisted line instead (S24).
  What survives of S20: the roles are fitted in, and nothing comes off anyone's plate.
