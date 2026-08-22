# C-ATS web artefacts — one check, five findings

*2026-08-20. **This file replaces three longer ones** — `the-system-page-checked`, `the-site-is-an-output-correction`
and `the-shopify-mockup-checked` — which were **mostly me correcting my own reading** as Neil supplied each site in
turn. Neil, closing it out: **"that fucking store is just the mockup. We are going in circles here."*** **He is
right. The audit was one look's worth of work and became five files.** *What follows is what survived.*

## The four artefacts, so nobody conflates them again

| | What it is |
|---|---|
| `www.c-ats.co.uk` | **The live site.** *Unchanged ~5 years. Four products, **no services**, and **the full BSRIA report plus five coefficient sheets, ungated*** |
| `c-ats.myshopify.com` | **The mockup Neil was working on** — *what `PR-18` describes. Unfinished by design; **not evidence of anything*** |
| `cats-98x.pages.dev` | *An Astro build Neil was shown once. **Provenance unknown and not worth chasing further*** |
| `copy.md` | *This repo's own copy — **stale**: it still carries "shallower than anything comparable", which `Q63` bounded* |

## The five findings that matter

1. **⚠ A published article attaches "diffuser" to the Reflection Control Panel** — *a section headed **Diffusers**
   with the panel named inside, and a table row reading **"Diffuser / reflection control"**. The panel sentence
   itself correctly says *scatter*.* **`C5.15` forbids the word on the product; ISO 17497 makes it a claim we cannot
   support** — *and the record had already caught the legacy brochure doing this.* **`SIT-9`. The only rule violation
   found.**
2. **`N3`'s "two of thirteen are written down" is wrong.** *At least five answers are published — bond-or-screw,
   behind-fabric, why-the-figures-look-low, fire ratings, and a BSRIA/ISO 354 data article.* **`SIT-12`: check whether
   each published answer is *right*, because finding 1 proves one is not.**
3. **`DOC-8` is answerable from a document already published.** *The live technical page: **"3 materials in 8
   different configurations… BS EN ISO 354:2003"**, one commission, and the marine sheet shipped in the same April
   2023 batch. **Read `BSRIA-Final-Report-100241-1.pdf`.***
4. **`P7` is an offer** — *verification **is** an offer: listed as a service, alongside Isolation System and Isolation
   Verification. **`copy.md` said so all along.***

## The lesson, since it cost a whole afternoon

**Before recording anything as *"unpublished"* or *"the site says"*, name the artefact and fetch it.** *`PR-24`
already said the repo's notes about what is published are unreliable; this session then produced the same failure
three more times **while investigating it**.* **And a mockup is not evidence.** *Auditing an unfinished thing against
the guardrails generates findings that dissolve the moment someone says what it is.*
