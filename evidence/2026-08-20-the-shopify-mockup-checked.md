# The Shopify mockup checked — `c-ats.myshopify.com`, 2026-08-20

*Supplied by Neil: **"this is the mockup I was working on."*** *Fetched and read; the articles quoted below were
**read**, not inferred from their titles.*

> **First, a correction I owe. There are two sites and I conflated them.**
>
> | | What it is |
> |---|---|
> | **`c-ats.myshopify.com`** | **Neil's mockup — this file.** *`PR-18`'s *"in-play mockup pending this process being complete"* **is accurate about this site**, and `copy.md`'s *"What to fix while pasting this in"* list is written against it* |
> | **`cats-98x.pages.dev`** | *A different thing — an Astro/Cloudflare Pages build Neil was **shown two hours ago**: **"it appeared almost like magic."** **Provenance unknown** (`SIT-8`)* |
>
> **So my claim that *"`PR-18`'s note is the stale thing"* is withdrawn.** *`PR-18` was describing this site, and the
> description holds.* **I audited one site and corrected a premise about another.**

---

## 1 · The finding that matters: a live guardrail breach

**The brand's hardest naming rule is broken on a published page.** *`claims.md` `C5.15` and the product record:
**scattering, never diffusion** — *"diffusion has a specific meaning under ISO 17497 that this does not claim."* The
record even caught the legacy brochure calling the REF-CP a *"faceted ABS diffuser"* and said **"the record is where
that gets fixed once rather than caught repeatedly."***

**`/blogs/acoustic-treatment/absorbers-diffusers-bass-control-explained` (7 June 2026):**

- **Title:** *"Absorbers, **diffusers** and bass control: what each does"*
- **A section headed "Diffusers"**, and the product is named inside it: *"The C-ATS Reflection Control Panel is tuned
  to control and scatter early reflections rather than simply absorb them."*
- **The comparison table files the product under the word:** *"**Diffuser** / reflection control — solves: imaging,
  early reflections."*
- **The FAQ pairs them again:** *"Do I need diffusers or absorbers? … absorbers control decay; diffusers/reflection
  control preserve…"*

> **The sentence about our panel is careful — it says *scatter*.** *But the panel sits under a **Diffusers** heading
> and in a **Diffuser** table row, which is exactly the attachment the rule exists to prevent: **the word ends up on
> the product**, and under ISO 17497 it is a claim we cannot support.* **`SIT-9` — and it is the most concrete thing
> found today.**

*The rest of the article is good and worth keeping — the three-tool explainer is category education of the kind
`Q64` permits, and *"over-absorb and a room sounds lifeless"* is the over-damping guard stated plainly.*

## 2 · `copy.md`'s fix list has not been applied

*`copy.md` § "What to fix while pasting this in" says: **"Replace the placeholder hero. *'This signature bestseller
exceeds all expectations'* is theme demo text and is precisely what the brand rules forbid."***

**It is still live**, verbatim: *"Our signature product — made with care and unconditionally loved by our customers,
this signature bestseller exceeds all expectations."* **So `copy.md` is not just stale as a source (`SIT-4`); its
action list is unexecuted** *(`EST-4` was framed as "quick fixes"; this is the quickest and it is undone)*.

## 3 · What the mockup shows that the repo's plan says is missing

| On the mockup | What this repo says |
|---|---|
| **`C-ATS-ISO-SYS` Isolation System** and **`C-ATS-VER-ISO` Isolation Verification**, as products | **`Q79` confirmed isolation is C-ATS's and `P2` says it has no plan.** *It has a listing* |
| **`C-ATS-VER-A` Acoustic Verification**, as a product | **`P7` says verification is "a capability, never made an offer."** *Withdrawn — it is listed as a service on the brand's own store* |
| **A "Room Selector"** in the nav (`/pages/acoustic-selector`) | **`EST-7` — the reference-room layouts — is half built.** *The route to it already exists* |
| **A Knowledge Base of 8 categories and 18 articles** | **`N3`: "two of thirteen are written down."** *See below* |

## 4 · The knowledge base — and `N3` is wrong again

**18 published articles.** *At least five answer questions the record marks unpublished or blocked:*

| Article | `N3` question | The record says |
|---|---|---|
| `panel-mounting-bonded-vs-screw-fixed` | **q1 — bond or screw?** | *`answered`, but **"written, unpublished"** (`DOC-1`)* |
| `how-to-conceal-acoustic-treatment` | **q3 — can it go behind fabric?** | *`known`, **"never stated as an answer"*** |
| `how-to-read-absorption-coefficient-table` | **q4 — why do the figures look low?** | *`known`, **"queued as content, blocked on `DOC-4`"*** |
| `acoustic-panel-fire-ratings-explained` + `superyacht-marine-cinema-acoustics-imo-solas` | **q12 — is it fire rated?** | *`known, partly`; **`T1` is "blocked on one fetch"** and called the strongest training row* |
| `c-ats-absorption-data-bsria-iso-354` | *the test-basis question* | ***`SIT-1` was already withdrawn earlier today** once the caveat was found published on the technical page. **A second published article on the same subject exists here** — so that item was wrong twice over* |

*Also published and unaccounted for: `slim-vs-deep-acoustic-treatment-cost-of-space` (the depth argument),
`does-room-correction-replace-acoustic-treatment` (an objection), `common-acoustic-specification-mistakes`
(specifier-facing), `first-reflection-points-home-cinema`, `what-is-rt60-target-cinema-listening-room`,
`structure-borne-vs-airborne-sound`, `soundproofing-vs-acoustic-treatment`.*

> **This is the third time today, and it is now a pattern with a name.** *`PR-24` said the repo's notes about what is
> published are unreliable. **The check is one fetch and nobody was doing it.*** **An article existing does not mean
> the answer is right** — §1 is the proof of that — *but it does mean **"unpublished" was never the state**.*

## 5 · Two things to look at, stated without inflating them

- **Every product and service shows £0.00**, and **the store answered an unauthenticated request** — I fetched it
  with no login. *`PR-18` already established that its prices are placeholder, and `Q45`'s £6,000–£12,000 came from
  this feed. **£0.00 is not a price**, so the never-publish-pricing rule is not breached — but a publicly readable
  store showing £0.00 on a design service is worth a decision rather than a shrug.* **`SIT-10`.**
- **`C-ATS-REF-CP-MAR` — Marine Reflection Control Panel — is listed**, while `copy.md`'s own rule check claims
  *"marine absent"* and **`DOC-8` has marine's absorption-sheet provenance open** *(same BSRIA report, or a separate
  test?)*. **A listed product with unresolved test provenance.** *`SIT-11`.*
- *Correct, and worth recording: **`REV-CP-12` is absent** — the discontinued product is not listed.*

## What to do

1. **`SIT-9` — the diffusion breach.** *Retitle and re-file the article so the word never attaches to the product.
   **This is the only item here that is a rule violation rather than an untidiness.***
2. **`SIT-12` — read the 18 articles against `N3` and `claims.md` properly.** *Five mapped from titles above;
   **titles are a summary.** The real question is whether each published answer is **right**, and §1 says at least
   one is not.*
3. **Apply `copy.md`'s fix list** (§2) — *starting with the theme demo text.*
4. **Correct the register**: *`P7` withdrawn, `N3` restated, `DOC-1`/`DOC-4`/`T1`'s "blocked" states re-checked
   against what is already live.*
