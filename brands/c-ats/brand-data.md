# C-ATS — brand data (captured)

Raw input, not settled positioning. **Sources:** the live site (`c-ats.co.uk`), **the C-ATS
storefront repo `ceenhad/c-ats-shopify`** (the staged B2B site + content — read properly this time),
the store, and the group site. Captured 2026-07-24. C-ATS is the origin of the whole plan; its
strategy instance already lives in this folder (`positioning.md`, `content.md`, etc.) and the
authoritative brand truth is `c-ats-shopify:CLAUDE.md`. Engineering differentiator: `measured-acoustics.md`.

## The key finding: the telling is largely BUILT, just not shipped

Unlike the other brands (where the external presence barely exists), **C-ATS already has a full B2B
storefront + a deep knowledge base + a rigorous content strategy — all staged in `c-ats-shopify` on
an unpublished dev theme, not yet public.** The live `c-ats.co.uk` is a **holding page**; the real
site is built and waiting. So the divergence here is **"built but not deployed,"** not "doesn't
exist." (Deploy has been blocked on a Shopify CLI re-auth, plus a pending configurator swap.)

> **Provenance — built ad-hoc, no plan.** The C-ATS site + content was built by Neil personally over
> the past year, with **no plan followed beyond "have more than nothing."** So it's *content-rich in
> volume*, but not the product of a strategy — treat it as a **placeholder / first attempt to
> re-base on the agreed plan**, not as settled intent to preserve. The strong content strategy doc is
> the closest thing to a plan and is worth building on; the deployed shape of the site is not.

## The live public front (`c-ats.co.uk`)

Holding page: the Three Rs, the four Control Panels (Reflection / Reflection Marine / Resonance /
Reverberation 50 mm), Technical Information, Contact; ~50 mm depth story; **no social links.**

## The staged storefront (`c-ats-shopify`, not public yet)

- **B2B Shopify Plus** store (`c-ats.myshopify.com`); dev theme (Horizon-based) with custom
  `cats-*` sections. Pages + articles deploy via Admin API; theme via CLI.
- **"The System" page** — the C-ATS journey: **Select → Design → Verify.**
- **Knowledge Base: 18 articles** across **8 GEO/AEO pillars**:
  A room-acoustics fundamentals · B acoustic treatment (products & how) · C measurement & analysis ·
  D design & specification · E marine & compliance · F isolation · G materials & construction ·
  H verification. (Titles incl. RT60, first reflections, panel thickness, slim-vs-deep, absorbers vs
  diffusers vs bass, checkerboard placement, reading an absorption table, BS EN ISO 354 / BSRIA
  results, fire ratings, mounting, spec mistakes, concealment, verification.)

## Content strategy (`content/content-strategy.md`) — genuinely strong

- **GEO/AEO-first:** the goal is to be the source **AI engines cite** for home-cinema acoustics;
  metric = **Share of Model** (how often C-ATS is named in AI answers), not raw traffic. Audience:
  CI installers / CEDIA first.
- **The citation moat is first-party, data-backed content rivals lack:** BSRIA **BS EN ISO 354**
  absorption data (real measured coefficients); the proprietary method (the Three Rs, per-axis
  Fitzroy balance, checkerboard placement, comb-filtering protection); the **50 mm vs 100–200 mm**
  space-value argument; real projects with measured results.
- Discipline: answer-first TL;DR, comparison tables, verifiable cited numbers, E-E-A-T (named
  author/dates), FAQ/Article schema, `llms.txt`, refresh cadence, Bing submission.
- **Cross-brand:** the "concealment" article routes to **Fabric Walls** (acoustics behind the fabric).

## Key decisions on the site (from the repo)

- **The free configurator / Room Selector is being removed** — it "cheapens the paid design
  services." Replacement = **pre-planned reference layouts**: a showcase of three designed 7.1.4
  example rooms (5×4×2.7 / 7×5×3 / 10×7×3.5) that drives to the **paid design service** (no
  self-serve quantities). Built locally, **not deployed** (blocked on CLI re-auth).
- **The acoustic engine is OFF the site** (no runtime wiring to the separate cinema-platform engine).
- **Pricing is £0.00 / deferred to last, on purpose** (consistent with the group's fully-gated policy).

## Live-site vs brand-truth tensions (flag — brand truth wins)

- ~~**"Complete Acoustic Treatment System"** used as canonical, but brand truth flags the "Complete" expansion
  as unresolved.~~ **NOT A TENSION — `Q26`/`Q65`: the expansion is permitted, C-ATS is the standard form, the
  legal name is for contracts.** *One of the five "live breaches" was never a breach; the rule was what was
  wrong (`Q26`).*
- **"maximum performance" / "unique"** — the unbacked superlatives brand truth says to avoid.
- The `about.html` "recommended retail price" line contradicts the gated-pricing policy.

## Note

C-ATS has the **most content by volume** by far (though built ad-hoc, not to a plan — see
Provenance). So the coherence job here is mostly **re-base + reconcile + deploy + connect to the
group story**, rather than create from nothing — the opposite of the thin brands.


---

# The two sites, compared — captured 2026-07-31

*Both read directly: `www.c-ats.co.uk` (WordPress, © 2024) and `c-ats.myshopify.com` (Shopify, © 2026, generated
rather than authored). Between them they are the two halves of the on-ramp → depth → contact structure
(S15, `../../motion/sales-motion.md`), and **neither is whole.**

## The old site: depth without an on-ramp

**What is genuinely strong, and better than the repo credited:**

- **The full BSRIA report is published as a public PDF**, alongside **five per-panel absorption coefficient
  sheets** (REF-CP, RES-CP, REF-CP-MAR, REV-CP-50, and a RES-CP boundary-condition sheet). Freely downloadable,
  no gate. That is **specifier-grade proof, openly available** — more than most competitors offer, and it sits
  quietly on a page called "Technical Information" doing nothing for the brand.
- The **3 Rs leads the homepage**, the **50 mm depth** is stated, and the line *"a comprehensive and repeatable
  solution that remains easy to install"* is close to the positioning we settled on independently.

**What is wrong with it:**

- **No services at all.** Design, verification, isolation and isolation verification are absent — so the revenue
  that matters most is invisible.
- **"unique"** and **"maximum performance"** — the unbacked superlatives the brand rules forbid.
- ~~**"Complete Acoustic Treatment System"** as the canonical name throughout.~~ **Permitted — `Q26`/`Q65`.** *C-ATS is the standard form, so "throughout" is the only part to change.*
- **The marine panel at equal prominence** with the three core panels, in the nav and in the downloads.
- No reason to look, no contact route beyond a form, nothing about time saved or problems solved.

**Correction to an open item:** a **marine absorption coefficient sheet is published**, so the note in
`panels.json` that the marine panel has "no absorption data" is wrong as stated. What remains unclear is whether
that sheet derives from the same BSRIA report or a separate test — worth establishing, but the data is not absent.

## The new site: structure without content

**The architecture is right, and much fuller than the old one:** The System, Products, **all four Services**,
Start Your Project, About, Contact, and a **Knowledge Base with eight pillars**. That is the shape S15 describes,
and it is a real advance.

**But the on-ramp layer is unwritten, and it shows in the most literal way possible:**

- **The homepage hero is still the Shopify theme placeholder** — *"Our signature product. Made with care and
  unconditionally loved by our customers, this signature bestseller exceeds all expectations."* That is default
  demo text, and it happens to be **word for word the thing C-ATS's own brand rules prohibit**: no manufactured
  superlatives, no "signature bestseller" filler.
- **The 3 Rs has disappeared from the homepage.** The old site led with it. The new one does not mention it, nor
  the 50 mm depth. That is a regression on the brand's single most important positioning device.
- **£0.00 on every item, publicly, with "Sale price / Regular price" labels.** Gating policy is right
  (C4, `../../group-strategy/commercial-model.md`) but the presentation reads as broken or free, which is worse than no price at all.
- **"Join our email list — get exclusive deals and early access to new products."** Consumer-retail register, and
  "exclusive deals" directly contradicts gated trade pricing.
- **The Room Selector is still in the navigation**, though the decision was to remove it because it cheapens the
  paid design service.
- **The nav leads with SKUs** — *"C-ATS-RES-CP — Resonance Control Panel"*. Products are named by the problem they
  solve; putting the code first inverts the naming convention that does the positioning work.
- **The product grid is alphabetical**, so four services and the marine edge case appear before the three panels.
  No editorial decision has been made about order.
- **Marine is over-elevated again** — a product entry at equal prominence plus a full Knowledge Base pillar, for
  what is a narrow compliance case.

## What the comparison actually proves

**The new site's placeholder text is not laziness — it is a missing source.** Nobody had written down what belongs
in a hero, so the theme default survived. Same for the disappearance of the 3 Rs: there was no canonical
definitional or on-ramp record to generate from, so a generated site produced generic copy in the right-shaped
slots.

**Which is the case for the product-data layer, demonstrated rather than argued** (`../../registers/record-schema.md`).
The fix is not "write better website copy." It is to fill **group 1 (what the product is)** and **group 2 (why to
buy it)** for the three panels, at which point the hero, the product pages and the store listings have a source to
inherit from. The old site has the depth; the new site has the shape; the schema supplies what connects them.

**And the strongest asset on either site is currently doing nothing.** A complete, public, third-party test report
is exactly what a doubting specifier wants and exactly what AI answer engines cite. It sits behind a nav item
called "Technical Information."
