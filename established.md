# Established

**Facts that are settled and sourced.** *The layer between `evidence/` — where a thing was read — and the documents
that use it. A fact enters here when it has a **named source** and something **rests on it**; it leaves only by being
superseded, and then it is replaced rather than annotated.*

## What belongs here, and what does not

| File | Holds |
|---|---|
| **`established.md`** | **Settled facts with a source.** *What is true, how we know, what rests on it* |
| `decided.md` | **Decisions the business acts on.** *Choices, not facts* |
| `registers/questions.md` | **The act of asking and answering.** *The record of how a thing came to be settled* |
| `registers/premises.md` | **Assumptions still carrying weight, with falsifiers.** *Things that could turn out false* |
| `evidence/` | **Dated reads of primary sources.** *The raw material a fact is drawn from* |

Every entry carries the same three fields under its statement: `basis` — measured, calculated, documented or
owner-stated · `source` · `rests on`.

---

## C-ATS — the range

### E-01 · The panels are 50 mm, 50 mm and 43 mm

`basis` owner-stated, corroborated twice · `source` Neil `Q63`, `Q82`; and his own 2021 statement to a test lab,
which gives the resonance panel as 600 × 600 × 43 mm two years earlier
· `rests on` The whole depth argument; the floorspace case; every datasheet figure.

*BSRIA's Table 1 records the resonance panel at 50 mm. That is a nominal logged at test, not a different article
(`Q82`) — 40 mm of foam plus a 3 mm face rounds to it.*

### E-02 · Every panel is a different construction

`basis` owner-stated · `source` Neil `Q82`, `Q83`; the locked performance record
· `rests on` The three-mechanism argument; the fire position; what may be said about any one panel.

*Reverberation: a single 50 mm acoustic foam. Reflection: a 3 mm injection-moulded flame-retardant polymer with relief
out to 50 mm — **not a 50 mm solid**. Resonance: 3 mm acrylic bonded to 40 mm foam, a pressure-driven membrane.
Marine: hand made in 3 mm solid-surface material, press-moulded to the standard panel's profile.*
**Material and supplier names stay internal — `decided.md` `D-06`.**

### E-03 · The reverberation foam is 85 kg/m³ — roughly 3.5× standard acoustic foam

`basis` owner-stated · `source` Neil `Q85`. *The reseller's page says 23.5–25.5 kg/m³ and is wrong; the
manufacturer's own 2021 datasheet records 94.7 kg/m³ as a thermal-test sample condition*
· `rests on` Why that panel performs as it does at 50 mm; the density-not-depth mechanism.

### E-04 · A foam's lab figures are its installed figures; a reflection panel's are not

`basis` documented · `source` The locked performance record
· `rests on` The mounting caveat, which applies per panel rather than across the range.

*A foam has a rigid backing whether it lies on a chamber floor or is stuck to a wall. The reflection panel is the one
where fixing changes the result, because bonding damps the panel itself.*

## C-ATS — measured performance

### E-05 · The resonance panel returns more absorption than its own area at 125 Hz

`basis` measured · `source` BSRIA 100241/1 via the locked record: **1.52 m² per box from 1.44 m² of coverage**
· `rests on` The single strongest low-frequency claim in the range. Self-contained — it needs no comparative.

### E-06 · The resonance and reverberation panels cross at 400–500 Hz

`basis` measured · `source` The locked record. Resonance falls with frequency, reverberation rises
· `rests on` The full-range claim, and the system-is-the-product argument. **The crossing is what makes a
full-range result out of two 50 mm devices, and it is invisible in any single table.**

### E-07 · Corner placement more than doubles the resonance panel at low frequency, and the loading reverses across the band

`basis` measured · `source` BSRIA Tests 3, 5 and 4 via the locked record
· `rests on` Corner placement being non-negotiable; the `T4` training subject.

*Per panel, as bounding planes are added: **×1.00 → ×1.89 → ×2.55 at 125 Hz**, and **×1.00 → ×0.71 → ×0.60 at 2 kHz** —
the plate loads up while the exposed foam edge band is shadowed. BSRIA records the corner configuration as ours rather
than the standard's.*

### E-08 · The resonance panel's tuning is calculable and lands where the measurement does

`basis` calculated, correlated with measurement · `source` The locked record: `f₀ = K/√(m·d)`, **134 Hz calculated**
against a **measured peak at 125 Hz** with a notch immediately above it at 160 Hz
· `rests on` *A notch above a peak is the resonance signature.* And a capability nothing else claims: **because f₀
scales as 1/√(m·d), a variant is predictable without a new test.**

### E-09 · A coefficient above 1.0 cannot be applied across a wall

`basis` documented · `source` BSRIA's own note, and the locked record: the samples were **1.44 m² against the
10–12 m² the standard asks for**
· `rests on` Which figure a design uses. *The reverberation panel reads 1.09–1.18 from 1–4 kHz; that is
edge-inflated. **Per-object figures are what a spaced layout should be sized on.***

### E-10 · The bonded install condition — the default — has no lab measurement behind it

`basis` documented · `source` The locked record and `panels.json`. *BSRIA tested only unfixed panels; the bonded
figures come from the legacy CATS Calculator*
· `rests on` The honesty caveat beside any bonded number. **It is the range's default install and its one
unmeasured performance figure.**

## Acoustics — the method's own limits

### E-11 · 100 Hz is the floor of reverberation-room testing, not a gap in our data

`basis` calculated from the method · `source` `Q96`, the locked record. *A 210 m³ chamber is a diffuse field only
above roughly 300–400 Hz; reaching 100 Hz needs ~3,200 m³ (15×) and 30 Hz needs 170×*
· `rests on` Why "full range" is design intent below 100 Hz and must not carry data — and why **in-situ
verification is the only evidence route down there**, which makes it load-bearing rather than reassurance.

*Neil: "It's simply not possible to measure panels below 100 Hz — it would need a nuclear bunker sized reverb
chamber." And below that region the critical in-room factor is subwoofer placement, not absorption.*

### E-12 · Sabine coefficients are band-limited and diffuse-field averaged — for everyone

`basis` documented · `source` `Q96`. A diffuse-field energy average says nothing about angle of incidence
· `rests on` A reason not to over-rely on coefficients. **Not a defect in ours** — it is the same limitation behind
every published figure in the category. *BSRIA's tables are third-octave across eighteen bands, better granularity than
most published summaries.*

### E-13 · Audibility has a published threshold: Olive & Toole, 1989

`basis` documented · `source` *"The Detection of Reflections in Typical Rooms,"* J. Audio Eng. Soc. Vol. 37
No. 7/8, via Cinema Tools' validation reference
· `rests on` **The reflection panel's entire performance claim.** *"Audible to inaudible" is measured against
published research rather than asserted.*

*The level of a single reflection relative to direct at which it becomes just detectable. Normal-room curve is operative
for a cinema: **−5 dB at 2 ms, to about −13 dB by 20 ms and flat above.** Offsets for direction and signal; judged per
reflection and per band, the excess over the line setting the required reduction. **Values are figure-digitised at
±1–3 dB — quote the curve's shape and the citation, not a precise number.***

### E-14 · An energy-time-curve peak under-reports an HF-poor reflection by about 20 dB

`basis` documented · `source` The same paper
· `rests on` **The sharpest technical statement available to the brand, and it names nobody.** *Speaker directivity
and boundary absorption roll a reflection's high frequencies off — so the metric most people would reach for is wrong by
~20 dB in exactly the situation that matters. It is the reason the judgement is made per band.*

### E-15 · A phase diffuser's reach and its depth are the same axis; an array's is not

`basis` calculated from the method · `source` Cinema Tools, recorded in `cinema-platform` ADR 092 §6 (`Q98`)
· `rests on` Why the low-frequency reach comes from the layout rather than the panel — and the aperiodic
requirement surviving the move away from claiming diffusion.

***Wells 50 mm deep reach 1,715 Hz; reaching 143 Hz needs 600 mm; our build-out reaching 143 Hz is 50 mm. Twelve
times.*** *An octave lower means twice as deep for a phase device. **The array reaches by spatial scale, which costs
surface area instead.** Measured on the two candidate layouts, the aperiodic one distributes across uniformity 0.66
against a checkerboard's 0.21.*

## The business

### E-16 · The legal entity is Cinema Acoustic Treatment Systems Ltd

`basis` documented by a third party · `source` BSRIA 100241/1 — client named on every page header, 272 Bath Street,
Glasgow, G2 4JR
· `rests on` Contracts, certificates and test reports. **Copy uses "Complete" instead — `decided.md` `D-11`, and
the divergence is deliberate.**

### E-17 · Seven of the thirteen questions we know we get asked have a written answer

`basis` documented · `source` `evidence/2026-08-21-c-ats-knowledge-base-read.md` — all eighteen articles read
against `N3`
· `rests on` The content plan's priorities. *The record said two. **Two it credited have none** — the warm-room
adhesive rule is in no article, and "can it be painted" was recorded as unanswered when the concealment article answers
it.*

### E-18 · Registration earns nothing today: 35 customers have ordered, 6 gave marketing permission

`basis` measured · `source` `evidence/2026-08-20-gateway-instrumentation.md` — engine, `G3` 6 · `G4` 35 · `G6` 2
· `rests on` Whether the registration gate closes or the claim softens — and the case for putting the gated tier
behind it, since worked examples are what a specifier would register to reach.
