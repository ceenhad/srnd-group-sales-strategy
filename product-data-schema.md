# Product data — the sales and marketing layer

*Why this file exists: **capturing what needs to be documented has to come before what is and will be
documented.** But the useful contribution is narrower than a schema. **Engine already handles the mechanical
record** — SKU, name, weight, dimensions, stock, pricing — because that is what an operational system is built
for. What it was never designed to hold is the layer that makes a product sellable and specifiable. **That layer
is the opportunity here, and the deliverable is not a field list but three answers per field: what data is
needed, why it is needed, and how it will be used.**

**Two rules that keep this from colliding with Engine:**

- **Engine owns the mechanical layer and the storage.** Not specified here, not duplicated here. Where a field
  below already exists there, this file defers and records the mapping.
- **This file specifies the layer above it** — and the *why* and *how used* columns are the point. A field with
  no stated consumer is a field nobody will fill in, and that is how product data dies.

**And the order matters.** Definition comes first. You cannot state what problem a product solves until you have
stated what it *is* and what it *does* — and "definition" is not SKU, name and weight either. Engine has those and
they define nothing. The definitional layer is missing in the middle: Engine knows the object, the marketing knows
the pitch, and nothing holds the canonical account of what the thing actually is.

**That gap is doing real damage.** Without one canonical definition, every datasheet, web page, store listing and
email describes the product slightly differently — which is most of what makes a range feel unprofessional, and it
is why the same questions keep arriving.

*A first cut, for correction. Every row is a claim about how the estate works, so a wrong row is worth striking.*

> **This file is the model and the argument; the form is `product-record-template.md`; the roster is
> `product-register.md`.** Fill records against the form; change the model here and the form follows.

---

# Part one — the model

*Added 2026-08-02, and it reorders everything below it. **The question is not "what data does a product have?" It
is "what must the database hold for content to act as the sales and marketing rep?"** (Neil). Those produce
different lists, and the first version of this file answered the first question.*

## The rep test — what "done" means

A rep does **four jobs**. The database is complete when it can do all four without the rep.

| # | The job | The test | Where in the journey |
|---|---|---|---|
| **1** | **Attract** — make the solution as attractive as it honestly is | Can you start a conversation a dealer actually wants to have? **This is where every hook comes from** | Stages 1–2 · gateways G1, G2 |
| **2** | **Defend** — hold it against the alternatives | Can you win the comparison, including against doing nothing and against the dealer's incumbent supplier? | Stages 2–3 · G2, G3 |
| **3** | **Build trust** | Can you be believed? The proof, the honest limits, **and the claims we refuse to make** | Stage 3 · **G3, the hinge** |
| **4** | **Deliver** — answer every question clearly, all the way to a working install | Can a dealer get from interest to a room that works without asking us anything? | Stages 4–6 · G4, G5, G6 |

**Jobs 1 and 2 are the front half and they are joined:** you cannot make something attractive for long without
being able to defend it, and **a claim you cannot defend is a hook that costs you the dealer** when it meets a
competitor's answer. Jobs 3 and 4 are the back half — trust, then the questions answered clearly on the way to
install. **The front half starts things; the back half is what makes them repeat.**

## The tasks — what the database has to serve

*The jobs above are what a rep is **for**. **The tasks are what they actually do all week**, and the record has to
be the substrate for each one — otherwise it is a reference book rather than a working system.*

**The tasks are enumerated once, in [`group/10-tasks.md`](group/10-tasks.md)** — 46 of them across a sales person's
week and a marketing person's, each with an automation verdict (`automated` · `automatable` · `assisted` ·
`manual`), the performer today, where it fits in the journey, and the record fields it consumes and feeds. Not
repeated here.

**Three things from it bear directly on this model:**

1. **`assisted` is the largest verdict at 46 % of all tasks** — a person reviewing what the system drafted.
   **The system can only draft from the record**, so an empty record silently reverts every assisted task to
   manual. That is where the tasks fit: **the record is the automation substrate.**
2. **A field no task consumes should be struck.** The tasks are what the fields are *for*, and that is the
   difference between a product database and a filing cabinet.
3. **Tasks are the capture routes, read from the worker's side.** A rep gets smarter by doing the job; content does
   not, unless the task's output is caught. **Every task removed from a human also removes a learning input** — the
   routes in the next section exist to catch what would otherwise be discarded.

## The domains — what the database must hold

*Twelve subject areas, each named by the question a dealer asks. A rep carries all twelve; one of the four jobs
fails without each. The right-hand column is the state of the form today, which is what shows where the form has
no fields at all.*

| The dealer's question | Domain | What it holds | Serves | In the form today |
|---|---|---|---|---|
| *"What is it?"* | **Physical** | Construction, materials, finishes, sizes, weights, what arrives in the box | 4 | `D1` `D6` `D8` — thin, and rightly: engine owns the mechanical half |
| *"What does it do, and how well?"* | **Performance** | The function, the mechanism, the measured numbers, the test they came from, the limits | 2, 3 | `D2` `D3` `D9` `G1` — **split across two groups; performance has no home of its own** |
| *"Where does it go, and how many do I need?"* | **Application** | Which rooms and positions, the sizing rule, the quantity, a worked example, where it does not belong | 1, 4 | `D4` `D5` `N1` `N2` — **the most-asked domain in every brand** |
| *"What does it need from everything else?"* | **Integration** | Power, structure, clearance, what the builder must leave, what it pairs with | 4, 1 | `D7` `D10` `N5` |
| *"Why this one and not theirs?"* | **Competitive** | The named alternatives, what decides between them, where we win, **where they win**, what to say to a dealer who already buys the other | **2** | **`N4` only — one field for the whole job of defending** |
| *"What does it cost me to sell and fit?"* | **Commercial** | Order unit, lead time, availability, margin position, the labour it takes on site, what skipping it costs. **Never the price** | 1, 4 | **nothing** |
| *"How do I know it works?"* | **Evidence** | Test reports, reference rooms, demonstrations, renders — and which we may show | **3** | `G4` |
| *"What could go wrong?"* | **Risk** | The doubt behind the question, the failure modes on site, what a mistake costs | 3, 4 | `R1` `R2` `R4` |
| *The questions we actually get asked* | **Answers** | Each one written down, answered in the answerer's own words, with where it is published | **all four** | `R3` `N3` |
| *"What happens after I order it?"* | **Lifecycle** | Delivery, install sequence, commissioning, spares, what can be replaced, how long we support it | **4** | **assets only (`A1`–`A11`) — the documents, not the facts** |
| *"What is interesting enough to lead with?"* | **Hook material** | Which of the five appeals this product can honestly carry, and the substance behind each | **1** | **nothing** — hooks are designed in `group/09-motion-design.md` with no product-level source |
| *"What are we allowed to say?"* | **Governance** | Claims supported and by what, claims we refuse to make, whether it is released yet, when the record was last checked | all four | `G2` `G3` `K1`–`K3` |

**What that table says:**

- **The form covers the back half well and the front half barely.** Jobs 3 and 4 — trust and delivery — have
  fields. **Job 2, defend, has one field. Job 1, attract, has no source at all** beyond the on-ramp group. Which is
  the wrong way round, because the front half is where things start.
- **Domain 5 is one field doing a whole job.** *"A rep must be able to defend it against the competition"* — and
  the record offers a single line called "comparison". Defending needs the named alternative, the dimension, where
  we lose, and what to say when the dealer already buys from them.
- **Domain 6 is absent entirely**, and it is half of why a dealer specifies anything. Not price — **price is
  engine's and is gated** — but lead time, order unit, availability and the dealer's own business case.
- **Domain 11 is the missing link to the hook machinery.** `group/09-motion-design.md` designs hooks by appeal
  category — *more revenue · time saved · easier to do · better results · the problem named* — and **nothing at
  product level says which appeals a given product can honestly carry.** So hook volume, which the design says is
  the point of G1, currently has no source and would be invented per campaign. That is exactly the failure the
  production line forbids.
- **Domain 10 holds documents where it should hold facts.** The asset audit says whether an install manual exists.
  It does not say the lead time, the install sequence, or whether a part can be replaced without pulling the
  assembly — which are the things a dealer asks *on the way to install*.

## Where each domain comes from — the capture routes

***This is the process half, and it is the part that decides whether any of it ever gets filled.*** A rep's
knowledge is not written in a documentation project; it accretes from the work. **So does this.** Twelve domains do
not need twelve projects.

**A route is a rule of the form: *when this happens, this gets written down.*** That is all one is. It has a
trigger, a thing captured, and a person who is already present at the moment it fires. **Five of the six triggers
are events that already happen every week** — the work is being done either way; only the writing-down is new.

*Named by the trigger, deliberately: a route whose name does not say when it fires is a route nobody remembers to
run.*

| # | When this happens… | …this gets written down | Who is already there | How often |
|---|---|---|---|---|
| **RT1** | **A product is made or changed** | What it is, what it is supplied with, what it needs from the building, how it goes in — Physical, Performance, Integration | Design & production | Per change |
| **RT2** | **A test result or report arrives** | The measured performance, the test basis, and what may be shown as proof — Performance, Evidence | Whoever commissioned it | Rarely |
| **RT3** | **We help specify a job** | How you choose it and how many, the layout, what it pairs with — Application, Integration | Whoever specs jobs, **and we help spec routinely** | **Daily.** Our only discovery channel (`NEXT.md` lane 4) |
| **RT4** | **We answer a question** — pre-sale or on site | The question itself, the answer in the answerer's words, and what went wrong — Risk, Answers, Lifecycle | Whoever answered it | **Daily**, and already answered once by email |
| **RT5** | **We quote, and when we win or lose** | The commercial case, and which competitor beat us on which dimension — Competitive, Commercial | Whoever quoted | Per quote. **Already runs — engine's CRM is classic pipeline management** |
| **RT6** | **A position is settled or reviewed** | What may and may not be claimed, and what a product can honestly be hooked on — Hook material, Governance | The owners | **The one genuinely new habit** |

**Three consequences worth stating plainly.**

1. **A running route fills its domains forever; a field filled by a push starts decaying the day it is written.**
   Stand the routes up before filling more fields — otherwise this becomes another documentation project, and the
   reason those fail is that they ask one person to hold all twelve domains.
2. **RT5 already runs, and this file previously said it did not.** **SRND Engine's CRM does classic pipeline
   management** (Neil, 2026-08-02), so quotes, stages and win/loss are captured today. The corrected question is
   narrower and is a question *for* engine, not an assumption about it: **does the recorded loss reason carry which
   competitor and which dimension** — the structure domain 5 needs — or only that the deal was lost? If it does,
   `X6` is a read from engine rather than a new habit. **Checking that is `backlog.md` SYS-2**, and it is a Fetch.
3. **The two daily triggers already produce this and throw it away.** Every spec conversation fills the
   application domain; every support answer fills the answers domain. Both happen anyway, both get written into an
   email and lost. The archive is the proof (`backlog.md` CON-3) — **the knowledge exists, it has just never had
   anywhere to land.**

**And the standing boundary is unchanged.** Engine owns the mechanical record and the numbers — SKU, dimensions,
stock, pricing, lead times as data. **The record holds the argument, not the number**: not the price but the
dealer's business case, not the stock level but what to say about availability. Where a domain touches engine, it
defers and records the mapping (`decided.md` S16a). **And group commercial policy — terms, credit, territory —
stays out of the record entirely**; it is settled in `decided.md` and is not product data (Neil, 2026-08-02).

---

# Part two — the fields

*The detail beneath the model. Sections 1–8 are the original groups; **9–12 add the domains the model showed were
missing.** Read in the domain table's order, not in number order — the numbers are anchors, kept stable because
other files cite them.*

---

## 1. What the product actually is

*The foundation, and the group that has to be filled before any of the rest can be written honestly.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **What it is, in one sentence** — category, not pitch | One canonical definition, or the estate drifts into several. This is the sentence every other asset inherits | Datasheet opener, page title, store listing, the answer to "what is this" |
| **What it does** — its function, plainly | Function is not benefit and not mechanism; conflating them is how technical copy goes wrong | The technical layer; the basis of the marketing layer above it |
| **How it works** — the mechanism | Depth for the reader who needs it, and the field that lets documentation be written **per mechanism rather than per SKU** | Grouping the manual set; explainer content |
| **What it is for** — the applications | Products get misapplied when the intended use is implied rather than stated | Selection guidance; specifier material |
| **What it is *not* for, and where it does not apply** | **Misapplication is expensive** — a bad room, a lost reputation, a support case that was never a fault. Nobody writes this down and everybody needs it | Boundaries in the datasheet; the first question support should be able to point at |
| **Scope of supply — what is actually supplied** | The commonest cause of a bad first order is a wrong assumption about what is in the box | Order confirmation, install manual, quoting |
| **What it requires from others** — power, data, structure, fixings, clearances, site conditions, adjacent products | **This is the biggest single source of site pain**: what must be true, and what the builder has to leave. It is definitional, not marketing | Install manual, drawings, the specifier's coordination notes, and the pre-order conversation |
| **Configuration space** — variants, sizes, options, and precisely what varies | A variant-heavy range documented as separate products multiplies work for no benefit | Collapsing the manual set; configurators; the store |
| **Limits** — maximum and minimum sizes, loads, environmental range | The honest edge of the envelope, which is also where the interesting questions come from | Feasibility answers; avoiding a promise the product cannot keep |
| **Where it sits in the room or system** | The layer it belongs to, and what it meets | Whole-room content; the adjacency map |

## 2. Why to buy it — the on-ramp

*The layer that turns a record into a reason to look. Nothing operational needs these, which is exactly why they
are missing.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **The problem it solves, in the dealer's words** | A product on its own does nothing; the problem is what engages. And the dealer's phrasing — not ours — is what gets searched | Hook copy, page opener, campaign silo, search terms, the words AI answers match against |
| **The time or labour it saves** | One of the four things a dealer actually cares about, and the most under-used | Comparison arguments; the format that already works for us — the Fabric Walls factory-versus-site film is the brand's best performer |
| **The opportunity it opens** | Dealers often don't know *why* to specify something; a product that wins a job is worth more than one that fits a job | Sales enablement, cross-sell prompts in the spec conversation |
| **What it replaces or avoids** | The dealer is choosing between options, including doing nothing | Comparison content, objection handling |
| **Is this an entry product or a flagship?** | Every brand needs a door-opener distinct from its showpiece; the flagship demonstrates depth, the entry product opens the relationship | Targeting the on-ramp; deciding what gets promoted to cold audiences |

## 3. The doubt it has to remove

*The single most valuable group here, and the one no operational system would ever contain. **De-risking is the
conversion mechanism** at this level — a dealer specifying a product puts their own reputation on someone else's
box.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **The specific doubt or objection this product meets** | Different products fail to sell for different reasons — will it fit, will it be quiet enough, will it look right, can I install it | Decides *which technical asset is load-bearing* for this product, rather than documenting everything equally |
| **The questions it actually generates** — pre-sale and on site | This is the content backlog, per product, and the two are the same question at different times | Ranks the corpus; tells you what to write next; measures support load |
| **What goes wrong on site with it** | The installer's real fear, and the thing peer reputation is made of | Fault-finding guide, "how do you do X" video, install-manual priorities |

## 4. Who decides on it

*Engine knows who bought it. It does not know who specified it, and those are different people.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **Purchaser vs specifier** — integrator, AV consultant, architect, interior designer, end client | Being named pre-tender is worth more than winning a spec conversation later, and the machinery differs entirely | Decides whether this product needs NBS clauses, Revit objects and finish samples, or only an install guide |
| **Who signs it off, and what convinces them** | The end client, the architect and the integrator are reassured by different things — a finish sample, a measured report, an install time | What proof to put in front of whom, rather than one asset for all |

## 5. What we may and may not say

*Governance, and it belongs in the record rather than in someone's memory.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **Claims supported, with the test standard and report reference** | No superlative without a measurement behind it | Copy approval; specifier-grade downloads |
| **The claims we refuse to make** — the wording boundary | **Not modesty: these are claims that would be untrue or unsupported.** C-ATS is why — scattering is not diffusion, and saying otherwise loses a specifier's trust permanently | Written next to the product, so a writer cannot cross the line without seeing it |
| **Marketing status** — pre-release, demonstrable but undocumented, current, discontinued | Build it, then say it. This field alone would have caught three live errors | The Screen Wall (demonstrable since ISE 2023, no datasheet), the commercial range (not to be written up as shipping), REV-CP-12 (discontinued, still listed) |
| **Proof available, and whether it is publishable** | At this tier the best jobs are the least publishable — NDA'd documents, no photography | What may appear in a case study; prevents someone reaching for an encumbered asset |

## 6. Where it is sold

| Field | Why it is needed | How it is used |
|---|---|---|
| **Channel** — `srnd.store`, Cinema Store, or trade-only | No product exists in two places; shared SKUs are how channel confusion returns | Store split enforcement; the worklist |
| **Territory availability and any exclusivity** | The distributor roster is being pruned, and a vacated territory should be visibly open | Direct approach after an appointment ends |

## 7. The asset audit

*Each with a state — **exists / current / missing / not applicable** — because that is what turns "the manuals
are poor" into a completeness percentage per product.*

| Asset | Primarily for | Why it exists |
|---|---|---|
| Datasheet | Specifier, dealer evaluating | The first doubt-removal document anyone opens |
| Dimensioned drawings | Specifier, installer | Will it fit, and what does the builder need to leave |
| CAD | Specifier | *Publish-versus-gate decision outstanding* |
| BIM / Revit object | Architect | A product that drops into the model is a product that gets specified |
| NBS clause | Spec writer | Being present in the system specifiers write in |
| Install manual | Installer on site | The highest-intent reader we will ever have |
| Commissioning / calibration guide | Installer, integrator | Where a good product still becomes a bad room |
| Fault-finding guide | Installer, support | Most support volume, answered once |
| "How do you do X" video | Installer | The atom of the corpus — support, enablement and marketing at once |
| Training module | Certification | Assembled from the above, not authored separately |
| Spares and service instructions | Installer, support | Buying a part instead of replacing an assembly is a form of backing a dealer |

## 8. Record keeping

**Owner of the record · last reviewed · review interval.** A stale answer is worse than no answer because a
dealer acts on it, so a record with no review date is not complete.

## 9. Competitive — how it is defended *(domain 5)*

*The job the record currently does with one field. **A rep who cannot answer "why not theirs?" is not a rep**, and
this is where the durable hooks come from — a comparison the dealer has not thought of is the most reliable way to
start a conversation.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **The named alternatives, per product** | The dealer is not choosing between us and nothing; they are choosing between us and a specific thing, usually one they already buy | Comparison content, objection handling, the answer in the spec conversation |
| **The dimensions the comparison actually turns on** | Every category has two or three that decide it. Arguing the others is noise | Choosing what a comparison piece argues; what a data card leads with |
| **Where we genuinely win, dimension by dimension** | The defensible half. **With the measurement behind it or it is not a claim** | The comparison, the datasheet emphasis, the hook |
| **Where they genuinely win** | **The field that makes the rest believable.** A rep who concedes nothing is not trusted twice, and the dealer already knows the answer | Honest comparison; knowing which jobs not to chase; where to improve the product |
| **The switch argument** — what to say to a dealer who already buys the alternative | Different from a cold pitch: there is an incumbent relationship, a stocked shelf and a habit to overcome | Direct outreach after a territory opens; the conversation with a rival's dealer |
| **What to watch for in their specification** | Where a rival's product creates a problem the dealer will own later — stated as a caution, never as an attack | Specifier conversations; the honest technical answer |
| **Why deals are lost** — accumulating, one line each | The only outside view of the market we have | Ranks everything above; tells you what is actually wrong |

> **The discipline binds hardest here.** Position by capability, never disparagement; never attack a competitor in
> public copy; **no superlative without a measurement**; and never claim to be *the* most anything
> (`CLAUDE.md`). *Where they win* is not a concession bolted on for balance — it is what makes the rest of the
> comparison worth reading.

## 10. Commercial — the dealer's business case *(domain 6)*

*Absent from the record entirely, and it is half of why anything gets specified. **Not price.** Price is engine's,
is partner-gated, and is never published (`decided.md`, settled). This is the argument around it.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **Order unit and minimum** | The commonest cause of a wrong first order after scope of supply. Boxes, not panels; sheets, not metres | Quoting, the store listing, the first-order conversation |
| **Lead time, and what changes it** | The question that decides whether we are specified on a live project at all | Feasibility answers, the spec conversation, honest expectation setting |
| **Availability posture** — stocked, made to order, made to size | Different products want different promises, and one wrong assumption loses a job | What may be said about delivery; the store |
| **The dealer's business case** | Their margin position relative to the alternative, plus **what it costs them in labour** to install and to support. **A cheaper product that takes two more days on site is not cheaper** | The `more revenue` and `time saved` appeals; the comparison; partner conversations |
| **What not specifying it costs them** | The risk side of the same argument — the callback, the room that underperforms, the client who is unhappy | Objection handling; the honest version of urgency |
| **Where the numbers live** | Engine, per partner and per country. **The record points; it never copies** | Prevents a stale price in a marketing asset — the failure mode this boundary exists to stop |

## 11. Lifecycle & support — the way to install, and after *(domain 10)*

*Today the record holds the *documents* (`A1`–`A11`) and none of the *facts*. **A dealer on the way to install asks
about the facts.***

| Field | Why it is needed | How it is used |
|---|---|---|
| **What happens between order and site** | Lead time to delivery, what arrives, in what state, and what has to be ready | The order confirmation; the pre-install conversation |
| **The install sequence, and who does it** | Where it sits in the build order, and whether it needs a specialist. **Fabric Walls' whole proposition is the answer to this** — no upholsterers, predictable times | Install manual structure; the `easier to do` appeal; the programme conversation |
| **Commissioning and verification** | Where a good product still becomes a bad room. The step that decides whether it worked | Commissioning guide; the verification service; the G5 signal |
| **Serviceability** — what can be replaced without pulling the assembly | **Buying a part instead of replacing an assembly is a form of backing a dealer**, and it is a purchasing argument as much as a support one | Spares listing; the service-replacement rule; the support proposition |
| **What we support and for how long** | The claim behind "support is part of the sales proposition, not a cost behind it" | The partner conversation; the international dealer's real question |

## 12. Narrative & hook material *(domain 11)*

*The missing source under the hook machinery. `group/09-motion-design.md` designs hooks by **appeal category**, and
**many hooks per door is deliberate** — volume is part of the G1 design (`decided.md` S23). **But volume needs a
source, or hooks get invented per campaign**, which is precisely what the production line forbids.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **Which of the five appeals this product can honestly carry**, and the substance behind each — *more revenue · time saved · easier to do · better results · the problem named* | **Not every product carries every appeal**, and stretching one it cannot carry is how a hook becomes a claim we cannot defend. Marking which are *empty* is as useful as filling the others | The hook matrix per door (`backlog.md` JNY-4); deciding which products lead a campaign |
| **The single most interesting true thing about it** | Every product has one, and it is usually not what the datasheet leads with. C-ATS's ~300 mm tolerance sat unused for years | The lead hook; the explainer's opening; what a piece is *about* |
| **What has actually bitten** — hooks issued, and which caught | The loop that turns hook volume from guesswork into evidence, and the reason source-tagging exists (S23) | Ranks the next batch; retires hooks that never bite |

> **This section holds material, never wording.** The hook matrix and the wording stay where they are designed —
> per door, set by an owner, never generic (`backlog.md` JNY-4). **The record says what a product can honestly be
> hooked on; the matrix says what is said and where.** Keeping those apart is what stops the record becoming
> marketing copy.

## How to use it

1. **Hold it up against Engine first.** Establish what already exists mechanically, then work only on the layer
   above. **The gap between the two is the deliverable** — a list of fields the estate needs and the operational
   record does not hold.
2. **C-ATS is done — `brands/c-ats/product-records.md`.** The worked example, and it found six things without any
   new research: the REF-CP bond-versus-screw trap (the recommended install deliberately absorbs *less*, so an
   installer who skips the adhesive gets acoustics the design didn't assume), the REV-CP cold-adhesive failure, a
   corner-factor double-count warning living in a code comment, a "faceted ABS diffuser" wording violation in our
   own legacy source, the marine panel having no acoustic data of its own, and a ~300 mm layout tolerance that is a
   real selling point appearing in no marketing.
3. **Then DT, by mechanism rather than by SKU.** The range is variant-heavy; document the mechanism once and table
   the variants. **The grouping is now proposed and skeletoned** — `brands/display-technologies/product-records.md`
   collapses 52 catalogue lines into twelve record scopes and fills the definitional layer, leaving the rest as
   named gaps. It needs an hour of the owner's knowledge to confirm the families.
4. **Rank by the questions-generated field**, cross-checked against the archive's question frequency. Not
   alphabetically, and not by whichever product someone is currently annoyed about.
5. **Make completeness a gate on new products.** The only version of this that stops the debt returning.

**And the order the model changes, which supersedes points 2–4 as the *sequence* while leaving them true as the
*standard*:**

6. **Stand up the routes before filling any more fields.** Six capture events, five of them attached to work that
   already happens. **A route that is running fills its domains forever; a field filled by a push decays from the
   day it is written.** The cheapest two are the ones that fire daily — the support answer and the spec
   conversation. **RT5 is not a gap** — engine's pipeline already holds win/loss; what is worth checking is whether
   the loss reason is structured enough for domain 5 to read.
7. **Fill the front half first, against the model, one brand at a time.** Domains 5, 6 and 11 — defend, the
   business case, and what a product can honestly be hooked on — because that is where the journey is entered and
   where the record has almost no fields today. The back half is better covered and less urgent than it looks.
8. **Judge the record by the rep test, not by the meter.** A record at 90 % that cannot win a comparison or say
   what a job costs the dealer in labour is not 90 % of a rep. **The four jobs are the pass mark.**
