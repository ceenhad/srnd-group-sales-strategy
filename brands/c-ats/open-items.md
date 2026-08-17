# C-ATS — open items (brand-specific)

Group-level open items and sequencing live in `../../registers/open-items.md`. These are C-ATS's own.

**Decisions needed (flag, don't guess):**
- Consolidate the global C-ATS dealer list + finer buyer-truth from real jobs (who specified vs
  bought vs installed, and why) before hard-coding into copy.
- Lever-2 channel validation — which of pro install / commercial cinema / fit-out to pursue first,
  and each one's real buyer and proof needs.
- C-ATS partner pricing tiers — the numbers behind the shared gate (publication is settled group
  policy; tiers are not).
- Trading-name expansion: "Complete Acoustic Treatment System" vs the legal "Cinema Acoustic
  Treatment Systems." The live store hard-codes "Complete" on the brand page; brand `CLAUDE.md` says
  this is unresolved and must not be hard-coded. Reconcile — affects any tagline work.
- Commercial range launch timing — blocks any teaser content and gates lever 2's cinema channel.
- Public-safe case-study material from the NDA-constrained reference install(s) (stage-5 proof),
  built without naming the install.

**Site / execution (in the C-ATS site repo, `ceenhad/c-ats-shopify`):**
- Deploy corrected `about.html` (pricing line) on next content push.
- Launch: the public C-ATS site is a holding page; retiring it for the real site is its own gating
  step, best taken once the stage-1→4 operations exist.
- Pre-planned reference layouts (built, deploy previously blocked on Shopify CLI re-auth) — the
  "range in context" asset for stage 2.
