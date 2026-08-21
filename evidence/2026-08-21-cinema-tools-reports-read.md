# Two Cinema Tools reports, read — 2026-08-21

*Neil supplied `Acoustic Treatment Report` (12 pp) and `Acoustic Design Report` (46 pp), both **Galileo v3, issued
2026-08-19**, both outputs of Cinema Tools and both still being finalised: **"the reflection section is decent
already."** It is, and it settles the question this repo opened yesterday.*

**Read against `CLAUDE.md`'s standing instruction to check the platform before specifying anything that touches it.
Three things it settles, two it contradicts, one label that looks wrong.**

## `KNW-14` answered: "inaudible" has a definition and a number

*Opened hours earlier: `"audible to inaudible"` is a threshold claim, so below what?*

**A level- and delay-dependent audibility threshold, computed per reflection path.** The strength table's columns are
**TIME DIFF (ms) · LEVEL OFFSET (dB) · OVER THRESHOLD (dB)**, and the method states it plainly: *"each
first-order loudspeaker-to-seat reflection is traced to the surface it strikes and graded against a level- and
delay-dependent audibility threshold. Differences below that threshold are not carried into the schedule."*

The energy-time curve plots the threshold as a curve against delay, with a shaded window: *"a reflection is heard only
where it rises above the audibility threshold; those within **15 ms** of the direct (the shaded window) fuse with it
and set the image, later ones are reverberation."*

**And the counts are per room, not generic.** *789 reflections over threshold across every loudspeaker-to-seat path,
171 of them on the floor — which a panel cannot cover and the floor covering manages. At the reference seat, 77 over
threshold and 71 inside the early-reflection window.*

## The mechanism, stated better than anywhere in the brand folder

> *"The aim is to maximise the level offset and the time gap — a reflection panel does both, **breaking one large
> reflection into many smaller, later ones**, which increases clarity and spaciousness at once."*

**That is Neil's "break up reflections and move them from audible to inaudible" expressed as a mechanism, and it is the
complete answer to why absorption is the wrong measure for this panel.** *The panel is not removing energy. It is
splitting one arrival into many, each lower and later, until each falls under the threshold curve. **A coefficient
cannot express that**, which is why the measured absorption is near zero and why that was never the weakness the record
read it as (`N3` question 4).*

**It also resolves the diffusion question without needing the word.** *`Q95`: not a mathematical diffusor, and the
concept has limited application in a small room. What replaces it is a stated aim — level offset and time gap — that
can be computed, is computed, and is reported per reflection.*

## The layout uses aperiodic sequences, which nothing in this repo knew

*Pattern selection per patch: **"4 chequerboard (patch too small for a sequence), 13 maximum-length-sequence
(aperiodic), 5 solid (single point or line)."***

**So the distribution is achieved at the layout level by an aperiodic sequence, not at the panel level by a
mathematical profile.** *That is a sharper and more defensible version of the position than "we scatter rather than
diffuse": the sequence family is the one the diffusor literature uses, applied to where panels go rather than to how a
panel is shaped.* **Nothing in the brand folder mentions it, and it is a strong technical proof point.**

## Two contradictions with this repo, and the first one matters

**1. `T5`'s layout tolerance may be wrong for the reflection panel — the piece whose whole subject it is.**

*`draft-t5-layout-tolerance.md` claims panels may move ~±300 mm from the designed position without material
performance impact, and excludes only the resonance panel. The treatment report's method says: **"a reflection panel
cannot relocate (it works only at its bounce point)"**, and that an unplaced panel is reported as a clash rather than
counted, because it absorbs nothing.*

**Panels are set out on a 300 mm lattice, so ~300 mm is exactly one cell** — which may mean the two statements are
compatible at fine positioning and incompatible at reallocation. *But `T5`'s figure traces to a **2015 brochure
decode** already flagged *"legacy, confirm current spec"*, and the tool is the live authority. **A training piece
whose entire subject is tolerance cannot rest on a claim the design tool contradicts.** `KNW-15`.*

**2. `N3` question 1's answer is validated, and the tool goes further.** *The design report specifies **"REF Type A,
adhesive-bonded (clean reflector, lower absorption)"** for reflection control. So bonding is not a preference — it is
what the mechanism requires, because you want a clean reflector rather than a partial absorber. That is the α 0.28
against 0.54 story with a reason attached, and the published article's "match it to the job" is right but understates
it.*

## One label that looks wrong

*Schedule note: **"One panel is 1.44 m²."** Panels are set out on a **300 mm lattice**, and 1.44 m² is sixteen 300 mm
cells — which is the **box** quantum this repo has recorded throughout. **It should almost certainly read "one box is
1.44 m²."*** A 143-panel allocation at 1.44 m² each would be 206 m² on a room whose five surfaces total under 80 m².
`ENG-28` — reported, not fixed here.

## What the reports show about the platform, and it is the fourth instance

**The design report's plain-language explanation of the three Rs is better than anything in the C-ATS brand folder.**

> *"Low-frequency sounds have very long wavelengths — up to 20 m in a cinema. Because they are so long, they are
> bounced back on themselves by the room boundaries, setting up standing waves."*

*And the analysis suite behind it is a credibility inventory the brand does not claim: Walker Room Criteria, Bonello
chart, Schroeder transition frequency, per-axis relative resonance strength, room response, bass headroom, bass system
architecture.* **`PR-20` again — the platform is ahead of this repo, and this time on writing rather than on data.**

**Two things that are marketing assets in their own right, because of what they refuse to do.**

- **The tool reports its own failure to hit target.** *"125 Hz sits at 0.44 s, above its upper limit of 0.42 s by 4%.
  The panel quantum cannot close it without taking an adjacent band past the opposite edge."*
- **It refuses to credit treatment it cannot place.** *"An unplaced panel absorbs nothing"* — 49 reflection points land
  on a keep-out and are reported as coordination clashes, with the acoustic requirement standing whether or not a panel
  could be seated.

*A design tool that tells you where it fell short is a stronger sales instrument than one that always reports success,
and neither behaviour is claimed anywhere in the brand's material.*
