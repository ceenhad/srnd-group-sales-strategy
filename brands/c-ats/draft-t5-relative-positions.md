# Draft — `T5`: why the relative positions matter

**Leg 4, row `T5` (`training.md`), rewritten from the opposite of what it used to say.** *The old subject was
*"installing forgivingly"* — panels may move ~±300 mm without material effect. Neil struck it on 2026-08-21
(`../../registers/questions.md` `Q102`, `Q103`): the aperiodic layout's advantage comes from the panels being where
the sequence puts them.*

**A draft for correction.** *Audience: the integrator, on site. Runnable as our own class today.*

---

## Why am I here, and what will I learn

*The learning-objectives frame the CPD routes ask for.*

You will leave knowing **what the panel layout is actually doing**, why a neater-looking arrangement performs worse,
and the one rule that keeps a good design good through the install.

**And you will leave with a correction, if you have worked with these panels before.** The old guidance said the layout
tolerated being approximate. It doesn't any more, and the reason it doesn't is that the layout got better.

---

## 1. The layout is doing work, not just holding panels

A reflection panel does not absorb. Its job is to take one loud, early reflection and break it into many smaller,
later ones — until each of them drops below the level at which a listener can hear it as a separate arrival.

**That threshold is published, not our opinion.** It comes from Olive and Toole's 1989 AES paper on detecting
reflections in real rooms: a reflection has to be a certain level below the direct sound to go unnoticed, and **how far
below depends on how late it arrives.** Around 2 ms it only needs to be about 5 dB down. By 20 ms it needs about 13 dB.
The design grades every loudspeaker-to-seat bounce against that curve.

**So the target is a threshold, not a coverage percentage.** That is why the panel's absorption figures look
unimpressive and why that is beside the point — it isn't absorbing.

---

## 2. The pattern is where the low-frequency reach comes from

**This is the part worth understanding, because it explains everything about the install.**

A phase-based diffuser — the classic well-and-fin type — scatters by making sound take different path lengths down
different wells. Its reach and its depth are the same thing: **wells 50 mm deep work down to about 1,715 Hz, and to
reach an octave lower you need twice the depth.** To get down to about 143 Hz you would need wells 600 mm deep.

**Our build-out for the same reach is 50 mm.** Twelve times shallower — and it works because **the array reaches by
spatial scale rather than by depth.** The distances between panels are what set how low the break-up works.

Which is the whole point: **the spacing is the mechanism.** Move a panel on its own and you have not moved a panel —
you have changed the spacings around it, and the pattern loses the scales it was reaching with.

**Why the arrangement looks odd, and must.** A regular arrangement — a neat grid, a clean checkerboard — puts all its
energy at one scale. The layout you are given is deliberately irregular so that it works across many. *Measured on
the two candidate patterns, the irregular one spreads across three times as many scales as a checkerboard.* **A tidier
layout is a more regular one, and regularity is the thing the design is avoiding.**

---

## 3. What that means with a tape measure in your hand

**It does not need laser accuracy.** Nobody is asking for millimetres.

**What it needs is the relationships kept.** Three rules:

1. **Set out from the drawing**, not by eye and not from the last panel you fixed.
2. **If something has to shift, shift the run** — move the group together and the pattern survives. Move one panel out
   of a group and it doesn't.
3. **Do not substitute your own arrangement**, however much better it looks. If the layout cannot be built as drawn,
   that is a coordination item to raise, not a judgement call to make on the wall.

**And one exception that runs the other way:** the resonance panels go in the corners, and that is not negotiable at
all. Corner loading is the entire mechanism — measured, a resonance panel in a corner delivers more than twice what
the same panel does out in the room at low frequency. A resonance panel moved out of a corner is not a weaker
resonance panel; it is close to not being one.

---

## 4. Why this is good news, not a constraint

The old story was that the layout was forgiving, and it was told as the dealer's advantage: install approximately, get
the result.

**It was quietly arguing that the design wasn't worth paying for.**

The truth is better for everyone. The layout is computed for the room, the loudspeakers and the seats, and the pattern
is doing work no eye can reproduce. **Following it is what buys the result — which is exactly why it is designed rather
than estimated**, and why "just spread them evenly" was never going to get there.

---

## Discussion

**"When did you last change a layout on site, and why?"** *Every honest answer is something the design should have
anticipated: a keep-out nobody drew, a services clash, a finish that arrived different. **That list is worth more to us
than the seminar** — it is the set of things the design has to be told about earlier.*

---

## Confirmations before this runs

| Claim | Source | State |
|---|---|---|
| The panel splits one arrival into many, graded on audibility | Neil, `Q95` | **Owner's words** |
| Olive & Toole 1989; the threshold curve and its shape | `../../evidence/2026-08-21-olive-toole-threshold.md`, `Q104` | Recorded. **Values are figure-digitised at ±1–3 dB — the piece states the shape and cites the paper, and quotes no precise figure as ours** |
| 50 mm wells reach 1,715 Hz; 600 mm to reach 143 Hz; our 50 mm | Cinema Tools, recorded in `cinema-platform` ADR 092 §6 (`Q98`) | Recorded. *This repo has not read the ADR* |
| The array reaches by spatial scale, which costs area not depth | `Q98` | **Owner's statement** |
| The irregular pattern spreads across more scales than a checkerboard | `Q97`, the locked performance record | Recorded — **stated as a ratio, not a metric name**, since the metric is the platform's |
| Not laser accuracy; relative positions matter | Neil, `Q103` | **Owner's words** |
| Corner loading more than doubles the low-frequency result | BSRIA Table 4 via the locked record: 0.150 → 0.383 m²/panel at 125 Hz | **Measured** |

**Absent by design:** *no quantities, no coverage percentages, no material names, no densities, no competitor. Quantity
is gated (`gating-sort.md`); material identity never travels (`Q85`).*

## The one thing to check

**Is the 12× reach comparison sanctioned for an integrator audience?** *`the-depth-argument.md` §6 puts class-against-class
comparison on the public side, and this is a comparison against a **design method** rather than a product. But it is the
sharpest line in the piece, and it is the one a competitor would hear about.*
