# `DR-Q52` sorted on the gating test — `DEC-6`

*The test, Neil 2026-08-21 (`../../registers/questions.md` `Q90`): **"anything that sniffs of getting on the sales
ladder like reccomended layouts etc should be gated by login."** So the line is **does it advance the sale**, not **is
it technical**. `DR-Q52` belongs to `cinema-platform`, so this file sorts and flags; it does not close the request.*

**One thing to say first, because it changes how the list reads.** Applied honestly, the test puts the *strongest*
material on the public side. The items that most build credibility are the ones that argue against buying panels — and
those are product knowledge, not sales ladder.

## Publishes

| Item | Why it passes the test |
|---|---|
| **Per-axis RT60** — one overall figure hides an axis that is out of line; flatness across all three is the target | A statement about how rooms behave. Recommends no purchase. **Already live on the site** |
| **The surface-mismatch principle** — a carpet floor under a plasterboard ceiling cannot be balanced with panels; a wood perimeter walkway fixes it | **The clearest pass on the list, and `hooks.md` already rates it the best of the six.** It sends the reader to joinery instead of to us. Publishing it *costs* a sale, which is exactly why it is not sales-ladder material |
| **The low-frequency hierarchy** — for deep bass, build the wall right rather than buying traps; surface traps at 30 Hz cannot do what a compliant wall on isolation mounts does | Same shape. It tells a reader our panels are the wrong answer for a problem they were about to buy panels for |
| **Corner loading, corner-straddle placement, the ceiling-corner lever** | Where a panel goes once chosen. Product fact. Already live |
| **Checkerboarding toward the rear** | Intended use of a product already selected. Already live |
| **The 1.44 m² box quantum** | How the product is packaged and sold. Nobody can buy without it |

## Gates behind a login

| Item | Why it fails the test |
|---|---|
| **The five-step design hierarchy** | It is the method that produces a specification. This is the sales ladder itself |
| **The budget formula** | Converts a room into a spend |
| **The surface-palette rules**, as the operational table rather than the principle | The principle publishes (above); the table is an instruction for producing a layout |
| **The Joppa Road worked example** — 7.05 × 4.95 × 2.6 m, 7.1.4, Gold on carpet = 11 boxes, REF 6 + REV 1 + RES 4, per-axis 0.35 / 0.20 / 0.11 | A recommended layout with quantities against a real room. Neil's own example of what gates |
| **Any calculator or selector output** | By definition a recommended layout — and it has to exist before it can be gated (`DOC-37`) |

## The conclusion worth more than the sort

**The gated tier is the registration incentive, and registration is the group's weakest gateway.**

`JNY-1` measured the funnel for the first time on 2026-08-20: `G3` 6, `G4` 35. **Thirty-five customers have ordered and
six gave marketing permission** — so registration earns nothing today and the finding was that either the gate closes
or the claim softens. This sort supplies the third option. Worked examples against real rooms, the design hierarchy and
the budget formula are exactly what a specifier would register to reach, and they are already written, in
`cinema-platform`'s design-rules document, captured with Neil in 2026-06.

**Nothing has to be built. It has to be placed on the right side of a login.**

## What this un-gates immediately

- **`T4`** — *where a low-frequency absorber goes, and why a corner* — was gated on `DR-Q52`. Corner-straddle placement
  and the ceiling-corner lever are product fact on this test, so **`T4` is runnable**.
- **Three of the six blocked hooks** in `hooks.md` — per-axis flatness, the surface mismatch, the LF hierarchy — are on
  the publishable side and can be cast.
- **`Q59`'s promise is half repairable.** *"Specify from the documentation yourself"* was marked aspiration because
  there is no self-serve sizing route and ADR 017 v2 cancelled the one that was planned. On this test the *principles*
  publish, so a reader can genuinely self-serve **diagnosis and placement** while **quantity** stays gated. That is a
  narrower promise than §3 makes and it is true, which is the difference the mark was recording.

## What this repo does not decide

`DR-Q52` is `cinema-platform`'s to close, and the design-rules document is theirs. **This file is a sort against an
owner's stated test, to be handed over** — not a decision taken here. The one thing it asserts is that the test now
exists, and that it was not available when `DR-Q52` was raised.
