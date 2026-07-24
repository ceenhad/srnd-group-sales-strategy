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

- **"Complete Acoustic Treatment System"** used as canonical, but brand truth flags the "Complete"
  expansion as unresolved (legal name "Cinema Acoustic Treatment Systems"). Use the form **C-ATS**.
- **"maximum performance" / "unique"** — the unbacked superlatives brand truth says to avoid.
- The `about.html` "recommended retail price" line contradicts the gated-pricing policy.

## Note

C-ATS is the **most content-mature** brand by far. The coherence job here is mostly **deploy +
reconcile + connect to the group story**, not create — the opposite of the thin brands.
