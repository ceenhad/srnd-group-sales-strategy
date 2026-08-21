# The 18 C-ATS knowledge-base articles, read — 2026-08-21

`SIT-12`. All eighteen articles read against `N3`'s thirteen questions and against `claims.md`, plus the tool one of
them links to. All dated 7 June 2026, on `c-ats.myshopify.com`, in eight categories.

**One thing to fix in how this is described.** The live site, `c-ats.co.uk`, has four pages: home, products, technical
information, contact. **It has no knowledge base.** So these articles are written, not published — the 2026-08-20
check called them published, and that was the same artefact confusion the check itself warned about.

## The `N3` tally is wrong in both directions

`N3` says two of thirteen are written down. Seven have a written answer, and two the record credits do not.

| # | Question | Record said | Actually |
|---|---|---|---|
| 1 | Bond or screw? | `answered`, unpublished | **Written**, with both figures: bonded α ≈ 0.28 at 500 Hz, screw-only α ≈ 0.54. `DOC-1`'s "unpublished" is stale |
| 2 | How far off position is acceptable? | `known`, drafted | **Absent.** Checked in the three articles where it would sit. `draft-t5` stands |
| 3 | Behind fabric? | `known`, drafted | **Written**, and correctly: any cover must be acoustically transparent. But it stops short — see below |
| 4 | Why do the figures look low? | `known`, drafted, `DOC-4` blocks the values | **Absent.** The coefficient-table article explains values above 1.0 and that mounting matters; it never explains a scatterer's low figures. And `DOC-4` does not block the values — they are all published |
| 5 | How many, and where? | `known`, gap is publication | **Where is written; how many is not.** The article hands quantity to a tool that does not work |
| 6 | Replaces bass traps? | `unanswered` | **Written**: "Not thin ones. Low frequencies need dedicated, corner-loaded resonance control, not standard wall panels" |
| 7 | Why bigger than the others? | `known`, drafted | **Absent.** No article compares panel dimensions |
| 8 | Anywhere other than a corner? | `known`, drafted | **Absent.** "Corner-loaded" is stated; the weakness away from a corner is not |
| 9 | How much coverage? | `unanswered` | **Absent**, same gap as 5 |
| 10 | Checkerboard or continuous? | `known`, drafted | **Written**: side walls are "mirror images, often in a checkerboard pattern" |
| 11 | Will the adhesive hold? | `answered` | **Absent.** The warm-room rule is in no article. The mounting piece covers mechanism, not failure |
| 12 | Fire rated? | `known`, partly | **Written, and handled well.** See below |
| 13 | Painted or covered? | `unanswered`, "nobody has answered this" | **Answered in effect** by the conceal article: any cover must be acoustically transparent |

## `draft-answers.md` was not waste, and I recorded that it was

Three of its five answers are absent from the knowledge base — rows 4, 7 and 8. Row 10 is written. Row 3 is written
but without `N6`'s consequence, which is the commercially useful half. So one of five is redundant, not five of five.

**And `T2`'s subject is absent from all eighteen articles.** Deciding treatment before the wall is built does not
appear in the specification-mistakes article or the concealment article, the two places it would naturally sit. The
seven mistakes named are soundproofing-versus-treatment, ignoring bass, over-damping, forgetting the height axis,
treating the sides unequally, specifying treatment too deep, and overlooking the finish's fire rating — no sequencing.
`draft-t2` is the gap, not a duplicate.

## Five things to fix, in order of exposure

1. **`SIT-9` is three placements, not two.** The heading "Diffusers", the table row "Diffuser / reflection control",
   and a third in the FAQ: "diffusers/reflection control preserve a sense of space and protect imaging" — which pairs
   the two terms as synonyms. The panel sentence itself is correct and says scatter.
2. **The coefficients are published without their mounting condition.** The data article carries all three panels'
   full tables. The condition the record insists must travel with them — free, unfixed, edges exposed, confirmed in
   the BSRIA report itself — is in a different article, as a general remark that "results depend on how the sample was
   fixed". `Q46` is not met by that. One sentence added to the data article closes it.
3. **RT60 targets are published with no attribution.** Four ranges as "typical targets": 0.3–0.5 s for a dedicated
   cinema and for critical listening, 0.4–0.6 s for a multi-purpose media room, 0.2–0.4 s for a control room. No
   standard named. They are conventional ranges, but on our own page unattributed they are our claim. Either
   attribute them or state them as C-ATS design targets.
4. **An article promises a working tool that does not work.** "The free Room Selector turns your room dimensions and
   speaker layout into a suggested package and layout in seconds." `/pages/acoustic-selector` has a headline and no
   inputs, no outputs, no gate. This is `CLAUDE.md`'s build-it-then-say-it, a fourth independent instance. It also
   means `DR-Q52` is **not** answered by publication on quantity: placement and per-axis targets are live, sizing is
   not, and the thing that would output sizing is a shell.
5. **43 mm appears nowhere in eighteen articles.** Every one says the system is 50 mm. That is defensible as the
   system's deepest point, so it is not an error — but the resonance panel's 43 mm is, in Neil's words, a key design
   goal and the range's most remarkable result, and it is absent from all the content that argues about depth.

## Three things the articles get right, and one is better than the record

- **Fire is handled properly.** One product claim only — "the C-ATS Reverberation Control Panel uses a Class O
  acoustic foam core" — and then: "because fire performance can depend on the exact material, finish and build-up,
  confirm the current certificate for your specific specification rather than relying on a general class." No
  invented classification, and the finish is named as part of the assembly. `T1`'s explanation is written; only the
  current EN 13501-1 number is still missing (`DAT-3`/`DOC-7`).
- **No supplier is named anywhere**, and no competitor. The construction disclosed is "a Class O acoustic-foam core
  for the Reverberation panel, and thermoformed solid-surface panels for Reflection and Resonance control."
- **The group play is already running in the content**, unplanned: "we work alongside FabricWalls, a dedicated fabric
  wall system that delivers the finished face while the C-ATS treatment performs behind it." A C-ATS article
  cross-selling a sister brand is the thesis working. It writes the name as one word; the group's brand is Fabric
  Walls.

## And `DOC-32` is sharpened by our own content, twice

The data article states outright: "The Marine and Isolation products were not included in this report." The marine
article states: "Standard C-ATS panels are *not* constructed from IMO/SOLAS-compliant materials", and describes the
marine panel as a thermoformed solid-surface panel built to marine fire-resistance requirements.

So the marine panel is a different material from the standard panel. A different material has different absorption.
**The published marine coefficient sheet therefore cannot be REF-CP figures re-badged** — which was one of the two
answers `DOC-32` offered. Either a test exists that this repo has never seen, or the sheet is unsupportable. The
marine article itself cites no data and links no report, which is the right restraint.
