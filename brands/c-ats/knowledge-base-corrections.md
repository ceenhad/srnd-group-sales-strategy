# Knowledge-base corrections — paste-ready copy

*Seven fixes found by `SIT-12` (`../../evidence/2026-08-21-c-ats-knowledge-base-read.md`) and by the primary-source
reads of the same day. **Replacement text, not instructions** — each one is written to be dropped in.*

**Where this belongs.** *The articles live on `c-ats.myshopify.com` and this repo cannot edit them. But the C-ATS site
that appeared on 2026-08-20 was generated from answers in this repo, so **the corrected text belongs here and the
generator picks it up**. Anything applied by hand to the store instead will be overwritten by the next generation.*

---

## 0. `SIT-13` — ⚠ URGENT: a live false claim on `c-ats.co.uk`

*`/technical-information/` states that **reflection panels tolerate roughly 300 mm from the designed position**. Struck
2026-08-21 (`Q102`): the aperiodic layout's advantage comes from the panels being where the sequence puts them, so
moving one breaks the sequence. **This is on the real site, not a mockup, and it is the only live false claim found.**
Take the sentence down first — the replacement can follow separately.*

**Replacement copy, from `Q103`:**

> **Setting out.** The layout is computed for your room, and **what matters is the relative positions rather than
> millimetre accuracy**. Panels work as a pattern: the spacing between them is doing the work, so the pattern has to
> survive the install.
>
> In practice that means three things. **Set out from the drawing** rather than by eye. **Keep the pattern** — if
> something has to shift, shift the run rather than one panel. And **do not substitute your own arrangement**, however
> reasonable it looks, because a tidier-looking layout is usually a more regular one, and regularity is the thing the
> design is avoiding.
>
> This is why the layout is worth designing rather than estimating.

*Why this is better copy than what it replaces, and worth saying to whoever applies it: the old line sold ease —
install approximately, get the result — which quietly argued that the design was not worth paying for. **The new line
says the opposite, and it is true.***

---

## 1. `SIT-9` — "diffuser" is on the product in three places

*The brand's hardest naming rule (`claims.md` `C5.15`): diffusion has a specific meaning under ISO 17497 that this
product does not claim. The sentence about the panel is already correct and says **scatter**; the heading, the table
and the FAQ are not.*

| Where | Now | Replace with |
|---|---|---|
| Article title | "Absorbers, diffusers and bass control" | **"Absorb, scatter, control the bass: the three tools a room needs"** |
| Section heading | "Diffusers" | **"Scattering"** |
| Comparison table, row label | "Diffuser / reflection control" | **"Scattering / reflection control"** |
| FAQ | "diffusers/reflection control preserve a sense of space and protect imaging" | **"Reflection control preserves a sense of space and protects imaging"** |

**And add this, which turns the fix into content** — *place it at the end of the Scattering section:*

> **A note on the word "diffusion".** You will see it used loosely for anything that is not an absorber. It has a
> specific meaning: a scattering coefficient measured to ISO 17497. We have not measured one, so we say what the panel
> does — it scatters early reflections rather than absorbing them — and leave the word alone. If a supplier claims
> diffusion, ask which standard and what the coefficient is.

*The URL handle contains "diffusers". **Retitle without changing the handle, or set a redirect** — a broken link is a
worse outcome than an imperfect slug.*

---

## 2. `DOC-34` — the construction sentence is wrong for two of three panels

*It reads: "A Class O acoustic-foam core for the Reverberation panel, and thermoformed solid-surface panels for
Reflection and Resonance control." Every panel uses a different material (Neil, `Q83`), and solid surface describes
the **marine** panel.*

> **Each panel is built from the material its job needs, and they are not the same.** The Reverberation panel is an
> acoustic foam core with a Class 0 classification. The Reflection panel is injection moulded. The Resonance panel is a
> laminate, and its rigid face is what makes it resonate rather than absorb. The marine variant is moulded to the same
> profile as the standard Reflection panel, in a material specified by Lloyd's Register.

**How much construction detail to publish is Neil's call, and this version deliberately stops at function.** *`Q85`:
material identity is margin. The version above is accurate, gives the Lloyd's credential, and names nothing — and
`CLAUDE.md`'s voice rule is problems solved, not mechanisms.*

---

## 3. `DOC-35` — the coefficient tables are published without their mounting condition

*`Q46` and the record both require the condition to travel with the figures. It currently sits in a different article
as a general remark. **Place this immediately above the tables**, in the BSRIA data article.*

> **How the samples were mounted, because it governs every figure below.** BSRIA tested the panels laid directly on the
> floor of the chamber, with no fixings between the tiles, and the sample edges left exposed. That is a free, unfixed
> condition, and it is the right one for a comparable laboratory measurement.
>
> **An installed panel is bonded or screw-fixed to a wall or ceiling, and that changes the result.** On the Reflection
> panel it changes it measurably: bonded gives roughly 0.28 at 500 Hz, screw-only roughly 0.54, because bonding damps
> the panel and lets it work as a clean reflector.
>
> **So read these as design-stage reference figures rather than installed performance — but the size of that gap is not
> the same for all three panels.** A foam has a rigid backing whether it lies on a chamber floor or is stuck to a wall,
> so for the reverberation panel the lab condition is effectively the installed one. It is the reflection panel where
> fixing changes the result, because bonding damps the panel itself.
>
> **One more caution on the numbers above 1.0.** A coefficient above 1 is a known effect of this test method, and these
> samples were 1.44 m² where the standard asks for 10–12 m². **It is not a figure you can apply across a whole wall** —
> it over-predicts a large installation, and a spaced layout should be sized on the per-panel figures instead.

---

## 4. `DOC-36` — four RT60 ranges are published as "typical targets" with no standard named

*They are conventional ranges, but unattributed on our own page they are our claim, and no unbacked claims is a house
rule. **Own them instead** — and it lets the piece pivot to the per-axis point, which `DEC-6` confirms publishes.*

> **These are the targets C-ATS designs to.** They are not quoted from a standard — no standard sets a single number
> for a private cinema — and other designers work to slightly different ranges. We publish ours so you can see what we
> are aiming at.
>
> *[keep the existing four ranges as they stand]*
>
> **What matters more than the number is that the three axes agree.** A room can hit 0.4 s overall while its height
> axis sits well outside that, and it will still sound wrong. One figure hides the axis that is out of line, which is
> why we set a target on each.

---

## 5. `DOC-33` — the marine coefficient figures need their basis stated

*No marine test exists and none is owed (`Q83`), but a shared dataset published in silence reads as a separate test.
**Add to the marine article, and to the coefficient sheet if it can be reissued.***

> **About these absorption figures.** The marine panel is moulded to the same profile as the standard Reflection
> Control Panel, and a reflection panel's job is to scatter early reflections rather than absorb them. The figures
> published here are the standard panel's bonded-condition data, which the identical geometry makes representative. It
> has not been separately tested in a reverberation chamber, and we would rather say so than let you assume otherwise.

---

## 6. `DOC-40` — the marine article says "IMO/SOLAS" where a surveyor needs two named tests

> **Marine work is signed off against Lloyd's Register requirements**, and the tests a lining has to satisfy are named:
> **IMO FTP Code Annex 1 Part 2** for smoke and toxicity, and **Annex 1 Part 5** for surface flammability.
>
> **"IMO/SOLAS compliant" is not a specification.** Ask for those two by name — for the material, in the build-up you
> are actually using. On a yacht project that one question saves weeks.

---

## 7. `DOC-37` — an article promises a tool that does not exist

*Current: "The free Room Selector turns your room dimensions and speaker layout into a suggested package and layout in
seconds." `/pages/acoustic-selector` has a headline and no inputs, no outputs. **Build it, then say it.***

**Replace the sentence with:**

> Getting the quantities right is a design step rather than a lookup, and it is the part we do for you. Tell us the
> room and the speaker layout and we will specify it.

*And remove the Room Selector from the navigation — already `EST-4`.*

**When the tool does exist, its output is gated.** *`DEC-6`: a suggested package and layout is a recommended layout,
which is Neil's own example of what sits behind a login (`Q90`).*
