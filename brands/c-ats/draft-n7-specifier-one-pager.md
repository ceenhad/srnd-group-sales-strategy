# Draft — `N7`: the one-pager a dealer hands the specifier

**`KNW-5`/`KNW-11`. Replaces `draft-n7-client-leave-behind.md`, which was written for the wrong reader.** *Neil,
2026-08-21 (`../../registers/questions.md` `Q76`): **"This would be a dealer to specifier and should be C-ATS branded.
its not B2C just a different stage of B2B."** So the reader is the architect, interior designer or AV consultant; the
moment is specification stage, not handover; the voice is the trade voice; and it carries technical substance the first
draft deliberately stripped out.*

**Reader test.** *This lands on the desk of someone drawing a room. It has to earn its page in the ten seconds before
they decide it is a brochure.*

**It sits with `T2`, not against it.** *`T2` — deciding acoustics before the wall is built — is the seminar for this
same reader. **This is the page they keep afterwards**, or the page that reaches the ones who never attend. Where they
overlap, this one states and `T2` argues.*

---

## The piece

### Draft title: **The acoustic layer: what to allow for, and when**

**A room like this has an acoustic layer, and it is concealed.** It sits behind the stretch-fabric wall and ceiling
system, so by the time the room is finished there is nothing to see. That has one consequence that matters more than
any other on your drawings: **it is decided with the wall, not added to it.**

---

### 1. The treatment decides how deep your wall build-up is

The panels sit in the cavity between the structural wall and the fabric wall. **The depth of that cavity is set by the
acoustic treatment**, not by the fabric system — so this is the number that decides how much of the room the wall
build-up takes.

Acoustic treatment is usually 100–200 mm deep, mostly for bass. **This system works at 50 mm.** On a 6.0 × 4.5 m room,
the difference between a 150 mm build-up and a 50 mm one is about **2 m² of floor** — and at this end of the market the
floor is worth considerably more per square metre than the treatment that consumed it.

**That is the whole reason the system was designed shallow.** It is not a spec detail; it is the dimension you are
being asked to give up, and we made it as small as we could.

**What we need from you is the cavity, not the panel layout.** Set the zone on the surfaces that will be treated and we
will work inside it. What we cannot do is recover depth from a room already dimensioned as though the acoustics were a
finish.

---

### 2. Three problems, three panels, and only one of them is fussy about position

- **Reflections.** Sound arriving off a hard surface a moment after the direct sound. Left alone it blurs detail and
  makes dialogue harder to follow. These panels **scatter** those reflections away from the seats rather than deadening
  the room. **The layout is computed, and the relative positions are what matter** — it does not need laser accuracy, but the pattern has to survive the install.
- **Resonance.** The uneven bass that makes one seat sound heavy and the next thin. **These go in the corners**, where
  that energy collects, and this is the one place where position is not negotiable. Corner loading is the whole
  mechanism.
- **Reverberation.** The room's overall decay. Too long and everything smears; too short and the room feels dead. This
  is a quantity question, and over-use is as real a failure as under-use.

**The reason this matters to a drawing:** corners are the constraint. If joinery, cabling or a subwoofer position takes
the room's corners, the resonance layer loses the only place it works.

---

### 3. Somebody has to design it, and it is usually nobody

On most projects the acoustic layer falls between three parties. **The acoustic consultant is engaged for sound
isolation** — the structure, the box, the dimensions — and the treatment inside the finished room is not what they were
appointed for. **The interior designer owns the surfaces** but not the acoustics behind them. **The integrator owns the
system** but rarely has the hours to spend on a treatment design.

So it goes unowned, and gets estimated late.

**It can be ours.** We design the treatment layer as a service, working from your room and the speaker layout, and the
output is a specification you can put in the drawings — quantities, positions and the depth to allow.

---

### 4. One rating you own, and it is not ours

Because the panels are concealed, **the surface the room actually presents is the fabric** — and the fabric carries its
own reaction-to-fire classification, specified with the fabric.

That is the one an inspector looks at. It is also the one most often left to whoever happens to be supplying the
finish. **Specify it deliberately, at the same time as you specify the fabric.**

The treatment behind it is still part of the construction and we will provide its classification against your
specification. But it is the second question, not the first — and knowing which order they come in saves a week late in
a programme.

---

### 5. It can be proved

Acoustics is usually the one part of a room nobody can see and nobody can demonstrate. **This part can be measured.**
The panels are independently tested to BS EN ISO 354, and the finished room can be verified against the design.

You do not have to take it on trust, and neither does your client.

---

### What to do with this page

**Bring the acoustic layer into the conversation at the stage you are fixing dimensions**, not at the stage you are
choosing finishes. Ask for the depth to allow, and ask who is designing it. If the answer to the second question is
nobody, that is the normal answer and it is the one worth fixing early.

---

## Traceability

| Claim | Source | State |
|---|---|---|
| Concealed behind the finish, so decided with the wall | `product-records.md` § Where they sit; `N6` | **`N6` is this repo's derivation** — the load-bearing one, and `Q75`/`Q77` support it without stating it |
| 50 mm against a conventional 100–200 mm | `product-records.md` § Depth; the published depth article | Recorded. *The system's deepest point is 50 mm; the resonance panel is 43 mm and the piece does not need per-panel figures* |
| ~2 m² on a 6.0 × 4.5 m room | The published depth article's own worked example | Recorded. **Deliberately no money figure** — the article carries £/sq ft and this page must not |
| Three problems, one panel each | shared § What they are; `claims.md` `C1.15`, `C1.20` | Confirmed — *"the 3 Rs is the design system"* (Neil, `Q70`) |
| Scatter, never diffusion | `claims.md` `C5.15` | Hard rule |
| **The layout is computed; relative positions matter, laser accuracy does not** | `Q102`, `Q103`; shared § Layout tolerance, struck | **Replaces the ~300 mm tolerance claim, struck 2026-08-21.** *Former note: traces to a 2015 brochure decode flagged "legacy, confirm current spec"** — `draft-t5` carries the same caveat, and the piece says "around" for that reason |
| Corner loading is the mechanism; position not negotiable | resonance record `O4`, `R1`; `claims.md` `C4.15` | Recorded, and un-gated 2026-08-21 (`gating-sort.md`) |
| Over-use dulls a room | reverberation record § Limits | Recorded |
| The three refusals | Neil, `Q77`; `claims.md` `C1.43`, `C1.44` | **Owner's words** |
| Design offered as a service | `CAT-06`; `Q89` — a single fee per room | Recorded. **No price on the page** |
| The fabric is the exposed surface and carries its own rating | `draft-t1-fire-evidence.md` §3, from the 2026-08-21 primary-source reads | **New today.** The strongest thing on this page for this reader |
| Tested to BS EN ISO 354; the room can be verified | shared § Test basis; `positioning.md` §4; `P7` — verification is a listed service | Recorded |

**Absent by design:** no price, no coefficient, no competitor, no material or supplier name, no per-panel dimensions,
no quantity guidance. *Quantity is sales-ladder material and gates (`Q90`, `gating-sort.md`), so a page that hands out
depth-to-allow but not quantities is on the right side of that line by construction.*

---

## Sourced, 2026-08-21

**The question this draft could not answer — whether the 50 mm sits inside the fabric system's build-up or adds to it —
is answered and it is neither** (`../../registers/questions.md` `Q92`). Neil: *"it sits betwen the structural wall and
the fabric wall. the depth is not driven by the fabrc system though, its driven by the acoustic treatment system which
is entirely the point of making it so shallow."*

*The first framing here was the weaker one: that we fit inside a zone the architect was giving up anyway. **The truth is
stronger** — the treatment sets the cavity, so the 50 mm is the architect's number directly, and minimum depth being a
design goal follows from that rather than being a boast about it.* §1 is rewritten accordingly.
