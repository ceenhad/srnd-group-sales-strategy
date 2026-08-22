# DR-Q52 — decision request to cinema-tools: what is C-ATS's self-serve route, and what of the rules layer publishes

**This is not an ADR and does not pretend to be one.** An ADR is a record of a decision, numbered in the repo that
owns it. This is a **decision request** raised from the sales-strategy work, keyed to `../registers/questions.md`
**Q52**, for whoever owns `cinema-platform` to accept, reject or reshape.

> **Rewritten 2026-08-18 after Neil caught it citing superseded ADRs.** The first draft rested the "methodology is
> proprietary" half on `products/cinema-tools/docs/product/03-c-ats-partner-tool.md`, and cited ADR 043. **Both are
> dead.** 043 is superseded by 042. The partner-tool document is 24 May, framed throughout on **ADR 019** — which
> ADR 017 superseded on 13 August — and describes a **Level 2 surface that ADR 017 v2 decision 5 withdraws
> outright.** The question below is regrounded on the live ADRs and its shape changed as a result.

| Field | Value |
|---|---|
| ID | DR-Q52 (this repo's namespace) |
| Raised | 2026-08-18, from the C-ATS brand run; rewritten same day |
| Decision-maker | Neil |
| Goes to | `cinema-platform` → `products/cinema-tools/docs/decisions/` (scope `cinema-tools`) |
| Bears on | **ADR 017 v2** (accepted 2026-08-13) — *what Cinema Tools is and what is sold*. Adjacent: **ADR 042 v5** (accepted) — acoustic treatment sizing and placement |
| Likely form | *`cinema-platform`'s ADR 079 has them versioned rather than amended — **its rule, not ours**, and Neil has called that family of rules noise-generating (2026-08-20), so **it is his to drop there***. Probably **017 version 3**, since it turns on 017's own decisions 2, 5 and 6. **The owner's call, not this repo's.** |
| Status | raised — no decision made |

## What the live ADRs establish

*Read from the files on 2026-08-18, statuses verified rather than assumed.*

| ADR | Status | What it settles that bears on this |
|---|---|---|
| 017 v2 | accepted | **§1** engine depth is the IP. **§2** the monetised deliverable is the engines' output — reports and recipes, priced per project; tool access is outside the price list. **§4** Cinema Tools Pro is **internal tooling — no external user logs into it**. **§5** Level 2 / Cinema Tools Online is **withdrawn** — "not a paid design environment, not a thin entry surface". **§6** the surfaces are the **seven free Level 1 calculators** and Pro. **§9** the free calculators exist to put qualified people into the funnel |
| 042 v5 | accepted (supersedes 43, 47) | **§32** the treatment report is a schedule and a drawing set — it does not teach. **The teaching belongs in the Acoustic Design Report.** Two documents both explaining reverberation is how the shorter one explains it badly |
| 019 | superseded by 017 | The C-ATS partner tool's placement and framing. Do not build on it |
| 043 | superseded by 042 | The three-Rs objective model. Do not cite it |

**Consequence, and it is the substance of this request:** there is no self-serve design surface for a C-ATS
dealer, and ADR 017 withdrew the one that was planned. The route to *how many panels do I need* is currently
either an engine output priced per project, or a free Level 1 calculator, or the design service.

## The open question

`../brands/c-ats/positioning.md` §1 withdrew the no-public-calculator rule and put in its place: *"C-ATS
publishes worked examples showing how quantities are derived"* as **the self-serve route**, with a
reflection-point calculator named as a good candidate. That position is live in this repo and predates ADR 017 v2.

**ADR 017 has since withdrawn the design surface it implied.** So the brand's stated self-serve route has no
mechanism behind it, and the question is not the abstract one the first draft asked. It is:

**What is C-ATS's self-serve route for sizing, given Pro is internal and Level 2 is withdrawn?** Three
candidates, not exclusive:

| Option | What it is | Fits ADR 017 |
|---|---|---|
| A — a free Level 1 calculator | C-ATS sizing joins the seven, as a funnel surface | Directly: §6, §9 |
| B — worked examples as published content | No tool. Room, grade, box count, per-axis result, as articles — the Joppa reference is the first | Silent on it; this is a content decision, not a surface |
| C — neither; sizing stays a paid deliverable | The engine output is the product (§2); `positioning.md` §1 is what changes | Directly: §2 |

## And the sub-question that survives either way

**Whichever route is chosen, what of the rules layer may be said in public?** The design-rules document draws a
line in its own words — the rules *"deliver a good result with minimal effort"*, the engine *"deepens the
accuracy, it does not replace the rules"*.

| Proposed publishable | Proposed not |
|---|---|
| The design hierarchy and its ordering | ETC scoring weights; directivity and delay terms |
| Per-axis flatness in place of one overall RT60; the over-damping guard | The budget allocation formula |
| Surface-palette matching; the material-match check | The 11-layer placement algorithm |
| The wall-on-isolation-mounts LF hierarchy | Modal and boundary-impedance implementations |
| That reflections are triaged, not all treated | The material catalogue and its provenance |
| Install-type A/B effects | Anything sufficient to reproduce a design without the engine |
| Corner-straddle placement; the ceiling-corner height-axis lever | |
| The 1.44 m² box quantum | |
| Worked **results** — room, grade, box count, per-axis outcome | Worked **derivations** at algorithm level |

**The test:** a rule that changes how a competent integrator *thinks about a room* publishes. A rule that lets
software *reproduce our output* does not.

**Note it sits with ADR 042 §32**, which already places teaching in the Acoustic Design Report rather than the
schedule. This asks the same question one layer out: what teaches *in public*, before anyone is a customer.

## What is riding on it, in this repo

| | |
|---|---|
| `../brands/c-ats/positioning.md` §1 | Its self-serve commitment has no mechanism until this resolves |
| `../brands/c-ats/hooks.md` | Six candidate angles held; one more blocked on the route |
| `../brands/c-ats/pathway-resonance.md` | The sizing slot on all three doors |
| `../registers/premises.md` | PR-4, PR-10 |

## Residual risk, stated not solved

Published rules are copyable by competitors. The mitigation is the one ADR 017 §1 already relies on: the rules
without the engine, the measured catalogue and the accountability do not produce a defensible design.
