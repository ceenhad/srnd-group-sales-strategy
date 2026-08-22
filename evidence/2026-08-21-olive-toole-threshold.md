# The audibility threshold — Olive & Toole, found in Cinema Tools — 2026-08-21

**`KNW-14` answered.** *Neil pointed at it: **"look in the Cinema Tools repo for olive and toole audibility threshold.
It's used in the etc tests most obviously."*** *Read at
`products/cinema-tools/docs/validation/olive-toole-reflection-threshold.md` and
`engines/modal_analysis/reflection_threshold.py` — the validation reference and the implementation.*

**So "move them from audible to inaudible" is measured against published psychoacoustic research, not against our own
assertion.** *That is the thing the brand's strongest qualitative claim was missing.*

## The source and the criterion

**Sean E. Olive & Floyd E. Toole, *"The Detection of Reflections in Typical Rooms,"* J. Audio Eng. Soc. Vol. 37
No. 7/8, July/August 1989** *(presented at the 85th AES Convention, 1988).* **The paper is copyright and not committed;
the platform holds transcribed, figure-digitised values at ±1–3 dB — the paper's own listener standard deviation, three
expert listeners.**

**The threshold is the level of a single reflection relative to the direct sound at which it becomes just detectable.**

## The curve the engine grades against

*Operative for a cinema is the **normal-room** curve, because a cinema is reverberant. The anechoic curve is the
conservative bound. Baseline signal is a **transient**, which is the most revealing and therefore the conservative
choice.*

| Delay | Normal room *(operative)* | Anechoic *(bound)* |
|---|---|---|
| 2 ms | −5 dB | −5 dB |
| 5 ms | −10 dB | −10 dB |
| 10 ms | −12 dB | −15 dB |
| 20 ms | −13 dB | −20 dB |
| 40 ms | −13 dB | −25 dB |
| 80 ms | −14 dB | −29 dB |

**Below ~20 ms the two curves nearly agree; above it a real room is 20–30 dB more forgiving.** *So the early window is
where the work is, and it is the window that sets the image.*

**Two offsets.** *Direction: lateral 65° and ceiling 60° are the imaging-critical baseline at 0 dB; **a reflection from
the same direction as the direct is masked about 7 dB more**. Signal: transient is the baseline, **speech and music sit
about 10 dB higher** — less audible.*

**And the criterion is per reflection, per band:** *`audible = band level re direct > threshold(delay, direction)`, with
`priority = level − threshold` — so **the excess over the line sets how much reduction is required**. Scattering brings
the per-band level under the line, and the score is the final per-seat result.*

## The finding that is worth more than the threshold

> **The paper shows an ETC peak under-reports a reflection poorer in HF than the direct by about 20 dB** — and that is
> exactly the C-ATS case, because speaker directivity and boundary absorption roll the reflection's high frequencies
> off.

**So the metric most people would reach for — a peak off an energy-time curve — is wrong by roughly 20 dB in precisely
the situation that matters.** *That is the direct justification for judging per band rather than broadband, and it is
the platform's stated reason for the per-band criterion in ADR 043.*

**Three things this gives the brand, and none of them names a competitor.**

- **A citation instead of an assertion.** *"Inaudible" is a published, named curve — this is `Q100`'s "we can write the
  science" with a reference attached.*
- **A reason the near-zero absorption figures are the wrong measure, for the third time and finally the right one.**
  *The panel's job is to bring band levels under a line. **Excess over threshold is the measure; absorption is not.***
- **A technical position stated as a category fact rather than a comparison.** *A collapsed or peak metric
  under-reports by ~20 dB where the reflection is HF-poor. **True, sourced, and it says nothing about anybody's
  product** — which is the form `../CLAUDE.md` sanctions.*

## One question inside it, and the validation doc raises it itself

**Absolute threshold or image-shift threshold?** *The paper measures both: **absolute** is where a reflection becomes
just detectable; **image-shift** is where the auditory image just moves, and it is a few dB stricter. The validation
doc's own closing caveat: **"decide which the engine grades against (imaging is the more relevant for cinema; it is a
few dB stricter)."*** `KNW-18`.

*Also flagged there and worth carrying: **comb-filter colouration below ~1 ms is a separate mechanism**, not
discrete-reflection detection, and is handled separately.*

## Provenance caution

*The values are figure-digitised approximations from the paper's figures 2, 6 and 13, at ±1–3 dB. **Publishing a
specific dB figure inherits that tolerance**, so quote the curve's shape and the citation rather than a precise
number, or re-digitise first. The validation doc says exactly this.*
