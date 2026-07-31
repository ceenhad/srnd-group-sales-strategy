# The product data schema — what must exist per product

*Why this file exists: **capturing what needs to be documented has to come before what is and will be
documented.** Without a definition of the required set, "the manuals are poor" is an opinion rather than a
measurable gap, and no amount of writing converges. This is a reference artefact, not an argument — a field list
to audit against. A first cut, for correction.*

**What it buys, and it is more than tidiness:**

- **It makes the work finite and delegable.** A missing field is a task with an owner. "Improve the
  documentation" is neither.
- **It turns a vague deficit into a completeness percentage per product**, so progress is visible and
  prioritisation is possible — highest-selling and highest-support-load products first.
- **It enforces consistency across a range**, which is most of what makes a catalogue feel professional.
- **It becomes a gate on new products.** A product does not ship until its record is complete. That fixes the
  problem at source instead of perpetually catching up — and the Screen Wall, demonstrable since ISE 2023 with no
  page and no datasheet, is what its absence looks like.
- **One record feeds everything.** Datasheet, brand-site page, store listing, manual, training module, specifier
  download and the design tools all draw on the same fields. Written once, used everywhere — which is the
  compounding argument applied to data rather than content (`group/08-sales-motion.md`).
- **And it is plausibly the fragmentation fix the strategy has been waiting on.** Whole-room ease and cross-sell
  are both recorded as blocked on "unfragmenting the data" (`open-items.md` item 4). What that actually means is
  that there is no canonical product record. This is that record.

## Before writing any of this: check Engine

**Much of this is likely already under consideration in SRND Engine, and some may be implemented.** So the first
move is not to fill this in — it is to find out what Engine already models, and then reconcile. **Two competing
product schemas would be worse than none**, and this repo has already made the equivalent mistake once by basing
a position on a superseded ADR.

The division of labour that keeps this useful rather than duplicative:

- **Engine is the system of record.** The data model, the storage, the identifiers, the workflow. Not this repo's
  business, and not to be specified here.
- **This file is the requirements view — the demand side.** What the sales, marketing and support estate *needs*
  to exist per product, who consumes each field, and what it is for. That is the part an operational data model
  would not necessarily capture, because it is about downstream use rather than storage.
- **Where Engine already models a field, this file defers to it** and records the mapping. Where the estate needs
  something Engine does not hold, that is the actual finding — and it is a much more useful output than a schema
  written from scratch.

*Read the field groups below as a checklist to hold up against Engine, not as a specification to implement.*

---

## 1. Identity

Product code · name · brand · status (current / pre-release / discontinued) · variants and **what varies between
them** · the mechanism or platform it belongs to (so documentation can be written per mechanism, not per SKU) ·
supersedes / superseded by.

## 2. The problem it solves — the on-ramp fields

Per `decided.md` S15, and **fields rather than freeform copy**, which is what makes the marketing layer writable
instead of improvised each time:

- The problem it solves, in the dealer's words.
- The opportunity it opens.
- The time or labour it saves.
- Who it is for, and where it is used.
- What it replaces or avoids.

## 3. Commercial

Channel (`srnd.store` / Cinema Store / trade-only — per `decided.md` C5) · price band · MOQ · lead time · country
of manufacture · spares and service parts list · what is field-replaceable · warranty terms.

## 4. Physical

Dimensions and weight, per variant · finishes and options · tolerances · **required clearances and service
access** · fixing and load requirements · shipping dimensions and packaging · what the installer must provide.

## 5. Performance

Measured data with **the test standard and report reference** · conditions of measurement · and a field that
looks unusual but is a discipline: **claims deliberately not made.** C-ATS is why — scattering is not diffusion,
and recording the boundary in the product record stops it being crossed by someone writing copy later.

## 6. Integration

Power · data and control protocol · network requirements · diagnostics available and what they report ·
**what it has to meet** — the adjacent products, structures and surfaces from our own range and from others ·
known incompatibilities.

## 7. The documentation set

Each item with a state: **exists / current / missing / not applicable.** This is the audit.

| Asset | Audience |
|---|---|
| Datasheet | Specifier, dealer evaluating |
| Dimensioned drawings | Specifier, installer |
| CAD | Specifier — *note the publish-versus-gate decision, `group/06-competitors.md`* |
| BIM / Revit object | Architect |
| NBS clause | Spec writer |
| Install manual | Installer on site |
| Commissioning / calibration guide | Installer, integrator |
| Fault-finding guide | Installer, support |
| "How do you do X" video(s) | Installer — the atom of the corpus (`decided.md` S14) |
| Training module | Certification |
| Spares and service instructions | Installer, support |

## 8. Support

Common faults and their answers · known issues and workarounds · the RMA route · which published answers cover
this product · **support-load note**: what this product actually generates calls about. That last field is how
the schema tells you what to document next.

## 9. Record keeping

Owner of the record · last reviewed · review interval. The maintenance obligation made concrete
(`group/08-sales-motion.md`) — a stale answer is worse than none, so a record with no review date is not
complete.

---

## How to use it

1. **Fill it for C-ATS first.** Three SKUs, the data largely exists, and Neil wants the standard higher than it
   currently is — so C-ATS is where "good" gets defined against a real example rather than in the abstract.
2. **Then DT, by mechanism rather than by SKU.** The range is variant-heavy; document the mechanism once and table
   the variants (`decided.md` S11a).
3. **Rank by support load and sales volume**, using field 8 and the archive's question frequency. Do not attempt
   the range alphabetically.
4. **Make completeness a gate on new products**, which is the only version of this that stops the debt returning.
