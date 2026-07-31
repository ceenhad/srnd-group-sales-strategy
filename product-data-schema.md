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

*A first cut, for correction. Every row is a claim about how the estate works, so a wrong row is worth striking.*

---

## 1. Why to buy it — the on-ramp

*The layer that turns a record into a reason to look. Nothing operational needs these, which is exactly why they
are missing.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **The problem it solves, in the dealer's words** | A product on its own does nothing; the problem is what engages. And the dealer's phrasing — not ours — is what gets searched | Hook copy, page opener, campaign silo, search terms, the words AI answers match against |
| **The time or labour it saves** | One of the four things a dealer actually cares about, and the most under-used | Comparison arguments; the format that already works for us — the Fabric Walls factory-versus-site film is the brand's best performer |
| **The opportunity it opens** | Dealers often don't know *why* to specify something; a product that wins a job is worth more than one that fits a job | Sales enablement, cross-sell prompts in the spec conversation |
| **What it replaces or avoids** | The dealer is choosing between options, including doing nothing | Comparison content, objection handling |
| **Is this an entry product or a flagship?** | Every brand needs a door-opener distinct from its showpiece; the flagship demonstrates depth, the entry product opens the relationship | Targeting the on-ramp; deciding what gets promoted to cold audiences |

## 2. The doubt it has to remove

*The single most valuable group here, and the one no operational system would ever contain. **De-risking is the
conversion mechanism** at this level — a dealer specifying a product puts their own reputation on someone else's
box.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **The specific doubt or objection this product meets** | Different products fail to sell for different reasons — will it fit, will it be quiet enough, will it look right, can I install it | Decides *which technical asset is load-bearing* for this product, rather than documenting everything equally |
| **The questions it actually generates** — pre-sale and on site | This is the content backlog, per product, and the two are the same question at different times | Ranks the corpus; tells you what to write next; measures support load |
| **What goes wrong on site with it** | The installer's real fear, and the thing peer reputation is made of | Fault-finding guide, "how do you do X" video, install-manual priorities |

## 3. Who decides on it

*Engine knows who bought it. It does not know who specified it, and those are different people.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **Purchaser vs specifier** — integrator, AV consultant, architect, interior designer, end client | Being named pre-tender is worth more than winning a spec conversation later, and the machinery differs entirely | Decides whether this product needs NBS clauses, Revit objects and finish samples, or only an install guide |
| **Where it sits in the room, and what it must physically meet** | Cross-sell is only credible where the adjacency is physically true — the treatment goes behind the fabric, the speakers sit in the front-of-room structure | The adjacency map; whole-room content; the cross-sell prompt at the moment the room is decided |

## 4. What we may and may not say

*Governance, and it belongs in the record rather than in someone's memory.*

| Field | Why it is needed | How it is used |
|---|---|---|
| **Claims supported, with the test standard and report reference** | No superlative without a measurement behind it | Copy approval; specifier-grade downloads |
| **Claims deliberately not made** | C-ATS is why: scattering is not diffusion, and the line is a credibility boundary with specifiers | Stops a writer crossing it later without knowing it exists |
| **Marketing status** — pre-release, demonstrable but undocumented, current, discontinued | Build it, then say it. This field alone would have caught three live errors | The Screen Wall (demonstrable since ISE 2023, no datasheet), the commercial range (not to be written up as shipping), REV-CP-12 (discontinued, still listed) |
| **Proof available, and whether it is publishable** | At this tier the best jobs are the least publishable — NDA'd documents, no photography | What may appear in a case study; prevents someone reaching for an encumbered asset |

## 5. Where it is sold

| Field | Why it is needed | How it is used |
|---|---|---|
| **Channel** — `srnd.store`, Cinema Store, or trade-only | No product exists in two places; shared SKUs are how channel confusion returns | Store split enforcement; the worklist |
| **Territory availability and any exclusivity** | The distributor roster is being pruned, and a vacated territory should be visibly open | Direct approach after an appointment ends |

## 6. The asset audit

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

## 7. Record keeping

**Owner of the record · last reviewed · review interval.** A stale answer is worse than no answer because a
dealer acts on it, so a record with no review date is not complete.

---

## How to use it

1. **Hold it up against Engine first.** Establish what already exists mechanically, then work only on the layer
   above. **The gap between the two is the deliverable** — a list of fields the estate needs and the operational
   record does not hold.
2. **Then fill it for C-ATS.** Three SKUs, the data largely exists, and the standard is wanted higher than it is —
   so "good" gets defined against a real example rather than in the abstract.
3. **Then DT, by mechanism rather than by SKU.** The range is variant-heavy; document the mechanism once and table
   the variants.
4. **Rank by the questions-generated field**, cross-checked against the archive's question frequency. Not
   alphabetically, and not by whichever product someone is currently annoyed about.
5. **Make completeness a gate on new products.** The only version of this that stops the debt returning.
