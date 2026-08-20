# The site is an output of this repo — and it has moved ahead of the record's notes about itself

*Written 2026-08-20 after Neil: ***"the website you just analysed has been auto generated based on answers in this
repo, so there is the proof of that part of the method."*** **Correcting `2026-08-20-the-system-page-checked.md`,
which audited one page of five and read the site as hand-written copy.**

**Five pages exist** — `/`, `/the-system/`, `/products/`, `/technical-information/`, `/start-your-project/` — *all
fetched as raw HTML and read.* **The technical page is the one that matters and I had not read it.**

---

## 1 · What the generation shows — and the provenance is mixed, so the claim is narrower than I first wrote

> **⚠ Corrected twice on 2026-08-20, and the second correction is that nobody here knows how the site was made.**
>
> *My first version said **"rows in this repo became a published site without anyone writing page copy"** and called
> it *"the strongest evidence in the repo"* for the method. **That was a causal claim built on one sentence.***
>
> **Then two things from Neil, in order.** *(1) **"I'm sure that our other sites were used as reference also"** —
> which is **a surmise, not an observation**, and this repo's own source discipline requires it to be recorded as
> one. (2) **"That site was only shown to me a couple of hours ago. It appeared almost like magic."***
>
> **So the owner does not know its provenance either.** *Which means the honest state is **`unknown`**, not *"this
> repo"* and not *"the old sites"*. **Neither of Neil's statements is evidence of origin** — the first is his
> inference, the second is explicitly that he was handed it. *The one hard indicator is the host:
> `cats-98x.pages.dev` is a Cloudflare Pages deployment, and the dev team monitor this repo — **consistent with
> generation from here, and consistent with several other explanations.*** **`SIT-8` is therefore not a tidy-up: it
> is the difference between a proven method and a coincidence.**

**What can be said, and it is worth having.** *Content in this repo and content on the generated site **agree** —
the 210 m³ chamber is in `brands/c-ats/copy.md` and `product-records.md`; the A/B install story is `Q46`; the corner
double-count warning is a caveat the record said *"lives in a JSON comment today and belongs in the published data
note"*, and it is now in a published data note.* **Agreement is not attribution.** *Any of those could have come
from the record, from `c-ats.co.uk`, or from both — **and the technical page states that the data files are "served
from the current site"**, which makes the existing site a live source rather than a historical one.*

**One observation that does survive independently of provenance.** *`copy.md`'s depth block reads **"shallower than
anything comparable"** — the unbounded superlative `Q63`/`C5.20` bounded — **and no page says it.** The site says
*"nothing deeper than 50 mm"* plus *"43 mm for the Resonance Control Panel"*. **Wherever the wording came from, the
published version is the disciplined one and `copy.md` is not** (`SIT-4`).*

**`SIT-8`: establish the actual provenance before this file is cited for anything.** *One comparison against
`c-ats.co.uk` would separate *"the record generated it"* from *"the old site supplied it"* — **and the two have
different consequences for every conclusion below.***

**And the generation is more disciplined than its own source in one place.** *`copy.md`'s depth block still reads
**"shallower than anything comparable"** — the unbounded superlative `Q63`/`C5.20` bounded. **The site does not say
it.** The home page says *"nothing deeper than 50 mm"* and the stat block gives *"43 mm for the Resonance Control
Panel"* — bounded, factual, and current to Neil's 2026-08-19 correction.* **So the pipeline is reading the corrected
claims, not the older copy file.** *`copy.md` is now the stale artefact and should be marked as superseded rather
than left as though it were the source (`SIT-4`).*

## 2 · Withdrawn: the "defect" was me reading the wrong page

**I wrote that the test-basis block *"omits the mounting condition"* and called it the one real defect. It does
not.** *`/technical-information/`, in its own words:*

> ***"Three materials were tested in eight configurations in a 210 m³ reverberation chamber, to BS EN ISO 354:2003,
> in July 2019. The figures are design stage reference values measured with panels free and unfixed, which is a
> laboratory mounting rather than a finished install. Where a configuration matters to the result, it is stated with
> the figure."***

**That is the record's caveat, verbatim in substance, sitting next to the data where it belongs** — *not on the
marketing page, which is the correct editorial choice.* **`SIT-1` withdrawn.**

**And the page goes further than the record does**, on three counts:

- **The A/B install types are explained, not just plotted.** *"A panel bonded with adhesive is damped by the bond: it
  absorbs less and behaves as a clean scatterer, which is the condition a design assumes. A panel fixed with screws
  alone is free to resonate, which adds absorption the design did not allow for. **Bonded is the default in the
  modelling tools for that reason.**"* — `Q46`, published.
- **The corner double-count warning is public.** *"Those values already include the effect of corner loading, so a
  design tool must not apply a corner factor again."*
- **The absence of low-frequency data is stated honestly.** *"No claim is made below 125 Hz, because the report does
  not extend there."*

**New provenance the record does not hold:** *the report number — **BSRIA Report 100241/1** — plus **test 6** as the
Type B source, **July 2019**, and *"three materials in eight configurations"*.* **`SIT-5`: fold these into
`product-records.md` § Provenance.**

## 3 · The finding that matters most: I drafted answers that were already published

**`/technical-information/` carries a *"Questions these panels raise"* section that answers, in public, today:**

| `N3` question | State in the record | On the site |
|---|---|---|
| 1 · Bond or screw? | `answered` — *"written, unpublished"* | **Published**, with the reason and the site-level warning |
| 2 · How far off the designed position? | `known` — *"never published; the brand's best unused `O2`"* | **Published**, *"roughly 300 mm"*, **including the resonance exception** |
| 3 · Behind fabric? | `known` — *"never stated as an answer"* | **Published**, with the Fabric Walls non-dependency |
| 4 · Why do the figures look low? | `known` — *"queued as content, blocked on `DOC-4`"* | **Published**, and it needed no coefficient |
| 5 · How many panels? | `known` — *"the gap is publication, not knowledge"* | **Published** as *"that is what the design service answers"*, with the 1.44 m² box quantum |
| — · Data below 125 Hz? | A known gap | **Published as a stated absence** |

> **So `KNW-1` — which I drafted yesterday as *"the single highest-return work available in the brand"* — was
> already live.** *`draft-answers.md` is a re-derivation of published material. **The record's own status column was
> the thing out of date**, not the brand.*

**And it breaks the premise under the `T5` training draft.** *That piece rests on the record calling the ±300 mm
tolerance **"a genuine selling point that is nowhere in the marketing."*** **It is in the marketing, with its
exception, on the technical page.** *The subject survives as a class; the *"nobody says this"* framing does not.*

**This is `PR-1`'s pattern a sixth time.** *The material was not missing and not in the platform either — **it was
published**.* **↻ And the twist I claimed is withdrawn:** *I wrote *"in this brand's own output, **generated from
this repo**"*. **Provenance unknown** (see §1) — *and if the existing `c-ats.co.uk` supplied this content, then these
answers were **already public before this repo drafted them**, which makes the record's error older and larger, not
smaller.* **The finding does not depend on which it is: the answers are published and the record says they are
not.***

## 4 · Corrected: verification and isolation are both offered

**`P7` said verification is *"a capability that was never made an offer."* Wrong.** *`/products/` § Beyond the
panels: **"Acoustic verification — measurement of how the finished room behaves: reflection behaviour, decay
uniformity and spatial consistency, so the design's targets can be shown to have been met."*** *And
`/start-your-project/` lists scope as **"isolation, treatment, verification, or the full sequence."*** **So it is an
offer on two pages.** *What it lacks is a **price** and a place in a service ladder — a smaller and different claim.
`P7` is corrected to that.*

**And `/the-system/` under-selling isolation was a one-page reading.** *The intake page offers **isolation** as a
scope option outright, and `copy.md` says it plainly — *"two different problems, both acoustic, **both ours**."*
**But `/products/` calls isolation *"a separate discipline… specified separately from treatment"* and never says it
is ours.*** **So the real finding is an inconsistency across pages, not an absence** — *the intake sells it, the
product pages describe it as somebody else's field.* **That is `SIT-6`, and it is `P2` again: the isolation layer has
no plan, so the generator has nothing consistent to say about it.**

## 5 · What still stands from the original audit

- **`DR-Q52` is being answered by publication** *(§2 of the earlier file)* — **and more strongly than I wrote**,
  because the technical page publishes the corner-loading rule and the install-type effects too. *Both are on the
  DR's own **proposed publishable** side; nothing from **proposed not** appears on any of the five pages.*
- **The two unbuilt promises stand** *(§3)* — *"start from a designed reference room"* appears on **both** `/` and
  `/the-system/`, and `EST-7` still has no finish schedule and one worked room. **A dealer at step 01 finds nothing
  to start from.**
- **The unsourced category claim stands** *(§6)* — *"100 mm to 200 mm or more on every treated wall"*, `SIT-3`.
- **The checkerboard question narrows** *(§4)*. *Only `/the-system/` assigns a checkerboard to the **Reflection**
  panel; `/` and `/technical-information/` do not mention one, and the record assigns it to **Reverberation**.
  **Still worth resolving, now as one page against the record rather than the site against the record.***
- **`DAT-1` narrows** — *the site states 43 mm correctly on two pages.*

## 6 · The standing consequence, and it changes how this repo works

**The site is downstream of this repo, so the repo's notes about what is published are now describing its own
output.** *Every *"never stated"*, *"nowhere in the marketing"*, *"unpublished"* and *"the gap is publication"* in
`product-records.md`, `claims.md` and `content-plan.md` **was written against the old Shopify site and may already be
false.***

> **The rule this earns: before recording that something is unpublished, check the generated site.** *It is one
> fetch. **Not doing it cost a training draft's premise, a set of answers re-derived from live material, and a
> defect report against a caveat that was already there.***

**And one thing to fix in this repo's own reading of itself:** *`PR-18` records the site as *"an in-play mockup"*.
**It is a generated output of the current record.** A note calling it a mockup is now the most misleading line in
the premises register (`SIT-7`).*

## Sources

- `https://cats-98x.pages.dev/` · `/the-system/` · `/products/` · `/technical-information/` · `/start-your-project/`
  — all fetched as raw HTML, 2026-08-20
- `2026-08-20-the-system-page-checked.md` — the audit this corrects
- Neil, 2026-08-20 — that the site is auto-generated from this repo
